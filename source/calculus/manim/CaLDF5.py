#%%manim -ql LIPoly

from manim import *







class Part1(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the derivative of  } k(t)=8\cos(t)^\frac{7}{5}", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        
        eq1 = MathTex(r"=").scale(0.8).shift(UP+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)




        lhs1 = MathTex(r"k(t)").scale(0.8).next_to(eq1, LEFT)
        lhs2 = MathTex(r"k'(t)").scale(0.8).next_to(eq2, LEFT)

        rhs1 = MathTex(r"8\cos(t)^\frac{7}{5}").scale(0.8).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"8\Big(", r" \cos(t) ", r"\Big)^\frac{7}{5}" ).scale(0.8).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"8\frac{7}{5}\Big(\cos(t)\Big)^\frac{2}{5}", r"\frac{d}{dt}[\cos(t)]").scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(RED)

        rhs3 = MathTex(r"8\frac{7}{5}\Big(\cos(t)\Big)^\frac{2}{5}", r"(-\sin(t))").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(RED)

        rhs3a = MathTex(r"-\frac{56}{5}\Big(\cos(t)\Big)^\frac{2}{5}\sin(t)").scale(0.8).next_to(eq3, RIGHT)

        
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Transform(rhs1, rhs1a))
        self.wait(3)
        self.play(rhs1[1].animate.set_color(RED))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2), Write(caption))

        self.wait(3)
        self.play(Write(eq3), Write(rhs3), FadeOut(caption))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(5)

class Part2(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the derivative of  } f(t)=8\cos\Big(t^\frac{7}{5}\Big)", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        
        eq1 = MathTex(r"=").scale(0.8).shift(UP+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)




        lhs1 = MathTex(r"f(t)").scale(0.8).next_to(eq1, LEFT)
        lhs2 = MathTex(r"f'(t)").scale(0.8).next_to(eq2, LEFT)

        rhs1 = MathTex(r"8\cos\Big(", r"t^\frac{7}{5}", r"\Big)").scale(0.8).next_to(eq1, RIGHT)
        #rhs1a = MathTex(r"8\Big(", r" \cos(t) ", r"\Big)^\frac{7}{5}" ).scale(0.8).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"-8\sin\Big(t^\frac{7}{5}\Big)", r"\frac{d}{dt}\Big[t^{\frac{7}{5}}\Big]").scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(RED)

        rhs3 = MathTex(r"-8\sin\Big(t^\frac{7}{5}\Big)", r"\Big(\frac{7}{5}t^{\frac{2}{5}}\Big)").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(RED)

        rhs3a = MathTex(r"-\frac{56}{5}\sin\Big(t^\frac{7}{5}\Big)t^{\frac{2}{5}}").scale(0.8).next_to(eq3, RIGHT)

        
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        #self.play(Transform(rhs1, rhs1a))
        #self.wait(3)
        self.play(rhs1[1].animate.set_color(RED))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2), Write(caption))

        self.wait(3)
        self.play(Write(eq3), Write(rhs3), FadeOut(caption))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(5)     


class Part3(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the derivative of  } h(x)=\sin\Big(-2x^2+5x-3e^x\Big)", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        
        eq1 = MathTex(r"=").scale(0.8).shift(UP+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)




        lhs1 = MathTex(r"h(x)").scale(0.8).next_to(eq1, LEFT)
        lhs2 = MathTex(r"h'(x)").scale(0.8).next_to(eq2, LEFT)

        rhs1 = MathTex(r"\sin\Big(", r"-2x^2+5x-3e^x", r"\Big)").scale(0.8).next_to(eq1, RIGHT)
        #rhs1a = MathTex(r"8\Big(", r" \cos(t) ", r"\Big)^\frac{7}{5}" ).scale(0.8).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"\cos\Big(-2x^2+5x-3e^x\Big)", r"\frac{d}{dx}\Big[-2x^2+5x-3e^x\Big]").scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(RED)

        rhs3 = MathTex(r"\cos\Big(-2x^2+5x-3e^x\Big)", r"\Big(-4x+5-3e^x\Big)").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(RED)

        rhs3a = MathTex(r"\cos\Big(-2x^2+5x-3e^x\Big)\Big(-4x+5-3e^x\Big)").scale(0.8).next_to(eq3, RIGHT)

        
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        #self.play(Transform(rhs1, rhs1a))
        #self.wait(3)
        self.play(rhs1[1].animate.set_color(RED))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2), Write(caption))

        self.wait(3)
        self.play(Write(eq3), Write(rhs3), FadeOut(caption))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(5)     


class Part4(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the derivative of  } g(x)=\ln\Big(2\sqrt{x}+3x+7\Big)", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        
        eq1 = MathTex(r"=").scale(0.8).shift(UP+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)




        lhs1 = MathTex(r"g(x)").scale(0.8).next_to(eq1, LEFT)
        lhs2 = MathTex(r"g'(x)").scale(0.8).next_to(eq2, LEFT)

        rhs1 = MathTex(r"\ln\Big(", r"2\sqrt{x}+3x+7", r"\Big)").scale(0.8).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"\ln\Big(", r"2x^\frac{1}{2}+3x+7", r"\Big)").scale(0.8).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"\frac{1}{2x^\frac{1}{2}+3x+7}", r"\frac{d}{dx}\Big[2x^\frac{1}{2}+3x+7\Big]").scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(RED)

        rhs3 = MathTex(r"\frac{1}{2x^\frac{1}{2}+3x+7}", r"\Big(-x^{-\frac{1}{2}}+3\Big)").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(RED)

        rhs3a = MathTex(r"\frac{3-\frac{1}{\sqrt{x}}}{2\sqrt{x}+3x+7}").scale(0.8).next_to(eq3, RIGHT)

        
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Transform(rhs1, rhs1a))
        self.wait(3)
        self.play(rhs1[1].animate.set_color(RED))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2), Write(caption))

        self.wait(3)
        self.play(Write(eq3), Write(rhs3), FadeOut(caption))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(10)    

        


        
        



        



  
       