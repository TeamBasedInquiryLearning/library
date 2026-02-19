#%%manim -ql LIPoly

from manim import *



class EstimateDerivative(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Estimate }g'(-1)\text{ if } g(-1)=2.1, g(-1.5)=1.9.").scale(0.8)        
        title1.to_edge(UP)

        eq1 = MathTex(r"\approx", ).scale(0.7).shift(RIGHT*3+UP*2)
        eq2 = MathTex(r"=", ).scale(0.7).next_to(eq1, DOWN*4)
        
        lhs = MathTex(r"g'(-1)", ).scale(0.7).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{g(-1)-g(-1.5)}{-1-(-1.5)}", ).scale(0.7).next_to(eq1, RIGHT)
        rhs2 = MathTex(r"\frac{2.1-1.9}{-1-(-1.5)}", ).scale(0.7).next_to(eq2, RIGHT)
        rhs3 = MathTex(r"\frac{0.2}{0.5}", ).scale(0.7).next_to(eq2, RIGHT)
        rhs4 = MathTex(r"0.4", ).scale(0.7).next_to(eq2, RIGHT)
        

        
        

        axes = Axes(x_range=[-3,1,1], y_range=[-1,3,1], x_length=4.2, y_length=4.2,).shift(LEFT*3)
        axes_labels = axes.get_axis_labels()
        numberplane = NumberPlane(x_range=[-3,1,1], 
            y_range=[-1,3,1], 
            x_length=4.2,
            y_length=4.2,
            ).add_coordinates().shift(LEFT*3)

        

        
        p1 = Dot(axes.coords_to_point(-1, 2.1), color=RED)
        p2 = Dot(axes.coords_to_point(-1.5, 1.9), color=RED)
        d = DashedLine(axes.coords_to_point(-3, 1.3), axes.coords_to_point(1, 2.9), color=BLUE)
        


        




        



        #self.add_fixed_in_frame_mobjects(title)
        self.add(axes, axes_labels, numberplane, title1)
        self.play(Create(p1), Create(p2))
        self.wait(4)
        self.play(Create(d))
        self.wait(4)
        self.play(Write(lhs))
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(4)
        self.play(Write(eq2), Write(rhs2))
        self.wait(4)
        self.play(Transform(rhs2, rhs3))
        self.wait(4)
        self.play(Transform(rhs2, rhs4))
        self.wait(5)







