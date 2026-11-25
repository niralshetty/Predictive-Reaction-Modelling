# reactions.py
# Holds the small "database" of supported reactions and the simple
# rule-based functions that match user input against it.
# No machine learning: just dictionaries and if-statements.

# ---------- 1. MOLECULES ----------
# Each molecule has a name, a formula (with subscripts) and a text drawing.
MOLECULES = {
    "ethene": {"name": "Ethene", "formula": "C₂H₄", "short": "H₂C=CH₂",
        "drawing": "H       H\n \\     /\n  C = C\n /     \\\nH       H"},
    "hydrogen": {"name": "Hydrogen", "formula": "H₂", "short": "H–H",
        "drawing": "H – H"},
    "ethane": {"name": "Ethane", "formula": "C₂H₆", "short": "CH₃–CH₃",
        "drawing": "    H   H\n    |   |\nH – C – C – H\n    |   |\n    H   H"},
    "methane": {"name": "Methane", "formula": "CH₄", "short": "CH₄",
        "drawing": "    H\n    |\nH – C – H\n    |\n    H"},
    "oxygen": {"name": "Oxygen", "formula": "O₂", "short": "O=O",
        "drawing": "O = O"},
    "carbon dioxide": {"name": "Carbon dioxide", "formula": "CO₂", "short": "O=C=O",
        "drawing": "O = C = O"},
    "water": {"name": "Water", "formula": "H₂O", "short": "H–O–H",
        "drawing": "  O\n / \\\nH   H"},
    "ethanol": {"name": "Ethanol", "formula": "C₂H₅OH", "short": "CH₃–CH₂–OH",
        "drawing": "    H   H\n    |   |\nH – C – C – O – H\n    |   |\n    H   H"},
    "nitrogen": {"name": "Nitrogen", "formula": "N₂", "short": "N≡N",
        "drawing": "N ≡ N"},
    "ammonia": {"name": "Ammonia", "formula": "NH₃", "short": "NH₃",
        "drawing": "    N\n  / | \\\n H  H  H"},
}

# Names a user may type -> molecule key (spaces are removed before lookup)
ALIASES = {
    "ethene": "ethene", "ethylene": "ethene", "c2h4": "ethene", "h2c=ch2": "ethene",
    "hydrogen": "hydrogen", "h2": "hydrogen",
    "ethane": "ethane", "c2h6": "ethane",
    "methane": "methane", "ch4": "methane",
    "oxygen": "oxygen", "o2": "oxygen",
    "carbondioxide": "carbon dioxide", "co2": "carbon dioxide",
    "water": "water", "h2o": "water", "steam": "water",
    "ethanol": "ethanol", "c2h5oh": "ethanol", "ethylalcohol": "ethanol",
    "nitrogen": "nitrogen", "n2": "nitrogen",
    "ammonia": "ammonia", "nh3": "ammonia",
}

CATALYSTS = {
    "ni": "Nickel (Ni)", "nickel": "Nickel (Ni)",
    "pt": "Platinum (Pt)", "platinum": "Platinum (Pt)",
    "pd": "Palladium (Pd)", "palladium": "Palladium (Pd)",
    "fe": "Iron (Fe)", "iron": "Iron (Fe)",
    "h3po4": "Phosphoric acid (H₃PO₄)", "phosphoricacid": "Phosphoric acid (H₃PO₄)",
}

