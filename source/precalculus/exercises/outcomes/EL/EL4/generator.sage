class Generator(BaseGenerator):
  def data(self):
    a=1
    b = choice([2,3,4,5,6])
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
      c = choice(range(1,8-b))*choice([-1,1])
    if shift == "vertical":
      d = choice(range(1,6))*choice([-1,1])
    
    f=a*log(k*x-c)/log(b)+d
    if a == 1:
      f_string = f"\\log _{{ {b} }} \\left({k*x-c}\\right)+{d}"
    else:
      f_string = f"-\\log _{{ {b} }} \\left({k*x-c}\\right)+{d}"

    return {
      "f": f,
      "f_string": f_string,
      "domain": f"(-\infty,{c})" if reflection=="horizontal" else f"({c},\infty)",
      "asymptote": c,
      "hshift": c,
      "base": b,
      "flipped": reflection == "vertical",
      "hflipped": reflection == "horizontal",
    } 

  @provide_data
  def graphics(data):
    ymin=-8
    ymax=8
    if data["hflipped"]:
      xmin=-8
      xmax = -1*data["hshift"]
      p1 = (data["hshift"]-1,data["f"].subs({x:data["hshift"]-1}))
      p2 = (data["hshift"]-data["base"],data["f"].subs({x:data["hshift"]-data["base"]}))
    else:
      xmin =data["hshift"] 
      xmax = 8
      p1 = (data["hshift"]+1,data["f"].subs({x:data["hshift"]+1}))
      p2 = (data["hshift"]+data["base"],data["f"].subs({x:data["hshift"]+data["base"]}))
    
    p=plot( data["f"],(x,xmin,xmax),ymin=ymin,ymax=ymax,thickness=3,gridlines=[[-8..8],[ymin..ymax]])
    p+=line([(data["asymptote"],-9),(data["asymptote"],9)], linestyle="--", color='red',xmin=-8, xmax=8, ymin=ymin, ymax=ymax, thickness=3)
    p+=point([p1,p2],pointsize=50,color='blue')
    return {"plot": p}