class Score:
    spare = '/'
    strike = 'X'
    miss = '-'
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    maxScore = 10
    missScore = 0


TOTAL_NUMBER_OF_FRAMES = 10


def score(game):
    result = 0
    frame = 1
    last = 0
    in_first_half = True
    for i in range(len(game)):
        result = CalculateScore(game, i, last, result)
        if frame < TOTAL_NUMBER_OF_FRAMES and get_value(game[i]) == Score.maxScore:
            result = CalculateScoreIfLastWasTotalled(game, i, result)
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
        if game[i].upper() == Score.strike:
            in_first_half = True
            frame += 1
    return result


def CalculateScore(game, i, last, result):
    if game[i] == Score.spare:
        result += Score.maxScore - last
    else:
        result += get_value(game[i])
    return result


def CalculateScoreIfLastWasTotalled(game, i, result):
    result += get_value(game[i + 1])
    if game[i].upper() == Score.strike:
        if game[i + 2] == Score.spare:
            result += Score.maxScore - get_value(game[i + 1])
        else:
            result += get_value(game[i + 2])
    return result


def get_value(char):
    if char in Score.nums:
        return int(char)
    elif char.upper() == Score.strike or char == Score.spare:
        return Score.maxScore
    elif char == Score.miss:
        return Score.missScore
    else:
        raise ValueError()
