import sympy

sympy.init_printing()

# TeX記法で数式を入力
wave_equation = r"""
\bm{\alpha}
"""

sympy.preview(
    wave_equation,
    viewer="file",
    filename="tex.png",
    euler=False,
    dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"],
)
