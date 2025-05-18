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

## Programmatūras izmantošanas metodes
