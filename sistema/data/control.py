import back
import json
from pathlib import Path

## Função que comverte os dados para dados de json
ARQUIVO_DADOS = Path(__file__).with_name("dados.json")
def salvar_dados():
    dados = {
        "alunos" : [
            {
            "nome" : aluno.nome,
            "rm" : aluno.rm,
            "aula" : aluno.aula,
            "disciplinas" : [
                    disciplina.ids
                    for disciplina in aluno.disciplinas
                ],
            "notas_por_disciplina" : aluno.notas_por_disciplina,
            }
            for aluno in back.alunos.values()
        ],
        "disciplinas" : [
            {
            "ids" : disciplina.ids,
            "profe" : disciplina.profe,
            "materia" : disciplina.materia
            }
            for disciplina in back.materias.values()
        ]
    }
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            indent=2,
            ensure_ascii=False
        )

## Função que vai carregar dados salvos antes de começar a execução
def carregar_dados():
    global alunos , materias
    
    if not ARQUIVO_DADOS.exists():
        return
    
    try:
        with open(ARQUIVO_DADOS , "r" , encoding= "utf-8") as arquivo:
            dados = json.load(arquivo)
    except json.JSONDecodeError:
        print("Json não valido")
        return
    
    materias_carregadas = {}
    alunos_carregados = {}
    
    for dados_disciplina in dados.get("disciplinas" , []):
        disciplina = back.Disciplina(
            dados_disciplina["profe"],
            dados_disciplina["materia"],
            dados_disciplina["ids"]
        )
        materias_carregadas[disciplina.ids] = disciplina

    for dados_aluno in dados.get("alunos" , []):
        aluno = back.Aluno(
            dados_aluno["nome"],
            dados_aluno["rm"],
            dados_aluno["aula"]
        )
        
        for id_disciplina in dados_aluno.get("disciplinas", []):
            disciplina = materias_carregadas.get(id_disciplina)
            if disciplina is not None:
                aluno.matricular(disciplina)

        notas_salvas = dados_aluno.get("notas_por_disciplina", {})
        aluno.notas_por_disciplina = {
            int(id_disciplina) : notas
            for id_disciplina , notas in notas_salvas.items()
        }
        for disciplina in aluno.disciplinas:
            aluno.notas_por_disciplina.setdefault(disciplina.ids, [])
        
        alunos_carregados[aluno.rm] = aluno
        
    back.materias = materias_carregadas
    back.alunos = alunos_carregados

## Função que vai mudar uma informação de um aluno ou disciplina
def mudar_info(tipo , objeto , nome):
    if not ARQUIVO_DADOS.exists():
        print("Nenhum dado salvo encontrado")
        return
        
    if tipo == 1:
        for aluno in back.alunos.values():
            if aluno == objeto:
                aluno.nome = nome
                break
    elif tipo == 2:
        for aluno in back.alunos.values():
            if aluno == objeto:
                aluno.aula = nome
                break
    elif tipo == 3:
        for materia in back.materias.values():
            if materia == objeto:
                materia.profe = nome
                break
    elif tipo == 4:
        for materia in back.materias.values():
            if materia == objeto:
                materia.materia = nome
                break
    salvar_dados()
    print("=== Mudança realizada ===")

## Apaga uma disciplina ou um aluno do banco de dados
def apagar_info(tipo , objeto):
    if not ARQUIVO_DADOS.exists():
        return
        
    if tipo == 1:
        for aluno in back.alunos.keys():
            if objeto.rm == aluno:
                back.alunos.pop(objeto.rm)
                break
    elif tipo == 2:
        for disciplina in back.materias.keys():
            if objeto.ids == disciplina:
                back.materias.pop(objeto.ids)
                break
        for aluno in back.alunos.values():
            if objeto in aluno.disciplinas:
                aluno.disciplinas.remove(objeto)
                aluno.notas_por_disciplina.pop(objeto.ids , None)
                
    salvar_dados()
    print("=== Informação apagada ===")