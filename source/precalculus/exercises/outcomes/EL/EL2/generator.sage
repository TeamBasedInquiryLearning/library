class Generator(BaseGenerator):
  def data(self):
    a=1
    b = choice([2..6]+[e])
    c=0
    d=0
    k=1

    reflection = choice(["vertical", "horizontal"])
    if reflection == "horizontal":
      shift="vertical"
    else:
      shift = choice(["vertical","horizontal"])
    
    if reflection == "horizontal":
      k = -1
    if reflection == "vertical":
      a=-1
    if shift == "horizontal":
      c = choice([-4..-1,1..4])
    if shift == "vertical":
      d = choice([-5..-1,1..5])
    
    f=a*b^(k*x-c)+d

    return {
      "f": f,
      "range": f"(-\infty,{d})" if reflection=="vertical" else f"({d},\infty)",
      "asymptote": d,
      "hshift": c,
      "flipped": reflection == "vertical",
      "hflipped": reflection == "horizontal",
    } 

  @provide_data
  def graphics(data):
    ymin = data["asymptote"]-8 if data["flipped"] else data["asymptote"]-2
    ymax = data["asymptote"]+2 if data["flipped"] else data["asymptote"]+8
    p=plot( data["f"],(x,-8,8),ymin=ymin,ymax=ymax,thickness=3,gridlines=[[-8..8],[ymin..ymax]])
    #p=plot( data["f"],(x,-3,3),ymin=-2,ymax=8,thickness=3,gridlines=[[-8..8],[-8..8]])
    p1 = (data["hshift"],data["f"].subs({x:data["hshift"]}))
    p2 = (data["hshift"]+1,data["f"].subs({x:data["hshift"]+1})) if not data["hflipped"] else (data["hshift"]-1,data["f"].subs({x:data["hshift"]-1}))
    p+=point([p1,p2],pointsize=50,color='blue')
    p+=line([(-9,data["asymptote"]),(9,data["asymptote"])], linestyle="--", color='red',xmin=-8, xmax=8, ymin=ymin, ymax=ymax, thickness=3)
    return {"plot": p}
