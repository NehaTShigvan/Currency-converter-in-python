
with open('text.txt') as f:
    data = f.readlines()

dict = {}
for line in data:
    lines = line.split('\t')
    dict[lines[0]] = lines[1]

amount = int(input("Enter the amount to be converted: "))  
print("The available options to convert currency are as follows:\n")
[print(item) for item in dict.keys()]  
currency = input("Enter the name of a currency: ")    

print(f"{amount} INR is equal to {amount*float(dict[currency])} {currency}")
#type cast -->since dict value is string data type it should be converted into float 
