class Generator(BaseGenerator):
    def data(self):

      #Task 1
      function_type=choice(["polynomial","root","rational"])
      if function_type=="polynomial":
         d1=choice([2,3,4])
         d2=choice([0,1,2])
         d3=choice([0,1])
         f= choice([-4..-1,1..4])*x^d1+choice([-4..4])*x^d2 + choice([-4..1,1..4])*x^d3
         a=choice([-4..4])
         b=a+choice([2..6])
      elif function_type=="root":
        c=choice([1..4])
        d=choice([-5..-1,1..5])
        f=sqrt(c*x+d)
        a= round(-d/c,0)+ choice([2..6])
        b=a+choice([2..6])
      else: #rational
        c=choice([1..4])
        d=choice([-5..-1,1..5])
        e=choice([-4..4])
        f=choice([-4..-1,1..4])
        f=(e*x+f)/(c*x+d)
        a= round(-d/c,0)+ choice([2..6])
        b=a+choice([2..6])


      rate=(f.subs({x:b})-f.subs({x:a}))/(b-a)

      #Task 2
      tasks=[]

      #Graph
      m=choice([-3,-3+1/2,..,3])
      g=m*x+choice([-6..-1,1..6])
      #tasks.append({"graph_task":True,"line": "Line", "slope": f"{round(m,1):g}"})
      tasks.append({"graph_task":True,"line": "Line", "slope": m})

      slopes=[choice([-5..5])]
      d=choice([2..5])
      slopes.append(choice([-5..5])+choice([1..d-1])/d)
      shuffle(slopes)

      #Table
      m=slopes.pop()
      h=m*x+choice([-6..-1,1..6])
      if m.is_integer():
        xvals=sample([-7..7],choice([4..6]))
      else:
        xvals=sample([-3*d, -2*d, .., 3*d],choice([4..6]))
      points=[(a, h.subs({x:a})) for a in sorted(xvals)]
      tasks.append({"table_task":True,"table_rows": [{"x":p1, "y":p2} for (p1,p2) in points], "slope": m})



      #Two points
      p1=(choice([-8..8]),choice([-8..8]))
      m=slopes.pop()
      if m.is_integer():
        px=choice([-4..-1,1..4])
      else:
        px = choice([-3..-1,1..3])*d
      p2=(p1[0]+px, p1[1]+m*px )
      tasks.append({"points_task":True,"point1": p1, "point2": p2, "slope": m})

      shuffle(tasks)

      return {
        "f": f,
        "interval": f"[{a},{b}]",
        "rate": rate,
        "line_tasks": tasks,
        "g":g,
      } 

    @provide_data
    def graphics(data):
       p=plot(data["g"],-10,10,ymin=-10,ymax=10,thickness=2,gridlines=True,ticks=[1,1],aspect_ratio=1)
       return {"plot":p}