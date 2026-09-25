import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    def test_fibonacci_base_cases():
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_fibonacci_small_values():
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55

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


if __name__ == "__main__":
    app.run()
