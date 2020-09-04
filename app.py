from flask import Flask, render_template, request
from calc_mark import calc, is_float
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    info = ''
    if request.method == 'POST':
        req = request.form
        num = len(req)//2
        marks = []
        for i in range(num):
            temp = [req.get('mark'+str(i+1)), req.get('percent'+str(i+1))]
            marks.append(temp)
        to_remove = []
        print(marks)
        for mark in marks:
            if mark[0] == '' or mark[1] == '':
                to_remove.insert(0, marks.index(mark))
            elif not is_float(mark[0]) or not is_float(mark[1]):
                to_remove.insert(0, marks.index(mark))
        for i in to_remove:
            marks.pop(i)
        info = calc(marks)
    return render_template('index.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)
