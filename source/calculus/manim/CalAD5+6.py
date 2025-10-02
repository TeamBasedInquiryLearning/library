#%%manim -ql LIPoly

from manim import *







class FindCP(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the critical values of } f(x)=4x^3-3x^4 \text{ and classify them.}").scale(0.8)        
        title1.to_edge(UP)
        title1.set_color(TEAL)


        caption1 = MathTex(r"\text{The CV are: } x=0, 1.", color="RED").scale(0.8) 
        caption1.to_edge(DOWN)

        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"f(x)", ).scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"4x^3-3x^4", ).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"f'(x)", ).scale(0.8).next_to(eq2, LEFT)
        lhs2a = MathTex(r"0", color="RED").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"12x^2-12x^3 ", ).scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"0", ).scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"12x^2(1-x)", ).scale(0.8).next_to(eq3, RIGHT)

        lhs4 = MathTex(r"x", ).scale(0.8).next_to(eq4, LEFT)
        rhs4 = MathTex(r"0, 1 ", ).scale(0.8).next_to(eq4, RIGHT)


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1),Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(lhs2),Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Transform(lhs2, lhs2a))
        self.wait(5)
        self.play(Write(lhs3),Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(lhs4),Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(FadeOut(lhs1, rhs1,  lhs2, rhs2, eq2, lhs4, rhs4, eq4, eq3 ))
        self.play(lhs3.animate.next_to(eq1, LEFT), rhs3.animate.next_to(eq1, RIGHT), Write(caption1))
        self.wait(10)


        caption2 = MathTex(r"f(x) \text{ has a local max at } (1,f(1)), \text{ and no extrema at }(0,f(0)).", color="RED").scale(0.8) 
        caption2.to_edge(DOWN)

        caption3 = MathTex(r"f(x) \text{ has a local max at } (1,4\cdot1^3-3\cdot1^4), \text{ and no extrema at }(0,4\cdot0^3-3\cdot0^4).", color="RED").scale(0.8) 
        caption3.to_edge(DOWN)

        caption4 = MathTex(r"f(x) \text{ has a local max at } (1,1), \text{ and no extrema at }(0,0).", color="RED").scale(0.8) 
        caption4.to_edge(DOWN)


        NumLine = Line([-5,0.5,0], [5,0.5,0], color="Yellow")

        tick1 = Line([-2,0,0], [-2,1,0], color="Yellow")
        tick2 = Line([3,0,0], [3,1,0], color="Yellow")
        label1 = MathTex(r"0", color="RED").scale(0.8).next_to(tick1, UP)
        label2 = MathTex(r"1", color="RED").scale(0.8).next_to(tick2, UP)

        factor1 = MathTex(r"12", ).scale(0.8).next_to([-6,-0.5,0])
        sign11 =  MathTex(r"+", color="BLUE").scale(0.8).next_to([-3.5,-0.5,0])
        sign12 =  MathTex(r"+", color="BLUE").scale(0.8).next_to([0.5,-0.5,0])
        sign13 =  MathTex(r"+", color="BLUE").scale(0.8).next_to([4,-0.5,0])

        factor2 = MathTex(r"x^2", ).scale(0.8).next_to(factor1, DOWN*1.5)
        sign21 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign11, DOWN*1.5)
        sign22 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign12, DOWN*1.5)
        sign23 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign13, DOWN*1.5)

        factor3 = MathTex(r"1-x", ).scale(0.8).next_to(factor2, DOWN*1.5)
        sign31 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign21, DOWN*1.5)
        sign32 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign22, DOWN*1.5)
        sign33 =  MathTex(r"-", color="RED").scale(0.8).next_to(sign23, DOWN*2)

        factor4 = MathTex(r"f'(x)", ).scale(0.8).next_to(factor3, DOWN*1.5)
        sign41 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign31, DOWN*1.5)
        sign42 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign32, DOWN*1.5)
        sign43 =  MathTex(r"-", color="RED").scale(0.8).next_to(sign33, DOWN*2.5)

        self.play(Create(NumLine), Create(tick1), Create(tick2), Write(label1), Write(label2))
        self.wait(3)
        self.play(Write(factor1))
        self.wait(3)
        self.play(Write(sign11), Write(sign12), Write(sign13))
        self.wait(3)
        self.play(Write(factor2))
        self.wait(3)
        self.play(Write(sign21), Write(sign22), Write(sign23))
        self.wait(3)
        self.play(Write(factor3))
        self.wait(3)
        self.play(Write(sign31), Write(sign32), Write(sign33))
        self.wait(5)
        self.play(Write(factor4))
        self.wait(5)
        self.play(Write(sign41), Write(sign42), Write(sign43))

        self.wait(7)
        self.play(Transform(caption1, caption2))
        self.wait(7)
        self.play(Transform(caption1, caption3))
        self.wait(7)
        self.play(Transform(caption1, caption4))


        self.wait(10)

