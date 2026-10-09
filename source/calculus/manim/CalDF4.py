#%%manim -ql LIPoly

from manim import *










class FindQuotient(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the derivative of } h(t)=\frac{\sin(t)}{2t^2-5t+7}.}", color=TEAL).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"\text{By the Quotient Rule}." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"h(t)",).scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{\sin(t)}{2t^2-5t+7}",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"h'(t)",).scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"\frac{d}{dt} \Biggl[", r"{\sin(t)", r"\over", r"2t^2-5t+7}", r"\Biggr]").scale(0.8).next_to(eq2, RIGHT)

        rhs2[1].set_color(BLUE)
        rhs2[3].set_color(RED)

        


        rhs3 = MathTex(r"{(t^2-5t+7)", r"\frac{d}{dt}[\sin(t)]", r"-", r"\sin(t)", r"\frac{d}{dt}[2t^2-5t+7]", r"\over", r"(2t^2-5t+7)^2}",).scale(0.8).next_to(eq3, RIGHT)
        rhs3[0].set_color(RED)
        rhs3[1].set_color(BLUE)
        rhs3[3].set_color(BLUE)
        rhs3[4].set_color(RED)
        rhs3[6].set_color(RED)

        rhs4 = MathTex(r"{(t^2-5t+7)", r"\cos(t)", r"-", r"\sin(t)", r"(4t-5)", r"\over", r"(2t^2-5t+7)^2}", ).scale(0.8).next_to(eq4, RIGHT)
        rhs4[0].set_color(RED)
        rhs4[1].set_color(BLUE)
        rhs4[3].set_color(BLUE)
        rhs4[4].set_color(RED)
        rhs4[6].set_color(RED)

        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)        
        self.play(Write(eq3), Write(rhs3), Write(caption1))
        self.wait(5)
        self.play(FadeOut(caption1))
        self.play(Write(eq4), Write(rhs4))
        self.wait(3)
        self.play(rhs4.animate.set_color(WHITE))
        
        self.wait(5)




class FindProduct(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the derivative of } g(x)=(3x^2-7x+4)e^x.}", color=TEAL).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"\text{By the Product Rule}." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"g(x)",).scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"(3x^2-7x+4)e^x",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"g'(x)",).scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"\frac{d}{dt} \Biggl[", r"(3x^2-7x+4)", r"e^x", r"\Biggr]").scale(0.8).next_to(eq2, RIGHT)

        rhs2[1].set_color(BLUE)
        rhs2[2].set_color(RED)

        


        rhs3 = MathTex(r"(3x^2-7x+4)", r"\frac{d}{dx}[e^x]", r"+", r"e^x", r"\frac{d}{dx}[3x^2-7x+4]").scale(0.8).next_to(eq3, RIGHT)
        rhs3[0].set_color(BLUE)
        rhs3[1].set_color(RED)
        rhs3[3].set_color(RED)
        rhs3[4].set_color(BLUE)

        rhs4 = MathTex(r"(3x^2-7x+4)", r"e^x", r"+", r"e^x", r"(6x-7)").scale(0.8).next_to(eq4, RIGHT)
        rhs4[0].set_color(RED)
        rhs4[1].set_color(BLUE)
        rhs4[3].set_color(BLUE)
        rhs4[4].set_color(RED)

        rhs4a = MathTex(r"(3x^2-x-3)", r"e^x").scale(0.8).next_to(eq4, RIGHT)

        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)        
        self.play(Write(eq3), Write(rhs3), Write(caption1))
        self.wait(5)
        self.play(FadeOut(caption1))
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        
        self.wait(5)




