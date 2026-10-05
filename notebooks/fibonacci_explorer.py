# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "matplotlib",
#     "fibonacci-kata-sam84",
# ]
# ///

import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_kata import fibonacci


@app.cell
def _():
    mo.md(
        r"""
        # Fibonacci Explorer

        Choisis le nombre de termes et observe la suite, sous forme de liste
        et de graphique. Ce notebook utilise le package `fibonacci_kata` :
        il ne redéfinit pas la fonction.
        """
    )
    return


@app.cell
def _():
    n_terms = mo.ui.slider(2, 60, value=15, label="Nombre de termes")
    log_scale = mo.ui.checkbox(label="Échelle logarithmique")
    mo.hstack([n_terms, log_scale])
    return log_scale, n_terms


@app.cell
def _(n_terms):
    values = [fibonacci(i) for i in range(1, n_terms.value + 1)]
    values
    return (values,)


@app.cell
def _(log_scale, n_terms, values):
    fig, ax = plt.subplots()
    ax.plot(range(1, n_terms.value + 1), values, marker="o")
    if log_scale.value:
        ax.set_yscale("log")
    ax.set_xlabel("n")
    ax.set_ylabel("F(n)")
    ax.set_title("Suite de Fibonacci")
    fig
    return


if __name__ == "__main__":
    app.run()
