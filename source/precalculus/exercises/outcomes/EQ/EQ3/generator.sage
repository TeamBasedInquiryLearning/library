class Generator(BaseGenerator):
    def data(self):

      pointA = ( choice([-10..10]), choice([-10..10]))
      pointB = ( choice([-10..10]), choice([-10..10]))
      distance= sqrt((pointA[0]-pointB[0])^2+(pointA[1]-pointB[1])^2)
      midpoint= ( (pointA[0]+pointB[0])/2, (pointA[1]+pointB[1])/2)

      names = ["Jana", "Luna", "Alakai", "Maria", "Lujain", "Stepan", "Reethi", "Jun Young", "Fadi", 
               "Adriana", "Diego", "DeAngelo", "Andrés", "Angel",  ]
      places = ["the post office", "the library", "the grocery store", "the park", "the soccer field",
                "the coffee shop", "the hardware store", "the food truck"]
      placeA, placeB, placeC = sample( [ name+"'s house" for name in names]+places ,3)
      
      #Display approximation for non-integral distances
      if not distance in ZZ:
        distance = f"{latex(distance)}\\text{{ or }}{round(distance,1)}"

      return {
        "pointA": pointA,
        "pointB": pointB,
        "distance": distance,
        "midpoint": midpoint,
        "placeA": placeA,
        "placeB": placeB,
        "placeC": placeC,
      } 