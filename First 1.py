# First Simple Project:

# Rehan = 10
# Abid = 5
# rating = 4.9
# name = 'Rehan'
# is_published = Ture
# print(Rehan + Abid)



# Input 2 Project:

# name = input('What is your name? ')
# print('Hi ' + name)

# name = input('What is your name ?: ')
# f_c = input('What is your favorite color ?: ')
# print(name + ' likes ' + f_c + ' color')


# Number Input 3 Project:

# Birth_Year = input('What is Your Date of Birth ?: ')
# age = 2022 - int(Birth_Year)
# print(age)

# Type Of Thing 4 Project:

# Birth_Year = input('What is Your Date of Birth ?: ')
# print(type(Birth_Year))
# age = 2022 - int(Birth_Year)
# print(type(age))
# print(age)



# Kg Into Lbs 5 Project

# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)


# Use Of ('') into sentance 6 Project:

# course = "Python's Course for Beginners"
# print(course)


# Words Number 7 Project:

# course = "Python's Course for Beginners"
# print(course[28])

# course = "Python's Course for Beginners"
# print(course[-1])

# course = "Python's Course for Beginners"
# print(course[0:2])


# In A Full Message 8 Project:

# First = 'Rehan'
# Last = 'Bhatti'
# message = First + ' [' + Last + '] is a Programmer'
# print(message)

# First = 'Rehan'
# Last = 'Bhatti'
# msg = f'{First} [{Last}] is a Programmer'
# print(msg)


# Count Word 9 Project:

# course = 'Python For Beginners'
# print(len(course))

# course = 'Python For Beginners'
# print(course.upper())

# course = 'Python For Beginners'
# print(course.lower())


# Find Word 10 Project:

# course = 'Python for Beginners'
# print(course.find('0'))

# course = 'Python for Beginners'
# print(course.replace('Beginners', 'Absolute Beginners'))

# course = 'Python for Beginners'
# print(course.replace('f', 'F'))


# Ture False 11 Project:

# course = 'Python for Beginners'
# print('Python' in course)

# course = 'Python for Beginners'
# print('Pythone' in course)


# Math Equation 12 Project:

# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 == 10)
# print(10 - 3)
# print(10 + 3)
# print(10 * 3)
# print(10 ** 3)

# x = 10
# x = x + 1
# print(x)

# x = 10 + 3 * 2
# print(x )


# Round & abs 13 Project:

# x = 2.3
# print(round(x))

# x = 2.3
# print(abs(-2.9))


# if & else 14 Porject:

# is_hot = True

# if is_hot:
   # print("It's a hot day")
# else:
   # print("It's not hot day")

# is_hot = False
# is_cold = True

# if is_hot:
#    print('Its a hot day')
#    print('Drink plenty of water')
    
# elif is_cold:
#    print("It's a cold day")
#    print("Wear warm clothes")

# else:
#    print("It's a lovely day")
    
# print('Enjoy your day')


# Down Payment 15 Project:

# price = 1000000
# has_good_credit = True

# if has_good_credit:
#    down_payment = 0.1 * price
# else:
#   down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")


# AND OR 16 Project:

# has_high_income = True
# has_good_credit = True

# if has_high_income and has_good_credit:
#    print("Eligible for loan")

# has_high_income = False
# has_good_credit = True

# if has_high_income and has_good_credit:
#    print("Eligible for loan")

# has_high_income = False
# has_good_credit = True

# if has_high_income or has_good_credit:
#    print("Eligible for loan")

# Temperature 17 Project

# temperature = 30

# if temperature < 30 # > or == or !=:
#    print("It's a hot day")
# else:
#    print("It's not a hot day")


# If Elif Else 18 Project:


# name = "Rehan"

# if len(name) > 3:
#    print("Name must be at least 3 character")
# elif len(name) < 50:
#    print("Name must be a maximum of 50 charachter")
# else:
#    print("Name looks good")


# If Else With Input 19 Project:

# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#    converted = weight * 0.45
#    print(f"You are {converted} kilos")
# else:
#    converted = weight / 0.45
#    print(f"You are {converted} pounds")



# While 20 Project:

# i = 1
# while i <= 10:
#    print(i)
#    i = i + 1    
# print("Done")

# i = 1
# while i <= 10:
#    print('*' * i)
#    i = i + 1    
# print("Done")


# Guess Game 21 Project:

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#    guess = int(input('Guess: '))
#    guess_count += 1
#    if guess == secret_number:
#        print('Yon won!')
#        break
# else:
#    print('Sorry, you failed!')



# Car Game 22 Project:

# command = ""
# started = False
# while True:
#   command = input("> ").lower()
#    if command == "start":
#       if started:
#            print("Car is already started!")
#        else:
#            started = True
#            print("Car started...")
#    elif command == "stop":
#        if not started:
#            print("Car is already stopped!")
#        else:
#           started = False
#            print("Car stopped.")
#    elif command == "help":
#        print("""
#        start - to start the car
#        stop - to stop the car
#        quit - to quit
#        """)
#    elif command == "quit":
#        break
#    else:
#            print("Sorry, I don't understand that!")



