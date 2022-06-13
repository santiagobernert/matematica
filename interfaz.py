from tkinter import *

class Ventana:
    def __init__(self, ventana):
        self.ventana = ventana
        function_type = None

        ventana.title("FunctionSolver")
        ventana.geometry('800x600')
        ventana.resizable(width=False, height=False)

        root = Frame(ventana)
        root.place(x=0,y=0,width=800,height=600)
        root.config(bg='#121212')

#       TITLE

        titulo = Label(root)
        titulo.config(bg='#121212', fg='#f2f2f2', justify=CENTER, font=('Helvetica', '24', 'bold'))
        titulo.config(text='FunctionSolver')
        titulo.place(x=315, y=35)

        #SELECT FUNCTION TYPE

        labelSelectType = Label(root)
        labelSelectType.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        labelSelectType.config(text='Select function type:')
        labelSelectType.place(x=85, y=105)

        polinomical = Radiobutton(root)
        polinomical.config(variable=function_type, value='polinomical', bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        polinomical.config(text='Polinomical')
        polinomical.place(x=85, y=140)

        rational = Radiobutton(root)
        rational.config(variable=function_type, value='rational', bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        rational.config(text='Rational')
        rational.place(x=245, y=140)

        irrational = Radiobutton(root)
        irrational.config(variable=function_type, value='irrational', bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        irrational.config(text='Irrational')
        irrational.place(x=395, y=140)

        trigonometric = Radiobutton(root)
        trigonometric.config(variable=function_type, value='trigonometric', bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        trigonometric.config(text='Trigonometric')
        trigonometric.place(x=545, y=140)

        exponential = Radiobutton(root)
        exponential.config(variable=function_type, value='exponential', bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        exponential.config(text='Exponential')
        exponential.place(x=85, y=180)

        logarithmic = Radiobutton(root)
        logarithmic.config(variable=function_type, value='logarithmic', bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        logarithmic.config(text='Logarithmic')
        logarithmic.place(x=245, y=180)


        # SELECT FUNCTION SUBTYPE

        labelSelectSubType = Label(root)
        labelSelectSubType.config(bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        labelSelectSubType.config(text='Select function subtype:')
        labelSelectSubType.place(x=85, y=225)

        constant = Radiobutton(root)
        constant.config(variable=function_type, value='constant', bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        constant.config(text='Constant')
        constant.place(x=85, y=270)

        linear = Radiobutton(root)
        linear.config(variable=function_type, value='linear', bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        linear.config(text='Linear')
        linear.place(x=245, y=270)

        quadratic = Radiobutton(root)
        quadratic.config(variable=function_type, value='quadratic', bg='#121212', fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        quadratic.config(text='Quadratic')
        quadratic.place(x=395, y=270)

        # FUNCTION TYPE LABEL

        labelType = Label(root)
        labelType.config(fg='#f2f2f2', justify=LEFT, font=('Helvetica', '16'))
        labelType.config(text=function_type.upper() if function_type != None else 'None')
        labelType.place(x=85, y=105)


        # PASS VALUES

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
    ventana = Ventana(tk)
    tk.mainloop()