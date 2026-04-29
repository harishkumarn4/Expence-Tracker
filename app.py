from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_data():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open("expenses.json", "w") as f:
        json.dump(data, f)

@app.route("/", methods=["GET", "POST"])
def index():
    expenses = load_data()

    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        date = request.form["date"]

        expenses.append({
            "amount": amount,
            "category": category,
            "date": date
        })

        save_data(expenses)
        return redirect("/")

    total = sum(exp["amount"] for exp in expenses)

    monthly_data = {}

    for exp in expenses:
        month = exp["date"][:7]  # extract YYYY-MM

        if month in monthly_data:
            monthly_data[month] += exp["amount"]
        else:
            monthly_data[month] = exp["amount"]


    category_data = {}

    for exp in expenses:
        category = exp["category"]

        if category in category_data:
            category_data[category] += exp["amount"]
        else:
            category_data[category] = exp["amount"]

    return render_template("index.html",
                       expenses=expenses,
                       total=total,
                       monthly_data=monthly_data,
                       category_data=category_data)

if __name__ == "__main__":
    app.run(debug=True)