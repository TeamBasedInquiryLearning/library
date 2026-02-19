#%%manim -ql LIPoly

from manim import *










class FindIndef(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the indefinite integral } \displaystyle \int \frac{\sqrt{\ln(x)+3}}{x} \,dx.", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        equ1 = MathTex(r"=", color=RED).scale(0.6).shift(RIGHT*4+UP*1)
        equ2 = MathTex(r"=", color=BLUE).scale(0.6).next_to(equ1, DOWN*2)

        lhs1 = MathTex(r"\displaystyle \int \frac{\sqrt{\ln(x)+3}}{x} \,dx").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \int ", r" { (", r"\ln(x) + 3", r")^{1/2} ", r" \over" ,r" x }", r"\,dx").scale(0.8).next_to(eq1, RIGHT)
        
        rhs2 = MathTex(r"\displaystyle \int ", r" { (", r"u", r")^{1/2} ", r" \over" ,r" x }", r"\,dx").scale(0.8).next_to(eq2, RIGHT)
        rhs2[5].set_color(BLUE)
        rhs2[6].set_color(BLUE)

        rhs2a = MathTex(r"\displaystyle \int ",    r"u", r"^{1/2} " , r" \,du").scale(0.8).next_to(eq2, RIGHT)
        rhs2a[1].set_color(RED)
        rhs2a[3].set_color(BLUE)

        lhsu1 = MathTex(r"u", color=RED).scale(0.6).next_to(equ1, LEFT)
        rhsu1 = MathTex(r"\ln(x)+3", color=RED).scale(0.6).next_to(equ1, RIGHT)

        lhsu2 = MathTex(r"du", color=BLUE).scale(0.6).next_to(equ2, LEFT)
        rhsu2 = MathTex(r"\frac{1}{x}dx", color=BLUE).scale(0.6).next_to(equ2, RIGHT)

        rhs3 = MathTex(r"\frac{1}{\frac{3}{2}}", r"u", r"^{3/2}+C").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(RED)
        rhs3a = MathTex(r"\frac{2}{3}", r"u", r"^{3/2}+C").scale(0.8).next_to(eq3, RIGHT)
        rhs3a[1].set_color(RED)

        rhs4 = MathTex(r"\frac{2}{3}", r"(\ln(x)+3)", r"^{3/2}+C.").scale(0.8).next_to(eq4, RIGHT)
        rhs4[1].set_color(RED)        
        
        


        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(rhs1), Write(eq1))
        self.wait(5)
        self.play(Wiggle(rhs1[2]))
        self.wait(2)
        self.play(Write(lhsu1))
        self.wait(2)
        self.play(Write(equ1), Write(rhsu1))
        self.wait(3)
        self.play(Write(lhsu2))
        self.wait(2)
        self.play(Write(equ2), Write(rhsu2))
        self.wait(5)
        self.play(Wiggle(rhs1[2]))
        self.play(rhs1[2].animate.set_color(RED))
        self.wait(3)
        self.play(Wiggle(rhs1[5]), Wiggle(rhs1[6]))
        self.play(rhs1[5].animate.set_color(BLUE), rhs1[6].animate.set_color(BLUE))
        self.wait(2)
        self.play(Write(rhs2), Write(eq2))
        self.wait(3)
        self.play(Wiggle(lhsu2), Wiggle(rhsu2))
        self.play(Transform(rhs2, rhs2a))
        self.wait(5)
        self.play(Write(rhs3), Write(eq3))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(2)
        self.play(Wiggle(lhsu1), Wiggle(rhsu1))
        self.play(Write(eq4), Write(rhs4))
        self.wait(3)
        self.play(rhs4[1].animate.set_color(WHITE))

        


        self.wait(10)


