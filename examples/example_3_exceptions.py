num = 0

try:
    inverse = 1 / num
except ZeroDivisionError:
    inverse = "not defined"

print(f"Inverse of {num} is {inverse}")
