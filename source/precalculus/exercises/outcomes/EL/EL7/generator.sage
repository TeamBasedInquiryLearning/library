from decimal import Decimal
class Generator(BaseGenerator):
  def data(self):
    scenario = "scenario"+choice(["A","B","C","D"])

    if scenario == "scenarioA":
      APR = choice([2,2.25,..,6])
      r=APR/100
      compounding , n = choice([("annually", 1), ("semiannually", 2), ("quarterly", 4), ("monthly", 6)])
      amount = choice([10,..,30])*1000
      variable = var('t')
      f=amount*pow(1+r/n,n*variable)
      xrange = [5..25]
      scenario_params={"APR": Decimal(str(APR)).normalize(), 
                       "compounding": compounding,
                       "amount": amount,
                       "f": f"A({variable})=P\left(1+\dfrac{{r}}{{n}}\\right)^{{ n{variable} }}",
                       "var": variable,
                       "account": choice(["savings account", "529 college savings account", "certificate of deposit"]),
                      }
    elif scenario == "scenarioB":
      creatures, units, amount, b = choice([("bacteria", "days", 1000*choice([1..9]), choice([1.2,1.4,..,2.6])),
                                            ("deer", "years", 100*choice([2..8]), choice([1.5,1.6,..,2.5])), 
                                            ("algae", "days", 1000*choice([2..8]), choice([1.5,1.6,..,3.5])), 
                                            ("jellyfish", "weeks", 1000*choice([2..8]), choice([1.5,1.6,..,3.5])), 
                                           ])
      variable = var('t')
      f=amount*b^variable
      x0=choice([2..5])
      xrange = [x0+1..10]
      scenario_params={"creatures": creatures,
                       "units": units,
                       "amount": amount,
                       "f": f"P({variable})=a\cdot b^{variable}",
                       "x0": x0,
                       "y0": round(f.subs({variable:x0}),0),
                      }
    
    elif scenario == "scenarioC":
      APR = choice([2,2.25,..,6])
      r=APR/100
      amount = choice([30,..,60])*1000
      variable = var('t')
      f=amount*pow(1-r,variable)
      xrange = [5..25]
      scenario_params={"APR": Decimal(str(APR)).normalize(), 
                       "amount": amount,
                       "f": f"A({variable})=A\left(1-r\\right)^{{ {variable} }}",
                       "var": variable,
                       "asset": choice(["car", "RV", "boat"]),
                      }

    elif scenario == "scenarioD":
      isotope, units, amount, half_life, time_units = choice([("Carbon-14", "grams", choice([120,125,..,300]), 5730, "years"),
                                                              ("Cesium-137", "micrograms",choice([100,150,..,900]), 30, "years"),
                                                              ("Uranium-235", "grams",choice([100,120,..,900]), 704, "million years"),
                                                              ("Plutonium-239", "grams",choice([100,120,..,900]), 24065, "years"),
                                                            ])
      variable = var('t')
      f=amount*2^(-1*variable/half_life)
      #x0=choice([2..5])
      xrange = [i*half_life for i in [2..6]]
      scenario_params={"isotope": isotope,
                       "units": units,
                       "amount": amount,
                       "half_life": half_life,
                       "time_units": time_units,
                       "f": f"A({variable})=A\cdot \\left(\\frac{{1}}{{2}}\\right)^{{\\left( \\frac{{ {variable} }}{{h}} \\right)}}",
                       #"x0": x0,
                       #"y0": round(f.subs({variable:x0}),0),
                      }

    point1, point2 = tuple([ (a, f.subs({variable:a})) for a in sample(xrange,2)])
    tasks = [ {"find_y_task": { "x": point1[0], "y": round(point1[1],0) }},
              {"find_x_task": { "x": point2[0], "y": round(point2[1],0) }},
            ]
    shuffle(tasks)

    return {
      scenario: scenario_params, 
      "tasks": tasks,
    } 