num = 12
count = 0

for number in range(1,num+1):
    check = str(number)
    suma = 0
    
    for digit in check:
        suma += int(digit)
    if suma % 2 == 0:
        count += 1
print(count)
    


        
    


        
    