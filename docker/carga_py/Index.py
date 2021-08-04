from LerArquivos import LerArquivos
from BancoDeDados import BancoDeDados

class Index:

    def __init__(self, folder: str) -> None:
        self.lerArquivos = LerArquivos()
        self.lerArquivos.lerDiretorio(folder)
        self.bancoDeDados = BancoDeDados()
        self.bancoDeDados.removerPhotos()
        self.lerArquivos.inserirNovasImagens(folder)



index = Index('archive_imagens')
# index = Index('standard_test_images')

