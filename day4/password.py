def checker(password, part1=True):
    return (digits_increase(password) and 
            contains_double(password, part1))

def correct_length(password):
    return len(str(password)) == 6

def digits_increase(password):
    pw = str(password)
    if correct_length(pw):
        for i in range(5):
            if pw[i] > pw[i+1]:
                return False
        return True
    return False

def is_doubled(password, number, part1):
    if part1:
        return password.count(str(number)) >= 2
    return password.count(str(number)) == 2


def contains_double(password, part1=True):
    p = str(password)
    for i in range(10):
        if is_doubled(p, i, part1):
            return True
    return False

if __name__ == '__main__':
    pt1 = 0
    pt2 = 0
    lower = 264793
    upper = 803935
    for input in range(lower, upper):
        if checker(input, True): pt1+=1
        if checker(input, False): pt2+=1
    print("Part 1: ", pt1)
    print("Part 2: ", pt2)