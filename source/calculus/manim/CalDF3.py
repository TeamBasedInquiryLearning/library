#%%manim -ql LIPoly

from manim import *










class FindDtransc(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the derivative of } h(t)=-3\cos(t)+2\ln(t).}", color=BLUE).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"h'(t)=3\sin(t)+\frac{2}{t}." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"h(t)",).scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"-3\cos(t)+2\ln(t)",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"h'(t)",).scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"-3", r"\frac{d}{dt} \bigl[", r" \cos(t)", r"\bigr] ", r" +2 ", r"\frac{d}{dt}\bigl[ ", r" \ln(t)", r"\bigr]").scale(0.8).next_to(eq2, RIGHT)

        rhs2[1].set_color(BLUE)
        rhs2[3].set_color(BLUE)
        rhs2[5].set_color(BLUE)
        rhs2[7].set_color(BLUE)

        


        rhs3 = MathTex(r"-3(-\sin(t))+2\frac{1}{t}",).scale(0.8).next_to(eq3, RIGHT)
        rhs4 = MathTex(r"3\sin(t)+\frac{2}{t}.").scale(0.8).next_to(eq4, RIGHT)

        
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
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.play(Write(caption1))
        self.wait(5)




class FindDpower(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the derivative of } g(y)=\sqrt[3]{y^7}+\frac{7}{y^4}.}", color=BLUE).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"g'(y)=\frac{7}{3}\sqrt[3]{y^4}-\frac{28}{y^5} ." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"g(y)",).scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\sqrt[3]{y^7}+\frac{7}{y^4}",).scale(0.8).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"y^{\frac{7}{3}}+7y^{-4}",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"g'(y)",).scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex( r"\frac{d}{dy} \bigl[", r" y^{\frac{7}{3}}", r"\bigr] ", r" +7 ", r"\frac{d}{dt}\bigl[ ", r"y^{-4}", r"\bigr]").scale(0.8).next_to(eq2, RIGHT)

        rhs2[0].set_color(BLUE)
        rhs2[2].set_color(BLUE)
        rhs2[4].set_color(BLUE)
        rhs2[6].set_color(BLUE)

        


        rhs3 = MathTex(r"\frac{7}{3}(y^{\frac{4}{3}})+7(-4)y^{-5}",).scale(0.8).next_to(eq3, RIGHT)
        rhs4 = MathTex(r"\frac{7}{3}\sqrt[3]{y^4}-\frac{28}{y^5}.").scale(0.8).next_to(eq4, RIGHT)

        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1))
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Transform(rhs1, rhs1a))
        self.wait(3)
        self.play(Write(lhs2))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)        
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.play(Write(caption1))
        self.wait(5)       
        








class FindDpoly(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the derivative of } f(x)=8x^5+x^4-7x^2-3.}", color=BLUE).scale(0.8).to_edge(UP)
        caption1 = MathTex(r"f'(x)=40x^4+4x^3-14x'." ,color="ORANGE").scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*3)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=").scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"f(x)",).scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"8x^5+x^4-7x^2-3",).scale(0.8).next_to(eq1, RIGHT)

        lhs2 = MathTex(r"f'(x)",).scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"8", r"\frac{d}{dx} \bigl[", r" x^5", r"\bigr] ", r" + ", r"\frac{d}{dx}\bigl[ ", r" x^4", r"\bigr]", 
            r" -7 ", r"\frac{d}{dx}\bigl[ ", r" x^2", r"\bigr]", r" - ", 
            r"\frac{d}{dx}\bigl[ ", r" 3", r"\bigr]",).scale(0.8).next_to(eq2, RIGHT)

        rhs2[1].set_color(BLUE)
        rhs2[3].set_color(BLUE)
        rhs2[5].set_color(BLUE)
        rhs2[7].set_color(BLUE)
        rhs2[9].set_color(BLUE)
        rhs2[11].set_color(BLUE)
        rhs2[13].set_color(BLUE)
        rhs2[15].set_color(BLUE)

        


        rhs3 = MathTex(r"8(5)x^4+4x^3-7(2)x-0",).scale(0.8).next_to(eq3, RIGHT)
        rhs4 = MathTex(r"40x^4+4x^3-14x.").scale(0.8).next_to(eq4, RIGHT)

        
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
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.play(Write(caption1))
        self.wait(5)        





        


       





        
        



        


        
        



        



  
       