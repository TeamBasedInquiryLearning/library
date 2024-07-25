class Generator(BaseGenerator):
    def data(self):
        scenario = choice([
            "distance_toward",
            "distance_apart",
            "mixture_value",
            "mixture_percent",
        ])
        scenario_alt = choice([
            "scenarioA",
            "scenarioB"
        ])

        scenario = "distance_toward"
        scenario_alt = "scenarioB"
        data = {}

        if scenario == "distance_toward":
            d_unit = choice(["mi","km"])
            vehicles = choice(["trains", "cars", "trucks"])
            mults = sample(range(4,11),2)
            rates = [20*m for m in mults]
            time = 15*choice([3,5,7,9,11])  # minutes
            dist = sum(rates)*time/60
            data = {
                "dist": dist,
                "rate1": rates[0],
                "rate2": rates[1],
                "rate_diff": abs(rates[0]-rates[1]),
                "time": time,
                "d_unit": d_unit,
                "vehicles": vehicles,          
            }


        return {
          scenario: {
            scenario_alt: data
          }
        } 