#importar o tkinter

from tkinter import *
from tkinter import ttk

#cores

cor1 = "#353b4a" #preta
cor2 = "#dedddc" #branca
cor3 = "#8da9eb" #azul
cor4 = "#c4c6cc" #cinza
cor5 = "#d69b60" #laranja


janela =Tk()
janela.title("Calculadora")
janela.geometry("235x314")
janela.config(bg=cor1)

#frames

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variável todos valores

todos_valores = ""

# label
valor_texto = StringVar()

#função

def entrar_valores(event):
  
  global todos_valores
  
  todos_valores = todos_valores + str(event)
  
  #passando valor p/ tela
  valor_texto.set(todos_valores)
  
  #calcular
  
def calcular():
  global todosValores
  try:
      resultado = eval(todosValores)
      valor_texto.set(str(resultado))
  except Exception as e:
      valor_texto.set('Erro')
      todosValores = ""
      resultado = eval (todos_valores)
      print(resultado)
      
      valor_texto.set(str(resultado))
      
      
      #função limpar tela
      
def limpar_tela():
      global todos_valores
      todos_valores = ""
      valor_texto.set("")



app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#botões

b1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, command= lambda: entrar_valores ("%"), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3 = Button(frame_corpo, command= lambda: entrar_valores ("/"), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

b4 = Button(frame_corpo, command= lambda: entrar_valores ("7"), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=53)
b5 = Button(frame_corpo, command= lambda: entrar_valores ("6"), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=53)
b6 = Button(frame_corpo, command= lambda: entrar_valores ("5"), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=53)
b7 = Button(frame_corpo, command= lambda: entrar_valores ("*"), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=53)

b8 = Button(frame_corpo, command= lambda: entrar_valores ("4"), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=106)
b9 = Button(frame_corpo, command= lambda: entrar_valores ("5"), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=106)
b10 = Button(frame_corpo, command= lambda: entrar_valores ("6"), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=106)
b11 = Button(frame_corpo, command= lambda: entrar_valores ("-"), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=106)

b12 = Button(frame_corpo, command= lambda: entrar_valores ("1"), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=159)
b13 = Button(frame_corpo, command= lambda: entrar_valores ("2"), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=159)
b14 = Button(frame_corpo, command= lambda: entrar_valores ("3"), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=159)
b15 = Button(frame_corpo, command= lambda: entrar_valores ("+"), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=159)

b16 = Button(frame_corpo, command= lambda: entrar_valores ("0"), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=212)
b17 = Button(frame_corpo, command= lambda: entrar_valores ("."), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=212)
b18 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=212)



  


janela.mainloop()