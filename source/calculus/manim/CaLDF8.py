#%%manim -ql LIPoly

from manim import *







class Part1(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the derivative of  } h(x)=\ln\Big( \arcsin(x) - 8\arctan(x) \Big)", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption1 = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        caption2 = MathTex(r"\text{Product Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        caption3 = MathTex(r"\text{Quotient Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.75).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.75).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.75).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.75).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"h(x)").scale(0.75).next_to(eq1, LEFT)
        lhs2 = MathTex(r"h'(x)").scale(0.75).next_to(eq2, LEFT)

        rhs1 = MathTex(r"\ln\Big( ", r" \arcsin(x) - 8\arctan(x) ", r" \Big)").scale(0.75).next_to(eq1, RIGHT)
        #rhs1[0].set_color(BLUE)
        #rhs1[1].set_color(RED)
        #rhs1[2].set_color(BLUE)

        rhs2 = MathTex(r"{1 \over", r" \arcsin(x) - 8\arctan(x)}", r"\frac{d}{dx}\left[ \arcsin(x) - 8\arctan(x) \right]").scale(0.75).next_to(eq2, RIGHT)
        rhs2[0].set_color(BLUE) 
        rhs2[1].set_color(RED)
        rhs2[2].set_color(RED)

        rhs3 = MathTex(r"{1 \over", r" \arcsin(x) - 8\arctan(x)}", r"\left( \frac{1}{\sqrt{1-x^2}} - 8\frac{1}{1+x^2} \right)").scale(0.75).next_to(eq3, RIGHT)
        rhs3[0].set_color(BLUE) 
        rhs3[1].set_color(RED)
        rhs3[2].set_color(RED)

        rhs3a = MathTex(r"{1 \over", r" \arcsin(x) - 8\arctan(x)}", r"\left( \frac{1}{\sqrt{1-x^2}} - \frac{8}{1+x^2} \right)").scale(0.75).next_to(eq3, RIGHT)
        rhs3a[0].set_color(BLUE) 
        rhs3a[1].set_color(RED)
        rhs3a[2].set_color(RED)
        
        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(rhs1[1].animate.set_color(RED), rhs1[0].animate.set_color(BLUE), rhs1[2].animate.set_color(BLUE))
        self.wait(3)
        
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2), Write(caption1))

        self.wait(5)
        self.play(Write(eq3), Write(rhs3), FadeOut(caption1))
        self.wait(5)
        self.play(Transform(rhs3, rhs3a))
        self.wait(5)




