#%%manim -ql LIPoly

from manim import *










class FindDerivative1(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the derivative } \frac{d}{dx} \left[ \displaystyle \int_{5}^{e^{x+6}} 7  {\left(9  \cos\left(t\right) + 5\right)}^{4}\,dt \right].", color=TEAL).scale(0.6).to_edge(UP)
        caption1 = MathTex(r"\text{Let } F(t) \text{ be an anti-derivative of }  7  {\left(9  \cos\left(t\right) + 5\right)}^{4}.", color=ORANGE).scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*0.5)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\frac{d}{dx} \Biggl[ \displaystyle \int ",  r" ^{e^x+6} ", r" _{5}", r"  7  {\left(9  \cos\left(t\right) + 5\right)}^{4}\,dt \Biggr]").scale(0.8).next_to(eq1, LEFT)
        lhs1[1].set_color(BLUE)
        lhs1[2].set_color(RED)

        rhs1 = MathTex(r"\frac{d}{dx} [ F( ", r" e^x+6 ", r"  ) - F( ", r" 5 ", r" ) ]",).scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(BLUE)
        rhs1[3].set_color(RED)
        
        rhs2 = MathTex(r"\frac{d}{dx} [ F( ", r" e^x+6  ", r")] -  ", r" \frac{d}{dx} [ F( ", r" 5 ", r" ) ]",).scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(BLUE)
        rhs2[4].set_color(RED)


        rhs3 =MathTex(r" F'(", r" e^x+6 ", r" ) \frac{d}{dx}[ ", r" e^x+6 ", r" ] +0  ").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(BLUE)
        rhs3[3].set_color(BLUE)

        rhs4 = MathTex(r"  7\bigl( 9\cos( ", r"e^x+6  ", r" )  \bigr)^4 ", r"e^x  .").scale(0.8).next_to(eq4, RIGHT)
        rhs4[1].set_color(BLUE)
        rhs4[3].set_color(BLUE)
        


        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1),)
        self.wait(5)
        self.play(Write(caption1))
        self.wait(5)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Wiggle(rhs2[3]), Wiggle(rhs2[4]), Wiggle(rhs2[5]))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Wiggle(caption1))
        self.wait(3)
        self.play(Write(eq4), Write(rhs4))
        self.wait(10)

        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4, title1)
            )



class FindDerivative2(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the derivative } \frac{d}{dx} \left[ \displaystyle \int_{\frac{1}{x^3+2}}^{9} 8e^{-t^2}\,dt \right].", color=TEAL).scale(0.6).to_edge(UP)
        caption1 = MathTex(r"\text{Let } F(t) \text{ be an anti-derivative of }  8e^{t^2}.", color=ORANGE).scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*0.5)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\frac{d}{dx} \Biggl[ \displaystyle \int ",  r" ^{9} ", r" _{\frac{1}{x^3+2}}", r"  8e^{-t^2}\,dt \Biggr]").scale(0.8).next_to(eq1, LEFT)
        lhs1[1].set_color(BLUE)
        lhs1[2].set_color(RED)

        rhs1 = MathTex(r"\frac{d}{dx} \biggl[ F( ", r" 9 ", r"  ) - F\biggl( ", r" \frac{1}{x^3+2} ", r" \biggr) \biggr]",).scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(BLUE)
        rhs1[3].set_color(RED)
        
        rhs2 = MathTex(r"\frac{d}{dx} [ F( ", r" 9  ", r")]   ", r" -\frac{d}{dx} \biggl[ F\biggl( ", r" \frac{1}{x^3+2} ", r" \biggr) \biggr]",).scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(BLUE)
        rhs2[4].set_color(RED)


        rhs3 =MathTex(r" 0 - F'\biggl(", r" \frac{1}{x^3+2} ", r" \biggr) \frac{d}{dx} \biggl[ ", r" \frac{1}{x^3+2} ", r" \biggr]   ").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(RED)
        rhs3[3].set_color(RED)

        rhs4 = MathTex(r"  -8e^{-\bigl(", r" \frac{1}{x^3+2}  ", r" \bigr)^2} ", r"\frac{-3x^2}{(x^3+2)^2}  .").scale(0.8).next_to(eq4, RIGHT)
        rhs4[1].set_color(BLUE)
        rhs4[3].set_color(BLUE)

        rhs4a = MathTex(r"  8e^{", r" -\frac{1}{x^6+4x^3+4}  ", r" } ", r"\frac{3x^2}{x^6+4x^3+4}  .").scale(0.8).next_to(eq4, RIGHT)


        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1),)
        self.wait(5)
        self.play(Write(caption1))
        self.wait(5)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Wiggle(rhs2[0]), Wiggle(rhs2[1]), Wiggle(rhs2[2]))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Wiggle(caption1))
        self.wait(3)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10)

        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4, title1)
            )


