"""Etapa 2: mostrar um quadro com os totais gerais."""
from rich.panel import Panel
from etapa1_carregar import carregar_dados
from formatacao import console, numero_br

def mostrar_resumo(df):
    total_registros = len(df)
    total_votos = df["votos"].sum()
    total_cidades = df["cidade"].nunique()
    total_candidatos = df["candidato"].nunique()
    total_partidos = df["partido"].nunique() # <-- NOVO

    texto = (
        f"[bold]Registros:[/] {numero_br(total_registros)} "
        f"[bold]Votos:[/] {numero_br(total_votos)} "
        f"[bold]Cidades:[/] {total_cidades} "
        f"[bold]Candidatos:[/] {total_candidatos} "
        f"[bold]Partidos:[/] {total_partidos}" # <-- NOVO
    )
    console.print(Panel(texto, title="Eleições 2024 (dados fictícios)", expand=False))

if __name__ == "__main__":
    df = carregar_dados()
    mostrar_resumo(df)