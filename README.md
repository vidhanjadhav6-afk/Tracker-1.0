# Dual-Track (Capacitor + Local Notifications)

Reminders are scheduled on the phone by Android itself (weekly, per task), so they
fire even when the app is closed.

## Build the APK on GitHub (free, no Android Studio)
1. Create a repository and upload everything in this folder (keep the .github/workflows/android.yml path).
2. Open the Actions tab -> "Build Android APK" -> Run workflow (it also runs on every push).
3. When it turns green, open the run and download the "Dual-Track-APK" artifact (zip with app-debug.apk).
4. Install the APK on your phone (allow "install unknown apps").
5. Open the app -> gear icon -> switch "Task reminders" on -> allow notifications.
   If Settings shows "Allow exact alarm timing", tap it and allow, so alerts fire on the minute.

## Edit the app
All app code is in www/index.html (schedule data `S`, quotes `Q`, wallpapers `WP`).
Commit a change and the workflow builds a new APK.

## Notes
- Capacitor 6 (Node 20, Java 17). To move to a newer Capacitor, change the versions in package.json and the
  Node/Java versions in the workflow to match Capacitor's current requirements.
- Alarm-style long vibration and the alarm-tone option need custom native code; with the plugin,
  vibration/sound follow the phone's notification settings for the app.
- Battery saver on some phones can delay alarms: set the app to "Unrestricted" battery use.
