plv1=input()
plv2=input()

intersection=set(plv1) and set(plv2)



resultado=""

for car in plv1:
    if car in intersection and car not in resultado:
        resultado+=car

print(resultado)
print(intersection)