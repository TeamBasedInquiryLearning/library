class Generator(BaseGenerator):
    def data(self):
        x = var("x")
        y = var("y")
        f="f"
        g="g"
        h="h"

        # Function Names
        functionnames=[f,g,h]
        fn = choice(functionnames)

        # Determine Domain [a,b]
        a = randrange(-11,3)
        b = a + randrange(8,11)
        interiors = list(range(a+1,b))
        shuffle(interiors)
        # Determine Range
        outputs = list(range(-4,5))
        shuffle(outputs)

        # Choose if the infinite limit is the left- or right-hand limit or both.
        vert = ["leftinf","rightinf","bothinf","vertleft","vertright"]

        # Choose the description for a removable discontinuity.
        remove = ["limneqval","specfuncval"]

        # Choose the description for a jump discontinuity (some of these could be vertical asymptotes, as well).
        jump = ["leftneqright","jumpspecleft","jumpspecright","jumpspecleftright"]

        # Choose property from each category and pair them with x-values.
        props = [choice(vert),choice(remove),choice(jump)]
        #shuffle(props)

        properties = [
            {props[0]: True,"x":interiors[0],"y1":outputs[0],"y2":outputs[1]},
            {props[1]: True,"x":interiors[1],"y1":outputs[2],"y2":outputs[3]},
            {props[2]: True,"x":interiors[2],"y1":outputs[4],"y2":outputs[5]},
        ]

        return {
            "fn": fn,
            "a": a,
            "b": b,
            "properties": properties,
        }
