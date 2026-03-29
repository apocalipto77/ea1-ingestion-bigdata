"""
Script para generar archivos complementarios en diferentes formatos
para enriquecimiento de datos - Actividad 3
"""
import pandas as pd
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

print("="*70)
print("GENERANDO ARCHIVOS COMPLEMENTARIOS PARA ENRIQUECIMIENTO")
print("="*70)

# Datos base que usaremos para los 10 usuarios
base_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'usuario': ['Bret', 'Antonette', 'Samantha', 'Karianne', 'Kamren', 
                'Leopoldo_Corkery', 'Elwyn.Skiles', 'Maxime_Nienow', 'Delphine', 'Moriah.Stanton']
}

# ============================================================================
# 1. CSV - UBICACIÓN GEOGRÁFICA Y CONTACTO
# ============================================================================
print("\n1️⃣  Generando CSV (Ubicación)...")
csv_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'pais': ['USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA'],
    'ciudad': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
               'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'provincia': ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'TX', 'CA', 'TX', 'CA'],
    'telefono': ['+1-212-555-0145', '+1-323-555-0198', '+1-312-555-0156', 
                 '+1-713-555-0143', '+1-602-555-0147', '+1-215-555-0142',
                 '+1-210-555-0159', '+1-619-555-0154', '+1-972-555-0181',
                 '+1-408-555-0165']
}
df_csv = pd.DataFrame(csv_data)
df_csv.to_csv('src/data/location_data.csv', index=False)
print("   ✅ Archivo: src/data/location_data.csv")

# ============================================================================
# 2. JSON - INFORMACIÓN DE EMPRESA
# ============================================================================
print("\n2️⃣  Generando JSON (Empresa)...")
json_data = [
    {'id': 1, 'empresa': 'Acme Corp', 'departamento': 'IT', 'puesto': 'Senior Developer'},
    {'id': 2, 'empresa': 'Tech Solutions', 'departamento': 'Backend', 'puesto': 'Backend Engineer'},
    {'id': 3, 'empresa': 'Innovatech', 'departamento': 'Frontend', 'puesto': 'Frontend Lead'},
    {'id': 4, 'empresa': 'Digital Hub', 'departamento': 'Cloud', 'puesto': 'Cloud Architect'},
    {'id': 5, 'empresa': 'Data Systems', 'departamento': 'Analytics', 'puesto': 'Data Scientist'},
    {'id': 6, 'empresa': 'Code Factory', 'departamento': 'QA', 'puesto': 'QA Manager'},
    {'id': 7, 'empresa': 'Web Devs Inc', 'departamento': 'Frontend', 'puesto': 'UI/UX Designer'},
    {'id': 8, 'empresa': 'Cloud Native', 'departamento': 'DevOps', 'puesto': 'DevOps Engineer'},
    {'id': 9, 'empresa': 'AI Solutions', 'departamento': 'Research', 'puesto': 'ML Engineer'},
    {'id': 10, 'empresa': 'Cyber Secure', 'departamento': 'Security', 'puesto': 'Security Officer'}
]
with open('src/data/company_data.json', 'w') as f:
    json.dump(json_data, f, indent=2)
print("   ✅ Archivo: src/data/company_data.json")

# ============================================================================
# 3. XLSX - HABILIDADES TÉCNICAS
# ============================================================================
print("\n3️⃣  Generando XLSX (Habilidades)...")
xlsx_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'skill1': ['Python', 'Java', 'JavaScript', 'Go', 'R', 
               'C++', 'HTML/CSS', 'Bash', 'Python', 'Network'],
    'skill2': ['SQL', 'Spring', 'React', 'Kubernetes', 'Python',
               'Testing', 'Vue.js', 'Docker', 'TensorFlow', 'Linux'],
    'skill3': ['Git', 'Microservices', 'Node.js', 'AWS', 'Data Analysis',
               'Selenium', 'TypeScript', 'CI/CD', 'PyTorch', 'Firewall'],
    'experiencia_anos': [8, 6, 5, 7, 4, 5, 6, 7, 5, 9]
}
df_xlsx = pd.DataFrame(xlsx_data)
df_xlsx.to_excel('src/data/skills_data.xlsx', index=False)
print("   ✅ Archivo: src/data/skills_data.xlsx")

