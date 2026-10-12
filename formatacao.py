"""Ferramentas de exibição usadas por todas as etapas."""

from rich.console import Console

# O "console" do rich é o que imprime tabelas e cores no terminal.
# Criamos um só aqui e todas as etapas usam o mesmo.
console = Console()

def numero_br(valor, casas=0):
    """Escreve um número no padrão brasileiro. Ex.: 1008 -> '1.008' e 41.6 -> '41,6'."""
    # O Python escreve no padrão americano: 1008.5 vira "1,008.5"
    texto = f"{valor:,.{casas}f}"

    # Precisamos trocar "," por "X" e "." por ",".
    # Usamos um "X" temporário para as trocas não se misturarem.
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")
    return texto