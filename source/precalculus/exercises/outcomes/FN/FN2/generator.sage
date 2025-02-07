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


    #Construct some line segments with integral slopes so that it passes through
    #few points (x,y) with y an integer and x not an integer
    #Pick endpoints of line segments
    xpoints=sample([2*n+choice([0,1]) for n in range(-4,4)],choice([4..5]))
    xpoints.sort()
    #Ensure origin is included
    if xpoints[-1] <=0:
       xpoints[-1] = choice([1,3])
    if xpoints[0] >=0:
       xpoints[0] = choice([-1,-3])

    #Pick first point arbitrarily
    points=[(xpoints[0], choice([-8..8]))]
    lines=[]
    slope=choice([-2..-1,1..2])
    for i in [1..len(xpoints)-1]:
      lines.append(slope*(x-points[i-1][0])+points[i-1][1])
      points.append((xpoints[i],lines[i-1].subs({x:xpoints[i]})))
      #Ensure slope for next piece is different
      slopes=[-2..-1,1..2]
      slopes.remove(slope)
      slope=choice(slopes)

    #Need to give them c, ask them to compute g(c)
    #So pick a point on the graph (c,gc)
    #Start with c
    c=choice([xpoints[0]+1,..,xpoints[-1]-1])
    #Figure out which line segment its on
    index=0
    while c>=xpoints[index+1]:
        index+=1
        if index==len(xpoints)-2:
            break
    #Get y-value from correct line
    gc=lines[index].subs({x:c})

    #Need to give them b, have them find all points a with g(a)=b
    #Pick a point on the graph (a,b)
    #Start with a
    a=choice([xpoints[0]+1,..,xpoints[-1]-1])
    #Figure out which line segment its on
    index=0
    while a>=xpoints[index+1]:
        index+=1
        if index==len(xpoints)-2:
            break
    #Get y-value from correct line
    b=lines[index].subs({x:a})

    #Find out what other x-values map to b
    xvalues=set()
    for j in [0..len(lines)-1]:
        if (points[j][1]<=b and b<=points[j+1][1]) or (points[j][1]>=b and b>=points[j+1][1]):
            s=solve(lines[j]==b,x)[0].rhs()
            if xpoints[j]<=s and s<=xpoints[j+1]:
                xvalues.add(round(s,1))

    tasks2=[ {"findy": {"xvalue": c, "gx": gc} },
             {"findx": {"result": b, "values": ",".join([ f"x={i:g}" for i in xvalues])}}
            ]
    shuffle(tasks2)

    return {
      "fname": fname,
      "f":flatex,
      "tasks":tasks,
      "gname": gname,
      "g_pieces":[((xpoints[i],xpoints[i+1]),lines[i]) for i in [0..len(lines)-1] ],
      "interval":f"[{xpoints[0]},{xpoints[-1]}]",
      "tasks2":tasks2,
      #"xvalue":c, 
      #"gx":gc,
      #"result":b,
      #Use the g (general format) to make sure 4 prints as 4, not 4.0
      #"values": [{"x": f"{i:g}"} for i in xvalues]
      #"values": ",".join([ f"x={i:g}" for i in xvalues])
    } 


  @provide_data
  def graphics(data):
    p=Graphics()
    ymin=-1
    ymax=1
    for piece in data["g_pieces"]:
      ymin=min(piece[1].subs({x:piece[0][0]}), piece[1].subs({x:piece[0][1]}),ymin)
      ymax=max(piece[1].subs({x:piece[0][0]}), piece[1].subs({x:piece[0][1]}),ymax)
      p+=plot(piece[1],piece[0][0],piece[0][1],thickness=3,gridlines=True,ticks=[1,1],aspect_ratio=1,ymin=ymin,ymax=ymax)
    return {"plot": p}