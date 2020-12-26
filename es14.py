print("ES.14 Questo programma secrive:")
print("- la differenza di due numeri a e b se il loro prodotto è maggiore di 10")
print("- la somma di sue numeri a e b se il loro prodotto è minore o uguale a 10")

n_a = float(input("Numero a: "))
n_b = float(input("Numero b: "))
prod= n_a * n_b

if prod == 10 or prod < 10 :
    somma = n_a + n_b
    print("Il prodotto dei due numeri forniti è ", prod, ", quindi minore o uguale a 10, e la loro somma è ", somma)
elif prod > 10 :
    diff = n_a - n_b
    print("Il prodotto dei due numeri forniti è ", prod, ", quindi maggiore di  10, e la loro differenza è ", diff)
