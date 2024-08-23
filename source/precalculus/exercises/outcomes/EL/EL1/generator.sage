class Generator(BaseGenerator):
  def data(self):

    table_function, table_is_exponential = choice([ ( choice([-3,-2,-1,1,2,3])*choice([2..5])^(choice([-1,1])*x) , True), 
                                                    (choice([choice([-4..-1,1..4])*x+choice([1..5]), 
                                                             choice([-1,1])*x^2+choice([-3..3])*x+choice([-4..4]), 
                                                             choice([1..3])/(x+choice([1..4])), 
                                                            ]) , False)])


    fname1,fname2 = sample(["f","g","h","p","q"],2)
    function1 = choice([-4..-1,1..4])*choice([b for a in [2..5] for b in (a,1/a)])^x 
    val1=choice([-4..-2,2..4])
    shift = choice([-3..-1,1..3])*x+choice([-3..-1,1..3])
    function2 = choice([2..4])^(shift)
    val2= solve(shift==choice([-4..-2,2..4]),x)[0].rhs()

    exponential_function = choice([-4..-2,2..4])*choice([b for a in [2..5] for b in (a,1/a)])^x 
    points=[(0,exponential_function.subs({x:0}))]
    a=choice([-4..-1,2..5])
    points.append((a,exponential_function.subs({x:a})))
    shuffle(points)

    return {
      "table_rows": [{"x": a, "y": table_function.subs({x:a})} for a in [1..5]],
      "does": "does" if table_is_exponential else "does not",
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