class Generator(BaseGenerator):
    def data(self):
      (fname,gname)=sample(["f","g","h"],2)

      types = sample(["polynomial","radical","rational"],2)
      cut=choice([-2..2])

      pieces=[]
      for type in types:
        if type == "polynomial":
          pieces.append(choice([1..3])*x^choice([2,3])+choice([-3..3])*x^choice([0,1]))
        if type == "radical":
          pieces.append(sqrt(choice([1,3])*x^2+choice([1,5])))
        if type == "rational":
          pieces.append((choice([1,4])*x+choice([-4..4]))/(choice([1,2])*x^2+choice([1..5])))
      
      f1(x)=pieces[0]
      f2(x)=pieces[1]

      #f1(x)=-x^2
      #f2(x)=x^3

      cut_left = choice([True,False])
      if cut_left:
        intervals=[[-5,cut],(cut,5)]
      else:
        intervals=[(-5,cut),[cut,5]]
      f(x) = piecewise([(intervals[0], f1(x)), (intervals[1], f2(x))])
      flatex=r"\begin{cases}"+latex(f1(x))
      if cut_left: 
        flatex += r"& -5 < x \leq "
      else:
        flatex += r"& -5 < x < "
      flatex +=str(cut)+r" \\ "+ latex(f2(x))+r" & "+ str(cut) 
      if cut_left:
        flatex+=r" < x < 5 "
      else:
        flatex+=r" \leq x < 5 "
      flatex+=r"\end{cases}"

      x1=choice([-4..cut-1])
      x2=choice([cut+1..4])

      tasks= [ {"value": x1, "result": f(x1)}, {"value": x2, "result": f(x2)}, {"value":cut, "result":f(cut)}]
      shuffle(tasks)


      g0(x)= choice([-4..-1,1..4])*x+choice([-4..4])
      g1(x)= choice([-4..-1,1..4])*x+choice([-4..4])

      cut2 = choice([-2..2])
      g1(x)=g1(x)+g0(cut2)-g1(cut2)

      g=piecewise([((-5,cut2),g0(x)),([cut2,5],g1(x))] )
      xvalue=choice([-4..4])

      return {
        "fname": fname,
        "f":flatex,
        "tasks":tasks,
        "gname": gname,
        "g_pieces":[g0,g1],
        "g_interval":[(x,-5,cut2),(x,cut2,5)],
        "xvalue":xvalue, 
        "gx":g(xvalue),
        
      } 


    @provide_data
    def graphics(data):
      p=plot(data["g_pieces"][0],data["g_interval"][0])+plot(data["g_pieces"][1],data["g_interval"][1])
      return {"plot": plot(p)}
        