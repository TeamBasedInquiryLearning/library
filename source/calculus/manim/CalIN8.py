#%%manim -ql LIPoly

from manim import *





class Graph(Scene):
    def construct(self):   

        title1 = MathTex(r"\text{Find  the }  \text{area bound by }y=-x^2+5, y=-x-1, y=-4x+5, y=2x-1.", color=TEAL).scale(0.6).to_edge(UP)



        axes = Axes(x_range=[-4,4,2], y_range=[-2, 6, 2], x_length=5, y_length=5,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))

        numberplane = NumberPlane(x_range=[-4,4,2], y_range=[-2, 6, 2], x_length=5, y_length=5,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        #L1 = DashedLine(axes.coords_to_point(-5, 2/3), axes.coords_to_point(1, 2/3), color="RED")

        
        

        plot1 = axes.plot(lambda x:( -1*x**2+5 ), 
            x_range=[-2.64,2.64],
            use_smoothing=True,
            color=YELLOW)

        plot2 = axes.plot(lambda x:( -1*x-1 ), 
            x_range=[-4, 1], 
            use_smoothing=True,
            color=YELLOW)

        plot3 = axes.plot(lambda x:( -4*x+5 ), 
            x_range=[-0.25, 1.75], 
            use_smoothing=True,
            color=YELLOW)

        plot4 = axes.plot(lambda x:( 2*x-1 ), 
            x_range=[-0.5, 3.5], 
            use_smoothing=True,
            color=YELLOW)

        plot1a = axes.plot(lambda x:( -1*x**2+5 ), 
            x_range=[-2,0],
            use_smoothing=True,
            color=YELLOW)

        plot2a = axes.plot(lambda x:( -1*x-1 ), 
            x_range=[-2,0], 
            use_smoothing=True,
            color=YELLOW)

        plot3a = axes.plot(lambda x:( -4*x+5 ), 
            x_range=[-0,1], 
            use_smoothing=True,
            color=YELLOW)

        plot4a = axes.plot(lambda x:( 2*x-1 ), 
            x_range=[0,1], 
            use_smoothing=True,
            color=YELLOW)

        area1 = axes.get_area(graph=plot1, x_range=[-2,0], color=YELLOW, bounded_graph=plot2)
        area2 = axes.get_area(graph=plot3, x_range=[0,1], color=YELLOW, bounded_graph=plot4)

        label1 = MathTex("y=-x^2+5").scale(0.5).next_to(axes.c2p(-1.25,3), (LEFT+UP)/2).set_color(YELLOW)
        label2 = MathTex("y=-x-1").scale(0.5).next_to(axes.c2p(-1,-0.25), (LEFT+DOWN)/2).set_color(YELLOW)
        label3 = MathTex("y=-4x+5").scale(0.5).next_to(axes.c2p(0.5,3.5), (RIGHT+UP)/2).set_color(YELLOW)
        label4 = MathTex("y=2x-1").scale(0.5).next_to(axes.c2p(0.25,0), (RIGHT+DOWN)/2).set_color(YELLOW)

        
        P1=Dot(axes.coords_to_point(-2, 1), color=WHITE)
        labelP1 = MathTex(r"(-2,1)", color=WHITE).scale(0.5).next_to(P1, LEFT)
        P2=Dot(axes.coords_to_point(0, 5), color=WHITE)
        labelP2 = MathTex(r"(0,5)", color=WHITE).scale(0.5).next_to(P2, RIGHT)
        P3=Dot(axes.coords_to_point(0, -1), color=WHITE)
        labelP3 = MathTex(r"(0,-1)", color=WHITE).scale(0.5).next_to(P3, DOWN)
        P4=Dot(axes.coords_to_point(1, 1), color=WHITE)
        labelP4 = MathTex(r"(1,1)", color=WHITE).scale(0.5).next_to(P4, RIGHT)



        
        self.add(title1)
        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        #self.play(Create(L1))
        self.play(Create(plot1), Create(plot2),Create(plot3),Create(plot4),)
        self.wait(3)
        self.play(Create(area1), Create(area2),)
        self.play(Transform(plot1, plot1a), Transform(plot2, plot2a), Transform(plot3, plot3a), Transform(plot4, plot4a), )
        self.wait(2)
        self.play(Write(label1), Write(label2), Write(label3), Write(label4), )       
        self.play(Create(P1), Write(labelP1), Create(P2), Write(labelP2), Create(P3), Write(labelP3), Create(P4), Write(labelP4), )
        self.wait(5) 
        self.play(plot1.animate.set_color(BLUE), area1.animate.set_color(BLUE), label1.animate.set_color(BLUE),
            plot2.animate.set_color(BLUE),  label2.animate.set_color(BLUE),)

        self.play(plot3.animate.set_color(RED), area2.animate.set_color(RED), label3.animate.set_color(RED),
            plot4.animate.set_color(RED),  label4.animate.set_color(RED),)      

        self.wait(10)





class FindArea1(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the }  \text{area bound by }y=-x^2+5, y=-x-1, y=-4x+5, y=2x-1.", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*4)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\text{Area}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\text{Area before }x=0", r"+", r"\text{Area after }x=0").scale(0.8).next_to(eq1, RIGHT)
        rhs1[0].set_color(BLUE)
        rhs1[2].set_color(RED)
        rhs1a = MathTex(r"\displaystyle \int_{-2}^{0} \left(\left(-x^2+5\right) - \left(-x-1\right) \right)\, dx", r"+", r"\displaystyle \int_{0}^{1} \left(\left(-4x+5\right) - \left(2x-1\right) \right) dx").scale(0.6).next_to(eq1, RIGHT)
        rhs1a[0].set_color(BLUE)
        rhs1a[2].set_color(RED)

        rhs2 = MathTex(r"\displaystyle \int_{-2}^{0} -x^2+x+6\, dx", r"+", r"\displaystyle \int_{0}^{1} -6x+6 dx").scale(0.8).next_to(eq2, RIGHT)
        rhs2[0].set_color(BLUE)
        rhs2[2].set_color(RED)

        rhs3 = MathTex(r"\left(-\frac{1}{3}x^3+\frac{1}{2}x^2+6x|_{x=-2}^{x=0}\right)", r"+", r"\left(-\frac{6}{2}x^2+6x|_{x=0}^{x=1}\right)").scale(0.8).next_to(eq3, RIGHT)
        rhs3[0].set_color(BLUE)
        rhs3[2].set_color(RED)

        rhs3a = MathTex(r"\left(-\frac{1}{3}x^3+\frac{1}{2}x^2+6x|_{x=-2}^{x=0}\right)", r"+", r"\left(-3x^2+6x|_{x=0}^{x=1}\right)").scale(0.8).next_to(eq3, RIGHT)
        rhs3a[0].set_color(BLUE)
        rhs3a[2].set_color(RED)

        
        

        rhs4 = MathTex(r"\left(0 - \left(-\frac{22}{3} \right)\right)", r"+", r"\left(3-0 \right)").scale(0.8).next_to(eq4, RIGHT)
        rhs4[0].set_color(BLUE)
        rhs4[2].set_color(RED)

        

        rhs4a = MathTex(r" \frac{31}{3}").scale(0.8).next_to(eq4, RIGHT)
        


        
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
        self.wait(3)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10)
        
        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4, title1)
            )


