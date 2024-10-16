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
            "scenarioB",
            "scenarioC",
            "scenarioD",
        ])
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

        result = {}

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
            result = {
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
            part1, part2, percentage = sample([10,20,30,40,60,70,80,90], 3)
            mixpart = part1*percentage/100 + part2*(100-percentage)/100
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
            result = {
                "name": name,
                "weight": weight,
                "part1": part1,
                "part2": part2,
                "percentage": percentage,
                "mixpart": mixpart,
                "totalamount": totalamount,
                "amount1": amount1,
                "amount2": amount2,
                "ingredient1": ingredient1,
                "ingredient2": ingredient2,
            }
        
        if scenario == "mixture_percent":
            if scenario_alt in ["scenarioA", "scenarioB"]:
                if scenario_alt == "scenarioA":
                    aprs = sample([4,5,6,7,8,9], 2)
                else:
                    aprs = sample([7,8,9,11,12,13], 2)
                investments = [n*1000 for n in sample(range(2,10),2)]
                totalinvestment = sum(investments)
                interests = [investments[i]*aprs[i]/100 for i in range(2)]
                totalinterest = sum(interests)
                result = {
                    "name": name,
                    "apr1": aprs[0],
                    "apr2": aprs[1],
                    "totalinvestment": totalinvestment,
                    "totalinterest": totalinterest,
                    "investment1": investments[0],
                    "investment2": investments[1],
                }
            else:
                denominator = choice([4,10])
                meats = sample([
                    "chuck",
                    "sirloin",
                    "brisket",
                    "round",
                    "beef"
                ], 2)
                juices = sample([
                    "apple juice",
                    "lemonade",
                    "limeade",
                    "orange juice",
                    "cranberry juice"
                ], 2)
                percents = [denominator*i for i in sample([2,3,4],2)]
                if denominator == 4:
                    parts = [25,75]
                    shuffle(parts)
                else:
                    part1 = choice([20,30,40,60,70,80])
                    parts = [part1,100-part1]
                mixpercent = (parts[0]*percents[0]+parts[1]*percents[1])/100
                result = {
                    "name": name,
                    "meat1": meats[0],
                    "meat2": meats[1],
                    "juice1": juices[0],
                    "juice2": juices[1],
                    "percent1": percents[0],
                    "percent2": percents[1],
                    "part1": parts[0],
                    "part2": parts[1],
                    "mixpercent": mixpercent,
                }


        return {
          scenario: {
            scenario_alt: result
          }
        } 