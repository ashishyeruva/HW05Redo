def classify_triangle(a,b,c):
    try:
        a, b, c = float(a), float(b), float(c)
    except ValueError:
              return "Not a valid triangle"
    
    if a <= 0 or b <= 0 or c <= 0:
         return "Not a valid triangle"
    
    if a + b <= c or b + c <= a or a + c <= b:
         return "Not a valid triangle"
    
    if a == b == c:
         return "Equilateral"
    elif a == b or b ==c or a == c:
         return "Isosceles"
    else:
         sides = [a, b, c]
         sides.sort()
         if sides[0]**2 + sides[1]**2 == sides[2]**2:
              return "Right-angled"
         else:
              return "Scalene"
         
         