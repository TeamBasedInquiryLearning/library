#%%manim -ql LIPoly

from manim import *





class AskQuestion(Scene):
    def construct(self):
     #3d stuff

        prose1 = MathTex(r"\text{Consider a  12 cm by 12 cm sheet of paper.}", color=TEAL).shift(UP*2)
        prose2 = MathTex(r"\text{A }x\times x\text{ square is cut out of each corner.}", color=TEAL).next_to(prose1, DOWN)
        prose3 = MathTex(r"\text{ The sides are then folded up to form a box. }", color=TEAL).next_to(prose2, DOWN)

        question1 = MathTex(r"\text{What should }x\text{ be to maximize the box's volume?}", color=RED).next_to(prose3, DOWN*2)
        #question2 = MathTex(r"\text{in the river to reach the Child as quickly as possible?}", color=RED).next_to(question1, DOWN)
        #question3 = MathTex(r"\text{in each to maximize the output of the factory?}", color=RED).next_to(question2, DOWN)


        self.play(Write(prose1), Write(prose2), Write(prose3))
        self.wait(8)
        self.play(Write(question1),)
        self.wait(8)
        self.play(FadeOut(prose1), FadeOut(prose2), FadeOut(prose3),  FadeOut(question1), )

        Paper = Polygon([-2, -2, 0], [2, -2, 0], [2, 2, 0], [-2,2,0], color=BLUE)
        Paper.set_fill(BLUE, 0.5)

        lP1 = MathTex(r"12", color=BLUE).scale(0.5).next_to([0,-2,0], DOWN)
        lP2 = MathTex(r"12", color=BLUE).scale(0.5).next_to([2,0,0], RIGHT)
        lP3 = MathTex(r"12", color=BLUE).scale(0.5).next_to([0,2,0], UP)
        lP4 = MathTex(r"12", color=BLUE).scale(0.5).next_to([-2,0,0], LEFT)

        S1 = Polygon([-2, -2, 0], [-1, -2, 0], [-1, -1, 0], [-2,-1,0], color=BLACK)
        S1.set_fill(BLACK, 1)
        S2 = Polygon([1, -2, 0], [2, -2, 0], [2, -1, 0], [1,-1,0], color=BLACK)
        S2.set_fill(BLACK, 1)
        S3 = Polygon([-2, 1, 0], [-1, 1, 0], [-1, 2, 0], [-2,2,0], color=BLACK)
        S3.set_fill(BLACK, 1)
        S4 = Polygon([1, 1, 0], [2, 1, 0], [2, 2, 0], [1,2,0], color=BLACK)
        S4.set_fill(BLACK, 1)

        lS11 = MathTex(r"x", color=PURPLE).scale(0.5).next_to([-1.5,-1,0], DOWN)
        lS12 = MathTex(r"x", color=PURPLE).scale(0.5).next_to([-1,-1.5,0], LEFT)
        lS21 = MathTex(r"x", color=PURPLE).scale(0.5).next_to([1.5,-1,0], DOWN)
        lS22 = MathTex(r"x", color=PURPLE).scale(0.5).next_to([1,-1.5,0], RIGHT)
        lS31 = MathTex(r"x", color=PURPLE).scale(0.5).next_to([1.5,1,0], UP)
        lS32 = MathTex(r"x", color=PURPLE).scale(0.5).next_to([1,1.5,0], RIGHT)
        lS41 = MathTex(r"x", color=PURPLE).scale(0.5).next_to([-1.5,1,0], UP)
        lS42 = MathTex(r"x", color=PURPLE).scale(0.5).next_to([-1,1.5,0], LEFT)


        B1=DashedLine([-1,-1,0], [1,-1,0], color=YELLOW)
        B2=DashedLine([1,-1,0], [1,1,0], color=ORANGE)
        B3=DashedLine([1,1,0], [-1,1,0], color=YELLOW)
        B4=DashedLine([-1,1,0], [-1,-1,0], color=ORANGE)

        lB1=MathTex(r"12-2x", color=YELLOW).scale(0.5).next_to([0,-1,0], DOWN)
        lB2=MathTex(r"12-2x", color=ORANGE).scale(0.5).next_to([1,0,0], RIGHT)
        lB3=MathTex(r"12-2x", color=YELLOW).scale(0.5).next_to([0,1,0], UP)
        lB4=MathTex(r"12-2x", color=ORANGE).scale(0.5).next_to([-1,0,0], LEFT)
        



        

        self.play(Create(Paper))
        self.play(Write(lP1), Write(lP2), Write(lP3), Write(lP4))
        self.wait(5)
        self.play(FadeOut(lP1, lP2, lP3, lP4))
        self.play(Create(S1), Create(S2), Create(S3), Create(S4), Write(lS11), Write(lS12), Write(lS21), Write(lS22), 
            Write(lS31), Write(lS32), Write(lS41), Write(lS42), )
        self.wait(5)
        self.play(Create(B1), Create(B2), Create(B3), Create(B4), Write(lB1), Write(lB2), Write(lB3), Write(lB4),  )
        
        self.wait(5)


        caption1 = MathTex(r"\text{Maximize: } V(x)=", r"\text{Length}", "\cdot",r"\text{Width}", r"\cdot", r"\text{Height}.", r", x\in[0,6]").scale(0.8).to_edge(DOWN)
        caption1[1].set_color(YELLOW)
        caption1[3].set_color(ORANGE)
        caption1[5].set_color(PURPLE)

        caption2 = MathTex(r"\text{Maximize: } V(x)=", r"\text{Length}", "\cdot",r"\text{Width}", r"\cdot", r"x.", r", x\in[0,6]").scale(0.8).to_edge(DOWN)
        caption2[1].set_color(YELLOW)
        caption2[3].set_color(ORANGE)
        caption2[5].set_color(PURPLE)


        caption3 = MathTex(r"\text{Maximize: } V(x)=", r"(12-2x)", "\cdot",r"(12-2x)", r"\cdot", r"x.", r", x\in[0,6]").scale(0.8).to_edge(DOWN)
        caption3[1].set_color(YELLOW)
        caption3[3].set_color(ORANGE)
        caption3[5].set_color(PURPLE)

        caption4 = MathTex(r"\text{Maximize: } V(x)=4", r"(6-x)", "\cdot",r"(6-x)", r"\cdot", r"x.", r", x\in[0,6]").scale(0.8).to_edge(DOWN)
        caption4[1].set_color(YELLOW)
        caption4[3].set_color(ORANGE)
        caption4[5].set_color(PURPLE)

        caption5 = MathTex(r"\text{Maximize: } V(x)=4", r"(x^3-12x^2+36x)", r", x\in[0,6]").scale(0.8).to_edge(DOWN)

        self.play(Write(caption1))
        self.wait(5)
        self.play(Transform(caption1, caption2))
        self.wait(5)
        self.play(Transform(caption1, caption3))
        self.wait(5)
        self.play(Transform(caption1, caption4))
        self.wait(5)
        self.play(Transform(caption1, caption5))
        self.wait(10)





