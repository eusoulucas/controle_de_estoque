#import the libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

def cria_janprodutos():

	def mostra_prod():
		classe = lista_classes.get(ACTIVE)
		for item in database.ponta1.execute("SELECT * FROM Produtos WHERE Classe = ?", classe):
			lista_produtos.insert(END, item)
			
	janela_inv = Tk()
	janela_inv.title('Inventário')
	janela_inv.geometry("600x600")
	janela_inv.attributes('-alpha', 0.9)
	janela_inv.iconbitmap(default = 'logoicone.ico')

	frame_classes = Frame(janela_inv, bg = 'black')
	frame_classes.place(relx = '0', rely = '0', relwidth = '0.3', relheight = '1')

	frame_produtos = Frame(janela_inv, bg = 'white')
	frame_produtos.place(relx = '0.3', rely = '0', relwidth = '0.7', relheight = '1')

	lista_classes = Listbox(frame_classes, bg = 'black', fg = 'gray', font = 'Arial 11', relief = 'groove',
		selectmode = 'SINGLE', selectbackground = 'gray')
	lista_classes.place(relx = '0.09', rely = '0.05', relwidth = '0.8', relheight = '0.75')

	for item in database.ponta1.execute("SELECT Classe FROM Produtos"):
		lista_classes.insert(END, item)

	lista_produtos = Listbox(frame_produtos, bg = 'black', fg = 'gray', font = 'Arial 11', relief = 'groove',
		selectmode = 'SINGLE', selectbackground = 'gray')
	lista_produtos.place(relx = '0.09', rely = '0.05', relwidth = '0.8', relheight = '0.75')

	bt_mostraprod = Button(frame_classes, text = "Mostrar produtos da classe", bg = 'black', fg = 'white', command = mostra_prod)
	bt_mostraprod.place(relx = '0.08', rely = '0.87', relwidth = '0.85', relheight = '0.08')

def logar():
	usuario = usuario_en.get()
	senha = senha_en.get()

	database.ponta.execute('''
		SELECT * FROM Usuarios
		WHERE (usuario = ? and senha = ?)
		''', (usuario, senha))

	verificar = database.ponta.fetchone()

	if(usuario in verificar and senha in verificar):
		janela_main.destroy()
		cria_janprodutos()
	else:
		messagebox.showerror(title = "Informação de login", message = "Dados incorretos ou usuário inexistente")	

def registrar():
	def voltar():
		#removendo widgets
		botao_registrar.place(rely = '1000')
		botao_voltar.place(rely = '1000')
		nome_lb.place(relx = '1000')
		nome_en.place(relx = '1000')
		mail_lb.place(relx = '1000')
		mail_en.place(relx = '1000')

		#voltando os outros botoes
		botao_login.place(rely = '0.52', relx = '0.2')
		botao_registro.place(rely = '0.65', relx = '0.2')

	def registrardb():
		nome = nome_en.get()
		usuario = usuario_en.get()
		senha = senha_en.get()
		mail = mail_en.get()
		
		if(nome == "" and mail == "" and senha == "" and usuario == ""):
			messagebox.showerror(title = 'Erro de registro', message = 'Preencha todos os campos')
		else:
			database.ponta.execute("""
			INSERT INTO Usuarios(Nome, Email, Usuario, Senha)
			VALUES(?, ?, ?, ?)
			""", (nome, mail, usuario, senha))
			database.coneccao.commit()
			messagebox.showinfo(title = 'Informação de Registro', message = 'Conta criada com sucesso!')

	# gambiarra pra remover botôes
	botao_login.place(relx = '1000000')
	botao_registro.place(relx = '1000000')

	#inserindo widgets de cadastro
	nome_lb = Label(login, text = 'Nome:', bg = 'black', fg = 'white', font = ("Century Ghotic", 12))
	nome_lb.place(relx = '0.07', rely = '0.1')

	nome_en = ttk.Entry(login)
	nome_en.place(relx = '0.17', rely = '0.11', relwidth = '0.35')

	mail_lb = Label(login, text = 'E-Mail:', bg = 'black', fg = 'white', font = ("Century Ghotic", 12))
	mail_lb.place(relx = '0.06', rely = '0.54')

	mail_en = ttk.Entry(login)
	mail_en.place(relx = '0.17', rely = '0.55', relwidth = '0.35')

	#inserindo botões do cadastro
	botao_registrar = ttk.Button(login, text = 'Salvar', command = registrardb)
	botao_registrar.place(rely = '0.67', relx = '0.2')

	botao_voltar = ttk.Button(login, text = 'Voltar', command = voltar)
	botao_voltar.place(rely = '0.80', relx = '0.2')

janela_main = Tk()
janela_main.title('LE Sistemas - Painel de Acesso')
janela_main.geometry('600x300')
janela_main.configure(bg = 'white')
janela_main.attributes('-alpha', 0.9)
janela_main.iconbitmap(default = 'logoicone.ico')

logo = PhotoImage(file = 'logo.png')

logo_reis = Frame(janela_main)
logo_reis.place( relheight = '1', relwidth = '0.45')

login = Frame(janela_main, bg = 'black')
login.place(relx = '0.45', relheight = '1', relwidth = '1')

logo_lb = Label(logo_reis, image = logo)
logo_lb.place(relx = '0.2', rely = '0.2')

usuario_lb = Label(login, text = 'Usuário:', bg = 'black', fg = 'white', font = ("Century Ghotic", 12))
usuario_lb.place(relx = '0.05', rely = '0.25')

usuario_en = ttk.Entry(login)
usuario_en.place(relx = '0.17', rely = '0.26', relwidth = '0.35')

senha_lb = Label(login, text = 'Senha:', bg = 'black', fg = 'white', font = ("Century Ghotic", 12))
senha_lb.place(relx = '0.06', rely = '0.4')

senha_en = ttk.Entry(login, show = '*')
senha_en.place(relx = '0.17', rely = '0.41', relwidth = '0.35')

botao_login = ttk.Button(login, text = 'Log in', command = logar)
botao_login.place(rely = '0.52', relx = '0.2')

botao_registro = ttk.Button(login, text = 'Registrar', command = registrar)
botao_registro.place(rely = '0.65', relx = '0.2')

janela_main.mainloop()