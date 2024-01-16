from flask import Flask, request, send_file
import matplotlib.pyplot as plt
import matplotlib
import io

# GUIバックエンドを使用しないように設定
matplotlib.use("Agg")

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/latex_to_image", methods=["POST"])
def latex_to_image():
    data = request.json
    latex_formula = data.get("formula")

    # LaTeX数式を画像に変換
    buffer = io.BytesIO()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    text = ax.text(
        0.5,
        0.5,
        f"${latex_formula}$",
        fontsize=20,
        ha="center",
        va="center",
        transform=ax.transAxes,
    )
    ax.axis("off")

    # 余白を削除
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

    # Textオブジェクトを使用してトリミングをより正確に
    plt.savefig(
        buffer,
        format="png",
        bbox_inches=text.get_window_extent().transformed(
            fig.dpi_scale_trans.inverted()
        ),
        pad_inches=0,
        dpi=300,
    )
    buffer.seek(0)

    # リソースを解放
    plt.close(fig)

    return send_file(buffer, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5001)
