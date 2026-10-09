#%%manim -ql LIPoly

from manim import *










class FindDquad(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the derivative of } f(x)=x^2-3x+2 \text{ using the limit definition.}", color=BLUE).scale(0.8).to_edge(UP)
        title1a = MathTex(r"\text{Find  } f'(-5).", color=BLUE).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"f'(x)=2x-3." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"f'(x)",).scale(0.8).next_to(eq1, LEFT)
        

        rhs1 = MathTex(r"\displaystyle \lim_{h\to 0}", r"{ f(x+h) ", r"- ", r"f(x) ", "\over h }",).scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(GREEN)
        rhs1[3].set_color(RED)

        rhs2 = MathTex(r"\displaystyle \lim_{h\to 0}", r"{ f(x+h) ", r"- ", r"f(x) ", "\over h }",).scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(GREEN)
        rhs2[3].set_color(RED)

        rhs2a = MathTex(r"\displaystyle \lim_{h\to 0}", r"{ f(x+h) ", r"- ", r"(x^2-3x+2) ", "\over h }",).scale(0.8).next_to(eq2, RIGHT)
        rhs2a[1].set_color(GREEN)
        rhs2a[3].set_color(RED)

        rhs2b = MathTex(r"\displaystyle \lim_{h\to 0}", r"{ ((x+h)^2-3(x+h)+2) ", r"- ", r"(x^2-3x+2) ", "\over h }",).scale(0.8).next_to(eq2, RIGHT)
        rhs2b[1].set_color(GREEN)
        rhs2b[3].set_color(RED)


        rhs3 = MathTex(r"\displaystyle \lim_{h\to 0}\frac{x^2+2xh+h^2-3x-3h+2-x^2+3x-2}{h}",).scale(0.8).next_to(eq3, RIGHT)
        rhs4 = MathTex(r"\displaystyle \lim_{h\to 0}\frac{2xh+h^2-3h}{h}", r"=\displaystyle \lim_{h\to 0} 2x+h-3", r"=2x-3").scale(0.8).next_to(eq4, RIGHT)

        lhs1a = MathTex(r"f'(-5)",).scale(0.8).next_to(eq1, LEFT)
        rhs1a = MathTex(r"2(-5)-3=-18.").scale(0.8).next_to(eq1, RIGHT)

        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Transform(rhs2, rhs2a))
        self.wait(3)
        self.play(Transform(rhs2, rhs2b))
        self.wait(5)        
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4[0]))
        self.wait(3)
        self.play(Write(rhs4[1]))
        self.wait(3)
        self.play(Write(rhs4[2]))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(5)
        self.play(Transform(title1, title1a),
            FadeOut( eq4, rhs4,  eq3, rhs3, eq2, rhs2, eq1, rhs1),
            Transform(lhs1, lhs1a))
        self.wait(5)
        self.play(Write(eq1), Write(rhs1a))
        self.wait(5)

class FindDrational(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the derivative of } g(x)=\frac{2}{x^2} \text{ using the limit definition.}", color=BLUE).scale(0.8).to_edge(UP)
        title1a = MathTex(r"\text{Find  } g'(-0.5).", color=BLUE).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"g'(x)=-\frac{4}{x^3}." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"g'(x)",).scale(0.8).next_to(eq1, LEFT)
        

        rhs1 = MathTex(r"\displaystyle \lim_{h\to 0}", r"{ f(x+h) ", r"- ", r"f(x) ", "\over h }",).scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(GREEN)
        rhs1[3].set_color(RED)

        rhs2 = MathTex(r"\displaystyle \lim_{h\to 0} \Biggl(", r" f(x+h) ", r"- ", r"f(x) ", r"\Biggr)\frac{1}{h}",).scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(GREEN)
        rhs2[3].set_color(RED)

        rhs2a = MathTex(r"\displaystyle \lim_{h\to 0} \Biggl(", r" f(x+h) ", r"- ", r"\frac{2}{x^2} ", r"\Biggr)\frac{1}{h}",).scale(0.8).next_to(eq2, RIGHT)
        rhs2a[1].set_color(GREEN)
        rhs2a[3].set_color(RED)

        rhs2b = MathTex(r"\displaystyle \lim_{h\to 0} \Biggl(", r" \frac{2}{(x+h)^2} ", r"- ", r"\frac{2}{x^2} ", r"\Biggr)\frac{1}{h}",).scale(0.8).next_to(eq2, RIGHT)
        rhs2b[1].set_color(GREEN)
        rhs2b[3].set_color(RED)


        rhs3 = MathTex(r"\displaystyle \lim_{h\to 0} \frac{2x^2-2x^2-4xh+4h^2}{x^2(x+h)^2} \frac{1}{h}",).scale(0.8).next_to(eq3, RIGHT)
        rhs4 = MathTex(r"\displaystyle \lim_{h\to 0} \frac{(-4x+4h)h}{x^2(x+h)^2}\frac{1}{h}", r"=\displaystyle \lim_{h\to 0} \frac{-4x+4h}{x^2(x+h)^2}", r"=-\frac{4x}{x^4}=-\frac{4}{x^3}.").scale(0.8).next_to(eq4, RIGHT)

        lhs1a = MathTex(r"g'(-0.5)",).scale(0.8).next_to(eq1, LEFT)
        rhs1a = MathTex(r"-\frac{4}{(-0.5)^3}=32.").scale(0.8).next_to(eq1, RIGHT)

        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Transform(rhs2, rhs2a))
        self.wait(3)
        self.play(Transform(rhs2, rhs2b))
        self.wait(5)        
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4[0]))
        self.wait(3)
        self.play(Write(rhs4[1]))
        self.wait(3)
        self.play(Write(rhs4[2]))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(5)
        self.play(Transform(title1, title1a),
            FadeOut( eq4, rhs4,  eq3, rhs3, eq2, rhs2, eq1, rhs1),
            Transform(lhs1, lhs1a))
        self.wait(5)
        self.play(Write(eq1), Write(rhs1a))
        self.wait(5)        
        