# ============================================================================
# 4. XML - DATOS DE CONTACTO ADICIONALES
# ============================================================================
print("\n4️⃣  Generando XML (Contacto)...")
root = ET.Element('contactos')
contactos = [
    {'id': '1', 'direccion': '123 Main St', 'codigo_postal': '10001'},
    {'id': '2', 'direccion': '456 Oak Ave', 'codigo_postal': '90001'},
    {'id': '3', 'direccion': '789 Pine Rd', 'codigo_postal': '60601'},
    {'id': '4', 'direccion': '321 Elm St', 'codigo_postal': '77001'},
    {'id': '5', 'direccion': '654 Maple Drive', 'codigo_postal': '85001'},
    {'id': '6', 'direccion': '987 Cedar Lane', 'codigo_postal': '19101'},
    {'id': '7', 'direccion': '147 Birch Blvd', 'codigo_postal': '78201'},
    {'id': '8', 'direccion': '258 Spruce Way', 'codigo_postal': '92101'},
    {'id': '9', 'direccion': '369 Willow Ct', 'codigo_postal': '75201'},
    {'id': '10', 'direccion': '741 Ash Court', 'codigo_postal': '95101'}
]
for contacto in contactos:
    elem = ET.SubElement(root, 'contacto')
    for key, value in contacto.items():
        child = ET.SubElement(elem, key)
        child.text = str(value)

xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
with open('src/data/contact_info.xml', 'w') as f:
    f.write(xml_str)
print("   ✅ Archivo: src/data/contact_info.xml")

# ============================================================================
# 5. TXT - COMENTARIOS/NOTAS
# ============================================================================
print("\n5️⃣  Generando TXT (Comentarios)...")
comentarios = """COMENTARIOS Y NOTAS DE USUARIOS
================================================================================

ID 1 - Bret:
- Empleado destacado con 8 años de experiencia
- Especialista en soluciones backend
- Certificación en AWS (2024)
- Disponibilidad: Tiempo completo

ID 2 - Antonette:
- Ingeniero con fuerte experiencia en arquitectura de microservicios
- Liderazgo en equipo de 5 desarrolladores
- Capacitación en Spring Boot completada
- Disponibilidad: Remoto

ID 3 - Samantha:
- Experta frontend con portafolio destacado
- Desarrolladora especializada en React y Vue.js
- Proyecto personal destacado: Landing page para startup
- Disponibilidad: Híbrido

ID 4 - Karianne:
- Arquitecto en la nube con experiencia en AWS y GCP
- Certificación CKA (Kubernetes)
- Mentor en programa de jóvenes talentos
- Disponibilidad: Tiempo completo

ID 5 - Kamren:
- Científico de datos con formación en estadística
- Publicaciones en análisis de big data
- Certificación en scikit-learn y pandas
- Disponibilidad: Flexible

ID 6 - Leopoldo_Corkery:
- QA Manager con experiencia en automatización
- Implementación de framework de testing
- Certificación en Selenium y pytest
- Disponibilidad: Tiempo completo

ID 7 - Elwyn.Skiles:
- Diseñador UX/UI con portfol io en Dribbble
- Especialista en usabilidad web
- Certificación en UX Research
- Disponibilidad: Freelance

ID 8 - Maxime_Nienow:
- DevOps Engineer con 7 años en infraestructura cloud
- Experto en Docker y Kubernetes
- Certificación Docker DCA
- Disponibilidad: Tiempo completo

ID 9 - Delphine:
- Machine Learning Engineer especializado en NLP
- Publicaciones en conferencias de AI
- Experiencia con TensorFlow y PyTorch
- Disponibilidad: Remoto

ID 10 - Moriah.Stanton:
- Oficial de seguridad con 9 años de experiencia
- Certificación CISSP (2023)
- Especialista en firewall y VPN
- Disponibilidad: Tiempo completo

================================================================================
Fecha de generación: 2026-03-29
Fuente: Sistema de recursos humanos
Total de registros: 10
"""
with open('src/data/comments.txt', 'w', encoding='utf-8') as f:
    f.write(comentarios)
print("   ✅ Archivo: src/data/comments.txt")

