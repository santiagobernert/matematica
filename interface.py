from mimetypes import init
from tkinter import *
from grapher import graph



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
        polinomical.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=self.subtype)
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

        trigonometric = Button(root)
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
        logarithmic.place(x=245, y=180)
    
    def subtype(self):
        new_window = Subtype(self.window)
        new_window.mainloop()

    def enterFunction(self, function_type):
        new_window = EnterFunction(self.window, function_type)
        new_window.mainloop()

class Subtype(Menu):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        function_type = None

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


        labelSelectSubType = Label(root)
        labelSelectSubType.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        labelSelectSubType.config(text='Select function subtype:')
        labelSelectSubType.place(x=85, y=100)

        constant = Button(root)
        constant.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:Menu.enterFunction(self, 'Constant'))
        constant.config(text='Constant')
        constant.place(x=85, y=140)

        linear = Button(root)
        linear.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:Menu.enterFunction(self, 'Linear'))
        linear.config(text='Linear')
        linear.place(x=245, y=140)

        quadratic = Button(root)
        quadratic.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:Menu.enterFunction(self, 'Quadratic'))
        quadratic.config(text='Quadratic')
        quadratic.place(x=395, y=140)


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

        if self.function_type == 'Constant':
            fn = Constant(root)


# CREATE A DIFFERENT CLASS FOR EVERY TYPE OF FUNCTION
class Constant:
    def __init__(self, root):
        fromula = Label(root)
        fromula.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        fromula.config(text='Constant function formula\n f(x) = a')
        fromula.place(x=85, y=140)
        valueLabel = Label(root)
        valueLabel.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        valueLabel.config(text='a =')
        valueLabel.place(x=85, y=240)

 
        entry = Entry(root)
        entry.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'))
        entry.place(x=120, y=240)

        value = StringVar(value='f(x) = ')
        def changeText():
            value.set('f(x) = ' + entry.get())



        change = Button(root)
        change.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=changeText)
        change.config(text='Change')
        change.place(x=450, y=240)

        function = Label(root)
        function.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        function.config(textvariable=value)
        function.place(x=150, y=340)

        graphBtn = Button(root)
        graphBtn.config(bg='#f2f2f2', fg='#121212', justify=LEFT, font=('Helvetica', '16'), command=lambda:graph(value.get()))
        graphBtn.config(text='Graph')
        graphBtn.place(x=450, y=390)



        '''GButton_975=tk.Button(root)
        GButton_975["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_975["font"] = ft
        GButton_975["fg"] = "#000000"
        GButton_975["justify"] = "center"
        GButton_975["text"] = "Button"
        GButton_975.place(x=80,y=120,width=70,height=25)
        GButton_975["command"] = self.GButton_975_command

        GRadio_584=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_584["font"] = ft
        GRadio_584["fg"] = "#333333"
        GRadio_584["justify"] = "center"
        GRadio_584["text"] = "RadioButton"
        GRadio_584.place(x=220,y=120,width=85,height=25)
        GRadio_584["command"] = self.GRadio_584_command

        GCheckBox_728=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_728["font"] = ft
        GCheckBox_728["fg"] = "#333333"
        GCheckBox_728["justify"] = "center"
        GCheckBox_728["text"] = "CheckBox"
        GCheckBox_728.place(x=350,y=120,width=70,height=25)
        GCheckBox_728["offvalue"] = "0"
        GCheckBox_728["onvalue"] = "1"
        GCheckBox_728["command"] = self.GCheckBox_728_command

        GLineEdit_360=tk.Entry(root)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"
        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = "Entry"
        GLineEdit_360.place(x=450,y=120,width=70,height=25)

        GLineEdit_864=tk.Entry(root)
        GLineEdit_864["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_864["font"] = ft
        GLineEdit_864["fg"] = "#333333"
        GLineEdit_864["justify"] = "center"
        GLineEdit_864["text"] = "Entry"
        GLineEdit_864.place(x=80,y=170,width=70,height=25)'''




if __name__ == "__main__":
    tk = Tk()
    menu = Menu(tk)
    tk.mainloop()

    