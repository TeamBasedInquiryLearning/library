class Generator(BaseGenerator):
  def data(self):
    
    scenario = choice(["scenarioA"])

    m=choice([5,10])
    b=100
    thing,m,b, xrange = choice( [ ( "book", choice([3..15]), choice([100,200,..,1000]), [100,110,..,1000] ),
                          ( "insulated cup", choice([4..12]), choice([100,125,..,500]), [300,320,..,1200]),
                        ])
    verb_present,verb_past,verb_infinitive = choice([ ("manufacture","manufactured", "manufacturing"),
                                                      ("produce", "produced", "producing"),
                                                    ])
    C=m*x+b
    point1, point2 = tuple([ (a, C.subs({x:a})) for a in sample(xrange,2)])
    scenario_params = { "thing":thing,
                        "amount": m,
                        "fixed_amount": b,
                        "function": C,
                        "verb": verb_present,
                        "verbed": verb_past,
                        "verbing": verb_infinitive,
                      }
    taskset1 = [ {"slope_task": { "slope": m}},
                 {"intercept_task": {"intercept": b} }
               ]
    shuffle(taskset1)

    taskset2 = [ {"find_y_task": { "x":point1[0], "y": point1[1]}},
                 {"find_x_task": { "x":point2[0], "y": point2[1]}},
               ]
    shuffle(taskset2)

    return {
      scenario: scenario_params, 
      "taskset1": taskset1,
      "taskset2": taskset2,
    } 