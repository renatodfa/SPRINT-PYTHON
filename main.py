#EXEMPLO 1

""" 
import json


# Dados fictícios sobre corridas e pilotos da Fórmula E
dados_corridas = '''
{
    "corridas": [
        {
            "id": 1,
            "local": "Mônaco",
            "data": "2024-05-15",
            "vencedor": "Piloto A",
            "equipes": ["Equipe X", "Equipe Y", "Equipe Z"]
        },
        {
            "id": 2,
            "local": "Berlim",
            "data": "2024-06-01",
            "vencedor": "Piloto B",
            "equipes": ["Equipe W", "Equipe X", "Equipe Y"]
        }
    ],
    "pilotos": [
        {
            "nome": "Piloto A",
            "nacionalidade": "Brasil",
            "equipe": "Equipe X",
            "vitorias": 5
        },
        {
            "nome": "Piloto B",
            "nacionalidade": "Alemanha",
            "equipe": "Equipe Y",
            "vitorias": 3
        }
    ]
}
'''

# Carregar os dados do JSON
dados = json.loads(dados_corridas)


# Função para exibir todas as corridas da Fórmula E
def exibir_corridas():
    print("\nCorridas da Fórmula E:")
    for corrida in dados['corridas']:
        print(
            f"ID: {corrida['id']} | Local: {corrida['local']} | Data: {corrida['data']} | Vencedor: {corrida['vencedor']}")


# Função para exibir todos os pilotos
def exibir_pilotos():
    print("\nPilotos da Fórmula E:")
    for piloto in dados['pilotos']:
        print(
            f"Nome: {piloto['nome']} | Nacionalidade: {piloto['nacionalidade']} | Equipe: {piloto['equipe']} | Vitórias: {piloto['vitorias']}")


# Função para buscar uma corrida pelo ID
def buscar_corrida_por_id(corrida_id):
    for corrida in dados['corridas']:
        if corrida['id'] == corrida_id:
            return corrida
    return None


# Função para comparar o número de vitórias entre dois pilotos
def comparar_pilotos(piloto1, piloto2):
    vitorias1 = piloto1['vitorias']
    vitorias2 = piloto2['vitorias']

    if vitorias1 > vitorias2:
        return f"{piloto1['nome']} tem mais vitórias ({vitorias1}) do que {piloto2['nome']} ({vitorias2})."
    elif vitorias1 < vitorias2:
        return f"{piloto2['nome']} tem mais vitórias ({vitorias2}) do que {piloto1['nome']} ({vitorias1})."
    else:
        return f"Ambos os pilotos têm o mesmo número de vitórias ({vitorias1})."


# Sistema interativo com o usuário
def interagir_com_usuario():
    print("Bem-vindo ao sistema de consulta da Fórmula E!")
    while True:
        print("\nEscolha uma opção:")
        print("1. Exibir todas as corridas")
        print("2. Exibir todos os pilotos")
        print("3. Buscar corrida por ID")
        print("4. Comparar vitórias de dois pilotos")
        print("5. Sair")

        escolha = input("\nDigite sua escolha: ")

        if escolha == "1":
            exibir_corridas()
        elif escolha == "2":
            exibir_pilotos()
        elif escolha == "3":
            corrida_id = int(input("Digite o ID da corrida: "))
            corrida = buscar_corrida_por_id(corrida_id)
            if corrida:
                print(
                    f"\nCorrida encontrada: Local: {corrida['local']}, Data: {corrida['data']}, Vencedor: {corrida['vencedor']}")
            else:
                print("\nCorrida não encontrada.")
        elif escolha == "4":
            piloto1_nome = input("Digite o nome do primeiro piloto: ")
            piloto2_nome = input("Digite o nome do segundo piloto: ")

            piloto1 = next((p for p in dados['pilotos'] if p['nome'] == piloto1_nome), None)
            piloto2 = next((p for p in dados['pilotos'] if p['nome'] == piloto2_nome), None)

            if piloto1 and piloto2:
                print(comparar_pilotos(piloto1, piloto2))
            else:
                print("\nUm ou ambos os pilotos não foram encontrados.")
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Escolha inválida, tente novamente.")


# Executa a interação com o usuário
interagir_com_usuario()
"""""
#EXEMPLO 2 - GRAFICO


import pandas as pd
import matplotlib.pyplot as plt

# Dados fictícios de desempenho dos pilotos
dados = {
    'Piloto': ['Piloto A', 'Piloto B', 'Piloto C'],
    'Corrida 1': [10, 8, 15],
    'Corrida 2': [12, 7, 13],
    'Corrida 3': [14, 9, 11]
}

df = pd.DataFrame(dados)
df['Total Pontos'] = df[['Corrida 1', 'Corrida 2', 'Corrida 3']].sum(axis=1)

# Gerando gráfico de desempenho
plt.plot(df['Piloto'], df['Total Pontos'], marker='o')
plt.title('Desempenho dos Pilotos')
plt.xlabel('Pilotos')
plt.ylabel('Total de Pontos')
plt.show()

