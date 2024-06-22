class Generator(BaseGenerator):
    def data(self):
        scenario = choice(["box","sales","river"])

        # omitted as comparatively easy
        # if scenario == "rectangle":
        #     fencing = 20*randrange(4,31)
        #     units = choice(["feet", "meters", "yards"])
        #     area = fencing^2/8
        #     person = choice([
        #         "homeowner",
        #         "friend",
        #         "farmer",
        #         "colleague",
        #         "neighbor",
        #     ])
        #     wording = f"wording{randrange(4)}"
        #     data = {
        #         scenario: True,
        #         wording: True,
        #         "fencing": fencing,
        #         "units": units,
        #         "area": area,
        #         "person": person,
        #     }
        if scenario == "box":
            dimensions = choice([
                # chosen so m^2+n^2-mn is square
                [3,8],
                [5,8],
                [7,15],
                [8,15],
                [11,11],
                [13,13],
                [7,7],
            ])
            shuffle(dimensions)
            prelength,prewidth = dimensions # 1/6 of actual length/width
            scale = randrange(2,10)
            prelength = prelength*scale 
            prewidth = prewidth*scale
            length = prelength*6
            width = prewidth*6
            crit = prelength+prewidth-sqrt(prelength^2+prewidth^2-prelength*prewidth)
            # vol = crit*(length-2*crit)*(width-2*crit)
            units = choice([
                "inches",
                "centimeters",
                "millimeters",
            ])
            data = {
                "length": length,
                "width": width,
                "crit": crit,
                "units": units,
            }


        
        elif scenario == "sales":
            change_in_sales = randrange(2,10)
            base_sales = 2*change_in_sales*randrange(30,100)
            optimal_cost_change = randrange(1,6)*choice([-1,1])
            # if randrange(3)==0:
            #     optimal_cost_change = 0
            # else:
            #     optimal_cost_change = randrange(1,6)*choice([-1,1])
            base_cost = base_sales/change_in_sales-2*optimal_cost_change
            widget = choice([
                "thingamajig",
                "widget",
                "gizmo",
            ])
            person = choice([
                "supervisor",
                "boss",
                "manager",
            ])
            farmer = choice([
                "farmer",
                "rancher",
                "horticulturist",
            ])
            plant = choice([
                "plant",
                "tree",
                "shrub",
            ])
            pound = choice([
                'kilogram',
                'pound'
            ])
            if optimal_cost_change > 0:
                optimal_change = "increase"
            elif optimal_cost_change == 0:
                optimal_change = "keep"
            else:
                optimal_change = "decrease"
            data = {
                "widget": widget,
                "person": person,
                "base_cost": base_cost,
                "base_sales": base_sales,
                "change_in_sales": change_in_sales,
                "optimal_cost_change": abs(optimal_cost_change),
                "farmer": farmer,
                "pound": pound,
                "plant": plant,
                optimal_change: True,
            }
        
        elif scenario == "river":
            triple = choice([
                [5,12,13],
                [12,5,13],
                [8,15,17],
                [15,8,17],
                [24,7,25],
            ])
            land_speed = triple[2]
            river_speed = triple[0]
            width = triple[1]*randrange(2,6)
            optimal_swimming = river_speed*width/triple[1]
            optimal_running = width + randrange(10,100)
            length = optimal_swimming + optimal_running
            predator = choice([
                "crocodile",
                "tiger",
                "lion",
            ])
            prey = choice([
                "zebra",
                "warthog",
                "bushpig",
            ])
            units = choice(["feet", "meters", "yards"])
            speedrunner = choice(["M","N","Ch","F","St"]) + \
                choice(["a","i","u","o"]) + \
                choice(["ll","ss","bb"]) + \
                choice(["eo","y","ia"])
            avatar = choice ([
                "avatar",
                "character",
                "plumber",
                "superhero",
            ])
            pixels = choice([
                "pixels",
                "bloxels",
                "units",
            ])

            data = {
                "land_speed": land_speed,
                "river_speed": river_speed,
                "width": width,
                "length": length,
                "optimal_running": optimal_running,
                "predator": predator,
                "prey": prey,
                "units": units,
                "pixels": pixels,
                "avatar": avatar,
                "speedrunner": speedrunner,
            }

        data[scenario] = True
        data[f"wording{randrange(4)}"] = True

        return data