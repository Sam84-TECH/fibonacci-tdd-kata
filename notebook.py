import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    def test_fibonacci_base_cases():
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_fibonacci_small_values():
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55

    return


@app.cell
def _(mo):
    mo.md("""
    this fonction calcultate the n number of fibonacci
    """)
    return


@app.function
def fibonacci(n):
    a = 0
    b = 1
    for i in range (n):
        last_a = a
        a = b
        b= last_a+b
        
    return (a)


@app.cell
def _(mo):
    n_input = mo.ui.number(start=0, stop=1000, value=10, label="n")
    n_input
    return (n_input,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _(n_input):
    fibonacci(n_input.value)
    return


@app.function
def test_fibonacci_large_n():
    assert fibonacci(10000000) >= 0


@app.function
def fibonacci_fast(n):
    def fib_pair(k):
        if k == 0:
            return (0, 1)
        a, b = fib_pair(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
    return fib_pair(n)[0]


if __name__ == "__main__":
    app.run()
