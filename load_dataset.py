import pandas as pd
import sqlite3

print("="*60)
print("CARGANDO DATASET LIMPIO - ACTIVIDAD 2")
print("="*60)

# Opción 1: Desde Excel
print("\n1. Cargando desde Excel (src/xlsx/cleaned_data.xlsx)...")
df_excel = pd.read_excel('src/xlsx/cleaned_data.xlsx')
print(f"   ✅ {len(df_excel)} registros cargados")
print(f"   ✅ Columnas: {list(df_excel.columns)}")

# Opción 2: Desde BD SQLite
print("\n2. Cargando desde BD SQLite (src/db/ingestion.db)...")
conn = sqlite3.connect('src/db/ingestion.db')
df_db = pd.read_sql_query("SELECT id, nombre, usuario, email FROM usuarios", conn)
conn.close()
print(f"   ✅ {len(df_db)} registros cargados")

# Mostrar datos
print("\n" + "="*60)
print("MUESTRA DEL DATASET LIMPIO:")
print("="*60)
print(df_excel.to_string(index=False))

print("\n" + "="*60)
print("RESUMEN ESTADÍSTICO:")
print("="*60)
print(f"Total de registros: {len(df_excel)}")
print(f"Usuarios únicos: {df_excel['usuario'].nunique()}")
print(f"Emails únicos: {df_excel['email'].nunique()}")
print(f"Registros con email válido: {df_excel['email'].notna().sum()}")
