#%%manim -ql LIPoly

from manim import *







class Limit1(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the limit} \displaystyle \lim_{x\to\infty} \frac{2x+4\ln(x)}{-3x+3}.").scale(0.8)        
        title1.to_edge(UP)
        title1.set_color(TEAL)


        caption1 = MathTex(r"\text{L'Hopitals Applies}", color="BLUE").scale(0.8) 
        caption1.to_edge(DOWN)

        

       

        eq1LH = MathTex(r"=_{LH}").scale(0.8).shift(UP*2)
        eq2LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq1LH, DOWN*5)
        eq3LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq2LH, DOWN*5)
        eq4LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq3LH, DOWN*5)

        eq1Q = MathTex(r"= \text{ ({\tiny kinda})}").scale(0.8).shift(UP*2)

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1LH, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)


        lhs0 = MathTex(r"\frac{2\infty+4\ln(\infty)}{-3\infty+3}", ).scale(0.8).next_to(eq1Q, LEFT)
        rhs0 = MathTex(r"\frac{\infty}{-\infty}", ).scale(0.8).next_to(eq1Q, RIGHT)


        lhs1 = MathTex(r" \displaystyle \lim_{x\to\infty} \frac{2x+4\ln(x)}{-3x+3}", ).scale(0.8).next_to(eq1LH, LEFT)
        rhs1 = MathTex(r" \displaystyle \lim_{x\to\infty} \frac{2+\frac{4}{x}}{-3}", ).scale(0.8).next_to(eq1LH, RIGHT)

        
        rhs2 = MathTex(r"\frac{2+0}{-3}", ).scale(0.8).next_to(eq2, RIGHT)

        
        rhs3 = MathTex(r"-\frac{2}{3}", ).scale(0.8).next_to(eq3, RIGHT)


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0))
        self.wait(5)
        self.play(Write(eq1Q), Write(rhs0))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(3)
        self.play(FadeOut(lhs0, eq1Q, rhs0, caption1))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(5)
        self.play(Write(eq1LH), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(FadeOut(lhs1, rhs1,  eq1LH, rhs2, eq2, rhs3, eq3 ))





        axes = Axes(x_range=[0.01,100,20], y_range=[-12,12,6], x_length=10, y_length=6,)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[0.01,100,20], y_range=[-12,12,6], x_length=10, y_length=6,
            ).add_coordinates()

        
        
        L1 = DashedLine(axes.coords_to_point(0.01, -2/3), axes.coords_to_point(100, -2/3), color="RED")

        
        

        theplot = axes.plot(lambda x:(2*x+4*np.log(x))/(-3*x+3), 
            x_range=[0.01, 100], 
            use_smoothing=False,
            color=YELLOW)

        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        self.play(Create(L1))
        self.wait(5)
        self.play(Create(theplot))
       
        self.wait(5)


        

class Limit2(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the limit} \displaystyle \lim_{x\to\infty} x^2e^{-x}.").scale(0.8)        
        title1.to_edge(UP)
        title1.set_color(TEAL)


        caption1 = MathTex(r"\text{L'Hopitals Applies}", color="BLUE").scale(0.8) 
        caption1.to_edge(DOWN)

        

       

        eq1LH = MathTex(r"=_{LH}").scale(0.8).shift(UP*2)
        eq2LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq1LH, DOWN*5)
        eq3LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq2LH, DOWN*5)
        eq4LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq3LH, DOWN*5)

        eq1Q = MathTex(r"= \text{ ({\tiny kinda})}").scale(0.8).shift(UP*2)

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1LH, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)


        lhs0 = MathTex(r"\lim_{x\to\infty} x^2e^{-x}", ).scale(0.8).next_to(eq1Q, LEFT)
        rhs0 = MathTex(r"\infty \cdot 0", ).scale(0.8).next_to(eq1Q, RIGHT)


        lhs1 = MathTex(r" \displaystyle \lim_{x\to\infty} x^2e^{-x}", ).scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r" \displaystyle \lim_{x\to\infty} \frac{x^2}{e^x}", ).scale(0.8).next_to(eq1, RIGHT)

        
        rhs2 = MathTex(r"\displaystyle \lim_{x\to\infty} \frac{2x}{e^x}", ).scale(0.8).next_to(eq2LH, RIGHT)

        
        rhs3 = MathTex(r"\displaystyle \lim_{x\to\infty} \frac{2}{e^x}", ).scale(0.8).next_to(eq3LH, RIGHT)

        rhs4 = MathTex(r"0", ).scale(0.8).next_to(eq4, RIGHT)



        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0))
        self.wait(5)
        self.play(Write(eq1Q), Write(rhs0))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(3)
        self.play(FadeOut(lhs0, eq1Q, rhs0, caption1))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(5)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2LH), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3LH), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(FadeOut(lhs1, rhs1,  eq1, rhs2, eq2LH, rhs3, eq3LH, rhs4, eq4 ))





        axes = Axes(x_range=[-1,10,2], y_range=[-1,3,1], x_length=10, y_length=6,)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[-1,10,2], y_range=[-1,3,1], x_length=10, y_length=6,
            ).add_coordinates()

        
        
        L1 = DashedLine(axes.coords_to_point(-1, 0), axes.coords_to_point(10, 0), color="RED")

        
        

        theplot = axes.plot(lambda x:( x*x* np.e**(-x)), 
            x_range=[-1,10], 
            use_smoothing=True,
            color=YELLOW)

        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        self.play(Create(L1))
        self.wait(5)
        self.play(Create(theplot))
       
        self.wait(5)



