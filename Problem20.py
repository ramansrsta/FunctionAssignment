number1 = [1, 2, 3, 5, 7, 8, 9, 10]
number2 = [1, 2, 4, 7, 9,11,14,17]
intersection = list(filter(lambda x: x in number1, number2)) 
print (intersection)