from tkinter import *
from tkinter import messagebox 



class won():
    
    def __init__(self):

        self.btn1 = Button(tk, width = 15, height = 6, state = "disabled", fg = "white", command = self.cl1, )
        self.btn1.place(x = 5, y = 50)
        
        self.btn2 = Button(tk, width = 15, height = 6, state = "disabled", fg = "white", command = self.cl2)
        self.btn2.place(x = 140, y = 50)
        
        self.btn3 = Button(tk, width = 15, height = 6, state = "disabled", fg = "white", command = self.cl3)
        self.btn3.place(x = 280, y = 50)
        
        self.btn4 = Button(tk, width = 15, height = 6, state = "disabled", fg = "white", command = self.cl4)
        self.btn4.place(x = 5, y = 200)
         
        self.btn5 = Button(tk, width = 15, height = 6, state = "disabled", fg = "white", command = self.cl5)
        self.btn5.place(x = 140, y = 200)
        
        self.btn6 = Button(tk, width = 15, height = 6, state = "disabled", fg = "white", command = self.cl6)
        self.btn6.place(x = 280, y = 200)
        
        self.btn7 = Button(tk, width = 15, height = 6, state = "disabled", fg = "white", command = self.cl7)
        self.btn7.place(x = 5, y = 340)
        
        self.btn8 = Button(tk, width = 15, height = 6, state = "disabled", fg = "white", command = self.cl8)
        self.btn8.place(x = 140, y = 340)
        
        self.btn9 = Button(tk, width = 15, height = 6, state = "disabled", fg = "white", command = self.cl9)
        self.btn9.place(x = 280, y = 340)

        self.btn10 = Button(tk, width = 10, text = "Новая игра", bg = "#ab9ab8", fg = "white", command = self.newgame)
        self.btn10.place(x = 10, y = 5)

        self.btn11 = Button(tk, width = 6, text = "Выход", bg = "#ab9ab8", fg = "white", command = tk.destroy)
        self.btn11.place(x = 100, y = 5)
        
        self.hod = True
                    
    def newgame(self):
        self.btn1.configure(state = "normal")
        self.btn2.configure(state = "normal")
        self.btn3.configure(state = "normal")
        self.btn4.configure(state = "normal")
        self.btn5.configure(state = "normal")
        self.btn6.configure(state = "normal")
        self.btn7.configure(state = "normal")
        self.btn8.configure(state = "normal")
        self.btn9.configure(state = "normal")
        self.btn1['text'] = ""
        self.btn2['text'] = ""
        self.btn3['text'] = ""
        self.btn4['text'] = ""
        self.btn5['text'] = ""
        self.btn6['text'] = ""
        self.btn7['text'] = ""
        self.btn8['text'] = ""
        self.btn9['text'] = ""
        
    def cl1 (self):
        if self.hod == True:
            
            self.btn1['text'] = "X"
            self.btn1.configure(state = "disabled")
            self.hod = False
            if (self.btn1['text'] == "X" and self.btn4['text'] == "X" and self.btn7['text'] == "X") or (self.btn1['text'] == "X" and self.btn2['text'] == "X" and self.btn3['text'] == "X") or (self.btn3['text'] == "X" and self.btn6['text'] == "X" and self.btn9['text'] == "X") or (self.btn7['text'] == "X" and self.btn8['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] ==  "X" and self.btn8['text'] == "X") or (self.btn4['text'] == "X" and self.btn5['text'] == "X" and self.btn6['text'] == "X") or (self.btn1['text'] == "X" and self.btn5['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] == "X" and self.btn7['text'] == "X"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли КРЕСТИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()                    
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
        else:
            self.btn1['text'] = "0"
            self.btn1.configure(state = "disabled")
            self.hod = True
            if (self.btn1['text'] == "0" and self.btn4['text'] == "0" and self.btn7['text'] == "0") or (self.btn1['text'] == "0" and self.btn2['text'] == "0" and self.btn3['text'] == "0") or (self.btn3['text'] == "0" and self.btn6['text'] == "0" and self.btn9['text'] == "0") or (self.btn7['text'] == "0" and self.btn8['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] ==  "0" and self.btn8['text'] == "0") or (self.btn4['text'] == "0" and self.btn5['text'] == "0" and self.btn6['text'] == "0") or (self.btn1['text'] == "0" and self.btn5['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] == "0" and self.btn7['text'] == "0"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")                
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли НОЛИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "." and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()

    def cl2 (self):
        if self.hod == True:
            self.btn2['text'] = "X"
            self.btn2.configure(state = "disabled")
            self.hod = False
            if (self.btn1['text'] == "X" and self.btn4['text'] == "X" and self.btn7['text'] == "X") or (self.btn1['text'] == "X" and self.btn2['text'] == "X" and self.btn3['text'] == "X") or (self.btn3['text'] == "X" and self.btn6['text'] == "X" and self.btn9['text'] == "X") or (self.btn7['text'] == "X" and self.btn8['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] ==  "X" and self.btn8['text'] == "X") or (self.btn4['text'] == "X" and self.btn5['text'] == "X" and self.btn6['text'] == "X") or (self.btn1['text'] == "X" and self.btn5['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] == "X" and self.btn7['text'] == "X"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли КРЕСТИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
        else:
            self.btn2['text'] = "0"
            self.btn2.configure(state = "disabled")
            self.hod = True
            if (self.btn1['text'] == "0" and self.btn4['text'] == "0" and self.btn7['text'] == "0") or (self.btn1['text'] == "0" and self.btn2['text'] == "0" and self.btn3['text'] == "0") or (self.btn3['text'] == "0" and self.btn6['text'] == "0" and self.btn9['text'] == "0") or (self.btn7['text'] == "0" and self.btn8['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] ==  "0" and self.btn8['text'] == "0") or (self.btn4['text'] == "0" and self.btn5['text'] == "0" and self.btn6['text'] == "0") or (self.btn1['text'] == "0" and self.btn5['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] == "0" and self.btn7['text'] == "0"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли НОЛИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
            
    def cl3 (self):
        if self.hod == True:
            self.btn3['text'] = "X"
            self.btn3.configure(state = "disabled")
            self.hod = False
            if (self.btn1['text'] == "X" and self.btn4['text'] == "X" and self.btn7['text'] == "X") or (self.btn1['text'] == "X" and self.btn2['text'] == "X" and self.btn3['text'] == "X") or (self.btn3['text'] == "X" and self.btn6['text'] == "X" and self.btn9['text'] == "X") or (self.btn7['text'] == "X" and self.btn8['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] ==  "X" and self.btn8['text'] == "X") or (self.btn4['text'] == "X" and self.btn5['text'] == "X" and self.btn6['text'] == "X") or (self.btn1['text'] == "X" and self.btn5['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] == "X" and self.btn7['text'] == "X"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли КРЕСТИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
        else:
            self.btn3['text'] = "0"
            self.btn3.configure(state = "disabled")
            self.hod = True
            if (self.btn1['text'] == "0" and self.btn4['text'] == "0" and self.btn7['text'] == "0") or (self.btn1['text'] == "0" and self.btn2['text'] == "0" and self.btn3['text'] == "0") or (self.btn3['text'] == "0" and self.btn6['text'] == "0" and self.btn9['text'] == "0") or (self.btn7['text'] == "0" and self.btn8['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] ==  "0" and self.btn8['text'] == "0") or (self.btn4['text'] == "0" and self.btn5['text'] == "0" and self.btn6['text'] == "0") or (self.btn1['text'] == "0" and self.btn5['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] == "0" and self.btn7['text'] == "0"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли НОЛИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()

    def cl4 (self):
        if self.hod == True:
            self.btn4['text'] = "X"
            self.btn4.configure(state = "disabled")
            self.hod = False
            if (self.btn1['text'] == "X" and self.btn4['text'] == "X" and self.btn7['text'] == "X") or (self.btn1['text'] == "X" and self.btn2['text'] == "X" and self.btn3['text'] == "X") or (self.btn3['text'] == "X" and self.btn6['text'] == "X" and self.btn9['text'] == "X") or (self.btn7['text'] == "X" and self.btn8['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] ==  "X" and self.btn8['text'] == "X") or (self.btn4['text'] == "X" and self.btn5['text'] == "X" and self.btn6['text'] == "X") or (self.btn1['text'] == "X" and self.btn5['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] == "X" and self.btn7['text'] == "X"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли КРЕСТИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
        else:
            self.btn4['text'] = "0"
            self.btn4.configure(state = "disabled")
            self.hod = True
            if (self.btn1['text'] == "0" and self.btn4['text'] == "0" and self.btn7['text'] == "0") or (self.btn1['text'] == "0" and self.btn2['text'] == "0" and self.btn3['text'] == "0") or (self.btn3['text'] == "0" and self.btn6['text'] == "0" and self.btn9['text'] == "0") or (self.btn7['text'] == "0" and self.btn8['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] ==  "0" and self.btn8['text'] == "0") or (self.btn4['text'] == "0" and self.btn5['text'] == "0" and self.btn6['text'] == "0") or (self.btn1['text'] == "0" and self.btn5['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] == "0" and self.btn7['text'] == "0"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли НОЛИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
            
    def cl5 (self):
        if self.hod == True:
            self.btn5['text'] = "X"
            self.btn5.configure(state = "disabled")
            self.hod = False
            if (self.btn1['text'] == "X" and self.btn4['text'] == "X" and self.btn7['text'] == "X") or (self.btn1['text'] == "X" and self.btn2['text'] == "X" and self.btn3['text'] == "X") or (self.btn3['text'] == "X" and self.btn6['text'] == "X" and self.btn9['text'] == "X") or (self.btn7['text'] == "X" and self.btn8['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] ==  "X" and self.btn8['text'] == "X") or (self.btn4['text'] == "X" and self.btn5['text'] == "X" and self.btn6['text'] == "X") or (self.btn1['text'] == "X" and self.btn5['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] == "X" and self.btn7['text'] == "X"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли КРЕСТИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
        else:
            self.btn5['text'] = "0"
            self.btn5.configure(state = "disabled")
            self.hod = True
            if (self.btn1['text'] == "0" and self.btn4['text'] == "0" and self.btn7['text'] == "0") or (self.btn1['text'] == "0" and self.btn2['text'] == "0" and self.btn3['text'] == "0") or (self.btn3['text'] == "0" and self.btn6['text'] == "0" and self.btn9['text'] == "0") or (self.btn7['text'] == "0" and self.btn8['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] ==  "0" and self.btn8['text'] == "0") or (self.btn4['text'] == "0" and self.btn5['text'] == "0" and self.btn6['text'] == "0") or (self.btn1['text'] == "0" and self.btn5['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] == "0" and self.btn7['text'] == "0"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли НОЛИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()

    def cl6 (self):
        if self.hod == True:
            self.btn6['text'] = "X"
            self.btn6.configure(state = "disabled")
            self.hod = False
            if (self.btn1['text'] == "X" and self.btn4['text'] == "X" and self.btn7['text'] == "X") or (self.btn1['text'] == "X" and self.btn2['text'] == "X" and self.btn3['text'] == "X") or (self.btn3['text'] == "X" and self.btn6['text'] == "X" and self.btn9['text'] == "X") or (self.btn7['text'] == "X" and self.btn8['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] ==  "X" and self.btn8['text'] == "X") or (self.btn4['text'] == "X" and self.btn5['text'] == "X" and self.btn6['text'] == "X") or (self.btn1['text'] == "X" and self.btn5['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] == "X" and self.btn7['text'] == "X"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли КРЕСТИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
        else:
            self.btn6['text'] = "0"
            self.btn6.configure(state = "disabled")
            self.hod = True
            if (self.btn1['text'] == "0" and self.btn4['text'] == "0" and self.btn7['text'] == "0") or (self.btn1['text'] == "0" and self.btn2['text'] == "0" and self.btn3['text'] == "0") or (self.btn3['text'] == "0" and self.btn6['text'] == "0" and self.btn9['text'] == "0") or (self.btn7['text'] == "0" and self.btn8['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] ==  "0" and self.btn8['text'] == "0") or (self.btn4['text'] == "0" and self.btn5['text'] == "0" and self.btn6['text'] == "0") or (self.btn1['text'] == "0" and self.btn5['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] == "0" and self.btn7['text'] == "0"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли НОЛИЛКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()

    def cl7 (self):
        if self.hod == True:
            self.btn7['text'] = "X"
            self.btn7.configure(state = "disabled")
            self.hod = False
            if (self.btn1['text'] == "X" and self.btn4['text'] == "X" and self.btn7['text'] == "X") or (self.btn1['text'] == "X" and self.btn2['text'] == "X" and self.btn3['text'] == "X") or (self.btn3['text'] == "X" and self.btn6['text'] == "X" and self.btn9['text'] == "X") or (self.btn7['text'] == "X" and self.btn8['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] ==  "X" and self.btn8['text'] == "X") or (self.btn4['text'] == "X" and self.btn5['text'] == "X" and self.btn6['text'] == "X") or (self.btn1['text'] == "X" and self.btn5['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] == "X" and self.btn7['text'] == "X"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли КРЕСТИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
        else:
            self.btn7['text'] = "0"
            self.btn7.configure(state = "disabled")
            self.hod = True
            if (self.btn1['text'] == "0" and self.btn4['text'] == "0" and self.btn7['text'] == "0") or (self.btn1['text'] == "0" and self.btn2['text'] == "0" and self.btn3['text'] == "0") or (self.btn3['text'] == "0" and self.btn6['text'] == "0" and self.btn9['text'] == "0") or (self.btn7['text'] == "0" and self.btn8['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] ==  "0" and self.btn8['text'] == "0") or (self.btn4['text'] == "0" and self.btn5['text'] == "0" and self.btn6['text'] == "0") or (self.btn1['text'] == "0" and self.btn5['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] == "0" and self.btn7['text'] == "0"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли НОЛИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()

    def cl8 (self):
        if self.hod == True:
            self.btn8['text'] = "X"
            self.btn8.configure(state = "disabled")
            self.hod = False
            if (self.btn1['text'] == "X" and self.btn4['text'] == "X" and self.btn7['text'] == "X") or (self.btn1['text'] == "X" and self.btn2['text'] == "X" and self.btn3['text'] == "X") or (self.btn3['text'] == "X" and self.btn6['text'] == "X" and self.btn9['text'] == "X") or (self.btn7['text'] == "X" and self.btn8['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] ==  "X" and self.btn8['text'] == "X") or (self.btn4['text'] == "X" and self.btn5['text'] == "X" and self.btn6['text'] == "X") or (self.btn1['text'] == "X" and self.btn5['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] == "X" and self.btn7['text'] == "X"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли КРЕСТИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
        else:
            self.btn8['text'] = "0"
            self.btn8.configure(state = "disabled")
            self.hod = True
            if (self.btn1['text'] == "0" and self.btn4['text'] == "0" and self.btn7['text'] == "0") or (self.btn1['text'] == "0" and self.btn2['text'] == "0" and self.btn3['text'] == "0") or (self.btn3['text'] == "0" and self.btn6['text'] == "0" and self.btn9['text'] == "0") or (self.btn7['text'] == "0" and self.btn8['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] ==  "0" and self.btn7['text'] == "0") or (self.btn4['text'] == "0" and self.btn5['text'] == "0" and self.btn6['text'] == "0") or (self.btn1['text'] == "0" and self.btn5['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] == "0" and self.btn7['text'] == "0"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли НОЛИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()

    def cl9 (self):
        if self.hod == True:
            self.btn9['text'] = "X"
            self.btn9.configure(state = "disabled")
            self.hod = False
            if (self.btn1['text'] == "X" and self.btn4['text'] == "X" and self.btn7['text'] == "X") or (self.btn1['text'] == "X" and self.btn2['text'] == "X" and self.btn3['text'] == "X") or (self.btn3['text'] == "X" and self.btn6['text'] == "X" and self.btn9['text'] == "X") or (self.btn7['text'] == "X" and self.btn8['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] ==  "X" and self.btn8['text'] == "X") or (self.btn4['text'] == "X" and self.btn5['text'] == "X" and self.btn6['text'] == "X") or (self.btn1['text'] == "X" and self.btn5['text'] == "X" and self.btn9['text'] == "X") or (self.btn3['text'] == "X" and self.btn5['text'] == "X" and self.btn7['text'] == "X"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли КРЕСТИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
        else:
            self.btn9['text'] = "0"
            self.btn9.configure(state = "disabled")
            self.hod = True
            if (self.btn1['text'] == "0" and self.btn4['text'] == "0" and self.btn7['text'] == "0") or (self.btn1['text'] == "0" and self.btn2['text'] == "0" and self.btn3['text'] == "0") or (self.btn3['text'] == "0" and self.btn6['text'] == "0" and self.btn9['text'] == "0") or (self.btn7['text'] == "0" and self.btn8['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] ==  "0" and self.btn7['text'] == "0") or (self.btn4['text'] == "0" and self.btn5['text'] == "0" and self.btn6['text'] == "0") or (self.btn1['text'] == "0" and self.btn5['text'] == "0" and self.btn9['text'] == "0") or (self.btn3['text'] == "0" and self.btn5['text'] == "0" and self.btn7['text'] == "0"):
                self.btn1.configure(state = "disabled")
                self.btn2.configure(state = "disabled")
                self.btn3.configure(state = "disabled")
                self.btn4.configure(state = "disabled")
                self.btn5.configure(state = "disabled")
                self.btn6.configure(state = "disabled")
                self.btn7.configure(state = "disabled")
                self.btn8.configure(state = "disabled")
                self.btn9.configure(state = "disabled")
                self.answer = messagebox.askyesno(title="Вопрос", message="Выиграли НОЛИКИ!\nНачать заново?")
                if self.answer == True:
                    self.newgame()
                else:
                    tk.destroy()
            else:
                if self.btn1['text'] != "" and self.btn2['text'] != "" and self.btn3['text'] != "" and self.btn4['text'] != "" and self.btn5['text'] != "" and self.btn6['text'] != "" and self.btn7['text'] != "" and self.btn8['text'] != "" and self.btn9['text'] != "":
                    self.answer = messagebox.askyesno(title="Вопрос", message="НИЧЬЯ!\nНачать заново?")
                    if self.answer == True:
                        self.newgame()
                    else:
                        tk.destroy()
                

tk = Tk()
tk.geometry("400x450+500+180")
tk.resizable(False,False)
tk.title("Крестики\Нолики")
tk["bg"] = "#8cbd95"
wn = won()
tk.mainloop()





        
