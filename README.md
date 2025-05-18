# Projekts – kredītu salīdzināšana
### Projekta temata izvēles pamatojums
Mācos finanšu inženieriju, tāpēc vēlējos izstrādat projekta darbu, kas sevī apvienotu gan skaitliskus aprēķinus, gan _Datu struktūras un algoritmi_ priekšmetā apgūto. Tā kā savā nākotnes profesionālajā darbā bieži nāksies saskarties ar _Excel_ izmantošanu, nolēmu šo projektu izmantot kā iespēju labāk apgūt un praktiski pielietot 'openpyxl' bibliotēku.

## Projekta uzdevums
Projekta mērķis bija izveidot programmu, kas, balstoties uz lietotāja ievadīto informāciju – aizņēmuma apjomu (eiro), gada procentu likmi un atmaksas termiņu (mēnešos), veic aprēķinus. Pēcāk tiek izveidots _Excel_ fails, kurā abi kredīti tiek salīdzināti pēc kopējās atmaksas summas, procentuālā intereses apjoma no aizņēmuma summas, anuitātes un aizņēmuma koeficienta.

Papildus lietotāja var simulēt papildus iemaksas konkrētā mēnesī, lai redzētu, kā tās ietekmē kredīta atlikumu, atmaksas ilgumu un kopējo samaksāto summu.

Visi rezultāti tiek saglabāti _Excel_ failā `kreditu_salidzinasana`, kur iespējams ērti pārskatīt un salīdzinat abu kredītu atmaksas grafikus – gan sākotnējos, gan pēc papildu iemaksu veikšanas.

Projektu iespējams pielietot arī priekšmeta _Finanšu matemātika_ atsevišķu uzdevumu pārbaudei un modelēšanai.
### Galvenie uzdevumi
1. Ievākt informāciju no lietotāja – kredīta nosaukums, pamatsumma (euro), gada procentu likme, termiņš (mēnešos).
2. Aprēķināt anuitātes maksājumu un atmaksas grafiku.
3. Apstrādāt papildus veiktās iemaksas un to ietekmi uz kredītu atmaksu.
4. Ierakstīt un saglabāt iegūtos un aprēķinātos datus _EXCEL_ formātā.

## Izmantotā Python bibliotēka
**Openpyxl** – Python bibliotēka, kuru izmanto, lai izveidotu, rakstītu vai lasītu no _Excel_ faila.
### Pielietojums manā kodā
1. `Workbook()` – izveido jaunu _Excel_ failu.
2. `wb.active` un `create_sheet()` – izveido darba lapas.
3. `ws.append([])` – darba lapā pievieno rindas ar datiem.
4. `wb.save(faila_nosaukums)` – saglabā failu ar konkrēto nosaukumu.
### Kāpēc pielietota tieši šī bibliotēka?
**Openpyxl** bibliotēka tika izvēlēta, jo tā ļāva ērti izveidot un saglabāt _Excel_ failus no Python koda. Šī bibliotēka atbalsta `.xlsx` formātu, kas ir plaši izplatīts formāts tieši finanšu aprēķinos, ievāktie dati tiek vizuāli un strukturēti attēloti tā, lai lietotājs tos varētu pārskatīt daudz vieglāk. Dati saprotami arī cilvēkiem bez programmēšanas zināšanām.

## Manis izmantotās un definētās datu struktūras
Šī projekta ietvaros tika definēta un izmantota pašveidota **rinda** **_(queue)_**, ko realizēju ar klasēm `Rinda` un `Mezgls_rindai`. Rinda tika izveidota, lai saglabātu un apstrādātu datus par kredīta maksājumiem to hronoloģiskajā secībā. Šāda datu struktūra ļāva pārvaldīt maksājumu grafiku tieši tādā veidā, kādā tas notiek realitātē – mēnesis seko mēnesim, un dati tiek "patērēti" šajā pašā kārtībā (FIFO princips).
### Kāpēc izvēlēta rinda?
Kredīta maksājumiem ir būtiska secība, jo katrs veiktais maksājums ietekmē nākamo. Datu struktūra rinda šo principu lieliski attēlo, izmantojot to pašu loģiku – pirmais tiek izņemts pirmais maksājums, nākamie seko.
Šī datu struktūtas izmantošana nodrošināja _time complexity_ O(1) tādām darbībām kā datu pievienošanai un noņemšanai.

Kodā tas redzams tieši darbībās ar papildus iemaksām. Piemēram,
`while (not self.papildus_iemaksas.tuksa_rinda() and self.papildus_iemaksas.paskatit_pirmo().menesis == menesis):
                iemaksa = self.papildus_iemaksas.iznemt_elementu()`
Šeit redzams, ka katrā mēnesī tiek pārbaudīts, vai rinda nav tukša un vai pirmais elements (pirmā iemaksa) ir paredzēta šim mēnesim. Ja abi nosacījumi izpildās, tad pirmais elements (iemaksa) tiek izņemta no rindas.

Programmas izstrādei izmantotas arī citas datu struktūras – **saraksti** un **vardnīcas**.

## Programmatūras izmantošanas metodes
Programma paredzēta kredītu salīdzināšanai, ļaujot lietotājam ievadīt datus un modelēt dažādus atmaksas scenārijus, tai skaitā ar papildus iemaksām. Tā nodrošina skaidru vizualizāciju caur automatizēti ģenerētu _Excel_ failu, padarot rezultātu pārskatāmu un praktiski pielietojamu finanšu lēmumu pieņemšanā.
