class Generator(BaseGenerator):
    def data(self):


      map_function = choice([True,False])
      table_function = choice([True,False])
      pairs_function = choice([True,False])



      tasks = [
                {"map_task": {"map_function": map_function}},
                {"table_task": {"table_function": table_function}},
                {"pairs_task": {"pairs_function": pairs_function}},
            ]
      shuffle(tasks)

      return {
        "tasks":tasks,
        "map_function":map_function,

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