class FindCP(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Minimize: } T(x)=", r"\frac{128-x}{17}", "+",r"\frac{\sqrt{x^2+576}}{15}", r", x\in[0,128]").scale(0.8).to_edge(UP)
        title1[1].set_color(YELLOW)
        title1[3].set_color(ORANGE)


        caption1 = MathTex(r"x =2, 6 \text{ are the critical numbers. }" ,color="ORANGE").scale(0.8).to_edge(DOWN)
        caption2 = MathTex(r"V(x) \text{ is maximized when } x=2." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        caption3 = MathTex(r"\text{The volume of the box is 128 cm}^3." ,color="ORANGE").scale(0.8).to_edge(DOWN)  


        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"V(x)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"4(x^3-12x^2+36x)",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"V'(x)").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"4(3x^2-24x^2+36)",).scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"0", color="RED").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"12(x^2-8x^2+12)",).scale(0.8).next_to(eq3, RIGHT)

        
        rhs4 = MathTex(r"12(x-2)(x-6)",).scale(0.8).next_to(eq4, RIGHT)

        lhs5 = MathTex(r"x",).scale(0.8).next_to(eq4, LEFT)
        rhs5 = MathTex(r"2, 6",).scale(0.8).next_to(eq4, RIGHT)

        

        self.play(Write(lhs1), Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Write(lhs3))
        self.wait(5)
        self.play( Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(
            FadeOut(rhs3),
            rhs4.animate.next_to(eq3, RIGHT),
            Write(lhs5), Write(rhs5)
            )
        self.wait(5)
        
        self.play(Write(caption1))
        self.play(FadeOut(lhs1, rhs1, eq1, lhs2, lhs3, rhs2, eq2, rhs4, eq3, lhs5, rhs5, eq4, ),
            )

        lhs1 = MathTex(r"V(0)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"4(6-0)^2(0)", r"=0\text{ cm}^3.").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"V(2)").scale(0.8).next_to(eq2, LEFT)
        rhs2 =  MathTex(r"4(6-2)^2(2)", r"=128\text{ cm}^3.").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"V(6)").scale(0.8).next_to(eq3, LEFT)
        rhs3 =  MathTex(r"4(6-6)^2(6)", r"=0\text{ cm}^3.").scale(0.8).next_to(eq3, RIGHT)

        self.play(Write(lhs1), Write(lhs3))
        self.wait(3)
        self.play(Write(eq1), Write(eq3), Write(rhs1[0]), Write(rhs3[0]))
        self.wait(2)
        self.play(Write(rhs1[1]), Write(rhs3[1]))
        self.wait(2)

        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2[0]))
        self.wait(2)
        self.play(Write(rhs2[1]))

        
        self.wait(5)
        self.play(FadeOut(eq1, eq3, lhs1, lhs3, rhs1, rhs3),
            lhs2.animate.set_color(BLUE),
            rhs2.animate.set_color(BLUE),
            )
        self.wait(3)
        self.play(Transform(caption1, caption2))
        

        
        self.wait(5)
        self.play(Transform(caption1, caption3))
        self.wait(10)






        


       





        
        



        


        
        



        



  
       