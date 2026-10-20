import os
import sys

# Allow importing the app package from the project root when running on Vercel
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app_data import STACK, FEATURED_PROJECTS, OTHER_PROJECTS, SAP_PROJECTS, PROFILE
from flask import Flask, render_template, send_from_directory

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates"),
    static_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static"),
)


@app.route("/")
def home():
    return render_template(
        "index.html",
        stack=STACK,
        featured_projects=FEATURED_PROJECTS,
        other_projects=OTHER_PROJECTS,
        sap_projects=SAP_PROJECTS,
        profile=PROFILE,
    )


@app.route("/favicon.ico")
def favicon():
    # Los navegadores piden /favicon.ico por defecto; lo servimos desde static/
    return send_from_directory(app.static_folder, "favicon.ico", mimetype="image/vnd.microsoft.icon")


# Vercel's Python runtime looks for a WSGI-compatible `app` object.
if __name__ == "__main__":
    app.run(debug=True)
