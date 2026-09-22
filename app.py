from flask import Flask, render_template

app = Flask(__name__)

RECIPE = {
    "week": "August 31 - September 6",
    "name": "Pad Thai Goong (Thai Stir-Fried Noodles with Shrimp)",
    "description": "Classic Thai street food - rice noodles stir-fried with shrimp, eggs, tofu, bean sprouts, and a perfect balance of sweet, sour, and savory tamarind sauce.",
    "ingredients": [
        "200g dried rice noodles (sen lek, medium width)",
        "150g fresh shrimp, peeled and deveined",
        "2 large eggs",
        "100g firm tofu, cut into small cubes",
        "1 cup bean sprouts",
        "2 tbsp garlic chives, cut into 1-inch pieces",
        "2 tbsp roasted peanuts, crushed",
        "2 tbsp vegetable oil",
        "2 cloves garlic, minced",
        "1 shallot, thinly sliced",
        "Lime wedges for serving",
        "For the Pad Thai sauce:",
        "3 tbsp tamarind paste",
        "2 tbsp fish sauce",
        "1 tbsp palm sugar (or brown sugar)",
        "1 tsp chili powder (adjust to taste)",
    ],
    "instructions": [
        "Soak rice noodles in room temperature water for 45-60 minutes until pliable but still firm. Drain.",
        "Mix tamarind paste, fish sauce, palm sugar, and chili powder until sugar dissolves. This is your Pad Thai sauce.",
        "Heat 1 tbsp oil in a wok over high heat. Add shrimp and cook 1-2 minutes until pink. Remove and set aside.",
        "Add remaining oil, then garlic and shallot. Stir-fry 30 seconds until fragrant.",
        "Add tofu and stir-fry 1 minute until golden on edges.",
        "Push tofu to side, crack eggs into wok. Scramble lightly, then mix with tofu.",
        "Add drained noodles and Pad Thai sauce. Toss continuously for 2-3 minutes until noodles absorb sauce and are cooked through.",
        "Add bean sprouts, garlic chives, and cooked shrimp. Toss for 30 seconds.",
        "Serve immediately topped with crushed peanuts and lime wedges on the side.",
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
