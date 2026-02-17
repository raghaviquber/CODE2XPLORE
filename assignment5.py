weights=[]
n=int(input("Enter the number of weights: "))
for i in range(n):
    w=int(input("Enter weight "+str(i+1)+": "))
    weights.append(w)
invalid_entry=[]
very_light=[]
normal_load=[]
overloaded=[]
heavy_load=[]
for w in weights:
    if w<0:
        invalid_entry.append(w)
    elif 0<= w<=5:
        very_light.append(w)
    elif 6<=w<=25:
        normal_load.append(w)
    elif 26<=w<=60:
        heavy_load.append(w)
    elif w>60:
        overloaded.append(w)
name=input("enter your full name: ")
L=0
for i in name:
    if i!=" ":
        L+=1
PLI= L%3
affected=0
print("PLI: ",PLI)
print("length of name: ",L)
if PLI==0:
    for i in overloaded:
        invalid_entry.append(i)
        affected+=1
    overloaded=[]
    print("Applied rule:A")
    print("Invalid entries: ",invalid_entry)
    print("Very light loads: ",very_light)
    print("Normal loads: ",normal_load)
    print("Heavy loads: ",heavy_load)
elif PLI==1:
    for i in very_light:
        affected=affected+1
    very_light=[]
    print("Applied rule:B")
    print("Invalid entries: ",invalid_entry)
    print("normal loads: ",normal_load)
    print("Heavy loads: ",heavy_load)
    print("Overloaded: ",overloaded)
elif PLI==2:
    for i in very_light:
        affected=affected+1
    for i in overloaded:
        affected=affected+1
    for i in invalid_entry:
        affected=affected+1
    very_light=[]
    overloaded=[]
    invalid_entry=[]
    print("Applied rule:C")
    print("normal loads: ",normal_load)
    print("Heavy loads: ",heavy_load)
total_valid = 0

for i in very_light:
    total_valid += 1
for i in normal_load:
    total_valid += 1
for i in heavy_load:
    total_valid += 1
for i in overloaded:
    total_valid += 1

print("Total valid weights:", total_valid)

print("Affected items: ",affected)
