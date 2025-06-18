# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo==0.13.15",
# ]
# ///
import marimo

__generated_with = "0.10.10"
app = marimo.App()

with app.setup:
    import marimo as mo


@app.cell
def _():
    mo.md(r"""# Demo""")
    return


if __name__ == "__main__":
    app.run()
