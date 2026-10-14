# Importando as classes
from aluno import Aluno
from disciplina import Disciplina
from data import control
import os
import random 

# Função para limpar o terminal
def limpar():
    return os.system('cls' if os.name == 'nt' else 'clear')

def validar_info(texto):
    while True:
        nome = input(texto).strip().title()
        if any(char.isdigit() for char in nome):
            print("Nome não permitido")
        elif not nome:
            print("Informação vazia")
        else:
            limpar()
            return nome

## Funções para o Aluno
alunos = {}
def add_aluno():
    limpar()
    aluno = validar_info("Digite o seu nome: ")
    
    while True:
        rm = random.randint(100000, 999999)
        if rm not in alunos:
            break
    
    sala = input("Digite a sua sala: ").strip()
    if not sala:
        print("Informação da sala invalida")
        return
        
    aluno_criado = Aluno(aluno , rm , sala)
    alunos[rm] = aluno_criado
    control.salvar_dados()
    print(f"Aluno: {aluno} - sala: {sala}")
    print("== Aluno cadastrado com sucesso ==")

def mostrar_alunos():
    limpar()
    if not alunos:
        print("Alunos não cadastrados ainda")
        return
    
    aluno_busca = validar_info("Digite o seu nome:")
    encontrado = False
    for rm , aluno in alunos.items():
        if aluno_busca in aluno.nome:
            encontrado = True
            aluno.mostrar_info()
    if not encontrado:
        print("Aluno não encontrado")
        return

## Funções para a Disciplina
## materias guarda as diciplinas com o ids como chave 
materias = {}
def add_aula():
    limpar()
    nome_profe = validar_info("Digite o nome do professor: ")
    aula = validar_info("Digite o nome da disciplina: ")
    
    while True:
        ids = random.randint(100,999)
        if ids not in materias:
            break
    
    materia = Disciplina(nome_profe,aula,ids)
    materias[ids] = materia
    control.salvar_dados()
    print(f"Professor: {nome_profe} - materia: {aula}")
    print("== Disciplina cadastrada com sucesso ==")

def info_aulas():
    limpar()
    if not materias:
        print("Nenhuma disciplina foi adicionada ainda")
        return
    
    print("\nDisciplinas disponiveis:")
    for i , disciplina in enumerate(materias):
        print(i+1 ,'-', materias[disciplina])

def info_aluno():
    limpar()
    print("\nAlunos cadastrados:")
    for i , aluno in enumerate(alunos):
        print(i+1,'- ',end='')
        alunos[aluno].mostrar_info()

## Escolha de aluno ou disciplina
def escolha_aluno():
    info_aluno()
    if not alunos:
        print("Alunos não cadastrados ainda")
        return
    
    nome_aluno_num = int(input("Escolha o aluno: "))
    if nome_aluno_num > len(alunos) or nome_aluno_num <=0:
        return
    
    nome_aluno = [*alunos.keys()][nome_aluno_num - 1]
    return alunos[nome_aluno]

def escolha_disciplina():
    info_aulas()
    escolha_materia_num = int(input("Escolha a disciplina: "))
    if escolha_materia_num > len(materias) or escolha_materia_num <=0:
        return 
    
    escolha_materia = [*materias.keys()][escolha_materia_num - 1]
    return materias[escolha_materia]

## Função de matricula
def matricular_aluno():
    limpar()
    if not alunos or not materias:
        print("Aluno ou disciplina não adicionados")
        return
    
    try:
        aluno = escolha_aluno()
        if aluno is None:
            print("Escolha invalida")
            return
        disciplina = escolha_disciplina()
        if disciplina is None:
            print("Escolha invalida")
            return
        if disciplina in aluno.disciplinas:
            print("Aluno já foi matriculado nesta disciplina")
            return
    except ValueError:
        print("Informação invalida")
        return
    
    aluno.matricular(disciplina)
    control.salvar_dados()
    print(f"O aluno {aluno.nome}(sala: {aluno.aula}) esta matriculado em:", end=' ')
    for d in aluno.disciplinas:
        print(f"{d.materia}({d.profe})", end=" | ")

