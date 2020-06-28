def func_compute(n):
 return lambda x : x * n

result = func_compute(4)
print(result(2))