# For Item 23 Project:

# for item in 'Python':
#    print(item)

# for item in ['Python', 'Css', 'Java']:
#    print(item)

# for item in range(10):
#   print(item)

# for item in range(5, 10):
#    print(item)

# for item in range(5, 10, 2):
#     print(item)


# Prices Total 24 Project:

# prices = [10, 20, 30]

# total = 0
# for price in prices:
#    total += price
# print(f"Total: {total}")


# For X

# for x in range(4):
#    print(x)

# for x in range(4):
#    for y in range(3):
#        print(f'({x}, {y})')


# For Game 24 Project:

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#    print('x' * x_count)

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#    output = ''
#    for count in range(x_count):
#        output += 'x'
#    print('x' * x_count)


# Name 25 Prject:

# names = ['Java', 'Css', 'Python', 'Html']
# print(names[3])


# Find Number In List 26 Project:

# numbers = [3, 6, 2, 8, 29, 23, 55, 22, 423, 123, 555]
# max = numbers[0]
# for number in numbers:
#    if number > max:
#        max = number
# print(max)


# Append & Insert & Remove & Clear & Pop 27 Project:

# numbers = [5, 2, 1, 7, 4]
# numbers.append(20)
# print(numbers)

# numbers = [5, 2, 1, 7, 4]
# numbers.insert(0, 10)
# print(numbers)

# numbers = [5, 2, 1, 7, 4]
# numbers.remove(7)
# print(numbers)

# numbers = [5, 2, 1, 7, 4]
# numbers.clear()
# print(numbers)

# numbers = [5, 2, 1, 7, 4]
# numbers.pop()
# print(numbers)

# numbers = [5, 2, 1, 7, 4]
# print(numbers.index(5))


# In & Count & Sort & Reverse & Copy Use 28 Project:

# numbers = [5, 2, 1, 7, 4]
# print(50 in numbers) # False

# numbers = [5, 2, 1, 7, 4]
# print(5 in numbers) # True

# numbers = [5, 2, 2, 5, 7, 4]
# print(numbers.count(5))

# numbers = [5, 2, 2, 5, 7, 4]
# print(numbers.sort())

# numbers = [5, 2, 2, 5, 7, 4]
# numbers.sort()
# print(numbers)

# numbers = [5, 2, 2, 5, 7, 4]
# numbers.sort()
# numbers.reverse()
# print(numbers)

# numbers = [5, 2, 2, 5, 7, 4]
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2)


# Remove Duplicates 29 Project:

# numbers = [2, 2, 4, 6, 3, 4 ,6, 3]
# uniques = []
# for number in numbers:
#    if number not in uniques:
#        uniques.append(number)
# print(uniques)


# X, Y, Z 30 Project:

# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(z)


# Message From & Get 31 Project:

# customer = {
#     "name": "Rehan Bhatti",
#     "age": 13,
#     "is_verified": True
# }
# print(customer["name"])

# customer = {
#     "name": "Rehan Bhatti",
#     "age": 13,
#    "is_verified": True
# }
# print(customer.get("birthdate"))
# print(customer.get("birthdate", "Aug 1 2009"))


# Phone 123 32 Project:

# phone = input("Phone: ")
# digits_mapping = {  
#        "1": "One",
#        "2": "Two",
#        "3": "Three",
#        "4": "Four",
#        "5": "Five"
# }
# output = ""
# for ch in phone:
#    output += digits_mapping.get(ch, "!") + " "
# print(output)


# Def Use 33 Project:

# def greet_user():
#    print('Hi There!')
#    print('Welcome Aboard')
#
# print("Start")
# greet_user()
# print("Finish")

# def greet_user(name):
#    print(f"Hi {name}!")
#    print('Welcome Aboard')
#
# print("Start")
# greet_user("Rehan")
# print("Finish")

# def greet_user(name):
#    print(f"Hi {name}!")
#    print('Welcome Aboard')
#
# print("Start")
# greet_user("Rehan")
# greet_user("Bhatti")
# print("Finish")

# def greet_user(first_name, last_name):
#    print(f"Hi {first_name} {last_name}!")
#    print('Welcome Aboard')
#
# print("Start")
# greet_user("Rehan", "Bhatti")
# print("Finish")


# Math Equation 34 Project:

# def square(number):
#    return number * number
# print(square(3))


# Emoji Game 35 Project:

# def emoji_converter(message):
# words = message.split(" ")
# emojis = {
#      ":)": "S",
#      "(:": "D"
# }
# output = ""
# for word in words:
#    output += emojis.get(word, word) + " "
#    return output
#
# message = input(">")
# print(emoji_converter(message))


# Except 35 Project:

# age = int(input('Age: '))
#    print(age)

# try:
#    age = int(input('Age: '))
#    print(age)
# except ValueError:
#    print('Invalid Value')

# try:
#    age = int(input('Age: '))
#    income = 20000
#    risk = income / age
#    print(age)
# except ZeroDivisionError:
#    print('Age cannot be 0.')
# except ValueError:
#    print('Invalid Value')


# Comments 36 Project:

# This is a Comment
# print("Sky is blue")
