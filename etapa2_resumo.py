"""Etapa 2: mostrar um quadro com os totais gerais."""
from rich.panel import Panel
from etapa1_carregar import carregar_dados
from formatacao import console, numero_br

def mostrar_resumo(df):
    total_registros = len(df) # quantidade de linhas
    total_votos = df["votos"].sum() # soma da coluna votos
    total_cidades = df["cidade"].nunique() # quantas cidades diferentes
    total_candidatos = df["candidato"].nunique() # quantos candidatos diferentes
    # [bold]...[/] é a forma do rich deixar o texto em negrito
    texto = (
        f"[bold]Registros:[/] {numero_br(total_registros)}\n"
        f"[bold]Votos:[/] {numero_br(total_votos)}\n"
        f"[bold]Cidades:[/] {total_cidades}\n"
        f"[bold]Candidatos:[/] {total_candidatos}\n"
    )
    # Panel desenha uma caixa com titulo em volta do texto
    console.print(Panel(texto, title="Eleições 2024 (dados fictícios)", expand=False))

if __name__ == "__main__":
    df = carregar_dados()
    mostrar_resumo(df)