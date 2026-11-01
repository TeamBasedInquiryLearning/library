#%%manim -ql LIPoly

from manim import *







class ComputeCont(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{What is  } b \text{ so that } f(x) = \begin{cases} \frac{11}{2}x^{2} + b + 2x, & x < 2 \\ -x^{2} + 8x - 10, & x \geq 2 \end{cases} \text{ is continuous}?", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP+LEFT)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").next_to(eq2, DOWN*5)




        lhs1 = MathTex(r"\displaystyle \lim_{x\to 2^-}\frac{11}{2} x^2+b+2x").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"26+b").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"\displaystyle \lim_{x\to 2^+}-x^2+8x-10").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"2").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"\displaystyle \lim_{x\to 2^-}\frac{11}{2} x^2+b+2x").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"\displaystyle \lim_{x\to 2^+}-x^2+8x-10").scale(0.8).next_to(eq3, RIGHT)
        lhs4 = MathTex(r"26+b").scale(0.8).next_to(eq3, LEFT)
        rhs4 = MathTex(r"2").scale(0.8).next_to(eq3, RIGHT)
        lhs5 = MathTex(r"b").scale(0.8).next_to(eq3, LEFT)
        rhs5 = MathTex(r"-24").scale(0.8).next_to(eq3, RIGHT)
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
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
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Transform(lhs3, lhs4))
        self.wait(3)
        self.play(Transform(rhs3, rhs4))
        self.wait(3)
        self.play(Transform(lhs3, lhs5), Transform(rhs3, rhs5))
        


        self.wait(3)
        self.play(FadeOut(eq1, eq2, eq3, rhs1, rhs2, rhs3, lhs1, lhs2, lhs3))


        axes = Axes(x_range=[-10.1,10.1,2], y_range=[-30.1,30.1,6], x_length=4.2, y_length=4.2,)
        axes_labels = axes.get_axis_labels()
        

        


        tracker=ValueTracker(0)

        leftcurve = axes.plot(lambda x: (11/2)*x**2+2*x, 
            x_range=[-((664)**(1/2)-2)/11, 2], 
            use_smoothing=False, color=YELLOW)

        
        
        def update(mob):
            mob.become(
                axes.plot(lambda x: (11/2)*x**2+2*x + tracker.get_value(), 
            x_range=[-((664-22*tracker.get_value())**(1/2)-2)/11, 2], 
            use_smoothing=False, color=YELLOW)
                
        )
        

        leftcurve.add_updater(update)

        rightcurve = axes.plot(lambda x: (-1)*x**2+8*x-10, 
            x_range=[2, 10], 
            use_smoothing=False, color=YELLOW)

        
        btext = MathTex(r"b=").scale(0.7).shift(DOWN*3)


        number=DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=0,
            include_sign=True,
        ).scale(0.7).next_to(btext, RIGHT)
        def updateNum(mob):
            mob.become(DecimalNumber(
            tracker.get_value(),
            show_ellipsis=True,
            num_decimal_places=0,
            include_sign=True,
        )).scale(0.7).next_to(btext, RIGHT)
        number.add_updater(updateNum)

        
        self.play(Create(axes), Create(axes_labels))
        self.play(Write(btext), Write(number), Create(leftcurve), Create(rightcurve))
        self.wait(4)
        self.play(tracker.animate.set_value(-29), run_time=5)
        self.wait(4)
        self.play(tracker.animate.set_value(-24), run_time=2)


        self.wait(10)


class ComputeRemovable(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Identify the discontinuity: } g(x) = \begin{cases} -8 \, x + 30, & x < 4 \\ 3, & x = 4 \\ 2 \, x - 10, & x > 4 \\ \end{cases}.", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP+LEFT)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").next_to(eq2, DOWN*5)




        lhs1 = MathTex(r"\displaystyle \lim_{x\to 4^-}-8x+30").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"-2").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"\displaystyle \lim_{x\to 4^+}2x-10").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"-2").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"\displaystyle \lim_{x\to 4^-}-8x+30").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"\displaystyle \lim_{x\to 4^+}2x-10").scale(0.8).next_to(eq3, RIGHT)
        
        caption = MathTex(r"\text{Removable discontinuity}", color=BLUE).shift(DOWN*2.5)
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Write(lhs3), Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Write(caption))
        
        


        self.wait(3)
        self.play(FadeOut(eq1, eq2, eq3, rhs1, rhs2, rhs3, lhs1, lhs2, lhs3))


        axes = Axes(x_range=[-0.1,8.1,2], y_range=[-10.1,10.1,2], x_length=4.2, y_length=4.2,)
        axes_labels = axes.get_axis_labels()
        

        



        leftcurve = axes.plot(lambda x: -8*x+30, 
            x_range=[2.5,3.95], 
            use_smoothing=False, color=YELLOW)

        

        rightcurve = axes.plot(lambda x: 2*x-10, 
            x_range=[4.05, 8], 
            use_smoothing=False, color=YELLOW)

        point = Point(axes.coords_to_point(4, 3), color=YELLOW).scale(1.5)

        Bound = DashedLine(axes.coords_to_point(4, -10), axes.coords_to_point(4, 10), color=RED)

        


        

        
        self.play(Create(axes), Create(axes_labels))
        self.play(Create(Bound), Create(leftcurve), Create(rightcurve))
        self.play(Create(point))
        self.wait(2)
        self.play(FadeOut(Bound))
        


        self.wait(10)


class ComputeJump(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Identify the discontinuity: } h(x) = \begin{cases} 4x + 3, & x < -2 \\ 5, & x = -2 \\ -6x-7, & x > -2 \\ \end{cases}.", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP+LEFT)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)
        eq3 = MathTex(r"\neq").next_to(eq2, DOWN*5)




        lhs1 = MathTex(r"\displaystyle \lim_{x\to -2^-}4x+3").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"-5").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"\displaystyle \lim_{x\to -2^+}-6x-7").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"-2").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"\displaystyle \lim_{x\to -2^-}4x+3").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"\displaystyle \lim_{x\to -2^+}-6x-7").scale(0.8).next_to(eq3, RIGHT)
        
        caption = MathTex(r"\text{Jump discontinuity}", color=BLUE).shift(DOWN*2.5)
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Write(lhs3), Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Write(caption))
        
        


        self.wait(3)
        self.play(FadeOut(eq1, eq2, eq3, rhs1, rhs2, rhs3, lhs1, lhs2, lhs3))


        axes = Axes(x_range=[-4,4,2], y_range=[-10,10,2], x_length=4.2, y_length=4.2,)
        axes_labels = axes.get_axis_labels()
        

        point = Point(axes.coords_to_point(-2, 5), color=YELLOW).scale(1.5)



        leftcurve = axes.plot(lambda x: 4*x+3, 
            x_range=[-13/4,-2.05], 
            use_smoothing=False, color=YELLOW)

        

        rightcurve = axes.plot(lambda x: -6*x-7, 
            x_range=[-1.95, 0.5], 
            use_smoothing=False, color=YELLOW)

        

        Bound = DashedLine(axes.coords_to_point(-2, -10), axes.coords_to_point(-2, 10), color=RED)

        


        

        
        self.play(Create(axes), Create(axes_labels))
        self.play(Create(Bound), Create(leftcurve), Create(rightcurve))
        self.play(Create(point))
        self.wait(2)
        self.play(FadeOut(Bound))
        


        self.wait(10)









        


        
        



        



  
       