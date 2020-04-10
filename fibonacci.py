def perimetre(nb):
    square_1 = 0
    square_2 = 1
    square_3 = 1
    perimeter = 4

    for i in range(nb):
        perimeter += 4 * square_3
        square_1 = square_2
        square_2 = square_3
        square_3 += square_1
    return perimeter
