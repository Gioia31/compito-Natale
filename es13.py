print("Con questo programma puoi verificare se un numero è pari o dispari")
n_utente = int(input("Inserisci il numero: "))
p_d = n_utente % 2 #vedo se la divisione n:2 ha resto o no, il che determina se è p o d

if p_d == 0 :
    print("Il numero ", n_utente, " è pari")
else:
    print("Il numero ", n_utente, " è dispari")
