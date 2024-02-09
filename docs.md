# Conway's Game of Life

## 1. Uživatelská část

### Spuštění programu
Program se spouští z příkazové řádky pomocí Pythonu 3.8+ následujícím způsobem:

```
python main.py
```

### Ovládání
Po spuštění programu se zobrazí `Welcome to the game of life`. Po stisknutí klávesy `Enter` se zobrazí nabídka možností, které uživatel vybírá pomocí číslic `1 - 5`.  
Všechny možnosti uživatel musí potvrzovat pomocí klávesy `Enter`.

- **1**: Úprava hracího plátna
- **2**: Spusti simulaci po 10 generací
- **3**: Spusti simulaci po X generací
- **4**: Nastavení
- **5**: Vyčistit plátno (vymazat všechny buňky)
- **6**: Nápověda stavů buněk

#### Úprava hracího plátna
Po stisknutí klávesy `1` se zobrazí editační okno plátna.
Po zadání souřadnic buňky (řádek, sloupec) se buňka na daných souřadnicích změní na opačný stav (živá/mrtvá).
Ukončení editace se provede stisknutí `0`.

#### Nastavení
Po stisknutí klávesy `4` se zobrazí nabídka možností, které uživatel vybírá pomocí číslic `1 - 5`.
- **1**: Nutnost stisknutí klávesy `Enter` pro každou generaci.
- **2**: Ukazovat číslo generace.
- **3**: Zobrazení mezistavů mezi generacemi. (označování buněk, které zemřou/ožijí)
- **4**: Zobrazení aktualizovaného plátna.
- **5**: Nekonečné plátno (plátno bude reprezentovat povrch koule).

#### Nápověda stavů buněk
Po stisknutí klávesy `6` se zobrazí nápověda stavů buněk.\
- <span style="color:#1fb0ff;">███</span> živá buňka\
- <span style="color:#4cb716;">▓▓▓</span> buňka, která ožije v další generaci\
- <span style="color:#ea4f4a;">▓▓▓</span> buňka, krerá zemře v další generaci\
- <span style="color:#aab7b9;">▓▓▓</span> prázdná buňka

## 2. Programátorská část

### Struktura programu
- `main.py`: Hlavní spouštěcí bod programu. Obsahuje herní smyčku a zajišťuje interaktivní ovládání.
- `cell.py`: Třída `Cell` reprezentuje jednu buňku na herním plátně.
- `bcolors.py`: Třída `Bcolors` upravuje barvy pro text v termínálu.
### Herní logika
Herní logika je implementována podle pravidel hry Conway's Game of Life. 
Každá buňka na plátně má dva stavy - živý nebo mrtvý. 
Na základě počtu živých sousedů buňka buď přežije do další generace, nebo zemře.\
Pravidla:
- Každá živá buňka s méně než dvěma živými sousedy zemře.
- Každá živá buňka se dvěma nebo třemi živými sousedy zůstává žít.
- Každá živá buňka s více než třemi živými sousedy zemře.
- Každá mrtvá buňka s právě třemi živými sousedy oživne.

## 3. Ukázky použití

### Příklad spuštění
Po spuštění programu se zobrazí herní plátno s náhodně vygenerovaným stavem buněk. Uživatel může interagovat s hrou pomocí klávesnice podle výše uvedených instrukcí.

### Příklad ovládání
