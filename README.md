# Network_Monitor
Ağımızdaki donanımların, daha çok güvenlik cihazlarının, aktif olup olmadığını ya da hangi portların açık olduğunu local ip den basit bir dashboard ile gösteriyor.
------------------
dosya yapısı şu şekilde olmalı:
Network_Monitor
|
|- app.py
|- ping_monitor.py
|- port_scanner.py
|- devices.json
|- templates/
    |- dashboard.html
|- logs/
    |- ping.log
    |- port.log
-------------------
cihaz ekleme çıkarma gibi durumlarda devices.json dosyasındaki bilgileri değiştirmeniz yeterlidir.
logs dosyalarında ise hangi ip ya da portun hangi tarih/saatte açık ya da kapalı olduğu bilgileri yazılır.