class FindDradical(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the derivative of } h(x)=\sqrt{x-5} \text{ using the limit definition.}", color=BLUE).scale(0.8).to_edge(UP)
        title1a = MathTex(r"\text{Find  } h'(9).", color=BLUE).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"h'(x)=\frac{1}{2\sqrt{x-5}}." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*5)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"h'(x)",).scale(0.8).next_to(eq1, LEFT)
        

        rhs1 = MathTex(r"\displaystyle \lim_{h\to 0}", r"{ f(x+h) ", r"- ", r"f(x) ", r"\over h }",).scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(GREEN)
        rhs1[3].set_color(RED)

        rhs2 = MathTex(r"\displaystyle \lim_{h\to 0}", r"{ f(x+h) ", r"- ", r"f(x) ", r"\over h }",).scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(GREEN)
        rhs2[3].set_color(RED)

        rhs2a = MathTex(r"\displaystyle \lim_{h\to 0}", r"{ f(x+h) ", r"- ", r"\sqrt{x-5} ", r"\over h }",).scale(0.8).next_to(eq2, RIGHT)
        rhs2a[1].set_color(GREEN)
        rhs2a[3].set_color(RED)

        rhs2b = MathTex(r"\displaystyle \lim_{h\to 0}", r"{ \sqrt{(x+h)-5} ", r"- ", r"\sqrt{x-h} ", r"\over h }",).scale(0.8).next_to(eq2, RIGHT)
        rhs2b[1].set_color(GREEN)
        rhs2b[3].set_color(RED)

        rhs2c = MathTex(r"\displaystyle \lim_{h\to 0}", r"{ \sqrt{(x+h)-5} ", r"- ", r"\sqrt{x-h} ", r"\over h }", r"\frac{ \sqrt{x+h-5} + \sqrt{x-5} }{ \sqrt{x+h-5} + \sqrt{x-5} }").scale(0.8).next_to(eq2, RIGHT)
        rhs2c[1].set_color(GREEN)
        rhs2c[3].set_color(RED)


        rhs3 = MathTex(r"\displaystyle \lim_{h\to 0}\frac{(x+h-5)-(x-5) }{\sqrt{x+h-5} + \sqrt{x-5}} \frac{1}{h}",).scale(0.8).next_to(eq3, RIGHT)
        rhs4 = MathTex(r"\displaystyle \lim_{h\to 0}\frac{h}{h}\frac{1}{\sqrt{x+h-5} + \sqrt{x-5}}",  r"=\frac{1}{\sqrt{x+0-5} + \sqrt{x-5}}=\frac{1}{2\sqrt{x-5}}").scale(0.8).next_to(eq4, RIGHT)

        lhs1a = MathTex(r"h'(9)",).scale(0.8).next_to(eq1, LEFT)
        rhs1a = MathTex(r"\frac{1}{2\sqrt{9-5}}=\frac{1}{4}.").scale(0.8).next_to(eq1, RIGHT)

        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Transform(rhs2, rhs2a))
        self.wait(3)
        self.play(Transform(rhs2, rhs2b))
        self.wait(5)     
        self.play(Transform(rhs2, rhs2c))
        self.wait(5)        
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4[0]))
        self.wait(3)
        self.play(Write(rhs4[1]))
        self.wait(3)
        self.play(Write(caption1))
        self.wait(5)
        self.play(Transform(title1, title1a),
            FadeOut( eq4, rhs4,  eq3, rhs3, eq2, rhs2, eq1, rhs1),
            Transform(lhs1, lhs1a))
        self.wait(5)
        self.play(Write(eq1), Write(rhs1a))
        self.wait(5)





        


       





        
        



        


        
        



        



  
       