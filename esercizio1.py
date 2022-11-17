def sum_list(the_list):
    if(len(the_list)==0):
        return None; # caso in cui la lista è vuota
    risultato = 0        #bisogna scrivere dentro alla definizione della funzione altrimenti non trova la variabile; 0 perchè None non può essere sommato
    for item in the_list:
        risultato = risultato + item
    return risultato

my_list = [1,2,3,4,5]
l = sum_list(my_list)
print(l)

