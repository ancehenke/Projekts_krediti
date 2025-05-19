from openpyxl import Workbook

def informacija_par_kreditu(numurs):
    print(f"Ievadiet datus par {numurs}. kredītu:")
    nosaukums = input("Kredīta nosaukums: ")
    pamatsumma = float(input("Pamatsumma (€): "))
    procenti = float(input("Gada procentu likme (%): "))
    termins = int(input("Termiņš mēnešos: "))
    return Kredits(nosaukums, pamatsumma, procenti, termins)

class Mezgls_rindai:
    def __init__(self, dati):
        self.dati = dati
        self.nakamais = None

class Rinda: # Definēju savu datu struktūru
    def __init__(self):
        self.pirmais_elements = None
        self.pedejais_elements = None

    def tuksa_rinda(self):
        return self.pirmais_elements is None

    def pievienot_elementu(self, dati):
        jauns_mezgls = Mezgls_rindai(dati)

        if self.pedejais_elements:
            self.pedejais_elements.nakamais = jauns_mezgls
        self.pedejais_elements = jauns_mezgls

        if self.pirmais_elements is None:
            self.pirmais_elements = jauns_mezgls

    def iznemt_elementu(self):
        if self.tuksa_rinda():
            raise Exception("Rinda ir tukša")
        
        dati = self.pirmais_elements.dati
        self.pirmais_elements = self.pirmais_elements.nakamais

        if self.pirmais_elements is None:
            self.pedejais_elements = None
        return dati

    def paskatit_pirmo(self):
        if self.tuksa_rinda():
            return None
        return self.pirmais_elements.dati

class Papildus_iemaksa:
    def __init__(self, menesis, summa):
        self.menesis = menesis
        self.summa = summa

class Kredits:
    def __init__(self, nosaukums, pamatsumma, gada_procenti, termins_menesos):
        self.nosaukums = nosaukums
        self.pamatsumma = pamatsumma
        self.gada_procenti = gada_procenti / 100
        self.termins = termins_menesos
        self.menesa_maksa = self.aprekinat_menesa_maksu()
        self.atmaksas_grafiks = []

        self.papildus_iemaksas = Rinda()

    def aprekinat_menesa_maksu(self):  
        i = self.gada_procenti / 12
        n = self.termins
        P = self.pamatsumma

        if i == 0:
            return P / n
        else:
           return P * (i * (1 + i) ** n) / ((1 + i) ** n - 1) # = A (anuitāte)
        
    def pievienot_papildus_iemaksu(self, menesis, summa):
        iemaksa = Papildus_iemaksa(menesis, summa)
        self.papildus_iemaksas.pievienot_elementu(iemaksa)    
        
    def aprekina_atmaksas_grafiku(self, sakt_no_menesa=1):
        if sakt_no_menesa == 1:
            self.atmaksas_grafiks.clear()
            atlikums = self.pamatsumma # atlikums ir tas, cik vēl bankai jāmaksā
        else:
            atlikusais_grafiks = self.atmaksas_grafiks[:sakt_no_menesa - 1]
            self.atmaksas_grafiks = atlikusais_grafiks
            if atlikusais_grafiks:
                atlikums = atlikusais_grafiks[-1][3]
            else:
                atlikums = self.pamatsumma

        self._kopeja_summa = 0
        self._kopeja_intereses_summa = 0

        if sakt_no_menesa > 1:
            for _, i, s, _ in self.atmaksas_grafiks:
                self._kopeja_summa += i + s
                self._kopeja_intereses_summa += i
        
        for menesis in range(sakt_no_menesa, self.termins + 1):

            while (not self.papildus_iemaksas.tuksa_rinda() and self.papildus_iemaksas.paskatit_pirmo().menesis == menesis):
                iemaksa = self.papildus_iemaksas.iznemt_elementu()
                print(f"[{self.nosaukums}] {menesis}. mēnesī veikta papildus iemaksa: {iemaksa.summa} €")
                atlikums -= iemaksa.summa
                if atlikums < 0:
                    atlikums = 0  

            interese = atlikums * (self.gada_procenti / 12)
            atmaksas_summa = self.menesa_maksa - interese
            atlikums -= atmaksas_summa
            if atlikums < 0:
                atmaksas_summa += atlikums
                atlikums = 0

            self.atmaksas_grafiks.append((menesis, round(interese, 2), round(atmaksas_summa, 2), round(atlikums, 2)))
            
            self._kopeja_summa += interese + atmaksas_summa
            self._kopeja_intereses_summa += interese

            if atlikums <= 0:
                break 

    def kopeja_summa(self):
        return round(self._kopeja_summa, 2) # Tas, ko mēs samaksājam kopā
              

    def kopeja_intereses_summa(self):
        return round(self._kopeja_intereses_summa, 2)
    
    def interese_procentuali(self):
        return round((self.kopeja_intereses_summa() / self.pamatsumma) * 100, 2)
    
    def koeficients(self): # cik jāmaksā par katru aizņemto eiro
        return round(self.kopeja_summa() / self.pamatsumma, 4)

