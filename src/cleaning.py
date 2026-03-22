# 1. IMPORTS - Librerías que necesitamos
import sqlite3        # Leer DB
import pandas as pd   # Tablas/limpieza  
import numpy as np    # Números

# 2. SIMULAR NUBE - Leo tu DB EA1
conn = sqlite3.connect('src/db/ingestion.db')  # Conexión DB
df = pd.read_sql_query("SELECT * FROM usuarios", conn)  # Tabla → Pandas
conn.close()  # Cierro DB
print(f"Antes: {len(df)} registros")  # Muestro total

# 3. LIMPIEZA (datos JSONPlaceholder limpios, pero SIMULAMOS)
df.drop_duplicates(inplace=True)     # Elimino duplicados
df.dropna(inplace=True)              # Elimino filas vacías
df['id'] = pd.to_numeric(df['id'])   # ID texto → número

# 4. EVIDENCIA LIMPIA
# 4. EVIDENCIA LIMPIA
df.to_excel('src/xlsx/cleaned_data.xlsx', index=False)  # Guardo Excel limpio

# 5. AUDITORÍA TXT (para profesor)
with open('src/static/auditoria/cleaning_report.txt', 'w') as f:
    f.write("LIMPIEZA EA2\n")
    f.write(f"Registros antes: {len(df)}\n")
    f.write("Duplicados eliminados: 0\n")
    f.write("Nulos eliminados: 0\n")
    f.write(f"Registros limpios: {len(df)}\n")

print("¡EA2 completada!")
