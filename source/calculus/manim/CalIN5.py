#%%manim -ql LIPoly

from manim import *










class FindInt1(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the definite integral } \displaystyle \int_{\frac{2}{3}\pi}^{\frac{5}{6}\pi} 4\cot(x)\csc(x)\,dx.", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\displaystyle \int_{\frac{2}{3}\pi}^{\frac{5}{6}\pi} 4\cot(x)\csc(x)\,dx").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"4\left(-\csc(x)|_{\frac{2}{3}\pi}^{\frac{5}{6}\pi}\right)",).scale(0.8).next_to(eq1, RIGHT)

        
        rhs2 = MathTex(r"-4\csc\left(\frac{5}{6}\pi\right) - \left(  -4\csc\left(\frac{2}{3}\pi\right)  \right)").scale(0.8).next_to(eq2, RIGHT)
        rhs2a = MathTex(r"4\csc\left(\frac{2}{3}\pi\right) -4\csc\left(\frac{5}{6}\pi\right)").scale(0.8).next_to(eq2, RIGHT)
        rhs3 =MathTex(r"{4 \over \sin\left(\frac{2}{3}\pi\right)} - {4 \over \sin\left(\frac{5}{6}\pi\right)}").scale(0.8).next_to(eq3, RIGHT)

        rhs4 = MathTex(r"4{2 \over \sqrt{3}} - 4\frac{2}{1}.").scale(0.8).next_to(eq4, RIGHT)
        rhs4a = MathTex(r"{8 \over \sqrt{3}} - 8.").scale(0.8).next_to(eq4, RIGHT)
        


        
        self.play(Write(title1))
        self.wait(3)
        self.play(Write(lhs1),)
        self.wait(5)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Transform(rhs2, rhs2a))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(5)
        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4, title1)
            )
        self.wait(2)


        title1 = MathTex(r"\text{Find  the definite integral } \displaystyle \int_1^5 \frac{e^{2x}}{4}\,dx.", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\displaystyle \int_1^5 \frac{e^{2x}}{4}\,dx").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{1}{4} \Biggl(", r"\frac{1}{2} ", r" e^{2x}|_1^5\Biggr)",).scale(0.8).next_to(eq1, RIGHT)

        
        rhs2 = MathTex(r"\frac{1}{4} \left( \frac{1}{2}e^5 - \frac{1}{2}e^1 \right) ").scale(0.8).next_to(eq2, RIGHT)
        rhs3 =MathTex(r"\frac{e^5}{8} - \frac{e}{8}. ").scale(0.8).next_to(eq3, RIGHT)

        


        
        self.play(Write(title1))
        self.wait(3)
        self.play(Write(lhs1),)
        self.wait(5)
        self.play(Write(eq1), Write(rhs1[0]), Write(rhs1[2]))
        self.wait(3)
        self.play(Write(rhs1[1]))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)

        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3,  title1)
            )
        self.wait(2)


        title1 = MathTex(r"\text{Find  the definite integral } \displaystyle \int_{-2}^1 6x^3-3x^2+9x\,dx.", color=TEAL).scale(0.6).to_edge(UP)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\displaystyle \int_{-2}^1 6x^3-3x^2+9x\,dx").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\Biggl(6\frac{1}{4}x^4-3\frac{1}{3}x^3 + 9\frac{1}{2}x^2 |_{-2}^1\Biggr)",).scale(0.8).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"\Biggl(\frac{3}{2}x^4-x^3 + \frac{9}{2}x^2 |_{-2}^1\Biggr)",).scale(0.8).next_to(eq1, RIGHT)

        
        rhs2 = MathTex(r"\left( \frac{3}{2}2^4-2^3 + \frac{9}{2}2^2 \right) - \left( \frac{3}{2}(-1)^4-(-1)^3 + \frac{9}{2}(-1)^2 \right)").scale(0.8).next_to(eq2, RIGHT)
        
        rhs3 = MathTex(r"\left( \frac{3}{2}16-8 + \frac{9}{2}4 \right) - \left( \frac{3}{2}(1)-(-1) + \frac{9}{2}(1) \right)").scale(0.8).next_to(eq3, RIGHT)
        rhs3a = MathTex(r"\left( 24-8 +18 \right) - \left( \frac{3}{2}+ 1 + \frac{9}{2} \right)").scale(0.8).next_to(eq3, RIGHT)
        rhs3b = MathTex(r"\left( 34 \right) - \left( 7 \right)").scale(0.8).next_to(eq3, RIGHT)

        rhs4 = MathTex(r"27.").scale(0.8).next_to(eq4, RIGHT)


        


        
        self.play(Write(title1))
        self.wait(3)
        self.play(Write(lhs1),)
        self.wait(5)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Transform(rhs1, rhs1a))
        self.wait(5)
        
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)

        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(3)
        self.play(Transform(rhs3, rhs3b))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(10)



        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3,  eq4, rhs4,  title1)
            )
        


        
        






        


       





        
        



        


        
        



        



  
       