class FindPower(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the derivative of } f(y)=\frac{y^2+3y-2}{\sqrt{y}}.}", color=TEAL).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"\text{By the Quotient Rule}." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"f(y)",).scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\frac{y^2+3y-2}{\sqrt{y}}",).scale(0.8).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"\frac{y^2+3y-2}{y^{\frac{1}{2}}}",).scale(0.8).next_to(eq1, RIGHT)
        rhs1b = MathTex(r"y^{\frac{3}{2}} +3y^{\frac{1}{2}} -2y^{-\frac{1}{2}} ",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"f'(y)",).scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"\frac{3}{2}y^{\frac{1}{2}} +3\frac{1}{2}y^{-\frac{1}{2}} -2\left(-\frac{1}{2}\right)y^{-\frac{3}{2}}").scale(0.8).next_to(eq2, RIGHT)

        


        rhs3 = MathTex(r"\frac{3}{2}\sqrt{y} +\frac{3}{2\sqrt{y}} +\frac{1}{y\sqrt{y}}").scale(0.8).next_to(eq3, RIGHT)

        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Transform(rhs1, rhs1a))
        self.wait(5)
        self.play(Transform(rhs1, rhs1b))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)        
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(FadeOut(rhs3, eq3, rhs2, eq2, lhs2, rhs1, eq1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1a))
        self.wait(3)
        


        rhs2 = MathTex(r"\frac{d}{dy}\Biggl[", r"{y^2+3y-2", r"\over", r"y^{\frac{1}{2}} }", r"\Biggr]").scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(BLUE)
        rhs2[3].set_color(RED)

        rhs3 = MathTex(r"{y^\frac{1}{2}", r"\frac{d}{dy}[y^2+3y-2]", r"-", r"(y^2+3y-2)", r"\frac{d}{dy}[y^{\frac{1}{2}}]", r"\over", r"\left(y^\frac{1}{2}\right)^2} }",).scale(0.8).next_to(eq3, RIGHT)
        rhs3[0].set_color(RED)
        rhs3[1].set_color(BLUE)
        rhs3[3].set_color(BLUE)
        rhs3[4].set_color(RED)
        rhs3[6].set_color(RED)

        rhs4 = MathTex(r"{y^\frac{1}{2}", r"(2y+3)", r"-", r"(y^2+3y-2)", r"\frac{1}{2}y^{-\frac{1}{2}}", r"\over", r"\left(y^\frac{1}{2}\right)^2} }",).scale(0.8).next_to(eq4, RIGHT)
        rhs4[0].set_color(RED)
        rhs4[1].set_color(BLUE)
        rhs4[3].set_color(BLUE)
        rhs4[4].set_color(RED)
        rhs4[6].set_color(RED)

        rhs4a = MathTex(r"{y^\frac{1}{2}", r"(2y+3)", r"-", r"(y^2+3y-2)", r"\frac{1}{2}y^{-\frac{1}{2}}", r"\over", r"y}",).scale(0.8).next_to(eq4, RIGHT)
        rhs4a[0].set_color(RED)
        rhs4a[1].set_color(BLUE)
        rhs4a[3].set_color(BLUE)
        rhs4a[4].set_color(RED)
        rhs4a[6].set_color(RED)

        rhs4b = MathTex(r"y^{-\frac{1}{2}}", r"(2y+3)", r"-", r"(y^2+3y-2)", r"\frac{1}{2}y^{-\frac{3}{2}}").scale(0.8).next_to(eq4, RIGHT)
        rhs4c = MathTex( r"2y^{\frac{1}{2}}+3y^{-\frac{1}{2}}", r"-", r"\frac{1}{2}y^{\frac{1}{2}} -\frac{3}{2}y^{-\frac{1}{2}}+y^{-\frac{3}{2}}").scale(0.8).next_to(eq4, RIGHT)
        rhs4d = MathTex( r"\frac{3}{2}y^{\frac{1}{2}}+\frac{3}{2}y^{-\frac{1}{2}}+y^{-\frac{3}{2}}").scale(0.8).next_to(eq4, RIGHT)
        rhs4e = MathTex(r"\frac{3}{2}\sqrt{y} +\frac{3}{2\sqrt{y}} +\frac{1}{y\sqrt{y}}").scale(0.8).next_to(eq4, RIGHT)

        self.play(Write(lhs2))
        self.wait(3)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)        
        self.play(Write(eq3), Write(rhs3), Write(caption1))
        self.wait(5)
        self.play(FadeOut(caption1))
        self.play(Write(eq4), Write(rhs4))
        self.wait(3)
        self.play(Transform(rhs4, rhs4a))
        self.wait(5)
        self.play(Transform(rhs4, rhs4b))
        self.wait(5)
        self.play(Transform(rhs4, rhs4c))
        self.wait(5)
        self.play(Transform(rhs4, rhs4d))
        self.wait(5)
        self.play(Transform(rhs4, rhs4e))
        
        self.wait(5)




        


       





        
        



        


        
        



        



  
       