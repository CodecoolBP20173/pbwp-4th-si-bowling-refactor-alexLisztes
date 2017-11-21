class Score:
    spare = '/'
    strike = 'X'
    miss = '-'
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', ]


def score(game):
    result = 0
    frame = 1
    last = 0
    in_first_half = True
    for i in range(len(game)):
        if game[i] == Score.spare:
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == Score.spare:
                result += get_value(game[i + 1])
            elif game[i].upper() == Score.strike:
                result += get_value(game[i + 1])
                if game[i + 2] == Score.spare:
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if game[i].upper() == Score.strike:
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char in Score.nums:
        return int(char)
    elif char.upper() == Score.strike:
        return 10
    elif char == Score.spare:
        return 10
    elif char == Score.miss:
        return 0
    else:
        raise ValueError()