class Part2(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the derivative of  } g(t)=-3\arcsin(t)\ln\left(t^4+9 \right)", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption1 = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        caption2 = MathTex(r"\text{Product Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        caption3 = MathTex(r"\text{Quotient Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.75).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.75).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.75).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.75).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"g(t)").scale(0.75).next_to(eq1, LEFT)
        lhs2 = MathTex(r"g'(t)").scale(0.75).next_to(eq2, LEFT)

        rhs1 = MathTex(r"-3\arcsin(t)",r" \ln\left(t^4+9 \right)").scale(0.75).next_to(eq1, RIGHT)
        #rhs1a = MathTex(r"\Big(", r"\frac{-5y^2-2}{4y^6+6}", r"\Big)^4").scale(0.75).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"-3\arcsin(t)", r"\frac{d}{dt}\left[ \ln\Big( ", r" t^4+9 ", r" \Big) \right]", r"+", r"\ln\left(t^4+9 \right)", r"\frac{d}{dt}\Big[ -3\arcsin(t) \Big]").scale(0.75).next_to(eq2, RIGHT)
        rhs2[0].set_color(BLUE)
        rhs2[1].set_color(RED)
        rhs2[2].set_color(RED)
        rhs2[3].set_color(RED)
        rhs2[5].set_color(RED)
        rhs2[6].set_color(BLUE)

        rhs3 = MathTex(r"-3\arcsin(t)", r"\frac{1}{t^4+9}", r"\frac{d}{dt}\left[t^4+9 \right]",  r"+", r"\ln\left(t^4+9 \right)", r"(-3)\frac{1}{\sqrt{1-x^2}}").scale(0.75).next_to(eq3, RIGHT)
        rhs3[1].set_color(ORANGE)
        rhs3[2].set_color(GREEN)
        rhs3[5].set_color(BLUE)

        rhs4 = MathTex(r"-3\arcsin(t)", r"\frac{1}{t^4+9}", r"(4t^3)",  r"+", r"\ln\left(t^4+9 \right)", r"(-3)\frac{1}{\sqrt{1-x^2}}").scale(0.75).next_to(eq4, RIGHT)
        rhs4[2].set_color(GREEN)

        rhs4a = MathTex(r"-\frac{12t^3\arcsin(t)}{t^4+9} - \frac{3\ln\left(t^4+9 \right)}{\sqrt{1-x^2}}").scale(0.75).next_to(eq4, RIGHT)

        



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
        self.play(rhs1[1].animate.set_color(RED))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2), Write(caption2))
        self.wait(5)
        self.play(rhs2[1].animate.set_color(ORANGE), rhs2[2].animate.set_color(GREEN), rhs2[3].animate.set_color(ORANGE), )

        self.wait(3)
        self.play(Write(eq3), Write(rhs3), FadeOut(caption2), Write(caption1))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4), FadeOut(caption1))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(5)

        


