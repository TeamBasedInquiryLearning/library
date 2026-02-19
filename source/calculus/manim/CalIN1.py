#%%manim -ql LIPoly

from manim import *






class Part1(Scene):
    def construct(self):

        #Domain
        title1 = MathTex(r"\text{Find }\displaystyle \int_1^4(-3x+6)dx").scale(0.8).to_edge(UP).set_color(TEAL)


        axes = Axes(x_range=[-2,6,2], y_range=[-8,4,4], x_length=5, y_length=5,).shift(3*RIGHT)

        axes_labels = axes.get_axis_labels(MathTex("x_1").scale(0.5), MathTex("x_2").scale(0.5))
        numberplane = NumberPlane(x_range=[-2,6,2], y_range=[-8,4,4], x_length=5, y_length=5,).add_coordinates().shift(3*RIGHT)

        
        plot1 = axes.plot(lambda x:( -3*x+6 ), 
            x_range=[1, 4], 
            use_smoothing=True,
            color=YELLOW)


        area1 = axes.get_area(graph=plot1, x_range=[1,2], color=BLUE)

        area2 = axes.get_area(graph=plot1, x_range=[2,4], color=RED)

        P1=Dot(axes.coords_to_point(1, 3), color=WHITE)
        label1 = MathTex(r"(1,3)", color=WHITE).scale(0.5).next_to(P1, RIGHT)

        P2=Dot(axes.coords_to_point(2, 0), color=WHITE)
        label2 = MathTex(r"(2,0)", color=WHITE).scale(0.5).next_to(P2, UP/1.4+RIGHT/1.4)

        P3=Dot(axes.coords_to_point(4, -6), color=WHITE)
        label3 = MathTex(r"(4,-6)", color=WHITE).scale(0.5).next_to(P3, RIGHT)

        


        eq1 = MathTex(r"=").scale(0.6).shift(UP, LEFT*3)
        eq2 = MathTex(r"=").scale(0.6).next_to(eq1, DOWN*4)
        eq3 = MathTex(r"=").scale(0.6).next_to(eq2, DOWN*4)
        eq4 = MathTex(r"=").scale(0.6).next_to(eq3, DOWN*4)


       
        

        lhs1 = MathTex(r"\displaystyle \int_1^4(-3x+6)dx").scale(0.6).next_to(eq1, LEFT)

        rhs1 = MathTex(r"\displaystyle \frac{1}{2}(3\cdot 1) ", r" - ", r" \frac{1}{2}(6\cdot 2)").scale(0.6).next_to(eq1, RIGHT)
        rhs1[0].set_color(BLUE)
        rhs1[2].set_color(RED)

        rhs2 = MathTex(r"\displaystyle \frac{3}{2} ",  r" - ", r" 6").scale(0.6).next_to(eq2, RIGHT)
        rhs2[0].set_color(BLUE)
        rhs2[2].set_color(RED)

        rhs3 = MathTex(r"\displaystyle -\frac{9}{2} ").scale(0.6).next_to(eq3, RIGHT)

        self.add(axes, axes_labels,  title1, numberplane)
        self.wait(5)
        self.play(Create(plot1), Create(area1), Create(area2))
        self.wait(10)
        self.play(Create(P1), Write(label1), Create(P2), Write(label2), Create(P3), Write(label3), )
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(10)


