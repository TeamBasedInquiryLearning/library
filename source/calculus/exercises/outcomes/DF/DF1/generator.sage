class Generator(BaseGenerator):
    def data(self):
        base = randrange(-3, 3)
        baseval = (randrange(0, 4) + randrange(1, 5) / 10)*choice([-1, 1])
        increment = base + (choice([1,2,4,5]) / 10)*choice([-1, 1])
        incrementval = baseval + randrange(1,10)*choice([-1,1]) / 10

        vals = list(range(-9,10))
        shuffle(vals)
        variations = [f"v{i}" for i in range(4)]
        shuffle(variations)
        criteria = [
            {"positive": True, "a": vals[0], variations[0]: True},
            {"negative": True, "a": vals[1], variations[1]: True},
            {"zero": True, "a": vals[2], variations[2]: True},
            {"DNE": True, "a": vals[3], variations[3]: True},
        ]
        shuffle(criteria)


        return {
            "base": base,
            "baseval": format(n(baseval), '.1f'),
            "increment": format(n(increment), '.1f'),
            "incrementval": format(n(incrementval), '.1f'),
            "secantslope": format(n((incrementval - baseval)/(increment - base)), '.2f'),
            "criteria": criteria,
        }