class FindIP(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the inflection points of } f(x)=4x^3-3x^4 \text{ and classify them.}").scale(0.8)        
        title1.to_edge(UP)
        title1.set_color(TEAL)


        caption1 = MathTex(r"f''(x)=0 \text{ when } x=0, \frac{2}{3}.", color="RED").scale(0.8) 
        caption1.to_edge(DOWN)

        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"f'(x)", ).scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"12x^2-12x^3", ).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"f''(x)", ).scale(0.8).next_to(eq2, LEFT)
        lhs2a = MathTex(r"0", color="RED").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"24x-36x^2 ", ).scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"0", ).scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"12x(2-3x)", ).scale(0.8).next_to(eq3, RIGHT)

        lhs4 = MathTex(r"x", ).scale(0.8).next_to(eq4, LEFT)
        rhs4 = MathTex(r"0, \frac{2}{3} ", ).scale(0.8).next_to(eq4, RIGHT)


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1),Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(lhs2),Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Transform(lhs2, lhs2a))
        self.wait(5)
        self.play(Write(lhs3),Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(lhs4),Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(FadeOut(lhs1, rhs1,  lhs2, rhs2, eq2, lhs4, rhs4, eq4, eq3 ))
        self.play(lhs3.animate.next_to(eq1, LEFT), rhs3.animate.next_to(eq1, RIGHT), Write(caption1))
        self.wait(10)


        caption2 = MathTex(r"f(x) \text{ has an inflection point, changing from concave down to up ,at } (0,f(0)).", color="RED").scale(0.5) 
        caption2.to_edge(DOWN)

        caption3 =  MathTex(r"f(x) \text{ has an inflection point, changing from concave down to up, at } (0,4\cdot0^3-3\cdot 0^4).", color="RED").scale(0.5) 
        caption3.to_edge(DOWN)

        caption4 = MathTex(r"f(x) \text{ has an inflection point, changing from concave down to up, at }(0,0).", color="RED").scale(0.5) 
        caption4.to_edge(DOWN)


        caption5 = MathTex(r"f(x) \text{ has an inflection point, changing from concave up to down, at } \left(\frac{2}{3},f\left(\frac{2}{3}\right)\right).", color="RED").scale(0.5) 
        caption5.to_edge(DOWN)

        caption6 =  MathTex(r"f(x) \text{ has an inflection point, changing from concave up to down, at } \left(\frac{2}{3},4\cdot \left(\frac{2}{3}\right)^3-3\cdot \left(\frac{2}{3}\right)^4\right).", color="RED").scale(0.5) 
        caption6.to_edge(DOWN)

        caption7 = MathTex(r"f(x) \text{ has an inflection point, changing from concave up to down, at }\left(\frac{2}{3},\frac{16}{27}\right).", color="RED").scale(0.5) 
        caption7.to_edge(DOWN)


        NumLine = Line([-5,0.5,0], [5,0.5,0], color="Yellow")

        tick1 = Line([-2,0,0], [-2,1,0], color="Yellow")
        tick2 = Line([3,0,0], [3,1,0], color="Yellow")
        label1 = MathTex(r"0", color="RED").scale(0.8).next_to(tick1, UP)
        label2 = MathTex(r"\frac{2}{3}", color="RED").scale(0.8).next_to(tick2, UP)

        factor1 = MathTex(r"12", ).scale(0.8).next_to([-6,-0.5,0])
        sign11 =  MathTex(r"+", color="BLUE").scale(0.8).next_to([-3.5,-0.5,0])
        sign12 =  MathTex(r"+", color="BLUE").scale(0.8).next_to([0.5,-0.5,0])
        sign13 =  MathTex(r"+", color="BLUE").scale(0.8).next_to([4,-0.5,0])

        factor2 = MathTex(r"x", ).scale(0.8).next_to(factor1, DOWN*1.5)
        sign21 =  MathTex(r"-", color="RED").scale(0.8).next_to(sign11, DOWN*2)
        sign22 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign12, DOWN*1.5)
        sign23 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign13, DOWN*1.5)

        factor3 = MathTex(r"3-2x", ).scale(0.8).next_to(factor2, DOWN*1.5)
        sign31 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign21, DOWN*2)
        sign32 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign22, DOWN*1.5)
        sign33 =  MathTex(r"-", color="RED").scale(0.8).next_to(sign23, DOWN*2)

        factor4 = MathTex(r"f''(x)", ).scale(0.8).next_to(factor3, DOWN*1.5)
        sign41 =  MathTex(r"-", color="RED").scale(0.8).next_to(sign31, DOWN*2)
        sign42 =  MathTex(r"+", color="BLUE").scale(0.8).next_to(sign32, DOWN*1.5)
        sign43 =  MathTex(r"-", color="RED").scale(0.8).next_to(sign33, DOWN*2.5)

        self.play(Create(NumLine), Create(tick1), Create(tick2), Write(label1), Write(label2))
        self.wait(3)
        self.play(Write(factor1))
        self.wait(3)
        self.play(Write(sign11), Write(sign12), Write(sign13))
        self.wait(3)
        self.play(Write(factor2))
        self.wait(3)
        self.play(Write(sign21), Write(sign22), Write(sign23))
        self.wait(3)
        self.play(Write(factor3))
        self.wait(3)
        self.play(Write(sign31), Write(sign32), Write(sign33))
        self.wait(5)
        self.play(Write(factor4))
        self.wait(5)
        self.play(Write(sign41), Write(sign42), Write(sign43))

        self.wait(7)
        self.play(Transform(caption1, caption2))
        self.wait(7)
        self.play(Transform(caption1, caption3))
        self.wait(7)
        self.play(Transform(caption1, caption4))
        self.wait(7)
        self.play(Transform(caption1, caption5))
        self.wait(7)
        self.play(Transform(caption1, caption6))
        self.wait(7)
        self.play(Transform(caption1, caption7))


        self.wait(10)        


       



