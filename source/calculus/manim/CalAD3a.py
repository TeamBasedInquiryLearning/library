#%%manim -ql LIPoly

from manim import *





class AskQuestion(Scene):
    def construct(self):
     #3d stuff

        prose1 = MathTex(r"\text{A person  6.1 feet tall is standing between a light on the ground and a wall.}", color=TEAL).scale(0.6).shift(UP*2)
        prose2 = MathTex(r"\text{They are 50 feet from light, 30 feet from wall.}", color=TEAL).scale(0.6).next_to(prose1, DOWN)
        prose3 = MathTex(r"\text{They walk towards the light at 2.1 feet/second. }", color=TEAL).scale(0.6).next_to(prose2, DOWN)

        question1 = MathTex(r"\text{How is the height of their shadow on the wall changing? }", color=RED).scale(0.6).next_to(prose3, DOWN*2)
        #question2 = MathTex(r"\text{in capital and labor, how much should be invested}", color=RED).next_to(question1, DOWN)
        #question3 = MathTex(r"\text{in each to maximize the output of the factory?}", color=RED).next_to(question2, DOWN)


        self.play(Write(prose1), Write(prose2), Write(prose3))
        self.wait(8)
        self.play(Write(question1))
        self.wait(8)
        self.play(FadeOut(prose1), FadeOut(prose2), FadeOut(prose3),  FadeOut(question1), )

class ShowCars(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  }\frac{dy}{dt}.", r"\ \ x=50,  \frac{dx}{dt}=-2.1,", r"y=9.76").scale(0.8)        
        title1.to_edge(UP)
        title1[1].set_color(RED)
        title1[2].set_color(ORANGE)

        

        L1=Line([-4,0,0], [-2,0,0], color="YELLOW")
        L2=Line([-6,0,0], [-2,2,0], color="YELLOW")
        L3=Line([-2,0,0], [-2,2,0], color="GREEN")

        Person = Line([-4,0,0], [-4,1,0], color="BLUE")

        L4=Line([-6,0,0], [-4,0,0], color="RED")


        label1=MathTex(r"6.1", color="BLUE" ).scale(0.6).next_to(Person, RIGHT)
        label2=MathTex(r"y", color="GREEN").scale(0.6).next_to(L3, RIGHT)
        label3=MathTex(r"x", color="RED").scale(0.6).next_to(L4, DOWN)
        label4=MathTex(r"80-x", ).scale(0.6).next_to(L1, DOWN)

        
        eq1 = MathTex(r"=").shift(RIGHT*2, UP*2)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").next_to(eq2, DOWN*5)

        lhs1 = MathTex(r"\frac{d}{dt}\Big[", r"\frac{6.1}{x}", r"\Big]" ,color=BLUE).scale(0.7).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{d}{dt}\Big[", r"\frac{y}{80}", r"\Big]", color=BLUE).scale(0.7).next_to(eq1, RIGHT)
        lhs1a = MathTex(r"\frac{d}{dt}\Big[", r"488", r"\Big]" ,color=BLUE).scale(0.7).next_to(eq1, LEFT)
        rhs1a = MathTex(r"\frac{d}{dt}\Big[", r"xy", r"\Big]", color=BLUE).scale(0.7).next_to(eq1, RIGHT)

        lhs1a[0].set_color(RED)
        lhs1a[2].set_color(RED)
        rhs1a[0].set_color(RED)
        rhs1a[2].set_color(RED)
        
        lhs2 = MathTex(r"0", color=BLUE).scale(0.7).next_to(eq2, LEFT)
        rhs2 = MathTex(r"y", r"\frac{dx}{dt}+", r"x", r"\frac{dy}{dt}", color=BLUE).scale(0.7).next_to(eq2, RIGHT)
        rhs2a = MathTex(r"9.76", r"\cdot -2.1", r"+", r"50", r"\frac{dy}{dt}", color=RED).scale(0.7).next_to(eq2, RIGHT)
        rhs2a[4].set_color(BLUE)
        #rhs2a[3].set_color(BLUE)

        #lhs2a = MathTex(r"2(", r"100", r")\frac{dD}{dt}", color=BLUE).scale(0.7).next_to(eq2, LEFT)
        #lhs2a[1].set_color(ORANGE)

        
        lhs3 = MathTex(r"\frac{dy}{dt}", color=BLUE).scale(0.7).next_to(eq3, LEFT)
        rhs3 = MathTex(r"\frac{9.76\cdot 2.1}{50}", color=BLUE).scale(0.7).next_to(eq3, RIGHT)
        rhs3a = MathTex(r"0.40992\ \text{feet/second}", color=BLUE).scale(0.7).next_to(eq3, RIGHT)
        



        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1[0], title1[1])
        self.wait(2)
        self.play(Create(L1), Create(L2), Create(L3), Create(L4), Create(Person))
        self.wait(2)
        self.play(Create(label1), Create(label2), Create(label3), Create(label4))
        self.wait(5)



       

        

       

        
        self.play(Write(lhs1[1]))
        self.wait(2)
        self.play(Write(eq1), Write(rhs1[1]))
        self.wait(5)

        self.play(Transform(lhs1[1], lhs1a[1]), Transform(rhs1[1], rhs1a[1]))
        self.wait(5)
        self.play(Write(title1[2]))
        self.wait(5)
        self.play(Write(rhs1a[0]), Write(rhs1a[2]), Write(lhs1a[0]), Write(lhs1a[2]))
        self.wait(5)
        self.play(Write(lhs2))
        self.wait(2)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Transform(rhs2, rhs2a))
        self.wait(5)
        #self.play(Transform(lhs2, lhs2a))
        #self.wait(5)
        self.play(Write(lhs3))
        self.wait(2)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Transform(rhs3, rhs3a))
        self.wait(15)



