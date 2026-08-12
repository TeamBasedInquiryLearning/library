#%%manim -ql LIPoly

from manim import *







class LimitInfinity(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute  } \displaystyle \lim_{x\to -\infty} \frac{7x^2 - x^6 + 3}{5x + 3x^3 - 5}, \displaystyle \lim_{x\to \infty} \frac{7x^2 - x^6 + 3}{5x + 3x^3 - 5}", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP+LEFT)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").next_to(eq2, DOWN*5)




        lhs1 = MathTex(r"\displaystyle \lim_{x\to -\infty}\frac{7x^2 - x^6 + 3}{5x + 3x^3 - 5}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\lim_{x\to -\infty}\frac{\frac{7x^2}{x^3} - \frac{x^6}{x^3} + \frac{3}{x^3} }{ \frac{5x}{x^3} + \frac{3x^3}{x^3} - \frac{5}{x^3} }").scale(0.8).next_to(eq1, RIGHT)

        
        rhs1b = MathTex(r"\lim_{x\to -\infty}\frac{\frac{7}{x} - x^3 + \frac{3}{x^3} }{ \frac{5}{x^2} + 3 - \frac{5}{x^3} }").scale(0.8).next_to(eq1, RIGHT)
        rhs1c = MathTex(r"\lim_{x\to -\infty}\frac{0 - x^3 + 0 }{ 0 + 3 - 0 }").scale(0.8).next_to(eq1, RIGHT)
        rhs1d = MathTex(r"\lim_{x\to -\infty}-\frac{x^3}{3}=\infty").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"\displaystyle \lim_{x\to \infty}\frac{7x^2 - x^6 + 3}{5x + 3x^3 - 5}").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"\lim_{x\to \infty}-\frac{x^3}{3}", r"=-\infty").scale(0.8).next_to(eq2, RIGHT)

        

        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Transform(rhs1, rhs1b))
        self.wait(5)
        self.play(Transform(rhs1, rhs1c))
        self.wait(5)
        self.play(Transform(rhs1, rhs1d))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2[0]))
        self.wait(5)
        self.play(Write(rhs2[1]))





        self.wait(10)


class LimitConstant(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute  } \displaystyle \lim_{x\to -\infty} \frac{8x^3  +3x^4 - 4}{5x^2 + 8x^4 - 9}, \displaystyle \lim_{x\to \infty} \frac{8x^3  +3x^4 - 4}{5x^2 + 8x^4 - 9}", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP+LEFT)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").next_to(eq2, DOWN*5)




        lhs1 = MathTex(r"\displaystyle \lim_{x\to -\infty}\frac{8x^3  +3x^4 - 4}{5x^2 + 8x^4 - 9}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\lim_{x\to -\infty}\frac{\frac{8x^3}{x^4}  + \frac{3x^4}{x^4} - \frac{4}{x^4} }{ \frac{5x^2}{x^4} + \frac{8x^4}{x^4} - \frac{9}{x^4} }").scale(0.8).next_to(eq1, RIGHT)

        
        rhs1b = MathTex(r"\lim_{x\to -\infty}\frac{\frac{8}{x}  + 3 - \frac{4}{x^4} }{ \frac{5}{x^2} + 8 - \frac{9}{x^4} }").scale(0.8).next_to(eq1, RIGHT)
        rhs1c = MathTex(r"\frac{0 +3 - 0 }{ 0 + 8 - 0 }").scale(0.8).next_to(eq1, RIGHT)
        rhs1d = MathTex(r"\frac{3}{8}").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"\displaystyle \lim_{x\to \infty}\frac{8x^3  +3x^4 - 4}{5x^2 + 8x^4 - 9}").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"\lim_{x\to \infty}\frac{\frac{8}{x}  + 3 - \frac{4}{x^4} }{ \frac{5}{x^2} + 8 - \frac{9}{x^4} }", r"=\frac{3}{8}").scale(0.8).next_to(eq2, RIGHT)

        

        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Transform(rhs1, rhs1b))
        self.wait(5)
        self.play(Transform(rhs1, rhs1c))
        self.wait(5)
        self.play(Transform(rhs1, rhs1d))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2[0]))
        self.wait(5)
        self.play(Write(rhs2[1]))





        self.wait(10)     


class LimitZero(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute  } \displaystyle \lim_{x\to -\infty} \frac{2x^2  - x^3 +5}{2x^3 + 7x^5 - 2x}, \displaystyle \lim_{x\to \infty} \frac{2x^2  - x^3 +5}{2x^3 + 7x^5 - 2x}", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP+LEFT)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").next_to(eq2, DOWN*5)




        lhs1 = MathTex(r"\displaystyle \lim_{x\to -\infty} \frac{2x^2  - x^3 +5}{2x^3 + 7x^5 - 2x}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\lim_{x\to -\infty} \frac{ \frac{2x^2}{x^3}  - \frac{x^3}{x^3} + \frac{5}{x^3} }{ \frac{2x^3}{x^3} + \frac{7x^5}{x^3} - \frac{2x}{x^3} }").scale(0.8).next_to(eq1, RIGHT)

        
        rhs1b = MathTex(r"\lim_{x\to -\infty} \frac{ \frac{2}{x}  - 1 + \frac{5}{x^3} }{ 2 + 7x^2 - \frac{2}{x^2} }").scale(0.8).next_to(eq1, RIGHT)
        rhs1c = MathTex(r"\lim_{x\to -\infty} \frac{0 -1 + 0 }{ 2 + 7x^2 - 0 }").scale(0.8).next_to(eq1, RIGHT)
        rhs1d = MathTex(r"0").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"\displaystyle \lim_{x\to \infty} \frac{2x^2  - x^3 +5}{2x^3 + 7x^5 - 2x}").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"\lim_{x\to \infty} \frac{0 -1 + 0 }{ 2 + 7x^2 - 0 }", r"=0").scale(0.8).next_to(eq2, RIGHT)

        

        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Transform(rhs1, rhs1b))
        self.wait(5)
        self.play(Transform(rhs1, rhs1c))
        self.wait(5)
        self.play(Transform(rhs1, rhs1d))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2[0]))
        self.wait(5)
        self.play(Write(rhs2[1]))





        self.wait(10)                
        


        








        


        
        



        



  
       