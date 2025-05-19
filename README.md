# Projekts – kredītu salīdzināšana
### Projekta temata izvēles pamatojums
Mācos finanšu inženieriju, tāpēc vēlējos izstrādat projekta darbu, kas sevī apvienotu gan skaitliskus aprēķinus, gan _Datu struktūras un algoritmi_ priekšmetā apgūto. Tā kā savā nākotnes profesionālajā darbā visticamāk nāksies saskarties ar _Excel_ izmantošanu, nolēmu šīprojekta izstrādes laikā apgūt un praktiski pielietot 'openpyxl' bibliotēku.


## Projekta uzdevums
Projekta mērķis bija izveidot programmu, kas, balstoties uz lietotāja ievadīto informāciju veic aprēķinus un salīdzina divus kredītus.

Lietotājam ir arī iespēja apskatīties un izvērtēt, kā papildus iemaksas konkrētā mēnesī ietekmētu kredītu atmaksas grafiku.

Aprēķinātie un apkopotie rezultāti tiek saglabāti _Excel_ failā `kreditu_salidzinasana`.
### Programmas darbības apraksts
1. Lietotājs ievada informāciju par diviem kredītiem:
   - kredīta nosaukums;
   - aizņēmuma summa euro;
   - gada procentu likme %;
   - termiņš mēnešos.
2. Programma aprēķina:
   - anuitāti;
   - katra mēneša procenta maksājumu;
   - par cik samazinās kredīts ik mēnesi;
   - atlikušo summu, kas jāmaksā.
3. Tiek piedāvāta iespēa ievadīt papildus iemaksas kādā no mēnešiem. Ja lietotājs izvēlas to darīt, tad samazinās kopējās procentu izmaksas un atmaksas ilgums.
4. Rezultāti tiek saglabāti _Excel_ failā `kreditu_salidzinasana.xlsx`, kurā ir:
   – tabula ar bāzes informāciju par abiem kredītiem;
   – kredītu atmaksu grafiki dalījumā pa mēnešiem;
   – atmaksas grafiks pēc papildus iemaksām (2. darba lapa), ja tādas tiek veiktas.
5. Izmantojot aizņēmuma koeficientu, tiek salīdzināts, kurš kredīts izdevīgāks.


## Izmantotā Python bibliotēka
**Openpyxl** – Python bibliotēka, kuru izmanto, lai izveidotu, rakstītu vai lasītu no _Excel_ faila.
### Pielietojums manā kodā
1. `Workbook()` – izveido jaunu _Excel_ failu.
2. `wb.active` – ļauj strādat ar pirmo darba lapu.
3. `create_sheet()` – izveido jaunu darba lapu.
4. `ws.append([])` – darba lapā pievieno rindas ar datiem.
5. `wb.save(faila_nosaukums)` – saglabā failu ar konkrēto nosaukumu.
### Kāpēc pielietota tieši šī bibliotēka?
**Openpyxl** bibliotēka tika izvēlēta, jo tā ļāva ērti izveidot un saglabāt _Excel_ failus no Python koda. Šī bibliotēka atbalsta `.xlsx` formātu, kas ir plaši izplatīts formāts tieši finanšu aprēķinos. Ievāktie dati tiek vizuāli un strukturēti attēloti tā, lai lietotājs tos varētu pārskatīt daudz vieglāk. Dati saprotami arī cilvēkiem bez programmēšanas zināšanām.


## Manis izmantotās un definētās datu struktūras
Šī projekta ietvaros tika definēta datu struktūra **rinda** jeb **_(queue)_**. Tā tika realizēta ar klasēm `Rinda` un `Mezgls_rindai`.
### Kāpēc izvēlēta rinda?
Kredīta maksājumiem ir būtiska secība, jo katrs veiktais maksājums ietekmē nākamo (svarīga hronoloģiska secība). Datu struktūra rinda ļāva pārvaldīt maksājumu grafiku tieši tādā veidā, kādā tas notiek realitātē – mēnesis seko mēnesim, un dati tiek "patērēti" šajā pašā kārtībā (FIFO princips).
Šī datu struktūtas izmantošana nodrošināja _time complexity_ O(1) tādām darbībām kā datu pievienošanai beigās un noņemšanai no sākuma.

Kodā tas redzams tieši darbībās ar papildus iemaksām. Piemēram,

Programmas izstrādei izmantotas arī citas datu struktūras – **saraksti** un **vardnīcas**.


## Programmatūras izmantošanas metodes
Programma paredzēta kredītu salīdzināšanai, ļaujot lietotājam ievadīt datus un modelēt dažādus atmaksas scenārijus, tai skaitā ar papildus iemaksām. Tā nodrošina skaidru vizualizāciju caur automatizēti ģenerētu _Excel_ failu, padarot rezultātu pārskatāmu un praktiski pielietojamu finanšu lēmumu pieņemšanā.

Projektu iespējams pielietot arī priekšmetā _Finanšu matemātika_ atsevišķu uzdevumu pārbaudei un modelēšanai.