class FindDerivative3(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the derivative } \frac{d}{dx} \left[ \displaystyle \int_{x}^{x^2} \frac{\sin(t)}{t^6+1}\,dt \right].", color=TEAL).scale(0.6).to_edge(UP)
        caption1 = MathTex(r"\text{Let } F(t) \text{ be an anti-derivative of }  \frac{\sin(t)}{t^6+1}.", color=ORANGE).scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*0.5)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\frac{d}{dx} \Biggl[ \displaystyle \int ",  r" ^{x^2} ", r" _{x}", r"  \frac{\sin(t)}{t^6+1}\,dt \Biggr]").scale(0.8).next_to(eq1, LEFT)
        lhs1[1].set_color(BLUE)
        lhs1[2].set_color(RED)

        rhs1 = MathTex(r"\frac{d}{dx} [ F( ", r" x^2 ", r"  ) - F( ", r" x ", r" ) ]",).scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(BLUE)
        rhs1[3].set_color(RED)
        
        rhs2 = MathTex(r"\frac{d}{dx} [ F( ", r" x^2  ", r")] -  ", r" \frac{d}{dx} [ F( ", r" x ", r" ) ]",).scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(BLUE)
        rhs2[4].set_color(RED)


        rhs3 =MathTex(r" F'(", r" x^2 ", r" ) \frac{d}{dx}[ ", r" x^2 ", r" ] + F'(", r"x", r")\frac{d}{dx}[", r"x", r"]" ).scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(BLUE)
        rhs3[3].set_color(BLUE)
        rhs3[5].set_color(RED)
        rhs3[7].set_color(RED)

        rhs4 = MathTex(  r"{ \sin(", r"x^2", r") \over (", r"x^2", r")^6+1}", r"(2x)", r"-",   r"{ \sin(", r"x", r") \over (", r"x", r")^6+1}", r"1" ).scale(0.8).next_to(eq4, RIGHT)
        rhs4[1].set_color(BLUE)
        rhs4[3].set_color(BLUE)
        rhs4[5].set_color(BLUE)

        rhs4[8].set_color(RED)
        rhs4[10].set_color(RED)
        rhs4[12].set_color(RED)


        rhs4a = MathTex( r"\frac{2x\sin(x^2)}{x^{12}+1} - \frac{\sin(x)}{x^6+1}" ).scale(0.8).next_to(eq4, RIGHT)

        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1),)
        self.wait(5)
        self.play(Write(caption1))
        self.wait(5)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Wiggle(caption1))
        self.wait(3)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10)

        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4, title1)
            )   




