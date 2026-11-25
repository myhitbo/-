package org.shnayimmikra.app;

import android.Manifest;
import android.app.Activity;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.print.PrintManager;
import android.view.View;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import android.webkit.JavascriptInterface;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;

/**
 * Affiche l'application web embarquée (assets/www).
 * Les liens vers des sites s'ouvrent dans le navigateur du téléphone ; les rappels sont confiés à {@link Reminders}.
 */
public class MainActivity extends Activity {
    private static final int ASK_NOTIFICATIONS = 1;
    private WebView web;
    private FrameLayout root;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        web = new WebView(this);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setAllowFileAccess(true);
        s.setTextZoom(100);
        web.setWebViewClient(new WebViewClient() {
            @Override public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                Uri u = request.getUrl();
                if ("file".equals(u.getScheme())) return false;   // pages de l'app
                openExternal(u.toString());
                return true;
            }
        });
        web.addJavascriptInterface(new Bridge(), "SMAndroid");
        web.setOverScrollMode(WebView.OVER_SCROLL_NEVER);

        /* Depuis Android 15, l'app s'étend sous la barre d'état et la barre de navigation.
           Le cadre laisse la place de ces barres (et du clavier) et prend la couleur de fond de l'app. */
        root = new FrameLayout(this);
        root.setBackgroundColor(Color.parseColor("#F6F2EC"));
        root.addView(web, new FrameLayout.LayoutParams(FrameLayout.LayoutParams.MATCH_PARENT, FrameLayout.LayoutParams.MATCH_PARENT));
        root.setOnApplyWindowInsetsListener(new View.OnApplyWindowInsetsListener() {
            @Override public WindowInsets onApplyWindowInsets(View v, WindowInsets insets) {
                if (Build.VERSION.SDK_INT >= 30) {
                    android.graphics.Insets i = insets.getInsets(WindowInsets.Type.systemBars() | WindowInsets.Type.displayCutout() | WindowInsets.Type.ime());
                    v.setPadding(i.left, i.top, i.right, i.bottom);
                } else {
                    v.setPadding(insets.getSystemWindowInsetLeft(), insets.getSystemWindowInsetTop(), insets.getSystemWindowInsetRight(), insets.getSystemWindowInsetBottom());
                }
                return insets;
            }
        });
        setContentView(root);
        applyTheme("#F6F2EC", false);

        if (savedInstanceState != null) web.restoreState(savedInstanceState);
        else web.loadUrl("file:///android_asset/www/index.html");
        Reminders.schedule(this);

        /* Retour : revient à l'écran précédent de l'app, ou la quitte depuis le premier écran.
           (Android 16 n'appelle plus onBackPressed : il faut s'inscrire auprès du système.) */
        if (Build.VERSION.SDK_INT >= 33) {
            getOnBackInvokedDispatcher().registerOnBackInvokedCallback(android.window.OnBackInvokedDispatcher.PRIORITY_DEFAULT,
                    new android.window.OnBackInvokedCallback() { @Override public void onBackInvoked() { goBack(); } });
        }
    }

    private void goBack() {
        if (web.canGoBack()) web.goBack();
        else finish();
    }

    /** Ouvre un site (page de don, licences, Sefaria) dans le navigateur du téléphone. */
    private void openExternal(String url) {
        if (url == null || !(url.startsWith("https://") || url.startsWith("http://"))) return;
        try { startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(url))); } catch (ActivityNotFoundException e) { /* pas de navigateur */ }
    }

    /** Couleur du cadre et des barres du système, selon l'apparence choisie dans l'app (claire ou sombre). */
    @SuppressWarnings("deprecation")
    private void applyTheme(String bg, boolean dark) {
        int color;
        try { color = Color.parseColor(bg); } catch (Exception e) { return; }
        root.setBackgroundColor(color);
        if (Build.VERSION.SDK_INT < 35) { getWindow().setStatusBarColor(color); getWindow().setNavigationBarColor(color); }
        if (Build.VERSION.SDK_INT >= 30) {
            WindowInsetsController c = getWindow().getInsetsController();
            int light = WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS | WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS;
            if (c != null) c.setSystemBarsAppearance(dark ? 0 : light, light);
        } else {
            int flags = View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR | (Build.VERSION.SDK_INT >= 26 ? View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR : 0);
            View d = getWindow().getDecorView();
            d.setSystemUiVisibility(dark ? d.getSystemUiVisibility() & ~flags : d.getSystemUiVisibility() | flags);
        }
    }

    /** Prévient l'app web que l'autorisation des notifications a changé. */
    private void notifyChanged() {
        if (web != null) web.evaluateJavascript("window.SM_NOTIFY_CHANGED && SM_NOTIFY_CHANGED()", null);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == ASK_NOTIFICATIONS) { Reminders.schedule(this); notifyChanged(); }
    }

    @Override
    protected void onResume() {
        super.onResume();
        notifyChanged();   // l'utilisateur a pu changer l'autorisation dans les réglages d'Android
    }

    /** Pont appelé par l'app web (window.SMAndroid). */
    private class Bridge {
        /** Lien vers un site : appelé par runtime.js. */
        @JavascriptInterface
        public void open(final String url) {
            runOnUiThread(new Runnable() { @Override public void run() { openExternal(url); } });
        }

        /** Apparence : couleur de fond de l'app et mode sombre ou non. */
        @JavascriptInterface
        public void theme(final String bg, final boolean dark) {
            runOnUiThread(new Runnable() { @Override public void run() { applyTheme(bg, dark); } });
        }

        /** Liste des prochains rappels, calculée par l'app web (JSON). Une liste vide annule les rappels. */
        @JavascriptInterface
        public void reminders(String json) {
            Reminders.save(MainActivity.this, json);
        }

        /** Vrai si Android laisse l'app afficher des notifications. */
        @JavascriptInterface
        public boolean canNotify() {
            return Reminders.allowed(MainActivity.this);
        }

        /** Demande l'autorisation d'afficher des notifications (Android 13 et plus) ; sinon ouvre les réglages de l'app. */
        @JavascriptInterface
        public void askNotify() {
            runOnUiThread(new Runnable() {
                @Override public void run() {
                    if (Reminders.allowed(MainActivity.this)) return;
                    if (Build.VERSION.SDK_INT >= 33 && checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED
                            && shouldAskAgain()) {
                        requestPermissions(new String[] { Manifest.permission.POST_NOTIFICATIONS }, ASK_NOTIFICATIONS);
                    } else {
                        try {
                            startActivity(new Intent(android.provider.Settings.ACTION_APP_NOTIFICATION_SETTINGS)
                                    .putExtra(android.provider.Settings.EXTRA_APP_PACKAGE, getPackageName()));
                        } catch (ActivityNotFoundException e) { /* réglages indisponibles */ }
                    }
                }
            });
        }

        /** Impression (ou PDF) de la page : appelée par SM_PRINT() dans globals.js. */
        @JavascriptInterface
        public void print(final String title) {
            runOnUiThread(new Runnable() {
                @Override public void run() {
                    PrintManager pm = (PrintManager) getSystemService(PRINT_SERVICE);
                    if (pm != null) pm.print(title, web.createPrintDocumentAdapter(title), null);
                }
            });
        }
    }

    /** Android ne repose plus la question après deux refus : on le sait par le drapeau « déjà demandé ». */
    private boolean shouldAskAgain() {
        android.content.SharedPreferences p = getSharedPreferences("app", MODE_PRIVATE);
        boolean asked = p.getBoolean("notifAsked", false);
        if (!asked) { p.edit().putBoolean("notifAsked", true).apply(); return true; }
        return Build.VERSION.SDK_INT >= 33 && shouldShowRequestPermissionRationale(Manifest.permission.POST_NOTIFICATIONS);
    }

    @Override
    protected void onSaveInstanceState(Bundle out) {
        super.onSaveInstanceState(out);
        web.saveState(out);
    }

    @Override
    @SuppressWarnings("deprecation")
    public void onBackPressed() {
        goBack();
    }
}
