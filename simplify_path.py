def dirReduit(arr):
    vertical = 0
    horizontal = 0

    for i in arr:
        if i == "NORD":
            vertical += 1
        elif i == "SUD":
            vertical -= 1
        elif i == "EST":
            horizontal += 1
        elif i == "OUEST":
            horizontal -= 1
    if vertical < 0:
        dir = ["SUD" for i in range(0, vertical, -1)]
    elif vertical > 0:
        dir = ["NORD" for i in range(vertical)]
    if horizontal < 0:
        dir += ["OUEST" for i in range(0, horizontal, -1)]
    elif horizontal > 0:
        dir += ["EST" for i in range(horizontal)]
    print(dir)
