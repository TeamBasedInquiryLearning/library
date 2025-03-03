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

      plots = { "ellipse": False, "parabola": choice([True,False]), "points": choice([True,False]),
                "line": True, "cubic": True, "hyperbola": False, "piecewise": choice([True,False])}
      plots= [(k,plots[k]) for k in sample(list(plots),3)]

      tasks3=[ {"plot": f"plot{n}", "is_function": plots[n][1]} for n in [0..2]]

      return {
        "tasks":tasks,
        "map_function":map_function,
        "tasks2":tasks2,
        "tasks3":tasks3,
        "plots": plots,
      } 

    @provide_data
    def graphics(data):
      p=ellipse((-2,0),1,2,fill=True,alpha=0.1)
      p+=ellipse((2,0),1,2,fill=True,alpha=0.1)
      domain = sample([1..20],6)
      codomain = sample([1..20],6)
      for x in domain:
        p+=text(f"${x}$", (-2,1.5-0.6*domain.index(x)),fontsize=20,horizontal_alignment="right",color="black")

      for y in codomain:
        p+=text(f"${y}$", (2,1.5-0.6*codomain.index(y)),fontsize=20,horizontal_alignment="left",color="black")
      
      #draw arrows randomly but make it a function
      f={x:choice(codomain) for x in domain}
      for x in domain:
        p+= arrow( (-2,1.5-0.6*domain.index(x)), (2,1.5-0.6*codomain.index(f[x])))

      #If it's not supposed to be a function, draw an extra arrow
      if not data["map_function"]:
        x=choice(domain)
        y=choice([z for z in codomain if z!= f[x]])
        p+= arrow( (-2,1.5-0.6*domain.index(x)), (2,1.5-0.6*codomain.index(y)))

      p.axes(False)

      q=[]
      x = var('x')
      y = var('y')
      for (plot_type,is_function) in data["plots"]:
        if plot_type == "ellipse": 
          q.append(ellipse((choice([-3..3]),choice([-3..3])),choice([1..4]),choice([1..4]),thickness=2))
        if plot_type == "parabola" and is_function: 
          q.append(plot(choice([-1,1])*choice([1..3])*x^2+choice([-3..3])*x+choice([-3..3]),(x,-5,5),thickness=2))
        if plot_type == "parabola" and not is_function: 
          q.append(parametric_plot((choice([-1,1])*choice([1,3])*y^2+choice([-3..3])*y+choice([-3..3]),y),(y,-5,5),thickness=2))
        if plot_type == "points" and is_function: 
          q.append(point([(x,choice([-5..5])) for x in sample([-5..5],5)],size=30))
        if plot_type == "points" and not is_function: 
          xlist=[-5..5]
          duped_x=xlist.pop()
          q.append(point([(x,choice([-5..5])) for x in sample(xlist,3)],size=30)+point([(duped_x,y) for y in sample([-5..5],2)],size=30))
        if plot_type == "line":
          q.append(plot(choice([-4..4])*x+choice([-4..4]),(x,-5,5),thickness=2))
        if plot_type == "cubic":
          q.append(plot(choice([-1,1])*choice([1..3])*x^3+choice([-3..3])*x^2+choice([-3..3])*x+choice([-3..3]),(x,-5,5),thickness=2))
        if plot_type == "hyperbola":
          q.append(implicit_plot(choice([1..4])*x^2-choice([1..4])*y^2+choice([-1,1])*choice([1..4]),(x,-3,3),(y,-3,3),linewidth=2))
        if plot_type ==  "piecewise":
          cut=choice([-2..2])
          if is_function:
            xranges=[(x,-5,cut),(x,cut+1,5)]
          if not is_function:
            xranges=[(x,-5,cut),(x,cut-1,5)]
          shuffle(xranges)
          q.append(plot(choice([-1,1])*x^2+choice([-3..3])*x,xranges[0],thickness=2)+plot(choice([-3..3])*x+choice([-3..3]),xranges[1],thickness=2))


      return {
            "mapping": plot(p),
            "plot0": plot(q[0]),
            "plot1": plot(q[1]),
            "plot2": plot(q[2]),
      }

# trigger preview build...
