#%%manim -ql LIPoly

from manim import *







class Part1(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the derivative of  } f(y)=\Big( -\frac{5y^2+2}{4y^6+6} \Big)^4", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption1 = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        caption2 = MathTex(r"\text{Product Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        caption3 = MathTex(r"\text{Quotient Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.6).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.6).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.6).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.6).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"f(y)").scale(0.6).next_to(eq1, LEFT)
        lhs2 = MathTex(r"f'(y)").scale(0.6).next_to(eq2, LEFT)

        rhs1 = MathTex(r"\Big(", r"-\frac{5y^2+2}{4y^6+6}", r"\Big)^4").scale(0.6).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"\Big(", r"\frac{-5y^2-2}{4y^6+6}", r"\Big)^4").scale(0.6).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"4\Big( \frac{-5y^2-2}{4y^6+6} \Big)^3", r"\frac{d}{dy}\Big[\frac{-5y^2-2}{4y^6+6}\Big]").scale(0.6).next_to(eq2, RIGHT)
        rhs2[1].set_color(RED)

        rhs3 = MathTex(r"4\Big( \frac{-5y^2-2}{4y^6+6} \Big)^3", r"\Big(\frac{(4y^6+6)\frac{d}{dy}[-5y^2-2]-(-5y^2-2)\frac{d}{dy}[4y^6+6]}{(4y^6+6)^2}\Big)").scale(0.6).next_to(eq3, RIGHT)
        rhs3[1].set_color(RED)

        rhs4 = MathTex(r"4\Big( \frac{-5y^2-2}{4y^6+6} \Big)^3", r"\Big(\frac{(4y^6+6)(-10y)-(-5y^2-2)(24y^5)}{(4y^6+6)^2}\Big)").scale(0.6).next_to(eq4, RIGHT)
        rhs4[1].set_color(RED)

        rhs4a = MathTex(r"4\Big( \frac{-5y^2-2}{4y^6+6} \Big)^3", r"\Big(\frac{20y^7+12y^5-15y }{4y^{12}+12y^6+9}\Big)").scale(0.6).next_to(eq4, RIGHT)

        
        

        




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
        self.play(Write(eq2), Write(rhs2), Write(caption1))

        self.wait(3)
        self.play(Write(eq3), Write(rhs3), FadeOut(caption1), Write(caption3))
        self.wait(3)
        self.play(Write(eq4), Write(rhs4), FadeOut(caption3))
        self.wait(3)
        self.play(Transform(rhs4, rhs4a))
        self.wait(5)




class Part2(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the derivative of  } h(t)=\ln\Big( t^2+3t^4\Big)\cos(t)", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption1 = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        caption2 = MathTex(r"\text{Product Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        caption3 = MathTex(r"\text{Quotient Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.6).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.6).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.6).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.6).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"h(t)").scale(0.6).next_to(eq1, LEFT)
        lhs2 = MathTex(r"h'(t)").scale(0.6).next_to(eq2, LEFT)

        rhs1 = MathTex(r"\ln\Big( t^2+3t^4\Big)", r"\cos(t)").scale(0.6).next_to(eq1, RIGHT)
        #rhs1a = MathTex(r"\Big(", r"\frac{-5y^2-2}{4y^6+6}", r"\Big)^4").scale(0.6).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"\ln\Big( t^2+3t^4\Big)", r"\frac{d}{dt}[\cos(t)]", r"+\cos(t)", r"\frac{d}{dt}\Big[ \ln\Big( t^2+3t^4\Big)\Big]").scale(0.6).next_to(eq2, RIGHT)
        rhs2[1].set_color(GREEN)
        rhs2[3].set_color(BLUE)

        rhs3 = MathTex(r"\ln\Big( t^2+3t^4\Big)", r"(-\sin(t))", r"+\cos(t)", r"\frac{1}{t^2+3t^4}", r"\frac{d}{dt}[t^2+3t^4]").scale(0.6).next_to(eq3, RIGHT)
        rhs3[4].set_color(RED)

        rhs4 = MathTex(r"\ln\Big( t^2+3t^4\Big)", r"(-\sin(t))", r"+\cos(t)", r"\frac{1}{t^2+3t^4}", r"(2t+12t^3)").scale(0.6).next_to(eq4, RIGHT)
        rhs4[4].set_color(RED)

        rhs4a = MathTex(r"-\sin(t)\ln\Big( t^2+3t^4\Big)+\cos(t)\frac{2t+12t^3}{t^2+3t^4}").scale(0.6).next_to(eq4, RIGHT)

        
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        #self.play(Transform(rhs1, rhs1a))
        #self.wait(3)
        self.play(rhs1[0].animate.set_color(BLUE))
        self.play(rhs1[1].animate.set_color(GREEN))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2), Write(caption2))

        self.wait(3)
        self.play(Write(eq3), Write(rhs3), FadeOut(caption2), Write(caption1))
        self.wait(3)
        self.play(Write(eq4), Write(rhs4), FadeOut(caption1))
        self.wait(3)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10)

        


class Part3(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the derivative of  } g(x)=\sqrt{\cos(3x^4+4x)}", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption1 = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        caption2 = MathTex(r"\text{Product Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        caption3 = MathTex(r"\text{Quotient Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.6).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.6).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.6).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.6).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"g(x)").scale(0.6).next_to(eq1, LEFT)
        lhs2 = MathTex(r"g'(x)").scale(0.6).next_to(eq2, LEFT)

        rhs1 = MathTex(r"\sqrt{\cos(3x^4+4x)}").scale(0.6).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"\Big(", r"\cos(3x^4+4x)", r"\Big)^\frac{1}{2}").scale(0.6).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"\frac{1}{2}\Big(\cos(3x^4+4x)\Big)^{-\frac{1}{2}}", r"\frac{d}{dx}[\cos(3x^4+4x)]").scale(0.6).next_to(eq2, RIGHT)
        rhs2[1].set_color(RED)

        rhs3 = MathTex(r"\frac{1}{2}\Big(\cos(3x^4+4x)\Big)^{-\frac{1}{2}}", r"\Big( -\sin(3x^4+4x)\Big)", r"\frac{d}{dx}[3x^4+4x]").scale(0.6).next_to(eq3, RIGHT)
        rhs3[2].set_color(RED)

        rhs4 = MathTex(r"\frac{1}{2}\Big(\cos(3x^4+4x)\Big)^{-\frac{1}{2}}", r"\Big( -\sin(3x^4+4x)\Big)", r"(12x^3+4)").scale(0.6).next_to(eq4, RIGHT)
        rhs4[2].set_color(RED)

        rhs4a = MathTex(r"\frac{-\sin(3x^4+4x)(12x^3+4)}{2\sqrt{\cos(3x^4+4x)}}").scale(0.6).next_to(eq4, RIGHT)

        
        

        




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
        self.play(Write(eq2), Write(rhs2), Write(caption1))

        self.wait(3)
        self.play(Write(eq3), Write(rhs3), FadeOut(caption1), Write(caption1))
        self.wait(3)
        self.play(Write(eq4), Write(rhs4), FadeOut(caption1))
        self.wait(3)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10)        
        



        



  
       