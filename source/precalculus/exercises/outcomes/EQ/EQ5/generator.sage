load("../sage/common.sage")

class Generator(BaseGenerator):
  def data(self):
    

    methods=["factoring", "the square root property", "completing the square", "the quadratic formula"]
    equations =[]

    #Factoring
    r1=choice([-1,1])*choice([2..6])
    #Make sure r1+r2 is odd
    if r1 % 2 == 0:
      r2=choice([-1,1])*choice([1,3,5,7])
    else:
      r2 = choice([-1,1])*choice([2,4,6,8])
    equations.append( { "equation":  x^2-(r1+r2)*x==-1*r1*r2, "method":"factoring and the zero product property", "roots": f"{r1}\\text{{ and }}{r2}"})

    #Square root property
    a=choice([2..5])
    h=choice([-7..-1,1..7])
    c=choice([sqrt(i) for i in [2..12] if not i.is_square()])
    k=choice([-10..-1,1..10])
    d=k+a*c^2
    equations.append( { "equation":  a*(x-h)^2+k==d , "method":"the square root property", "roots": f"{latex(h+c)}\\text{{ and }}{latex(h-c)}"})

    #Completing the square

    a=choice([-7..7])
    b=choice([i for i in [-1*a^2+5,..,10] if not (i+a^2).is_square()])
    r1=-1*a+sqrt(b+a^2)
    r2=-1*a-sqrt(b+a^2)
    equations.append( { "equation":  x^2+2*a*x== b , "method":"completing the square", "roots": f"{latex(r1)}\\text{{ and }}{latex(r2)} "})

    #Quadratic Equation
    irrationals = list(TBILPrecal.small_irrationals(rational_part=[-8..1,1..8]).items())[0]
    r1,r2=irrationals[0]
    c=irrationals[1]
    equations.append( { "equation": c^2*x^2-(r1+r2)*c^2*x == expand(-1*c^2*r1*r2), 
                       "method":"the quadratic formula", "roots": f"{latex(r1)}\\text{{ and }}{latex(r2)}"})
    shuffle(equations)


    return {
      "equations": equations
    } 
