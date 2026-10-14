from disciplina import Disciplina
class Aluno:
    def __init__(self , nome , rm , aula):
        self.nome = nome
        self.rm = rm
        self.aula = aula
        ## diciplinas serve para guardar cada diciplina na qual o aluno se matriculou 
        self.disciplinas = []
        self.notas_por_disciplina= {}
    
    def __str__(self):
        return f"Aluno: {self.nome} - RM: {self.rm} - Aula: {self.aula}"
    
    def mostrar_info(self):
        print(self)
    
    def matricular(self , d:Disciplina):
        self.disciplinas.append(d)
        self.notas_por_disciplina.setdefault(d.ids, [])
    
    def adicionar_nota(self , d:Disciplina , nota:float):
        self.notas_por_disciplina[d.ids].append(nota)
        print(f"Notas de {d.materia}({d.profe}): {self.notas_por_disciplina[d.ids]}")
    
    def mostrar_notas(self, d:Disciplina):
        return f"Notas de {d.materia}({d.profe}): {self.notas_por_disciplina[d.ids]}"
    
    def calcular_media(self , d:Disciplina)->float:
        notas = self.notas_por_disciplina.get(d.ids, [])
        if not notas:
            return
        return round(sum(notas)/len(notas), 2)
    
    def calcular_media_geral(self)->float:
        if not self.disciplinas:
            return None
        medias = []
        for d in self.disciplinas:
            media = self.calcular_media(d)
            if media is not None:
                medias.append(media)
        if medias == []:
            return []
        return round(sum(medias)/len(medias) , 2)