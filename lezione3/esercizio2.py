def sum_csv(file_name):
    values = [] #variabile che salva la lista di valori che voglio sommare
    
    my_file = open(file_name, 'r')
    for line in my_file:
        elements = line.split(',')
        print(elements)#per vedere cos'è 'elements'
            
        if elements[0] != 'Date':
            date = elements[0]
            value = elements[1]
            values.append(float(value))
        somma = sum(values)

    return somma

#chiamata della funzione
print(sum_csv('shampoo_sales.csv'))