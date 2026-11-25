# app.py
# Flask application: routes, reading the form and checking the inputs.
from flask import Flask, render_template, request
import reactions

app = Flask(__name__)


def read_number(text, name, minimum):
    """Turn text into a number. Returns (number, error_message)."""
    text = text.strip()
    if text == "":
        return "", None            # optional field left empty
    try:
        number = float(text)
    except ValueError:
        return "", "Please enter a valid number for " + name + "."
    if number < minimum:
        return "", name.capitalize() + " is out of the possible range."
    return number, None


@app.route("/", methods=["GET", "POST"])
def home():
    form = {"reactants": "", "catalyst": "", "solvent": "",
            "temperature": "", "pressure": "", "extra": ""}
    page = {"error": None, "warning": None, "result": None, "chips": []}

    if request.method == "POST":
        for field in form:
            form[field] = request.form.get(field, "").strip()

        # 1. Check the reactants
        names = reactions.split_reactants(form["reactants"])
        keys, unknown = [], []
        for name in names:
            key = reactions.find_molecule(name)
            if key is None:
                unknown.append(name.strip())
            elif key not in keys:
                keys.append(key)
        page["chips"] = [reactions.MOLECULES[k] for k in keys]

        # 2. Check temperature and pressure
        temperature, temp_error = read_number(form["temperature"], "temperature", -273.15)
        pressure, pressure_error = read_number(form["pressure"], "pressure", 0.0001)

        # 3. Report the first problem found, otherwise predict
        if not names:
            page["error"] = "Please enter at least one reactant."
        elif unknown:
            page["error"] = "One or more reactants could not be recognised: " + ", ".join(unknown) + ". Separate reactants with + or a comma."
        elif temp_error or pressure_error:
            page["error"] = temp_error or pressure_error
        else:
            conditions = {"catalyst": "", "solvent": form["solvent"],
                          "temperature": temperature, "pressure": pressure}
            outcome = reactions.predict(keys, form["catalyst"], conditions)
            page["error"] = outcome.get("error")
            page["warning"] = outcome.get("warning")
            page["result"] = outcome.get("result")

    return render_template("index.html", form=form, page=page)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
