import pandas as pd
archivo = pd.read_csv("resultados.csv")
final = {
        "nacional_math": 0,
        "performance_math": 0,
        "mejor_resultado":0
    }
def estadisticas(final):
    mat = archivo["PUNT_MATEMATICAS"]
    baq = archivo[(archivo["ESTU_MCPIO_RESIDE"]=="BARRANQUILLA")]
    baqprom = (baq["PUNT_MATEMATICAS"]).mean()
    promath = mat.mean()
    if(promath > baqprom):
        mejorN_L = promath
        Naci_loc = "Nacional"
    else:
        mejorN_L = baqprom
        Naci_loc = "local"
    ofi= archivo[(archivo["COLE_NATURALEZA"]=="OFICIAL")]
    noofi= archivo[(archivo["COLE_NATURALEZA"]=="NO OFICIAL")]
    promofi = (ofi["PUNT_MATEMATICAS"]).mean()
    promnoofi = (noofi["PUNT_MATEMATICAS"]).mean()
    if(promofi > promnoofi):
        mejor = promofi
        naturaleza = "OFICIAL"
    else:
        mejor = promnoofi
        naturaleza = "NO OFICIAL"
    final = {
        "nacional_math": promath,
        "performance_math": (mejorN_L, Naci_loc),
        "mejor_resultado": (mejor, naturaleza)
    }
    return final
print(estadisticas(final))