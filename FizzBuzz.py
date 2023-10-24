# Function to calculate if the number is multiple of the chosen ones.
def logic(a, b, x, y, num):
    c = a + b
    if (num % x == 0) and (num % y == 0):
        return f"{c}"
    elif (num % x == 0):
        return f"{a}"
    elif (num % y == 0):
        return f"{b}"
    else:
        return num
#____________________________________________________________________
#TITLE
print("---------------------FIZZ BUZZ---------------------\n\n"
      "This is a logic that shows numbers from 1 to N,\n"
      "by default, numbers divisible by 3 are replaced by the word Fizz, \n"
      "while numbers divisible by 5 are replaced by Buzz.\n"
      "Also, if the number is divisible by 3 AND 5,\n"
      "it will be replaced by the whole word combined, FizzBuzz\n\n")
#___________________________________________________________________________
#User inputs
n = int(input("Type the size of the list: "))
a = input("\nType what you want to be the first word: ")
b = input("\nType what you want to be the second word: ")
x = int(input(f"\nType which number you want to be divisible for the word {a}: "))
y = int(input(f"\nType which number you want to be divisible for the word {b}: "))
#_________________________________________________________________________________
#List Creation
nums = []
for i in range(n):
    i += 1
    nums.append(i)
answr = []
for i in nums:
    answr.append((logic(a, b, x, y, i)))
#________________________________________
#List printing
print("\nThe list is as follows:\n")
print(answr)
#__________________________________________