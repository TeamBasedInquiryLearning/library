from sage.functions.log import logb
class Generator(BaseGenerator):
  def data(self):
    #Get 4 different variables, two for first sub task, two for second
    vars = sample([var(a) for a in ['a','b','c','d','m','n','p','q','x','y','z']],4)
    exp_vars = vars[:2]
    log_vars = vars[2:]

    exp_vars.append(choice([2..10]))
    shuffle(exp_vars)
    exp_equation = pow(exp_vars[0],exp_vars[1])== exp_vars[2]

    log_vars.append(choice([2..10]))
    shuffle(log_vars)
    log_equation = pow(log_vars[0],log_vars[1])== log_vars[2]

    b=choice([2..10])
    d=choice([-1,1])*choice([1/2,2,3,4])
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