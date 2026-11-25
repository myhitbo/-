package org.shnayimmikra.app;

import android.app.Activity;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.print.PrintManager;
import android.webkit.JavascriptInterface;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

/** Affiche l'application web embarquée (assets/www). Les liens vers des sites s'ouvrent dans le navigateur du téléphone. */
public class MainActivity extends Activity {
    private WebView web;

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
        setContentView(web);
        if (savedInstanceState != null) web.restoreState(savedInstanceState);
        else web.loadUrl("file:///android_asset/www/index.html");
    }

    /** Ouvre un site (page de don, licences, Sefaria) dans le navigateur du téléphone. */
    private void openExternal(String url) {
        if (url == null || !(url.startsWith("https://") || url.startsWith("http://"))) return;
        try { startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(url))); } catch (ActivityNotFoundException e) { /* pas de navigateur */ }
    }

    /** Pont appelé par l'app web (window.SMAndroid). */
    private class Bridge {
        /** Lien vers un site : appelé par runtime.js. */
        @JavascriptInterface
        public void open(final String url) {
            runOnUiThread(new Runnable() { @Override public void run() { openExternal(url); } });
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

    @Override
    protected void onSaveInstanceState(Bundle out) {
        super.onSaveInstanceState(out);
        web.saveState(out);
    }

    @Override
    public void onBackPressed() {
        if (web.canGoBack()) web.goBack();
        else super.onBackPressed();
    }
}
