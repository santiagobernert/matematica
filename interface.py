from tkinter import *
from grapher import graph, evalInPoint
from limit import getLimitByLeft, getLimitByRight
#from functions import Rational, Irrational, Polinomical

class Menu:
    def __init__(self, window):
        self.window = window
        self.function_type = None

        window.title("FunctionSolver")
        window.geometry('1000x700')
        window.attributes('-fullscreen', True)
        window.resizable(width=False, height=False)

        root = Frame(window)
        root.place(x=0,y=0,width=1400,height=800)
        root.config(bg='#121212')

#       TITLE

        titulo = Label(root, width=75)
        titulo.config(bg='#121212', fg='#f2f2f2', justify=CENTER, font=('Helvetica', '24', 'bold'))
        titulo.config(text='FunctionSolver')
        titulo.place(x=0, y=35)

        labelEnterFunction = Label(root)
        labelEnterFunction.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        labelEnterFunction.config(text='Enter function:')
        labelEnterFunction.place(x=85, y=105)

        labelFX = Label(root)
        labelFX.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        labelFX.config(text='f(x) = ')
        labelFX.place(x=85, y=145)

        entry = Entry(root)
        entry.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), width=40)
        entry.place(x=150, y=145)

        def changeText():
            entry_text = entry.get()
            if ')/(' in entry_text:
                entry_text = entry_text.replace('/', ' / ')
            if '+' in entry_text:
                entry_text = entry_text.replace('+', ' + ')
            if '-' in entry_text:
                entry_text = entry_text.replace('-', ' - ')
            function.set('f(x) = ' + entry_text)

        def write(operation):
            entry.insert(-1, operation)



        change = Button(root)
        change.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=changeText)
        change.config(text='Change')
        change.place(x=650, y=145)


        zoomBtn = Button(root, width=2)
        zoomBtn.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda : window.attributes('-fullscreen', False))
        zoomBtn.config(text='-')
        zoomBtn.place(x=1250, y=35)

        exitBtn = Button(root)
        exitBtn.config(bg='#ff0000', fg='#fdfdfd', justify=LEFT, font=('Helvetica', '16'), command=lambda : window.quit())
        exitBtn.config(text='X')
        exitBtn.place(x=1300, y=35)

        function = StringVar(value=f'f(x) = ')

        #Label that shows the function entered
        functionLabel = Label(root)
        functionLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        functionLabel.config(textvariable=function)
        functionLabel.place(x=85, y=180)

        #Button that calls the "graph" function
        graphBtn = Button(root)
        graphBtn.config(bg='#4444ee', fg='#fafafa', justify=LEFT, font=('Helvetica', '16'), command=lambda:graph(function.get()[7:]))
        graphBtn.config(text='Graph')
        graphBtn.place(x=85, y=240)

        #SYMBOL BUTTONS

        #Button of the square root symbol
        squareRootBtn = Button(root)
        squareRootBtn.config(font=('Cambira Math', 24), justify=LEFT, command=lambda:write('**(0.5)'))
        squareRootBtn.config(text='√')
        squareRootBtn.place(x=250, y=240)

        #Button of the root of n symbol
        nRootBtn = Button(root)
        nRootBtn.config(font=('Cambira Math', 24), justify=CENTER, command=lambda:write('**(0.)'))
        nRootBtn.config(text='ⁿ√')
        nRootBtn.place(x=320, y=240)

        #Button of the dividend symbol
        rationBtn = Button(root)
        rationBtn.config(font=('Cambira Math', 24), justify=CENTER, command=lambda:write('() / ()'))
        rationBtn.config(text='⎯⎯⎯')
        rationBtn.place(x=410, y=240)

        #Button of the power symbol
        powerBtn = Button(root)
        powerBtn.config(font=('Cambira Math', 24), justify=CENTER, command=lambda:write('**()'))
        powerBtn.config(text='xⁿ')
        powerBtn.place(x=500, y=240)

        #Function that gets the foint selected by the user and calls the "graph" function
        def selectPointInX():
            point = entryPoint.get()
            funcInPoint.set(f'f({point}) = {evalInPoint(point, function.get()[7:])}')
            graph(function.get()[7:], int(entryPoint.get()))

        #Label:"select point in x"
        labelSelectPoint = Label(root)
        labelSelectPoint.config(bg='#121212', fg='#fafafa', justify=LEFT, font=('Helvetica', '16'))
        labelSelectPoint.config(text='Select point in x:')
        labelSelectPoint.place(x=1000, y=145)

        #Input the point
        entryPoint = Entry(root)
        entryPoint.config(bg='#fefefe', fg='#121212', justify=LEFT, font=('Helvetica', '16'), width=5)
        entryPoint.place(x=1050, y=185)

        #Button to call the function "selectPoint"
        selectPoint = Button(root)
        selectPoint.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=selectPointInX)
        selectPoint.config(text='Select Point')
        selectPoint.place(x=1020, y=230)

        funcInPoint = StringVar(value='')

        #Label to show the point selected
        labelPointSelected = Label(root)
        labelPointSelected.config(bg='#121212', fg='#fafafa', justify=LEFT, font=('Helvetica', '16'))
        labelPointSelected.config(textvariable=funcInPoint)
        labelPointSelected.place(x=1000, y=290)

        #Button to get the limit by left
        leftLimit = Button(root)
        leftLimit.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=getLimitByLeft)
        leftLimit.config(text='Get limit by left')
        leftLimit.place(x=900, y=330)

        #Button to get the limit by right
        rightLimit = Button(root)
        rightLimit.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=getLimitByRight)
        rightLimit.config(text='Get limit by right')
        rightLimit.place(x=1100, y=330)

        #Label to show the limits

        limit = StringVar(value='')
        
        labelLimit = Label(root)
        labelLimit.config(bg='#121212', fg='#fafafa', justify=LEFT, font=('Helvetica', '16'))
        labelLimit.config(textvariable=limit)
        labelLimit.place(x=1000, y=390)


if __name__ == "__main__":
    tk = Tk()
    menu = Menu(tk)
    tk.mainloop()


    