class FindExtrema(Scene):
    def construct(self):

        
        title1 = MathTex(r"\text{Maximize }", r"f(K,R)=65K^{\frac{4}{5}}R^{\frac{1}{5}}}", r"\text{ subject to }", r"K+R=165.").scale(0.8)        
        title1.to_edge(UP)

        title1[1].set_color(BLUE)
        title1[3].set_color(YELLOW)
        

        eqr1 = MathTex(r"=").shift(LEFT*3, UP*1.5)
        lhsr1 = MathTex(r"52 K^{-\frac{1}{5}}R^{\frac{1}{5}}").scale(0.7).next_to(eqr1, LEFT)
        rhsr1 = MathTex(r"\lambda").scale(0.7).next_to(eqr1, RIGHT)

        eqr2 = MathTex(r"=").next_to(eqr1, DOWN*3)
        lhsr2 = MathTex(r"13 K^{\frac{4}{5}}R^{-\frac{4}{5}}").scale(0.7).next_to(eqr2, LEFT)
        rhsr2 = MathTex(r"\lambda").scale(0.7).next_to(eqr2, RIGHT)

        eqr3 = MathTex(r"=").next_to(eqr2, DOWN*3)
        lhsr3 = MathTex(r"K+R").scale(0.7).next_to(eqr3, LEFT)
        rhsr3 = MathTex(r"165").scale(0.7).next_to(eqr3, RIGHT)

        eqr4 = MathTex(r"=").next_to(eqr3, DOWN*3)
        lhsr4 = MathTex(r"K").scale(0.7).next_to(eqr4, LEFT)
        rhsr4 = MathTex(r"132").scale(0.7).next_to(eqr4, RIGHT)

        eqr5 = MathTex(r"=").next_to(eqr4, DOWN*3)
        lhsr5 = MathTex(r"R").scale(0.7).next_to(eqr5, LEFT)
        rhsr5 = MathTex(r"33").scale(0.7).next_to(eqr5, RIGHT)

        eqr6 = MathTex(r"=").next_to(eqr5, DOWN*3)
        lhsr6 = MathTex(r"\lambda").scale(0.7).next_to(eqr6, LEFT)
        rhsr6 = MathTex(r"26 \cdot 8^{\frac{1}{5}}").scale(0.7).next_to(eqr6, RIGHT)

        eq1 = MathTex(r"=").shift(RIGHT*2, UP*1.5)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*3)
        eq2a = MathTex(r"\approx").next_to(eq1, DOWN*3)
        eq3 = MathTex(r"=").next_to(eq2, DOWN*3)

        lhs1 = MathTex(r"52 K^{-\frac{1}{5}}R^{\frac{1}{5}}").next_to(eq1, LEFT)
        rhs1 = MathTex(r"13 K^{\frac{4}{5}}R^{-\frac{4}{5}}").next_to(eq1, RIGHT)

        lhs2 = MathTex(r"4 K^{-\frac{1}{5}}R^{\frac{1}{5}}").next_to(eq1, LEFT)
        rhs2 = MathTex(r"K^{\frac{4}{5}}R^{-\frac{4}{5}}").next_to(eq1, RIGHT)

        lhs3 = MathTex(r"4 R^{\frac{1}{5}}").next_to(eq1, LEFT)
        rhs3 = MathTex(r"KR^{-\frac{4}{5}}").next_to(eq1, RIGHT)

        lhs4 = MathTex(r"4 R").next_to(eq1, LEFT)
        rhs4 = MathTex(r"K").next_to(eq1, RIGHT)

        lhs5 = MathTex(r"4 R + R").next_to(eq2, LEFT)
        rhs5 = MathTex(r"165").next_to(eq2, RIGHT)

        lhs6 = MathTex(r"5R").next_to(eq2, LEFT)
        rhs6 = MathTex(r"165").next_to(eq2, RIGHT)

        lhs7 = MathTex(r"R").next_to(eq2, LEFT)
        rhs7 = MathTex(r"33").next_to(eq2, RIGHT)

        lhs8 = MathTex(r"4(33)").next_to(eq1, LEFT)
        lhs9 = MathTex(r"132").next_to(eq1, LEFT)

        lhs10 = MathTex(r"\lambda").next_to(eq3, LEFT)
        rhs10 = MathTex(r"52(132)^{-\frac{1}{5}}(33)^{\frac{1}{5}}").next_to(eq3, RIGHT)

        rhs11 = MathTex(r"26 \cdot 8^{\frac{1}{5}}").next_to(eq3, RIGHT)

        lhs12 = MathTex(r"f(132, 33)").next_to(eq1, LEFT)
        rhs12 = MathTex(r"65(132)^{\frac{4}{5}}(33)^{\frac{1}{5}}").next_to(eq1, RIGHT)
        rhs13 = MathTex(r"6502.47").next_to(eq2, RIGHT)


        self.add(title1)
        self.play(Write(eqr1), Write(lhsr1), Write(rhsr1))
        self.play(Write(eqr2), Write(lhsr2), Write(rhsr2))
        self.play(Write(eqr3), Write(lhsr3), Write(rhsr3))
        self.wait(4)
        self.play(Write(eqr4), Write(lhsr4))
        self.play(Write(eqr5), Write(lhsr5))
        self.play(Write(eqr6), Write(lhsr6))
        self.wait(4)
        self.play(lhsr1.animate.scale(1.5), rhsr1.animate.scale(1.5), lhsr2.animate.scale(1.5), rhsr2.animate.scale(1.5))
        self.wait(3)
        self.play(Write(eq1), Write(lhs1), Write(rhs1))
        self.play(lhsr1.animate.scale(2/3), rhsr1.animate.scale(2/3), lhsr2.animate.scale(2/3), rhsr2.animate.scale(2/3))
        self.wait(3)
        self.play(Transform(lhs1, lhs2), Transform(rhs1, rhs2))
        self.wait(2)
        self.play(Transform(lhs1, lhs3), Transform(rhs1, rhs3))
        self.wait(2)
        self.play(Transform(lhs1, lhs4), Transform(rhs1, rhs4))
        self.wait(3)

        self.play(lhsr3.animate.scale(1.5), rhsr3.animate.scale(1.5))
        self.wait(3)
        self.play(Write(eq2), Write(lhs5), Write(rhs5))
        self.play(lhsr3.animate.scale(2/3), rhsr3.animate.scale(2/3))
        self.wait(3)
        self.play(Transform(lhs5, lhs6), Transform(rhs5, rhs6))
        self.wait(2)
        self.play(Transform(lhs5, lhs7), Transform(rhs5, rhs7))
        self.wait(3)
        self.play(Write(rhsr5), Transform(lhs1, lhs8))
        self.wait(2)
        self.play(Write(rhsr4), Transform(lhs1, lhs9))
        self.wait(5)
        self.play(lhsr1.animate.scale(1.5), rhsr1.animate.scale(1.5))
        self.play(Write(lhs10), Write(eq3), Write(rhs10))
        self.play(lhsr1.animate.scale(2/3), rhsr1.animate.scale(2/3))
        self.wait(3)
        self.play(Transform(rhs10, rhs11))
        self.play(Write(rhsr6))
        self.wait(2)
        self.play(FadeOut(lhs1, rhs1, eq1, eq2, eq3, rhs10, lhs10, lhs5, rhs5))
        self.play(Write(lhs12))
        self.wait(2)
        self.play(Write(rhs12), Write(eq1))
        self.wait(2)
        self.play(Write(eq2a), Write(rhs13))




        


       





        
        



        


        
        



        



  
       