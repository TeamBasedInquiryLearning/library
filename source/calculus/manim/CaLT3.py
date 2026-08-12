#%%manim -ql LIPoly

from manim import *







class ComputeLimitRad(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute  }\displaystyle \lim_{x\to 9} \frac{\sqrt{x+27}-6}{x-9}.", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP+LEFT)
        eq0 = MathTex(r"=?").shift(UP+LEFT)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)



        lhs0 = MathTex(r"\frac{\sqrt{9+27}-6}{9-9}").scale(0.8).next_to(eq0, LEFT)
        rhs0 = MathTex(r"\frac{\sqrt{36}-6}{9-9}", r"=?\frac{0}{0}", r"\text{ is undefined.}").scale(0.8).next_to(eq0, RIGHT)
        rhs0[2].set_color(RED)

        lhs1 = MathTex(r"\displaystyle \lim_{x\to 9}\frac{\sqrt{x+27}-6}{x-9}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \lim_{x\to 9} \frac{\sqrt{x+27}-6}{x-9}", r"\cdot \frac{\sqrt{x+27}+6}{\sqrt{x+27}+6}").scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(BLUE)

        rhs2 = MathTex(r"\displaystyle \lim_{x\to 9}  \frac{(x+27)-6^2}{(x-9)(\sqrt{x+27}+6)}").scale(0.8).next_to(eq2, RIGHT)
        rhs3 = MathTex(r"\displaystyle \lim_{x\to 9}  \frac{x+27-36}{(x-9)(\sqrt{x+27}+6)}").scale(0.8).next_to(eq2, RIGHT)
        rhs4 = MathTex(r"\displaystyle \lim_{x\to 9}  \frac{x-9}{(x-9)(\sqrt{x+27}+6)}").scale(0.8).next_to(eq2, RIGHT)
        rhs5 = MathTex(r"\displaystyle \lim_{x\to 9}  \frac{1}{\sqrt{x+27}+6}").scale(0.8).next_to(eq2, RIGHT)
        rhs6 = MathTex(r"\displaystyle \frac{1}{\sqrt{9+27}+6}").scale(0.8).next_to(eq2, RIGHT)
        rhs7 = MathTex(r"\displaystyle \frac{1}{\sqrt{36}+6}").scale(0.8).next_to(eq2, RIGHT)
        rhs8 = MathTex(r"\displaystyle \frac{1}{6+6}", r"=\frac{1}{12}.").scale(0.8).next_to(eq1, RIGHT)




        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0))
        self.wait(3)
        self.play(Write(eq0), Write(rhs0[0]))
        self.wait(1)
        self.play(Write(rhs0[1]))
        self.wait(3)
        self.play(Write(rhs0[2]))
        self.wait(3)
        self.play(FadeOut(eq0, lhs0, rhs0))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1[0]))
        self.wait(1)
        self.play(Write(rhs1[1]))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(FadeOut(rhs1), rhs2.animate.next_to(eq1, RIGHT), Write(rhs3))
        self.wait(3)
        self.play(FadeOut(rhs2), rhs3.animate.next_to(eq1, RIGHT), Write(rhs4))
        self.wait(3)
        self.play(FadeOut(rhs3), rhs4.animate.next_to(eq1, RIGHT), Write(rhs5))
        self.wait(3)
        self.play(FadeOut(rhs4), rhs5.animate.next_to(eq1, RIGHT), Write(rhs6))
        self.wait(3)
        self.play(FadeOut(rhs5), rhs6.animate.next_to(eq1, RIGHT), Write(rhs7))
        self.wait(3)
        self.play(FadeOut(rhs6), rhs7.animate.next_to(eq1, RIGHT), FadeOut(eq2))
        self.wait(3)
        self.play(FadeOut(rhs7), Write(rhs8[0]))
        self.wait(3)
        self.play(Write(rhs8[1]))

        self.wait(10)

        

