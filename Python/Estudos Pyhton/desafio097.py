def escreva(msg):
    tam = len(msg) +4
    print("~"*tam)
    print(f"  {msg}")
    print("~"*tam)



#Programa Principal
a = str(input("Digite uma frase: "))
escreva(a)