class Model:

    def __init__ (self):
        #metodo construtor
        self.codLivro = -1
        self.nLivro = ""
        self.vLivro = ""
        self.qtLivro = 0

    def cadLivro(self):
        self.i = 0
        for self.i in range(0, 2):
            self.nLivro = input(f"Insira o nome do {self.i + 1}º livro: ")
            self.vLivro = float(input("Insira o valor: "))
            self.qtLivro = int(input("Insira a quantidade: "))
            print("\n")

    def catalogo(self):
        print("--- Catálogo ---")
        for self.i in range(0, 4):
            print(f"Livro {self.i + 1}:\n"
                  f"Nome: {self.nLivro}\n"
                  f"Valor: R$ {self.vLivro}\n"
                  f"Quantidade: {self.qtLivro}\n")

    def compra(self):
        self.escolha = int(input("Digite o código do livro desejado."))

        for self.qtLivro in range (self.escolha):
            self.reserva = int(input("Livro Indisponível\n\n"
                  "Deseja fazer uma reserva?\n"
                  "1.Sim"
                  "2.Não"))
            if (self.reserva == 1):
                print("Livro reservado! :)")
            else:
                print("Obrigado! Volte sempre :)")
        else:
            print("Resumo da compra:")

    def cadUsuario(self):
        self.nome = input("Qual nome do usuário?: ")
        self.cpf = int(input("Informe o CPF: "))
        self.cadLogin = input("Crie um nome de login: ")
        self.cadSenha = int(input("Crie uma senha numérica: "))

    def login(self):
        self.login = input("Informe seu login: ")
        self.senha = input("Informe sua senha: ")







