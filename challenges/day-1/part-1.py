with open("input.txt") as input:

    lastNum = 1000000
    count = 0
    
    for raw_value in input:
        value = int(raw_value.rstrip())
        if value > lastNum:
            count += 1
        lastNum = value

    print(count)