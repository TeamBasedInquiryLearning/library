#%%manim -ql LIPoly

from manim import *







class ShowFunction(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Sketch  }y=g(x)\text{ such that:}").scale(0.8)        
        title1.to_edge(UP)

        text1 = MathTex(r"\displaystyle \lim_{x\to 1^-}g(x) \text{ finite, }\lim_{x\to 1^+}g(x)=\infty.}", color=RED).scale(0.8).shift(RIGHT*3+UP*2)
        text2 = MathTex(r"\displaystyle \lim_{x\to -3}g(x)\neq g(-3) \text{, both exist.}", color=BLUE).scale(0.8).next_to(text1, DOWN*2)
        text3 = MathTex(r"\displaystyle \lim_{x\to -4}\neq 0, \lim_{x\to -4^+}g(x)=0.", color=YELLOW).scale(0.8).next_to(text2, DOWN*2)

        
        

        axes = Axes(x_range=[-5.1,3.1,1], y_range=[-4.1,4.1,1], x_length=4.2, y_length=4.2,).shift(LEFT*3)
        axes_labels = axes.get_axis_labels()
        numberplane = NumberPlane(x_range=[-5.1,3.1,2], 
            y_range=[-4.1,4.1,2], 
            x_length=4.2,
            y_length=4.2,
            ).add_coordinates().shift(LEFT*3)

        

        
        d1 = DashedLine(axes.coords_to_point(1, -4), axes.coords_to_point(1, 4), color=RED)
        d2 = DashedLine(axes.coords_to_point(-3, -4), axes.coords_to_point(-3, 4), color=BLUE)
        d3 = DashedLine(axes.coords_to_point(-4, -4), axes.coords_to_point(-4, 4), color=YELLOW)


        #First x

        tracker11=ValueTracker(0.5)
        tracker12=ValueTracker(0.5)
        tracker13=ValueTracker(0.5)


        curve11 = axes.plot(lambda x: 0.5, 
            x_range=[-1, 0.99], 
            use_smoothing=False)

        
        def update11(mob):
            mob.become(
                axes.plot(lambda x: tracker11.get_value(), 
            x_range=[-1, 0.99], 
            use_smoothing=False)
                
        )
        

        curve11.add_updater(update11)

        curve12 = axes.plot(lambda x: (x-1)**(-1/2)+0.5, 
            x_range=[1.0816, 3], 
            use_smoothing=False)

        
        def update12(mob):
            mob.become(
                axes.plot(lambda x: (x-1)**(-1/2)+tracker12.get_value(), 
            x_range=[1/(4-tracker12.get_value())**(2)+1, 3], 
            use_smoothing=False)
                
        )
        

        curve12.add_updater(update12) 

        p1 = Point(axes.coords_to_point(1, 0.5), color=WHITE)

        def update13(mob):
            mob.become(
                Point(axes.coords_to_point(1, tracker13.get_value()), color=WHITE)
                
        )
        

        p1.add_updater(update13)




        #Second x

        tracker21=ValueTracker(0.5)
        tracker22=ValueTracker(-1)

        curve21 = axes.plot(lambda x: 0.5, 
            x_range=[-3.5, -3.05], 
            use_smoothing=False)

        
        def update21(mob):
            mob.become(
                axes.plot(lambda x: tracker21.get_value(), 
            x_range=[-3.5, -3.05], 
            use_smoothing=False)
                
        )
        

        curve21.add_updater(update21)

        curve22 = axes.plot(lambda x: 0*(x+1)+0.5, 
            x_range=[-2.95, -1], 
            use_smoothing=False)

        
        def update22(mob):
            mob.become(
                axes.plot(lambda x: ((0.5-tracker21.get_value())/2)*(x+1)+0.5, 
            x_range=[-2.95, -1], 
            use_smoothing=False)
                
        )
        

        curve22.add_updater(update22) 

        p2 = Point(axes.coords_to_point(-3, -1), color=WHITE)

        def update23(mob):
            mob.become(
                Point(axes.coords_to_point(-3, tracker22.get_value()), color=WHITE)
                
        )
        

        p2.add_updater(update23)


        tracker31=ValueTracker(0.5)
        tracker32=ValueTracker(0.5)


        curve31 = axes.plot(lambda x: 0.5, 
            x_range=[-5, -4.05], 
            use_smoothing=False)

        
        def update31(mob):
            mob.become(
                axes.plot(lambda x: tracker31.get_value(), 
            x_range=[-5, -4.05], 
            use_smoothing=False)
                
        )
        

        curve31.add_updater(update31)

        p3 = Point(axes.coords_to_point(-4, 0.5), color=WHITE)

        def update32(mob):
            mob.become(
                Point(axes.coords_to_point(-4, tracker32.get_value()), color=WHITE)
                
        )

        p3.add_updater(update32)    





        curve32 = axes.plot(lambda x: (x+4), 
            x_range=[-3.95, -3.5], 
            use_smoothing=False)




        



        #self.add_fixed_in_frame_mobjects(title)
        self.add(axes, axes_labels, numberplane, title1)
        self.play(Write(text1), Write(text2), Write(text3))
        self.wait(1)
        self.play(text1.animate.scale(1.5))
        self.play(text1.animate.scale(2/3))
        self.wait(1)
        self.play(Create(d1))
        self.wait(3)
        self.play(Create(curve11), Create(curve12), )
        self.wait(2)
        
        self.play(tracker11.animate.set_value(-3.5), run_time=3)
        self.play(tracker11.animate.set_value(3.5), run_time=3)
        self.play(tracker11.animate.set_value(0.5), run_time=3)

        self.play(tracker12.animate.set_value(-3.5), run_time=3)
        self.play(tracker12.animate.set_value(3), run_time=3)
        self.play(tracker12.animate.set_value(0.5), run_time=3)

        self.play(Create(p1))

        self.play(tracker13.animate.set_value(-3.5), run_time=3)
        self.play(tracker13.animate.set_value(3), run_time=3)
        self.play(tracker13.animate.set_value(0.5), run_time=3)

        self.play(FadeOut(p1))

        self.play(FadeOut(d1))
        self.wait(3)

        self.play(text2.animate.scale(1.5))
        self.play(text2.animate.scale(2/3))
        self.wait(1)
        self.play(Create(d2))
        self.wait(3)
        self.play(Create(curve21), Create(curve22), Create(p2))
        self.wait(2)
        
        self.play(tracker21.animate.set_value(-3.5), run_time=3)
        self.play(tracker21.animate.set_value(3.5), run_time=3)
        self.play(tracker21.animate.set_value(0.5), run_time=3)

        self.play(tracker22.animate.set_value(-3.5), run_time=3)
        self.play(tracker22.animate.set_value(3.5), run_time=3)
        self.play(tracker22.animate.set_value(-1), run_time=3)

        self.play(FadeOut(d2))
        self.wait(3)

        self.play(text3.animate.scale(1.5))
        self.play(text3.animate.scale(2/3))
        self.wait(1)
        self.play(Create(d3))
        self.wait(1)
        self.play(Create(curve31), Create(curve32), Create(p3))
        self.wait(2)
        
        self.play(tracker31.animate.set_value(-3.5), run_time=3)
        self.play(tracker31.animate.set_value(3.5), run_time=3)
        self.play(tracker31.animate.set_value(0.5), run_time=3)

        self.wait(2)

        self.play(tracker32.animate.set_value(-3.5), run_time=3)
        self.play(tracker32.animate.set_value(3.5), run_time=3)
        self.play(tracker32.animate.set_value(0.5), run_time=3)

        self.play(FadeOut(d3))
        self.wait(10)


        """

        eq1 = MathTex(r"=").shift(RIGHT*2, UP)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*3)
        eq3 = MathTex(r"=").next_to(eq2, DOWN*3)

        lhs1 = MathTex(r"f(K, R)", color=BLUE).scale(0.7).next_to(eq1, LEFT)
        rhs1 = MathTex(r"65K^{\frac{4}{5}}R^{\frac{1}{5}}}", color=BLUE).scale(0.7).next_to(eq1, RIGHT)

        
        lhs2 = MathTex(r"\nabla f(K, R)", color=BLUE).scale(0.7).next_to(eq2, LEFT)
        rhs2 = MathTex(r"\left\langle 52 K^{-\frac{1}{5}} R^{\frac{1}{5}}, 13K^{\frac{4}{5}}R^{-\frac{4}{5}} \right\rangle", color=BLUE).scale(0.7).next_to(eq2, RIGHT)

        
        lhs3 = MathTex(r"g(K, R)", color=YELLOW).scale(0.7).next_to(eq2, LEFT)
        rhs3 = MathTex(r"K+R", color=YELLOW).scale(0.7).next_to(eq2, RIGHT)

        lhs4 = MathTex(r"\nabla g(K, R)", color=YELLOW).scale(0.7).next_to(eq3, LEFT)
        rhs4 = MathTex(r"\left\langle 1 , 1 \right\rangle",color=YELLOW).scale(0.7).next_to(eq3, RIGHT)

        rhs5 = MathTex(r"\nabla f(K, R)", color=BLUE).scale(0.7).next_to(eq3, RIGHT)
        lhs5 = MathTex(r"\lambda", r"\nabla g(K, R)",color=YELLOW).scale(0.7).next_to(eq3, LEFT)
        lhs5[0].set_color(WHITE)

        rhs6 = MathTex(r"\left\langle 52 K^{-\frac{1}{5}}R^{\frac{1}{5}}, 13K^{\frac{4}{5}}R^{-\frac{4}{5}} \right\rangle", color=BLUE).scale(0.7).next_to(eq3, RIGHT)
        lhs6 = MathTex(r"\lambda", r"\left\langle 1 , 1 \right\rangle",color=YELLOW).scale(0.7).next_to(eq3, LEFT)
        lhs6[0].set_color(WHITE)

        lhs7 = MathTex(r"\left\langle \lambda , \lambda \right\rangle",color=YELLOW).scale(0.7).next_to(eq3, LEFT)
        

        self.wait(4)
        self.play(Write(lhs1))
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(4)
        self.play(Write(lhs2))
        self.wait(2)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(FadeOut(lhs1, rhs1), rhs2.animate.next_to(eq1, RIGHT), lhs2.animate.next_to(eq1, LEFT))
        self.play(Write(lhs3), Write(rhs3))
        self.wait(4)
        self.play(Write(lhs4))
        self.wait(2)
        self.play(Write(eq3), Write(rhs4))
        self.wait(4)
        self.play(FadeOut(lhs3, rhs3), rhs4.animate.next_to(eq2, RIGHT), lhs4.animate.next_to(eq2, LEFT))
        self.wait(3)
        self.play(Write(lhs5), Write(rhs5))
        self.wait(3)
        self.play(Transform(lhs5, lhs6), Transform(rhs5, rhs6))
        self.wait(3)
        self.play(Transform(lhs5, lhs7))

        """


       





        
        



        


        
        



        



  
       