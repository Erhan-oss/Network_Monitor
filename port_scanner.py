import socket
import datetime

def check_port(ip, port, timeout=1):
    """
    Belirtilen IP ve port için bağlantı denemesi yapar.
    Port açıksa OPEN, kapalıysa CLOSED döner.
    """
    s = socket.socket()
    s.settimeout(timeout)

    try:
        s.connect((ip, port))
        s.close()
        status = True
    except:
        status = False

    # Log kaydı
    log_port(ip, port, status)

    return status


def log_port(ip, port, status):
    """
    Port sonucunu logs/ports.log dosyasına yazar.
    """
    with open("logs/ports.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {ip}:{port} - {'OPEN' if status else 'CLOSED'}\n")