class Limit3(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the limit} \displaystyle \lim_{x\to 0} \frac{5\sin(7x)}{-3x}.").scale(0.8)        
        title1.to_edge(UP)
        title1.set_color(TEAL)


        caption1 = MathTex(r"\text{L'Hopitals Applies}", color="BLUE").scale(0.8) 
        caption1.to_edge(DOWN)

        

       

        eq1LH = MathTex(r"=_{LH}").scale(0.8).shift(UP*2)
        eq2LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq1LH, DOWN*5)
        eq3LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq2LH, DOWN*5)
        eq4LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq3LH, DOWN*5)

        eq1Q = MathTex(r"= \text{ ({\tiny kinda})}").scale(0.8).shift(UP*2)

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1LH, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)


        lhs0 = MathTex(r"\lim_{x\to 0} \frac{5\sin(7x)}{-3x}", ).scale(0.8).next_to(eq1Q, LEFT)
        rhs0 = MathTex(r"\frac{0}{0}", ).scale(0.8).next_to(eq1Q, RIGHT)


        lhs1 = MathTex(r" \lim_{x\to 0} \frac{5\sin(7x)}{-3x}", ).scale(0.8).next_to(eq1LH, LEFT)
        rhs1 = MathTex(r" \lim_{x\to 0} \frac{35\cos(7x)}{-3}", ).scale(0.8).next_to(eq1LH, RIGHT)

        
        rhs2 = MathTex(r"\frac{35\cdot 1}{-3}", ).scale(0.8).next_to(eq2, RIGHT)

        
        rhs3 = MathTex(r"-\frac{35}{3}", ).scale(0.8).next_to(eq3, RIGHT)


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0))
        self.wait(5)
        self.play(Write(eq1Q), Write(rhs0))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(3)
        self.play(FadeOut(lhs0, eq1Q, rhs0, caption1))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(5)
        self.play(Write(eq1LH), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(FadeOut(lhs1, rhs1,  eq1LH, rhs2, eq2, rhs3, eq3 ))





        axes = Axes(x_range=[-4,4,2], y_range=[-18,6,6], x_length=10, y_length=6,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[-4,4,2], y_range=[-18,6,6], x_length=10, y_length=6,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        L1 = DashedLine(axes.coords_to_point(-4, -35/3), axes.coords_to_point(4, -35/3), color="RED")

        
        

        plot1 = axes.plot(lambda x:(5*np.sin(7*x)/(-3*x)), 
            x_range=[-4, -0.01], 
            use_smoothing=True,
            color=YELLOW)


        plot2 = axes.plot(lambda x:(5*np.sin(7*x)/(-3*x)), 
            x_range=[0.01, 4], 
            use_smoothing=True,
            color=YELLOW)

        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        self.play(Create(L1))
        self.wait(5)
        self.play(Create(plot1), Create(plot2))
       
        self.wait(5)









class Limit4(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the limit} \displaystyle \lim_{x\to \infty} \frac{5\sin(7x)}{-3x}.").scale(0.8)        
        title1.to_edge(UP)
        title1.set_color(TEAL)


        caption1 = MathTex(r"\text{L'Hopitals DOES NOT Apply}", color="RED").scale(0.8) 
        caption1.to_edge(DOWN)

        caption2 = MathTex(r"\text{By the Squeeze Theorem: }\lim_{x\to \infty} \frac{5\sin(7x)}{-3x}=0.", color="BLUE").scale(0.8) 
        caption2.to_edge(DOWN)

        

       

        

        eq1Q = MathTex(r"= \text{ ({\tiny kinda})}").scale(0.8).shift(UP*2)

        ineq11 = MathTex(r"\geq").scale(0.8).shift(UP*2+LEFT*2)
        ineq12 = MathTex(r"\geq").scale(0.8).shift(UP*2+RIGHT*2)
        ineq21 = MathTex(r"\leq").scale(0.8).next_to(ineq11, DOWN*5)
        ineq31 = MathTex(r"\leq").scale(0.8).next_to(ineq21, DOWN*5)
        ineq41 = MathTex(r"\leq").scale(0.8).next_to(ineq31, DOWN*5)

        ineq22 = MathTex(r"\leq").scale(0.8).next_to(ineq12, DOWN*5)
        ineq32 = MathTex(r"\leq").scale(0.8).next_to(ineq22, DOWN*5)
        ineq42 = MathTex(r"\leq").scale(0.8).next_to(ineq32, DOWN*5)


        lhs0 = MathTex(r"\lim_{x\to \infty} \frac{5\sin(7x)}{-3x}", ).scale(0.8).next_to(eq1Q, LEFT)
        rhs0 = MathTex(r"\frac{\text{UND}}{-\infty}", ).scale(0.8).next_to(eq1Q, RIGHT)



        lhs1 = MathTex(r" 5", ).scale(0.8).next_to(ineq11, LEFT)
        mhs1 = MathTex(r"5\sin(7x)", ).scale(0.8).next_to(ineq11, RIGHT*5)
        rhs1 = MathTex(r" -5", ).scale(0.8).next_to(ineq12, RIGHT)

        
        lhs2 = MathTex(r" -\frac{5}{3x}", ).scale(0.8).next_to(ineq21, LEFT)
        mhs2 = MathTex(r"-\frac{5\sin(7x)}{3x}", ).scale(0.8).next_to(ineq21, RIGHT*4)
        rhs2 = MathTex(r" \frac{5}{3x}", ).scale(0.8).next_to(ineq22, RIGHT)

        lhs3 = MathTex(r"\displaystyle \lim_{x\to \infty} -\frac{5}{3x}", ).scale(0.8).next_to(ineq31, LEFT)
        mhs3 = MathTex(r"\displaystyle \lim_{x\to \infty} -\frac{5\sin(7x)}{3x}", ).scale(0.8).next_to(ineq31, RIGHT*2.5)
        rhs3 = MathTex(r" \displaystyle \lim_{x\to \infty} \frac{5}{3x}", ).scale(0.8).next_to(ineq32, RIGHT)

        lhs4 = MathTex(r"0", ).scale(0.8).next_to(ineq31, LEFT)
        
        rhs4 = MathTex(r" 0", ).scale(0.8).next_to(ineq32, RIGHT)


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0))
        self.wait(5)
        self.play(Write(eq1Q), Write(rhs0))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(3)
        self.play(FadeOut(lhs0, eq1Q, rhs0, caption1))
        self.wait(3)
        self.play(Write(lhs1), Write(ineq11), Write(mhs1), Write(ineq12), Write(rhs1))
        self.wait(5)
        self.play(Write(lhs2), Write(ineq21), Write(mhs2), Write(ineq22), Write(rhs2))
        self.wait(5)
        self.play(Write(lhs3), Write(ineq31), Write(mhs3), Write(ineq32), Write(rhs3))
        self.wait(5)
        self.play(Transform(lhs3, lhs4), Transform(rhs3, rhs4))
        self.wait(5)
        self.play(Write(caption2))
        self.wait(5)
        self.play(FadeOut(lhs1, rhs1,  lhs2, rhs2, lhs3, rhs3,  mhs1, mhs2, mhs3, ineq11, ineq21, ineq31, ineq12, ineq22, ineq32, caption2))





        axes = Axes(x_range=[0,25,5], y_range=[-18,18,6], x_length=10, y_length=6,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[0,25,5], y_range=[-18,18,6], x_length=10, y_length=6,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        L1 = DashedLine(axes.coords_to_point(0, 0), axes.coords_to_point(25, 0), color="RED")

        
        

        plot1 = axes.plot(lambda x:(5*np.sin(7*x)/(-3*x)), 
            x_range=[0.1, 25], 
            use_smoothing=True,
            color=YELLOW)

        bound1 = axes.plot(lambda x:(5/(3*x)), 
            x_range=[0.1, 25], 
            use_smoothing=True,
            color=BLUE)

        bound2 = axes.plot(lambda x:(-5/(3*x)), 
            x_range=[0.1, 25], 
            use_smoothing=True,
            color=BLUE)


        bound1 = DashedVMobject(bound1)
        bound2 = DashedVMobject(bound2)



        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        self.play(Create(L1))
        self.wait(5)
        self.play(Create(bound1), Create(bound2))
        self.wait(5)
        self.play(Create(plot1), )
       
        self.wait(5)        



class Limit5(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the limit} \displaystyle \lim_{x\to 0} \frac{9\cos(-3x)}{5x-7}.").scale(0.8)        
        title1.to_edge(UP)
        title1.set_color(TEAL)


        caption1 = MathTex(r"\text{L'Hopitals DOES NOT Apply}", color="RED").scale(0.8) 
        caption1.to_edge(DOWN)

        

       

        eq1LH = MathTex(r"=_{LH}").scale(0.8).shift(UP*2)
        eq2LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq1LH, DOWN*5)
        eq3LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq2LH, DOWN*5)
        eq4LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq3LH, DOWN*5)

        eq1Q = MathTex(r"= \text{ ({\tiny kinda})}").scale(0.8).shift(UP*2)

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1LH, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)


        lhs0 = MathTex(r"\lim_{x\to 0} \frac{9\cos(-3x)}{5x-7}", ).scale(0.8).next_to(eq1, LEFT)
        rhs0 = MathTex(r"\frac{9\cdot 1}{0-7}", ).scale(0.8).next_to(eq1, RIGHT)


        
        rhs2 = MathTex(r"-\frac{9}{7}", ).scale(0.8).next_to(eq2, RIGHT)

        
        


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0))
        self.wait(5)
        self.play(Write(eq1), Write(rhs0))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(3)
       
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(FadeOut(lhs0, rhs0,  eq1, rhs2, eq2, caption1))





        axes = Axes(x_range=[-1,1,1], y_range=[-2,5,2], x_length=10, y_length=6,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[-1,1,1], y_range=[-2,5,2],  x_length=10, y_length=6,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        L1 = DashedLine(axes.coords_to_point(-1, -9/7), axes.coords_to_point(1, -9/7), color="RED")

        
        

        plot1 = axes.plot(lambda x:(9*np.cos(-3*x)/(5*x-7)), 
            x_range=[-1, 1], 
            use_smoothing=True,
            color=YELLOW)


        

        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        self.play(Create(L1))
        self.wait(5)
        self.play(Create(plot1), )
       
        self.wait(5)



class Limit6(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the limit} \displaystyle \lim_{x\to -3} \frac{x^2-9}{x^2-3x-18}.").scale(0.8)        
        title1.to_edge(UP)
        title1.set_color(TEAL)


        caption1 = MathTex(r"\text{L'Hopitals Applies}", color="BLUE").scale(0.8) 
        caption1.to_edge(DOWN)

        

       

        eq1LH = MathTex(r"=_{LH}").scale(0.8).shift(UP*2)
        eq2LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq1LH, DOWN*5)
        eq3LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq2LH, DOWN*5)
        eq4LH = MathTex(r"=_{LH}").scale(0.8).next_to(eq3LH, DOWN*5)

        eq1Q = MathTex(r"= \text{ ({\tiny kinda})}").scale(0.8).shift(UP*2)

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1LH, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)


        lhs0 = MathTex(r"\lim_{x\to -3} \frac{x^2-9}{x^2-3x-18}", ).scale(0.8).next_to(eq1Q, LEFT)
        rhs0 = MathTex(r"\frac{0}{0}", ).scale(0.8).next_to(eq1Q, RIGHT)


        lhs1 = MathTex(r" \lim_{x\to -3} \frac{x^2-9}{x^2-3x-18}", ).scale(0.8).next_to(eq1LH, LEFT)
        rhs1 = MathTex(r" \lim_{x\to -3} \frac{2x}{2x-3}", ).scale(0.8).next_to(eq1LH, RIGHT)

        
        rhs2 = MathTex(r"\frac{2\cdot (-3)}{2\cdot(-3)-3}", ).scale(0.8).next_to(eq2, RIGHT)

        
        rhs3 = MathTex(r"\frac{2}{3}", ).scale(0.8).next_to(eq3, RIGHT)


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0))
        self.wait(5)
        self.play(Write(eq1Q), Write(rhs0))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(3)
        self.play(FadeOut(lhs0, eq1Q, rhs0, caption1))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(5)
        self.play(Write(eq1LH), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(FadeOut(lhs1, rhs1,  eq1LH, rhs2, eq2, rhs3, eq3 ))





        axes = Axes(x_range=[-5,1,1], y_range=[-1,1,0.5], x_length=10, y_length=6,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[-5,1,1], y_range=[-1,1,0.5], x_length=10, y_length=6,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        L1 = DashedLine(axes.coords_to_point(-5, 2/3), axes.coords_to_point(1, 2/3), color="RED")

        
        

        plot1 = axes.plot(lambda x:((x-3)/(x-6)), 
            x_range=[-5, 1], 
            use_smoothing=True,
            color=YELLOW)


        

        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        self.play(Create(L1))
        self.wait(5)
        self.play(Create(plot1), )
       
        self.wait(10)

        
        



        


        
        



        



  
       