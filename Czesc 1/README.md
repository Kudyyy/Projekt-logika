#Część 1
W tym folderze znajduje się rozwiązanie pierwszej części zadania.
Aby przetestowac program conditions.py wystarczy uruchomić skrypt test.py w tym samym folderze.
W następujący sposób:

	./test.py
	
Aby przetestować program negations.py należy zmienić w skrypcie wiersz:

	exec_str = "\npython conditions.py "+str_a+" "+str_b+" "+str_c+" "+str_d+" "+str_e+" "+str_f+" "+str_g

na

	exec_str = "\npython negations.py "+str_a+" "+str_b+" "+str_c+" "+str_d+" "+str_e+" "+str_f+" "+str_g	
Zauważymy wtedy, iż oczekiwana wartość będzie przeciwna do otrzymywanej.