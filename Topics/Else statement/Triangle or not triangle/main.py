a = int(input())
b = int(input())
c = int(input())


def sum_of_angle(a, b, c):
    return a + b + c


if sum_of_angle(a, b, c) == 180:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