# ---------- 2. SUPPORTED REACTIONS ----------
# reactants / products are lists of (coefficient, molecule key)
REACTIONS = [
    {
        "name": "Hydrogenation of Ethene", "type": "Addition Reaction",
        "reactants": [(1, "ethene"), (1, "hydrogen")], "products": [(1, "ethane")],
        "catalysts": ["Nickel (Ni)", "Platinum (Pt)", "Palladium (Pd)"],
        "typical": "Finely divided Ni, Pt or Pd metal; Ni commonly used with moderate heating (about 150 °C).",
        "solvent_note": "No solvent is needed for the gas-phase demonstration.",
        "explanation": ["Ethene reacts with hydrogen in the presence of a metal catalyst to form ethane.",
                        "Hydrogen atoms are added across the carbon–carbon double bond.",
                        "The C=C double bond becomes a C–C single bond."],
        "bonds": "Broken: C=C (one of the two bonds, the π bond) and H–H. Formed: two new C–H bonds.",
        "pathway": "Simplified picture: both gases stick to the metal surface, the H–H bond breaks, and the H atoms add to the two carbons one at a time.",
        "selectivity": "Only one product is possible here, so selectivity is not a concern.",
        "behaviour": "Alkene is fully saturated to an alkane.",
        "ref": "Hydrogenation",
    },
    {
        "name": "Hydration of Ethene", "type": "Addition Reaction",
        "reactants": [(1, "ethene"), (1, "water")], "products": [(1, "ethanol")],
        "catalysts": ["Phosphoric acid (H₃PO₄)"],
        "typical": "Phosphoric acid catalyst, steam, about 300 °C and about 60–70 atm (industrial process).",
        "solvent_note": "Water is itself a reactant (used as steam).",
        "explanation": ["Ethene adds the elements of water in the presence of an acid catalyst to form ethanol.",
                        "The C=C double bond becomes a C–C single bond.",
                        "One carbon gains an –H and the other gains an –OH."],
        "bonds": "Broken: C=C (π bond) and one H–O bond of water. Formed: one C–H and one C–O bond.",
        "pathway": "Simplified picture: the acid adds H⁺ to the double bond, water then attaches to the carbon, and H⁺ is released again.",
        "selectivity": "Ethene is symmetrical, so only ethanol is expected from the addition itself.",
        "behaviour": "The reaction is reversible, so conditions control how much ethanol is present at equilibrium.",
        "ref": "Hydration",
    },
    {
        "name": "Combustion of Methane", "type": "Combustion (Oxidation) Reaction",
        "reactants": [(1, "methane"), (2, "oxygen")], "products": [(1, "carbon dioxide"), (2, "water")],
        "catalysts": [],
        "typical": "No catalyst needed. An ignition source or heat starts the reaction; excess oxygen gives complete combustion.",
        "solvent_note": "Gas-phase reaction; no solvent is used.",
        "explanation": ["Methane burns in excess oxygen to give carbon dioxide and water.",
                        "The reaction releases heat (it is exothermic).",
                        "Carbon is oxidised from −4 to +4."],
        "bonds": "Broken: C–H bonds in methane and the O=O bond. Formed: C=O bonds in CO₂ and O–H bonds in water.",
        "pathway": "Only the overall change is shown. Real combustion happens through many fast radical steps that this model does not cover.",
        "selectivity": "With limited oxygen, carbon monoxide and soot can form instead; this model covers complete combustion only.",
        "behaviour": "Strongly exothermic once started.",
        "ref": "Combustion",
    },
    {
        "name": "Combustion of Ethanol", "type": "Combustion (Oxidation) Reaction",
        "reactants": [(1, "ethanol"), (3, "oxygen")], "products": [(2, "carbon dioxide"), (3, "water")],
        "catalysts": [],
        "typical": "No catalyst needed. An ignition source or heat starts the reaction; excess oxygen gives complete combustion.",
        "solvent_note": "Burns as a vapour; no solvent is used.",
        "explanation": ["Ethanol burns in excess oxygen to give carbon dioxide and water.",
                        "The reaction releases heat (it is exothermic).",
                        "Both carbon atoms are oxidised."],
        "bonds": "Broken: C–H, C–C, C–O and O–H bonds in ethanol, and O=O. Formed: C=O bonds in CO₂ and O–H bonds in water.",
        "pathway": "Only the overall change is shown. Real combustion happens through many fast radical steps that this model does not cover.",
        "selectivity": "With limited oxygen, carbon monoxide and soot can form; this model covers complete combustion only.",
        "behaviour": "Strongly exothermic once started.",
        "ref": "Combustion",
    },
    {
        "name": "Haber Process (Ammonia Synthesis)", "type": "Combination (Synthesis) Reaction",
        "reactants": [(1, "nitrogen"), (3, "hydrogen")], "products": [(2, "ammonia")],
        "catalysts": ["Iron (Fe)"],
        "typical": "Iron catalyst, about 400–450 °C and about 150–250 atm (industrial process).",
        "solvent_note": "Gas-phase reaction; no solvent is used.",
        "explanation": ["Nitrogen and hydrogen combine over an iron catalyst to form ammonia.",
                        "The strong N≡N triple bond must be broken, which is why a catalyst and heat are needed.",
                        "The reaction is reversible."],
        "bonds": "Broken: N≡N and H–H. Formed: N–H bonds in ammonia.",
        "pathway": "Simplified picture: N₂ and H₂ split into atoms on the iron surface, then N and H atoms combine step by step into NH₃.",
        "selectivity": "Ammonia is the only product expected.",
        "behaviour": "Exothermic and reversible, so temperature and pressure trade off rate against equilibrium amount.",
        "ref": "Combination",
    },
]

# ---------- 3. SMALL HELPER FUNCTIONS ----------
SUBSCRIPTS = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")

def clean(text):
    """Lower-case, remove spaces and turn subscripts into plain digits."""
    return text.lower().translate(SUBSCRIPTS).replace(" ", "").strip()

def split_reactants(text):
    """Split 'ethene + hydrogen' or 'ethene, hydrogen' into a list."""
    text = text.replace("+", ",").replace(";", ",").replace("\n", ",")
    text = text.replace(" and ", ",")
    return [part for part in text.split(",") if part.strip()]

