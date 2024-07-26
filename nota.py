from dataclasses import dataclass

@dataclass
class Notas:
    def __init__(self, nota1=0.0, nota2=0.0):
        self.nota1 = nota1
        self.nota2 = nota2