class FindDerivative4(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find  the derivative } \frac{d}{dx} \left[ \displaystyle \int_{-1}^{\sqrt{x}} \ln(t^4+4)\,dt \right].", color=TEAL).scale(0.6).to_edge(UP)
        caption1 = MathTex(r"\text{Let } F(t) \text{ be an anti-derivative of } \ln(t^4+4).", color=ORANGE).scale(0.8).to_edge(DOWN)
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*0.5)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\frac{d}{dx} \Biggl[ \displaystyle \int ",  r" ^{\sqrt{x}} ", r" _{-1}", r" \ln(t^4+4)\,dt \Biggr]").scale(0.8).next_to(eq1, LEFT)
        lhs1[1].set_color(BLUE)
        lhs1[2].set_color(RED)

        rhs1 = MathTex(r"\frac{d}{dx} [ F( ", r" \sqrt{x} ", r"  ) - F( ", r" -1 ", r" ) ]",).scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(BLUE)
        rhs1[3].set_color(RED)
        
        rhs2 = MathTex(r"\frac{d}{dx} [ F( ", r" \sqrt{x} ", r")] -  ", r" \frac{d}{dx} [ F( ", r" -1 ", r" ) ]",).scale(0.8).next_to(eq2, RIGHT)
        rhs2[1].set_color(BLUE)
        rhs2[4].set_color(RED)


        rhs3 =MathTex(r" F'(", r" \sqrt{x} ", r" ) \frac{d}{dx}[ ", r" \sqrt{x} ", r" ] +0  ").scale(0.8).next_to(eq3, RIGHT)
        rhs3[1].set_color(BLUE)
        rhs3[3].set_color(BLUE)

        rhs4 = MathTex(r"  \ln\bigl( \bigl( ", r"\sqrt{x}  ", r" \bigr)^4 + 4 \bigr) ", r"\frac{1}{2}x^{-1/2}").scale(0.8).next_to(eq4, RIGHT)
        rhs4[1].set_color(BLUE)
        rhs4[3].set_color(BLUE)

        rhs4a = MathTex(r"  \frac{\ln\bigl( x^2 + 4 \bigr)}{2\sqrt{x}} ").scale(0.8).next_to(eq4, RIGHT)
        


        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1),)
        self.wait(5)
        self.play(Write(caption1))
        self.wait(5)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(3)
        self.play(Wiggle(rhs2[3]), Wiggle(rhs2[4]), Wiggle(rhs2[5]))
        self.wait(3)
        self.play(Write(eq3), Write(rhs3))
        self.wait(3)
        self.play(Wiggle(caption1))
        self.wait(3)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10)

        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4, title1)
            )


        
class Graph(Scene):
    def construct(self):   

        title1 = MathTex(r" y=\ln(t^4+4) \text{axis on }[-1,\sqrt{x}].", color=TEAL).scale(0.6).to_edge(UP)

        caption1 = MathTex(r" x=", color=ORANGE).scale(0.8).to_edge(DOWN)



        axes = Axes(x_range=[-2,4,2], y_range=[-1, 6, 2], x_length=5, y_length=5,).shift(DOWN*0.5)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        axes_labels2 = axes.get_axis_labels(MathTex("u").scale(0.5), MathTex("y").scale(0.5))
        axes_labels3 = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))

        numberplane = NumberPlane(x_range=[-2,4,2], y_range=[-1, 6, 2], x_length=5, y_length=5,
            ).add_coordinates().shift(DOWN*0.5)

        
        
        #L1 = DashedLine(axes.coords_to_point(-5, 2/3), axes.coords_to_point(1, 2/3), color="RED")

        
        

        plot1 = axes.plot(lambda x:( np.log(x**4+4) ), 
            x_range=[-2, 4], 
            use_smoothing=True,
            color=BLUE)


        area1 = axes.get_area(graph=plot1, x_range=[-1,0], color=RED)


        tracker=ValueTracker(0.01)


       

        
        
        def update(mob):
            mob.become(
                axes.get_area(graph=plot1, x_range=[-1, tracker.get_value()**(1/2)], color=RED)
                
        )
        

        area1.add_updater(update)


        number=DecimalNumber(
            0,
            show_ellipsis=False,
            num_decimal_places=4,
            include_sign=False,
            color=ORANGE,
        ).scale(0.8).next_to(caption1, RIGHT)
        def updateNum(mob):
            mob.become(DecimalNumber(
            tracker.get_value(),
            show_ellipsis=False,
            num_decimal_places=4,
            include_sign=False,
            color=ORANGE,
        )).scale(0.8).next_to(caption1, RIGHT)
        number.add_updater(updateNum)


        




        
        self.add(title1, caption1, number)
        self.add(axes, axes_labels, numberplane, )
        self.wait(1)
        #self.play(Create(L1))
        self.play(Create(plot1), )
        self.wait(3)
        self.play(Create(area1), )
        self.wait(5)

        self.play(tracker.animate.set_value(15), run_time=5)        
        self.wait(3)

        self.play(tracker.animate.set_value(0), run_time=5)        
        self.wait(3)

        self.play(tracker.animate.set_value(15), run_time=5)        
        self.wait(3)

        self.play(tracker.animate.set_value(0), run_time=5)        
        self.wait(3)

        
        

       

        
        






        


       





        
        



        


        
        



        



  
       