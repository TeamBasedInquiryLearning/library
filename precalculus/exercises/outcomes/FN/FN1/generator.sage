class Generator(BaseGenerator):
    def data(self):


      tasks = [
                {"map_task": {"a": 2}},
                {"table_task": {"b": 3}},
            ]
      shuffle(tasks)

      return {
        "pairs": 3,
        "tasks":tasks,
      } 

    @provide_data
    def graphics(data):
      p=ellipse((-2,0),1,2,fill=True,alpha=0.3)
      p+=ellipse((2,0),1,2,fill=True,alpha=0.3)
      p+=arrow( (-2,1.5), (2,-1.5))
      p+=arrow( (-2,1.5), (2,1.5))
      p+=arrow( (-2,0), (2,-1.5))
      p+=arrow( (-2,-1.5), (2,0))
      p+=text("$2$", (-2,1.5),fontsize=20,horizontal_alignment="right",color="black")
      p+=text("$3$", (-2,0),fontsize=20,horizontal_alignment="right",color="black")
      p+=text("$4$", (-2,-1.5),fontsize=20,horizontal_alignment="right",color="black")
      p+=text("$5$", (2,1.5),fontsize=20,horizontal_alignment="left",color="black")
      p+=text("$6$", (2,0),fontsize=20,horizontal_alignment="left",color="black")
      p+=text("$7$", (2,-1.5),fontsize=20,horizontal_alignment="left",color="black")
      p.axes(False)

      return {
            "mapping": plot(p)
      }