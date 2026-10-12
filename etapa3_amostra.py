"""Etapa 3: mostrar as primeiras linhas dos dados em uma tabela."""
from rich.table import Table
from etapa1_carregar import carregar_dados
from formatacao import console

def mostrar_amostra(df, linhas=5):
    # 1. Adicionei "zona" aqui
    colunas = ["estado", "cidade", "zona", "secao", "cargo", "candidato", "partido", "votos"]

    tabela = Table(title=f"Primeiras {linhas} linhas", header_style="bold cyan")

    for coluna in colunas:
        tabela.add_column(coluna)

    for _, linha in df.head(linhas).iterrows():
        valores = [str(linha[coluna]) for coluna in colunas]
        tabela.add_row(*valores)

    console.print(tabela)

if __name__ == "__main__":
    df = carregar_dados()
    # 2. Mudei de 5 para 10 aqui
    mostrar_amostra(df, 10)