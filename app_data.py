# -*- coding: utf-8 -*-
"""
Contenido del portfolio.
Edita este fichero para actualizar el stack, los proyectos o los datos de contacto:
no hace falta tocar el HTML.
"""

PROFILE = {
    "name": "Alberto Piedra Venegas",
    "role": "Desarrollador Big Data, IA & Desarrollo Web",
    "tagline": (
        "Me apasiona crear software y aprender nuevas tecnologías. Desarrollo aplicaciones web, "
        "soluciones de datos e inteligencia artificial, siempre con ganas de seguir creciendo."
    ),
    "email": "albertopiedra155@gmail.com",
    "github": "https://github.com/YellowAlberto",
    # Pega aquí la URL de tu perfil, p. ej. "https://www.linkedin.com/in/tu-usuario/".
    # Si lo dejas vacío, el botón no se muestra.
    "linkedin": "https://www.linkedin.com/in/alberto-piedra-venegas/",
    # Ruta del CV dentro de /static, p. ej. "docs/cv-alberto-piedra.pdf".
    # Si lo dejas vacío, el botón no se muestra.
    "cv": "",
    # URL pública de la web (se usa en la vista previa al compartir el enlace).
    "site_url": "https://portfolio-eight-green-ikjuxpkmp9.vercel.app",
    "location": "España",
}

# Categorías de tecnologías para la sección "Stack"
# "icon" es un emoji: ligero, sin dependencias externas, y encaja con el resto del diseño.
STACK = [
    {
        "category": "Lenguajes",
        "icon": "💻",
        "skills": ["Python", "JavaScript", "PHP", "R", "SQL"],
    },
    {
        "category": "Big Data",
        "icon": "🗄️",
        "skills": ["Hadoop (HDFS/MapReduce)", "Apache Pig", "Sqoop", "Flume", "Kafka", "Apache NiFi", "Dremio"],
    },
    {
        "category": "Bases de datos",
        "icon": "🧬",
        "skills": ["MongoDB", "Cassandra", "Redis", "Neo4j", "SQL Server / SSIS", "MySQL", "PostgreSQL", "SQLite"],
    },
    {
        "category": "Cloud (AWS)",
        "icon": "☁️",
        "skills": ["S3", "Glue", "Athena", "IAM"],
    },
    {
        "category": "ETL / BI",
        "icon": "📊",
        "skills": ["Pentaho (Kettle/PDI)", "Power BI", "Tableau", "Excel avanzado"],
    },
    {
        "category": "DevOps",
        "icon": "⚙️",
        "skills": ["Docker", "Docker Compose", "Dev Containers", "Git / GitHub", "GitHub Actions (CI/CD)", "Prometheus"],
    },
    {
        "category": "Machine Learning",
        "icon": "🧠",
        "skills": ["scikit-learn", "PyCaret"],
    },
    {
        "category": "Deep Learning / Visión artificial",
        "icon": "👁️",
        "skills": ["TensorFlow", "Keras", "YOLOv8", "OpenCV"],
    },
    {
        "category": "NLP",
        "icon": "💬",
        "skills": ["Tokenización", "TF-IDF", "Embeddings", "Whoosh", "Análisis de sentimiento"],
    },
    {
        "category": "IA generativa / Agentes",
        "icon": "🤖",
        "skills": ["OpenAI API", "Groq", "LangChain", "RAG (ChromaDB)", "CrewAI", "Ollama", "MCP / FastMCP"],
    },
    {
        "category": "Backend / APIs",
        "icon": "🔌",
        "skills": ["FastAPI", "Flask", "Spring Boot", "JWT", "SQLAlchemy", "JPA / Hibernate", "JUnit", "Gradio", "OpenAPI / Swagger"],
    },
    {
        "category": "SAP (en formación)",
        "icon": "🔷",
        "skills": ["SAP BTP", "SAP Business Application Studio", "CAP (Node.js)", "CDS", "OData V4", "Fiori Elements"],
    },
    {
        "category": "Desarrollo Web",
        "icon": "🌐",
        "skills": ["HTML5", "CSS3", "Jinja2", "Diseño responsive"],
    },
]

