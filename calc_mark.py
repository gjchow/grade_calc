def calc(lst_marks):
    if len(lst_marks) == 0:
        return ["No valid entries found"]
    out = []
    unknown = 100
    goal1 = 50
    goal2 = 85
    percentage = 0
    curr = 0
    for mark in lst_marks:
        perc, value = mark
        perc = round(float(perc), 3)
        value = round(float(value), 3)
        percentage += perc
        unknown -= perc
        if value < 1:
            curr += round(perc*value, 3)
        else:
            curr += round(perc/100*value, 3)
    out.append(f'Current mark is {round(curr, 3)}% out of {percentage}%.')
    out.append(f'Which is {round(curr*100/percentage, 3)}%.')
    if unknown > 0:
        out.append(f'{round(unknown, 3)}% of mark not yet recorded.')
        calc1 = goal1 - curr
        if calc1 < 0:
            out.append(f'Already reaching {goal1}%.')
        else:
            out.append(f'To get {goal1}%, {round(calc1*100/unknown, 3)}% is needed of the remaining {unknown}%.')
        calc2 = goal2 - curr
        if calc2 < 0:
            out.append(f'Already reaching {goal2}%.')
        else:
            out.append(f'To get {goal2}%, {round(calc2*100/unknown, 3)}% is needed of the remaining {unknown}%.')
    else:
        out.append('All 100% has been recorded .')
    return out


def is_float(num):
    try:
        float(num)
    except ValueError:
        return False
    return True
