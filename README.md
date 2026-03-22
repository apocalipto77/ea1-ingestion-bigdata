# EA1 - Ingesta y Limpieza de Datos (Big Data)

## 📋 Descripción del Proyecto

Proyecto integrador de **Big Data** que implementa un pipeline completo de ingesta, validación y limpieza de datos simulando un entorno en la nube.

### Objetivo
Implementar un pipeline automatizado que:
- ✅ **Ingiere datos** desde una API pública (JSONPlaceholder)
- ✅ **Almacena** en base de datos SQLite
- ✅ **Limpia y valida** datos (elimina duplicados, maneja nulos, corrige tipos)
- ✅ **Genera evidencias** (Excel + auditoría)
- ✅ **Automatiza** con GitHub Actions

---

## 🏗️ Estructura del Proyecto

```
project-root/
├── .github/
│   └── workflows/
│       └── bigdata.yml                 # Workflow automatizado
├── src/
│   └── db/
│       └── cleaning.py                 # Script de limpieza (EA2)
├── db/
│   └── datos_api.db                    # BD SQLite con datos
├── xlsx/
│   └── cleaned_data.xlsx               # Datos limpios exportados
├── static/
│   └── auditoria/
│       └── cleaning_report.txt         # Reporte de auditoría
├── ea1_ejemplo_ingestión_de_datos_desde_un_api.py  # Ingesta (EA1)
├── requirements.txt                    # Dependencias
├── setup.py                            # Configuración del paquete
└── README.md                           # Este archivo
```

---

## 🚀 Instalación y Uso

### Requisitos Previos
- **Python 3.12+**
- **pip** instalado
- **git** instalado

### 1. Clonar el Repositorio
```bash
git clone https://github.com/apocalipto77/ea1-ingestion-bigdata.git
cd ea1-ingestion-bigdata
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

O usando setup.py:
```bash
pip install -e .
```

### 3. Ejecutar EA1 (Ingesta de Datos)
Descarga datos desde la API JSONPlaceholder y crea la BD:
```bash
python ea1_ejemplo_ingestión_de_datos_desde_un_api.py
```

**Resultado:** Se crea `db/datos_api.db` con tabla `usuarios` (10 registros)

### 4. Ejecutar EA2 (Limpieza de Datos)
Limpia, valida y exporta datos:
```bash
python src/db/cleaning.py
```

**Resultados:**
- `xlsx/cleaned_data.xlsx` - Datos limpios en Excel
- `static/auditoria/cleaning_report.txt` - Reporte detallado

---

## 📊 Pipeline de Datos

```
┌─────────────────────┐
│  API JSONPlaceholder │  (JSONPlaceholder.com/users)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   EA1: Ingestión    │  (ea1_ejemplo_ingestión_de_datos_desde_un_api.py)
│   SQLite Database   │  → db/datos_api.db
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  EA2: Limpieza      │  (src/db/cleaning.py)
│  - Duplicados       │
│  - Valores nulos    │
│  - Tipos de datos   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Evidencias:       │
│  • cleaned_data.xlsx│
│  • cleaning_report  │
└─────────────────────┘
```

---

## 🔄 Automatización con GitHub Actions

El workflow en `.github/workflows/bigdata.yml` se ejecuta automáticamente en cada:
- **push** a la rama `main`
- **workflow_dispatch** (ejecución manual)

### Qué hace el Workflow:
1. Descarga el código
2. Instala Python 3.12 + dependencias
3. Ejecuta el script de limpieza
4. Genera artefactos (Excel + auditoría)
5. Carga evidencias como artifact

**Ver ejecuciones:** https://github.com/apocalipto77/ea1-ingestion-bigdata/actions

---

## 📝 Documentación de Datos

### Entrada (API JSONPlaceholder)
Tabla `usuarios` con campos:
- `id` (INT) - Identificador único
- `name` (VARCHAR) - Nombre del usuario
- `username` (VARCHAR) - Nombre de usuario
- `email` (VARCHAR) - Email
- Campos adicionales JSON

### Salida (Datos Limpios)
Excel `cleaned_data.xlsx` con:
- ✅ Sin duplicados
- ✅ Sin valores nulos
- ✅ Tipos de datos correctos
- ✅ 10 registros procesados

### Auditoría
Archivo `cleaning_report.txt` documenta:
- Registros antes/después
- Operaciones ejecutadas
- Timestamp de ejecución

---

## 🔧 Requisitos Técnicos

### Stack Tecnológico
- **Lenguaje:** Python 3.12
- **BD:** SQLite3
- **Procesamiento:** Pandas + NumPy
- **Exportación:** OpenPyXL (Excel)
- **Automatización:** GitHub Actions
- **Control de versiones:** Git

### Dependencias
```
requests      # Consumo de APIs
pandas        # Análisis y limpieza de datos
numpy         # Operaciones numéricas
openpyxl      # Generación de archivos Excel
```

---

## 📊 Resultados Esperados

Después de ejecutar el pipeline completo:

```
✅ Base de datos creada: db/datos_api.db
✅ Datos limpios exportados: xlsx/cleaned_data.xlsx
✅ Reporte de auditoría: static/auditoria/cleaning_report.txt
✅ GitHub Actions ejecutado: logs en Actions tab
```

---

## 👨‍💻 Autor

- **Nombre:** Anderson Castrillón
- **GitHub:** [@apocalipto77](https://github.com/apocalipto77)
- **Repositorio:** [ea1-ingestion-bigdata](https://github.com/apocalipto77/ea1-ingestion-bigdata)

---

## 📚 Referencias

- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## 📄 Licencia

Este proyecto es de uso educativo como parte de la formación en Big Data.

---

**Estado:** ✅ Completo (EA1 + EA2)  
**Última actualización:** 22 de Marzo de 2026  
**GitHub Actions:** ✅ Automatizado
