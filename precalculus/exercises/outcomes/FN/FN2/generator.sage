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


    R.<z> = PolynomialRing(QQ)
    count = choice([0..3])
    xpoints = sample([-8..8],3)
    xpoints.sort()
    ypoints = sample([-20..20],2)
    ypoints.sort()
    ypoints.append(choice([-20..(ypoints[1]-1)]))

    level=choice([-10..-1,1..7])
    ypoints=sample([(level+1)..12],3)
    ypoints.sort()
    xpoints=[]
    xpoints.append(choice([-8..-2]))
    xpoints.append(choice([(xpoints[0]+2)..8]))
    xpoints.append(choice([(xpoints[1]+2)..11]))
    xpoints.append(choice([(xpoints[2]+2)..15]))

    g_domain=(min(xpoints)-choice([3..5]),max(xpoints)+choice([2..5]))

    L1=[(xpoints[0]-1,level),(xpoints[0]+1,level), (xpoints[1],ypoints[0])]
    L2=[(xpoints[1],ypoints[1]),(xpoints[2],ypoints[2]), (xpoints[3],level) ]

    g1=R.lagrange_polynomial(L1)
    g2=R.lagrange_polynomial(L2)


    from sage.symbolic.integration.integral import indefinite_integral
    g=indefinite_integral((z-xpoints[0])*(z-xpoints[1])*(z-xpoints[2]),z)
    critical_points=xpoints+list(g_domain)
    r=max([abs(g.subs({z:p})) for p in critical_points])
    g=10/r*g+choice([-5,5])

    #g=R.lagrange_polynomial(lagrange_points)

    xvalue=choice([-4..4])

    return {
      "fname": fname,
      "f":flatex,
      "tasks":tasks,
      "gname": gname,
      "g":g,
      "g1":g1,
      "g2":g2,
      "cut":xpoints[1],
      "g_domain":g_domain,
      "xvalue":xvalue, 
      "gx":g.subs({z:xvalue}),
      "result":level,
      "values": [ {x:i for i in [xpoints[0],xpoints[]]}]
    } 


  @provide_data
  def graphics(data):
    p=plot(data["g1"],data["g_domain"][0],data["cut"],thickness=3)+plot(data["g2"],data["cut"],data["g_domain"][1],thickness=3)
    return {"plot": plot(p)}
      