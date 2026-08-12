#%%manim -ql LIPoly

from manim import *










class FindPosition(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the position function of a particle } s(t), \text{ if: } a(t)=2t-1, v(2)=1, s(0)=-5.", color=BLUE).scale(0.6).to_edge(UP)
        caption1 = MathTex(r"s(t)=\frac{1}{3}t^3+\frac{1}{2}t^2-t-5." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"v'(t)=", "a(t)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"2t-1",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"s'(t)=", "v(t)").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"t^2-t", "+C_1").scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(BLUE)
        rhs2a = MathTex(r"t^2-t-1").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex("1=", r"v(2)").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"2^2-2", "+C_1").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(BLUE)
        lhs3a = MathTex(r"C_1").scale(0.8).next_to(eq3, LEFT)
        rhs3a = MathTex(r"1-2^2+2").scale(0.8).next_to(eq3, RIGHT)
        rhs3b = MathTex(r"-1").scale(0.8).next_to(eq3, RIGHT)


        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1[1]), Write(eq1), Write(rhs1))
        self.wait(2)
        self.play(Write(lhs1[0]))
        self.wait(5) 
        self.play(Write(lhs2[1]))       
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))        
        self.wait(4)
        self.play(Write(lhs3[1]))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3))
        self.play(Write(lhs3[0]))
        self.wait(3)
        self.play(Transform(lhs3, lhs3a), Transform(rhs3, rhs3a))
        self.wait(2)
        self.play(Transform(rhs3, rhs3b))
        self.wait(3)
        self.play(Transform(rhs2, rhs2a))
        self.wait(3)
        self.play(
            FadeOut(rhs3,lhs3, eq3), Write(lhs2[0])
            )


        lhs3 = MathTex("s(t)").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"\frac{1}{3}t^3+\frac{1}{2}t^2-t", "+C_2").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(BLUE)
        rhs3a = MathTex(r"\frac{1}{3}t^3+\frac{1}{2}t^2-t-5").scale(0.8).next_to(eq3, RIGHT)

        lhs4 = MathTex("-5=", r"s(0)").scale(0.8).next_to(eq4, LEFT)
        rhs4 = MathTex(r"\frac{1}{3}(0)^3+\frac{1}{2}(0)^2-(0)", "+C_2").scale(0.8).next_to(eq4, RIGHT)
        rhs4[1].set_color(BLUE)
        lhs4a = MathTex(r"C_2").scale(0.8).next_to(eq4, LEFT)
        rhs4a = MathTex(r"0-5").scale(0.8).next_to(eq4, RIGHT)
        rhs4b = MathTex(r"-5").scale(0.8).next_to(eq4, RIGHT)


        self.play(Write(lhs3))       
        self.wait(3)
        self.play(Write(eq3), Write(rhs3))        
        self.wait(4)
        self.play(Write(lhs4[1]))
        self.wait(3)
        self.play(Write(eq4), Write(rhs4))
        self.play(Write(lhs4[0]))
        self.wait(3)
        self.play(Transform(lhs4, lhs4a), Transform(rhs4, rhs4a))
        self.wait(1)
        self.play(Transform(rhs4, rhs4b))
        self.wait(3)
        self.play(Transform(rhs3, rhs3a))
        self.wait(3)
        self.play(
            FadeOut(rhs4,lhs4, eq4), Write(caption1)
            )
        self.wait(10)

        
        






        


       





        
        



        


        
        



        



  
       