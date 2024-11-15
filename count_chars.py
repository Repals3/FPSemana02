frase=str(input())

palavras=frase.split(" ")

resultado={}

for palavra in palavras:
    resultado[palavra]=len(palavra)

print (resultado)