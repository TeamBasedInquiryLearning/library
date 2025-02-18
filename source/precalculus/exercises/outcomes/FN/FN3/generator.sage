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
      line_length=3
      graph["y_intercept"] = (0,choice([3..10]))
      graph["endpoints"]=[(-2*a-2*b-line_length,0), (2*c+line_length,math.ceil(graph["y_intercept"][1])+line_length)]
      graph["domain"] = [graph["endpoints"][0][0]-b, graph["endpoints"][1][0]]
      graph["domain_left_included"]=choice([True,False])
      graph["domain_right_included"]=choice([True,False])
      graph["x_intercept"] = [(-2*a-2*b-line_length,0),(-2*a-line_length,0)]
      graph["extrema"] = {"points":[(-2*a-b-line_length,choice([-8..-3])),
                                    (-1*a,choice([(graph["y_intercept"][1]+1)..13])),
                                    (c,choice([1..(graph["y_intercept"][1]-1)]))],
                          "type": ["min","max","min"]}

      graph["decreasing"] = [ [graph["domain"][0],graph["extrema"]["points"][0][0]],
                              [graph["extrema"]["points"][1][0], graph["extrema"]["points"][2][0]]
                            ]
      graph["increasing"] = [ [graph["extrema"]["points"][0][0], graph["extrema"]["points"][1][0]],
                              [graph["extrema"]["points"][2][0], graph["domain"][1]]
                            ]

      #Flip vertically sometimes
      flip_vertically = choice([True,False])
      if flip_vertically:
        graph["y_intercept"]=(graph["y_intercept"][0],-1*graph["y_intercept"][1])
        graph["endpoints"][1] = (graph["endpoints"][1][0], -1*graph["endpoints"][1][1])
        for i in range(0,3):
          graph["extrema"]["points"][i]=(graph["extrema"]["points"][i][0], -1*graph["extrema"]["points"][i][1])
        graph["extrema"]["type"]=["max","min","max"] 
        graph["increasing"],graph["decreasing"]=graph["decreasing"],graph["increasing"]


      graph["cut_points"] = [graph["x_intercept"][1], (-2*a,graph["y_intercept"][1]), 
                             graph["y_intercept"], (2*c,graph["y_intercept"][1])] 

      graph["pieces"] = [R.lagrange_polynomial([graph["endpoints"][0],graph["extrema"]["points"][0],graph["cut_points"][0]]),
                        R.lagrange_polynomial([graph["cut_points"][0], graph["cut_points"][1]]),
                        R.lagrange_polynomial([graph["cut_points"][1],graph["extrema"]["points"][1],graph["cut_points"][2]]),
                        R.lagrange_polynomial([graph["cut_points"][2],graph["extrema"]["points"][2],graph["cut_points"][3]]),
                        R.lagrange_polynomial([graph["cut_points"][3], graph["endpoints"][1]])
                        ]



      #extreme_point_possibilities = [ graph["pieces"][0].subs({x:graph["domain"][0]}), graph["pieces"][4].subs({x:graph["domain"][1]})] + [ p[1] for p in graph["extrema"]["points"] ]

      #graph["range"] = [ min(extreme_point_possibilities), max(extreme_point_possibilities)]

      domain_string = ('[' if graph["domain_left_included"] else '(') + \
                      ",".join(str(i) for i in graph["domain"]) +  \
                      (']' if graph["domain_right_included"] else ')')  
      graph["features"] =  [
        {"feature": "has domain", "result": domain_string},
        {"feature": "has a y-intercept at", "result": graph["y_intercept"]},
        {"feature": "has a x-intercepts at", "result": graph["x_intercept"]}
        ] + [
          {"feature": f'has a local {graph["extrema"]["type"][i]} at ', "result":graph["extrema"]["points"][i]} for i in range(0,3)
        ] 

    #Increasing/decreasing intervals.  For Task 1, alternate which is supplied
    if choice(["increasing","decreasing"])== "increasing":
      graphs[0]["features"].append(
      {"feature": "is increasing on ", "result": "\\cup".join( [f'({",".join(str(i) for i in interval)})' for interval in graphs[0]["increasing"]]) }
                      ) 
    else:
      graphs[0]["features"].append(
      {"feature": "is decreasing on ", "result": "\\cup".join( [f'({",".join(str(i) for i in interval)})' for interval in graphs[0]["decreasing"]]) }
                      ) 
    graphs[1]["features"].append(
      {"feature": "is increasing on ", "result": "\\cup".join( [f'({",".join(str(i) for i in interval)})' for interval in graphs[1]["increasing"]]) }
                    ) 
    graphs[1]["features"].append(
      {"feature": "is decreasing on ", "result": "\\cup".join( [f'({",".join(str(i) for i in interval)})' for interval in graphs[1]["decreasing"]]) }
                      ) 

    #Determine global max/min and range for Task 2
    extrema_possibilities = [p[1] for p in graphs[1]["extrema"]["points"]]
    interior_max = max(extrema_possibilities)
    interior_min = min(extrema_possibilities)
    left_endpoint = (graphs[1]["domain"][0], graphs[1]["pieces"][0].subs(graphs[1]["domain"][0]))
    right_endpoint = (graphs[1]["domain"][1], graphs[1]["pieces"][-1].subs(graphs[1]["domain"][1]))
    range_string=""
    #Min and left endpoint
    if min(left_endpoint[1],right_endpoint[1]) < interior_min:
      if left_endpoint[1] < right_endpoint[1]:
        if graphs[1]["domain_left_included"]:
          global_min=left_endpoint[1]
          range_string+=f"[{global_min},"
        else:
          global_min=None
          range_string+=f"({left_endpoint[1]},"
      elif left_endpoint[1] == right_endpoint[1]:
        if graphs[1]["domain_left_included"] or graphs[1]["domain_right_included"]:
          global_min=left_endpoint[1]
          range_string+=f"[{global_min},"
        else:
          global_min=None
          range_string+=f"({left_endpoint[1]},"
      elif right_endpoint[1] < left_endpoint[1]:
        if graphs[1]["domain_right_included"]:
          global_min=right_endpoint[1]
          range_string+=f"[{global_min},"
        else:
          global_min=None
          range_string+=f"({right_endpoint[1]},"
    else:
      global_min = interior_min
      range_string+=f"[{global_min},"

    #Max and right endpoint
    if max(left_endpoint[1],right_endpoint[1]) > interior_max:
      if left_endpoint[1] > right_endpoint[1]:
        if graphs[1]["domain_left_included"]:
          global_max=left_endpoint[1]
          range_string+=f"{global_max}]"
        else:
          global_max=None
          range_string+=f"{left_endpoint[1]})"
      elif left_endpoint[1] == right_endpoint[1]:
        if graphs[1]["domain_left_included"] or graphs[1]["domain_right_included"]:
          global_max=left_endpoint[1]
          range_string+=f"{global_max}]"
        else:
          global_max=None
          range_string+=f"{left_endpoint[1]})"
      elif right_endpoint[1] > left_endpoint[1]:
        if graphs[1]["domain_right_included"]:
          global_max=right_endpoint[1]
          range_string+=f"{global_max}]"
        else:
          global_max=None
          range_string+=f"{right_endpoint[1]})"
    else:
      global_max = interior_max
      range_string+=f"{global_max}]"
    

    graphs[1]["features"].insert(1,{"feature": "has range", "result": range_string})
    if global_max:
      graphs[1]["features"].insert(7,{"feature": "has a global maximum of ", "result": global_max})
    else:
      graphs[1]["features"].insert(7,{"feature": "has no global maximum", "result": ""})
    if global_min:
      graphs[1]["features"].insert(8,{"feature": "has a global minimum of ", "result": global_min})
    else:
      graphs[1]["features"].insert(8,{"feature": "has no global minimum", "result": ""})
      
    return {
        "features1": graphs[0]["features"],
        "features2": graphs[1]["features"],
        "graphs": graphs
    }

  @provide_data
  def graphics(data):
  # updated by clontz
      plots=[]
      for i in [0,1]:
        plots.append( plot(data["graphs"][i]["pieces"][0],xmin=data["graphs"][i]["domain"][0],xmax=data["graphs"][i]["cut_points"][0][0],thickness=3) +
                      plot(data["graphs"][i]["pieces"][1],xmin=data["graphs"][i]["cut_points"][0][0],xmax=data["graphs"][i]["cut_points"][1][0],thickness=3) +
                      plot(data["graphs"][i]["pieces"][2],xmin=data["graphs"][i]["cut_points"][1][0],xmax=data["graphs"][i]["cut_points"][2][0],thickness=3) +
                      plot(data["graphs"][i]["pieces"][3],xmin=data["graphs"][i]["cut_points"][2][0],xmax=data["graphs"][i]["cut_points"][3][0],thickness=3) +
                      plot(data["graphs"][i]["pieces"][4],xmin=data["graphs"][i]["cut_points"][3][0],xmax=data["graphs"][i]["domain"][1],thickness=3,gridlines="minor")
                    )
        #Left endpoint
        if data["graphs"][i]["domain_left_included"]:
          plots[i]+= point( (data["graphs"][i]["domain"][0],data["graphs"][i]["pieces"][0].subs(data["graphs"][i]["domain"][0])), 
                           color='blue',size=75)
        else:
          plots[i] +=point( (data["graphs"][i]["domain"][0],data["graphs"][i]["pieces"][0].subs(data["graphs"][i]["domain"][0])), 
                           pointsize=75,markeredgecolor='blue',color='white',zorder=5)

        #Right endpoint
        if data["graphs"][i]["domain_right_included"]:
          plots[i]+= point( (data["graphs"][i]["domain"][1],data["graphs"][i]["pieces"][-1].subs(data["graphs"][i]["domain"][1])), 
                           color='blue',size=75)
        else:
          plots[i]+= point( (data["graphs"][i]["domain"][1],data["graphs"][i]["pieces"][-1].subs(data["graphs"][i]["domain"][1])), 
                           pointsize=75,markeredgecolor='blue',color='white',zorder=5)


      return {
          
          "graph1": plots[0],
          "graph2": plots[1]
          }
