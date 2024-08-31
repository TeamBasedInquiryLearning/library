import operator
load("../sage/common.sage")

class Generator(BaseGenerator):
  def data(self):

    #Task 1
    roots = [-6..6]
    roots.extend(TBILPrecal.small_rationals(numerators=[-3..3],denominators=[2,3],dictionary=False,length=3))
    r1,r2=sample(roots,2)
    d1=r1.denominator()
    d2=r2.denominator()
    quadratic_inequality = CheckIt.shuffled_inequality(*[a*x^b for (a,b) in expand(d1*d2*(x-r1)*(x-r2)).coefficients()])
    partition_points=sorted([r1,r2])

    quadratic_intervals=TBILPrecal.intervals_from_inequality(quadratic_inequality,partition_points)

    #Task 2
    partition_points=[]
    equation_type=choice(["linear", "quadratic"])

    if equation_type=="linear":
      #Ensure a=d

      a=choice([0..6])
      d=a
      c=choice([-6..-1,1..6])
      e=choice([-6..-1,1..6])
      #If f=c, then necessarily b=e and we end up with LHS=RHS.  So let's avoid that
      f=choice([ i for i in [-6..-1,1..6] if i!=c])
      b=(f-1)*a*(f-c)+e*(c-f+1)
      partition_points = [1-f]

    else:
      #Quadratic
      e=choice([-6..-1,1..6])
      r1,r2 = sample([-5..-1,1..5],2)
      #Pre-empt f=c causing a divide by zero error below
      c= choice([a for a in [-5..-1,1..5] if a!=r1 and a!=r2 and (e==1 or a!= r1*r2/(1-e))])
      b=1
      f=r1*r2+e*c
      a=(-r1-r2+e-c-b)/(f-c)
      d=a-1
      partition_points = [r1,r2]

    undefined_points=[-c,-f]
    #Prevent duplicates
    partition_points.extend([x for x in undefined_points if x not in partition_points])
    partition_points.sort()

    LHS = (expand((a*x+b)*a.denominator())).mul(1/(x+c),hold=True)
    RHS = (expand((d*x+e)*a.denominator())).mul(1/(x+f),hold=True)

    op = choice([operator.lt, operator.le, operator.ge, operator.gt])
    rational_inequality = op(LHS,RHS)

    rational_intervals=TBILPrecal.intervals_from_inequality(rational_inequality,partition_points,undefined_points)
    
    return {
      "quadratic_ineq": quadratic_inequality,
      "quadratic_intervals": quadratic_intervals,
      "quadratic_interval_string": "\\cup".join(quadratic_intervals),
      "rational_ineq": rational_inequality,
      "rational_interval_string": "\\cup".join(rational_intervals),
      "rational_intervals": rational_intervals,
    } 
  
  @provide_data
  def graphics(data):
      P=TBILPrecal.numberline_from_intervals(data["rational_intervals"])      
      P.axes(False)
      Q=TBILPrecal.numberline_from_intervals(data["quadratic_intervals"])      
      Q.axes(False)
      return {
          "rational_plot": plot(P),
          "quadratic_plot": plot(Q)
      }