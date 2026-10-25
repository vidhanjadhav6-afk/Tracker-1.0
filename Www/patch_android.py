"""Runs in CI after `npx cap add android`: adds permissions, dark system bars and the notification icon."""
import pathlib, re, shutil

root = pathlib.Path("android")

# 1) copy overlay files (notification icon etc.)
overlay = pathlib.Path("android-overlay")
if overlay.exists():
    shutil.copytree(overlay, root, dirs_exist_ok=True)

# 2) permissions needed for on-time reminders
manifest = root / "app/src/main/AndroidManifest.xml"
text = manifest.read_text()
perms = [
    "android.permission.POST_NOTIFICATIONS",
    "android.permission.SCHEDULE_EXACT_ALARM",
    "android.permission.VIBRATE",
    "android.permission.RECEIVE_BOOT_COMPLETED",
]
add = "".join('    <uses-permission android:name="%s" />\n' % p for p in perms if p not in text)
if add:
    text = text.replace("</manifest>", add + "</manifest>")
    manifest.write_text(text)

# 3) dark status bar and navigation bar to match the app
styles = root / "app/src/main/res/values/styles.xml"
s = styles.read_text()
if "statusBarColor" not in s:
    s = re.sub(
        r'(<style name="AppTheme\.NoActionBar"[^>]*>)',
        r'\1\n        <item name="android:statusBarColor">#0B1120</item>\n        <item name="android:navigationBarColor">#0B1120</item>',
        s, count=1)
    styles.write_text(s)

print("Android project patched")
