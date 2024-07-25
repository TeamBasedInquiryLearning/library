class Generator(BaseGenerator):
    def data(self):


      map_function = choice([True,False])
      table_function = choice([True,False])
      pairs_function = choice([True,False])

      table_domain = sample([1..20],6)
      table_codomain = sample([1..20],6)
      table_pairs = [ (x, choice(table_codomain)) for x in table_domain]
      if not table_function:
        duplicated_x = choice([x for x in table_domain if x != table_domain[0]])
        #Make sure we don't put the same ordered pair in there twice.
        second_y= choice([y for y in table_codomain if (duplicated_x,y) not in table_pairs])                      
        table_pairs[0] = (duplicated_x, second_y)
        shuffle(table_pairs)

      pairs_domain = sample([1..20],6)
      pairs_codomain = sample([1..20],6)
      pairs = [ (x, choice(pairs_codomain)) for x in pairs_domain]
      if not pairs_function:
        duplicated_x = choice([x for x in pairs_domain if x != pairs_domain[0]])
        #Make sure we don't put the same ordered pair in there twice.
        second_y= choice([y for y in pairs_codomain if (duplicated_x,y) not in pairs])                      
        pairs[0] = (duplicated_x, second_y)
        shuffle(pairs)

      tasks = [
                {"map_task": {"map_function": map_function}},
                {"table_task": {"table_function": table_function,
                                "table_rows": [{"x": x, "y": y} for (x,y) in table_pairs]}},
                {"pairs_task": {"pairs_function": pairs_function,"pairs":pairs}},
            ]
      shuffle(tasks)

      var('x', 'y')
      #f needs to be a bijection
      f(y)= choice([1..5])*y^choice([3,5,7])
      g(x)= choice([1..5])*x^choice([2,4,6])

      tasks2 = [
        {"eq":CheckIt.shuffled_equation(f(y),-g(x)), "eq_function":True},
        {"eq":CheckIt.shuffled_equation(f(x),-g(y)), "eq_function":False},
      ]
      shuffle(tasks2)

      return {
        "tasks":tasks,
        "map_function":map_function,
        #"table_function":table_function,
        #"pairs_function":pairs_function,
        "tasks2":tasks2,
      } 

    @provide_data
    def graphics(data):
      p=ellipse((-2,0),1,2,fill=True,alpha=0.3)
      p+=ellipse((2,0),1,2,fill=True,alpha=0.3)
      domain = sample([1..20],6)
      codomain = sample([1..20],6)
      for x in domain:
        p+=text(f"${x}$", (-2,1.5-0.6*domain.index(x)),fontsize=20,horizontal_alignment="right",color="black")

      for y in codomain:
        p+=text(f"${y}$", (2,1.5-0.6*codomain.index(y)),fontsize=20,horizontal_alignment="left",color="black")
      
      #draw arrows randomly but make it a function
      for x in domain:
        p+= arrow( (-2,1.5-0.6*domain.index(x)), (2,1.5-0.6*choice([0..5])))

      #If it's not supposed to be a function, draw an extra arrow
      if not data["map_function"]:
        p+= arrow( (-2,1.5-0.6*choice([0..5])), (2,1.5-0.6*choice([0..5])))

      p.axes(False)

      return {
            "mapping": plot(p)
      }