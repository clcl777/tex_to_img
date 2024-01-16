import subprocess
from flask import Flask, request, send_file

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/latex_to_image", methods=["POST"])
def latex_to_image():
    data = request.json
    latex_formula = data.get("formula")

    latex_source = f"""
    \\documentclass[12pt]{{article}}
    \\usepackage{{bm}}
    \\usepackage{{amsmath}}
    \\pagestyle{{empty}}
    \\begin{{document}}
    \\[ {latex_formula} \\]
    \\end{{document}}
    """

    with open("formula.tex", "w") as file:
        file.write(latex_source)

    # LaTeXファイルをPDFに変換
    subprocess.run(["pdflatex", "formula.tex"])

    # PDFをPNG画像に変換
    subprocess.run(
        [
            "convert",
            "-density",
            "300",
            "formula.pdf",
            "-trim",
            "+repage",
            "-background",
            "transparent",
            "formula.png",
        ]
    )
    return send_file("formula.png", mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5001)
