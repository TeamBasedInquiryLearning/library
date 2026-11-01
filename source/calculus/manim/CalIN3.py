#%%manim -ql LIPoly

from manim import *










class FindAD(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the general antiderivative for } \frac{10}{x}.", color=BLUE).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"\text{The anti-derivatives are }\ln(|x|)", r"+C," , r" \text{(sorta)}." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        
        caption1[1].set_color(BLUE) 

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*1)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*3)
        eq3 = MathTex(r"=", color="GREEN").scale(0.8).next_to(eq2, DOWN*3)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*3)

        lhs1 = MathTex(r"f'(x)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{10}{x}",).scale(0.8).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"10x^{-1}",).scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"f(x)", color=GREEN).scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"10\ln(|x|)", r"+C", color=GREEN).scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(BLUE)

        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1), Write(eq1), Write(rhs1))
        self.wait(5)        
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(lhs3))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3[0]))
        self.wait(3)
        self.play(Write(rhs3[1]))
        self.wait(1)
        self.play(Write(caption1[0]))
        self.play(Write(caption1[1]))
        self.wait(2)
        self.play(Wiggle(rhs3[0]))
        self.wait(2)
        self.play(Write(caption1[2]))
        self.wait(5)
        self.play(
            FadeOut(rhs3,lhs3, eq3, rhs2, eq2, rhs1, eq1, lhs1, caption1),
            )

        title2 = MathTex(r"\text{Find the general antiderivative for } 2\sec^2(x).", color=BLUE).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"\text{The anti-derivatives are }2\tan(x)", r"+C."  ,color="ORANGE").scale(0.8).to_edge(DOWN)
        
        caption1[1].set_color(BLUE) 

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*1)
        eq2 = MathTex(r"=", color="GREEN").scale(0.8).next_to(eq1, DOWN*3)
        eq3 = MathTex(r"=", color="GREEN").scale(0.8).next_to(eq2, DOWN*3)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*3)

        lhs1 = MathTex(r"g'(x)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"2\sec^2(x)",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"g(x)", color=GREEN).scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"2\tan(x)", "+C", color=GREEN).scale(0.8).next_to(eq2, RIGHT)

        rhs2[1].set_color(BLUE)

        
        self.play(Transform(title1, title2))
        self.wait(3)
        self.play(Write(lhs1), Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(lhs2))    
        self.wait(3)    
        self.play(Write(eq2), Write(rhs2[0]))
        self.wait(2)
        self.play( Write(rhs2[1]))
        self.wait(1)
        self.play(Write(caption1))
        self.wait(5)
        self.play(
            FadeOut(lhs2, rhs2, eq2, rhs1, eq1, lhs1, caption1),
            )


        title3 = MathTex(r"\text{Find the general antiderivative for } 6x^4+10x^3+9x^2.", color=BLUE).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"\text{The anti-derivatives are }\frac{6}{5}x^5+\frac{5}{2}x^4+3x^3", r"+C."  ,color="ORANGE").scale(0.8).to_edge(DOWN)
        
        caption1[1].set_color(BLUE) 

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=", color="GREEN").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=", color="GREEN").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"h'(x)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"6x^4+10x^3+9x^2",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"h(x)", color=GREEN).scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"6\frac{1}{4+1}x^{4+1}+10\frac{1}{3+1}x^{3+1}+9\frac{1}{3}x^{2+1}", "+C", color=GREEN).scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(BLUE)

        rhs3 = MathTex(r"\frac{6}{5}x^{5}+\frac{10}{4}x^{4}+\frac{9}{3}x^{3}", "+C", color=GREEN).scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(BLUE)

        rhs3a = MathTex(r"\frac{6}{5}x^{5}+\frac{5}{2}x^{4}+3x^{3}", "+C", color=GREEN).scale(0.8).next_to(eq3, RIGHT)
        rhs3a[1].set_color(BLUE)

        
        self.play(Transform(title1, title3))
        self.wait(3)
        self.play(Write(lhs1), Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(lhs2))    
        self.wait(3)    
        self.play(Write(eq2), Write(rhs2[0]))
        self.wait(2)
        self.play(Write(rhs2[1]))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(1)
        self.play(Write(caption1))
        self.wait(5)
        self.play(
            FadeOut(rhs3,lhs2, eq3, rhs2, eq2, rhs1, eq1, lhs1, caption1),
            )


        title4 = MathTex(r"\text{Find the general antiderivative for } \frac{4}{x^{\frac{1}{7}}} -3e^x+6\sin(2x).", color=BLUE).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"\text{The anti-derivatives are }\frac{14}{3}x^{\frac{6}{7}}-3e^x-3\cos(x)", r"+C."  ,color="ORANGE").scale(0.8).to_edge(DOWN)
        
        caption1[1].set_color(BLUE) 

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=", color="GREEN").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=", color="GREEN").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"k'(x)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{4}{x^{\frac{1}{7}}} -3e^x+6\sin(2x)",).scale(0.8).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"4x^{-\frac{1}{7}} -3e^x+6\sin(2x)").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"k(x)").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"4\frac{1}{-\frac{1}{7}+1}x^{-\frac{1}{7}+1} -3e^x+ ", "(-3)", "\cos(2x)", "+C", color=GREEN).scale(0.8).next_to(eq3, RIGHT)
        rhs3[3].set_color(BLUE)

        rhs4 = MathTex(r"\frac{28}{6}x^{\frac{6}{7}}-3e^x-3\cos(2x)", "+C", color=GREEN).scale(0.8).next_to(eq4, RIGHT)
        rhs4[1].set_color(BLUE)

        rhs4a = MathTex(r"\frac{14}{3}x^{\frac{6}{7}}-3e^x-3\cos(2x)", "+C", color=GREEN).scale(0.8).next_to(eq4, RIGHT)
        rhs4a[1].set_color(BLUE)

        
        self.play(Transform(title1, title4))
        self.wait(3)
        self.play(Write(lhs1), Write(eq1), Write(rhs1))
        self.wait(3)    
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(lhs3))
        self.wait(2)
        self.play(Write(eq3), Write(rhs3[0]), Write(rhs3[2]))
        self.wait(5)
        self.play(Write(rhs3[1]))
        self.wait(3)
        self.play(Write(rhs3[3]))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(3)
        self.play(Transform(rhs4, rhs4a))
        self.wait(1)
        self.play(Write(caption1))
        self.wait(10)
        






        


       





        
        



        


        
        



        



  
       