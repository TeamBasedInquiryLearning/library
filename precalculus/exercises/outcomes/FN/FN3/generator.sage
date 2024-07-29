import numpy as np
class Generator(BaseGenerator):
  def data(self):
    #Adapted from https://github.com/matthematician/collegealgebra/blob/main/outcomes/FN5/generator.sage -- Thanks Matt!
    R.<x> = PolynomialRing(QQ)
    graphs=[{},{}]
    for graph in graphs:
      a=choice([1,2,3])
      b=choice([2,3])
      c=choice([2..6])
      graph["y_intercept"] = (0,choice([3..10]))
      graph["endpoints"]=[(-2*a-2*b,0), (2*c,graph["y_intercept"][1])]
      graph["x_intercept"] = [(-2*a-2*b,0),(-2*a,0)]
      graph["extrema"] = {"points":[(-2*a-b,choice([-8..-3])),
                                    (-1*a,choice([(graph["y_intercept"][1]+1)..13])),
                                    (c,choice([1..(graph["y_intercept"][1]-1)]))],
                          "type": ["min","max","min"]}
      graph["pieces"] = [R.lagrange_polynomial([graph["endpoints"][0],graph["extrema"]["points"][0],graph["x_intercept"][1]]),
                        #Next one not centered like it should be!  Need to move above over one and draw line to (-2a, yintercept)
                        R.lagrange_polynomial([graph["x_intercept"][1],graph["extrema"]["points"][1],graph["y_intercept"]]),
                        R.lagrange_polynomial([graph["y_intercept"],graph["extrema"]["points"][2],graph["endpoints"][1]])
                        ]

      graph["domain"] = [graph["endpoints"][0][0]-choice([1..3]), graph["endpoints"][1][0]+choice([1..3])]
      graph["decreasing"] = [ [graph["domain"][0],graph["extrema"]["points"][0][0]],
                              [graph["extrema"]["points"][1][0], graph["extrema"]["points"][2][0]]
                            ]
      graph["increasing"] = [ [graph["extrema"]["points"][0][0], graph["extrema"]["points"][1][0]],
                              [graph["extrema"]["points"][2][0], graph["domain"][1]]
                            ]
      graph["plot_pieces"] = [plot(graph["pieces"][0],xmin=graph["domain"][0],xmax=graph["x_intercept"][1][0],thickness=3),
                              plot(graph["pieces"][1],xmin=graph["x_intercept"][1][0],xmax=0,thickness=3),
                              plot(graph["pieces"][2],xmin=0,xmax=graph["domain"][1],thickness=3),
                            ]

      extreme_point_possibilities = [ graph["pieces"][0].subs({x:graph["domain"][0]}), graph["pieces"][2].subs({x:graph["domain"][1]})] + [ p[1] for p in graph["extrema"]["points"] ]
      graph["range"] = [ min(extreme_point_possibilities), max(extreme_point_possibilities)]

      graph["features"] =  [
        {"feature": "has domain", "result": f'[{",".join(str(i) for i in graph["domain"])}]'},
        {"feature": "has a y-intercept at", "result": graph["y_intercept"]},
        {"feature": "has an x-intercepts at", "result": graph["x_intercept"]},
        {"feature": f'''has a local {graph["extrema"]["type"][0]} at <m>{graph["extrema"]["points"][0]}</m>, 
                            a local {graph["extrema"]["type"][1]} at <m>{graph["extrema"]["points"][1]}</m>,
                        and a local {graph["extrema"]["type"][2]} at <m>{graph["extrema"]["points"][2]}</m>'''}, 
        #{"feature": "has a local "+extreme+" at", "result": vector(P[2])},
        #{"feature": "has domain", "result": str(domain[0])+r"\leq x \leq"+str(domain[1])},
        {"feature": "is increasing on ", "result": "\cup".join( [f'({",".join(str(i) for i in interval)})' for interval in graph["increasing"]]) }
         ]

    graphs[1]["features"].insert(1,{"feature": "has range", "result": f'({",".join(str(d) for d in graphs[1]["range"])})'})
      
    return {
#        "expr": expr,
#        "domain": domain,
#        "points": [tuple(P[i]) for i in range(3)],
        "features1": graphs[0]["features"],
        "features2": graphs[1]["features"],
        "graphs": graphs
    }

  @provide_data
  def graphics(data):
  # updated by clontz
      return {
          "graph1": plot(sum(data["graphs"][0]["plot_pieces"])),
          "graph2": plot(sum(data["graphs"][1]["plot_pieces"])),
          #"graph2": plot(sum(graphs[1]["plot_pieces"])),
          }

