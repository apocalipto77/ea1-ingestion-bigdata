# Proyecto Integrador de Big Data - Anderson Castrillón

## 📋 Descripción del Proyecto

Proyecto integrador de **Big Data** que implementa un **pipeline completo de ingesta, limpieza y enriquecimiento de datos**, simulando un entorno profesional en la nube con automatización mediante GitHub Actions.

### Objetivo General

Implementar un pipeline automatizado de procesamiento de datos que demuestre competencias en:
- ✅ **Ingesta de datos** desde APIs externas
- ✅ **Almacenamiento** en bases de datos
- ✅ **Limpieza y validación** de calidad
- ✅ **Enriquecimiento** desde múltiples fuentes
- ✅ **Automatización** con CI/CD (GitHub Actions)

---

## 🏗️ Estructura del Proyecto

```
Anderson_castrillon/
├── .github/
│   └── workflows/
│       └── bigdata.yml                 # Workflow automatizado (EA1+EA2+EA3)
│
├── src/
│   ├── cleaning.py                     # Script de limpieza (EA2)
│   ├── enrichment.py                   # Script de enriquecimiento (EA3)
│   │
│   ├── db/
│   │   └── ingestion.db                # BD SQLite con datos procesados
│   │
│   ├── data/                           # Archivos complementarios (EA3)
│   │   ├── location_data.csv           # Ubicación + Teléfono (CSV)
│   │   ├── company_data.json           # Empresa + Puesto (JSON)
│   │   ├── skills_data.xlsx            # Habilidades técnicas (XLSX)
│   │   ├── contact_info.xml            # Dirección + CP (XML)
│   │   ├── comments.txt                # Comentarios/Notas (TXT)
│   │   └── user_profiles.html          # Perfiles web (HTML)
│   │
│   ├── static/
│   │   └── auditoria/
│   │       ├── cleaning_report.txt     # Reporte limpieza (EA2)
│   │       └── enrichment_report.txt   # Reporte enriquecimiento (EA3)
│   │
│   └── xlsx/
│       ├── cleaned_data.xlsx           # Datos limpios (EA2)
│       └── enriched_data.xlsx          # Datos enriquecidos (EA3)
│
├── ea1_ejemplo_ingestión_de_datos_desde_un_api.py  # Script ingesta (EA1)
├── generate_enrichment_files.py        # Script generador archivos (EA3)
├── load_dataset.py                     # Script carga (EA2)
│
├── requirements.txt                    # Dependencias Python
├── setup.py                            # Configuración paquete
├── README.md                           # Este archivo
```

---

## 🔄 Pipeline de Procesamiento

```
┌──────────────────────────────────────────────────────────────────┐
│                    PIPELINE DE BIG DATA                          │
└──────────────────────────────────────────────────────────────────┘

┌─────────────────────┐
│  API JSONPlaceholder│     ← Fuente de datos externa
│  /users endpoint    │
└──────────┬──────────┘
           │ (10 usuarios)
           ▼
┌──────────────────────────────────────────┐
│        EA1: INGESTA DE DATOS             │
│  (ea1_ejemplo_ingestión_de_...)          │
│  ✅ Descarga desde API                   │
│  ✅ Almacena en SQLite                   │
│  📊 Resultado: ingestion.db              │
└──────────┬───────────────────────────────┘
           │ (10 registros × 4 columnas)
           ▼
┌──────────────────────────────────────────┐
│        EA2: LIMPIEZA DE DATOS            │
│        (src/cleaning.py)                 │
│  ✅ Elimina duplicados                   │
│  ✅ Maneja valores nulos                 │
│  ✅ Corrige tipos de datos               │
│  📊 Resultado: cleaned_data.xlsx         │
└──────────┬───────────────────────────────┘
           │ (10 registros × 4 columnas)
           ▼
┌──────────────────────────────────────────┐
│     EA3: ENRIQUECIMIENTO DE DATOS        │
│        (src/enrichment.py)               │
│  🔄 Integra 6 fuentes complementarias:   │
│     • CSV  → Ubicación + Teléfono       │
│     • JSON → Empresa + Puesto            │
│     • XLSX → Habilidades técnicas        │
│     • XML  → Dirección + CP              │
│     • TXT  → Comentarios/Notas          │
│     • HTML → Perfiles web                │
│  📊 Resultado: enriched_data.xlsx        │
└──────────────────────────────────────────┘
           │ (10 registros × 19 columnas)
           ▼
┌──────────────────────────────────────────┐
│      DATOS LISTOS PARA MODELADO          │
│      (EA4: Próxima actividad)            │
└──────────────────────────────────────────┘
```

---