def nokopet_grafiku(grafiks):
    return [(m, i, s, a) for m, i, s, a in grafiks] # m - mēnesis; i - procentu maksājums; s - summa, kas iet nost no parāda; a - atlikusī kredīta daļa

def izveidot_excel_failu(kredits1, kredits2, kredits1_bez, kredits2_bez, menesis=None, summa=None, faila_vards="kreditu_salidzinasana.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Kredītu salīdzinājums"

    # Virsraksti pamatinformācijai
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

    max_rindu = max(len(kredits1_bez), len(kredits2_bez)) # Lai saprastu, cik rindu jāizveido Excel

    # Virsraksti atmaksas grafika tabulai
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
        rinda = [i + 1]

        if i < len(kredits1_bez):
            rinda.extend(kredits1_bez[i][1:]) # Ņem pēdējos 3 laukus bez mēneša nr.
        else:
            rinda.extend(["", "", ""])

        if i < len(kredits2_bez):
            rinda.extend(kredits2_bez[i][1:])
        else:
            rinda.extend(["", "", ""])

        ws.append(rinda)

    # Ja grafiki ar un bez papildiemaksām atšķiras, tad bija papildiemaksas
    ir_papildus_iemaksas = (      
        kredits1.atmaksas_grafiks != kredits1_bez or
        kredits2.atmaksas_grafiks != kredits2_bez
    ) 

    # Vai papildiemaksa definēta ar mēnesi un summu
    if ir_papildus_iemaksas:
        if menesis is not None and summa is not None:
            nosaukums = f"Pēc papildiemaksas ({menesis}, {summa})"
        else:
            nosaukums = "Pēc papildiemaksas"
        ws_2 = wb.create_sheet(nosaukums)
    
        max_rindu_2 = max(len(kredits1.atmaksas_grafiks), len(kredits2.atmaksas_grafiks))

        ws_2.append([
            "Mēnesis",
            f"{kredits1.nosaukums} - Interese",
            f"{kredits1.nosaukums} - Summa, kas iet nost no parāda",
            f"{kredits1.nosaukums} - Atlikums",
            f"{kredits2.nosaukums} - Interese", 
            f"{kredits2.nosaukums} - Summa, kas iet nost no parāda",
            f"{kredits2.nosaukums} - Atlikums"
        ])                

        for i in range(max_rindu_2):
            rinda = [i + 1]

            if i < len(kredits1.atmaksas_grafiks):
                rinda.extend(kredits1.atmaksas_grafiks[i][1:])
            else:
                rinda.extend(["", "", ""])
            
            if i < len(kredits2.atmaksas_grafiks):
                rinda.extend(kredits2.atmaksas_grafiks[i][1:])
            else:
                rinda.extend(["", "", ""])

            ws_2.append(rinda)

    wb.save(faila_vards)
    print(f"Dati saglabāti failā '{faila_vards}'.")        
              
def main():
    kredits1 = informacija_par_kreditu(1)
    kredits2 = informacija_par_kreditu(2)

    kredits1.aprekina_atmaksas_grafiku()
    kredits2.aprekina_atmaksas_grafiku()

    kredits1_bez = nokopet_grafiku(kredits1.atmaksas_grafiks)
    kredits2_bez = nokopet_grafiku(kredits2.atmaksas_grafiks)

    atbilde = input(f"Vai vēlaties kādā mēnesī veikt papildus iemaksu kredītiem (jā/nē)? ").strip().lower()
    menesis = None
    summa = None

    if atbilde == "jā":
        menesis = int(input("Kurā mēnesī vēlaties veikt papildiemaksu? "))
        summa = float(input("Cik euro iemaksāsiet papildus? "))
        kredits1.pievienot_papildus_iemaksu(menesis, summa)
        kredits2.pievienot_papildus_iemaksu(menesis, summa)

        kredits1.aprekina_atmaksas_grafiku(sakt_no_menesa=menesis) # pēc papildiemaksas
        kredits2.aprekina_atmaksas_grafiku(sakt_no_menesa=menesis) # pēc papildiemaksas

    izveidot_excel_failu(kredits1, kredits2, kredits1_bez, kredits2_bez, menesis=menesis, summa=summa)

    print("\nSalīdzinājums:")

    kredits1_koeficients = kredits1.koeficients()
    kredits2_koeficients = kredits2.koeficients()

    if kredits1_koeficients < kredits2_koeficients:
        print(f"Kredīts '{kredits1.nosaukums}' ir izdevīgāks, skatoties pēc atmaksas efektivitātes.")
    else:
        print(f"Kredīts '{kredits2.nosaukums}' ir izdevīgāks, skatoties pēc atmaksas efektivitātes.")

if __name__ == "__main__":
    main()