class Generator(BaseGenerator):
  def data(self):
    
    x=var('x')
    y=var('y')
    coefficient_range = 8
    solution = (choice([-8..8]),choice([-8..8]))
    lhs1= choice([-1*coefficient_range..-1,1..coefficient_range])*x+choice([-1*coefficient_range..-1,1..coefficient_range])*y
    line1 = lhs1 == lhs1.subs({x:solution[0],y:solution[1]})
    lhs2= choice([-1*coefficient_range..-1,1..coefficient_range])*x+choice([-1*coefficient_range..-1,1..coefficient_range])*y
    if lhs2.coefficients(y)[1][0]/lhs2.coefficients(x)[1][0] == lhs1.coefficients(y)[1][0]/lhs1.coefficients(x)[1][0]:
      lhs2 += choice([-3..-1,1..3])*y

    line2 = lhs2 == lhs2.subs({x:solution[0],y:solution[1]})

    return {
      "system": f"\\begin{{cases}} {latex(line1.lhs())}={latex(line1.rhs())} \\\\{latex(line2.lhs())}={latex(line2.rhs())} \\end{{cases}}",
      "solution": solution,
    } 