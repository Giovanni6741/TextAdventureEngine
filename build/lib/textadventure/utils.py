def box(text):
    """
    Incornicia un testo in un box ASCII.
    """
    lines = text.split("\n")
    width = max(len(l) for l in lines)
    top = "+" + "-" * width + "+"
    middle = "\n".join("|" + l.ljust(width) + "|" for l in lines)
    bottom = "+" + "-" * width + "+"
    return f"{top}\n{middle}\n{bottom}"
