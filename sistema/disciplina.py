class Disciplina:
    def __init__(self , profe , materia , ids):
        self.profe= profe
        self.materia = materia
        self.ids= ids
        
    def __str__(self):
        return f"ID: {self.ids} - Professor: {self.profe} - Materia: {self.materia}"