class PlotGraph(Scene):
    def construct(self):


        #title1 = MathTex(r"\text{Find the absolute extrema of } f(x)=x+2\sin(x) \text{ on } [0, 3\pi]").scale(0.8)        
        #title1.to_edge(UP)

        axes = Axes(x_range=[-2,2,0.5], y_range=[-2,2,0.5], x_length=6, y_length=6,)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[-2,2,0.5], 
            y_range=[-2,2,0.5], 
            x_length=6,
            y_length=6,
            ).add_coordinates()

        
        P1=Dot(axes.coords_to_point(0, 0), color=PURPLE)
        label1 = MathTex(r"(0,0)", color=PURPLE).scale(0.5).next_to(P1, UP)

        P2=Dot(axes.coords_to_point(1, 1), color=BLUE)
        label2 = MathTex(r"(1,1 )", color=BLUE).scale(0.5).next_to(P2, 0.707*(UP+RIGHT))

        P3=Dot(axes.coords_to_point(2/3, 16/27), color=RED)
        label3 = MathTex(r"\left(\frac{2}{3}, \frac{16}{27} \right)", color=RED).scale(0.5).next_to(P3, RIGHT)


        
        

        theplot = axes.plot(lambda x: 4*x**3-3*x**4, 
            x_range=[-0.691, 1.522], 
            use_smoothing=False,
            color=YELLOW)

        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        self.play(Create(theplot))
        self.wait(7)
        
        self.play(Create(P1), Create(P2) )
        self.wait(10)
        self.play(Create(P3),)
        self.wait(10)
        self.play(Write(label1), Write(label2), Write(label3), )
        self.wait(10)




        
        



        


        
        



        



  
       