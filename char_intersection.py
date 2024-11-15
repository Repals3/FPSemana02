plv1=input("first word? ")
plv2=input("second word? ")

intersection=set(plv1) and set(plv2)



resultado=""

for car in plv1:
    if car in intersection and car not in resultado:
        resultado+=car

print(resultado)
print(intersection)