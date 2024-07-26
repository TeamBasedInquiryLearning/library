class Generator(BaseGenerator):
    
    def data(self):
            
        small_rationals = {m/n:n for m in [-8..8]  for n in [2,3,5] if m%n!=0}
        small_irrationals = { ((a+sqrt(b))/c,(a-sqrt(b))/c):c for a in [-5..5] for b in [2,3,5,6,7,8] for c in [-5..-1,1..5]}
        roots=[]
        f(x)=1
        for i in [0..choice([0,1])]:
            root=choice([-5..5])
            roots.append(root)
            f(x)=f(x)*(x-root)
        r=choice(list(small_rationals.keys()))
        roots.append(r)
        f(x)=f(x)*expand(small_rationals[r]*(x-r))
        s=choice(list(small_irrationals.keys()))
        roots.extend(list(s))
        f(x)=f(x)*expand(small_irrationals[s]*(x-s[0]))*expand(small_irrationals[s]*(x-s[1]))
        roots.sort()

        small_complex = [(a+b*I,a-b*I) for a in [-5..5] for b in [-5..-1,1..5]]
        roots2=[]
        g(x)=1
        for i in [0..choice([0,1])]:
            root=choice([-5..5])
            roots2.append(root)
            g(x)=g(x)*(x-root)
        r=choice(list(small_rationals.keys()))
        roots2.append(r)
        g(x)=g(x)*expand(small_rationals[r]*(x-r))
        s=choice(small_complex)
        roots2.extend(list(s))
        g(x)=g(x)*(x-s[0])*(x-s[1])
        roots2.sort()

        fnames=sample(["f","g","h"],2)
        tasks = [ {"f": expand(f(x)), "f_factored": f(x), "roots":",".join([latex(r) for r in roots]),"fname":fnames[0]},
                {"f": expand(g(x)), "f_factored": g(x), "roots":",".join([latex(r) for r in roots2]),"fname":fnames[1]}
                ]
        shuffle(tasks)

        
        return {
            "tasks":tasks,
            "name": choice(["zeros","roots"]),
        }

        
        
        
        
