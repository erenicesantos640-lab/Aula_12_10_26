"""Etapa 5: descobrir o prefeito eleito em cada cidade."""
from rich.table import Table
from etapa1_carregar import carregar_dados
from formatacao import console, numero_br

def calcular_vencedores(df):
    prefeitos = df[df["cargo"] == "Prefeito"]
    por_candidato = prefeitos.groupby(
        ["estado", "cidade", "candidato", "partido"], as_index=False
    )["votos"].sum()
    total_da_cidade = por_candidato.groupby("cidade")["votos"].transform("sum")
    por_candidato["percentual"] = (por_candidato["votos"] / total_da_cidade * 100).round(1)
    ordenado = por_candidato.sort_values("votos", ascending=False)
    vencedores = ordenado.drop_duplicates("cidade")
    return vencedores.sort_values("cidade")

def mostrar_vencedores(vencedores):
    tabela = Table(title="Prefeitos eleitos", header_style="bold cyan")
    tabela.add_column("UF")
    tabela.add_column("Cidade")
    tabela.add_column("Candidato", style="bold")
    tabela.add_column("Partido")
    tabela.add_column("Votos", justify="right")
    tabela.add_column("%", justify="right")
    for _, linha in vencedores.iterrows():
        tabela.add_row(
            linha["estado"], linha["cidade"], linha["candidato"],
            linha["partido"], numero_br(linha["votos"]),
            numero_br(linha["percentual"], 1),
        )
    console.print(tabela)

# --- DESAFIO ---
def calcular_vencedores_vereador(df):
    vereadores = df[df["cargo"] == "Vereador"]
    por_candidato = vereadores.groupby(
        ["estado", "cidade", "candidato", "partido"], as_index=False
    )["votos"].sum()
    total_da_cidade = por_candidato.groupby("cidade")["votos"].transform("sum")
    por_candidato["percentual"] = (por_candidato["votos"] / total_da_cidade * 100).round(1)
    ordenado = por_candidato.sort_values("votos", ascending=False)
    vencedores = ordenado.drop_duplicates("cidade")
    return vencedores.sort_values("cidade")

def mostrar_vencedores_vereador(vencedores):
    tabela = Table(title="Vereadores mais votados", header_style="bold magenta")
    tabela.add_column("UF")
    tabela.add_column("Cidade")
    tabela.add_column("Candidato", style="bold")
    tabela.add_column("Partido")
    tabela.add_column("Votos", justify="right")
    tabela.add_column("%", justify="right")
    for _, linha in vencedores.iterrows():
        tabela.add_row(
            linha["estado"], linha["cidade"], linha["candidato"],
            linha["partido"], numero_br(linha["votos"]),
            numero_br(linha["percentual"], 1),
        )
    console.print(tabela)

if __name__ == "__main__":
    df = carregar_dados()
    
    vencedores = calcular_vencedores(df)
    mostrar_vencedores(vencedores)
    
    print()
    vencedores_vereador = calcular_vencedores_vereador(df)
    mostrar_vencedores_vereador(vencedores_vereador)