from functools import reduce
 
fibonacciNumbers = lambda n: reduce(lambda x,: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
print(fibonacciNumbers(2))