import random

data = []
counter = 0
for i in range(20):
    numbers = random.randint(1, 100)
    data.append(numbers)
    if (data[i] % 2) == 0: 
        counter = counter +1
    
for i in range(len(data)):
    print(data[i])
print("Even numbers:", counter)