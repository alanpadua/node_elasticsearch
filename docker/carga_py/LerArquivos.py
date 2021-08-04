from Photo import Photo
from pathlib import Path
from mimetypes import MimeTypes
import magic
import os
from BancoDeDados import BancoDeDados


class LerArquivos:
    def __init__(self) -> None:
        self.folder = 'standard_test_images'
        self.bancoDeDados = BancoDeDados()

    def lerDiretorio(self, folder: str):
        i = 0
        for diretorio, subpastas, arquivos in os.walk(folder):
            print(f"diretório: {diretorio}")

            for nm_arquivo in arquivos:
                i += 1
                row_file = os.path.join(diretorio, nm_arquivo)
                print(f"{i}: {row_file}")

    def inserirNovasImagens(self, folder: str):
        mime = MimeTypes()
        i = 0
        for diretorio, subpastas, arquivos in os.walk(folder):
            print(f"diretório: {diretorio}")

            for nm_arquivo in arquivos:
                i += 1
                row_file = os.path.join(diretorio, nm_arquivo)
                print(f"{i}: {row_file}")

                photo = Photo(i, nm_arquivo, self.convertFileToBlob(row_file))
                print(photo)

                self.bancoDeDados.inserirPhotos(photo)

                blobFile = self.convertFileToBlob(row_file)

    def convertFileToBlob(self, arquivo: str):
        with open(arquivo, 'rb') as file:
            binaryData = file.read()
        return binaryData
