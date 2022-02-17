def find_happiest(happiness_file):
    conts = {}
    for line in open(happiness_file, "r"):
        line = line.strip()
        sId, country, rank, cont = line.split(",")
        if cont not in conts:
            conts[cont] = []

        conts[cont].append((float(rank), country))

    result = {}
    for cont, countries in conts.items():
        countries.sort(reverse=True)
        _, max_c = countries[0]
        result[cont] = max_c

    return result
