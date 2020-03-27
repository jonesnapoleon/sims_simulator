class TheSims:

    def __init__(self, name):
        self.hygiene = 0
        self.energy = 10
        self.fun = 0
        self.name = name

    def isWin(self):
        if (self.hygiene == 15 and self.energy == 15 and self.fun == 15):
            print("============= YOU WIN =============")
        else:
            print("============= YOU LOSE =============")
        
    def isHygieneEnergyFunValid(self, hygiene_bonus, energy_bonus, fun_bonus):
        isHygieneValid = (self.hygiene + hygiene_bonus) >= 0 and (self.hygiene + hygiene_bonus) <= 15
        isEnergyValid = (self.energy + energy_bonus) >= 0 and (self.energy + energy_bonus) <= 15
        isFunValid = (self.fun + fun_bonus) >= 0 and (self.fun + fun_bonus) <= 15 
        return (isHygieneValid and isEnergyValid and isFunValid)

    def hygieneEnergyFunAdd(self, hygiene_bonus, energy_bonus, fun_bonus):
        if (not self.isHygieneEnergyFunValid(hygiene_bonus, energy_bonus, fun_bonus)):
            print("Aksi tidak valid\n")
        else:
            self.hygiene += hygiene_bonus
            self.energy += energy_bonus
            self.fun += fun_bonus

    def switch(self, aksi):
        if (aksi == "Tidur Siang"):
            self.hygieneEnergyFunAdd(0, 10, 0)
        elif (aksi == "Tidur Malam"):
            self.hygieneEnergyFunAdd(0, 15, 0)
        elif (aksi == "Makan Hamburger"): 
            self.hygieneEnergyFunAdd(0, 5, 0)
        elif (aksi == "Makan Pizza"): 
            self.hygieneEnergyFunAdd(0, 10, 0)
        elif (aksi == "Makan Steak and Beans"): 
            self.hygieneEnergyFunAdd(0, 15, 0)
        elif (aksi == "Minum Air"): 
            self.hygieneEnergyFunAdd(-5, 0, 0)
        elif (aksi == "Minum Kopi"): 
            self.hygieneEnergyFunAdd(-10, 5, 0)
        elif (aksi == "Minum Jus"): 
            self.hygieneEnergyFunAdd(-5, 10, 0)
        elif (aksi == "Buang Air Kecil"): 
            self.hygieneEnergyFunAdd(5, 0, 0)
        elif (aksi == "Buang Air Besar"): 
            self.hygieneEnergyFunAdd(10, -5, 0)
        elif (aksi == "Bersosialisasi ke Kafe"): 
            self.hygieneEnergyFunAdd(-5, -10, 15)
        elif (aksi == "Bermain Media Sosial"): 
            self.hygieneEnergyFunAdd(0, -10, 10)
        elif (aksi == "Bermain Komputer"): 
            self.hygieneEnergyFunAdd(0, -10, 15)
        elif (aksi == "Mandi"):
            self.hygieneEnergyFunAdd(15, -5, 0)
        elif (aksi == "Cuci Tangan"): 
            self.hygieneEnergyFunAdd(5, 0, 0)
        elif (aksi == "Mendengarkan Musik Di Radio"): 
            self.hygieneEnergyFunAdd(0, -5, 10)
        elif (aksi == "Membaca Koran"): 
            self.hygieneEnergyFunAdd(0, -5, 5)
        elif (aksi == "Membaca Novel"): 
            self.hygieneEnergyFunAdd(0, -5, 10) 
        else:
            print("Tidak ada aksi\n")

    def printData(self):
        print("Hygiene: " + str(self.hygiene))
        print("Energy: " + str(self.energy))
        print("Fun: " + str(self.fun))

    def isMati(self):
        return (self.hygiene == 15 and self.energy == 15 and self.fun == 15) or (self.hygiene == 0 and self.energy == 0 and self.fun == 0)

nama = input("Welcome to The Sims\nNama karakter: ")
Game = TheSims(nama)
print()

while ( not Game.isMati() ):
    print("==== Keadaan karakter "+ Game.name +" ====")
    Game.printData()
    print("=====================================")
    aksi = input("Aksi: ")
    Game.switch(aksi)

print("============ GAME OVER ============")
Game.isWin()
print("Keadaan final "+ Game.name +" sebelum game:")
Game.printData()
print("=====================================")