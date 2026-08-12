#%%manim -ql LIPoly

from manim import *





class Graph(Scene):
    def construct(self):   

        title1 = MathTex(r"\text{Find  the } \textbf{total} \text{ area between }y=-x^2+4x+12\text{ and the }x-\text{axis on }[-1,8].", color=TEAL).scale(0.6).to_edge(UP)



        axes = Axes(x_range=[-2,9,2], y_range=[-25, 20, 10], x_length=5, y_length=5,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        axes_labels2 = axes.get_axis_labels(MathTex("u").scale(0.5), MathTex("y").scale(0.5))
        axes_labels3 = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))

        numberplane = NumberPlane(x_range=[-2,9,2], y_range=[-25, 20, 10], x_length=5, y_length=5,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        #L1 = DashedLine(axes.coords_to_point(-5, 2/3), axes.coords_to_point(1, 2/3), color="RED")

        
        

        plot1 = axes.plot(lambda x:( -1*x**2+4*x+12 ), 
            x_range=[-1, 6], 
            use_smoothing=True,
            color=BLUE)

        plot2 = axes.plot(lambda x:( -1*x**2+4*x+12 ), 
            x_range=[6, 8], 
            use_smoothing=True,
            color=RED)

        area1 = axes.get_area(graph=plot1, x_range=[-1,6], color=BLUE)

        area2 = axes.get_area(graph=plot2, x_range=[6,8], color=RED)

        




        
        self.add(title1)
        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        #self.play(Create(L1))
        self.play(Create(plot1), )
        self.play(Create(plot2), )
        self.wait(3)
        self.play(Create(area1), Create(area2))
        self.wait(5)
        

       
        self.wait(10)   





class FindArea(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the } \textbf{total} \text{ area between }y=-x^2+4x+12\text{ and the }x-\text{axis.}", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*4)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\text{Area}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\text{Area over }x-\text{axis}", r"+", r"\text{Area under }x-\text{axis}").scale(0.8).next_to(eq1, RIGHT)
        rhs1[0].set_color(BLUE)
        rhs1[2].set_color(RED)
        rhs1a = MathTex(r"\displaystyle \int_{-1}^{6} \left|-x^2+4x+12\right|\, dx", r"+", r"\displaystyle \int_{6}^{8} \left| -x^2+4x+12 \right|\, dx").scale(0.8).next_to(eq1, RIGHT)
        rhs1a[0].set_color(BLUE)
        rhs1a[2].set_color(RED)

        rhs2 = MathTex(r"\displaystyle \int_{-1}^{6} -x^2+4x+12\, dx", r"+", r"\displaystyle \int_{6}^{8} x^2-4x-12\, dx").scale(0.8).next_to(eq2, RIGHT)
        rhs2[0].set_color(BLUE)
        rhs2[2].set_color(RED)

        rhs3 = MathTex(r"(-\frac{1}{3}x^3+\frac{4}{2}x^2+12x|_{x=-1}^{x=6})", r"+", r"(\frac{1}{3}x^3-\frac{4}{2}x^2-12x|_{x=6}^{x=8})").scale(0.8).next_to(eq3, RIGHT)
        rhs3[0].set_color(BLUE)
        rhs3[2].set_color(RED)

        rhs3a = MathTex(r"(-\frac{1}{3}x^3+2x^2+12x|_{x=-1}^{x=6})", r"+", r"(\frac{1}{3}x^3-2x^2-12x|_{x=6}^{x=8})").scale(0.8).next_to(eq3, RIGHT)
        rhs3a[0].set_color(BLUE)
        rhs3a[2].set_color(RED)

        
        

        rhs4 = MathTex(r"\left( 72 - \left(-\frac{29}{3} \right)\right)", r"+", r"\left(-\frac{160}{3} -(-72) \right)").scale(0.8).next_to(eq4, RIGHT)
        rhs4[0].set_color(BLUE)
        rhs4[2].set_color(RED)

        rhs4a = MathTex(r"\left( \frac{245}{3}\right) ", r"+", r"\left( \frac{56}{3} \right)").scale(0.8).next_to(eq4, RIGHT)
        rhs4a[0].set_color(BLUE)
        rhs4a[2].set_color(RED)

        rhs4b = MathTex(r" \frac{301}{3}").scale(0.8).next_to(eq4, RIGHT)
        


        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1),)
        self.wait(5)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Transform(rhs1, rhs1a))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(5)
        self.play(Transform(rhs4, rhs4b))
        self.wait(5)
        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4, title1)
            )
        self.wait(2)



