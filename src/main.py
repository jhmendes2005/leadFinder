from tkinter import *
import autoSearch
from utils import get_key

api_key = get_key.get_api_key()

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 30
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 30
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 30
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 30
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 30
        self.sextoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="SearchLeads_V1")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.locLabel = Label(self.segundoContainer,text="Loc. Inicial:", font=self.fontePadrao)
        self.locLabel.pack(side=LEFT)
        self.loc = Entry(self.segundoContainer)
        self.loc["width"] = 30
        self.loc["font"] = self.fontePadrao
        self.loc.pack(side=LEFT)

        self.keywordsLabel = Label(self.terceiroContainer, text="Palavras chave:", font=self.fontePadrao)
        self.keywordsLabel.pack(side=LEFT)
        self.keywords = Entry(self.terceiroContainer)
        self.keywords["width"] = 30
        self.keywords["font"] = self.fontePadrao
        ##self.keywords["show"] = "*"
        self.keywords.pack(side=LEFT)

        self.raioLabel = Label(self.quartoContainer, text="Raio de busca:", font=self.fontePadrao)
        self.raioLabel.pack(side=LEFT)
        self.raio = Entry(self.quartoContainer)
        self.raio["width"] = 30
        self.raio["font"] = self.fontePadrao
        self.raio.pack(side=LEFT)

        self.search = Button(self.quintoContainer)
        self.search["text"] = "BUSCAR DADOS"
        self.search["font"] = ("Calibri", "8")
        self.search["width"] = 12
        self.search["command"] = self.buscaInit
        self.search.pack()
        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def buscaInit(self):
        locInit = self.loc.get()
        locInit = f"{locInit}"
        keywordsInit: str = self.keywords.get()
        keywords = []
        
        def noEmpty(x):
            return x != ""

        keywords = list(filter(noEmpty, keywordsInit.split(' ')))

        print(keywordsInit)
        radInit = self.raio.get()
        radInit = f"{radInit}"
        self.mensagem["text"] = "Gerando busca..."
        
        #busca = autoSearch.start(locInit, radInit, keywords, 12371283)
        busca = autoSearch.start('-23.550520,-46.633308', 50000, keywords, 12371283, api_key)
        print(busca)


root = Tk()
Application(root)
root.title("SearchLeads - V0.0.1")
root.geometry("750x500")
root.mainloop()





location = '-23.550520,-46.633308' # Latitude e longitude do centro da área de busca
radius = '50000' # Raio de busca em metros
keywords = ['restaurante', 'cafeteria', 'bar'] # Palavras-chave a serem buscadas