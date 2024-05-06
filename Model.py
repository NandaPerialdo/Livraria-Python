class Model:

    def __init__ (self):
        #metodo construtor
        self.codLivro = -1
        self.coletar = 0
        self.livroUm = []
        self.livroDois = []

    def cadLivro(self):
            self.coletar = input("Insira o nome do 1º livro: ")
            self.livroUm.insert(0, self.coletar)
            self.coletar = float(input("Insira o valor: "))
            self.livroUm.insert(1, self.coletar)
            self.coletar = int(input("Insira a quantidade: "))
            self.livroUm.insert(2, self.coletar)
            self.coletar = input("\nInsira o nome do 2º livro: ")
            self.livroDois.insert(0, self.coletar)
            self.coletar = float(input("Insira o valor: "))
            self.livroDois.insert(1, self.coletar)
            self.coletar = int(input("Insira a quantidade: "))
            self.livroDois.insert(2, self.coletar)
            print("\n")

    def catalogo(self):
        print(f"Livro 1\n Nome: {self.livroUm[0]}\n Valor: R$ {self.livroUm[1]}\n Quantidade: {self.livroUm[2]}\n")
        print(f"Livro 2\n Nome: {self.livroDois[0]}\n Valor: R$ {self.livroDois[1]}\n Quantidade: {self.livroDois[2]}\n")

    def compra(self):
        self.escolha = int(input("Digite o código do livro desejado: "))

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







