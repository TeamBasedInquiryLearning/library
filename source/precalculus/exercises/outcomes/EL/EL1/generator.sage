class Generator(BaseGenerator):
  def data(self):
    exp_table = choice(["left", "right"])
    exp_func = choice([-3,-2,-1,1,2,3]) * choice(range(2,6)) ^ (choice([-1,1])*x)
    nonexp_func = choice([
        choice([-4,-3,-2,-1,1,2,3,4])*x+choice([1,2,3,4,5]),
        choice([-1,1])*x^2+choice(range(-3,4))*x+choice(range(-4,5)), 
        choice([1,2,3])/(x+choice([1,2,3,4])), 
    ])


    fname1,fname2 = sample(["f","g","h","p","q"],2)
    function1 = choice([-4,-3,-2,-1,1,2,3,4])*choice([b for a in [2..5] for b in (a,1/a)])^x 
    val1=choice([-4..-2,2..4])
    shift = choice([-3,-2,-1,1,2,3])*x+choice([-3,-2,-1,1,2,3])
    function2 = choice([2,3,4])^(shift)
    val2= solve(shift==choice([-4,-3,-2,2,3,4]),x)[0].rhs()

    exponential_function = choice([-4,-3,-2,2,3,4])*choice([b for a in [2,3,4,5] for b in (a,1/a)])^x 
    points=[(0,exponential_function.subs({x:0}))]
    a=choice([-4,-3,-2,-1,2,3,4,5])
    points.append((a,exponential_function.subs({x:a})))
    shuffle(points)

    return {
      exp_table: True,
      "exp_table_rows": [{"x": a, "y": exp_func.subs({x:a})} for a in [1,2,3,4,5]],
      "nonexp_table_rows": [{"x": a, "y": nonexp_func.subs({x:a})} for a in [1,2,3,4,5]],
      "fname1": fname1,
      "function1": function1,
      "val1": val1,
      "evaluate1": function1.subs({x:val1}),
      "fname2": fname2,
      "function2": function2,
      "val2": val2,
      "evaluate2": function2.subs({x:val2}),
      "point1": points[0],
      "point2": points[1],
      "exponential_function": exponential_function
    } 