## Funões das notas
def add_nota():
    limpar()
    if not alunos or not materias:
        print("Aluno ou disciplina não adicionados")
        return
    
    try:
        aluno = escolha_aluno()
        if aluno is None:
            print("Escolha invalida")
            return
        disciplina = escolha_disciplina()
        if disciplina is None:
            print("Escolha invalida")
            return
        if disciplina not in aluno.disciplinas:
            print("O aluno não foi cadastrado nesta aula")
            return
        nota = float(input("Digite a nota: "))
        if nota < 0 or nota > 10:
            print("Nota invalida")
            return
    except ValueError:
            print("Informação invalida")
            return
        
    aluno.adicionar_nota(disciplina, nota)
    control.salvar_dados()
    print("== Nota adicionada com sucesso ==")

def mostrar_notas():
    limpar()
    if not alunos or not materias:
        print("Aluno ou disciplinas não adicionados")
        return
    
    try:
        aluno = escolha_aluno()
        if aluno is None:
            print("Escolha invalida")
            return
        disciplina = escolha_disciplina()
        if disciplina is None:
            print("Escolha invalida")
            return
        if disciplina not in aluno.disciplinas:
            print("O aluno não foi cadastrado nesta aula")
            return
    except ValueError:
        print("Informação invalida")
        return
    
    if not aluno.notas_por_disciplina:
        print("Não tem notas")
        return
    print(aluno.mostrar_notas(disciplina))

## Funções de medias
def media():
    limpar()
    if not alunos or not materias:
        print("Nenhum aluno ou materia adicionados ainda")
        return
    
    try:
        aluno = escolha_aluno()
        if aluno is None:
            print("Escolha invalida")
            return
        disciplina = escolha_disciplina()
        if disciplina is None:
            print("Escolha invalida")
            return
        if disciplina not in aluno.disciplinas:
            print("O aluno não foi cadastrado nesta aula")
            return
    except ValueError:
        print("Informação invalida")
        return
    
    media = aluno.calcular_media(disciplina)
    if media is None:
        print("Não tem notas")
        return
    
    print(f"O aluno tem uma media de {media} em {disciplina.materia}({disciplina.profe})")

def media_geral():
    limpar()
    if not alunos or not materias:
        print("Nenhum aluno ou materia adicionados ainda")
        return
    
    try:
        aluno = escolha_aluno()
        if aluno is None:
            print("Escolha invalida")
            return
    except ValueError:
        print("Informação invalida")
        return
    
    media = aluno.calcular_media_geral()
    if media is None:
        print("O aluno não foi matriculado")
        return
    elif media == []:
        print("Não tem notas")
        return
    
    print(f"A media geral do aluno {aluno.nome} é {media}")

def atualizar(tipo):
    limpar()
    if not alunos and not materias:
        print("Nenhum aluno ou materia adicionados ainda")
        return
    
    if tipo == 1:
        try:
            aluno = escolha_aluno()
            if aluno is None:
                print("Escolha invalida")
                return
        except ValueError:
            print("Informação invalida")
            return
        dado = input("Qual dado vai mudar(Nome/Aula): ").strip().lower()
        if dado == 'nome':
            nome = validar_info("Digite o nome: ")
            control.mudar_info(1 , aluno, nome)
        elif dado == 'aula':
            nome = input("Digite a aula: ").strip()
            control.mudar_info(2 , aluno, nome)
        else:
            print("Informação invalida")
    else:
        try:
            disciplina = escolha_disciplina()
            if disciplina is None:
                print("Escolha invalida")
                return
        except ValueError:
            print("Informação invalida")
            return
        dado = input("Qual dado vai mudar(Professor/Materia): ").strip().lower()
        if dado == 'professor':
            nome = validar_info("Digite o nome do professor: ")
            control.mudar_info(3 , disciplina, nome)
        elif dado == 'materia':
            nome = validar_info("Digite a materia: ")
            control.mudar_info(4 , disciplina, nome)
        else:
            print("Informação invalida")

def apagar(tipo):
    limpar()
    if not alunos and not materias:
        print("Nenhum aluno ou materias adicionadas ainda")
        return
    
    if tipo == 1:
        try:
            aluno = escolha_aluno()
            if aluno is None:
                print("Escolha invalida")
                return
            control.apagar_info(1 , aluno)
        except ValueError:
            print("Informação invalida")
    else:
        try:
            disciplina = escolha_disciplina()
            if disciplina is None:
                print("Escolha invalida")
                return
            control.apagar_info(2 , disciplina)
        except ValueError:
            print("Informação invalida")