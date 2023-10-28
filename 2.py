a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

if a < b and b < c:
  print(f' {b}')
elif b < a and c > b:
  print(f' {a}')
elif b > c and c > a:
 print(f' {c}')
else:
  print('Ошибка')
