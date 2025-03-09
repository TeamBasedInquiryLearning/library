load("../../../source/common/sagemath/library.sage")

class Generator(BaseGenerator):
  irrational_dict = TBIL.small_irrationals(rational_part=[-8..1,1..8],full_list=True)
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
    irrational = choice(list(self.irrational_dict.keys()))
    r1,r2=irrational
    c=self.irrational_dict[irrational]
    equations.append( { "equation": c^2*x^2-(r1+r2)*c^2*x == expand(-1*c^2*r1*r2), 
                       "method":"the quadratic formula", "roots": f"{latex(r1)}\\text{{ and }}{latex(r2)}"})
    shuffle(equations)

    #Imaginary roots task
    r1=choice([-5..,-1,1..5])+choice([1..5])*I
    r2=conjugate(r1)
    imaginary_equation = expand((x-r1)*(x-r2)) == 0
    imaginary_roots = f"{latex(r1)}\\text{{ and }}{latex(r2)}"

    return {
      "equations": [ {"equation": f"{latex(eq['equation'].lhs())}={latex(eq['equation'].rhs())}", "method": eq['method'], "roots": eq['roots']} for eq in equations],
      "imaginary_equation": imaginary_equation,
      "imaginary_roots": imaginary_roots
    } 
