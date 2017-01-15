
from corepart import calculate
from tkinter import *
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master,)
        self.currentnum=''
        self.Abs=0
        self.Abs_flag=False
        self.series=['#']
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.screen = tk.Label(self, text='\n0', width=32, height=2, font=3,  anchor="w", justify="left")
        self.screen.grid(row=0,columnspan=5, )

        self.num1 = tk.Button(self,text='1', command=self.addnum1, width=8, height=2)
        self.num1.grid(row=1, column=0)

        self.num2 = tk.Button(self,text='2', command=self.addnum2, width=8, height=2)
        self.num2.grid(row=1, column=1)

        self.num3 = tk.Button(self,text='3', command=self.addnum3, width=8, height=2)
        self.num3.grid(row=1, column=2)

        self.oper_add = tk.Button(self, text='+', command=self.add_oper_add, width=8, height=2)
        self.oper_add.grid(row=1, column=3)
        
        self.num4 = tk.Button(self,text='4', command=self.addnum4, width=8, height=2)
        self.num4.grid(row=2, column=0)
        
        self.num5 = tk.Button(self,text='5', command=self.addnum5, width=8, height=2)
        self.num5.grid(row=2, column=1)

        self.num6 = tk.Button(self,text='6', command=self.addnum6, width=8, height=2)
        self.num6.grid(row=2, column=2)

        self.oper_minus = tk.Button(self, text='-', command=self.add_oper_minus, width=8, height=2)
        self.oper_minus.grid(row=2, column=3)

        self.delete = tk.Button(self, text='DEL', command=self.order_delete, width=8, height=2)
        self.delete.grid(row=2, column=4)
        
        self.num7 = tk.Button(self,text='7', command=self.addnum7, width=8, height=2)
        self.num7.grid(row=3, column=0)

        self.num8 = tk.Button(self,text='8', command=self.addnum8, width=8, height=2)
        self.num8.grid(row=3, column=1)

        self.num9 = tk.Button(self,text='9', command=self.addnum9, width=8, height=2)
        self.num9.grid(row=3, column=2)

        self.oper_multiply = tk.Button(self, text='*', command=self.add_oper_multiply, width=8, height=2)
        self.oper_multiply.grid(row=3, column=3)

        self.b_bracket = tk.Button(self, text='(', command=self.add_b_bracket, width=8, height=2)
        self.b_bracket.grid(row=3, column=4)

        self.num_dot = tk.Button(self,text='.', command=self.addnum_dot, width=8, height=2)
        self.num_dot.grid(row=4, column=0)

        self.num0 = tk.Button(self,text='0', command=self.addnum0, width=8, height=2)
        self.num0.grid(row=4, column=1)

        self.result = tk.Button(self, text='=', command= self.oper_calculate, width=8, height=2)
        self.result.grid(row=4, column=2)

        self.oper_divide = tk.Button(self, text='/', command=self.add_oper_divide, width=8, height=2)
        self.oper_divide.grid(row=4, column=3)

        self.r_bracket = tk.Button(self, text=')', command=self.add_r_bracket, width=8, height=2)
        self.r_bracket.grid(row=4, column=4)

        self.clear_screen = tk.Button(self, text='CLR', command=self.order_clear_screen, width=8, height=2)
        self.clear_screen.grid(row=1, column=4)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy, width=8, height=2)
        self.quit.grid(row=5, column=2)

    def update_screen(self):
        del self.screen
        #test code
        print(self.Abs)
        ###
        self.screen=tk.Label(self, text=self.currentnum+'\n'+str(self.Abs), width=32, height=2, font=3, anchor="w", justify="left")
        self.screen.grid(row=0, columnspan=5,)

    def addnum1(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='1'
        self.update_screen()
    def addnum2(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='2'
        self.update_screen()
    def addnum3(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='3'
        self.update_screen()
    def addnum4(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='4'
        self.update_screen()
    def addnum5(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='5'
        self.update_screen()
    def addnum6(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='6'
        self.update_screen()
    def addnum7(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='7'
        self.update_screen()
    def addnum8(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='8'
        self.update_screen()
    def addnum9(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='9'
        self.update_screen()
    def addnum0(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='0'
        self.update_screen()
    def addnum_dot(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='.'
        self.update_screen()
    def add_oper_add(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
            self.currentnum+=str(self.Abs)
        self.currentnum+='+'
        self.update_screen()
    def add_oper_minus(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
            self.currentnum+=str(self.Abs)
        self.currentnum+='-'
        self.update_screen()
    def add_oper_multiply(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
            self.currentnum+=str(self.Abs)
        self.currentnum+='*'
        self.update_screen()
    def add_oper_divide(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
            self.currentnum+=str(self.Abs)
        self.currentnum+='/'
        self.update_screen()    
    def oper_calculate(self):
        calculate(self)
    def order_clear_screen(self):
        self.series=["#"]
        self.currentnum=''
        self.Abs=0
        self.Abs_flag=False
        self.update_screen()
    def order_delete(self):
        if len(self.currentnum)==0:
            return
        self.currentnum = self.currentnum[:-1]
        self.update_screen()
    def add_b_bracket(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+='('
        self.update_screen()
    def add_r_bracket(self):
        if self.Abs_flag==True:
            self.Abs_flag=False
        self.currentnum+=')'
        self.update_screen()

root = tk.Tk()
root.title("My Caculator")
app = Application(master=root)

app.mainloop()

