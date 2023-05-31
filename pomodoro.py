import os, time, datetime

w = int(input("Give me the working time (int, min): "))
b = int(input("Give me the break time (int, min): "))
c = int(input("Number of times (int): "))


hTx = ""
mTx = ""
sTx = ""
def zht():
    if hT < 10:
        hTx = f"0{hT}"
    else:
        hTx = hT
    if mT < 10:
        mTx = f"0{mT}"
    else:
        mTx = mT
    if sT < 10:
        sTx = f"0{sT}"
    else:
        sTx = sT
    return hTx,  mTx, sTx

hS = ""
mS = ""
sS = ""
def zhs():
    if datetime.datetime.now().hour < 10:
        hS = f"0{datetime.datetime.now().hour}"
    else:
        hS = datetime.datetime.now().hour
    if datetime.datetime.now().minute < 10:
        mS = f"0{datetime.datetime.now().minute}"
    else:
        mS = datetime.datetime.now().minute
    if datetime.datetime.now().second < 10:
        sS = f"0{datetime.datetime.now().second}"
    else:
        sS = datetime.datetime.now().second
    return hS,  mS, sS

z = 1
def timeTo():
    if z%2 == 0:
        return b, "¡BREAK!🤩;"
    else:
        return w, " ¡WORK!😡;"
    
a = 0
hT = 0
mT = 0
sT = 0
while a < c:
    s = 0
    m = 0
    h = 0
    while m+(60*h) < timeTo()[0]:
        if s < 10:
            if m < 10:
                print(f"[{round(a+0.9)}]->", h, f"h 0{m}", f"min 0{s}", f"sec -> {timeTo()[1]}    TOTAL -> {zht()[0]}h {zht()[1]}min {zht()[2]}sec       [{zhs()[0]}:{zhs()[1]}:{zhs()[2]}]")
            else:
                print(f"[{round(a+0.9)}]->", h, "h", m, f"min 0{s}", f"sec -> {timeTo()[1]}    TOTAL -> {zht()[0]}h {zht()[1]}min {zht()[2]}sec       [{zhs()[0]}:{zhs()[1]}:{zhs()[2]}]")
        elif m < 10:
            print(f"[{round(a+0.9)}]->", h, f"h 0{m}", "min", s, f"sec -> {timeTo()[1]}    TOTAL -> {zht()[0]}h {zht()[1]}min {zht()[2]}sec       [{zhs()[0]}:{zhs()[1]}:{zhs()[2]}]")
        else:
            print(f"[{round(a+0.9)}]->", h, "h", m, "min", s, f"sec -> {timeTo()[1]}    TOTAL -> {zht()[0]}h {zht()[1]}min {zht()[2]}sec       [{zhs()[0]}:{zhs()[1]}:{zhs()[2]}]")
        s += 1
        sT += 1
        if s == 60:
            s = 0
            sT = 0
            m += 1
            mT += 1
        if m == 60:
            h += 1
            hT += 1
            m = 0
            mT = 0
        time.sleep(1)
        os.system("clear")
    z += 1
    a += 0.5