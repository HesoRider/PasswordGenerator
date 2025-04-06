import tkinter
import random

# n文字のランダムな文字列を生成する関数
def randomStr(n, whichSymbol):
    #選択する元となる文字列
    if whichSymbol == True:
        # 記号あり
        src = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!$%&@'
    else : 
        # 記号なし
        src = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join([random.choice(src) for _ in range(n)])

def randomWrap():
    whichSymbol = symbol_v.get()
    n = int(len.get())
    answer.delete(0, tkinter.END)
    answer.insert(0, randomStr(n, whichSymbol))

#「記号あり」「記号なし」の表示を変える
def offSymbol():
    symbolLabel['text'] = '記号なし'
def onSymbol():
    symbolLabel['text'] = '記号あり'

#フレームの生成
root = tkinter.Tk()

root.title(u"ランダム文字列生成") #ウィンドウ名

winWidth = 400
winHeight = 400
root.geometry(f"{winWidth}x{winHeight}") #ウィンドウサイズ

mainframe = tkinter.Frame(master=root)
mainframe.pack()

#英文字のみか記号アリか
symbolLabel = tkinter.Label(master=mainframe, text='記号なし', font=('System', 20))
symbolLabel.grid(row=0, column=0, columnspan=2)

symbol_v = tkinter.BooleanVar() #ウィジェット変数
frame1 = tkinter.Frame(master=mainframe) #横ならびにするためのフレーム
frame1.grid(row=1, column=0)
onlyStr = tkinter.Radiobutton(
    master=frame1, 
    text='記号なし', 
    variable=symbol_v, 
    width=5, 
    value=False, 
    command=offSymbol)
onlyStr.pack()

frame2 = tkinter.Frame(master=mainframe) #横ならびにするためのフレーム
frame2.grid(row=1, column=1)
symbol = tkinter.Radiobutton(
    master=frame2,
    text='記号あり', 
    variable=symbol_v, 
    width=5, 
    value=True, 
    command=onSymbol)
symbol.pack()

guide = tkinter.Label(master=mainframe, text='何文字にしますか？', font=20)
guide.grid(row=2, column=0, columnspan=2, pady=10)
len = tkinter.Entry(master=mainframe, width=5, font=20) #長さ入力
len.grid(row=3, column=0, columnspan=2)

#実行ボタン
enterBtn = tkinter.Button(master=mainframe, text='生成', width=5, command=randomWrap)
enterBtn.grid(row=4, column=0, columnspan=2)

answer = tkinter.Entry(master=mainframe, width=40, font=20) #答え表示
answer.grid(row=5, column=0, columnspan=2, pady=50)

root.mainloop() #メインループ
