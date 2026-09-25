import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.function
def fibonacci(n: int) -> int:
    raise NotImplementedError


@app.function
def fibonacci(n):
    pass


if __name__ == "__main__":
    app.run()
