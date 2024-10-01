from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QAbstractItemView, QTableWidgetItem, QMessageBox, QGroupBox, QRadioButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import QSize, Qt

import random

class Spiel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("4 Gewinnt Spiel")
        self.setFixedSize(495, 600)
        
        # Spiel Variablen
        self.spieler = 0
        self.spielfeld_status = [[0 for _ in range(7)] for _ in range(6)]
        
        # Für das Spielfeld
        self.spielfeld = QTableWidget(6, 7, self)
        self.spielfeld.horizontalHeader().hide()
        self.spielfeld.verticalHeader().hide()
        self.spielfeld.setSelectionMode(QTableWidget.NoSelection)
        self.spielfeld.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.spielfeld.resize(493, 423)
        self.spielfeld.setIconSize(QSize(65, 65))
       
        zeilen = range(0, 6)
        spalten = range(0, 7)
        
        for zeile in zeilen:
            self.spielfeld.setRowHeight(zeile, 70)
        for spalte in spalten:
            self.spielfeld.setColumnWidth(spalte, 70)
            
        # Groupbox Spieler Wahl
        self.spieler_wahl_box = QGroupBox(self)
        self.spieler_wahl_box.setGeometry(20, 446, 180, 40)
        spieler_wahl_layout = QHBoxLayout()
        
        self.vs_mensch = QRadioButton("VS Mensch")
        self.vs_computer = QRadioButton("VS Computer")
        self.vs_computer.setChecked(True)
        
        spieler_wahl_layout.addWidget(self.vs_mensch)
        spieler_wahl_layout.addWidget(self.vs_computer)
        self.spieler_wahl_box.setLayout(spieler_wahl_layout)
        
        # Groupbox Layout Spielstärke 
        self.spielstaerke_box = QGroupBox("Spielstärke", self)
        self.spielstaerke_box.setGeometry(220, 440, 250, 46)
        spielstaerke_layout = QHBoxLayout()
        
        self.spielstaerke_leicht = QRadioButton("Leicht")
        self.spielstaerke_mittel = QRadioButton("Mittel")            
        self.spielstaerke_schwer = QRadioButton("Schwer")       
        self.spielstaerke_mittel.setChecked(True)
         
        spielstaerke_layout.addWidget(self.spielstaerke_leicht)
        spielstaerke_layout.addWidget(self.spielstaerke_mittel)
        spielstaerke_layout.addWidget(self.spielstaerke_schwer)
        self.spielstaerke_box.setLayout(spielstaerke_layout)
        
        # Spielsteine laden        
        self.spielstein_rot = QIcon("Spielstein_rot.png")
        self.spielstein_blau = QIcon("Spielstein_blau.png")   
        
        self.spielfeld.cellClicked.connect(self.spielstein_platzieren)
        
        self.show()
        
    def finde_freie_zeile(self, spalte):
       for zeile in range(5, -1, -1):
           if self.spielfeld.item(zeile, spalte) is None:
               return zeile
       return -1
              
    def spielstein_platzieren(self, x, y):        
        freie_zeile = self.finde_freie_zeile(y) 
                
        if freie_zeile == -1:
            QMessageBox.information(self, "Fehler", "Diese Spalte ist voll!")
            return

        if self.spieler == 0:
           item = QTableWidgetItem()
           item.setIcon(self.spielstein_blau)
           self.spielfeld.setItem(freie_zeile, y, item)
           self.spielfeld_status[freie_zeile][y] = 1
           if self.pruefe_gewinner(1, freie_zeile, y):
               return
           
           self.spieler_wechsel()
        
        elif self.spieler == 2:
            item = QTableWidgetItem()
            item.setIcon(self.spielstein_rot)
            self.spielfeld.setItem(freie_zeile, y, item)
            self.spielfeld_status[freie_zeile][y] = 2
            if self.pruefe_gewinner(2, freie_zeile, y):
                return
            
            self.spieler_wechsel()
        
        if self.ist_spielfeld_voll() == True:
            QMessageBox.information(self, "Unentschieden", "Das Spiel endet mit einem Unentschieden")
            self.reset_spiel()

    def ist_spielfeld_voll(self):
        for zeile in range(6):
            for spalte in range(7):
                if self.spielfeld_status[zeile][spalte] == 0:
                    return False
        return True

        
    def spieler_wechsel(self):   
        if self.vs_computer.isChecked():
            if self.spieler == 0:
                self.spieler = 1
                self.computer_zug()
            else:
                self.spieler = 0

        if self.vs_mensch.isChecked():     
            if self.spieler == 0:
                self.spieler = 2               
            else:
                self.spieler = 0  

    def computer_zug(self):
        if self.spielstaerke_leicht.isChecked():
           spalte, zeile = self.computer_zug_leicht()
           
        elif self.spielstaerke_mittel.isChecked():
            spalte, zeile = self.computer_zug_mittel()
            
        elif self.spielstaerke_schwer.isChecked():
            spalte, zeile = self.computer_zug_mittel()
                       
        item = QTableWidgetItem()
        item.setIcon(self.spielstein_rot)
        self.spielfeld.setItem(zeile, spalte, item)
        self.spielfeld_status[zeile][spalte] = 2
        if self.pruefe_gewinner(2, zeile, spalte):
            return
             
        self.spieler_wechsel()                        
    
    def computer_zug_leicht(self):
        spalte = random.randint(0, 6)
        freie_zeile = self.finde_freie_zeile(spalte)
    
        while freie_zeile == -1:
            spalte = random.randint(0, 6)
            freie_zeile = self.finde_freie_zeile(spalte)
                   
        return spalte, freie_zeile
    
    def computer_zug_mittel(self):
        for spalte in range(7):
            freie_zeile = self.finde_freie_zeile(spalte)
            if freie_zeile != -1:
                self.spielfeld_status[freie_zeile][spalte] = 1
                if self.spiel_logik(1,freie_zeile, spalte):
                    self.spielfeld_status[freie_zeile][spalte] = 0
                    return spalte, freie_zeile
                self.spielfeld_status[freie_zeile][spalte] = 0
        
        return self.computer_zug_leicht()
    
    def computer_zug_schwer(self):
        for spalte in range(7):
            freie_zeile = self.finde_freie_zeile(spalte)
            if freie_zeile != -1:
                self.spielfeld_status[freie_zeile][spalte] = 2
                if self.spiel_logik(2, freie_zeile, spalte):
                    self.spielfeld_status[freie_zeile][spalte] = 0
                    return spalte, freie_zeile
                self.spielfeld_status[freie_zeile][spalte]
                
        return self.computer_zug_mittel()
       
    def spiel_logik(self, spieler, x, y):
        return (self.pruefe_horizontal(spieler,x, y) or
                self.pruefe_vertikal(spieler, x, y) or
                self.pruefe_diagonal_link(spieler, x, y) or
                self.pruefe_diagonal_recht(spieler, x, y))
    
    def pruefe_horizontal(self, spieler, x, y):
        count = 0
        gewinn_position = []

        for spalte in range(7):
            if self.spielfeld_status[x][spalte] == spieler:
                count += 1
                gewinn_position.append((x, spalte))
                if count == 4:
                    self.markiere_gewinn(gewinn_position)
                    return True
            else:
                count = 0
                gewinn_position = []
        return False
    
    def pruefe_vertikal(self, spieler, x, y):
        count = 0
        gewinn_position = []

        for zeile in range(6):
            if self.spielfeld_status[zeile][y] == spieler:
                count += 1
                gewinn_position.append((zeile, y))
                if count == 4:
                    self.markiere_gewinn(gewinn_position)
                    return True
            else:
                count = 0
                gewinn_position = []
        return False
    
    def pruefe_diagonal_link(self, spieler, x, y):
        count = 0
        gewinn_position = []
        zeile = x
        spalte = y
        
        while zeile > 0 and spalte > 0:
            zeile -= 1
            spalte -= 1
            
        while zeile < 6 and spalte < 7:
            if self.spielfeld_status[zeile][spalte] == spieler:
                count += 1
                gewinn_position.append((zeile, spalte))
                if count == 4:
                    self.markiere_gewinn(gewinn_position)
                    return True
            else:
                count = 0
                gewinn_position = []
            
            zeile += 1
            spalte += 1
            
        return False
    
    def pruefe_diagonal_recht(self, spieler, x, y):
        count = 0
        gewinn_position = []
        zeile = x
        spalte = y
        
        while zeile > 0 and spalte < 6:
            zeile -= 1
            spalte -= 1

        while zeile > 6 and spalte > 0:
            if self.spielfeld_status[zeile][spalte] == spieler:
                count += 1
                gewinn_position.append((zeile, spalte))
                if count == 4:
                    self.markiere_gewinn(gewinn_position)
                    return True
            else:
                count = 0
                gewinn_position = []
            
            zeile += 1
            spalte += 1
            
        return False
    
    def pruefe_gewinner(self, spieler, x, y):
        if self.spiel_logik(spieler, x, y):
            if spieler == 1:
                QMessageBox.information(self, "Spielende", "Spieler 1 hat gewonnen!")
            elif spieler == 2:
                if self.vs_computer.isChecked():
                    QMessageBox.information(self, "Spielende", "Der Computer hat gewonnen!")
                else:
                    QMessageBox.information(self, "Spielende", "Spieler 2 hat gewonnen")
            
            self.reset_spiel()
            return True
        return False
    
    def markiere_gewinn(self, gewinn_position):
        for zeile, spalte in gewinn_position:
            item = self.spielfeld.item(zeile, spalte)
            if item:
                item.setBackground(QColor(0, 0, 0))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def reset_spiel(self):
        for zeile in range(6):
            for spalte in range(7):
                self.spielfeld.setItem(zeile, spalte, None)
                self.spielfeld_status[zeile][spalte] = 0
                
        self.spieler = 0
       

app = QApplication([])
fenster = Spiel()

app.exec()
