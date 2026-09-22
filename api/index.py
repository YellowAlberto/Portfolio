import os
import sys

# Allow importing the app package from the project root when running on Vercel
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app_data import STACK, FEATURED_PROJECTS, OTHER_PROJECTS, PROFILE
from flask import Flask, render_template

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
        profile=PROFILE,
    )


# Vercel's Python runtime looks for a WSGI-compatible `app` object.
if __name__ == "__main__":
    app.run(debug=True)
