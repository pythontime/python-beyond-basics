"""
Read a file with a number on each line. Print the sum of those numbers.
"""
sum_ = 0
with open("data/input.txt") as file:
    for line in file.readlines():  # Read each line
        sum_ += int(line)

    file.seek(0)  # Move cursor back to the beginning
    contents = file.read()  # Return the whole file as a string
    print(contents)

print(f"The sum is {sum_}")
