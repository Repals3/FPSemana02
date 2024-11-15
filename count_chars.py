frase=str(input("uma frase pfv? "))

palavras=frase.split(" ")

resultado={}

for palavra in palavras:
    resultado[palavra]=len(palavra)

print (resultado)