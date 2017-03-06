import random
import tkinter as tk


def gen_bomb(field):
    i = random.randint(1, m - 1)
    j = random.randint(1, n - 1)
    while field[i][j] == 'b':
        i = random.randint(1, m - 1)
        j = random.randint(1, n - 1)
    field[i][j] = 'b'
    return field
    # if field[i][j] == 'b':
    #     return gen_field(field)
    # else:
    #     field[i][j] = 'b'
    # return field


def gen_field(field):
    for i in range(1, m):
        for j in range(1, n):
            cnt = 0
            if field[i][j] == 'b':
                continue
            else:
                if field[i - 1][j - 1] == 'b':
                    cnt += 1
                if field[i - 1][j] == 'b':
                    cnt += 1
                if field[i - 1][j + 1] == 'b':
                    cnt += 1
                if field[i][j - 1] == 'b':
                    cnt += 1
                if field[i][j + 1] == 'b':
                    cnt += 1
                if field[i + 1][j - 1] == 'b':
                    cnt += 1
                if field[i + 1][j] == 'b':
                    cnt += 1
                if field[i + 1][j + 1] == 'b':
                    cnt += 1
            field[i][j] = cnt
    return field


def opencell(i, j):
    if field[i][j] == 'b':
        for k in range(1, n):
            for l in range(1, m):
                if field[k][l] == 'b':
                    buttons[k][l]["bg"] = 'red'
                    buttons[k][l]["text"] = 'bomb'
        # exit()
    if field[i][j] == -1:
        return
    if field[i][j] == 0 and (i, j) not in walken:
        walken.append((i, j))
        opencell(i - 1, j - 1)
        opencell(i - 1, j)
        opencell(i - 1, j - 1)
        opencell(i, j - 1)
        opencell(i, j + 1)
        opencell(i + 1, j - 1)
        opencell(i + 1, j)
        opencell(i + 1, j + 1)
    if field[i][j] == 0:
        buttons[i][j]["text"] = 'no'
    else:
        buttons[i][j]["text"] = field[i][j]
    if buttons[i][j] == 1:
        buttons[i][j]["fg"] = 'azure'
    elif buttons[i][j] == 2:
        buttons[i][j]["fg"] = 'green'
    elif buttons[i][j] == 3:
        buttons[i][j]["fg"] = 'red'
    elif buttons[i][j] == 4:
        buttons[i][j]["fg"] = 'purple'
    elif buttons[i][j] == 5:
        buttons[i][j]["fg"] = 'brown'
    elif buttons[i][j] == 6:
        buttons[i][j]["fg"] = 'yellow'
    elif buttons[i][j] == 7:
        buttons[i][j]["fg"] = 'orange'
    elif buttons[i][j] == 8:
        buttons[i][j]["fg"] = 'white'
    buttons[i][j]["bg"] = 'grey'


def setflag(i, j):
    if buttons[i][j]["text"] == 'b':
        buttons[i][j]["text"] = '?'
    elif buttons[i][j]["text"] == '?':
        buttons[i][j]["text"] = ''
    else:
        buttons[i][j]["text"] = 'b'


def _opencell(i, j):
    def opencell_(event):
        opencell(i, j)
    return opencell_


def _setflag(i, j):
    def setflag_(event):
        setflag(i, j)
    return setflag_


root = tk.Tk()
print('Select level of difficulty(1 - easy (9x9 10 mines), 2 - medium (16x16 40 mines), 3 - hard (30x16 99 mines), 4 - custom')
lvl = int(input())
if lvl == 1:
    n, m, bombs = 9, 9, 10
elif lvl == 2:
    n, m, bombs = 16, 16, 40
elif lvl == 3:
    n, m, bombs = 30, 16, 99
else:
    print('Enter size of the field (x, y) and number of bombs, spliting with space')
    n, m, bombs = map(int, input().split())
if n * m <= bombs:
    bombs = n * m - 1
field = [[0 for i in range(n + 1)] for j in range(m + 1)]
for i in range(n + 1):
    field[0][i] = -1
    field[-1][i] = -1
for i in range(m + 1):
    field[i][0] = -1
    field[i][-1] = -1
for i in range(bombs):
    field = gen_bomb(field)
field = gen_field(field)
for i in range(m + 1):
    print(*field[i])
buttons = [[0 for i in range(0, n + 1)] for j in range(0, m + 1)]
for i in range(n + 1):
    buttons[0][i] = -1
    buttons[-1][i] = -1
for i in range(m + 1):
    buttons[i][0] = -1
    buttons[i][-1] = -1
for i in range(1, m):
    for j in range(1, n):
        btn = tk.Button(root, text='', bg='grey')
        btn.bind("<Button-1>", _opencell(i, j))
        btn.bind("<Button-2>", _setflag(i, j))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn
walken = []
# btn = tk.Button(root,                  #родительское окно
#              text="Click me",       #надпись на кнопке
#              width=30,height=5,     #ширина и высота
#              bg="white",fg="black")
# btn.bind("<Button-1>", opencell)
# btn.pack()
root.mainloop()
# root = tk.Tk()
# def Hello(event):
#     print("Yet another hello world")
#
# btn = tk.Button(root,                  #родительское окно
#              text="Click me",       #надпись на кнопке
#              width=30,height=5,     #ширина и высота
#              bg="white",fg="black") #цвет фона и надписи
# btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
# btn.pack()                          #расположить кнопку на главном окне
# root.mainloop()