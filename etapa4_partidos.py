"""Etapa 4: somar os votos de cada partido."""
from rich.table import Table
from etapa1_carregar import carregar_dados
from formatacao import console, numero_br

def calcular_votos_por_partido(df):
    por_partido = df.groupby("partido")["votos"].sum()
    por_partido = por_partido.sort_values(ascending=False)
    return por_partido

def mostrar_votos_por_partido(por_partido):
    total = por_partido.sum()
    tabela = Table(title="Votos por partido", header_style="bold cyan")
    tabela.add_column("Partido")
    tabela.add_column("Votos", justify="right")
    tabela.add_column("%", justify="right")
    tabela.add_column("Gráfico")
    for partido, votos in por_partido.items():
        percentual = votos / total * 100
        barra = "█" * round(percentual / 2)
        tabela.add_row(
            partido,
            numero_br(votos),
            numero_br(percentual, 1),
            f"[green]{barra}[/]",
        )
    console.print(tabela)

# --- DESAFIO: COPIA TROCANDO "partido" POR "estado" ---
def calcular_votos_por_estado(df):
    por_estado = df.groupby("estado")["votos"].sum()
    por_estado = por_estado.sort_values(ascending=False)
    return por_estado

def mostrar_votos_por_estado(por_estado):
    total = por_estado.sum()
    tabela = Table(title="Votos por estado", header_style="bold cyan")
    tabela.add_column("Estado")
    tabela.add_column("Votos", justify="right")
    tabela.add_column("%", justify="right")
    tabela.add_column("Gráfico")
    for estado, votos in por_estado.items():
        percentual = votos / total * 100
        barra = "█" * round(percentual / 2)
        tabela.add_row(
            estado,
            numero_br(votos),
            numero_br(percentual, 1),
            f"[blue]{barra}[/]",
        )
    console.print(tabela)

if __name__ == "__main__":
    df = carregar_dados()

    por_partido = calcular_votos_por_partido(df)
    mostrar_votos_por_partido(por_partido)

    print() # pula uma linha
    por_estado = calcular_votos_por_estado(df)
    mostrar_votos_por_estado(por_estado)