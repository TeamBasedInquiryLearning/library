class Generator(BaseGenerator):
    def data(self):

      fname1,fname2,fname3,fname4 = sample(["f","g","h","p","q","r"],4)

      functions = [choice([2..6])*x+choice([-5..5]),
                            choice([2..4])*x^2+choice([-3..3])*x^(choice([0,1])),
                            choice([1,2])*x^3+choice([-3..3])*x^(choice([0,1,2])),
                            sqrt(choice([2..5])*x+choice([1..4]),hold=True),
                            choice([1..4])*x/(x+choice([-5..-1,1..5]))
                            ]
      #f3(x)=choice(functions)
      f1,f2,f3,f4 = sample(functions,4)
      comp = f4.subs(x=f3,hold=True)

      #Ensure we choose a value that does not cause a rational denominator to vanish or for a complex number to arise
      xval=choice([a for a in [-6..-1,1..6] if (not f4.is_rational_expression() or (f4.is_rational_expression() and f4.denominator().subs({x:a})!=0)) \
                   and f4.subs({x:a}).imag_part()==0   \
                   and (not f3.is_rational_expression() or (f3.is_rational_expression() and f3.denominator().subs({x:f4.subs({x:a})})!=0)) \
                   and f3.subs({x:(f4.subs({x:a}))}).imag_part()==0  ])
      compx= f3.subs(x=f4).subs(x=xval)

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
        "swap": choice([True,False]),
        "composition":comp,
        "xvalue":xval,
        "composition_value":compx
      } 
  