def je_tah_mozny(figurka: dict, cilova_pozice: tuple, obsazene_pozice):
    typ, pozice = figurka.values()

    if not (0 <= cilova_pozice[0] < 8 and 0 <= cilova_pozice[1] < 8):
        return False
    if cilova_pozice in obsazene_pozice:
        return False

    if typ == "pěšec":
        if cilova_pozice[1] == pozice[1]:
            if cilova_pozice[0] == pozice[0] + 1:
                return True
            elif pozice[0] == 2 and cilova_pozice[0] == pozice[0] + 2:
                return True
        return False

    elif typ == "jezdec":
        dx, dy = abs(cilova_pozice[0] - pozice[0]), abs(cilova_pozice[1] - pozice[1])
        return (dx, dy) in [(2, 1), (1, 2)]

    elif typ == "věž":
        return pozice[0] == cilova_pozice[0] or pozice[1] == cilova_pozice[1]

    elif typ == "střelec":
        return abs(pozice[0] - cilova_pozice[0]) == abs(pozice[1] - cilova_pozice[1])

    elif typ == "dáma":
        return (
            pozice[0] == cilova_pozice[0]
            or pozice[1] == cilova_pozice[1]
            or abs(pozice[0] - cilova_pozice[0]) == abs(pozice[1] - cilova_pozice[1])
        )

    elif typ == "král":
        return (
            max(abs(pozice[0] - cilova_pozice[0]), abs(pozice[1] - cilova_pozice[1]))
            == 1
        )

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    obsazene_pozice = {(2, 2), (3, 3), (8, 3)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (6, 3), obsazene_pozice))  # True
