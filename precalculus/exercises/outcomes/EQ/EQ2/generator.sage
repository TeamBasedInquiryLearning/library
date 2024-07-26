class Generator(BaseGenerator):
    def data(self):
        scenario = choice([
            "distance_toward",
            "distance_apart",
            "mixture_value",
            # "mixture_percent",
        ])
        scenario_alt = choice([
            "scenarioA",
            "scenarioB",
            "scenarioC",
            "scenarioD",
        ])

        data = {}

        if scenario == "distance_toward" or scenario == "distance_apart":
            d_unit = choice(["mi","km"])
            vehicles = choice(["trains", "cars", "trucks"])
            directions = choice([
                ["north", "south"],
                ["east", "west"],
                ["northeast", "southwest"],
                ["northwest", "southeast"],
            ])
            faster_slower = choice(["faster", "slower"])
            shuffle(directions)
            mults = sample(range(4,11),2)
            rates = [20*m for m in mults]
            time = choice([3,5,7,9,11])/4  # hours
            dist = sum(rates)*time
            data = {
                "dist": dist,
                "rate1": rates[0],
                "rate2": rates[1],
                "rate_diff": abs(rates[0]-rates[1]),
                "time": time,
                "d_unit": d_unit,
                "vehicles": vehicles,
                "direction1": directions[0],
                "direction2": directions[1],    
                "faster_slower": faster_slower,   
            }
        
        if scenario == "mixture_value":
            name = choice([
                "Anne-Fatima",
                "Boram",
                "Consolata",
                "Dalisay",
                "Edgar",
                "Fionnuala",
                "Gurlez",
                "Hisako",
                "Inga",
                "Julia",
            ])
            cost1, cost2, percentage = sample([10,20,30,40,60,70,80,90], 3)
            mixcost = cost1*percentage/100 + cost2*(100-percentage)/100
            totalamount = choice(range(10,100,10))
            amount1 = totalamount*percentage/100
            amount2 = totalamount*(100-percentage)/100
            if scenario_alt in ["scenarioA", "scenarioB"]:
                weight = choice(["lb", "kg"])
                ingredient1, ingredient2 = sample([
                    "chocolate",
                    "caramel",
                    "nuts",
                    "taffy",
                ], 2)
            else:
                weight = choice(["oz"])
                ingredient1, ingredient2 = sample([
                    "strawberry",
                    "banana",
                    "mango",
                    "peach",
                ], 2)
            data = {
                "name": name,
                "weight": weight,
                "cost1": cost1,
                "cost2": cost2,
                "percentage": percentage,
                "mixcost": mixcost,
                "totalamount": totalamount,
                "amount1": amount1,
                "amount2": amount2,
                "ingredient1": ingredient1,
                "ingredient2": ingredient2,
            }


        return {
          scenario: {
            scenario_alt: data
          }
        } 