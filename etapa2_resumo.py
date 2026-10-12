import pandas as pd

def gerar_resumo():
    # antes era: df
    dados_eleitorais = pd.read_csv("dados/eleicoes.csv")

    # antes eram: total_registros, total_votos, etc
    quantidade_registros = len(dados_eleitorais)
    soma_votos = dados_eleitorais['votos'].sum()
    numero_municipios = dados_eleitorais['cidade'].nunique()
    quantidade_candidatos = dados_eleitorais['candidato'].nunique()

    # antes era: texto
    mensagem_resumo = (
        f"Registros: {quantidade_registros} "
        f"Votos: {soma_votos:,.0f} "
        f"Cidades: {numero_municipios} "
        f"Candidatos: {quantidade_candidatos}"
    )
    
    print(mensagem_resumo)
    return mensagem_resumo

if __name__ == "__main__":
    gerar_resumo()