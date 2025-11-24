import subprocess
import platform
import datetime

def ping_device(ip):
    """
    Belirtilen IP adresine 1 kez ping atar.
    Windows için -n, Linux/Unix için -c parametresi kullanılır.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        success = (result.returncode == 0)
    except Exception:
        success = False

    # Log kaydı
    log_ping(ip, success)

    return success


def log_ping(ip, status):
    """
    Ping sonucunu logs/ping.log dosyasına yazar.
    """
    with open("logs/ping.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {ip} - {'ONLINE' if status else 'OFFLINE'}\n")
