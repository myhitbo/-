package org.shnayimmikra.app;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

/** Reçoit l'alarme d'un rappel, et le redémarrage du téléphone (les alarmes sont alors à reprogrammer). */
public class ReminderReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        if (intent != null && Reminders.ACTION.equals(intent.getAction())) Reminders.fire(context);
        else Reminders.schedule(context);
    }
}