def find_molecule(name):
    """Return the molecule key for a typed name, or None if unknown."""
    return ALIASES.get(clean(name))

def find_catalyst(name):
    """Return the catalyst display name, or None if unknown/empty."""
    return CATALYSTS.get(clean(name))

def show_side(side):
    """Build text like '2 O₂ + CH₄' from a list of (coefficient, key)."""
    parts = []
    for number, key in side:
        prefix = "" if number == 1 else str(number) + " "
        parts.append(prefix + MOLECULES[key]["formula"])
    return " + ".join(parts)

def equation(reaction):
    return show_side(reaction["reactants"]) + " → " + show_side(reaction["products"])

def molecule_cards(side):
    """Turn a side of the reaction into a list of dicts for the template."""
    cards = []
    for number, key in side:
        card = dict(MOLECULES[key])
        card["number"] = number
        cards.append(card)
    return cards

def find_reaction(keys):
    """Find the supported reaction whose reactants match (order ignored)."""
    for reaction in REACTIONS:
        needed = set(key for number, key in reaction["reactants"])
        if needed == set(keys):
            return reaction
    return None

def or_not_specified(value, unit=""):
    return (str(value) + " " + unit).strip() if value not in ("", None) else "Not specified"

def build_factors(reaction, conditions):
    """Create the 'Factors Affecting the Reaction' list."""
    return [
        {"title": "Temperature", "yours": or_not_specified(conditions["temperature"], "°C"),
         "general": "Higher temperature usually speeds up a reaction, but it can also favour side reactions or shift the balance of reversible reactions. It does not always improve yield.",
         "specific": reaction["typical"]},
        {"title": "Pressure", "yours": or_not_specified(conditions["pressure"], "atm"),
         "general": "Pressure mainly matters for reactions involving gases. Higher pressure brings gas molecules closer together and can shift gas equilibria.",
         "specific": reaction["typical"]},
        {"title": "Catalyst", "yours": conditions["catalyst"] or "Not specified",
         "general": "A catalyst lowers the activation energy so the reaction runs faster. It is not used up and does not change the overall equation.",
         "specific": "Supported catalyst(s): " + (", ".join(reaction["catalysts"]) if reaction["catalysts"] else "none needed.")},
        {"title": "Solvent", "yours": conditions["solvent"] or "Not specified",
         "general": "A solvent can dissolve reactants, help them mix, and control heat. The choice may affect rate and selectivity.",
         "specific": reaction["solvent_note"]},
        {"title": "Reactant concentration", "yours": "Not specified",
         "general": "Higher concentration (or partial pressure) means more frequent collisions, which usually increases the reaction rate.",
         "specific": "This model does not calculate rate from concentration."},
    ]

def predict(keys, catalyst_text, conditions):
    """
    Main prediction function.
    Returns a dictionary with either an 'error', a 'warning', or a 'result'.
    """
    reaction = find_reaction(keys)
    if reaction is None:
        return {"error": "This reaction is not currently supported by the educational prediction model."}

    # Some reactions need a catalyst. Without the right one we do not predict a product.
    if reaction["catalysts"]:
        catalyst = find_catalyst(catalyst_text)
        if catalyst not in reaction["catalysts"]:
            needed = " or ".join(reaction["catalysts"])
            return {"warning": "These reactants match a supported reaction, but it needs a catalyst: "
                    + needed + ". Add one to see the prediction. Typical conditions: " + reaction["typical"]}
        conditions["catalyst"] = catalyst
    elif catalyst_text.strip():
        conditions["catalyst"] = catalyst_text.strip() + " (not required for this reaction)"

    result = {
        "name": reaction["name"], "type": reaction["type"],
        "equation": equation(reaction),
        "reactants": molecule_cards(reaction["reactants"]),
        "products": molecule_cards(reaction["products"]),
        "explanation": reaction["explanation"],
        "pathway": reaction["pathway"],
        "factors": build_factors(reaction, conditions),
        "insights": [
            ("Reactants", show_side(reaction["reactants"])),
            ("Products", show_side(reaction["products"])),
            ("Catalyst", conditions["catalyst"] or "Not specified"),
            ("Solvent", conditions["solvent"] or "Not specified"),
            ("Temperature", or_not_specified(conditions["temperature"], "°C")),
            ("Pressure", or_not_specified(conditions["pressure"], "atm")),
            ("Bond changes", reaction["bonds"]),
            ("Selectivity", reaction["selectivity"]),
            ("Expected behaviour", reaction["behaviour"]),
            ("Reaction rate", "Not estimated by this educational model."),
            ("Yield", "Not estimated by this educational model."),
        ],
    }
    return {"result": result}
