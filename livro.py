#contruir lista ligada
#encoding:utf-8
import os

class Book():
    def __init__(self, titulo=None, autor=None,resumo=None):
        self.titulo = titulo
        self.autor = autor
        self.resumo = resumo
        self.next = None
    def describe(self):
        print("Titulo: ",self.titulo)
        print("Autor: ",self.autor)
        print("Resumo da obra: \n",self.resumo)

first = Book()
now=first
ultimo =first

while(True):
    #os.system("clear")
    print("Entre sua opção:")
    print("<1> Cadastrar livro")
    print("<2> Listar livros")
    print("<3> Pesquisar")
    print("<4> Sair")
    option=raw_input("your option: ")
    if(option=="1"):
        titulo = raw_input("Entre o titulo: ")
        autor = raw_input("Entre o autor: ")
        resumo = raw_input("Breve resumo: ")

        book=Book(titulo,autor,resumo)

        if(first.titulo == None):
            first=book
            ultimo=first
        else:
            ultimo.next=book
            ultimo=ultimo.next
    elif(option=="2"):
        now=first
        while(True):
            print(now.titulo)

            if(now.next==None):
                break
            else:
                now=now.next
    elif(option=="3"):
        #os.system("clear")

        print("Pesquisa")
        titulo_livro = raw_input("Entre o titulo do livro: ")

        now=first
        while(True):
            if(now.titulo!=titulo_livro):
                now=now.next
            else:
                now.describe()
                break



    elif(option=="4"):
        break

print ("the end..!")