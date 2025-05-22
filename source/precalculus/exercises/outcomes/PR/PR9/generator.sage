import operator
load("../../../source/common/sagemath/library.sage")

class Generator(BaseGenerator):
  def data(self):

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

    rational_intervals=TBIL.intervals_from_inequality(rational_inequality,partition_points,undefined_points)
    
    return {
      "rational_ineq": rational_inequality,
      "rational_interval_string": "\\cup".join(rational_intervals),
      "rational_intervals": rational_intervals,
    } 
  
  @provide_data
  def graphics(data):
      P=TBIL.numberline_from_intervals(data["rational_intervals"])      
      P.axes(False)
      return {
          "rational_plot": plot(P),
      }