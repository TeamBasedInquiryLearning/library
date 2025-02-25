#%%manim -ql LIPoly

from manim import *







class FindLinear(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Suppose  } p(6)=17, p'(6)=2, p''(6)<0.", color=TEAL).scale(0.8).to_edge(UP)
        title2 = MathTex(r"\text{Find the linearization of }p(x)\text{ when }x=6.", color=TEAL).scale(0.8).next_to(title1, DOWN)

         
        
        eq1 = MathTex(r"=").scale(0.8).shift(UP*1+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*3)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*3)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*3)




        lhs1 = MathTex(r"p(6)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"17").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"p'(2)").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"2").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"L(x)").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r" m(x-x_0)+y_0", r"=2(x-6)+17", r"=2x+5").scale(0.8).next_to(eq3, RIGHT)
        

        
                
        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(title2))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Write(lhs3))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3[0]))
        self.wait(2)
        self.play(Write(rhs3[1]))
        self.wait(3)
        self.play(Write(rhs3[2]))
        self.wait(5)
        self.play(FadeOut(lhs1, eq1, rhs1, lhs2, eq2, rhs2, lhs3, eq3, rhs3, ))

        title2a = MathTex(r"\text{Find the differential }dy\text{ when }x=6.", color=TEAL).scale(0.8).next_to(title1, DOWN)

        lhs1 = MathTex(r"\frac{dy}{dx}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"p'(x)").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"dy").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"p'(x)dx").scale(0.8).next_to(eq2, RIGHT)
        rhs2a = MathTex(r"p'(6)dx").scale(0.8).next_to(eq2, RIGHT)
        rhs2b = MathTex(r"2dx").scale(0.8).next_to(eq2, RIGHT)
        

        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Transform(title2, title2a))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Transform(rhs2, rhs2a))
        self.wait(3)
        self.play(Transform(rhs2, rhs2b))
        self.wait(5)
        self.play(FadeOut(lhs1, eq1, rhs1, lhs2, eq2, rhs2, ))

        title2b = MathTex(r"\text{Estimate } p(5.97).", color=TEAL).scale(0.8).next_to(title1, DOWN)

        eq1 = MathTex(r"=").scale(0.8).shift(UP*1+LEFT*2)
        eq2 = MathTex(r"\approx").scale(0.8).next_to(eq1, DOWN*3)
        eq3 = MathTex(r"\approx").scale(0.8).next_to(eq2, DOWN*3)
        eq4 = MathTex(r"\approx").scale(0.8).next_to(eq3, DOWN*3)

        lhs1 = MathTex(r"dx").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"5.97-6=-0.03").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"dy").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"2dx", r"=2(-0.03)", r"=-0.06").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"p(5.97)").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"p(6)+dy", r"=17-0.06", r"=16.94").scale(0.8).next_to(eq3, RIGHT)

        lhs4 = MathTex(r"p(5.97)").scale(0.8).next_to(eq4, LEFT)
        rhs4 = MathTex(r"L(5.97)", r"=2(5.97)+5", r"=16.94").scale(0.8).next_to(eq4, RIGHT)

        caption1 = MathTex(r"p(5.97)\approx16.94\text{ is an overestimate since  }  p''(6)<0.", color=YELLOW).scale(0.8).to_edge(DOWN)
        

        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Transform(title2, title2b))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
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
        self.wait(5)
        self.play(Write(caption1))
        self.wait(5)






class ShowTanLine(Scene):
    def construct(self):   

        title1 = MathTex(r"\text{The linearization of } p(x) \text{ at }(6,17).").scale(0.8)        
        title1.to_edge(UP)
        title1.set_color(TEAL)     



        axes = Axes(x_range=[5.95,6.05,0.05], y_range=[16.85, 17.1, 0.1], x_length=6, y_length=6,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[5.95,6.05,0.05], y_range=[16.85, 17.1, 0.1], x_length=6, y_length=6,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        #L1 = DashedLine(axes.coords_to_point(-5, 2/3), axes.coords_to_point(1, 2/3), color="RED")

        
        

        plot1 = axes.plot(lambda x:( -8*(x-6)**2+2*x+5 ), 
            x_range=[5.95, 6.05], 
            use_smoothing=True,
            color=YELLOW)

        plotlabel = MathTex("y=p(x)").scale(0.5).next_to(plot1, RIGHT, buff=0.5).set_color(YELLOW)

        line1 = DashedLine( axes.c2p(5.95,16.9) , axes.c2p(6.05, 17.1), color=PURPLE)
        linelabel = MathTex("y=2(x-6)+17").scale(0.5).next_to(line1, LEFT, buff=0.5).set_color(PURPLE)


        P1=Dot(axes.coords_to_point(6, 17), color=WHITE)
        label1 = MathTex(r"(6,17)", color=WHITE).scale(0.5).next_to(P1, RIGHT)

        P2=Dot(axes.coords_to_point(5.97, 16.94), color=RED)
        label2 = MathTex(r"(5.97, 16.94)", color=RED).scale(0.5).next_to(P2, UP)

        P3=Dot(axes.coords_to_point(5.97, 16.9328), color=BLUE)
        label3 = MathTex(r"(5.97, p(5.97))", color=BLUE).scale(0.5).next_to(P3, RIGHT)


        self.add(title1)
        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        self.play(Create(P1), Write(label1),)
        self.wait(5)
        self.play(Create(line1), Write(linelabel),)
        self.wait(5)
        #self.play(Create(L1))
        self.play(Create(plot1), Write(plotlabel) )
        self.play(Create(P2), Write(label2),)
        self.play(Create(P3), Write(label3),)
        
        self.wait(20)
        
        

        



        



  
       