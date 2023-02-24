# || Pattern 01 || Square Stars ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= star:
        print("*", end = " ")
        col +=1 
    print()
    row += 1

# || Pattern 02 || Square Row Numbers ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= star:
        print(row, end = " ")
        col +=1 
    print()
    row += 1

# || Pattern 03 || Square Column Numbers ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= star:
        print(col, end = " ")
        col +=1 
    print()
    row += 1

# || Pattern 04 || Square Reverse Column Numbers ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= star:
        print(star - col + 1 , end = " ")
        col +=1 
    print()
    row += 1

# || Pattern 05 || Square Searial Numbers ||
star = int(input("Enter the stars number of a row :-"))
row = 1
count = 1
while row <= star:
    col = 1
    while col <= star:
        print(count, end = " ")
        count += 1
        col += 1
    print()
    row += 1

# || Pattern 06 || Triangle Stars ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= row:
        print("*", end = " ")
        col += 1
    print()
    row += 1

# || Pattern 07 || Triangle Row Numbers ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= row:
        print(row, end = " ")
        col += 1
    print()
    row += 1

# || Pattern 08 || Matrix ||
N = int(input("Enter a number between 1 to 9 :-"))
for row in range(2 * N - 1):
    for col in range(2 * N - 1):
        top = row
        left = col
        right = (2 * N - 2) - col
        bottom = (2 * N - 2) - row
        print(N - min(min(top, bottom), min(left, right)), end = " ")
    print()

# || Pattern 09 || Triangle Column Increment Numbers || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    value = row
    while col <= row:
        print(value, end = " ")
        value += 1
        col += 1
    print()
    row += 1

# # || Pattern 09 || Another Way Withoust Local Variable || Homework || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= row:
        print((row + col) - 1 , end = " ")
        col += 1
    print()
    row += 1

# || Pattern 10 || Triangle Column Decrement Numbers || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= row:
        print((row - col) + 1 , end = " ")
        col += 1
    print()
    row += 1

# || Pattern 11 || Square Capital Letter AAA || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= star:
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(char[row - 1] , end = " ")
        col += 1
    print()
    row += 1

# || Pattern 11 || Square Capital Letter ABC || Homework ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= star:
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(char[col - 1] , end = " ")
        col += 1
    print()
    row += 1

### || Pattern 11 || Square Capital Letter AB - CD || Homework ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    start = 0
    while col <= star:
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(char[start] , end = " ")
        start += 1
        col += 1
    print()
    row += 1

# || Pattern 12 || Square Column Increment Numbers || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= star:
        print((row + col) - 1 , end = " ")
        col += 1
    print()
    row += 1

# || Pattern 13 || Square Column Increment ABC || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= star:
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(char[row + col - 2] , end = " ")
        col += 1
    print()
    row += 1

# || Pattern 14 || Triangle Column Increment A - BB || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= row:
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(char[row - 1] , end = " ")
        col += 1
    print()
    row += 1

# || Pattern 15 || Triangle Column Increment A - BC - CDE || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= row:
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(char[row + col - 2] , end = " ")
        col += 1
    print()
    row += 1

# || Pattern 16 || Triangle Column Decrement B - AB || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= row:
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(char[star - row] , end = " ")
        col += 1
    print()
    row += 1

# || Pattern 17 || Triangle Column Decrement B - AB || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    while col <= row:
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(char[star - row] , end = " ")
        col += 1
    print()
    row += 1

### || Pattern 18 || Square increasing(Stars) + decreasing(Spaces) || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    space = star - row
    while space:
        print(" ")
        space -= 1
    col = 1
    while col <= row:
        print("*" , end = " ")
        col += 1
    print()
    row += 1

# || Pattern 19 || Triange Star Decrement ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    print_star = star - row + 1
    while col <= print_star:
        print("*" , end = " ")
        col += 1
    print()
    row += 1

### || Pattern 20 || Square decreasing(Stars) + increasing(Spaces) || Homework ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    col = 1
    print_star = star - row + 1
    while col <= print_star:
        print("*", end = " ")
        col += 1
    space = star - row
    while space:
        print("")
        space -= 1
    print()
    row += 1

# || Pattern 21 || Triangle increasing(Space) + decreasing(Numebers) 11 - 2 || Homework ||
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    space = 1
    while space <= row:
        print("", end = " ")
    space += 1
    col = 1
    while col <= star:
        print(row , end = " ")
        col += 1
    print()
    row += 1 

# || Pattern 22 || Triangle decreasing(Space) + increasing(Numebers) 1 - 22 || Homework ||

# || Pattern 23 || Triangle increasing(Space) + decreasing(Numebers) 123 - 23 - 3 || Homework ||

# || Pattern 24 || Triangle decreasing(Space) + increasing(Numebers) 1 - 23 - 456 || Homework ||

# || Final Pattern 25 || 
star = int(input("Enter the stars number of a row :-"))
row = 1
while row <= star:
    # First Triange Numbers
    col1 = star
    while col1 >= row:
        print(col1, end = " ")
        col1 -= 1
    # Second Triange Stars
    col2 = 1
    star1 = row - col2
    while col2 <= star1:
        print("*", end = "")
    # Third Triange Numbers
    print()
    row += 1

