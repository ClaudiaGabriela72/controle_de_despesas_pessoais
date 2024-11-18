from tkinter import *
from tkinter import Tk, ttk
import PIL


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"   
co6 = "#038cfc"   
co7 = "#3fbfb9"   
co8 = "#263238"   
co9 = "#e9edf5"   

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

# criando janela
janela = Tk()
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')


# Criando Frames
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief='flat')
frameCima.grid(row=0, column=0)

frameMeio  = Frame(janela, width=1043, height=361, bg=co1, relief='raised')
frameMeio.grid(row=1, column=0, pady=1,padx=0, sticky=NSEW)

frameBaixo  = Frame(janela, width=1043, height=300, bg=co1, relief='flat')
frameBaixo.grid(row=2, column=0,pady=0, padx=10, sticky=NSEW)

# Frame cima

root = Tk()
global app_img
app_img = Image("icons8-usuário-do-bloco-de-notas-50.png")
app_img = app_img.resize((45,45))
app_img = Tk.PhotoImage(app_img, master=root)
Label(root, image=app_img)


app_logo = Label(frameCima, image=app_img, text="Orçamento pessoal", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=7, y=5)

janela.mainloop()

#root = tk.Tk()
#photo = ImageTk.PhotoImage(image)
#label = tk.Label(root, image=photo)
#label.image = image
#label.pack()
#photo = ImageTk.PhotoImage(image, master=root)