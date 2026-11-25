package org.shnayimmikra.app;

import android.Manifest;
import android.app.AlarmManager;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.os.Build;

import org.json.JSONArray;
import org.json.JSONObject;

/**
 * Rappels de lecture. L'app web calcule la liste des prochains rappels (heure, titre, texte) : elle connaît
 * le rythme choisi, la paracha, et saute Shabbat et les fêtes. Ici on garde cette liste, on programme
 * une alarme pour le prochain rappel et on affiche la notification le moment venu.
 */
final class Reminders {
    static final String ACTION = "org.shnayimmikra.app.RAPPEL";
    private static final String PREFS = "rappels", KEY = "liste", CHANNEL = "rappel";
    private static final long MAX_LATE_MS = 12L * 3600 * 1000;   // un rappel resté en attente plus de 12 h n'est plus affiché

    private Reminders() {}

    /** Remplace la liste des rappels (JSON : [{"at": ms, "title": "…", "text": "…"}]) et programme le prochain. */
    static void save(Context ctx, String json) {
        prefs(ctx).edit().putString(KEY, json == null ? "[]" : json).apply();
        schedule(ctx);
    }

    /** Programme une alarme pour le prochain rappel à venir, ou annule l'alarme s'il n'y en a plus. */
    static void schedule(Context ctx) {
        AlarmManager am = (AlarmManager) ctx.getSystemService(Context.ALARM_SERVICE);
        if (am == null) return;
        PendingIntent pi = PendingIntent.getBroadcast(ctx, 0, new Intent(ctx, ReminderReceiver.class).setAction(ACTION),
                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);
        long now = System.currentTimeMillis(), next = 0;
        try {
            JSONArray list = new JSONArray(prefs(ctx).getString(KEY, "[]"));
            for (int i = 0; i < list.length(); i++) {
                long at = list.getJSONObject(i).optLong("at");
                if (at > now - MAX_LATE_MS && (next == 0 || at < next)) next = at;
            }
        } catch (Exception e) { next = 0; }
        if (next == 0) { am.cancel(pi); return; }
        am.setAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, Math.max(next, now + 1000), pi);
    }

    /** Alarme reçue : affiche le rappel arrivé à échéance (le plus récent), l'enlève de la liste, programme le suivant. */
    static void fire(Context ctx) {
        long now = System.currentTimeMillis();
        JSONObject due = null;
        JSONArray rest = new JSONArray();
        try {
            JSONArray list = new JSONArray(prefs(ctx).getString(KEY, "[]"));
            for (int i = 0; i < list.length(); i++) {
                JSONObject r = list.getJSONObject(i);
                long at = r.optLong("at");
                if (at > now + 60000) { rest.put(r); continue; }
                if (at > now - MAX_LATE_MS && (due == null || at > due.optLong("at"))) due = r;
            }
        } catch (Exception e) { /* liste illisible : on repart de zéro */ }
        prefs(ctx).edit().putString(KEY, rest.toString()).apply();
        if (due != null) show(ctx, due.optString("title"), due.optString("text"));
        schedule(ctx);
    }

    /** Vrai si Android laisse l'app afficher des notifications. */
    static boolean allowed(Context ctx) {
        if (Build.VERSION.SDK_INT >= 33 && ctx.checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) return false;
        NotificationManager nm = (NotificationManager) ctx.getSystemService(Context.NOTIFICATION_SERVICE);
        return nm != null && nm.areNotificationsEnabled();
    }

    private static void show(Context ctx, String title, String text) {
        NotificationManager nm = (NotificationManager) ctx.getSystemService(Context.NOTIFICATION_SERVICE);
        if (nm == null || !allowed(ctx)) return;
        Notification.Builder b;
        if (Build.VERSION.SDK_INT >= 26) {
            nm.createNotificationChannel(new NotificationChannel(CHANNEL, ctx.getString(R.string.channel_reminder), NotificationManager.IMPORTANCE_DEFAULT));
            b = new Notification.Builder(ctx, CHANNEL);
        } else {
            b = new Notification.Builder(ctx);
        }
        PendingIntent open = PendingIntent.getActivity(ctx, 1,
                new Intent(ctx, MainActivity.class).addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP),
                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);
        b.setSmallIcon(R.drawable.ic_stat).setContentTitle(title).setContentText(text)
                .setStyle(new Notification.BigTextStyle().bigText(text))
                .setAutoCancel(true).setContentIntent(open);
        nm.notify(1, b.build());
    }

    private static SharedPreferences prefs(Context ctx) { return ctx.getSharedPreferences(PREFS, Context.MODE_PRIVATE); }
}
