def evenLister(list):
    evenList = []
    for element in list:
        if element % 2 == 0:
            evenList.append(element)
    print(evenList)

evenLister([1,2,3,4,5])