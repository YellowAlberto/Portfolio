# Portfolio — Alberto Piedra Venegas

Portfolio personal construido con **Python + Flask**, pensado para desplegarse en **Vercel**
usando su runtime de Python (funciones serverless).

## Estructura

```
portfolio/
├── api/
│   └── index.py        # Punto de entrada Flask (función serverless de Vercel)
├── templates/
│   └── index.html       # Plantilla Jinja de la página
├── static/
│   └── css/style.css    # Estilos
├── app_data.py           # Contenido: perfil, stack y proyectos (edítalo aquí)
├── requirements.txt
├── vercel.json           # Configuración de build/rutas para Vercel
└── .gitignore
```

## Editar el contenido

Todo el texto de la web (nombre, tagline, stack de tecnologías y proyectos) vive en
`app_data.py`. No hace falta tocar el HTML para añadir o cambiar un proyecto: basta con
editar las listas `FEATURED_PROJECTS` y `OTHER_PROJECTS` de ese fichero.

## Probarlo en local

```bash
python -m venv .venv
source .venv/bin/activate   # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python api/index.py
```

Abre http://127.0.0.1:5000 en el navegador.

## Desplegar en Vercel

### Opción A — Desde GitHub (recomendado)

1. Crea un repositorio en GitHub (por ejemplo `portfolio`) y sube esta carpeta:
   ```bash
   git init
   git add .
   git commit -m "Portfolio inicial"
   git branch -M main
   git remote add origin https://github.com/YellowAlberto/portfolio.git
   git push -u origin main
   ```
2. Entra en [vercel.com](https://vercel.com), inicia sesión con tu cuenta de GitHub.
3. Pulsa **Add New → Project**, selecciona el repositorio `portfolio`.
4. Vercel detectará automáticamente `vercel.json` y el runtime de Python — no hace falta
   tocar ninguna opción de build. Pulsa **Deploy**.
5. En cada `git push` a `main`, Vercel volverá a desplegar automáticamente.

### Opción B — Con la CLI de Vercel

```bash
npm i -g vercel
cd portfolio
vercel        # despliegue de prueba
vercel --prod # despliegue a producción
```

## Notas

- El dominio por defecto será algo como `portfolio-tuusuario.vercel.app`; puedes
  añadir un dominio propio desde el panel de Vercel (Settings → Domains).
- Si en el futuro quieres añadir más páginas, crea nuevas rutas en `api/index.py`
  (`@app.route("/otra-ruta")`) y su plantilla correspondiente en `templates/`.
