def listToTXT(L, filename):
    with open(f"output/{filename}", "w", encoding="utf8") as f:
        f.write("\n".join(L))