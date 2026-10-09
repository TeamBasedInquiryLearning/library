#%%manim -ql LIPoly

from manim import *





class AskQuestion(Scene):
    def construct(self):
     #3d stuff

        prose1 = MathTex(r"\text{A Tiger is 'rescuing' a Child,  }", color=TEAL).shift(UP*2)
        prose2 = MathTex(r"\text{across a 24 yard river, 128 yards downstream.}", color=TEAL).next_to(prose1, DOWN)
        prose3 = MathTex(r"\text{ The tiger runs at 17 yards/sec and swims at 15 yard/sec. }", color=TEAL).next_to(prose2, DOWN)

        question1 = MathTex(r"\text{How far should the Tiger run before jumping }", color=RED).next_to(prose3, DOWN*2)
        question2 = MathTex(r"\text{in the river to reach the Child as quickly as possible?}", color=RED).next_to(question1, DOWN)
        #question3 = MathTex(r"\text{in each to maximize the output of the factory?}", color=RED).next_to(question2, DOWN)


        self.play(Write(prose1), Write(prose2), Write(prose3))
        self.wait(8)
        self.play(Write(question1), Write(question2))
        self.wait(8)
        self.play(FadeOut(prose1), FadeOut(prose2), FadeOut(prose3),  FadeOut(question1), FadeOut(question2))

        River = Polygon([-4, -1, 0], [4, -1, 0], [4, 1, 0], [-4,1,0], color=BLUE)
        River.set_fill(BLUE, 0.5)

        Tiger = Dot([-4,-1,0])
        labelT = MathTex(r"T").scale(0.5).next_to(Tiger, LEFT)

        Child = Dot([4,1,0])
        labelC = MathTex(r"C").scale(0.5).next_to(Child, UP)

        P = Dot([2,-1,0], color=RED)
        labelP = MathTex(r"P", color=RED).scale(0.5).next_to(P, DOWN)

        Run=DashedLine([-4,-1,0], [2,-1,0], color=YELLOW)
        Swim=DashedLine([2,-1,0], [4,1,0], color=ORANGE)

        labelR = MathTex(r"128-x", color=YELLOW).scale(0.5).next_to([-1,-1,0], DOWN)
        labelB = MathTex(r"x").scale(0.5).next_to([3,-1,0], DOWN)
        labelS = MathTex(r"\sqrt{x^2+24^2}", color=ORANGE).scale(0.5).next_to([3,0,0], (LEFT+UP)/1.4 )
        labelW = MathTex(r"24", color=BLUE).scale(0.5).next_to([4,0,0], RIGHT)

        self.play(Create(River))
        self.play(Create(Tiger), Write(labelT), Create(Child), Write(labelC))
        self.wait(2)
        self.play(Create(P), Write(labelP))
        self.play(Create(Run), Create(Swim))
        self.wait(2)
        self.play(Write(labelR), Write(labelB))
        self.wait(2)
        self.play(Write(labelW))
        self.wait(2)
        self.play(Write(labelS))
        self.wait(5)


        caption1 = MathTex(r"\text{Minimize: } T(x)=", r"\text{Time Running  }", "+",r"\text{Time Swimming  }", r", x\in[0,128]").scale(0.8).to_edge(DOWN)
        caption1[1].set_color(YELLOW)
        caption1[3].set_color(ORANGE)

        caption2 = MathTex(r"\text{Minimize: } T(x)=", r"\frac{128-x}{17}", "+",r"\text{Time Swimming  }", r", x\in[0,128]").scale(0.8).to_edge(DOWN)
        caption2[1].set_color(YELLOW)
        caption2[3].set_color(ORANGE)


        caption3 = MathTex(r"\text{Minimize: } T(x)=", r"\frac{128-x}{17}", "+",r"\frac{\sqrt{x^2+24^2}}{15}", r", x\in[0,128]").scale(0.8).to_edge(DOWN)
        caption3[1].set_color(YELLOW)
        caption3[3].set_color(ORANGE)

        caption4 = MathTex(r"\text{Minimize: } T(x)=", r"\frac{128-x}{17}", "+",r"\frac{\sqrt{x^2+576}}{15}", r", x\in[0,128]").scale(0.8).to_edge(DOWN)
        caption4[1].set_color(YELLOW)
        caption4[3].set_color(ORANGE)

        self.play(Write(caption1))
        self.wait(5)
        self.play(Transform(caption1, caption2))
        self.wait(5)
        self.play(Transform(caption1, caption3))
        self.wait(5)
        self.play(Transform(caption1, caption4))
        self.wait(10)





