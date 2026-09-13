#%%manim -ql LIPoly

from manim import *







class Part1(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find   }y'\text{ given } 4y^5+4x^3-2\sin(y)=3", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        #caption1 = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        #caption2 = MathTex(r"\text{Product Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        #caption3 = MathTex(r"\text{Quotient Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.8).shift(UP*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"\frac{d}{dx}\Big[", r"4y^5+4x^3-2\sin(y)", r"\Big]", color="RED").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{d}{dx}\Big[", r"3", r"\Big]", color="RED").scale(0.8).next_to(eq1, RIGHT)

        lhs1[1].set_color(WHITE)
        rhs1[1].set_color(WHITE)

        lhs2 = MathTex(r"20y^4", r"y'", "+12x^2-2\cos(y)", r"y'").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"0").scale(0.8).next_to(eq2, RIGHT)
        lhs2[1].set_color(RED)
        lhs2[3].set_color(RED)

        lhs3 = MathTex(r"y'",  r"(20y^4-2\cos(y))").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"-12x^2").scale(0.8).next_to(eq3, RIGHT)
        lhs3[0].set_color(RED)
        #lhs2[3].set_color(WHITE)

        lhs4 = MathTex(r"y'",  color="RED").scale(0.8).next_to(eq4, LEFT)
        rhs4 = MathTex(r"\frac{-12x^2}{20y^4-2\cos(y)}").scale(0.8).next_to(eq4, RIGHT)
        rhs4a = MathTex(r"\frac{6x^2}{\cos(y)-10y^4}").scale(0.8).next_to(eq4, RIGHT)


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1[1]),Write(eq1), Write(rhs1[1]))
        self.wait(5)
        self.play(Write(lhs1[0]), Write(lhs1[2]), Write(rhs1[0]), Write(rhs1[2]))
        self.wait(3)
        
        self.play(Write(lhs2),Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(lhs3),Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(lhs4),Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10)






class Part2(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find   }y'\text{ given } 4x\cos(y)=e^x", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        #caption1 = MathTex(r"\text{Chain Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        #caption2 = MathTex(r"\text{Product Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)      
        #caption3 = MathTex(r"\text{Quotient Rule!} ", color=YELLOW).scale(0.8).to_edge(DOWN)  
        
        eq1 = MathTex(r"=").scale(0.8).shift(UP*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)




        lhs1 = MathTex(r"\frac{d}{dx}\Big[", r"4x\cos(y)", r"\Big]", color="RED").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{d}{dx}\Big[", r"e^x", r"\Big]", color="RED").scale(0.8).next_to(eq1, RIGHT)

        lhs1[1].set_color(WHITE)
        rhs1[1].set_color(WHITE)

        lhs2 = MathTex(r"4x\frac{d}{dx}[\cos(y)] + \cos(y)\frac{d}{dx}[4x]").scale(0.8).next_to(eq2, LEFT)
        lhs2a = MathTex(r"4x(-\sin(y))", r"y'", r" + \cos(y)4").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"e^x").scale(0.8).next_to(eq2, RIGHT)
        lhs2a[1].set_color(RED)
        #lhs2[3].set_color(RED)

        lhs3 = MathTex(r"-4x\sin(y)",  r"y'").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"e^x-4\cos(y)").scale(0.8).next_to(eq3, RIGHT)
        lhs3[1].set_color(RED)
        #lhs2[3].set_color(WHITE)

        lhs4 = MathTex(r"y'",  color="RED").scale(0.8).next_to(eq4, LEFT)
        rhs4 = MathTex(r"\frac{e^x-4\cos(y)}{-4x\sin(y)}").scale(0.8).next_to(eq4, RIGHT)
        rhs4a = MathTex(r"\frac{4\cos(y)-e^x}{4x\sin(y)}").scale(0.8).next_to(eq4, RIGHT)


        

        




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs1[1]),Write(eq1), Write(rhs1[1]))
        self.wait(5)
        self.play(Write(lhs1[0]), Write(lhs1[2]), Write(rhs1[0]), Write(rhs1[2]))
        self.wait(5)
        
        self.play(Write(lhs2),Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Transform(lhs2, lhs2a))
        self.wait(5)

        self.play(Write(lhs3),Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(lhs4),Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10)



        



  
       