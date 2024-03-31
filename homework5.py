number_input = input("Send number: ")

if not number_input.isdigit():
    print("не вірне введення!")
else:
    number = int(number_input)
    cut = 'парне' if number % 2 == 0 else 'непарне'
    print("Ви ввели", cut, "число")
