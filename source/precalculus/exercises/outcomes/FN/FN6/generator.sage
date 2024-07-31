class Generator(BaseGenerator):

  def data(self):
    function_type = choice(["rational","odd_root"])
    a,b,c,d = sample([choice([-1,1])*n for n in [1,2,3,5,7]], 4)
    if function_type=="rational":
      f=(a*x+b)/(c*x+d)
      f_inv = (-d*x+b)/(c*x-a)
    if function_type=="odd_root":
      r=choice([1/3,1/5,1/7,3,5,7])
      f=a+(x+b)^r
      f_inv = (x-a)^(1/r)-b

    return {
      "f": f,
      "f_inverse": f_inv,
      "fname": choice(["f","g","h"])
    } 