class Part3(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute the derivative of  } f(u) = \frac{\arctan(u)}{\ln(-2u)}", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        caption1 = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        caption2 = MathTex(r"\text{Product Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        caption3 = MathTex(r"\text{Quotient Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.75).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.75).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.75).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.75).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"f(u)").scale(0.75).next_to(eq1, LEFT)
        lhs2 = MathTex(r"f'(u)").scale(0.75).next_to(eq2, LEFT)

        rhs1 = MathTex(r"{\arctan(7u)", r" \over", r" \ln(-2u) }").scale(0.75).next_to(eq1, RIGHT)
        #rhs1a = MathTex(r"\Big(", r"\frac{-5y^2-2}{4y^6+6}", r"\Big)^4").scale(0.75).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"{\ln(-2u)", r"\frac{d}{du}\Bigl[ \arctan{}(", r"7u ", r") \Bigr]", r"-", r"\arctan(7u)", r"\frac{d}{du}\left[ \ln(-2u)\right]", r"\over", r"\ln(-2u)^2 }").scale(0.75).next_to(eq2, RIGHT)
        rhs2[0].set_color(RED)
        rhs2[1].set_color(BLUE)
        rhs2[2].set_color(BLUE)
        rhs2[3].set_color(BLUE)
        rhs2[5].set_color(BLUE)
        rhs2[6].set_color(RED)
        rhs2[8].set_color(RED)

        rhs2a = MathTex(r"{\ln(-2u)", r"\frac{d}{du}\Bigl[ \arctan{}(", r"7u ", r") \Bigr]", r"-", r"\arctan(7u)", r"\frac{d}{du}\left[ \ln(-2) + \ln(u)\right]", r"\over", r"\ln(-2u)^2 }").scale(0.75).next_to(eq2, RIGHT)
        rhs2a[0].set_color(RED)
        rhs2a[1].set_color(ORANGE)
        rhs2a[2].set_color(GREEN)
        rhs2a[3].set_color(ORANGE)
        rhs2a[5].set_color(BLUE)
        rhs2a[6].set_color(RED)
        rhs2a[8].set_color(RED)





        rhs3 = MathTex(r"{\ln(-2u)", r"\frac{1}{1+(7u)^2}", r"\frac{d}{du}\left[ 7u \right]", r"-", r"\arctan(7u)", r"\frac{1}{u}", r"\over", r"\ln(-2u)^2 }").scale(0.75).next_to(eq3, RIGHT)
        rhs3[1].set_color(ORANGE)
        rhs3[2].set_color(GREEN)
        rhs3[5].set_color(RED)

        rhs4 = MathTex(r"{\ln(-2u)", r"\frac{1}{1+(7u)^2}", r"7", r"-", r"\arctan(7u)", r"\frac{1}{u}", r"\over", r"\ln(-2u)^2 }").scale(0.75).next_to(eq4, RIGHT)
        rhs4[2].set_color(GREEN)

        rhs4a = MathTex(r"\frac{  \frac{7\ln(-2u)}{1+49t^2}  - \frac{\arctan(7u)}{u}     }{ \ln(-2u)^2}").scale(0.75).next_to(eq4, RIGHT)

        rhs4b = MathTex(r"  \frac{7}{(1+49t^2)\ln(-2u)}  - \frac{\arctan(7u)}{u\ln(-2u)^2}     ").scale(0.75).next_to(eq4, RIGHT)

        rhs4c = MathTex(r"{\ln(-2u)", r"\frac{1}{1+(7u)^2}", r"7", r"-", r"\arctan(7u)", r"\frac{1}{u}", r"\over", r"\ln(-2u)^2 }").scale(0.75).next_to(eq4, RIGHT)
        rhs4c[2].set_color(GREEN)

        



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
        self.play(rhs1[2].animate.set_color(RED))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2), Write(caption3))
        self.wait(5)
        self.play(rhs2[1].animate.set_color(ORANGE), rhs2[2].animate.set_color(GREEN), 
         rhs2[3].animate.set_color(ORANGE) )
        self.wait(5)
        self.play(Transform(rhs2, rhs2a))

        self.wait(3)
        self.play(Write(eq3), Write(rhs3), FadeOut(caption3), Write(caption1))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4), FadeOut(caption1))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(5)
        self.play(Transform(rhs4, rhs4b))
        self.wait(10) 


        #rhs2s = MathTex(r"{\ln(-2u)", r"\frac{d}{du}\Bigl[ \arctan{}(", r"7u ", r")\Bigr]", r"-", r"\arctan(7u)", r"\frac{d}{du}[ \ln(", r"-2u ", r")]", r"\over", r"\ln(-2u)^2 }").scale(0.75).next_to(eq2, RIGHT)
        #rhs2s[0].set_color(RED)
        #rhs2s[1].set_color(ORANGE)
        #rhs2s[2].set_color(GREEN)
        #rhs2s[3].set_color(ORANGE)
        #rhs2s[5].set_color(BLUE)
        #rhs2s[6].set_color(ORANGE)
        #rhs2s[7].set_color(GREEN)
        #rhs2s[8].set_color(ORANGE)
        #rhs2s[10].set_color(RED)

        #rhs3s = MathTex(r"{\ln(-2u)", r"\frac{1}{1+(7u)^2}", r"\frac{d}{du}\left[ 7u \right]", r"-", r"\arctan(7u)", r"\frac{1}{-2u}", r"(-2)", r"\over", r"\ln(-2u)^2 }").scale(0.75).next_to(eq3, RIGHT)
        #rhs3s[1].set_color(ORANGE)
        #rhs3s[2].set_color(GREEN)
        #rhs3s[5].set_color(ORANGE)
        #rhs3s[6].set_color(GREEN)

        #self.play(FadeOut(eq4, rhs4, eq3, rhs3, rhs2))
        #self.play(Write(rhs2s))
        ##self.wait(3)
        #self.play(Write(eq3), Write(rhs3s), Write(caption1))
        #self.wait(5)
        #self.play(Transform(rhs3s, rhs3))

        #self.wait(5)
        #self.play(Write(eq4), Write(rhs4c), FadeOut(caption1))
        #self.wait(5)
        #self.play(Transform(rhs4c, rhs4a))
        #self.wait(5)
        #self.play(Transform(rhs4c, rhs4b))
        #self.wait(5) 
        



        



  
       