load("../sage/common.sage")

class Generator(BaseGenerator):
  def data(self):

    partition_points=[]
    equation_type=choice(["linear", "quadratic"])

    if equation_type=="linear":
      #Ensure a=d

      a=choice([0..6])
      d=a
      c=choice([-6..-1,1..6])
      e=choice([-6..-1,1..6])
      f=choice([-6..-1,1..6])
      b=(f-1)*a*(f-c)+e*(c-f+1)
      partition_points = [1-f]

    else:
      #Quadratic
      r1,r2 = sample([-5..-1,1..5],2)
      b=1
      e=choice([-6..6])
      c=choice([-6..6])
      f=r1*r2+e*c
      a=(-r1-r2+e-c-b)/(f-c)
      d=a-1
      partition_points = [r1,r2]

    partition_points.extend([-c,-f])
    partition_points.sort()

    LHS = (expand((a*x+b)*a.denominator()))/(x+c)
    RHS = (expand((d*x+e)*a.denominator()))/(x+f)
    ineq=choice(["<","<=",">",">="])

    numberline=[]
    checkpoints = [partition_points[0]-1/2]
    checkpoints.extend([ p+1/2 for p in partition_points])

    for p in checkpoints:
      if TBILPrecal.check(LHS.subs({x:p}), ineq, RHS.subs({x:p})):
        numberline.append("+")
      else:
        numberline.append("-")

    intervals= []

    return {
      #"eq": f"\dfrac{{{latex(a*x+b)}}}{{{latex(x+c)}}} {ineq} \dfrac{{{latex(d*x+e)}}}{{{latex(x+f)}}}",
      "eq": f"{latex(LHS)} {(ineq)} {latex(RHS)}",
      "cut": partition_points,
      "numberline":numberline
    } 