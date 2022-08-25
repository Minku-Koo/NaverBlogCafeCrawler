def listToTXT(L, filename):
    with open("output/{filename}", "w", encoding="utf8") as f:
        f.writelines(L)