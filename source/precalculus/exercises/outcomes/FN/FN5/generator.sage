class Generator(BaseGenerator):
    def data(self):

      fname1,fname2,fname3,fname4 = sample(["f","g","h","p","q","r"],4)

      functions = [choice([2..6])*x+choice([-5..5]),
                            choice([2..4])*x^2+choice([-3..3])*x^(choice([0,1])),
                            choice([1,2])*x^3+choice([-3..3])*x^(choice([0,1,2])),
                            sqrt(choice([2..5])*x+choice([-4..4])),
                            choice([1..4])*x/(x+choice([-5..-1,1..5]))
                            ]
      #f3(x)=choice(functions)
      f1,f2,f3,f4 = sample(functions,4)
      swap=choice([True,False])
      xval=choice([-5..-1,1..5])
      if swap:
        comp = f4.subs(x=f3)
        compx= f3.subs(x=f4).subs(x=xval)
      else:
        comp = f3.subs(x=f4)
        compx= f4.subs(x=f3).subs(x=xval)

      return {
        "funct1": f1,
        "funct2": f2,
        "funct3": f3,
        "funct4": f4,
        "fname1": fname1,
        "fname2": fname2,
        "fname3": fname3,
        "fname4": fname4,
        "sum": f1+f2,
        "difference": f1-f2,
        "product": f1*f2,
        "quotient": f1/f2,
        "swap":swap,
        "composition":comp,
        "xvalue":xval,
        "composition_value":compx
      } 
  