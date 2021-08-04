from typing import BinaryIO

class Photo:

  def __init__(self, id, name, file):
    self.id : int = id
    self.name: str = name
    self.file: BinaryIO = file


