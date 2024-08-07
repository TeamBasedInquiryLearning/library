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
      r1,r2,c = sample([-5..-1,1..5],3)
      b=1
      e=choice([-6..-1,1..6])
      #c=choice([-6..6])
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
    ineq=choice(["<","<=",">",">="])

    numberline=[]
    checkpoints = [partition_points[0]-1/2]
    checkpoints.extend([ p+1/2 for p in partition_points])

    intervals= []
    s=""
    #for p in checkpoints:
    for i in range(0,len(checkpoints)):
      p=checkpoints[i]
      s=""
      if TBILPrecal.check(LHS.subs({x:p}), ineq, RHS.subs({x:p})):
        if p<partition_points[0]:
          if partition_points[0] not in undefined_points and \
            TBILPrecal.check(LHS.subs({x:partition_points[0]}), ineq, RHS.subs({x:partition_points[0]})):
            intervals.append(f"(-\\infty, {partition_points[0]}]")
          else:
            intervals.append(f"(-\\infty, {partition_points[0]})")
        elif p>partition_points[-1]:
          if partition_points[-1] not in undefined_points and \
            TBILPrecal.check(LHS.subs({x:partition_points[-1]}), ineq, RHS.subs({x:partition_points[-1]})):
            intervals.append(f"[{partition_points[-1]}, \\infty)")
          else:
            intervals.append(f"({partition_points[-1]}, \\infty)")
        else:
          s=""
          if partition_points[i] not in undefined_points and \
              TBILPrecal.check(LHS.subs({x:partition_points[i]}), ineq, RHS.subs({x:partition_points[i]})):
            s+="["
          else:
            s+="("
          s+=f"{partition_points[i-1]}, {partition_points[i]}"
          if partition_points[i] not in undefined_points and \
              TBILPrecal.check(LHS.subs({x:partition_points[i]}), ineq, RHS.subs({x:partition_points[i]})):
            s+="]"
          else:
            s+=")"

      if s != "":
        intervals.append(s)

    
    return {
      "eq": f"{latex(LHS)} {(ineq)} {latex(RHS)}",
      "interval_string": "\\cup".join(intervals),
      "intervals": intervals,
    } 
  
  @provide_data
  def graphics(data):
      P=TBILPrecal.numberline_from_intervals(data["intervals"])      
      P.axes(False)
      return {
          "plot": plot(P)
      }