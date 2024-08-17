from tkinter import *
from tkinter import ttk

################# Cores ###############
 
co0 = "#444466"  # Preta
co1 = "#feffff"  # Branca
co2 = "#4065a1"  # Azul
 
janela = Tk()
janela.title('Calculadora de IMC')

# Obtendo as dimensões da tela do usuário
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calculando as dimensões desejadas
largura_janela = largura_tela
altura_janela = int(altura_tela * 0.8)

# Definindo o tamanho da janela e centralizando
pos_x = 0
pos_y = int((altura_tela - altura_janela) / 2)
janela.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

janela.configure(bg=co1)

################# Frames ####################
frame_cima = Frame(janela, width=largura_janela, height=50, bg=co1, pady=0, padx=0, relief="flat")
frame_cima.grid(row=0, column=0, sticky=NSEW)
 
frame_baixo = Frame(janela, width=largura_janela, height=altura_janela-50, bg=co1, pady=0, padx=0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW)
 
style = ttk.Style(janela)
style.theme_use("clam")

# ---------------- Configurações do Frame cima ---------------------
 
app_nome = Label(frame_cima, text="Calculadora de IMC", width=23, height=1, padx=0, relief="flat", anchor="center", font=('Ivy 16 bold'), bg=co1, fg=co0)
app_nome.place(relx=0.5, rely=0.5, anchor=CENTER)
 
app_linha = Label(frame_cima, text="", width=largura_janela, height=1, padx=0, relief="flat", anchor="nw", font=('Arial 1'), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

# ---------------- Configurações do Frame_baixo ---------------------
 
# Margens para os elementos
left_margin = 520
right_margin = 520
 
l_peso = Label(frame_baixo, text="Insira seu peso", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_peso.grid(row=0, column=0, sticky=E, pady=5, padx=(left_margin, 5))
e_peso = Entry(frame_baixo, width=15, font=('Ivy 10 bold'), justify='center', relief=SOLID)
e_peso.grid(row=0, column=1, sticky=W, pady=5, padx=(5, 0))
 
l_altura = Label(frame_baixo, text="Insira sua altura", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_altura.grid(row=1, column=0, sticky=E, pady=5, padx=(left_margin, 5))
e_altura = Entry(frame_baixo, width=15, font=('Ivy 10 bold'), justify='center', relief=SOLID)
e_altura.grid(row=1, column=1, sticky=W, pady=5, padx=(5, 0))
 
l_resultado = Label(frame_baixo, width=5, text="---", height=1, padx=6, pady=12, relief="flat", anchor="center", font=('Ivy 24 bold'), bg=co2, fg=co1)
l_resultado.grid(row=0, column=1, rowspan=2, padx=(0,300), pady=15)

l_resultado_texto = Label(frame_baixo, width=37, text="", height=1, padx=0, pady=12, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_resultado_texto.grid(row=2, column=0, columnspan=3, pady=10)

# ------------ Função para calcular o IMC ------------------
def calcular():
    try:
        peso = float(e_peso.get())
        altura = float(e_altura.get())**2
        resultado = peso / altura

        if resultado < 18.6:
            l_resultado_texto['text'] = "Seu IMC é: Abaixo do peso"
        elif resultado >= 18.5 and resultado < 24.9:
            l_resultado_texto['text'] = "Seu IMC é: Normal"
        elif resultado >= 25 and resultado < 29.9:
            l_resultado_texto['text'] = "Seu IMC é: Sobrepeso"
        else:
            l_resultado_texto['text'] = "Seu IMC é: Obesidade"
        
        l_resultado['text'] = "{:.2f}".format(resultado)
    except ValueError:
        l_resultado_texto['text'] = "Erro: Insira valores válidos"

# ------------ Função para limpar os campos ------------------
def limpar_campos():
    e_peso.delete(0, END)
    e_altura.delete(0, END)
    l_resultado['text'] = "---"
    l_resultado_texto['text'] = ""

# ------------ Botão calcular ------------------
b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=15, height=1, overrelief=SOLID, bg=co2, fg="white", font=('Ivy 10 bold'), anchor="center", relief=RAISED)
b_calcular.grid(row=3, column=0, pady=10, padx=(left_margin, 5))

# ------------ Botão limpar ------------------
b_limpar = Button(frame_baixo, command=limpar_campos, text="Limpar", width=15, height=1, overrelief=SOLID, bg=co0, fg="white", font=('Ivy 10 bold'), anchor="center", relief=RAISED)
b_limpar.grid(row=3, column=1, pady=10, padx=(5, right_margin))

# Ajustando para centralizar os botões
frame_baixo.grid_columnconfigure(0, weight=1)
frame_baixo.grid_columnconfigure(1, weight=1)
frame_baixo.grid_columnconfigure(2, weight=1)

janela.mainloop()

