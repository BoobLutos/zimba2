from flask import Flask, render_template

app = Flask(__name__)

RECIPE = {
    "week": "August 24 - August 30",
    "name": "Chicken Biryani",
    "description": "A fragrant Indian layered rice dish with marinated chicken, basmati rice, and aromatic spices.",
    "ingredients": [
        "1 kg chicken (bone-in, cut into pieces)",
        "3 cups basmati rice (soaked 30 minutes)",
        "1 cup plain yogurt",
        "2 tbsp ginger-garlic paste",
        "2 large onions (thinly sliced)",
        "1/2 cup ghee or oil",
        "2 tomatoes (chopped)",
        "1/2 cup fresh mint leaves",
        "1/2 cup fresh coriander leaves",
        "2-3 green chilies (slit)",
        "1 tsp turmeric powder",
        "2 tsp red chili powder",
        "1 tsp garam masala",
        "1/2 tsp saffron strands (soaked in 2 tbsp warm milk)",
        "2 tbsp lemon juice",
        "2 tbsp kewra water or rose water (optional)",
        "Salt to taste",
    ],
    "instructions": [
        "Marinate chicken with yogurt, ginger-garlic paste, turmeric, chili powder, garam masala, lemon juice, and salt. Refrigerate 2+ hours.",
        "Fry sliced onions in ghee/oil until golden brown and crisp (birista). Remove half for garnish.",
        "In the same pan, cook marinated chicken on high heat 5 min, then cover and cook 15-20 min until 80% done.",
        "Parboil rice with whole spices (bay leaves, cardamom, cloves, cinnamon, cumin, salt) until 70% done. Drain.",
        "Layer: spread half the chicken gravy in a heavy pot, add half the rice, sprinkle mint, coriander, chilies, garam masala, saffron milk, kewra water, and ghee. Repeat layers.",
        "Seal pot tightly (dum). Cook on high heat 5 min, then lowest heat 25-30 min. Place a tawa underneath to prevent burning.",
        "Rest 10 minutes. Gently fluff and mix. Garnish with fried onions.",
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