class FindDef(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the definite integral } \displaystyle \int_0^2 xe^{x^2-1} \,dx.", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        equ1 = MathTex(r"=", color=RED).scale(0.6).shift(RIGHT*4+UP*1)
        equ2 = MathTex(r"=", color=BLUE).scale(0.6).next_to(equ1, DOWN*2)

        lhs1 = MathTex(r"\displaystyle \int_{x=0}^{x=2} ", r" x ", r" e ", r" ^{x^2-1} ", r" \,dx").scale(0.8).next_to(eq1, LEFT)
        
        rhs1 = MathTex(r"\displaystyle \int_{x=0}^{x=2} ", r"e", r"^{u}",  r"x\,dx").scale(0.8).next_to(eq1, RIGHT)
        rhs1[2].set_color(RED)
        rhs1[3].set_color(BLUE)

        rhs1a = MathTex(r"\displaystyle \int_{x=0}^{x=2} ",    r"e", r"^{u} " , r"\frac{1}{2} \,du").scale(0.8).next_to(eq1, RIGHT)
        rhs1a[2].set_color(RED)
        rhs1a[3].set_color(BLUE)

        lhsu1 = MathTex(r"u", color=RED).scale(0.6).next_to(equ1, LEFT)
        rhsu1 = MathTex(r"x^2-1", color=RED).scale(0.6).next_to(equ1, RIGHT)

        lhsu2 = MathTex(r"du", color=BLUE).scale(0.6).next_to(equ2, LEFT)
        rhsu2 = MathTex(r"2xdx", color=BLUE).scale(0.6).next_to(equ2, RIGHT)

        lhsu2a = MathTex(r"\frac{1}{2}du", color=BLUE).scale(0.6).next_to(equ2, LEFT)
        rhsu2a = MathTex(r"xdx", color=BLUE).scale(0.6).next_to(equ2, RIGHT)

        rhs2 = MathTex(r"\frac{1}{2}e", r"^u", r" |", r"_{x=0}", r"^{x=2}").scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(RED)

        rhs2a = MathTex(r"\frac{1}{2}e", r"^u", r"|", r"_{u=-1}", r"^{u=3}").scale(0.8).next_to(eq2, RIGHT)
        rhs2a[1].set_color(RED)


        rhs3 = MathTex(r"\frac{1}{2} e", r"^{x^2-1}", r" |", r"_{x=0}", r"^{x=2}").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(RED)  

        rhs4 = MathTex(r"\frac{e^3}{2}-\frac{e^{-1}}{2} ").scale(0.8).next_to(eq4, RIGHT)
        rhs4a = MathTex(r"\frac{e^3}{2}-\frac{1}{2e} ").scale(0.8).next_to(eq4, RIGHT)
         

        
        


        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Wiggle(lhs1[3]))
        self.wait(2)
        self.play(Write(lhsu1))
        self.wait(2)
        self.play(Write(equ1), Write(rhsu1))
        self.wait(3)
        self.play(Write(lhsu2))
        self.wait(2)
        self.play(Write(equ2), Write(rhsu2))
        self.wait(5)
        self.play(Wiggle(lhs1[3]))
        self.play(lhs1[3].animate.set_color(RED))
        self.wait(3)
        self.play(Wiggle(lhs1[1]), Wiggle(lhs1[4]))
        self.play(lhs1[1].animate.set_color(BLUE), lhs1[4].animate.set_color(BLUE))
        self.wait(2)
        self.play(Transform(rhsu2, rhsu2a), Transform(lhsu2, lhsu2a))
        self.wait(3)
        self.play(Write(rhs1), Write(eq1))
        self.wait(3)
        self.play(Wiggle(lhsu2), Wiggle(rhsu2))
        self.play(Transform(rhs1, rhs1a))
        self.wait(5)
        self.play(Write(rhs2), Write(eq2))
        self.wait(3)
        self.play(Wiggle(lhsu1), Wiggle(rhsu1))
        self.play(Transform(rhs2, rhs2a))
        self.wait(5)
        self.play(Write(rhs4), Write(eq4))
        self.wait(5)
        self.play(FadeOut(eq4, rhs4))
        self.play(Wiggle(lhsu1), Wiggle(rhsu1))
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(rhs4), Write(eq4))
        self.wait(3)
        self.play(Transform(rhs4, rhs4a))


        self.wait(5)  



