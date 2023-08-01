# Einfaches Backup-Tool

Das Einfache Backup-Tool ist ein Python-Skript, mit dem Benutzer automatische Sicherungen wichtiger Dateien und Verzeichnisse auf einem externen Speichergerät planen können.

## Funktionen

- Benutzerfreundlich: Das Tool bietet eine interaktive Befehlszeilenschnittstelle für eine einfache Einrichtung.
- Geplante Sicherungen: Benutzer können das Quellverzeichnis, das Zielverzeichnis (externes Speichergerät) und das Intervall für die Sicherungen in Sekunden angeben, um regelmäßige Sicherungen zu planen.
- Fehlerbehandlung: Das Tool behandelt gängige Fehler wie nicht vorhandenes Quellverzeichnis und ungültige Eingaben für das Sicherungsintervall.

## Anleitung

1. Klone dieses Repository oder lade das Python-Skript `BackupScheduler.py` auf deinen lokalen Rechner herunter.

2. Stelle sicher, dass Python 3.x auf deinem System installiert ist.

3. Öffne ein Terminal oder eine Eingabeaufforderung und navigiere zum Verzeichnis, in dem sich die Datei `BackupScheduler.py` befindet.

4. Führe das Skript mit folgendem Befehl aus:

```bash
python BackupScheduler.py
```

5. Das Tool zeigt eine Begrüßungsnachricht an und fordert dich auf, den Pfad des Quellverzeichnisses einzugeben, das du sichern möchtest. Gib den absoluten oder relativen Pfad des Verzeichnisses ein und drücke die Eingabetaste.

6. Als nächstes wirst du aufgefordert, den Pfad des Zielverzeichnisses einzugeben, das das externe Speichergerät ist, auf dem die Sicherung gespeichert werden soll. Gib den Pfad ein und drücke die Eingabetaste.

7. Abschließend gib das Sicherungsintervall in Sekunden ein. Zum Beispiel, wenn du die Sicherung stündlich durchführen möchtest, gib 3600 ein. Das Intervall sollte eine positive Ganzzahl sein, die die Anzahl der Sekunden zwischen den Sicherungen angibt.

8. Sobald die Einrichtung abgeschlossen ist, beginnt das Tool automatisch mit der Erstellung von Sicherungen im angegebenen Intervall. Die Sicherungen werden im Zielverzeichnis gespeichert.

##Beispiel

```javascript
Willkommen beim einfachen Backup-Tool!
Gib den Pfad des Quellverzeichnisses ein, das gesichert werden soll: /pfad/zum/quellverzeichnis
Gib den Pfad des Zielverzeichnisses (externes Speichergerät) ein: /pfad/zum/externen_speicher
Gib das Sicherungsintervall in Sekunden ein (z. B. 3600 für 1 Stunde): 3600
Sicherung erfolgreich: /pfad/zum/quellverzeichnis -> /pfad/zum/externen_speicher
Sicherung erfolgreich: /pfad/zum/quellverzeichnis -> /pfad/zum/externen_speicher
Sicherung erfolgreich: /pfad/zum/quellverzeichnis -> /pfad/zum/externen_speicher
...
```

## Hinweise

- Das Tool läuft unbegrenzt und erstellt Sicherungen im angegebenen Intervall, bis du es manuell beendest, indem du Strg + C drückst.
- Stelle sicher, dass du Lese- und Schreibberechtigungen für die Quell- und Zielverzeichnisse hast, um mögliche Berechtigungsfehler zu vermeiden.
- Dieses Tool ist für grundlegende Sicherungszwecke gedacht. Für fortgeschrittene Sicherungs- und Wiederherstellungsfunktionen empfiehlt es sich, professionelle Backup-Lösungen zu verwenden.


## Haftungsausschluss 

Das Einfache Backup-Tool wird "wie es ist" ohne jegliche Gewährleistung oder Garantie zur Verfügung gestellt. Die Verwendung erfolgt auf eigene Gefahr. Der Entwickler haftet nicht für Datenverluste oder Schäden, die durch die Verwendung dieses Tools entstehen.

## Lizenz

Dieses Tool ist Open-Source und unter der MIT-Lizenz lizenziert. Weitere Details findest du in der Datei [Lizenzdatei](LICENSE).
