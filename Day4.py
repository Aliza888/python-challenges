from num2words import num2words

def number_to_words(num):
    return num2words(num).replace(",", "").title()

print(number_to_words(123))   
print(number_to_words(6799))