# ============================================================================
# 6. HTML - PERFIL WEB
# ============================================================================
print("\n6️⃣  Generando HTML (Perfil)...")
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Perfiles de Usuarios - Sistema de RRHH</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .perfil { border: 1px solid #ddd; padding: 10px; margin: 10px 0; }
        .id { font-weight: bold; color: #0066cc; }
    </style>
</head>
<body>
    <h1>Perfiles de Usuarios del Sistema</h1>
    <div class="perfil">
        <p class="id">ID: 1 | Usuario: Bret</p>
        <p>LinkedIn: <a href="https://linkedin.com/in/bret-acmecorp">linkedin.com/in/bret</a></p>
        <p>GitHub: <a href="https://github.com/bret1">github.com/bret1</a></p>
        <p>Website: <a href="https://bret-portfolio.com">bret-portfolio.com</a></p>
    </div>
    <div class="perfil">
        <p class="id">ID: 2 | Usuario: Antonette</p>
        <p>LinkedIn: <a href="https://linkedin.com/in/antonette-tech">linkedin.com/in/antonette</a></p>
        <p>GitHub: <a href="https://github.com/antonette2">github.com/antonette2</a></p>
    </div>
    <div class="perfil">
        <p class="id">ID: 3 | Usuario: Samantha</p>
        <p>LinkedIn: <a href="https://linkedin.com/in/samantha-frontend">linkedin.com/in/samantha</a></p>
        <p>Portfolio: <a href="https://samantha-designs.com">samantha-designs.com</a></p>
    </div>
    <div class="perfil">
        <p class="id">ID: 4 | Usuario: Karianne</p>
        <p>LinkedIn: <a href="https://linkedin.com/in/karianne-cloud">linkedin.com/in/karianne</a></p>
        <p>GitHub: <a href="https://github.com/karianne4">github.com/karianne4</a></p>
    </div>
    <div class="perfil">
        <p class="id">ID: 5 | Usuario: Kamren</p>
        <p>ResearchGate: <a href="https://researchgate.net/profile/Kamren">researchgate.net/profile/Kamren</a></p>
        <p>GitHub: <a href="https://github.com/kamren-data">github.com/kamren-data</a></p>
    </div>
    <div class="perfil">
        <p class="id">ID: 6 | Usuario: Leopoldo_Corkery</p>
        <p>LinkedIn: <a href="https://linkedin.com/in/leopoldo-qa">linkedin.com/in/leopoldo</a></p>
        <p>Blog QA: <a href="https://qa-automation-blog.com">qa-automation-blog.com</a></p>
    </div>
    <div class="perfil">
        <p class="id">ID: 7 | Usuario: Elwyn.Skiles</p>
        <p>Dribbble: <a href="https://dribbble.com/elwyn-design">dribbble.com/elwyn</a></p>
        <p>Behance: <a href="https://behance.net/elwyn">behance.net/elwyn</a></p>
    </div>
    <div class="perfil">
        <p class="id">ID: 8 | Usuario: Maxime_Nienow</p>
        <p>LinkedIn: <a href="https://linkedin.com/in/maxime-devops">linkedin.com/in/maxime</a></p>
        <p>Medium: <a href="https://medium.com/@maxime-devops">medium.com/@maxime</a></p>
    </div>
    <div class="perfil">
        <p class="id">ID: 9 | Usuario: Delphine</p>
        <p>LinkedIn: <a href="https://linkedin.com/in/delphine-ml">linkedin.com/in/delphine</a></p>
        <p>Kaggle: <a href="https://kaggle.com/delphine-ml">kaggle.com/delphine</a></p>
    </div>
    <div class="perfil">
        <p class="id">ID: 10 | Usuario: Moriah.Stanton</p>
        <p>LinkedIn: <a href="https://linkedin.com/in/moriah-security">linkedin.com/in/moriah</a></p>
        <p>Blog: <a href="https://cybersecurity-insights.com">cybersecurity-insights.com</a></p>
    </div>
</body>
</html>
"""
with open('src/data/user_profiles.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("   ✅ Archivo: src/data/user_profiles.html")

# ============================================================================
# RESUMEN
# ============================================================================
print("\n" + "="*70)
print("✅ ARCHIVOS GENERADOS EXITOSAMENTE:")
print("="*70)
print("""
📋 CSV   → src/data/location_data.csv       (Ubicación + Teléfono)
📄 JSON  → src/data/company_data.json       (Empresa + Puesto)
📊 XLSX  → src/data/skills_data.xlsx        (Habilidades técnicas)
🏢 XML   → src/data/contact_info.xml        (Dirección + Código postal)
📝 TXT   → src/data/comments.txt            (Comentarios/Notas)
🌐 HTML  → src/data/user_profiles.html      (Perfiles web)

Total archivos: 6
Total formatos diferentes: 6
Registros por archivo: 10
Clave de unión: ID (común en todos)
""")

print("="*70)
print("🎯 LISTO PARA ENRIQUECIMIENTO")
print("="*70)
