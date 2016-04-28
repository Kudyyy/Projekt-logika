#Część 2
W tym folderze znajduje się rozwiązanie drugiej części zadania.
Folder ten zawiera plik game.py który jest grą.
Grę uruchamia się w następujący sposób:

	./game.py --and and.txt --or or.txt --not not.txt --impl impl.txt
	
 W razie podania niepoprawnych argumentów program wypisze stosowny komunikat.
Gra ta obsługuje logike wielowartościową.
Pliki jakie znajdują się z grą posiadają zapisaną logike trójwartościową.
Gra umożliwia w łatwy sposób zmianę symboli dla funkcji logicznych poprzez zmienną *symbols*, zmianę dopuszczalnych nazw opcji *availableOptions* oraz zmianę dopuszczalnych nazw plików *mandatoryFilesName*.
