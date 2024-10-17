def cislo_text(cislo):
    cisla_0_20 = [
        "nula",
        "jedna",
        "dva",
        "tři",
        "čtyři",
        "pět",
        "šest",
        "sedm",
        "osm",
        "devět",
        "deset",
        "jedenáct",
        "dvanáct",
        "třináct",
        "čtrnáct",
        "patnáct",
        "šestnáct",
        "sedmnáct",
        "osmnáct",
        "devatenáct",
        "dvacet",
    ]
    desitky = [
        "",
        "",
        "dvacet",
        "třicet",
        "čtyřicet",
        "padesát",
        "šedesát",
        "sedmdesát",
        "osmdesát",
        "devadesát",
    ]

    # Ošetření vstupu
    try:
        cislo = int(cislo)
    except ValueError:
        return "Neplatné číslo"

    # Čísla do 20
    if cislo <= 20:
        return cisla_0_20[cislo]

    # Čísla 21-99
    if 20 < cislo < 100:
        desitka = cislo // 10  # určuje desítky
        jednotka = cislo % 10  # určuje jednotky
        if jednotka == 0:
            return desitky[desitka]
        else:
            return desitky[desitka] + " " + cisla_0_20[jednotka]

    # Číslo 100
    if cislo == 100:
        return "sto"

    return "Číslo mimo rozsah"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    print(cislo_text(cislo))
