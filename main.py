def is_even(num):
    return bool(num % 2 == 0)

def calculate_area(lenght, width):
    return (lenght * width )

def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Не треугольник"
    if(a == b == c):
        return "Равносторонний"
    if (a == b) or (a == c) or (b == c):
        return "Равнобедренный" 
    
    return "Разносторонний"
