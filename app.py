from flask import Flask, render_template
import json
from ping_monitor import ping_device
from port_scanner import check_port

app = Flask(__name__)

@app.route("/")
def dashboard():

    # Cihaz listesi yükleniyor
    with open("devices.json", "r") as f:
        devices = json.load(f)

    results = []

    # Her cihaz için ping + port taraması yapılıyor
    for dev in devices:
        ip = dev["ip"]
        name = dev["name"]

        # Ping
        ping_status = ping_device(ip)

        # Portlar
        port_results = {}
        for p in dev["ports"]:
            port_results[p] = check_port(ip, p)

        results.append({
            "name": name,
            "ip": ip,
            "status": ping_status,
            "ports": port_results
        })

    return render_template("dashboard.html", devices=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
