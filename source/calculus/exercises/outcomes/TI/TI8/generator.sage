class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        tasks = []

        # randomize appropriate powers
        pg1s = [4/3, 5/3, 6/5, 7/5, 8/5, 9/5]
        shuffle(pg1s)
        pl1s = [1/3, 2/3, 1/5, 2/5, 3/5, 4/5]
        shuffle(pl1s)
        x_0s = list(range(1,10))
        shuffle(x_0s)

        # improper, infinite bounds
        # convergent
        task = {}
        k = SR(choice([-1,1])*randrange(1,8)/randrange(1,8))
        p = pg1s[0]
        x_0 = choice([-1,1])*x_0s[0]
        task["integrand"] = k/(x-x_0)^p
        if choice([True,False]):
            task["bottom"] = x_0 + randrange(1,8)
            task["top"] = oo
            task["value"] = -k/(1-p)*(task["bottom"]-x_0)^(1-p)
        else:
            task["top"] = x_0 - randrange(1,8)
            task["bottom"] = -oo
            task["value"] = -k/(1-p)*(x_0-task["top"])^(1-p)
        task["approx"] = round(task["value"], ndigits=5)
        tasks.append(task)
        # divergent
        task = {}
        k = SR(choice([-1,1])*randrange(1,8)/randrange(1,8))
        p = pl1s[0]
        x_0 = choice([-1,1])*x_0s[1]
        if choice([True,False]):
            task["integrand"] = k/(x-x_0)^p
            task["bottom"] = x_0 + randrange(1,8)
            task["top"] = oo
            if k < 0:
                task["value"] = -oo
            else:
                task["value"] = oo
        else:
            task["integrand"] = k/(x-x_0)^p
            task["top"] = x_0 - randrange(1,8)
            task["bottom"] = -oo
            if k*(-1)^(1-p) < 0:
                task["value"] = -oo
            else:
                task["value"] = oo
        tasks.append(task)

        # improper, finite bounds
        # convergent
        task = {}
        k = SR(choice([-1,1])*randrange(1,8)/randrange(1,8))
        p = pl1s[1]
        x_0 = choice([-1,1])*x_0s[2]
        task["integrand"] = k/(x-x_0)^p
        if choice([True,False]):
            task["bottom"] = x_0
            task["top"] = x_0 + randrange(1,8)
            task["value"] = k/(1-p)*(task["top"]-x_0)^(1-p)
        else:
            task["top"] = x_0
            task["bottom"] = x_0 - randrange(1,8)
            task["value"] = k/(1-p)*(x_0-task["bottom"])^(1-p)
        task["approx"] = round(task["value"], ndigits=5)
        tasks.append(task)
        # divergent
        task = {}
        k = SR(choice([-1,1])*randrange(1,8)/randrange(1,8))
        p = pg1s[0]
        x_0 = choice([-1,1])*x_0s[3]
        task["integrand"] = k/(x-x_0)^p
        if choice([True,False]):
            task["top"] = x_0
            task["bottom"] = x_0 - randrange(1,8)
            if k < 0:
                task["value"] = -oo
            else:
                task["value"] = oo
        else:
            task["bottom"] = x_0
            task["top"] = x_0 + randrange(1,8)
            if k < 0:
                task["value"] = -oo
            else:
                task["value"] = oo
        tasks.append(task)

        # proper
        task = {}
        k = SR(choice([-1,1])*randrange(1,8)/randrange(1,8))
        p = choice([pl1s[2],pg1s[2]])
        x_0 = choice([-1,1])*x_0s[4]
        task["integrand"] = k/(x-x_0)^p
        task["bottom"] = x_0 - randrange(1,5)
        task["top"] = x_0 + randrange(1,5)
        task["proper"] = True
        tasks.append(task)

        shuffle(tasks)

        return {"tasks": tasks}