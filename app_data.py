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
        "Construyo pipelines de datos, modelos de IA/ML, agentes inteligentes y aplicaciones "
        "web de extremo a extremo: desde la ingesta de datos hasta el despliegue en producción."
    ),
    "email": "albertopiedra155@gmail.com",
    "github": "https://github.com/YellowAlberto",
    "location": "España",
}

# Categorías de tecnologías para la sección "Stack"
# "icon" es un emoji: ligero, sin dependencias externas, y encaja con el resto del diseño.
STACK = [
    {
        "category": "Lenguajes",
        "icon": "💻",
        "skills": ["Python", "R", "SQL"],
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
        "skills": ["S3", "Glue", "Athena", "IAM", "CloudFormation"],
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
        "skills": ["scikit-learn", "PyCaret", "K-means / DBSCAN", "Árboles de decisión", "SVM", "Regresión", "Ensembles"],
    },
    {
        "category": "Deep Learning / Visión artificial",
        "icon": "👁️",
        "skills": ["TensorFlow", "Keras", "CNNs", "YOLOv8", "OpenCV", "GANs", "Transfer learning"],
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
        "skills": ["FastAPI", "Flask", "JWT", "SQLAlchemy", "Gradio", "OpenAPI / Swagger"],
    },
    {
        "category": "Desarrollo Web",
        "icon": "🌐",
        "skills": ["HTML5", "CSS3", "JavaScript", "Jinja2", "Diseño responsive", "Vercel"],
    },
]

# Proyectos personales: iniciativas propias, desplegadas y accesibles en vivo
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
        "title": "WhatStats",
        "icon": "📈",
        "description": (
            "Analizador de estadísticas de conversaciones de WhatsApp: procesa el export del chat "
            "y genera métricas de actividad (mensajes por persona, horas de mayor actividad, "
            "emojis más usados, etc.)."
        ),
        "stack": ["Python", "Procesamiento de datos", "Render"],
        "url": "https://whatstats.onrender.com/",
        "cta": "Ver demo",
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
        "title": "Pipeline de streaming en tiempo real",
        "icon": "🔄",
        "description": (
            "Arquitectura de ingesta y consulta de datos en streaming: Kafka como cola de mensajes, "
            "NiFi para el flujo de datos, MongoDB como almacenamiento y Dremio como capa de consulta, "
            "con una app Flask como productor de datos."
        ),
        "stack": ["Kafka", "NiFi", "MongoDB", "Dremio", "Flask"],
        "url": None,
        "cta": None,
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