## 📊 Estadísticas del Pipeline

| Métrica | Valor |
|---------|-------|
| **Registros procesados** | 10 |
| **Columnas iniciales (EA1)** | 4 |
| **Columnas después limpieza (EA2)** | 4 |
| **Columnas enriquecidas (EA3)** | 19 |
| **Incremento de información** | +375% |
| **Nuevas dimensiones agregadas** | 15 |
| **Fuentes de datos integradas** | 6 formatos |
| **Tasa de completitud** | 100% |
| **Registros coincidentes en merge** | 100% |

---

## 🚀 Instalación y Uso

### Requisitos Previos

- **Python 3.12+**
- **pip** instalado
- **git** instalado
- Conexión a Internet (para descargar de API)

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/apocalipto77/ea1-ingestion-bigdata.git
cd ea1-ingestion-bigdata
```

### 2️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

**O usando setup.py:**

```bash
pip install -e .
```

**Dependencias principales:**
- `pandas` - Procesamiento de datos
- `numpy` - Operaciones numéricas
- `openpyxl` - Generación Excel
- `requests` - Consumo de APIs
- `lxml` - Procesamiento XML

### 3️⃣ Ejecutar EA1 - Ingesta de Datos

Descarga datos desde la API JSONPlaceholder y crea la BD:

```bash
python ea1_ejemplo_ingestión_de_datos_desde_un_api.py
```

**Resultado:**
- ✅ `src/db/ingestion.db` creado con tabla `usuarios`
- ✅ 10 usuarios descargados
- ✅ `muestra_usuarios.csv` generado como evidencia
- ✅ `auditoria.txt` con detalles de la carga

### 4️⃣ Ejecutar EA2 - Limpieza de Datos

Limpia, valida y exporta datos:

```bash
python src/cleaning.py
```

**Resultados:**
- ✅ `src/xlsx/cleaned_data.xlsx` - Dataset limpio
- ✅ `src/static/auditoria/cleaning_report.txt` - Reporte de limpieza

**Operaciones realizadas:**
- Eliminación de duplicados
- Manejo de valores nulos
- Corrección de tipos de datos

### 5️⃣ Generar Archivos Complementarios (EA3)

Crea archivos en 6 formatos diferentes para enriquecimiento:

```bash
python generate_enrichment_files.py
```

**Genera en `src/data/`:**
- `location_data.csv` - Ubicación geográfica y teléfono
- `company_data.json` - Información de empresa y puesto
- `skills_data.xlsx` - Habilidades técnicas y experiencia
- `contact_info.xml` - Dirección y código postal
- `comments.txt` - Comentarios y notas adicionales
- `user_profiles.html` - Perfiles web y redes sociales

### 6️⃣ Ejecutar EA3 - Enriquecimiento de Datos

Integra todas las fuentes complementarias:

```bash
python src/enrichment.py
```

**Resultados:**
- ✅ `src/xlsx/enriched_data.xlsx` - Dataset enriquecido (19 columnas)
- ✅ `src/static/auditoria/enrichment_report.txt` - Reporte de enriquecimiento

**Operaciones realizadas:**
- Merge CSV → 4 columnas (ubicación)
- Merge JSON → 3 columnas (empresa)
- Merge XLSX → 4 columnas (habilidades)
- Merge XML → 2 columnas (contacto)
- Integración TXT → 1 columna (comentarios)
- Referencias HTML → 1 columna (perfil web)

---

## 🤖 Automatización con GitHub Actions

### Workflow Configurado

El archivo `.github/workflows/bigdata.yml` automatiza **todo el pipeline**:

**Trigger eventos:**
- ✅ En cada **push** a la rama `main`
- ✅ Manualmente (workflow_dispatch)

**Pasos ejecutados:**
1. Checkout del código
2. Setup de Python 3.12
3. Instalación de dependencias
4. Ejecución de EA2 (limpieza)
5. Ejecución de EA3 (enriquecimiento)
6. Generación de artefactos

**Artefactos generados:**
```
datos-procesados/
├── cleaned_data.xlsx
├── enriched_data.xlsx
├── cleaning_report.txt
└── enrichment_report.txt
```

**Ver ejecuciones:**
https://github.com/apocalipto77/ea1-ingestion-bigdata/actions

### Configuración del Workflow

```yaml
name: Limpieza y Enriquecimiento de Datos
on: [push, workflow_dispatch]
jobs:
  procesar:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: '3.12'
    - run: pip install pandas numpy openpyxl lxml
    - run: echo "=== Ejecutando EA2: Limpieza ===" && python src/cleaning.py
    - run: echo "=== Ejecutando EA3: Enriquecimiento ===" && python src/enrichment.py
    - uses: actions/upload-artifact@v4
      with:
        name: datos-procesados
        path: |
          src/xlsx/cleaned_data.xlsx
          src/xlsx/enriched_data.xlsx
          src/static/auditoria/cleaning_report.txt
          src/static/auditoria/enrichment_report.txt