class Graph(Scene):
    def construct(self):   

        title1 = MathTex(r" \int_0^2 xe^{x^2-1}\,dx.", color=YELLOW).scale(0.8).to_edge(UP)
        title2 = MathTex(r" \int_{-1}^3 \frac{1}{2}e^u\,du.", color=PURPLE).scale(0.8).to_edge(UP)
        title3 = MathTex(r" \int_0^2 xe^{x^2-1}\,dx.", color=YELLOW).scale(0.8).to_edge(UP)



        axes = Axes(x_range=[-2,4,2], y_range=[-1, 42, 10], x_length=5, y_length=5,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        axes_labels2 = axes.get_axis_labels(MathTex("u").scale(0.5), MathTex("y").scale(0.5))
        axes_labels3 = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))

        numberplane = NumberPlane(x_range=[-2,4,2], y_range=[-1, 42, 10], x_length=5, y_length=5,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        #L1 = DashedLine(axes.coords_to_point(-5, 2/3), axes.coords_to_point(1, 2/3), color="RED")

        
        

        plot1 = axes.plot(lambda x:( x*np.exp(x**2-1) ), 
            x_range=[0, 2], 
            use_smoothing=True,
            color=YELLOW)
        plot3 = axes.plot(lambda x:( x*np.exp(x**2-1) ), 
            x_range=[0, 2], 
            use_smoothing=True,
            color=YELLOW)

        plot2 = axes.plot(lambda x:( (1/2)*np.exp(x) ), 
            x_range=[-1, 3], 
            use_smoothing=True,
            color=PURPLE)

        area1 = axes.get_area(graph=plot1, x_range=[0,2], color=YELLOW)

        area2 = axes.get_area(graph=plot2, x_range=[-1,3], color=PURPLE)

        area3 = axes.get_area(graph=plot1, x_range=[0,2], color=YELLOW)
        




        
        self.add(title1)
        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        #self.play(Create(L1))
        self.play(Create(plot1), )
        self.wait(3)
        self.play(Create(area1), )
        self.wait(5)
        self.play(Transform(plot1, plot2), Transform(title1, title2), Transform(area1, area2), Transform(axes_labels, axes_labels2))
        self.wait(7)
        self.play(Transform(plot1, plot3), Transform(title1, title3), Transform(area1, area3), Transform(axes_labels, axes_labels3))

       
        self.wait(5)        


class FindIndef2(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the indefinite integral } \displaystyle \int  (x-1)(x-10)^\frac{2}{3}\,dx.", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        equ1 = MathTex(r"=", color=RED).scale(0.6).shift(RIGHT*4+UP*1)
        equ2 = MathTex(r"=", color=BLUE).scale(0.6).next_to(equ1, DOWN*2)

        lhs1 = MathTex(r"\displaystyle \int    (x-1)(x-10)^\frac{2}{3}\,dx").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \int   ", r" (x-1) ", r" (x-10) ", r" ^\frac{2}{3} ", r" \,dx").scale(0.8).next_to(eq1, RIGHT)
        
        rhs2 = MathTex(r"\displaystyle \int   ", r" (x-1) ", r" u ", r" ^\frac{2}{3} ", r" \,du").scale(0.8).next_to(eq2, RIGHT)
        rhs2[2].set_color(RED)
        rhs2[4].set_color(BLUE)
        rhs2a = MathTex(r"\displaystyle \int   ", r" (u+9) ", r" u ", r" ^\frac{2}{3} ", r" \,du").scale(0.8).next_to(eq2, RIGHT)
        rhs2a[2].set_color(RED)
        rhs2a[1].set_color(RED)
        rhs2a[4].set_color(BLUE)

        rhs2b = MathTex(r"\displaystyle \int   ", r" (u+9) ", r" u ", r" ^\frac{2}{3} ", r" \,du").scale(0.8).next_to(eq2, RIGHT)
        rhs2b[2].set_color(RED)
        rhs2b[1].set_color(RED)
        rhs2b[4].set_color(BLUE)

        rhs2c = MathTex(r"\displaystyle \int ", r"u", r"^{\frac{5}{3}} + 9", r"u", r"^{\frac{2}{3}} ", r" \,du").scale(0.8).next_to(eq2, RIGHT)
        rhs2c[3].set_color(RED)
        rhs2c[1].set_color(RED)
        rhs2c[5].set_color(BLUE)

        lhsu1 = MathTex(r"u", color=RED).scale(0.6).next_to(equ1, LEFT)
        rhsu1 = MathTex(r"x-10", color=RED).scale(0.6).next_to(equ1, RIGHT)

        lhsu1a = MathTex(r"x-1", color=RED).scale(0.6).next_to(equ1, LEFT)
        rhsu1a = MathTex(r"u+9", color=RED).scale(0.6).next_to(equ1, RIGHT)

        lhsu1b = MathTex(r"u", color=RED).scale(0.6).next_to(equ1, LEFT)
        rhsu1b = MathTex(r"x-10", color=RED).scale(0.6).next_to(equ1, RIGHT)

        lhsu2 = MathTex(r"du", color=BLUE).scale(0.6).next_to(equ2, LEFT)
        rhsu2 = MathTex(r"dx", color=BLUE).scale(0.6).next_to(equ2, RIGHT)

        rhs3 = MathTex(r"\frac{1}{\frac{8}{3}}", r"u", r"^{8/3} ", r"+\frac{9}{\frac{5}{3}}", r"u", r"^{5/3} ", r" +C").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(RED)
        rhs3[4].set_color(RED)
        rhs3a = MathTex(r"\frac{3}{8}", r"u", r"^{8/3} ", r"+\frac{27}{5}", r"u", r"^{5/3} ", r" +C").scale(0.8).next_to(eq3, RIGHT)
        rhs3a[1].set_color(RED)
        rhs3a[4].set_color(RED)

        rhs4 = MathTex(r"\frac{3}{8}", r"(x-10)", r"^{8/3} ", r"+\frac{27}{5}", r"(x-10)", r"^{5/3} ", r" +C").scale(0.8).next_to(eq4, RIGHT)
        rhs4[1].set_color(RED)
        rhs4[4].set_color(RED)        
        
        


        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(rhs1), Write(eq1))
        self.wait(5)
        self.play(Wiggle(rhs1[2]))
        self.wait(2)
        self.play(Write(lhsu1))
        self.wait(2)
        self.play(Write(equ1), Write(rhsu1))
        self.wait(3)
        self.play(Write(lhsu2))
        self.wait(2)
        self.play(Write(equ2), Write(rhsu2))
        self.wait(5)
        self.play(Wiggle(rhs1[2]))
        self.play(rhs1[2].animate.set_color(RED))
        self.wait(3)
        self.play(Wiggle(rhs1[4]),)
        self.play(rhs1[4].animate.set_color(BLUE), )
        self.wait(2)
        self.play(Write(rhs2), Write(eq2))
        self.wait(3)
        
        self.play(Wiggle(rhs2[1]))
        self.play(Transform(lhsu1, lhsu1a), Transform(rhsu1, rhsu1a))
        self.wait(5)
        self.play(Wiggle(rhs2[1]))
        self.play(Transform(rhs2, rhs2b))
        self.wait(5)
        self.play(Transform(rhs2, rhs2c))
        self.wait(5)
        

        self.play(Write(rhs3), Write(eq3))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(2)
        self.play(Transform(lhsu1, lhsu1b), Transform(rhsu1, rhsu1b))
        self.play(Wiggle(lhsu1), Wiggle(rhsu1))
        self.play(Write(eq4), Write(rhs4))
        self.wait(3)
        self.play(rhs4[1].animate.set_color(WHITE))
        self.play(rhs4[4].animate.set_color(WHITE))

        


        self.wait(10)              


        

       





        
        



        


        
        



        



  
       