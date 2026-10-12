from etapa1_carregar import carregar_dados
from etapa2_resumo import mostrar_resumo
from etapa3_amostra import mostrar_amostra
from etapa4_partidos import calcular_votos_por_partido, mostrar_votos_por_partido
from etapa5_vencedores import calcular_vencedores, mostrar_vencedores
from etapa6_exportar import salvar_csv

df = carregar_dados()
mostrar_resumo(df)
mostrar_amostra(df)

por_partido = calcular_votos_por_partido(df)
mostrar_votos_por_partido(por_partido)

vencedores = calcular_vencedores(df)
mostrar_vencedores(vencedores)

salvar_csv(vencedores)