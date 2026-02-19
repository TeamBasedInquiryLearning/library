#%%manim -ql LIPoly

from manim import *







class FindTanLine(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the line tangent to  } y=h(x) \text{ where }h(x)=2x^4+4x-6,\text{ at }(-2,18).", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption1 = MathTex(r"y=", r"m", r"(x-x_0)+y_0", color=YELLOW).scale(0.8).to_edge(DOWN)  
        caption2 = MathTex(r"\text{Product Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        caption3 = MathTex(r"\text{Quotient Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"h(x)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"2x^4+4x-6").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"h'(x)").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"8x^3+4").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"m", r"=h'(-2)").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"8(-2)^3+4", r"=-60").scale(0.8).next_to(eq3, RIGHT)
        

        lhs4 = MathTex(r"y").scale(0.8).next_to(eq4, LEFT)
        rhs4 = MathTex(r"m(x-x_0)+y_0").scale(0.8).next_to(eq4, RIGHT)
        rhs4a = MathTex(r"-60(x-(-2))+18").scale(0.8).next_to(eq4, RIGHT)
        rhs4b = MathTex(r"-60(x+2)+18").scale(0.8).next_to(eq4, RIGHT)
        rhs4c = MathTex(r"-60x-102").scale(0.8).next_to(eq4, RIGHT)
        
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(caption1))
        self.wait(3)
        self.play(caption1[1].animate.set_color(WHITE))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Write(lhs3[0]))
        self.wait(2)
        self.play(Write(lhs3[1]))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3[0]))
        self.wait(2)
        self.play(Write(rhs3[1]))
        self.wait(3)
        self.play(Write(lhs4), Write(eq4), Write(rhs4))
        self.wait(4)
        self.play(Transform(rhs4, rhs4a))
        self.wait(4)
        self.play(Transform(rhs4, rhs4b))
        self.wait(4)
        self.play(Transform(rhs4, rhs4c))
        self.wait(5)



class ShowTanLine(Scene):
    def construct(self):   

        title1 = MathTex(r"\text{Graph } y=2x^4+4x-6 \text{ and it's tangent line at }(-2,18).").scale(0.8)        
        title1.to_edge(UP)
        title1.set_color(TEAL)     



        axes = Axes(x_range=[-3,3,1], y_range=[-10, 25, 10], x_length=6, y_length=6,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[-3,3,1], y_range=[-10, 25, 10], x_length=6, y_length=6,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        #L1 = DashedLine(axes.coords_to_point(-5, 2/3), axes.coords_to_point(1, 2/3), color="RED")

        
        

        plot1 = axes.plot(lambda x:( 2*x**4+4*x-6 ), 
            x_range=[-2.107, 1.853], 
            use_smoothing=True,
            color=YELLOW)

        plotlabel = MathTex("h(x)=2x^4+4x-6").scale(0.5).next_to(plot1, RIGHT, buff=0.5).set_color(YELLOW)

        line1 = DashedLine( axes.c2p(-2.117, 25) , axes.c2p(-1.533, -10), color=PURPLE)
        linelabel = MathTex("y=-60x-102").scale(0.5).next_to(line1, LEFT, buff=0.5).set_color(PURPLE)


        P1=Dot(axes.coords_to_point(-2, 18), color=WHITE)
        label1 = MathTex(r"(-2,18)", color=WHITE).scale(0.5).next_to(P1, RIGHT)


        self.add(title1)
        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        #self.play(Create(L1))
        self.play(Create(plot1), Write(plotlabel) )
        self.wait(2)
        self.play(Create(P1), Write(label1),)
        self.wait(5)
        self.play(Create(line1), Write(linelabel),)
        self.wait(5)

        


class FindPosition(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{A objects position in meters after } t \text{ seconds}  ", color=TEAL).scale(0.8).to_edge(UP)
        title2 = MathTex(r"\text{is measured by }s(t)=2t^3-3t^2-7t+4.", color=TEAL).scale(0.8).next_to(title1, DOWN)
        title3 = MathTex(r"\text{Find the object's position,  velocity and acceleration at } t=3 \text{ seconds.}", color=TEAL).scale(0.8).next_to(title2, DOWN)

        caption1 = MathTex(r"\text{When } t=3\text{ seconds, the position is 10 meters.}", color=YELLOW).scale(0.8).to_edge(DOWN)  
        caption2 = MathTex(r"\text{When } t=3\text{ seconds, the velocity is 29 meters/second.}", color=YELLOW).scale(0.8).to_edge(DOWN)      
        caption3 = MathTex(r"\text{When } t=3\text{ seconds, the acceleration is 30 meters/second}^2.", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.8).shift(UP*0.5+LEFT)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"s(t)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"2t^3-3t^2-7t+4").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"v(t)", r"=s'(t)").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"6t^2-6t-7").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"a(t)", r"=v'(t)", r"=s''(t)").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"12t-6").scale(0.8).next_to(eq3, RIGHT)

        lhs1a = MathTex(r"s(3)").scale(0.8).next_to(eq1, LEFT)
        rhs1a = MathTex(r"2(3)^3-3(3)^2-7(3)+4").scale(0.8).next_to(eq1, RIGHT)

        lhs2a = MathTex(r"v(3)", r"=s'(3)").scale(0.8).next_to(eq2, LEFT)
        rhs2a = MathTex(r"6(3)^2-6(3)-7").scale(0.8).next_to(eq2, RIGHT)

        lhs3a = MathTex(r"a(3)", r"=v'(3)", r"=s''(3)").scale(0.8).next_to(eq3, LEFT)
        rhs3a = MathTex(r"12(3)-6").scale(0.8).next_to(eq3, RIGHT)

        rhs1b = MathTex(r"=10.").scale(0.8).next_to(rhs1a, RIGHT)
        rhs2b = MathTex(r"=29.").scale(0.8).next_to(rhs2a, RIGHT)
        rhs3b = MathTex(r"=30.").scale(0.8).next_to(rhs3a, RIGHT)
        

        
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1, title2, title3)
        self.wait(5)
        
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2[0]))
        self.wait(2)
        self.play(Write(lhs2[1]))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Write(lhs3[0]))
        self.wait(2)
        self.play(Write(lhs3[1]))
        self.wait(2)
        self.play(Write(lhs3[2]))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Transform(lhs1, lhs1a))
        self.wait(2)
        self.play(Transform(rhs1, rhs1a))
        self.wait(3)
        self.play(Write(rhs1b))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(5)

        self.play(Transform(lhs2, lhs2a))
        self.wait(2)
        self.play(Transform(rhs2, rhs2a))
        self.wait(3)
        self.play(Write(rhs2b))
        self.wait(3)
        self.play(Transform(caption1, caption2))
        self.wait(5)

        self.play(Transform(lhs3, lhs3a))
        self.wait(2)
        self.play(Transform(rhs3, rhs3a))
        self.wait(3)
        self.play(Write(rhs3b))
        self.wait(3)
        self.play(Transform(caption1, caption3))
        self.wait(5)