# Proyectos personales: iniciativas propias, desplegadas y accesibles en vivo
# Carrusel de imágenes (opcional) en cualquier proyecto personal o de formación:
# copia las capturas a static/img/projects/ y añade al proyecto, por ejemplo:
#   "images": [
#       {"src": "img/projects/reciclia-1.png", "caption": "Pantalla principal"},
#       "img/projects/reciclia-2.png",
#   ],
# Si no pones "images", la tarjeta se queda sin carrusel.
FEATURED_PROJECTS = [
    {
        "title": "Inazuma Fantasy",
        "icon": "⚽",
        "description": (
            "Aplicación web de fantasy football basada en personajes de Inazuma Eleven. "
            "Sistema de ligas y subastas diarias, motor propio de simulación de partidos "
            "a partir de estadísticas de jugadores, repeticiones animadas y calendario de competición."
        ),
        "stack": ["Python", "Web app", "Motor de simulación"],
        "url": "https://yellowalberto.pythonanywhere.com/",
        "cta": "Ver demo",
    },
    {
        "title": "WhatsInChat",
        "icon": "📈",
        "description": (
            "Analizador gratuito y sin registro de chats y grupos de WhatsApp: a partir del export "
            "genera un ranking de quién escribe más, las horas de mayor actividad, un mapa de palabras, "
            "la afinidad entre miembros (quién responde a quién), perfiles de estilo de cada persona "
            "y búsqueda de palabras clave personalizadas."
        ),
        "stack": ["Python", "Procesamiento de datos", "Render"],
        "images": [
            {"src": "img/projects/whatsinchat-1-inicio.webp", "caption": "Sube tu chat de WhatsApp (.zip o .txt) y obtén el análisis al instante"},
            {"src": "img/projects/whatsinchat-2-ranking.webp", "caption": "Ranking de los miembros más activos del grupo"},
            {"src": "img/projects/whatsinchat-3-heatmap.webp", "caption": "Actividad por día de la semana y hora"},
            {"src": "img/projects/whatsinchat-4-conceptos.webp", "caption": "Mapa de conceptos: las palabras más usadas"},
            {"src": "img/projects/whatsinchat-5-perfil.webp", "caption": "Perfil de cada miembro y su estilo en el grupo"},
        ],
        "url": "https://whatsinchat.onrender.com/",
        "cta": "Ver demo",
    },
]

# Proyectos SAP (actualmente en formación)
SAP_PROJECTS = [
    {
        "title": "Caso práctico: gestión de tienda con CAP y Fiori Elements",
        "icon": "🔷",
        "status": "En formación",
        "description": (
            "Aplicación de gestión de categorías y compras de una tienda, construida desde cero en "
            "SAP Business Application Studio sobre SAP BTP. Modelo de datos en CDS con relación "
            "1:N (Composition), servicio OData V4 con CAP y SQLite, interfaz SAP Fiori Elements "
            "con lista y ficha de detalle, y gestión de borradores (Draft) para crear, editar, "
            "guardar y cancelar cambios. Incluye pruebas funcionales y validaciones."
        ),
        "stack": ["SAP BTP", "CAP", "CDS", "OData V4", "Fiori Elements", "Node.js", "SQLite"],
        "docs": [{"label": "Memoria del proyecto (PDF)", "url": "/static/docs/sap-cap-tienda.pdf"}],
    },
]

