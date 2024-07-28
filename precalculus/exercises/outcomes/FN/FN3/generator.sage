class Generator(BaseGenerator):
    def data(self):

      #Adapted from https://github.com/matthematician/collegealgebra/blob/main/outcomes/FN5/generator.sage -- Thanks Matt!
      ## Pick 3 points: an x-intercept, a y-intercept, and an extremum. No repeated x values
      P = [[0,0],[0,0],[0,0]]
      while(len(set([P[0][0],P[1][0],P[2][0]])) < 3 or abs(P[2][1]-P[0][1])<2):
          P = [[0,randint(-8,8)], [randint(2,8)*choice([-1,1]),0], [randint(-2,8)*choice([-1,1]),randint(-12,12)]]
      
      R.<x> = PolynomialRing(QQ)
      PP = [P[0],P[1],[P[2][0]+0.2,P[2][1]],[P[2][0]-0.2,P[2][1]]]
      expr = R.lagrange_polynomial(PP)
      
      D = [ min(P[r][0] for r in range(3)), max(P[r][0] for r in range(3)) ]
      
      domain = [D[0]-choice([1,2,3,4]), D[1]+choice([1,2,3,4])]
      
      lc = expr.derivative(x,3)/6
      
      extreme = "minimum" if expr.derivative(x,2).subs({x:P[2][0]})>0 else "maximum"
      
      if(lc > 0):
        direction = "increasing"
        direc = [domain[0],P[2][0]] if extreme == "maximum" else [P[2][0],domain[1]]
      else:
        direction = "decreasing"
        direc = [domain[0],P[2][0]] if extreme == "minimum" else [P[2][0],domain[1]]
      
      feat = [
          {"feature": "has a y-intercept at", "result": vector(P[0])},
          {"feature": "has an x-intercept at", "result": vector(P[1])},
          {"feature": "has a local "+extreme+" at", "result": vector(P[2])},
          {"feature": "has domain", "result": str(domain[0])+r"\leq x \leq"+str(domain[1])},
          {"feature": "is "+direction+" for", "result": str(direc[0])+r"< x <"+str(direc[1])}
      ]
        
        
      return {
          "expr": expr,
          "domain": domain,
          "points": [tuple(P[i]) for i in range(3)],
          "features": feat
      }

    @provide_data
    def graphics(data):
    # updated by clontz
        return {
            "graph": plot(data['expr'],xmin=data['domain'][0],xmax=data['domain'][1])+point(data['points'],size=48,color='black',xmin=data['domain'][0]-3,xmax=data['domain'][1]+3)
            }