class FindMoney(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{A gizmo sells for \$47 each and}", color=TEAL).scale(0.8).to_edge(UP)
        title2 = MathTex(r"\text{the cost to produce }x \text{ gizmos in dollars is } C(x)=x^3+2x^2+9x+8", color=TEAL).scale(0.8).next_to(title1, DOWN)
        title3 = MathTex(r"\text{Find marginal revenue, cost and profit.}", color=TEAL).scale(0.8).next_to(title2, DOWN)

        caption1 = MathTex(r"\text{Marginal revenue is } R'(x)=47\text{ dollars per gizmo.}", color=YELLOW).scale(0.8).to_edge(DOWN)  
        caption2 = MathTex(r"\text{Marginal cost is } C'(x)=3x^2+4x+9\text{ dollars per gizmo.}", color=YELLOW).scale(0.8).to_edge(DOWN)      
        caption3 = MathTex(r"\text{Marginal profit is } P'(x)=38-3x^2-4x\text{ dollars per gizmo.}", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.6).shift(UP*0.5+LEFT*4)
        eq2 = MathTex(r"=").scale(0.6).next_to(eq1, DOWN*3)
        eq3 = MathTex(r"=").scale(0.6).next_to(eq2, DOWN*3)
        eq4 = MathTex(r"=").scale(0.6).next_to(eq3, DOWN*3)




        lhs1 = MathTex(r"R(x)").scale(0.6).next_to(eq1, LEFT)
        rhs1 = MathTex(r"47x").scale(0.6).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"R'(x)").scale(0.6).next_to(eq2, LEFT)
        rhs2 = MathTex(r"47").scale(0.6).next_to(eq2, RIGHT)




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1, title2, title3)
        self.wait(5)
        
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(5)
        self.play(FadeOut(lhs2, eq2, rhs2, caption1))      

        lhs2 = MathTex(r"C(x)").scale(0.6).next_to(eq2, LEFT)
        rhs2 = MathTex(r"x^3+2x^2+9x+8").scale(0.6).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"C'(x)").scale(0.6).next_to(eq3, LEFT)
        rhs3 = MathTex(r"3x^2+4x+9").scale(0.6).next_to(eq3, RIGHT)

        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Write(lhs3))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Write(caption2))
        self.wait(5)
        self.play(FadeOut(lhs3, eq3, rhs3, caption2))

        lhs3 = MathTex(r"P(x)").scale(0.6).next_to(eq3, LEFT)
        rhs3 = MathTex(r"R(x)-C(x)", r"=47x-(x^3+2x^2+9x+8)", r"=-x^3-2x^2+38x-8").scale(0.6).next_to(eq3, RIGHT)

        lhs4 = MathTex(r"P'(x)").scale(0.6).next_to(eq4, LEFT)
        rhs4 = MathTex(r"R'(x)-C'(x)", r"=47-(3x^2+4x+9)", r"=-3x^2-4x+38").scale(0.6).next_to(eq4, RIGHT)

        self.play(Write(lhs3))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3[0]))
        self.wait(3)
        self.play(Write(rhs3[1]))
        self.wait(3)
        self.play(Write(rhs3[2]))
        self.wait(3)
        self.play(Write(lhs4))
        self.wait(3)
        self.play(Write(eq4), Write(rhs4[0]))
        self.wait(3)
        self.play(Write(rhs4[1]))
        self.wait(3)
        self.play(Write(rhs4[2]))
        self.wait(3)
        self.play(Write(caption3))
        self.wait(10)



        



  
       