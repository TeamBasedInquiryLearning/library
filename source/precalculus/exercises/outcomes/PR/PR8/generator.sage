import operator
load("../../../source/common/sagemath/library.sage")

class Generator(BaseGenerator):
  def data(self):

    #Task 1
    roots = [-6..6]
    roots.extend(TBIL.small_rationals(numerators=[-3..3],denominators=[2,3],dictionary=False,length=3))
    r1,r2=sample(roots,2)
    d1=r1.denominator()
    d2=r2.denominator()
    quadratic_inequality = CheckIt.shuffled_inequality(*[a*x^b for (a,b) in expand(d1*d2*(x-r1)*(x-r2)).coefficients()])
    partition_points=sorted([r1,r2])

    quadratic_intervals=TBIL.intervals_from_inequality(quadratic_inequality,partition_points)

    return {
      "quadratic_ineq": quadratic_inequality,
      "quadratic_intervals": quadratic_intervals,
      "quadratic_interval_string": "\\cup".join(quadratic_intervals),
    } 
  
  @provide_data
  def graphics(data):
      Q=TBIL.numberline_from_intervals(data["quadratic_intervals"])      
      Q.axes(False)
      return {
          "quadratic_plot": plot(Q)
      }