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
    for _ in range(n):
        last_a = a
        a = b
        b = last_a + b

    return a


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


@app.cell
def _():
    "def test_fibonacci_large_n():"
    "assert fibonacci(10000000) >= 0"
    return


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


@app.function
def test_fibonacci_large_n():
    assert fibonacci_fast(10_000_000) >= 0


@app.function
def test_fibonacci_mod_small_n():
    m = 1_000_000_000
    assert fibonacci_mod(10, m) == 55
    assert fibonacci_mod(20, m) == 6765


@app.function
def test_fibonacci_mod_huge_n():
    m = 1_000_000_000
    result = fibonacci_mod(10**18, m)
    assert 0 <= result < m


@app.function
def fibonacci_mod(n, m):
    def fib_pair_mod(k):
        if k == 0:
            return (0 % m, 1 % m)
        a, b = fib_pair_mod(k // 2)
        c = (a * ((2 * b - a) % m)) % m
        d = (a * a + b * b) % m
        if k % 2 == 0:
            return (c, d)
        else:
            return (d, (c + d) % m)

    return fib_pair_mod(n)[0]


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    if (Test-Path src\fizzbuzz_tdd_kata) {Rename-Item src\fizzbuzz_tdd_kata fizzbuzz_kata} elseif (-not (Test-Path src\fizzbuzz_kata)) {mkdir src\fizzbuzz_kata}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    @'
    "\"\"FizzBuzz kata package - see core.py for the implementation."\"\"

    from fizzbuzz_kata.core import fizzbuzz

    __all__ = ["fizzbuzz"]
    __version__ = "0.1.0"
    '@ | Set-Content src\fizzbuzz_kata\__init__.py
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    @'
    def fizzbuzz(n: int)-> str:
        if not isinstance(n,int) or n<=0:
            raise ValueError("fizzbuzz excepts a striclty positive integer")
        result = "\"
        if n % 3 == 0:
            return +="Fizz"
        if n % 5 == 0:
            return +="Buzz"
        return result or str(n)
        '@ | Set-Content src\fizzbuzz_kata\core.py
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    mkdir tests
    @'
    import pytest

    from fizzbuzz_kata.core import fizzbuzz

    @pytest.mark.parametrize(
        ("n", "excepted")
        [
        (1,"1")
        (2,"2")
        (3,"Fizz")
        (5,"Buzz")
        (6,"Fizz")
        (10,"Buzz")
        (15,"FizzBuzz")
        (30,"FizzBuzz")
        (100,"Buzz")
        ]
    )
    def test_cases(n, excepted):
        assert fizzbuzz(n) == excepted

    @pytest.mark.parametrize("invalid"[0, -3, -5, "3"])
    def test_fizzbuz_rejects_invalid_input(invalid):
        with pytest.raises(ValueError):
            fizzbuzz(invalid)
    '@ | set-Content tests\test_core.py
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    @'
    [tool.pytest.ini_options]
    pythonpath = ["src"]
    testpaths = ["tests"]
    '@ | Add-Content pyproject.html uv run pytest-v
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    @'
    [project]
    name = "fizzbuzz_kata"
    version = "0.1.0"
    description = "A TDD Kata"
    """)
    return


if __name__ == "__main__":
    app.run()
