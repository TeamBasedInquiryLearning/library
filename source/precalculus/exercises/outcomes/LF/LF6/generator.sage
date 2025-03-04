class Generator(BaseGenerator):
  def data(self):
    
    x=var('x')
    y=var('y')
    coefficient_range = 8
    denom1 = choice([1..3])
    denom2 = choice([1..3])
    solution = (choice([-8..8])/denom1,choice([-8..8])/denom2)
    lhs1= choice([-1*coefficient_range..-1,1..coefficient_range])*x+choice([-1*coefficient_range..-1,1..coefficient_range])*y
    line1 = lhs1 == lhs1.subs({x:solution[0],y:solution[1]})
    line1 = line1*line1.rhs().denominator()
    lhs2= choice([-1*coefficient_range..-1,1..coefficient_range])*x+choice([-1*coefficient_range..-1,1..coefficient_range])*y
    if lhs2.coefficients(y)[1][0]/lhs2.coefficients(x)[1][0] == lhs1.coefficients(y)[1][0]/lhs1.coefficients(x)[1][0]:
      lhs2 += choice([-3..-1,1..3])*y

    line2 = lhs2 == lhs2.subs({x:solution[0],y:solution[1]})
    line2 = line2*line2.rhs().denominator()

    return {
      "system": f"\\begin{{cases}} {latex(line1.lhs())}={latex(line1.rhs())} \\\\{latex(line2.lhs())}={latex(line2.rhs())} \\end{{cases}}",
      "solution": solution,
    } 