```

---

## 📝 Trazabilidad del Proceso

### Ficheros de Auditoría

Se generan reportes detallados en cada etapa:

**`cleaning_report.txt`** (EA2)
- Cantidad de registros antes/después
- Duplicados eliminados
- Valores nulos procesados
- Tipos de datos corregidos
- Timestamp de ejecución

**`enrichment_report.txt`** (EA3)
- Resumen de bases de datos
- Archivos complementarios procesados
- Operaciones de merge realizadas
- Análisis de completitud
- Estadísticas por columna
- Observaciones y conclusiones

### Tracking en Git

Cada cambio se registra en commits:

```bash
git log --oneline

1dfbe8e EA3: Enriquecimiento - 6 fuentes integradas, 15 nuevas columnas
591e5fd Restructura: Reorganizar proyecto según estructura Anderson_castrillon
06fb9af EA2: Completo con README.md, setup.py, workflow corregido
f5abc3f EA2: Preprocesamiento limpieza datos
5db0e36 Create bigdata.yml
a39347a Merge branch 'main'
```

---

## 💾 Contenido de Datasets

### `cleaned_data.xlsx` (EA2)

10 registros × 4 columnas:
- id (INT)
- nombre (VARCHAR)
- usuario (VARCHAR)
- email (VARCHAR)

**Calidad:** 100% completo, sin duplicados, sin nulos

### `enriched_data.xlsx` (EA3)

10 registros × 19 columnas:
- **Originales:** id, nombre, usuario, email
- **De CSV:** pais, ciudad, provincia, telefono
- **De JSON:** empresa, departamento, puesto
- **De XLSX:** skill1, skill2, skill3, experiencia_anos
- **De XML:** direccion, codigo_postal
- **De TXT:** comentarios
- **De HTML:** perfil_web

**Calidad:** 100% completo, 100% en merge

---

## 🔍 Comandos Útiles

### Ver estado del repositorio
```bash
git status
git log --oneline -5
```

### Ejecutar todo el pipeline
```bash
python ea1_ejemplo_ingestión_de_datos_desde_un_api.py
python src/cleaning.py
python generate_enrichment_files.py
python src/enrichment.py
```

### Ver contenido de datos
```bash
python load_dataset.py  # Cargar y visualizar cleaned_data
```

### Limpiar archivos generados
```bash
rm -rf src/data/*
rm src/xlsx/enriched_data.xlsx
rm src/static/auditoria/enrichment_report.txt
```

---

## 📊 Recursos Generados

- **BD SQLite:** `src/db/ingestion.db`
- **Datos limpios:** `src/xlsx/cleaned_data.xlsx`
- **Datos enriquecidos:** `src/xlsx/enriched_data.xlsx`
- **Archivos complementarios:** 6 formatos en `src/data/`
- **Reportes:** 2 ficheros de auditoría en `src/static/auditoria/`
- **Scripts:** 4 archivos Python reutilizables

---

## 👨‍💻 Autor

- **Nombre:** Anderson Castrillón
- **GitHub:** [@apocalipto77](https://github.com/apocalipto77)
- **Repositorio:** [ea1-ingestion-bigdata](https://github.com/apocalipto77/ea1-ingestion-bigdata)

---

## 📚 Tecnologías Utilizadas

- **Python 3.12** - Lenguaje principal
- **Pandas** - Procesamiento y análisis de datos
- **NumPy** - Operaciones numéricas
- **SQLite3** - Base de datos
- **OpenPyXL** - Generación de archivos Excel
- **Requests** - Consumo de APIs REST
- **lxml** - Procesamiento XML
- **Git** - Control de versiones
- **GitHub Actions** - Automatización CI/CD

---

## 📄 Licencia

Este proyecto es de uso educativo como parte de la formación en Big Data.

---

## ✅ Estado del Proyecto

- **EA1 (Ingesta):** ✅ Completada
- **EA2 (Limpieza):** ✅ Completada
- **EA3 (Enriquecimiento):** ✅ Completada
- **EA4 (Modelado):** ⏳ Por definir
- **GitHub Actions:** ✅ Automatizado
- **Documentación:** ✅ Completa

**Última actualización:** 29 de Marzo de 2026  
**Última sincronización:** Commit `1dfbe8e`  
**Estado general:** ✅ Proyecto activo y funcional

---
