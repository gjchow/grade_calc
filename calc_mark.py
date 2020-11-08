from typing import Any, List


def calc(lst_marks: List) -> List[str]:
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
        if '/' in value:
            value = value.split('/')
            value = float(value[0])/float(value[1])
            value = round(float(value), 3)
        else:
            value = round(float(value)/100, 3)
        percentage += perc
        unknown -= perc
        curr += round(perc*value, 3)
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


def is_float(num: Any) -> bool:
    try:
        float(num)
    except ValueError:
        if '/' in num:
            try:
                num = num.split('/')
                if len(num) != 2:
                    return False
                else:
                    float(float(num[0])/float(num[1]))
            except ValueError:
                return False
    return True