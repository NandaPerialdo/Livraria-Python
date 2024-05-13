class Model:

    def __init__ (self):
        #metodo construtor
        self.codLivro = -1
        self.coletar = ""
        self.titulos = []
        self.qtLivro = []
        self.valorLivro = []
        self.id = 0
        self.i = 0
        

    def cadLivro(self):
        self.i = 0
        for self.i in range(0, 2):
            self.coletar = input(f"\nInsira o titulo do {self.i + 1}º livro: ")
            self.titulos.append(self.coletar)
            self.coletar = input("Insira o valor: ")
            self.valorLivro.append(self.coletar)
            self.coletar = input("Insira a quantidade: ")
            self.qtLivro.append(self.coletar)

    def catalogo(self):
        self.i = 0
        print("----CATÁLOGO----\n")
        for self.i in range(0, 2):
            print(f"Livro {self.i + 1}: {self.titulos[self.i]}\n"
                  f"Valor: {self.valorLivro[self.i]}\n"
                  f"Quantidade {self.qtLivro[self.i]}\n")

    def compra(self):
        self.id = int(input("Insira o código do livro que deseja: "))
        if self.qtLivro[self.id - 1] == "0":
            self.escolha = int(input("\nLivro Insisponível!\n"
                  "Deseja fazer uma reserva?\n"
                  "1.Sim.\n"
                  "2.Não.\n"))
            if self.escolha == 1:
                print("\nLivro Reservado!")
            else:
                print("Obrigado!Volte Sempre!")
        else:
            print(f"\nResumo da compra:\n"
                  f"Livro: {self.titulos[self.id - 1]}\n"
                  f"Valor: {self.valorLivro[self.id - 1]}\n"
                  f"Quantidade: 1\n")

            self.idCartao = int(input("Insira o numero do cartão: "))

            print("\nCompra Efetuada!\n"
                  "Agradecemos a preferência :)\n")


    def cadUsuario(self):
        self.nome = input("Qual nome do usuário?: ")
        self.cpf = int(input("Informe o CPF: "))
        self.cadLogin = input("Crie um nome de login: ")
        self.cadSenha = int(input("Crie uma senha numérica: "))

    def login(self):
        self.login = input("Informe seu login: ")
        self.senha = input("Informe sua senha: ")







