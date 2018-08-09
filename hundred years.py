from datetime import datetime
name= input('Enter your name: ')
age= int(input('Enter your age: '))
hundred_years=int((100-age) + datetime.now().year)
print ('Your name is %s, you are %s years old, you will be 100 years old in %s.' % (name, age,hundred_years))
