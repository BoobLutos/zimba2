from flask import Flask, render_template

app = Flask(__name__)

RECIPE = {
    "week": "June 15 - June 21",
    "name": "Spaghetti Carbonara",
    "description": "A classic Roman pasta dish with eggs, cheese, pancetta, and black pepper.",
    "ingredients": [
        "400g spaghetti",
        "150g pancetta, diced",
        "4 large eggs",
        "100g Pecorino Romano, grated",
        "2 cloves garlic, minced",
        "Freshly ground black pepper",
        "Salt, to taste",
    ],
    "instructions": [
        "Cook spaghetti in salted boiling water until al dente.",
        "While the pasta cooks, fry the pancetta with garlic until crisp.",
        "Whisk the eggs and cheese together in a bowl.",
        "Drain the pasta, reserving a little of the cooking water.",
        "Off the heat, toss the hot pasta with the pancetta, then quickly stir in the egg mixture, adding pasta water to loosen.",
        "Season generously with black pepper and serve immediately.",
    ],
}


@app.route("/")
def index():
    return render_template("index.html", recipe=RECIPE)


@app.route("/healthz")
def healthz():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
