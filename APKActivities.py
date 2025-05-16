import xml.etree.ElementTree as ET
import subprocess
import os

def extract_manifest_info(manifest_path):
    try:
        tree = ET.parse(manifest_path)
        root = tree.getroot()

        # Get package name
        package_name = root.get('package')

        # Android namespace
        android_ns = 'http://schemas.android.com/apk/res/android'

        # Get activities
        application = root.find('application')
        activities = application.findall('activity') if application is not None else []

        # Extract activity names
        activity_names = []
        for activity in activities:
            name = activity.get(f'{{{android_ns}}}name')
            if name:
                if name.startswith('.'):
                    name = package_name + name
                elif '.' not in name:
                    name = package_name + '.' + name
                activity_names.append(name)

        if not activity_names:
            print(f"⚠️ Warning: No <activity> tags found in '{manifest_path}'.")
            exit(1)

        return package_name, activity_names
    except Exception as e:
        print(f"❌ Error parsing manifest: {e}")
        exit(1)

def run_adb_commands(package_name, activity_names):
    print("\n📱 Launching activities via ADB...\n")
    input("▶️ Press Enter to start testing activities...")

    for activity in activity_names:
        cmd = f"adb shell am start -n {package_name}/{activity}"
        print(f"\n🚀 Running: {cmd}")
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Failed to launch {activity}: {e}")
        input("\n⏭️ Press Enter to continue to the next activity...")

def print_adb_version():
    try:
        result = subprocess.run(["adb", "version"], capture_output=True, text=True, check=True)
        print(f"\n🔧 {result.stdout.strip()}")
    except Exception as e:
        print("❌ ADB not found or not installed.")
        exit(1)


# Main
if __name__ == "__main__":
    manifest_file = 'AndroidManifest.xml'
    if not os.path.exists(manifest_file):
        print(f"❌ Error: File '{manifest_file}' does not exist.")
        exit(1)

    print_adb_version()

    package_name, activity_names = extract_manifest_info(manifest_file)

    print(f"\n📦 Package: {package_name}")
    print("\n🎯 Activities:")
    for act in activity_names:
        print(f" - {act}")

    run_adb_commands(package_name, activity_names)