class FindArea(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the } \textbf{total} \text{ area between }y=-x^2+4x+12\text{ and the }x-\text{axis.}", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*4)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\text{Area}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\text{Area over }x-\text{axis}", r"+", r"\text{Area under }x-\text{axis}").scale(0.8).next_to(eq1, RIGHT)
        rhs1[0].set_color(BLUE)
        rhs1[2].set_color(RED)
        rhs1a = MathTex(r"\displaystyle \int_{-1}^{6} \left|-x^2+4x+12\right|\, dx", r"+", r"\displaystyle \int_{6}^{8} \left| -x^2+4x+12 \right|\, dx").scale(0.8).next_to(eq1, RIGHT)
        rhs1a[0].set_color(BLUE)
        rhs1a[2].set_color(RED)

        rhs2 = MathTex(r"\displaystyle \int_{-1}^{6} -x^2+4x+12\, dx", r"+", r"\displaystyle \int_{6}^{8} x^2-4x-12\, dx").scale(0.8).next_to(eq2, RIGHT)
        rhs2[0].set_color(BLUE)
        rhs2[2].set_color(RED)

        rhs3 = MathTex(r"\left(-\frac{1}{3}x^3+\frac{4}{2}x^2+12x|_{x=-1}^{x=6}\right)", r"+", r"\left(\frac{1}{3}x^3-\frac{4}{2}x^2-12x|_{x=6}^{x=8}\right)").scale(0.8).next_to(eq3, RIGHT)
        rhs3[0].set_color(BLUE)
        rhs3[2].set_color(RED)

        rhs3a = MathTex(r"\left(-\frac{1}{3}x^3+2x^2+12x|_{x=-1}^{x=6}\right)", r"+", r"\left(\frac{1}{3}x^3-2x^2-12x|_{x=6}^{x=8}\right)").scale(0.8).next_to(eq3, RIGHT)
        rhs3a[0].set_color(BLUE)
        rhs3a[2].set_color(RED)

        
        

        rhs4 = MathTex(r"\left( 72 - \left(-\frac{29}{3} \right)\right)", r"+", r"\left(-\frac{160}{3} -(-72) \right)").scale(0.8).next_to(eq4, RIGHT)
        rhs4[0].set_color(BLUE)
        rhs4[2].set_color(RED)

        rhs4a = MathTex(r"\left( \frac{245}{3}\right) ", r"+", r"\left( \frac{56}{3} \right)").scale(0.8).next_to(eq4, RIGHT)
        rhs4a[0].set_color(BLUE)
        rhs4a[2].set_color(RED)

        rhs4b = MathTex(r" \frac{301}{3}").scale(0.8).next_to(eq4, RIGHT)
        


        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1),)
        self.wait(5)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Transform(rhs1, rhs1a))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(5)
        self.play(Transform(rhs4, rhs4b))
        self.wait(10)
        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4, title1)
            )
             

class FindInt(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the } \textbf{net} \text{ area between }y=-x^2+4x+12\text{ and the }x-\text{axis.}", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\text{Signed Area}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \int_{-1}^{8} -x^2+4x+12\, dx",).scale(0.8).next_to(eq1, RIGHT)


        rhs2 = MathTex(r"\left(-\frac{1}{3}x^3+\frac{4}{2}x^2+12x|_{x=-1}^{x=8}\right)",).scale(0.8).next_to(eq2, RIGHT)

        rhs2a = MathTex(r"\left(-\frac{1}{3}x^3+2x^2+12x|_{x=-1}^{x=8}\right)", ).scale(0.8).next_to(eq2, RIGHT)

        
        

        rhs3 = MathTex(r"\frac{160}{3} - \left(-\frac{29}{3} \right)", ).scale(0.8).next_to(eq3, RIGHT)


        rhs4 = MathTex(r"63.").scale(0.8).next_to(eq4, RIGHT)
        


        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1),)
        self.wait(5)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Transform(rhs2, rhs2a))
        
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Write(rhs4), Write(eq4))
        self.wait(10)
        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, eq4, rhs4,  title1)
            )
        