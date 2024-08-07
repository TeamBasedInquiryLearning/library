load("../sage/common.sage")

class Generator(BaseGenerator):
  def data(self):
    

    methods=["factoring", "the square root property", "completing the square", "the quadratic formula"]
    equations =[]

    #Factoring
    r1=choice([-1,1])*choice([2..6])
    r2=choice([-1,1])*choice([2..6])
    equations.append( { "equation":  x^2-(r1+r2)*x==-1*r1*r2, "method":"factoring", "roots": f"{r1}\\text{{ and }}{r2}"})

    #Square root property
    a=choice([2..5])
    h=choice([-7..-1,1..7])
    c=choice([2..5])
    k=choice([-10..-1,1..10])
    d=k+a*c^2
    equations.append( { "equation":  a*(x-h)^2+k==d , "method":"the square root property", "roots": f"{h+c}\\text{{ and }}{h-c}"})

    #Completing the square

    a=choice([-7..7])
    b=(a+choice([1..4]))^2-a^2
    equations.append( { "equation":  x^2+2*a*x== (b+a^2) , "method":"completing the square", "roots": f"{-1*a+sqrt(b+a^2)}\\text{{ and }}{-1*a-sqrt(b+a^2)} "})

    #Quadratic Equation
    irrationals = list(TBILPrecal.small_irrationals(rational_part=[-8..1,1..8]).items())[0]
    r1,r2=irrationals[0]
    c=irrationals[1]
    equations.append( { "equation": c^2*x^2-2*(r1+r2)*c^2*x == expand(-1*c^2*r1*r2), 
                       "method":"the square root property", "roots": f"{latex(r1)}\\text{{ and }}{latex(r2)}"})
    shuffle(equations)


    return {
      "equations": equations
    } 