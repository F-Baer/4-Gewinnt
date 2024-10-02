Dieses Projekt ist eine Implementierung des klassischen "4 Gewinnt"-Spiels mit einer grafischen Benutzeroberfläche (GUI) in Python unter Verwendung des PyQt5-Frameworks. Es bietet sowohl die Möglichkeit, gegen einen anderen Spieler als auch gegen den Computer zu spielen. Der Computer verfügt über verschiedene Schwierigkeitsstufen.

Voraussetzungen
Um dieses Spiel auszuführen, benötigen Sie:

- Python 3.x
- PyQt5: Um die GUI-Komponenten zu verwenden.

Dateien
- Spiel.py: Die Hauptdatei, die das Spiel implementiert.
- Spielstein_rot.png: Das Bild des roten Spielsteins.
- Spielstein_blau.png: Das Bild des blauen Spielsteins.

Spielmodus
Das Spiel unterstützt zwei Spielmodi:

VS Mensch: Zwei Spieler spielen abwechselnd auf dem selben Gerät.
VS Computer: Der Spieler tritt gegen einen Computergegner an.

Computer-Schwierigkeitsstufen:
Leicht: Der Computer wählt zufällige Züge.
Mittel: Der Computer blockiert potenzielle Gewinnzüge des Gegners.
Schwer: Der Computer blockiert nicht nur den Gegner, sondern versucht, den bestmöglichen Zug zu machen.

Spielregeln
Das Ziel des Spiels ist es, vier Steine in einer Reihe anzuordnen, sei es horizontal, vertikal oder diagonal. Wenn das Spielfeld voll ist, endet das Spiel mit einem Unentschieden.

Verwendung
- Stellen Sie sicher, dass Sie Python 3.x installiert haben.
- Installieren Sie PyQt5, falls noch nicht geschehen.
- Platzieren Sie die Bilder der Spielsteine (Spielstein_rot.png und Spielstein_blau.png) im selben Verzeichnis wie die Python-Datei.
- Führen Sie das Spiel mit der 4_Gewinnt_Spiel.py aus:	
- Nach dem Start des Spiels können Sie den Spielmodus und die Schwierigkeitsstufe auswählen. Klicken Sie auf eine Zelle, um Ihren Spielstein zu platzieren.

Funktionen
- Spielmodus: Wählen Sie zwischen "VS Mensch" oder "VS Computer".
- Schwierigkeitsstufe: Wählen Sie die Spielstärke des Computers.
- Spielende: Das Spiel endet entweder mit einem Gewinner oder mit einem Unentschieden, wenn das Spielfeld voll ist.
- Neustart: Nach jedem Spiel (Sieg, Niederlage oder Unentschieden) wird das Spielfeld zurückgesetzt.

Weiterentwicklung Möglichkeit
- Erweiterung der KI-Logik für die Schwierigkeitsstufe "Schwer".
- Verbesserung der grafischen Darstellung.
- Hinzufügen eines Online-Mehrspielermodus.