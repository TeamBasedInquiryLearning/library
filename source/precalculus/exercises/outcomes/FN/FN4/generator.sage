class Generator(BaseGenerator):
  def data(self):
    fname,gname=sample(["f","g","h"],2)
    functions = [ choice([-1,1])*sqrt(4-x^2), 
                  choice([-1,1])*(4-x^2),
                  choice([-1,1])*(4-abs(x))
                ]
    f=choice(functions)
    #a=choice([-1,1])
    b=choice([1..5])
    c=choice([1..5])
    hshift=choice(["left","right"])
    vshift=choice(["up","down"])
    flipped=choice([True,False])
    if hshift=="left":
      g=f.subs(x=(x+b))
    if hshift=="right":
      g=f.subs(x=(x-b))

    if flipped:
      g=-g

    if vshift=="up":
      g=g+c
    if vshift=="down":
      g=g-c
    


    return {
      "fname":fname,
      "gname":gname,
      "g_transform": f"{'-' if flipped else ''}{fname}(x{'+' if hshift=='left' else '-'}{b}){'+'if vshift=='up' else '-'}{c}",
      "f":f,
      "g":g,
      "b":b,
      "c":c,
      "hshift":hshift,
      "vshift":vshift,
      "flip":flipped
    } 

  @provide_data
  def graphics(data):
    q=plot(data["f"],-2,2,ymin=-8,ymax=8,thickness=3,gridlines=[[-8..8],[-8..8]])
    q.xmin(-8)
    q.xmax(8)
    if data["hshift"]=="left":
      p=plot(data["g"],-2-data["b"],2-data["b"],ymin=-8,ymax=8,thickness=3,gridlines=[[-8..8],[-8..8]])
    else:
      p=plot(data["g"],-2+data["b"],2+data["b"],thickness=3,aspect_ratio=1)
    p.xmin(-8)
    p.xmax(8)
    return {"plot1": q,
            "plot2": p}
