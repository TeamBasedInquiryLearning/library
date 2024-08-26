from sage.functions.log import logb
class Generator(BaseGenerator):
  def data(self):
    #Get 4 different variables, two for first sub task, two for second
    vars = sample([var(a) for a in ['a','b','c','d','m','n','p','q','x','y','z']],4)
    exp_vars = vars[:2]
    log_vars = vars[2:]

    sage_ints = sample([ZZ(n) for n in range(4,11)],3)

    exp_vars.append(sage_ints[0])
    shuffle(exp_vars)
    exp_equation = pow(exp_vars[0],exp_vars[1]) == exp_vars[2]

    log_vars.append(sage_ints[1])
    shuffle(log_vars)
    log_equation = pow(log_vars[0],log_vars[1]) == log_vars[2]

    b=sage_ints[2]
    d=choice([-1,1])*choice([1/2,2,3])
    logarithm = f"\\log _{{ {b} }} \\left({latex(simplify(pow(b,d)))} \\right)"
    logarithm_evaluated = d
    

    return {
      "exponential_equation": exp_equation,
      "exponential_equation_in_logarithmic": f"\\log _{{ {exp_vars[0]} }} {exp_vars[2]} = {exp_vars[1]}",
      "logarithmic_equation": f"\\log _{{ {log_vars[0]} }} {log_vars[2]} = {log_vars[1]}",
      "logarithmic_equation_in_exponential": log_equation,
      "logarithm": logarithm,
      "evaluated_logarithm": logarithm_evaluated
    } 