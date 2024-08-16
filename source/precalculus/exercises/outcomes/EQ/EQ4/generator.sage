load("../sage/common.sage")

class Generator(BaseGenerator):
    def data(self):
        eq_center = choice([-1,1])*randrange(1,6)
        eq_radius = randrange(1,6)
        eq_scale = randrange(2,6)
        eq_offset = choice([-1,1])*randrange(1, eq_scale*eq_radius)
        eq = CheckIt.shuffled_equation(
            eq_scale*abs(x-eq_center),
            - eq_scale*eq_radius
        ) + eq_offset
        eq_set = f"{eq_center-eq_radius} , {eq_center+eq_radius}"

        
        ineq_strict = choice([True,False])
        ineq_inside = choice([True,False])
        ineqs = []

        for _ in range(2):
            ineq_center = choice([-1,1])*randrange(1,6)
            ineq_radius = randrange(1,6)
            ineq_scale = randrange(2,6)
            ineq_strict = not ineq_strict
            ineq_inside = not ineq_inside
            ineq_offset = choice([-1,1])*randrange(1, ineq_scale*ineq_radius)

            if ineq_inside:
                ineq = CheckIt.shuffled_inequality(
                    - ineq_scale*abs(x-ineq_center),
                    ineq_scale*ineq_radius,
                    strict=ineq_strict
                ) + ineq_offset
                if ineq_strict:
                    ineq_interval = f"( {ineq_center-ineq_radius} , {ineq_center+ineq_radius} )"
                else:
                    ineq_interval = f"[ {ineq_center-ineq_radius} , {ineq_center+ineq_radius} ]"
            else:
                ineq = CheckIt.shuffled_inequality(
                    ineq_scale*abs(x-ineq_center),
                    - ineq_scale*ineq_radius,
                    strict=ineq_strict
                ) + ineq_offset
                if ineq_strict:
                    ineq_interval = f"( -\\infty, {ineq_center-ineq_radius} ) \\cup ( {ineq_center+ineq_radius}, \\infty )"
                else:
                    ineq_interval = f"( -\\infty, {ineq_center-ineq_radius} ] \\cup [ {ineq_center+ineq_radius}, \\infty )"
            ineqs.append({
                "ineq": ineq,
                "ineq_interval": ineq_interval,
                "ineq_inside": ineq_inside,
                "ineq_strict": ineq_strict,
                "ineq_center": ineq_center,
                "ineq_radius": ineq_radius,
            })

        return {
            "eq": eq,
            "eq_set": eq_set,
            "eq_center": eq_center,
            "eq_radius": eq_radius,
            "ineqs": ineqs
        }

    @provide_data
    def graphics(data):
        # Q = TBILPrecal.numberline_plot()
        # Q += circle((data["eq_center"]-data["eq_radius"],0),0.2,color="#0088ff",fill=True)
        # Q += circle((data["eq_center"]+data["eq_radius"],0),0.2,color="#0088ff",fill=True)
        # Q.axes(False)

        for datum in data["ineqs"]:
            if datum["ineq_inside"]:
                Pi = TBILPrecal.numberline_plot()
                Pi += TBILPrecal.inequality_plot(
                    start=datum["ineq_center"]-datum["ineq_radius"],
                    strict_start=datum["ineq_strict"],
                    end=datum["ineq_center"]+datum["ineq_radius"],
                    strict_end=datum["ineq_strict"],
                    label_endpoints=False,
                )
                Pi.axes(False)
            else:
                Po = TBILPrecal.numberline_plot()
                Po += TBILPrecal.inequality_plot(
                    end=datum["ineq_center"]-datum["ineq_radius"],
                    strict_end=datum["ineq_strict"],
                    label_endpoints=False,
                )
                Po += TBILPrecal.inequality_plot(
                    start=datum["ineq_center"]+datum["ineq_radius"],
                    strict_start=datum["ineq_strict"],
                    label_endpoints=False,
                )
                Po.axes(False)
        return {
            # "eq_plot": plot(Q),
            "ineq_inside_plot": plot(Pi),
            "ineq_outside_plot": plot(Po),
        }
