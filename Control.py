from Model import Model

class Control:
    def __init__ (self):
        self.opcao = -1
        self.mod = Model()

    def menu(self):
        self.opcao = int(input("----- Menu ------" +
                                "\n0. Sair" +
                                "\n1. Cadastrar 2 Livros" +
                                "\n2. Cadastrar Usuário" +
                                "\n3. Fazer Login" +
                                "\n4. Fazer uma Compra\n"))

    def operacao(self):
        while (self.opcao != 0):
            self.menu()#mostrar menu
            if (self.opcao == 0):
                print("Obrigado")
            elif(self.opcao == 1):
                self.mod.cadLivro()
            elif(self.opcao == 2):
                self.mod.cadUsuario()
            elif(self.opcao == 3):
                self.mod.login()
            elif(self.opcao == 4):
                self.mod.catalogo()
                self.mod.compra()
            else:
                print ("O código inserido nao é valido")


