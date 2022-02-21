# Delění lomených čar
Jedná se o o program, který zajistí, že úseky liniových prvků nebudou delší než zvolená délka
a případně je rozdělí na půl.

## Vstupní a výstupní data
Při spuštění programu je nutno zadat 3 argumenty.
Argument:*-f* jedná se o cestu k vstupnímu souboru. Soubor musí být .geojson.
Argument:*-l* jedná se maximální délku segmentu. Musí se jednat o kladné číslo větší než nula.
Argument:*-f* jedná se o název výstupního souboru. Soubor musí mít příponu .geojson

Spuštění může vypadat takto:
*python3 du4.py -f vstup.geojson -l 30 -o vystup.geojson*

Program po provedení výpočtů vytvoří soubor ve formátu <argument o>.geojson.

## Popis programu
Program nejdříve nastaví parametry pro spuštění programu a uloží si parametry, dále načte data ze vstupního souboru.
Třída  Segment obsahuje vždy jeden segment, tedy počáteční a koncové souřadnice, má metodu divide, která zjišťuje délku Segmentu. Pokud je delší než zadaná maximální délka vytváří dva nové segmenty a vrací seznam s dvěma segmenty, pokud je kratší vrací seznam sama sebe.
Třída Polyline obsahuje seznam segmentů, má metodu divide_long_segments, která každý segment předává do divide() třídy Segment, pokud se vrátí dva segmenty, znamená to, že segment byl delší než zadaná maximální délka a proces se opakuje, dokud se nevrátí jen jeden segment. Jako další má metodu points, která vrací souřadnice, tak aby se daly rovnou zapsat do dat, ze kterých jde vytvořit geojson.
Následuje vytvoření výstupního souboru.