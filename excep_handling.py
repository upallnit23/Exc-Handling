#Exceptional Weather Forecast

#Task 1: Start

fahrenheit_temp = input("Enter the temperature in fahrenheit: ")
if fahrenheit_temp.isdigit():
    print(f"You entered {fahrenheit_temp} degrees fahrenheit.") 
else:
    print("Value entered is not numeric. ")

try:
    fahrenheit_temp = input("Enter the temperature in fahrenheit: ")
except Exception as e:
    print(e)
    #print("Cannot divide by zero. ")
else: 
    #no
    #fahrenheit_temp.isdigit():
    print(f"You entered {fahrenheit_temp} degrees fahrenheit.") 
#else:
    #print("Value entered is not numeric. ")


#Task 2 and 3: Temperature Conversion and User Experience

try:
    fahrenheit_temp = int(fahrenheit_temp)
    calc_temp = (fahrenheit_temp - 32) * (5/9)
except ZeroDivisionError:
    print("Cannot divide by zero. ")
except Exception as e:
    print(e)
else:
    print(f"The temperature in fahrenheit is {fahrenheit_temp}.")
    print(f"The temperature in celsius is {round(calc_temp)}.")
finally:
    print("Thank you for using this app.")

#The Recipe Ratio Adjuster - all tasks assigned

try:
    recipe_serves = int(input("Enter the original number of servings from the recipe: "))
except ValueError:
    print("Input enter is not a number. ")
else:
    print(f"The amount of servings entered is {recipe_serves}. ")

try:
    recipe_cserves = int(input("Enter the number of servings you want: "))
except ValueError as e:
    print(e)
else:
    print(f"The amount of servings entered is {recipe_cserves}.")
    recipe_adjserves = round(recipe_serves / recipe_cserves)
finally:
    print(f"This recipe has been adjusted to {recipe_adjserves}")







