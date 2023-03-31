print('''
+ add
- substraction
* multiply
/ divison
''')
value1=int(input('Enter The Value 1='))
value2=int(input('Enter The Value 2='))
sign=input('Enter The sign=')
if sign=='+':
   print(value1+value2)
elif sign=='-':
   print(value1-value2)
elif sign=='*':
	print(value1*value2)
elif sign=='/':
	print(value1/value2)
else:
		print('value error')
