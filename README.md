# 📱 Android Activity Launcher via ADB

This Python script parses an `AndroidManifest.xml` file to extract all defined `<activity>` components and interactively launches them on a connected Android device using ADB (`adb shell am start`). It's useful for quick manual testing.

---

## 📦 Features

- Extracts the **package name** and all **activities** from `AndroidManifest.xml`
- Automatically handles:
  - Relative activity names (e.g., `.MainActivity`)
  - Activities without dots (e.g., `MainActivity`)
- Verifies **ADB installation**
- Provides an **interactive interface** to launch each activity one by one

---

## 🧰 Requirements

- Python 3.6+
- [ADB (Android Debug Bridge)](https://developer.android.com/tools/adb) installed and added to your system's `PATH`
- `AndroidManifest.xml` in the script's directory

---

## 🚀 Usage

1. **Clone the repository or copy the script** into a file, e.g., `APKActivities.py`
2. Place your `AndroidManifest.xml` in the same directory
3. Run the script:
```bash
python APKActivities.py
```
4. Follow the prompts to:
  - Review the extracted package and activity names
  - Launch each activity one by one via ADB

---

## 🧪 Example Output

```bash
🔧 Android Debug Bridge version 1.0.41
📦 Package: com.example.myapp

🎯 Activities:
 - com.example.myapp.MainActivity
 - com.example.myapp.SettingsActivity

📱 Launching activities via ADB...

▶️ Press Enter to start testing activities...

🚀 Running: adb shell am start -n com.example.myapp/com.example.myapp.MainActivity
⏭️ Press Enter to continue to the next activity...
```

---

## 📂 File Structure
```bash
.
├── launch_activities.py     # The main script
└── AndroidManifest.xml      # Must be placed in the same directory
```

---

## ⚠️ Notes

- The script requires a connected Android device or emulator.
- If ADB or the device is not detected, the script will exit with an error.
- No activities found? Ensure your AndroidManifest.xml is properly formatted and complete.

---

## 📄 License

Feel free to modify and use this script in your own testing or automation tools.
