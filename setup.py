"""
Setup configuration for EA1 Big Data Project
Ingesta y Limpieza de Datos desde API
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ea1-ingestion-bigdata",
    version="1.0.0",
    author="Anderson Castrillón",
    author_email="anderson@example.com",
    description="Pipeline de ingesta y limpieza de datos desde API y BD SQLite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apocalipto77/ea1-ingestion-bigdata",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.12",
    install_requires=[
        "requests>=2.31.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "openpyxl>=3.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "flake8>=6.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ea1-ingest=ea1_ejemplo_ingestión_de_datos_desde_un_api:main",
            "ea2-clean=src.db.cleaning:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
