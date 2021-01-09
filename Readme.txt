Návod pro spouštění SW pro RasACam (Raspberry Astronomy Camera)
--------------------------------------------------------------

Historie verzí:

Verze 1.01
Dodělán progress bar pro zobrazení v jaké časové fázi je průběh snímání oblohy 
(expoziční čas x počet expozic)

Verze 1.0
První funkční aplikace

------------------------

Instalace:
1. Rozbalíte stažený soubor RasACam.zip v Downloads složce. Spustíte skript 
"./rasacam.sh" (pokud nelze spustit nastavíme práva příkazem "chmod +x rasacam.sh"), 
který vytvoří adresáře RasACam, als, scan a work a zkopíruje všechny 
rozbalené soubory do adresáře RasACam. Následně nainstaluje DCRAW 
s potřebnými knihovnami a nainstaluje ImageMagick.
2. Stáhněte si program ALS do složky RasACam, rozblate jej a přejmenujte složku na "als" a program na "als" z github: https://github.com/gehelem/als

Spuštění
3. Přepněte se do adresáře RasACam a pustíte příkaz v terminálu 
"python3 cam.py", který spustí GUI RasACam a program ALS. V programu ALS
nastavte cestu k pracovní složce als_jobs/scan a /work.

--------------------------

Pro ruční ovládání použijte následující skripty:

1. Pro zaostření na daný objekt nebo nastavení kompozice spostíme skript 
./foc.sh x, kde x je rovno 0 při plném rozlišení, nebo 1, při výřezu 0,25x.

Příklad:
./foc.sh 0 je rozlišení 640x480 pix
./foc.sh 1 je výřez 1/4 standardního rozlišení kamery ze středu pole.

2. Pro samotné pořizování snímků nejprve spustíme program ./als (nalezneme ve 
složce als-xxx), kde nastaveníme potřebné parametry a spustíme alignment

3. Nyni spustíme skript ./pichr x y pro JPEG (případně ./picraw x y pro RAW), kde 
x je počet expozic a y je délka expozice v sekundách.

Příklad:
./pichr.sh 10 10 znamená rozlišení 2028x1520 pix, počet snímků 10, expozice 10s
./picraw.sh 10 10 znamená rozlišení 4056x3040 pix, počet snímků 10, expozice 10s

4. Po spuštění se začnou skládat jednotlivé obrázky v programu als a výsledný 
obrázek můžeme uložit (adresář work).