class Part2(Scene):
    def construct(self):

        #Domain
        title1 = MathTex(r"\displaystyle \int_1^5", r"\left(-\sqrt{16 -{\left(x - 1\right)}^{2} }\right)", r"dx").scale(0.8).to_edge(UP).set_color(TEAL)


        axes = Axes(x_range=[0, 6, 2], y_range=[-5,1,2], x_length=5, y_length=5,).shift(3*RIGHT)

        axes_labels = axes.get_axis_labels(MathTex("x_1").scale(0.5), MathTex("x_2").scale(0.5))
        numberplane = NumberPlane(x_range=[0, 6, 2], y_range=[-5,1,2], x_length=5, y_length=5,).add_coordinates().shift(3*RIGHT)

        
        plot1 = axes.plot(lambda x:( -1*(-1*(x-1)**2+16)**(1/2) ), 
            x_range=[1, 5], 
            use_smoothing=True,
            color=YELLOW)


        area1 = axes.get_area(graph=plot1, x_range=[1,5], color=BLUE)

        #area2 = axes.get_area(graph=plot1, x_range=[2,4], color=RED)

        P1=Dot(axes.coords_to_point(1, -4), color=WHITE)
        label1 = MathTex(r"(1,-4)", color=WHITE).scale(0.5).next_to(P1, UP)

        P2=Dot(axes.coords_to_point(1, 0), color=WHITE)
        label2 = MathTex(r"(1,0)", color=WHITE).scale(0.5).next_to(P2, UP)

        P3=Dot(axes.coords_to_point(5, 0), color=WHITE)
        label3 = MathTex(r"(5,0)", color=WHITE).scale(0.5).next_to(P3, UP)

        


        eq1 = MathTex(r"=").scale(0.6).shift(UP, LEFT*3)
        eq2 = MathTex(r"=").scale(0.6).next_to(eq1, DOWN*4)
        eq3 = MathTex(r"=").scale(0.6).next_to(eq2, DOWN*4)
        eq4 = MathTex(r"=").scale(0.6).next_to(eq3, DOWN*4)


       
        

        lhs1 = MathTex(r"\displaystyle \int_1^5", r"\left(16 -\sqrt{-{\left(x - 1\right)}^{2} }\right)", r"dx").scale(0.6).next_to(eq1, LEFT)

        

        rhs1 = MathTex(r"-\displaystyle \frac{\pi\cdot 4^2}{4} ").scale(0.6).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"-\displaystyle 4\pi ").scale(0.6).next_to(eq2, RIGHT)

        self.add(axes, axes_labels,  title1, numberplane)
        self.wait(10)
        self.play(Wiggle(title1[1]))
        self.play(title1[1].animate.set_color(YELLOW))
        self.wait(10)
        self.play(Create(plot1), Create(area1), )
        self.play(Create(P1), Write(label1), Create(P2), Write(label2), Create(P3), Write(label3), )
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(10)






class Part3(Scene):
    def construct(self):

        #Domain
        title1 = MathTex(r"\text{Find }\displaystyle \int_2^4(-3x+6)dx").scale(0.8).to_edge(UP).set_color(TEAL)


        axes = Axes(x_range=[-2,6,2], y_range=[-8,4,4], x_length=5, y_length=5,).shift(3*RIGHT)

        axes_labels = axes.get_axis_labels(MathTex("x_1").scale(0.5), MathTex("x_2").scale(0.5))
        numberplane = NumberPlane(x_range=[-2,6,2], y_range=[-8,4,4], x_length=5, y_length=5,).add_coordinates().shift(3*RIGHT)

        
        plot1 = axes.plot(lambda x:( -3*x+6 ), 
            x_range=[2, 4], 
            use_smoothing=True,
            color=YELLOW)


        #area1 = axes.get_area(graph=plot1, x_range=[1,2], color=BLUE)

        area2 = axes.get_area(graph=plot1, x_range=[2,4], color=RED)

        #P1=Dot(axes.coords_to_point(1, 3), color=WHITE)
        #label1 = MathTex(r"(1,3)", color=WHITE).scale(0.5).next_to(P1, RIGHT)

        P2=Dot(axes.coords_to_point(2, 0), color=WHITE)
        label2 = MathTex(r"(2,0)", color=WHITE).scale(0.5).next_to(P2, UP/1.4+RIGHT/1.4)

        P3=Dot(axes.coords_to_point(4, -6), color=WHITE)
        label3 = MathTex(r"(4,-6)", color=WHITE).scale(0.5).next_to(P3, RIGHT)

        


        eq1 = MathTex(r"=").scale(0.6).shift(UP, LEFT*3)
        eq2 = MathTex(r"=").scale(0.6).next_to(eq1, DOWN*4)
        eq3 = MathTex(r"=").scale(0.6).next_to(eq2, DOWN*4)
        eq4 = MathTex(r"=").scale(0.6).next_to(eq3, DOWN*4)


       
        

        lhs1 = MathTex(r"\displaystyle \int_1^4(-3x+6)dx").scale(0.6).next_to(eq1, LEFT)

        rhs1 = MathTex(r"  \frac{1}{2}(-6\cdot 2)").scale(0.6).next_to(eq1, RIGHT)
        rhs1.set_color(RED)

        rhs2 = MathTex(r"-6").scale(0.6).next_to(eq2, RIGHT)
        rhs2.set_color(RED)


        self.add(axes, axes_labels,  title1, numberplane)
        self.wait(3)
        self.play(Create(plot1),  Create(area2))
        self.play( Create(P2), Write(label2), Create(P3), Write(label3), )
        self.wait(10)
        self.play(Write(lhs1))
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        #self.wait(5)
        #self.play(Write(eq3), Write(rhs3))
        self.wait(10)

        

        

        



        


        
        



        



  
       