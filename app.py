import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def gallery():
    # Path to your static image folder
    image_folder = os.path.join(app.static_folder, "images")

    # List all files in the folder
    image_files = []
    if os.path.exists(image_folder):
        image_files = [
            "images/" + f for f in os.listdir(image_folder)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))
        ]

    return render_template("gall.html", images=image_files)

if __name__ == "__main__":
    app.run(debug=True)