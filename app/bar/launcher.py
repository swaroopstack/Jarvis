import subprocess


def find_application(command):
    powershell_command = (
        f"Get-StartApps | "
        f"Where-Object {{$_.Name -like '*{command}*'}} | "
        f"Select-Object -First 1 -ExpandProperty AppID"
    )

    result = subprocess.run(
        ["powershell", "-Command", powershell_command],
        capture_output=True,
        text=True
    )

    app_id = result.stdout.strip()

    if app_id:
        return app_id

    return None


def launch_application(command):
    app_id = find_application(command)

    if not app_id:
        return False

    subprocess.Popen(
        ["explorer.exe", f"shell:AppsFolder\\{app_id}"]
    )

    return True