class ComputeLimitRat(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute  }\displaystyle \lim_{x\to 3} \frac{\frac{1}{x-6}+\frac{1}{3}}{x-3}.", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP+LEFT)
        eq0 = MathTex(r"=?").shift(UP+LEFT)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)



        lhs0 = MathTex(r"\frac{\frac{1}{3-6}+\frac{1}{3}}{3-3}").scale(0.8).next_to(eq0, LEFT)
        rhs0 = MathTex(r"\frac{-\frac{1}{3}+\frac{1}{3}}{3-3}", r"=?\frac{0}{0}", r"\text{ is undefined.}").scale(0.8).next_to(eq0, RIGHT)
        rhs0[2].set_color(RED)

        lhs1 = MathTex(r"\displaystyle \lim_{x\to 3} \frac{\frac{1}{x-6}+\frac{1}{3}}{x-3}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \lim_{x\to 3} \frac{3\frac{1}{x-6}+\frac{1}{3}\frac{x-6}{x-6}}{x-3}").scale(0.8).next_to(eq1, RIGHT)
        

        rhs2 = MathTex(r"\displaystyle \lim_{x\to 3} \frac{\frac{3}{3(x-6)}+\frac{x-6}{3(x-6)}}{x-3}").scale(0.8).next_to(eq2, RIGHT)
        rhs3 = MathTex(r"\displaystyle \lim_{x\to 3} \frac{\frac{3+x-6}{3x-18}}{x-3}").scale(0.8).next_to(eq2, RIGHT)
        rhs4 = MathTex(r"\displaystyle \lim_{x\to 3} \frac{\frac{x-3}{3x-18}}{x-3}").scale(0.8).next_to(eq2, RIGHT)
        rhs5 = MathTex(r"\displaystyle \lim_{x\to 3} \frac{\frac{1}{3x-18}}{1}").scale(0.8).next_to(eq2, RIGHT)
        rhs6 = MathTex(r"\displaystyle \lim_{x\to 3} \frac{1}{3x-18}").scale(0.8).next_to(eq2, RIGHT)
        rhs7 = MathTex(r"\displaystyle \frac{1}{9-18}", r"=-\frac{1}{9}").scale(0.8).next_to(eq1, RIGHT)

       



        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0))
        self.wait(3)
        self.play(Write(eq0), Write(rhs0[0]))
        self.wait(1)
        self.play(Write(rhs0[1]))
        self.wait(3)
        self.play(Write(rhs0[2]))
        self.wait(3)
        self.play(FadeOut(eq0, lhs0, rhs0))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(FadeOut(rhs1), rhs2.animate.next_to(eq1, RIGHT), Write(rhs3))
        self.wait(3)
        self.play(FadeOut(rhs2), rhs3.animate.next_to(eq1, RIGHT), Write(rhs4))
        self.wait(3)
        self.play(FadeOut(rhs3), rhs4.animate.next_to(eq1, RIGHT), Write(rhs5))
        self.wait(3)
        self.play(FadeOut(rhs4), rhs5.animate.next_to(eq1, RIGHT), Write(rhs6))
        self.wait(3)
        self.play(FadeOut(rhs5), rhs6.animate.next_to(eq1, RIGHT), FadeOut(eq2))
        self.wait(3)
        self.play(FadeOut(rhs6), Write(rhs7[0]))
        self.wait(3)
        self.play(Write(rhs7[1]))



        


        self.wait(10)


class ComputeLimit(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute  }\displaystyle \lim_{x\to 6} \frac{x^2-7x+6}{x^2-10x+24}.", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP+LEFT)
        eq0 = MathTex(r"=?").shift(UP+LEFT)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)



        lhs0 = MathTex(r"\displaystyle \frac{6^2-7(6)+6}{6^2-10(6)+24}").scale(0.8).next_to(eq0, LEFT)
        rhs0 = MathTex(r"\displaystyle \frac{36-42+6}{36-60+24}", r"=?\frac{0}{0}", r"\text{ is undefined.}").scale(0.8).next_to(eq0, RIGHT)
        rhs0[2].set_color(RED)

        lhs1 = MathTex(r"\displaystyle \lim_{x\to 6} \frac{x^2-7x+6}{x^2-10x+24}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \lim_{x\to 6} \frac{(x-1)(x-6)}{(x-4)(x-6)}").scale(0.8).next_to(eq1, RIGHT)
        

        rhs2 = MathTex(r"\displaystyle \lim_{x\to 6} \frac{x-1}{x-4}").scale(0.8).next_to(eq2, RIGHT)
        rhs3 = MathTex(r"\displaystyle \frac{6-1}{6-4}", r"=\frac{5}{2}.").scale(0.8).next_to(eq1, RIGHT)

       



        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0))
        self.wait(3)
        self.play(Write(eq0), Write(rhs0[0]))
        self.wait(1)
        self.play(Write(rhs0[1]))
        self.wait(3)
        self.play(Write(rhs0[2]))
        self.wait(3)
        self.play(FadeOut(eq0, lhs0, rhs0))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(FadeOut(rhs1), rhs2.animate.next_to(eq1, RIGHT), FadeOut(eq2))
        self.wait(3)
        self.play(FadeOut(rhs2), Write(rhs3[0]))
        self.wait(3)
        self.play(Write(rhs3[1]))



        


        self.wait(10)

