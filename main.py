

numbers = [5, 20, 30, 30, 50]
delval = int(input('Enter the deletion value: '))
for i in range(len(numbers)):
    if numbers[i] == delval:
        numbers.remove(numbers[i])

# ******************************
# Make your Code
# ******************************

print (numbers)
