#%%manim -ql LIPoly

from manim import *







class FindCP(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the absolute extrema of } f(x)=2x^3-96x+79 \text{ on } [-1,9]", color=TEAL).scale(0.8).to_edge(UP)

        caption1 = MathTex(r"-4\text{ is not in the domain of }f(x)", color=ORANGE).scale(0.8).to_edge(DOWN)

        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"f(x)", ).scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"2x^3-96x+79 ", ).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"f'(x)", ).scale(0.8).next_to(eq2, LEFT)
        lhs2a = MathTex(r"0", color="RED").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"6x^2-96 ", ).scale(0.8).next_to(eq2, RIGHT)

        rhs3 = MathTex(r"6(x^2-16) ", ).scale(0.8).next_to(eq3, RIGHT)
        rhs3a = MathTex(r"6(x-4)(x+4) ", ).scale(0.8).next_to(eq3, RIGHT)

        lhs4 = MathTex(r"x", ).scale(0.8).next_to(eq4, LEFT)
        rhs4 = MathTex(r"-4, ", r"4 ", ).scale(0.8).next_to(eq4, RIGHT)


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1),Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(lhs2),Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Transform(lhs2, lhs2a))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(5)
        self.play(Write(lhs4),Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(rhs4[0].animate.set_color(RED))
        self.play(Write(caption1))
        self.wait(3)
        self.play(FadeOut(rhs4[0]))
        self.wait(10)
        self.play(FadeOut(lhs1, rhs1, eq1, lhs2, rhs2, eq2, lhs4, rhs3, eq3,  rhs4[1], eq4, caption1))

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        #eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*4)
        #eq5 = MathTex(r"=").scale(0.8).next_to(eq4, DOWN*4)

        lhs1 = MathTex(r"f(-1)", ).scale(0.8).next_to(eq1, LEFT)
        #rhs1 = MathTex(r"0+2\sin(0) ", r"=0.", ).scale(0.8).next_to(eq1, RIGHT)
        rhs1 = MathTex(r"2(-1)^3-96(-1)+79 ", r"=173.").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"f\left(4 \right)", ).scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"2(4)^3-96(4)+79", r"=-177.").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"f\left(9 \right)", ).scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"2(9)^3-96(9)+79 ", r"=673.",).scale(0.8).next_to(eq3, RIGHT)

        gmin = MathTex(r"\text{ Global Min!}", color=RED).scale(0.8).next_to(rhs2, RIGHT)
        gmax = MathTex(r"\text{ Global Max!}", color=GREEN).scale(0.8).next_to(rhs3, RIGHT)

        
        self.play(Write(lhs1),Write(eq1), Write(rhs1[0]))
        self.wait(3)
        self.play(Write(rhs1[1]))
        self.wait(3)

        self.play(Write(lhs2),Write(eq2), Write(rhs2[0]))
        self.wait(3)
        self.play(Write(rhs2[1]))
        self.wait(3)

        self.play(Write(lhs3),Write(eq3), Write(rhs3[0]))
        self.wait(3)
        self.play(Write(rhs3[1]))
        self.wait(3)

        

        self.play(Write(gmin), Write(gmax))
        self.wait(5)

        self.play(FadeOut(lhs1, rhs1, eq1, lhs2, rhs2, eq2, lhs3, rhs3, eq3, gmin, gmax))



class ShowExtrema(Scene):
    def construct(self):


        title1 = MathTex(r"\text{Find the absolute extrema of } f(x)=2x^3-96x+79 \text{ on } [-1,9]").scale(0.8)        
        title1.to_edge(UP)

        axes = Axes(x_range=[-2,10,4], y_range=[-200,700,200], x_length=6, y_length=6,)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        #numberplane = NumberPlane(x_range=[-2,10,4], y_range=[-200,700,200],
        #    x_length=6,
        #    y_length=6,
        #    ).add_coordinates()

        
        P1=Dot(axes.coords_to_point(-1, 173), color=BLUE)
        label1 = MathTex(r"(-1,173)", color=BLUE).scale(0.5).next_to(P1, UP)

        P2=Dot(axes.coords_to_point(4, -179), color=RED)
        label2 = MathTex(r"(4, -179)", color=RED).scale(0.5).next_to(P2, RIGHT)

        P3=Dot(axes.coords_to_point(9, 673), color=GREEN)
        label3 = MathTex(r"(9, 673)", color=GREEN).scale(0.5).next_to(P3, RIGHT)
        

        theplot = axes.plot(lambda x: 2*x**3-96*x+79, 
            x_range=[-1, 9], 
            use_smoothing=False,
            color=YELLOW)

        self.add(axes, axes_labels,  title1)
        self.wait(1)
        self.play(Create(theplot))
        self.wait(5)
        self.play(Create(P1), Create(P2), Create(P3),)
        self.play(Write(label1), Write(label2), Write(label3),)
        self.wait(10)




        
        



        


        
        



        



  
       