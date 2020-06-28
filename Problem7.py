def upperAndLowerTester(inputString):
    dictionary={"numberOfUpper":0, "numberOfLower":0}
    for character in inputString:
        if character.isupper():
           dictionary["numberOfUpper"]+=1
        elif character.islower():
           dictionary["numberOfLower"]+=1
        else:
           pass
    print('Number of upperCase letter are' , dictionary['numberOfUpper'])
    print('Number of lowercase letter are' , dictionary['numberOfLower'])

upperAndLowerTester('The Quick Brown Fox')