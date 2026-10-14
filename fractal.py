def draw_pattern(x):
    print(x * "*")
    x -= 1
    if x == 0:
        return
    else:
        print(x * "*")
        draw_pattern(x)
        print((x + 1) * "*")


y = int(input("State how many times you want to make a fractal: "))
draw_pattern(y)