class ComputeLimitEZ(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute  }\displaystyle \lim_{x\to 5} \frac{x^2-7x+12}{x^2+3x+2}.", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP)
        eq0 = MathTex(r"=?").shift(UP)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)



        lhs0 = MathTex(r"\displaystyle \lim_{x\to 5} \frac{x^2-7x+12}{x^2+3x+2}=",r"\displaystyle  \frac{5^2-7(5)+12}{5^2+3(5)+2}").scale(0.8).next_to(eq0, LEFT)
        rhs0 = MathTex(r"\displaystyle  \frac{25-35+12}{25+15+2}", r"=\frac{2}{42}", r"=\frac{1}{21}.}").scale(0.8).next_to(eq0, RIGHT)
        

        #lhs1 = MathTex(r"\displaystyle \lim_{x\to 6} \frac{x^2-7x+6}{x^2-10x+24}").scale(0.8).next_to(eq1, LEFT)
        

       



        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0[1]))
        self.wait(3)
        self.play(Write(eq0), Write(rhs0[0]))
        self.wait(1)
        self.play(Write(rhs0[1]))
        self.wait(3)
        self.play(Write(rhs0[2]))
        self.wait(3)
        self.play(Write(lhs0[0]), Transform(eq0, eq1))



        


        self.wait(10)        



class ComputeLimitAbs(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Compute  }\displaystyle \lim_{x\to -1} \frac{x^2+3x+2}{|x+1|}.", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        
        eq1 = MathTex(r"=").shift(UP+LEFT*1.75)
        eq0 = MathTex(r"=?").shift(UP+LEFT*1.75)
        eq2 = MathTex(r"=").next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").next_to(eq2, DOWN*5)



        lhs0 = MathTex(r"\displaystyle \frac{(-1)^2+3(-1)+2}{|-1+1|}").scale(0.8).next_to(eq0, LEFT)
        rhs0 = MathTex(r"\displaystyle \frac{1-3+2}{|-1+1|}", r"=?\frac{0}{0}", r"\text{ is undefined.}").scale(0.8).next_to(eq0, RIGHT)
        rhs0[2].set_color(RED)

        lhs1 = MathTex(r"\displaystyle \lim_{x\to -1} \frac{x^2+3x+2}{|x+1|}").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \lim_{x\to -1} \frac{(x+2)(x+1)}{|x+1|}", r"\text{ is undefined.}").scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(RED)
        
        lhs2 = MathTex(r"\displaystyle \lim_{x\to -1^+} \frac{x^2+3x+2}{|x+1|}").scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"\displaystyle \lim_{x\to -1^+} \frac{(x+2)(x+1)}{x+1}", r"=\displaystyle \lim_{x\to -1^+} x+2", r"=1.").scale(0.8).next_to(eq2, RIGHT)

        lhs3 = MathTex(r"\displaystyle \lim_{x\to -1^-} \frac{x^2+3x+2}{|x+1|}").scale(0.8).next_to(eq3, LEFT)
        rhs3 = MathTex(r"\displaystyle \lim_{x\to -1^-} \frac{(x+2)(x+1)}{-(x+1)}", r"=\displaystyle \lim_{x\to -1^-} -(x+2)", r"=-1.").scale(0.8).next_to(eq3, RIGHT)
        

       



        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(5)
        self.play(Write(lhs0))
        self.wait(3)
        self.play(Write(eq0), Write(rhs0[0]))
        self.wait(1)
        self.play(Write(rhs0[1]))
        self.wait(3)
        self.play(Write(rhs0[2]))
        self.wait(3)
        self.play(FadeOut(eq0, lhs0, rhs0))
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1[0]))
        self.wait(3)

        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2[0]))
        self.wait(3)
        self.play(Write(rhs2[1]))
        self.wait(3)
        self.play(Write(rhs2[2]))
        self.wait(3)

        self.play(Write(lhs3))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3[0]))
        self.wait(3)
        self.play(Write(rhs3[1]))
        self.wait(3)
        self.play(Write(rhs3[2]))
        self.wait(3)

        self.play(Write(rhs1[1]))



        


        self.wait(10)
        
        



        


        
        



        



  
       