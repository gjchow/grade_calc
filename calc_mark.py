def get_marks():
    marks = []
    x = ''
    while x != 'q':
        x = str(input())
        y = x.split(' ')
        if x != 'q' and len(y) == 2:
            marks.append(y)
    return marks


def calc(lst_marks):
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
    print(f'Current mark is {round(curr, 3)}% out of {percentage}%')
    print(f'Which is {round(curr*100/percentage, 3)}%')
    if unknown > 0:
        print(f'{round(unknown, 3)}% of mark not yet recorded')
        calc1 = goal1 - curr
        if calc1 < 0:
            print(f'Already reaching {goal1}%')
        else:
            print(f'To get {goal1}%, {round(calc1*100/unknown, 3)}% is needed of the remaining {unknown}%')
        calc2 = goal2 - curr
        if calc2 < 0:
            print(f'Already reaching {goal2}%')
        else:
            print(f'To get {goal2}%, {round(calc2*100/unknown, 3)}% is needed of the remaining {unknown}%')
    else:
        print('All 100% has been recorded')


m = get_marks()
# m = []
calc(m)
