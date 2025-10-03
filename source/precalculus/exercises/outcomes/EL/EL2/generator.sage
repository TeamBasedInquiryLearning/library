class Generator(BaseGenerator):
  def data(self):
    flip = choice(["horizontal", "vertical"])
    if flip == "horizontal":
      shift = choice(["north", "south"])
    else:
      shift = choice(["north", "south", "east", "west"])
    
    b, s = sample([2,3,4,5,6], 2)
    if choice(range(4)) == 0:
      b = exp(1)

    if flip == "horizontal":
      if shift == "north":
        f = b^(-x)+s
        ftex = LatexExpr("\\left(\\frac{1}{") + \
          latex(b) + LatexExpr("}\\right)^x +") + latex(s)
        c = 0
        d = s
      else:
        f = b^(-x)-s
        ftex = LatexExpr("\\left(\\frac{1}{") + \
          latex(b) + LatexExpr("}\\right)^x -") + latex(s)
        c = 0
        d = -s
    else:
      if shift == "north":
        f = -b^x+s
        c = 0
        d = s
      elif shift == "south":
        f = -b^x-s
        c = 0
        d = -s
      elif shift == "west":
        f = -b^(x+s)
        c = -s
        d = 0
      else:
        f = -b^(x-s)
        c = s
        d = 0
      ftex = latex(f)

    return {
      "f": f,
      "ftex": ftex,
      "range": f"(-\\infty,{d})" if flip=="vertical" else f"({d},\\infty)",
      "asymptote": d,
      "hshift": c,
      "vflipped": flip == "vertical",
      "hflipped": flip == "horizontal",
    } 

  @provide_data
  def graphics(data):
    ymin = data["asymptote"]-8 if data["vflipped"] else min(data["asymptote"]-2, -1)
    ymax = max(data["asymptote"]+2,1) if data["vflipped"] else data["asymptote"]+8
    p=plot( data["f"],(x,-8,8),ymin=ymin,ymax=ymax,thickness=3,gridlines=[[-8..8],[ymin..ymax]])
    p1 = (data["hshift"],data["f"].subs({x:data["hshift"]}))
    p2 = (data["hshift"]+1,data["f"].subs({x:data["hshift"]+1})) if not data["hflipped"] else (data["hshift"]-1,data["f"].subs({x:data["hshift"]-1}))
    p+=point([p1,p2],pointsize=50,color='blue')
    p+=line([(-9,data["asymptote"]),(9,data["asymptote"])], linestyle="--", color='red',xmin=-8, xmax=8, ymin=ymin, ymax=ymax, thickness=3)
    return {"plot": p}
