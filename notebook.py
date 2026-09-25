import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.function
def fibonacci(n):
    pass


@app.cell
def _():
    def test_fibonacci_base_cases():
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_fibonacci_small_values():
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55

    return


if __name__ == "__main__":
    app.run()
