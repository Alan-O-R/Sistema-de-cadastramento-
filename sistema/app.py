## Importações
import back
from data import control

## Menu principal
def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("[1]- Opções para o Aluno")
        print("[2]- Opções para o Professor")
        print("[3]- Atualizar dados")
        print("[4]- Apagar dado")
        print('[0]- Sair')
        opt = input("Escolha uma opção:")
        if opt == '1':
            back.limpar()
            print("=== Menu do Aluno ===")
            print("[1]- Adicionar aluno")
            print("[2]- Exibir informação do aluno")
            print("[3]- Matricular aluno em uma disciplina")
            print("[4]- Mostrar notas")
            print("[ENTER]- Voltar")
            opt = input("Escolha uma opção:")
            if opt == '1':
                back.add_aluno()
            elif opt == '2':
                back.mostrar_alunos()
            elif opt == '3':
                back.matricular_aluno()
            elif opt == '4':
                back.mostrar_notas()
            elif opt == '':
                continue
            else:
                print("Opção não permitida")
        elif opt == '2':
            back.limpar()
            print("=== Menu do Professor")
            print("[1]- Adicionar disciplina")
            print("[2]- Listar disciplinas")
            print("[3]- Adicionar Nota do aluno")
            print("[4]- Media do Aluno")
            print("[5]- Media geral de um Aluno")
            print("[ENTER]- Voltar")
            opt = input("Escolha uma opção:")
            if opt == '1':
                back.add_aula()
            elif opt == '2':
                back.info_aulas()
            elif opt == '3':
                back.add_nota()
            elif opt == '4':
                back.media()
            elif opt == '5':
                back.media_geral()
            elif opt == '':
                continue
            else:
                print("Opção não permitida")
        elif opt == '3':
            back.limpar()
            print("[1]- Atualizar aluno")
            print("[2]- Atualizar Disciplina")
            print("[ENTER]- Voltar")
            opt = input("Escolha uma opção: ")
            if opt == '1':
                back.atualizar(1)
            elif opt == '2':
                back.atualizar(2)
            elif opt == '':
                continue
            else:
                print("Opção invalida")
        elif opt == '4':
            back.limpar()
            print("[1]- Apagar aluno")
            print("[2]- Apagar Disciplina")
            print("[ENTER]- Voltar")
            opt = input("Escolha uma opção: ")
            if opt == '1':
                back.apagar(1)
            elif opt == '2':
                back.apagar(2)
            elif opt == '':
                continue
            else:
                print("Opção invalida")
        elif opt == '0':
                back.limpar()
                print("Saindo....")
                break
        else:
            print("Opção não permitida")

if __name__=='__main__':
    control.carregar_dados()
    menu()