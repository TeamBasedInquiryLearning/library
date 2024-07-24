load("library/common.sage")

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
        eq_set = f"\\{{ {eq_center-eq_radius} , {eq_center+eq_radius} \\}}"

        ineq_center = choice([-1,1])*randrange(1,6)
        ineq_radius = randrange(1,6)
        ineq_scale = randrange(2,6)
        ineq_strict = choice([True,False])
        ineq_offset = choice([-1,1])*randrange(1, ineq_scale*ineq_radius)
        ineq_inside = choice([True,False])
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

        return {
            "eq": eq,
            "eq_set": eq_set,
            "ineq": ineq,
            "ineq_interval": ineq_interval,
            "ineq_inside": ineq_inside,
            "ineq_strict": ineq_strict,
            "ineq_center": ineq_center,
            "ineq_radius": ineq_radius,
        }

    @provide_data
    def graphics(data):
        P = TBILCalc.numberline_plot()
        if data["ineq_inside"]:
            P += TBILCalc.inequality_plot(
                start=data["ineq_center"]-data["ineq_radius"],
                strict_start=data["ineq_strict"],
                end=data["ineq_center"]+data["ineq_radius"],
                strict_end=data["ineq_strict"],
                label_endpoints=False,
            )
        else:
            P += TBILCalc.inequality_plot(
                end=data["ineq_center"]-data["ineq_radius"],
                strict_end=data["ineq_strict"],
                label_endpoints=False,
            )
            P += TBILCalc.inequality_plot(
                start=data["ineq_center"]+data["ineq_radius"],
                strict_start=data["ineq_strict"],
                label_endpoints=False,
            )
        P.axes(False)
        return {
            "ineq_plot": plot(P)
        }
