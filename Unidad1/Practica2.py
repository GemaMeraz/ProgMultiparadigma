#Practica 2 
lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"] 

for i in range(len(lista),1,-1): 
    if i % 3 ==0: 
        lista.pop(i -1) 
        print(lista) 