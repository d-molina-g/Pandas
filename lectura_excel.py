import pandas as pd
path_file = "Ordenes.xlsx"

hoja = "Pedidos"
df = pd.read_excel(path_file, sheet_name = hoja)

valores_columna = df.columns.values

print(valores_columna)
print(df)
print("No muestro nada si no soy un Notebook, tengo que darle a imprimir xd")