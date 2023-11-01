x = float(input("x = "))
y = float(input("y = "))
if x > 0 and y > 0:
    print(f' {x} "и" {y} "Это 1 четверти"')
elif x < 0 and y > 0:
    print(f' {x} "и" {y} "Это 2 четверти"')
elif x < 0 and y < 0:
   print(f' {x} "и" {y} "Это 3 четверти"')
elif x > 0 and y < 0:
    print(f' {x} "и" {y} "Это 4 четверти"')