class Graph2(Scene):
    def construct(self):   

        title1 = MathTex(r"\text{Find  the }  \text{area bound by }y=-x^2+5, y=-x-1, y=-4x+5, y=2x-1.", color=TEAL).scale(0.6).to_edge(UP)



        axes = Axes(x_range=[-4,4,2], y_range=[-2, 6, 2], x_length=5, y_length=5,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))

        numberplane = NumberPlane(x_range=[-4,4,2], y_range=[-2, 6, 2], x_length=5, y_length=5,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        #L1 = DashedLine(axes.coords_to_point(-5, 2/3), axes.coords_to_point(1, 2/3), color="RED")

        
        

        

        plot1 = axes.plot(lambda x:( -1*x**2+5 ), 
            x_range=[-2,0],
            use_smoothing=True,
            color=YELLOW)

        plot2 = axes.plot(lambda x:( -1*x-1 ), 
            x_range=[-2,0], 
            use_smoothing=True,
            color=YELLOW)

        plot3 = axes.plot(lambda x:( -4*x+5 ), 
            x_range=[-0,1], 
            use_smoothing=True,
            color=YELLOW)

        plot4 = axes.plot(lambda x:( 2*x-1 ), 
            x_range=[0,1], 
            use_smoothing=True,
            color=YELLOW)

        dummy = axes.plot(lambda x:( 1 ), 
            x_range=[-2,1], 
            use_smoothing=True,
            color=YELLOW)

        area1 = axes.get_area(graph=plot1, x_range=[-2,0], color=YELLOW, bounded_graph=dummy)
        area2 = axes.get_area(graph=plot2, x_range=[-2,0], color=YELLOW, bounded_graph=dummy)
        area3 = axes.get_area(graph=plot3, x_range=[0,1], color=YELLOW, bounded_graph=dummy)
        area4 = axes.get_area(graph=plot4, x_range=[0,1], color=YELLOW, bounded_graph=dummy)

        label1 = MathTex("y=-x^2+5").scale(0.5).next_to(axes.c2p(-1.25,3), (LEFT+UP)/2).set_color(YELLOW)
        label2 = MathTex("y=-x-1").scale(0.5).next_to(axes.c2p(-1,-0.25), (LEFT+DOWN)/2).set_color(YELLOW)
        label3 = MathTex("y=-4x+5").scale(0.5).next_to(axes.c2p(0.5,3.5), (RIGHT+UP)/2).set_color(YELLOW)
        label4 = MathTex("y=2x-1").scale(0.5).next_to(axes.c2p(0.25,0), (RIGHT+DOWN)/2).set_color(YELLOW)

        label1a = MathTex(r"x=-\sqrt{5-y}").scale(0.5).next_to(axes.c2p(-1.25,3), (LEFT+UP)/2).set_color(YELLOW)
        label2a = MathTex(r"x=-y-1").scale(0.5).next_to(axes.c2p(-1,-0.25), (LEFT+DOWN)/2).set_color(YELLOW)
        label3a = MathTex(r"x=\frac{5-y}{4}").scale(0.5).next_to(axes.c2p(0.5,3), (RIGHT+UP)/2).set_color(YELLOW)
        label4a = MathTex(r"x=\frac{y+1}{2}").scale(0.5).next_to(axes.c2p(0.25,0), (RIGHT+DOWN)/2).set_color(YELLOW)

        
        P1=Dot(axes.coords_to_point(-2, 1), color=WHITE)
        labelP1 = MathTex(r"(-2,1)", color=WHITE).scale(0.5).next_to(P1, LEFT)
        P2=Dot(axes.coords_to_point(0, 5), color=WHITE)
        labelP2 = MathTex(r"(0,5)", color=WHITE).scale(0.5).next_to(P2, RIGHT)
        P3=Dot(axes.coords_to_point(0, -1), color=WHITE)
        labelP3 = MathTex(r"(0,-1)", color=WHITE).scale(0.5).next_to(P3, DOWN)
        P4=Dot(axes.coords_to_point(1, 1), color=WHITE)
        labelP4 = MathTex(r"(1,1)", color=WHITE).scale(0.5).next_to(P4, RIGHT)



        
        self.add(title1)
        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        #self.play(Create(L1))
        self.play(Create(plot1), Create(plot2),Create(plot3),Create(plot4),)
        self.play(Create(area1), Create(area2), Create(area3), Create(area4))

        self.play(Write(label1), Write(label2), Write(label3), Write(label4), )       
        self.play(Create(P1), Write(labelP1), Create(P2), Write(labelP2), Create(P3), Write(labelP3), Create(P4), Write(labelP4), )
        self.wait(5)
        self.play(Transform(label1, label1a), Transform(label2, label2a), Transform(label3, label3a), Transform(label4, label4a), )
        self.wait(3) 
        self.play(plot1.animate.set_color(BLUE), area1.animate.set_color(BLUE), label1.animate.set_color(BLUE),
            plot3.animate.set_color(BLUE), area3.animate.set_color(BLUE),  label3.animate.set_color(BLUE),)

        self.play(plot2.animate.set_color(RED), area2.animate.set_color(RED), label2.animate.set_color(RED),
            plot2.animate.set_color(RED),  area4.animate.set_color(RED), label4.animate.set_color(RED),)      

        self.wait(10)   






class FindArea2(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the }  \text{area bound by }y=-x^2+5, y=-x-1, y=-4x+5, y=2x-1.", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*4)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\text{Area}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\text{Area before }y=1", r"+", r"\text{Area after }y=1").scale(0.8).next_to(eq1, RIGHT)
        rhs1[0].set_color(BLUE)
        rhs1[2].set_color(RED)
        rhs1a = MathTex(r"\displaystyle \int_{-1}^{1} \left(\left(\frac{1}{2}y+\frac{1}{2}\right) - \left(-y-1\right) \right)\, dy", r"+", r"\displaystyle \int_{1}^{5} \left(\left(\frac{5}{4}-\frac{1}{4}y\right) - \left(-\sqrt{5-y}\right) \right)\, dy").scale(0.6).next_to(eq1, RIGHT)
        rhs1a[0].set_color(BLUE)
        rhs1a[2].set_color(RED)

        rhs2 = MathTex(r"\displaystyle \int_{-1}^{1} \frac{3}{2}y+\frac{3}{2} \, dy", r"+", r"\displaystyle \int_{1}^{5} \frac{5}{4}-\frac{1}{4}y+\sqrt{5-y}\, dy").scale(0.8).next_to(eq2, RIGHT)
        rhs2[0].set_color(BLUE)
        rhs2[2].set_color(RED)

        rhs3 = MathTex(r"\left(-\frac{3}{4}y^2-\frac{3}{2}y|_{y=-1}^{y=1}\right)", r"+", r"\left(\frac{5}{4}y-\frac{1}{8}y^2-\frac{2}{3}(5-y)^{3/2}|_{x=0}^{x=1}\right)").scale(0.8).next_to(eq3, RIGHT)
        rhs3[0].set_color(BLUE)
        rhs3[2].set_color(RED)


        
        

        rhs4 = MathTex(r"\left(\frac{3}{4} - \left(-\frac{9}{4} \right)\right)", r"+", r"\left(\frac{25}{8}-\left( -\frac{101}{24}\right) \right)").scale(0.8).next_to(eq4, RIGHT)
        rhs4[0].set_color(BLUE)
        rhs4[2].set_color(RED)

        

        rhs4a = MathTex(r" \frac{31}{3}").scale(0.8).next_to(eq4, RIGHT)
        


        
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
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(3)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10)
        
        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4, title1)
            )             


        