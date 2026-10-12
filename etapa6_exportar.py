"""Etapa 6: salvar o resultado em um novo arquivo CSV."""
from etapa1_carregar import carregar_dados
from etapa5_vencedores import calcular_vencedores
from etapa4_partidos import calcular_votos_por_partido
from formatacao import console

CAMINHO_RESULTADO = "dados/resultado_prefeitos.csv"
CAMINHO_VOTOS_PARTIDO = "dados/votos_partido.csv"

def salvar_csv(tabela):
    tabela.to_csv(
        CAMINHO_RESULTADO,
        index=False,
        sep=";",
        decimal=",",
        encoding="utf-8-sig",
    )
    console.print(f"Resultado salvo em: {CAMINHO_RESULTADO}")

# --- DESAFIO ---
def salvar_votos_partido(por_partido):
    # por_partido é uma Series, então transformamos em tabela com reset_index
    # fica com colunas "partido" e "votos"
    tabela = por_partido.reset_index()
    tabela.columns = ["partido", "votos"]
    tabela.to_csv(
        CAMINHO_VOTOS_PARTIDO,
        index=False,
        sep=";",
        decimal=",",
        encoding="utf-8-sig",
    )
    console.print(f"Votos por partido salvos em: {CAMINHO_VOTOS_PARTIDO}")

if __name__ == "__main__":
    df = carregar_dados()

    vencedores = calcular_vencedores(df)
    salvar_csv(vencedores)

    por_partido = calcular_votos_por_partido(df)
    salvar_votos_partido(por_partido)