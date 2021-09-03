def check_float(number):
    if number - int(number) > 0:
        return int(number) + 1
    return int(number) 

def solution(X, Y, D):
    if X == Y:
        return 0
    else:
        distance = int(Y - X)
        division = distance / D
        return check_float(division)