class FindCP(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Minimize: } T(x)=", r"\frac{128-x}{17}", "+",r"\frac{\sqrt{x^2+576}}{15}", r", x\in[0,128]").scale(0.8).to_edge(UP)
        title1[1].set_color(YELLOW)
        title1[3].set_color(ORANGE)


        caption1 = MathTex(r"x =45 \text{ is a critical number. }" ,color="ORANGE").scale(0.8).to_edge(DOWN)
        caption2 = MathTex(r"T(x) \text{ is minimized when } x=45" ,color="ORANGE").scale(0.8).to_edge(DOWN)
        caption3 = MathTex(r"\text{The tiger runs 83 yards. }" ,color="ORANGE").scale(0.8).to_edge(DOWN)  


        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"T(x)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{128-x}{17}", "+",r"\frac{\sqrt{x^2+576}}{15}",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"T'(x)").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"-\frac{1}{17}", "+",r"\frac{1}{15}\frac{1}{2\sqrt{x^2+576}}2x",).scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"0", color="RED").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"-\frac{1}{17}", "+",r"\frac{1}{15}\frac{x}{\sqrt{x^2+576}}",).scale(0.8).next_to(eq3, RIGHT)

        lhs4 = MathTex(r"\frac{15}{17}").scale(0.8).next_to(eq4, LEFT)
        rhs4 = MathTex(r"\frac{x}{\sqrt{x^2+576}}",).scale(0.8).next_to(eq4, RIGHT)

        lhs5 = MathTex(r"\left(\frac{15}{17}\right)^2",).scale(0.8).next_to(eq4, LEFT)
        rhs5 = MathTex(r"\left(\frac{x}{\sqrt{x^2+576}}\right)^2",).scale(0.8).next_to(eq4, RIGHT)

        lhs6 = MathTex(r"\frac{225}{289}").scale(0.8).next_to(eq4, LEFT)
        rhs6 = MathTex(r"\frac{x^2}{x^2+576}",).scale(0.8).next_to(eq4, RIGHT)

        lhs7 = MathTex(r"\frac{225}{289}(x^2+576)").scale(0.8).next_to(eq4, LEFT)
        rhs7 = MathTex(r"x^2",).scale(0.8).next_to(eq4, RIGHT)

        lhs8 = MathTex(r"225(x^2+576)").scale(0.8).next_to(eq4, LEFT)
        rhs8 = MathTex(r"289x^2",).scale(0.8).next_to(eq4, RIGHT)

        lhs9 = MathTex(r"129600").scale(0.8).next_to(eq4, LEFT)
        rhs9 = MathTex(r"64x^2",).scale(0.8).next_to(eq4, RIGHT)

        lhs10 = MathTex(r"x^2").scale(0.8).next_to(eq4, LEFT)
        rhs10 = MathTex(r"\frac{129600}{64}",).scale(0.8).next_to(eq4, RIGHT)

        lhs11 = MathTex(r"x^2").scale(0.8).next_to(eq4, LEFT)
        rhs11 = MathTex(r"2025",).scale(0.8).next_to(eq4, RIGHT)

        lhs12 = MathTex(r"x").scale(0.8).next_to(eq4, LEFT)
        rhs12 = MathTex(r"45",).scale(0.8).next_to(eq4, RIGHT)

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
        self.play(Write(lhs4), Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(
            FadeOut(rhs3, lhs3),
            lhs4.animate.next_to(eq3, LEFT),
            rhs4.animate.next_to(eq3, RIGHT),
            Write(lhs5), Write(rhs5)
            )
        self.wait(5)
        self.play(
            FadeOut(rhs4, lhs4),
            lhs5.animate.next_to(eq3, LEFT),
            rhs5.animate.next_to(eq3, RIGHT),
            Write(lhs6), Write(rhs6)
            )
        self.wait(5)
        self.play(
            FadeOut(rhs5, lhs5),
            lhs6.animate.next_to(eq3, LEFT),
            rhs6.animate.next_to(eq3, RIGHT),
            Write(lhs7), Write(rhs7)
            )
        self.wait(5)
        self.play(
            FadeOut(rhs6, lhs6),
            lhs7.animate.next_to(eq3, LEFT),
            rhs7.animate.next_to(eq3, RIGHT),
            Write(lhs8), Write(rhs8)
            )
        self.wait(5)
        self.play(
            FadeOut(rhs7, lhs7),
            lhs8.animate.next_to(eq3, LEFT),
            rhs8.animate.next_to(eq3, RIGHT),
            Write(lhs9), Write(rhs9)
            )
        self.wait(5)
        self.play(
            FadeOut(rhs8, lhs8),
            lhs9.animate.next_to(eq3, LEFT),
            rhs9.animate.next_to(eq3, RIGHT),
            Write(lhs10), Write(rhs10)
            )
        self.wait(5)
        self.play(
            FadeOut(rhs9, lhs9),
            lhs10.animate.next_to(eq3, LEFT),
            rhs10.animate.next_to(eq3, RIGHT),
            Write(lhs11), Write(rhs11)
            )
        self.wait(5)
        self.play(
            FadeOut(rhs10, lhs10),
            lhs11.animate.next_to(eq3, LEFT),
            rhs11.animate.next_to(eq3, RIGHT),
            Write(lhs12), Write(rhs12)
            )
        self.wait(5)
        self.play(Write(caption1))
        self.play(FadeOut(lhs1, rhs1, eq1, lhs2, rhs2, eq2, lhs11, rhs11, eq3, lhs12, rhs12, eq4, ),
            )

        lhs1 = MathTex(r"T(0)").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{128-0}{17}+\frac{\sqrt{0^2+576}}{15}", r"=\frac{776}{85}", r"\approx 9.129\text{ seconds}").scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"T(45)").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"\frac{128-45}{17}+\frac{\sqrt{45^2+576}}{15}", r"=\frac{704}{85}", r"\approx 8.282\text{ seconds}").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"T(128)").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"\frac{128-128}{17}+\frac{\sqrt{128^2+576}}{15}", r"=\frac{\sqrt{16960}}{15}", r"\approx 8.682\text{ seconds}").scale(0.8).next_to(eq3, RIGHT)

        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1[0]))
        self.wait(2)
        self.play(Write(rhs1[1]))
        self.wait(2)
        self.play(Write(rhs1[2]))

        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2[0]))
        self.wait(2)
        self.play(Write(rhs2[1]))
        self.wait(2)
        self.play(Write(rhs2[2]))

        self.play(Write(lhs3))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3[0]))
        self.wait(2)
        self.play(Write(rhs3[1]))
        self.wait(2)
        self.play(Write(rhs3[2]))
        self.wait(5)
        self.play(FadeOut(eq1, eq3, lhs1, lhs3, rhs1, rhs3),
            lhs2.animate.set_color(BLUE),
            rhs2.animate.set_color(BLUE),
            )
        self.wait(3)
        self.play(Transform(caption1, caption2))
        self.wait(5)
        self.play(FadeOut(eq2, lhs2, rhs2))

        River = Polygon([-4, -1, 0], [4, -1, 0], [4, 1, 0], [-4,1,0], color=BLUE)
        River.set_fill(BLUE, 0.5)

        Tiger = Dot([-4,-1,0])
        labelT = MathTex(r"T").scale(0.5).next_to(Tiger, LEFT)

        Child = Dot([4,1,0])
        labelC = MathTex(r"C").scale(0.5).next_to(Child, UP)

        P = Dot([2,-1,0], color=RED)
        labelP = MathTex(r"P", color=RED).scale(0.5).next_to(P, DOWN)

        Run=DashedLine([-4,-1,0], [2,-1,0], color=YELLOW)
        Swim=DashedLine([2,-1,0], [4,1,0], color=ORANGE)

        labelR = MathTex(r"128-x", color=YELLOW).scale(0.5).next_to([-1,-1,0], DOWN)
        labelB = MathTex(r"x").scale(0.5).next_to([3,-1,0], DOWN)
        labelS = MathTex(r"\sqrt{x^2+24^2}", color=ORANGE).scale(0.5).next_to([3,0,0], (LEFT+UP)/1.4 )
        labelW = MathTex(r"24", color=BLUE).scale(0.5).next_to([4,0,0], RIGHT)

        labelR1 = MathTex(r"128-45", color=YELLOW).scale(0.5).next_to([-1,-1,0], DOWN)
        labelB1 = MathTex(r"45").scale(0.5).next_to([3,-1,0], DOWN)
        labelS1 = MathTex(r"\sqrt{45^2+24^2}", color=ORANGE).scale(0.5).next_to([3,0,0], (LEFT+UP)/1.4 )

        self.play(Create(River),Create(Tiger), Write(labelT), Create(Child), Write(labelC), 
            Create(P), Write(labelP), Create(Run), Create(Swim), Write(labelR), Write(labelB), Write(labelW),
            Write(labelS))
        
        self.wait(5)

        self.play(Transform(labelR, labelR1), Transform(labelB, labelB1), Transform(labelS, labelS1))
        self.wait(5)
        self.play(Transform(caption1, caption3))
        self.wait(10)






        


       





        
        



        


        
        



        



  
       