# Proyectos de formación (Big Data e IA) sin demo pública, o con repos
OTHER_PROJECTS = [
    {
        "title": "ReciclA — Asistente Inteligente de Reciclaje",
        "icon": "♻️",
        "description": (
            "Ecosistema de IA para fomentar el reciclaje: detección de residuos con YOLOv8, "
            "agente conversacional con Groq, backend FastAPI con autenticación JWT, "
            "base de datos híbrida PostgreSQL/SQLite, frontend en Gradio, Docker Compose "
            "y despliegue continuo con GitHub Actions a Hugging Face Spaces."
        ),
        "stack": ["FastAPI", "YOLOv8", "Groq", "Docker", "CI/CD"],
        "url": "https://huggingface.co/spaces/YellowAlberto/ReciclA",
        "cta": "Ver Space",
    },
    {
        "title": "Agente de seguimiento de matrículas y contenedores",
        "icon": "🚚",
        "description": (
            "Agente de IA para automatizar el seguimiento de stock y pedidos a partir de "
            "OCR sobre matrículas/contenedores, orquestado con CrewAI y modelos locales "
            "servidos con Ollama, expuesto mediante herramientas MCP dentro de un Dev Container."
        ),
        "stack": ["CrewAI", "Ollama", "MCP", "OCR", "Docker"],
        "url": None,
        "cta": None,
    },
    {
        "title": "SmartParkingFlow — Pipeline de streaming IoT",
        "icon": "🔄",
        "description": (
            "Sistema de aparcamiento inteligente para una Smart City: los sensores de cada plaza envían "
            "su estado en streaming a Kafka, NiFi orquesta el flujo hacia colecciones de MongoDB "
            "(estado actual e histórico), Dremio sirve de capa de análisis y una app Flask muestra "
            "en un mapa la ocupación en tiempo real."
        ),
        "stack": ["Kafka", "NiFi", "MongoDB", "Dremio", "Flask"],
        "url": None,
        "cta": None,
        "docs": [{"label": "Memoria del proyecto (PDF)", "url": "/static/docs/smartparking.pdf"}],
    },
    {
        "title": "ETL en AWS con modelo en estrella",
        "icon": "🪣",
        "description": (
            "Proceso ETL completo en AWS: ingesta en S3, transformación y catalogación con Glue "
            "Crawlers, y consultas analíticas con Athena sobre un modelo dimensional en estrella."
        ),
        "stack": ["AWS S3", "Glue", "Athena"],
        "url": None,
        "cta": None,
        "docs": [{"label": "Memoria del proyecto (PDF)", "url": "/static/docs/etl-aws.pdf"}],
    },
    {
        "title": "Asistente RAG con LangChain",
        "icon": "📚",
        "description": (
            "Sistema de Recuperación Aumentada por Generación (RAG) sobre documentación real "
            "de recursos de apoyo: chunking, embeddings y búsqueda semántica con ChromaDB "
            "integrados en LangChain."
        ),
        "stack": ["LangChain", "ChromaDB", "RAG", "Embeddings"],
        "url": None,
        "cta": None,
    },
    {
        "title": "Clasificadores de visión artificial",
        "icon": "🔬",
        "description": (
            "Modelos de clasificación de imágenes con CNNs y transfer learning: detección de "
            "melanoma y clasificación de residuos para reciclaje combinando YOLO y redes "
            "convolucionales propias."
        ),
        "stack": ["TensorFlow/Keras", "YOLO", "CNN", "Transfer learning"],
        "url": None,
        "cta": None,
        "docs": [
            {"label": "Informe: clasificador de melanoma (PDF)", "url": "/static/docs/clasificador-melanoma.pdf"},
            {"label": "Informe: clasificador de residuos (PDF)", "url": "/static/docs/clasificador-basura.pdf"},
        ],
    },
    {
        "title": "Data Warehouse & Business Intelligence",
        "icon": "🏢",
        "description": (
            "Modelado y explotación de un Data Warehouse con Pentaho/SSIS, análisis predictivo "
            "y de clustering de clientes con PyCaret, y visualización de datos de criminalidad "
            "de Chicago con Power BI."
        ),
        "stack": ["Pentaho", "SSIS", "Power BI", "PyCaret"],
        "url": None,
        "cta": None,
        "docs": [{"label": "Proyecto Chicago Crimes (PDF)", "url": "/static/docs/dw-bi-chicago-crimes.pdf"}],
    },
    {
        "title": "Dashboard de monitorización con Prometheus",
        "icon": "📡",
        "description": (
            "Sistema de monitorización de infraestructura con Prometheus, con configuración de "
            "scraping y visualización de métricas en tiempo real."
        ),
        "stack": ["Prometheus", "Monitorización"],
        "url": None,
        "cta": None,
        "docs": [{"label": "Memoria del dashboard (PDF)", "url": "/static/docs/dashboard-prometheus.pdf"}],
    },
]


# Sección "Formación" (de más reciente a más antigua)
EDUCATION = [
    {
        "title": "SAP ABAP y SAP BTP",
        "center": "Experis",
        "period": "Oct. 2026 – Nov. 2026",
        "current": True,
        "description": (
            "Formación en desarrollo SAP con ABAP Cloud y SAP BTP, orientada a la "
            "preparación de certificaciones oficiales."
        ),
        "tags": ["ABAP Cloud", "SAP BTP", "CAP", "Fiori Elements"],
    },
    {
        "title": "Curso de Especialización en Inteligencia Artificial y Big Data",
        "center": "IES Fernando Aguilar Quignon",
        "period": "Sept. 2025 – May. 2026",
        "current": False,
        "description": (
            "Pipelines de datos en streaming, ETL en la nube, modelos de visión "
            "artificial, sistemas RAG y agentes inteligentes."
        ),
        "tags": ["Python", "Big Data", "IA / ML", "AWS"],
    },
    {
        "title": "Ciclo Formativo de Grado Superior en Desarrollo de Aplicaciones Web (DAW)",
        "center": "IES Ntra. Sra. de los Remedios",
        "period": "Sept. 2020 – Jun. 2022",
        "current": False,
        "description": (
            "Desarrollo de aplicaciones web completas, tanto en cliente como en servidor, "
            "con bases de datos y pruebas."
        ),
        "tags": ["JavaScript", "PHP", "Spring Boot", "JPA / Hibernate", "JUnit"],
    },
]
