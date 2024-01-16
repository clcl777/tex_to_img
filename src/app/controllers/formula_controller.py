from app.database import db
from app.models import Formula
from flask import Flask, request, send_file
import matplotlib.pyplot as plt
import matplotlib
import io

matplotlib.use("Agg")


def show(atcoder_id):
    data = request.json
    latex_formula = data.get("formula")
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
    plt.close(fig)
    return send_file(buffer, mimetype="image/png")
