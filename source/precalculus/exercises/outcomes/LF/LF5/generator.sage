class Generator(BaseGenerator):
  def data(self):
    
    scenario = choice(["scenarioA", "scenarioB"])

    if scenario == "scenarioA":
      m=choice([5,10])
      b=100
      thing,m,b, xrange = choice( [ ( "book", choice([3..15]), choice([100,200,..,1000]), [100,110,..,1000] ),
                            ( "insulated cup", choice([4..12]), choice([100,125,..,500]), [300,320,..,1200]),
                            ( "hat", choice([5..13]), choice([300,320,..,600]), [50,60,..,200]),
                            ( "widget", choice([8..20]), choice([100,125,..,1000]), [100,200,..,2000]),
                            ( "poster", choice([1..5]), choice([50,60,..,200]), [300,350,..,800]),
                          ])
      verb_present,verb_past,verb_infinitive = choice([ ("manufacture","manufactured", "manufacturing"),
                                                        ("produce", "produced", "producing"),
                                                      ])
      f=m*x+b
      offset = 0 
      scenario_params = { "thing":thing,
                          "amount": m,
                          "fixed_amount": b,
                          "function": f,
                          "verb": verb_present,
                          "verbed": verb_past,
                          "verbing": verb_infinitive,
                        }

    elif scenario == "scenarioB":
      b = choice([20000,21000,..,100000])
      offset = choice([2000,..,2023])
      sign = choice([-1,1]) 
      if sign == 1:
        verb = choice(["grown", "increased" ])
      else:
        verb = choice(["shrunk", "decreased"])

      m = int(sign*choice([1000,1500,..,round(b/10,-3)]))

      f = m*x+b
      if sign==1:
        xrange = [5,..,25]
      else:
        xrange = [5,..,floor(b/abs(m))-1]


      scenario_params = { "town": choice(["Sunnydale", "Capeside", "Hawkins", "Pawnee", "Hill Valley", "Springfield", "Stars Hollow", "Bayside"]),
                          "initial_population": "{:,}".format(b),
                          "year": offset,
                          "rate": abs(m),
                          "function": f,
                          "verbed": verb,
                        }



    taskset1 = [ {"slope_task": { "slope": m}},
                 {"intercept_task": {"intercept": b} }
               ]
    shuffle(taskset1)

    point1, point2 = tuple([ (a, f.subs({x:a})) for a in sample(xrange,2)])
    taskset2 = [ #{"find_y_task": { "x":f"{point1[0]+offset:,}", "y": f"{point1[1]:,}"}},
                 #{"find_x_task": { "x":f"{point2[0]+offset:,}", "y": f"{point2[1]:,}"}},
                 {"find_y_task": { "x":point1[0]+offset, "y": "{:,}".format(int(point1[1]))}},
                 {"find_x_task": { "x":point2[0]+offset, "y": "{:,}".format(int(point2[1]))}},
               ]
    shuffle(taskset2)

    return {
      scenario: scenario_params, 
      "taskset1": taskset1,
      "taskset2": taskset2,
    } 