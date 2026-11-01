#%%manim -ql LIPoly

from manim import *







class ComputeLimits(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the left and right limits as  } x \text{ approaches } -1, 2 \text{ of }\frac{(x-4)(x+2)}{(x-2)^2(x+1)}", color=TEAL).scale(0.7)        
        title1.to_edge(UP)

        
        axes = Axes(x_range=[-5,5,2], y_range=[-10,10,2], x_length=4.2, y_length=4.2,)
        axes_labels = axes.get_axis_labels()
        
        

        



        curve1 = axes.plot(lambda x: (x-4)*(x+2)/((x-2)**2*(x+1)), 
            x_range=[-5,-1.051], 
            use_smoothing=False, color=YELLOW)

        curve2 = axes.plot(lambda x: (x-4)*(x+2)/((x-2)**2*(x+1)), 
            x_range=[-0.932, 1.392], 
            use_smoothing=False, color=YELLOW)

        curve3 = axes.plot(lambda x: (x-4)*(x+2)/((x-2)**2*(x+1)), 
            x_range=[2.448, 5], 
            use_smoothing=False, color=YELLOW)

        zero1 = DashedLine(axes.coords_to_point(-2, -10), axes.coords_to_point(-2, 10), color=BLUE)
        zero2 = DashedLine(axes.coords_to_point(4, -10), axes.coords_to_point(4, 10), color=BLUE)

        ass1 = DashedLine(axes.coords_to_point(-1, -10), axes.coords_to_point(-1, 10), color=PURPLE)
        ass2 = DashedLine(axes.coords_to_point(2, -10), axes.coords_to_point(2, 10), color=PURPLE)


        func = MathTex(r"\frac{(x-4)(x+2)}{(x-2)^2(x+1)}").scale(0.7).shift(LEFT*5)

        caption1 = MathTex("x<-2").scale(0.7).shift(DOWN*3)
        sign1 = MathTex(r"\frac{(-)(-)}{(-)^2(-)}", color=YELLOW).scale(0.7).shift(RIGHT*5)
        s1 = MathTex("-", color=RED).scale(0.5).move_to(axes.coords_to_point(-3.5, -9.5))

        caption2 = MathTex("-2<x<-1").scale(0.7).shift(DOWN*3)
        sign2 = MathTex(r"\frac{(-)(+)}{(-)^2(-)}", color=YELLOW).scale(0.7).shift(RIGHT*5)
        s2 = MathTex("+", color=GREEN).scale(0.5).move_to(axes.coords_to_point(-1.5, -9.5))

        caption3 = MathTex("-1<x<2").scale(0.7).shift(DOWN*3)
        sign3 = MathTex(r"\frac{(-)(+)}{(-)^2(+)}", color=YELLOW).scale(0.7).shift(RIGHT*5)
        s3 = MathTex("-", color=RED).scale(0.5).move_to(axes.coords_to_point(0.5, -9.5))

        caption4 = MathTex("2<x<4").scale(0.7).shift(DOWN*3)
        sign4 = MathTex(r"\frac{(-)(+)}{(+)^2(+)}", color=YELLOW).scale(0.7).shift(RIGHT*5)
        s4 = MathTex("-", color=RED).scale(0.5).move_to(axes.coords_to_point(3, -9.5))

        caption5 = MathTex("4<x").scale(0.7).shift(DOWN*3)
        sign5 = MathTex(r"\frac{(+)(+)}{(+)^2(+)}", color=YELLOW).scale(0.7).shift(RIGHT*5)
        s5 = MathTex("+", color=GREEN).scale(0.5).move_to(axes.coords_to_point(4.5, -9.5))


        limit1 = MathTex(r"\displaystyle \lim_{x\to -1^-} \frac{(x-4)(x+2)}{(x-2)^2(x+1)} = \infty,  \lim_{x\to -1^+} \frac{(x-4)(x+2)}{(x-2)^2(x+1)} = -\infty,  \lim_{x\to -1} \frac{(x-4)(x+2)}{(x-2)^2(x+1)} \text{ is undefined.}").scale(0.7).shift(DOWN*3)
        limit2 = MathTex(r"\displaystyle \lim_{x\to 2^-} \frac{(x-4)(x+2)}{(x-2)^2(x+1)} = -\infty,  \lim_{x\to 2^+} \frac{(x-4)(x+2)}{(x-2)^2(x+1)} = -\infty,  \lim_{x\to 2} \frac{(x-4)(x+2)}{(x-2)^2(x+1)} =-\infty.").scale(0.7).shift(DOWN*3)


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(2)
        self.play(Create(axes), Create(axes_labels), )
        self.wait(3)
        self.play(Create(zero1), Create(zero2))
        self.wait(3)
        self.play(Create(ass1), Create(ass2))
        self.wait(3)
        self.play(Write(func))
        self.wait(2)
        self.play(Write(caption1))
        self.wait(5)
        self.play(Write(sign1))
        self.wait(2)
        self.play(Write(s1))

        self.play(Transform(caption1, caption2))
        self.wait(5)
        self.play(Transform(sign1, sign2))
        self.wait(2)
        self.play(Write(s2))


        self.play(Transform(caption1, caption3))
        self.wait(5)
        self.play(Transform(sign1, sign3))
        self.wait(2)
        self.play(Write(s3))

        self.play(Transform(caption1, caption4))
        self.wait(5)
        self.play(Transform(sign1, sign4))
        self.wait(2)
        self.play(Write(s4))

        self.play(Transform(caption1, caption5))
        self.wait(5)
        self.play(Transform(sign1, sign5))
        self.wait(2)
        self.play(Write(s5))
        self.wait(2)

        self.play(FadeOut(caption1, sign1, func))
        self.wait(3)

        self.play(s2.animate.scale(1.5), s3.animate.scale(1.5),)
        self.play(s2.animate.scale(2/3), s3.animate.scale(2/3),)
        self.play(Write(limit1))
        self.wait(5)

        self.play(FadeOut(limit1))
        self.play(s4.animate.scale(1.5), s3.animate.scale(1.5),)
        self.play(s4.animate.scale(2/3), s3.animate.scale(2/3),)
        self.play(Write(limit2))
        self.wait(5)

        self.play(FadeOut(limit2))
        self.play(Create(curve1))
        self.play(Create(curve2))
        self.play(Create(curve3))




        self.wait(10)






        


        
        



        



  
       