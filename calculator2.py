def my_sum(a, b):
    result = a + b
    print(f"a + b = {result}")

def my_sub(a, b):
    result = a - b
    print(f"a - b = {result}")

def my_mul(a, b):
    result = a * b
    print(f"a * b = {result}")

def my_div(a, b):
    if b != 0:
        result = a / b
        print(f"a / b = {result}")
    

def my_calculator():
    a = int(input("Adade aval ro vared konid:\n"))
    b = int(input("Adade dovom ro vared konid:\n"))
    operator = input("Amalgar (jam: +, tafrigh: -, zarb: *, tagsim: /) ro vared konid:\n")

    if operator == "+":
        my_sum(a, b)
    elif operator == "-":
        my_sub(a, b)
    elif operator == "*":
        my_mul(a, b)
    elif operator == "/":
        my_div(a, b)
    else:
        print("Algoritme morede nazar poshtibani nemishavad!")

# فراخوانی تابع
my_calculator()
