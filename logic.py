def limConst(value):
    try:
        constant = float(value)
        return constant
    except ValueError:
        return "Invalid input"