class ShowFunction(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Sketch  }y=f(x)\text{ such that:}").scale(0.8)        
        title1.to_edge(UP)

        text1 = MathTex(r"\text{Defined and continuous on }[-10, 10].}", ).scale(0.6).shift(RIGHT*3+UP*2)
        text2 = MathTex(r"\displaystyle \lim_{h\to 0}\frac{f(-4+h)-f(-4)}{h}<0.", color=GREEN).scale(0.6).next_to(text1, DOWN*2)
        text3 = MathTex(r"f'(x)\text{ does not exist when }x=-1.", color=RED).scale(0.6).next_to(text2, DOWN*2)
        text4 = MathTex(r"\text{The rate of change of }f(x) \text{ when }x=1\text{ is positive}.", color=ORANGE).scale(0.6).next_to(text3, DOWN*2)
        text5 = MathTex(r"\text{The slope tangent to the graph }y=f(x)\text{ at }x=-3\text{ is zero}.", color=PURPLE).scale(0.6).next_to(text4, DOWN*2)


        text2a = MathTex(r"f'(-4)<0.", color=GREEN).scale(0.6).next_to(text1, DOWN*2)
        text4a = MathTex(r"f'(1)>0.", color=ORANGE).scale(0.6).next_to(text3, DOWN*2)
        text5a = MathTex(r"f'(-3)=0.", color=PURPLE).scale(0.6).next_to(text4, DOWN*2)

        
        

        axes = Axes(x_range=[-11,11,5], y_range=[-1,15,5], x_length=4.2, y_length=4.2,).shift(LEFT*4)
        axes_labels = axes.get_axis_labels()
        numberplane = NumberPlane(x_range=[-11,11,5], y_range=[-1,15,5],
            x_length=4.2,
            y_length=4.2,
            ).add_coordinates().shift(LEFT*4)

        

        
        d2 = DashedLine(axes.coords_to_point(-4, -1), axes.coords_to_point(-4, 15))
        d3 = DashedLine(axes.coords_to_point(-1, -1), axes.coords_to_point(-1, 15))
        d4 = DashedLine(axes.coords_to_point(1, -1), axes.coords_to_point(1, 15))
        d5 = DashedLine(axes.coords_to_point(-3, -1), axes.coords_to_point(-3, 15))






        #First x

        tracker1=ValueTracker(0)

        l2 = DashedLine(axes.coords_to_point(-11, 3), axes.coords_to_point(-1, -1), color=GREEN)
        l5 = DashedLine(axes.coords_to_point(-11, 0), axes.coords_to_point(11, -0), color=PURPLE)
        l4 = DashedLine(axes.coords_to_point(-8, -1), axes.coords_to_point(11, 2.8), color=ORANGE)

        def updatel2(mob):
            mob.become(
                DashedLine(axes.coords_to_point(-11, 3+tracker1.get_value()), 
                    axes.coords_to_point(-1, -1+tracker1.get_value()), 
                    color=GREEN)
                
        )
        

        l2.add_updater(updatel2)

        def updatel4(mob):
            mob.become(
                DashedLine(axes.coords_to_point(-8, -1+tracker1.get_value()), axes.coords_to_point(11, 2.8+tracker1.get_value()), color=ORANGE)
                
        )
        

        l4.add_updater(updatel4)


        def updatel5(mob):
            mob.become(
                DashedLine(axes.coords_to_point(-11, 0+tracker1.get_value()), axes.coords_to_point(11, -0+tracker1.get_value()), color=PURPLE)
                
        )
        

        l5.add_updater(updatel5)




        curve1 = axes.plot(lambda x: (x+3)**2/5, 
            x_range=[-10, -1], 
            use_smoothing=True,
            color=YELLOW)

        
        def updatecurve1(mob):
            mob.become(
                axes.plot(lambda x: (x+3)**2/5+tracker1.get_value(), 
            x_range=[-10, -1], 
            use_smoothing=True,
            color=YELLOW)
                
        )
        

        curve1.add_updater(updatecurve1)




        curve2 = axes.plot(lambda x: (x)**2/10+0.7, 
            x_range=[-1, 10], 
            use_smoothing=True,
            color=YELLOW)

        
        def updatecurve2(mob):
            mob.become(
                axes.plot(lambda x: (x)**2/10+0.7+tracker1.get_value(), 
            x_range=[-1, 10], 
            use_smoothing=True,
            color=YELLOW)
                
        )

        curve2.add_updater(updatecurve2)



        P2=Dot(axes.coords_to_point(-4, 0.2))
        def updateP2(mob):
            mob.become(
                Dot(axes.coords_to_point(-4, 0.2+tracker1.get_value())).scale(0.7)
                
        )
        P2.add_updater(updateP2)

        P3=Dot(axes.coords_to_point(-1, 0.8))
        def updateP3(mob):
            mob.become(
                Dot(axes.coords_to_point(-1, 0.8+tracker1.get_value())).scale(0.7)
                
        )
        P3.add_updater(updateP3) 

        P4=Dot(axes.coords_to_point(1, 0.8))
        def updateP4(mob):
            mob.become(
                Dot(axes.coords_to_point(1, 0.8+tracker1.get_value())).scale(0.7)
                
        )
        P4.add_updater(updateP4)

        P5=Dot(axes.coords_to_point(-3, 0))
        def updateP5(mob):
            mob.become(
                Dot(axes.coords_to_point(-3, 0+tracker1.get_value())).scale(0.7)
                
        )
        P5.add_updater(updateP5)
        




        



        #self.add_fixed_in_frame_mobjects(title)
        self.add(axes, axes_labels, numberplane, title1)
        self.play(Write(text1), Write(text2), Write(text3), Write(text4), Write(text5), )
        self.wait(5)
        self.play(Transform(text2, text2a))
        self.wait(5)
        self.play(Transform(text4, text4a))
        self.wait(5)
        self.play(Transform(text5, text5a))
        self.wait(5)
        self.play(text2.animate.scale(1.5))
        self.play(text2.animate.scale(2/3))
        self.wait(1)
        self.play(Create(d2), Create(l2), Create(P2))
        self.wait(3)
        
        self.play(text3.animate.scale(1.5))
        self.play(text3.animate.scale(2/3))
        self.wait(1)
        self.play(Create(d3), Create(P3))
        self.wait(3)

        self.play(text4.animate.scale(1.5))
        self.play(text4.animate.scale(2/3))
        self.wait(1)
        self.play(Create(d4), Create(l4), Create(P4))
        self.wait(3)

        self.play(text5.animate.scale(1.5))
        self.play(text5.animate.scale(2/3))
        self.wait(1)
        self.play(Create(d5), Create(l5), Create(P5))
        self.wait(5)
        self.play(Create(curve1))
        self.play(Create(curve2))
        self.play(FadeOut(d2, d3, d4, d5))
        self.wait(5)

        self.play(tracker1.animate.set_value(5), run_time=4)
        self.play(tracker1.animate.set_value(0), run_time=4)
        self.wait(5)

       





        
        



        


        
        



        



  
       