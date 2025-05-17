from openpyxl import Workbook

def informacija_par_kreditu(numurs):
    print(f"Ievadiet datus par {numurs}. kredītu:")
    nosaukums = input("Kredīta nosaukums: ")
    pamatsumma = float(input("Pamatsumma (€): "))
    procenti = float(input("Gada procentu likme (%): "))
    termins = int(input("Termiņš mēnešos: "))
    return Kredits(nosaukums, pamatsumma, procenti, termins)

class Kredits:
    def __init__(self, nosaukums, pamatsumma, gada_procenti, termins_menesos):
        self.nosaukums = nosaukums
        self.pamatsumma = pamatsumma
        self.gada_procenti = gada_procenti / 100
        self.termins = termins_menesos
        self.menesa_maksa = self.aprekinat_menesa_maksu()
        self.atmaksas_grafiks = []

    def aprekinat_menesa_maksu(self):  
        i = self.gada_procenti / 12
        n = self.termins
        P = self.pamatsumma

        if i == 0:
            return P / n
        else:
           return P * (i * (1 + i) ** n) / ((1 + i) ** n - 1) # = A (anuitāte)
        
    def aprekina_atmaksas_grafiku(self):
        atlikums = self.pamatsumma # atlikums ir tas, cik vēl bankai jāmaksā
        for menesis in range(1, self.termins + 1):
            interese = atlikums * (self.gada_procenti / 12)
            atmaksas_summa = self.menesa_maksa - interese
            atlikums -= atmaksas_summa
            if atlikums < 0:
                atmaksas_summa += atlikums
                atlikums = 0
            self.atmaksas_grafiks.append((menesis, round(interese, 2), round(atmaksas_summa, 2), round(atlikums, 2)))
            if atlikums <= 0:
                break 

    def kopeja_summa(self):
        return round(sum([x[1] + x[2] for x in self.atmaksas_grafiks]), 2) # Tas, ko mēs samaksājam kopā
              

    def kopeja_intereses_summa(self):
        return round(sum([x[1] for x in self.atmaksas_grafiks]), 2)
    
    def interese_procentuali(self):
        return round((self.kopeja_intereses_summa() / self.pamatsumma) * 100, 2)
    
    def koeficients(self): # cik jāmaksā par katru aizņemto eiro
        return round(self.kopeja_summa() / self.pamatsumma, 4)

def izveidot_excel_failu(kredits1, kredits2, faila_vards="kreditu_salidzinasana.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Kredītu salīdzinājums"

    # Virsraksti tabulā
    ws.append(["Kredīta nosaukums", kredits1.nosaukums, kredits2.nosaukums])
    ws.append(["Pamatsumma (€)", kredits1.pamatsumma, kredits2.pamatsumma])
    ws.append(["Gada procentu likme (%)", kredits1.gada_procenti * 100, kredits2.gada_procenti * 100])
    ws.append(["Termiņš (mēnešos)", kredits1.termins, kredits2.termins])
    ws.append([])

    ws.append(["Kopējā atmaksas summa (€)", kredits1.kopeja_summa(), kredits2.kopeja_summa()])
    ws.append([])

    ws.append(["Kopējā interese (€)", kredits1.kopeja_intereses_summa(), kredits2.kopeja_intereses_summa()])
    ws.append(["Interese % no aizņēmuma summas", kredits1.interese_procentuali(), kredits2.interese_procentuali()])
    ws.append(["Anuitātes summa (€)", round(kredits1.aprekinat_menesa_maksu(), 2), round(kredits2.aprekinat_menesa_maksu(), 2)])
    ws.append(["Aizņēmuma koeficients", kredits1.koeficients(), kredits2.koeficients()])
    ws.append([])

    max_rindu = max(len(kredits1.atmaksas_grafiks), len(kredits2.atmaksas_grafiks))

    ws.append([
    "Mēnesis", 
    f"{kredits1.nosaukums} - Interese",
    f"{kredits1.nosaukums} - Summa, kas iet nost no parāda",
    f"{kredits1.nosaukums} - Atlikums",

    f"{kredits2.nosaukums} - Interese", 
    f"{kredits2.nosaukums} - Summa, kas iet nost no parāda",
    f"{kredits2.nosaukums} - Atlikums"
    ])

    for i in range(max_rindu):
        rinda = []

        if i < len(kredits1.atmaksas_grafiks):
            menesis = i + 1
        elif i < len(kredits2.atmaksas_grafiks):
            menesis = i + 1    
        else:
            menesis = ""
        rinda.append(menesis)

        if i < len(kredits1.atmaksas_grafiks):
            rinda.extend(kredits1.atmaksas_grafiks[i][1:])
        else:
            rinda.extend(["", "", ""])

        if i < len(kredits2.atmaksas_grafiks):
            rinda.extend(kredits2.atmaksas_grafiks[i][1:])
        else:
            rinda.extend(["", "", ""])

        ws.append(rinda)            

    wb.save(faila_vards)
    print(f"Dati saglabāti failā '{faila_vards}'.")        

def main():
    kredits1 = informacija_par_kreditu(1)
    kredits2 = informacija_par_kreditu(2)

    kredits1.aprekina_atmaksas_grafiku()
    kredits2.aprekina_atmaksas_grafiku()

    izveidot_excel_failu(kredits1, kredits2)

    print("\nSalīdzinājums:")

    kredits1_koeficients = kredits1.koeficients()
    kredits2_koeficients = kredits2.koeficients()

    if kredits1_koeficients < kredits2_koeficients:
        print(f"Kredīts '{kredits1.nosaukums}' ir izdevīgāks, skatoties pēc atmaksas efektivitātes.")
    else:
        print(f"Kredīts '{kredits2.nosaukums}' ir izdevīgāks, skatoties pēc atmaksas efektivitātes.")

if __name__ == "__main__":
    main()