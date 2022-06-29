from tkinter import *
from grapher import graph
from info import getFunctionInfo
#from functions import Rational, Irrational, Polinomical

class Menu:
    def __init__(self, window):
        self.window = window
        self.function_type = None

        window.title("FunctionSolver")
        window.geometry('800x600')
        window.resizable(width=False, height=False)

        root = Frame(window)
        root.place(x=0,y=0,width=800,height=600)
        root.config(bg='#121212')

#       TITLE

        titulo = Label(root)
        titulo.config(bg='#121212', fg='#f2f2f2', justify=CENTER, font=('Helvetica', '24', 'bold'))
        titulo.config(text='FunctionSolver')
        titulo.place(x=280, y=35)

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

        def info():
            function_domain, function_rangee, function_y_intercept, function_zero, function_positivity, function_negativity, function_vertical_asintote, function_horizontal_asintote = getFunctionInfo(function.get()[7:])
            domain.set(f'{domainLabel.cget("text")} {function_domain}')
            rangee.set(f'{rangeeLabel.cget("text")} {function_rangee}')
            yIntercept.set(f'{yInterceptLabel.cget("text")} {function_y_intercept}')
            zero.set(f'{zeroLabel.cget("text")} {function_zero}')
            positivity.set(f'{positivityLabel.cget("text")} {function_positivity}')
            negativity.set(f'{negativityLabel.cget("text")} {function_negativity}')
            verticalAsintote.set(f'{verticalAsintoteLabel.cget("text")} {function_vertical_asintote}')
            horizontalAsintote.set(f'{horizontalAsintoteLabel.cget("text")} {function_horizontal_asintote}')

        def selectPoint():
            print('select point')
            menuPunto = Toplevel()
            menuPunto.title("Select a point")
            menuPunto.geometry('300x200')
            menuPunto.resizable(width=False, height=False)

            labelSelectPoint = Label(menuPunto)
            labelSelectPoint.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
            labelSelectPoint.config(text='Select point in x:')
            labelSelectPoint.place(x=85, y=50)

            entryPoint = Entry(menuPunto)
            entryPoint.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), width=40)
            entryPoint.place(x=85, y=105)


        change = Button(root)
        change.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=changeText)
        change.config(text='Change')
        change.place(x=650, y=145)

        selectPoint = Button(root)
        selectPoint.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda: selectPoint)
        selectPoint.config(text='Select Point')
        selectPoint.place(x=650, y=190)

        function = StringVar(value=f'f(x) = ')

        functionLabel = Label(root)
        functionLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        functionLabel.config(textvariable=function)
        functionLabel.place(x=85, y=180)

        graphBtn = Button(root)
        graphBtn.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:graph(function.get()[7:]))
        graphBtn.config(text='Graph')
        graphBtn.place(x=85, y=240)

        getInfoBtn = Button(root)
        getInfoBtn.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=info)
        getInfoBtn.config(text='Info')
        getInfoBtn.place(x=160, y=240)

        #SYMBOL BUTTONS

        squareRootBtn = Button(root)
        squareRootBtn.config(font=('Cambira Math', 24), justify=LEFT, command=lambda:write('**(0.5)'))
        squareRootBtn.config(text='√')
        squareRootBtn.place(x=250, y=290)

        nRootBtn = Button(root)
        nRootBtn.config(font=('Cambira Math', 24), justify=CENTER, command=lambda:write('**(0.)'))
        nRootBtn.config(text='ⁿ√')
        nRootBtn.place(x=320, y=290)

        rationBtn = Button(root)
        rationBtn.config(font=('Cambira Math', 24), justify=CENTER, command=lambda:write('() / ()'))
        rationBtn.config(text='⎯⎯⎯')
        rationBtn.place(x=410, y=290)

        powerBtn = Button(root)
        powerBtn.config(font=('Cambira Math', 24), justify=CENTER, command=lambda:write('**()'))
        powerBtn.config(text='xⁿ')
        powerBtn.place(x=500, y=290)

        #INFO LABELS

        domain = StringVar(value=f'Domain = ')

        domainLabel = Label(root)
        domainLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        domainLabel.config(textvariable=domain)
        domainLabel.place(x=85, y=390)

        rangee = StringVar(value=f'Range = ')

        rangeeLabel = Label(root)
        rangeeLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        rangeeLabel.config(textvariable=rangee)
        rangeeLabel.place(x=310, y=390)

        yIntercept = StringVar(value=f'Y Intercept = ')

        yInterceptLabel = Label(root)
        yInterceptLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        yInterceptLabel.config(textvariable=yIntercept)
        yInterceptLabel.place(x=505, y=390)

        zero = StringVar(value=f'Zero = ')

        zeroLabel = Label(root)
        zeroLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        zeroLabel.config(textvariable=zero)
        zeroLabel.place(x=85, y=445)

        positivity = StringVar(value=f'Positivity = ')

        positivityLabel = Label(root)
        positivityLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        positivityLabel.config(textvariable=positivity)
        positivityLabel.place(x=310, y=445)

        negativity = StringVar(value=f'Negativity = ')

        negativityLabel = Label(root)
        negativityLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        negativityLabel.config(textvariable=negativity)
        negativityLabel.place(x=505, y=445)

        verticalAsintote = StringVar(value=f'Vert. Asintote = ')

        verticalAsintoteLabel = Label(root)
        verticalAsintoteLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        verticalAsintoteLabel.config(textvariable=verticalAsintote)
        verticalAsintoteLabel.place(x=85, y=500)

        horizontalAsintote = StringVar(value=f'Hor. Asintote = ')

        horizontalAsintoteLabel = Label(root)
        horizontalAsintoteLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        horizontalAsintoteLabel.config(textvariable=horizontalAsintote)
        horizontalAsintoteLabel.place(x=310, y=500)




if __name__ == "__main__":
    tk = Tk()
    menu = Menu(tk)
    tk.mainloop()


    