# Słowotok solver
Program służy do rozwiązywania łamigłówki [Słowotok](https://slowotok.pl/). Z podanej tablicy słów znajduje wszystkie możliwe do utworzenia słowa, zgodnie z [zasadami gry](https://slowotok.pl/cms/pl/jak_grac).

## Używanie
Do poprawnego używania programu, potrzebna jest następująca struktura plików:
```
./dictionary.py
./settings.py
./slowotok.py
./solver.py
./trie.py
./data/gra.html
./data/slowa.txt
```

Uruchom plik `solver.py`. 

Tuż po uruchomieniu pojawi się informacja, że ładowane są wyrazy ze słownika. Po wypełnieniu się paska postępu, wyświetla się informacja o prawidłowym załadowaniu słownika i program zaczyna oczekiwać na dane do gry.

Komunikat `Czekanie na dane...` oznacza, że program czeka na klawisz użytkownika (enter). Po kliknięciu, program rozpoczyna pobieranie danych 
- z serwera slowotok.pl (domyślnie)
- z pliku `./data/gra.html` - w pliku powinna znajdować się strona html aktualnej planszy gry

Na ekranie pojawi się wizualizacja planszy gry oraz wypisane zostaną wszystkie słowa, które można uzyskać z planszy i które znajdują się w słowniku języka polskiego. Są posortowane względem długości.

Po wypisaniu wszystkich drzwi, program się zapętla i ponownie czeka na klawisz użytkownika. W tym czasie można podmienić plik z informacją o aktualnej grze albo poczekać na rozpoczęcie nowej gry (w przypadku pobierania danych z serwera).

## Implementacja
### Tworzenie słownika
Zgodnie z [FAQ](https://slowotok.pl/faq/ogolne) Słowotoku, gra wykorzystuje słowa SJP. W związku z tym używam bazy słów do gier udostępnianej przez serwis SJP dostępnej [tutaj](https://sjp.pl/slownik/growy/). Niestety, baza ta zawira nadzbiór słów używanych w grze, poszerzony w szczególności o odmiany rzeczowników ze względu na przypadki.

Ze wszystkich słów tworzone jest drzewo trie. 

### Szukanie wyrazów 
Szukanie wyrazów na planszy jest dokonywane przy użyciu algorytmu z powrotami. Równocześnie podczas sprawdzania wszystkich możliwych permutacji liter, chodzimy po wcześniej utworzonym drzewie. Jeśli  w drzewie nie istnieje dziecko posiadające literę, którą chcemy wybrać to znaczy, że nie istnieje żaden wyraz posiający taką sekwencję znaków. Wobec tego nie musimy sprawdzać wariantu zawierającego analizowaną literę.

Z racji ograniczeń słownika i zadad gry, maksymalna długość słowa wyn. 15. Stąd stos może zawierać co najwyżej 15 wywołań rekurencyjnych.
