from tkinter import *
from functions.grapher import graph

from functions import Rational, Irrational, Polinomical

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

        #SELECT FUNCTION TYPE

        labelSelectType = Label(root)
        labelSelectType.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        labelSelectType.config(text='Select function type:')
        labelSelectType.place(x=85, y=105)

        polinomical = Button(root)
        polinomical.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:self.enterFunction('Polinomical'))
        polinomical.config(text='Polinomical')
        polinomical.place(x=85, y=140)

        rational = Button(root)
        rational.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:self.enterFunction('Rational'))
        rational.config(text='Rational')
        rational.place(x=245, y=140)

        irrational = Button(root)
        irrational.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:self.enterFunction('Irrational'))
        irrational.config(text='Irrational')
        irrational.place(x=395, y=140)

        '''trigonometric = Button(root)
        trigonometric.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:self.enterFunction('Trigonometric'))
        trigonometric.config(text='Trigonometric')
        trigonometric.place(x=545, y=140)

        exponential = Button(root)
        exponential.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:self.enterFunction('Exponential'))
        exponential.config(text='Exponential')
        exponential.place(x=85, y=180)

        logarithmic = Button(root)
        logarithmic.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:self.enterFunction('Logarithmic'))
        logarithmic.config(text='Logarithmic')
        logarithmic.place(x=245, y=180)'''
    

    def enterFunction(self, function_type):
        new_window = EnterFunction(self.window, function_type)
        new_window.mainloop()



class EnterFunction:
    def __init__(self, window, function_type):
        self.function_type = function_type
        self.window = window

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

        # FUNCTION TYPE LABEL

        labelType = Label(root)
        labelType.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        labelType.config(text=function_type.upper() if function_type != None else 'None')
        labelType.place(x=85, y=105)

        if self.function_type == 'Polinomical':
            fn = Polinomical(root)
        
        if self.function_type == 'Rational':
            fn = Rational(root)
        
        if self.function_type == 'Irrational':
            fn = Irrational(root)



if __name__ == "__main__":
    tk = Tk()
    menu = Menu(tk)
    tk.mainloop()

    