#%%manim -ql LIPoly

from manim import *



class ShowPlot(Scene):
    def construct(self):


        title1 = MathTex(r"\text{Find } R_6, \text{for } f(x)=6x^3-9x^2+3 \text{ on } [0, 2].", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        axes = Axes(x_range=[0,2,0.5], y_range=[0,20,5], x_length=6, y_length=5,)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[0,2,0.5], y_range=[0,20,5],
            x_length=6,
            y_length=5,
            ).add_coordinates()

        
        
        

        theplot = axes.plot(lambda x: 6*x**3-9*x**2+3, 
            x_range=[0, 2], 
            use_smoothing=True,
            color=YELLOW)

        plotlabel = MathTex("f(x)=6x^3-9x^2+3").scale(0.5).next_to(theplot, RIGHT, buff=0.5).set_color(YELLOW)

        rectangles = numberplane.get_riemann_rectangles(theplot, x_range= [0,2 ], dx=2/6, color=RED, fill_opacity=0.6, input_sample_type="right")

        self.add(axes, axes_labels, numberplane, title1)
        self.wait(1)
        self.play(Create(theplot), Write(plotlabel))
        self.wait(5)
        self.play(Create(rectangles))
        self.wait(10)






class FindR6(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find } R_6, \text{for } f(x)=6x^3-9x^2+3 \text{ on }", " [0, 2].", color=TEAL).scale(0.8).to_edge(UP)        
        
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*4)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"R_6").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \sum_{i=1}^6 f(x_i)", "\Delta x",).scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(RED)
        rhs1a = MathTex(r"\displaystyle \sum_{i=1}^6 f(a+i", r"\Delta x", ")", r"\Delta x",).scale(0.8).next_to(eq1, RIGHT)
        rhs1a[1].set_color(RED)
        rhs1a[3].set_color(RED)
        rhs1b = MathTex(r"\displaystyle \sum_{i=1}^6 f(0+i", r"\Delta x", r")", r"\Delta x",).scale(0.8).next_to(eq1, RIGHT)
        rhs1b[1].set_color(RED)
        rhs1b[3].set_color(RED)
        rhs1c = MathTex(r"\displaystyle \sum_{i=1}^6 f\Biggl(0+i ", r" \frac{1}{3}", r"\Biggr)", r"\frac{1}{3}",).scale(0.8).next_to(eq1, RIGHT)
        rhs1c[1].set_color(RED)
        rhs1c[3].set_color(RED)
        rhs1d = MathTex(r"\displaystyle \sum_{i=1}^6 f\Biggl(", r"\frac{1}{3}", r"i\Biggr)", r"\frac{1}{3}",).scale(0.8).next_to(eq1, RIGHT)
        rhs1d[1].set_color(RED)
        rhs1d[3].set_color(RED)
        lhs2 = MathTex(r"\Delta x", color=RED).scale(0.8).next_to(eq2, LEFT)
        rhs2 = MathTex(r"\frac{b-a}{n}", r"=\frac{2-0}{6}", r"=\frac{1}{3}", color=RED).scale(0.8).next_to(eq2, RIGHT)
        



        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1)), 
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(2)
        self.play(Transform(rhs1, rhs1a))
        self.wait(5) 
        self.play(Write(lhs2))       
        self.wait(3)
        self.play(Write(eq2), Write(rhs2[0]))        
        self.wait(3)
        self.play(Wiggle(title1[1]))
        self.play(Write(rhs2[1]), )
        self.wait(3)
        self.play(Write(rhs2[2]))
        self.wait(3)
        self.play(Wiggle(title1[1]))
        self.play(Transform(rhs1, rhs1b), )
        self.wait(4)
        self.play(Transform(rhs1, rhs1c))
        self.wait(4)
        self.play(Transform(rhs1, rhs1d))
        self.wait(5)


        self.play(
            FadeOut(rhs2,lhs2, eq2))


        rhs2 = MathTex(r"\frac{1}{3}\Biggl(", r"f\left(\frac{1}{3}\right)", r"+f\left(\frac{2}{3}\right)",  r"+f\left(\frac{3}{3}\right)" , 
            r"+f\left(\frac{4}{3}\right)", r"+f\left(\frac{5}{3}\right)", r"+f\left(\frac{6}{3}\right)", r"\Biggr)").scale(0.8).next_to(eq2, RIGHT)

        #rhs3 = MathTex(r"\frac{1}{3}\Biggl(", 
        #    r"6 \left(\frac{1}{3}\right)^3-9 \left(\frac{1}{3}\right)^2+3", 
        #    r"+ 6 \left(\frac{2}{3}\right)^3-9 \left(\frac{2}{3}\right)^2+3", 
        #    r"+ 6 \left(\frac{3}{3}3\right)^3-9 \left(\frac{3}{3}\right)^2+3" , 
        ##    r"+ 6 \left(\frac{4}{3}1\right)^3-9 \left(\frac{4}{3}\right)^2+3", 
        #    r"+ 6 \left(\frac{5}{3}1\right)^3-9 \left(\frac{5}{3}\right)^2+3", 
        #    r"+ 6 \left(\frac{6}{3}1\right)^3-9 \left(\frac{6}{3}\right)^2+3",
        #    r"\Biggr)").scale(0.5).next_to(eq3, RIGHT)

        rhs3 = MathTex(r"\frac{1}{3}\Biggl(",
            r"\frac{20}{9}", 
            r"+ \frac{7}{9}" , 
            r"+ 0", 
            r"+ \frac{11}{9}", 
            r"+ \frac{52}{9}",
            r"+ \frac{135}{9}",
            r"\Biggr)").scale(0.8).next_to(eq3, RIGHT)
        rhs4 = MathTex(r"\frac{1}{3}(", 
            r"25", 
            r")").scale(0.8).next_to(eq4, RIGHT)

        rhs4a = MathTex(r"\frac{25}{3}",).scale(0.8).next_to(eq4, RIGHT)

        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3))
        for x in range(0, 8):
            self.play(Write(rhs3[x]))
            self.wait(2)
        self.wait(3)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(5)
        #self.play(Transform(rhs4, rhs4b))

            
class ShowPlot2(Scene):
    def construct(self):


        title1 = MathTex(r"\frac{1}{3}\Biggl(",
            r"\frac{20}{9}", 
            r"+ \frac{7}{9}" , 
            r"+ 0", 
            r"+ \frac{11}{9}", 
            r"+ \frac{52}{9}",
            r"+ \frac{135}{9}",
            r"\Biggr)", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        axes = Axes(x_range=[0,2,0.5], y_range=[0,20,5], x_length=6, y_length=5,)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[0,2,0.5], y_range=[0,20,5],
            x_length=6,
            y_length=5,
            ).add_coordinates()

        
        
        

        theplot = axes.plot(lambda x: 6*x**3-9*x**2+3, 
            x_range=[0, 2], 
            use_smoothing=True,
            color=YELLOW)

        plotlabel = MathTex("f(x)=6x^3-9x^2+3").scale(0.5).next_to(theplot, RIGHT, buff=0.5).set_color(YELLOW)

        rectangles = numberplane.get_riemann_rectangles(theplot, x_range= [0,2 ], dx=2/6, color=RED, fill_opacity=0.6, input_sample_type="right")

        self.add(axes, axes_labels, numberplane, title1)
        self.play(Create(theplot), Write(plotlabel))
        self.play(Create(rectangles))
        self.wait(10)


class ShowPlot3(Scene):
    def construct(self):


        title1 = MathTex(r"R_n, \text{where } n=", color=TEAL).scale(0.8).to_edge(UP)

        caption1 = MathTex(r"R_n \approx", color=ORANGE).scale(0.8).to_edge(DOWN)

        axes = Axes(x_range=[0,2,0.5], y_range=[0,20,5], x_length=6, y_length=5,)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[0,2,0.5], y_range=[0,20,5],
            x_length=6,
            y_length=5,
            ).add_coordinates()

        
        
        

        theplot = axes.plot(lambda x: 6*x**3-9*x**2+3, 
            x_range=[0, 2], 
            use_smoothing=True,
            color=YELLOW)

        rectangles = numberplane.get_riemann_rectangles(theplot, x_range= [0,2 ], dx=2/6, color=RED, fill_opacity=0.6, input_sample_type="right")

        tracker=ValueTracker(6)



        
        
        def update(mob):
            mob.become(
                numberplane.get_riemann_rectangles(theplot, 
                    x_range= [0,2 ], 
                    dx=2/np.floor(tracker.get_value()), 
                    color=RED, fill_opacity=0.6, input_sample_type="right")
                
        )
        

        rectangles.add_updater(update)

        number=DecimalNumber(
            6,
            show_ellipsis=False,
            num_decimal_places=0,
            include_sign=False,
            color=TEAL,
        ).scale(0.8).next_to(title1, RIGHT)
        def updateNum(mob):
            mob.become(DecimalNumber(
            np.floor(tracker.get_value()),
            show_ellipsis=False,
            num_decimal_places=0,
            include_sign=False,
            color=TEAL,
        )).scale(0.7).next_to(title1, RIGHT)
        number.add_updater(updateNum)


        number2=DecimalNumber(
            8.3333,
            show_ellipsis=True,
            num_decimal_places=4,
            include_sign=False,
            color=ORANGE
        ).scale(0.8).next_to(caption1, RIGHT)
        def updateNum2(mob):
            mob.become(DecimalNumber(
            6*((tracker.get_value()**2+2*(tracker.get_value())+2 ))/((tracker.get_value())**2),
            show_ellipsis=True,
            num_decimal_places=4,
            include_sign=False,
            color=ORANGE
        )).scale(0.7).next_to(caption1, RIGHT)
        number2.add_updater(updateNum2)

        plotlabel = MathTex("f(x)=6x^3-9x^2+3").scale(0.5).next_to(theplot, RIGHT, buff=0.5).set_color(YELLOW)

        

        self.add(axes, axes_labels, numberplane, title1, rectangles, theplot, plotlabel, number, caption1, number2)
        self.wait(5)
        self.play(tracker.animate.set_value(20), run_time=5)        
        self.wait(3)
        self.play(tracker.animate.set_value(500), run_time=5)        
        self.wait(3)
        self.play(tracker.animate.set_value(1), run_time=5)
        self.wait(3)
        self.play(tracker.animate.set_value(6), run_time=2)
        self.wait(5)



        
class FindRn(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find } R_n, \text{for } f(x)=6x^3-9x^2+3 \text{ on }", " [0, 2].", color=TEAL).scale(0.8).to_edge(UP)        
        
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*4)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*7)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*7)

        lhs1 = MathTex(r"R_n").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \sum_{i=1}^n f(x_i)", "\Delta x",).scale(0.8).next_to(eq1, RIGHT)
        rhs1[1].set_color(RED)
        rhs1a = MathTex(r"\displaystyle \sum_{i=1}^n f(a+i", r"\Delta x", ")", r"\Delta x",).scale(0.8).next_to(eq1, RIGHT)
        rhs1a[1].set_color(RED)
        rhs1a[3].set_color(RED)
        rhs1b = MathTex(r"\displaystyle \sum_{i=1}^n f(0+i", r"\Delta x", r")", r"\Delta x",).scale(0.8).next_to(eq1, RIGHT)
        rhs1b[1].set_color(RED)
        rhs1b[3].set_color(RED)
        rhs1c = MathTex(r"\displaystyle \sum_{i=1}^n f\Biggl(0+i ", r" \frac{2}{n}", r"\Biggr)", r"\frac{2}{n}",).scale(0.8).next_to(eq1, RIGHT)
        rhs1c[1].set_color(RED)
        rhs1c[3].set_color(RED)
        rhs1d = MathTex(r"\displaystyle \sum_{i=1}^n f\Biggl(", r"\frac{2}{n}", r"i\Biggr)", r"\frac{2}{n}",).scale(0.8).next_to(eq1, RIGHT)
        rhs1d[1].set_color(RED)
        rhs1d[3].set_color(RED)
        rhs1e = MathTex(r"\displaystyle \sum_{i=1}^n  \left( 6\left( \frac{2}{n} i\right)^3 - 9\left( \frac{2}{n}i\right)^2 +3  \right)\frac{2}{n}",).scale(0.8).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"\displaystyle  \left( 6\sum_{i=1}^n \left( \frac{2}{n}i\right)^3 - 9\sum_{i=1}^n \left( \frac{2}{n}i\right)^2 + \sum_{i=1}^n 3  \right)\frac{2}{n}",).scale(0.8).next_to(eq2, RIGHT)
        rhs3 = MathTex(r"\displaystyle  \left( 6\sum_{i=1}^n \left( \frac{2}{n}i\right)^3 - 9\sum_{i=1}^n \left( \frac{2}{n}i\right)^2 + 3n  \right)\frac{2}{n}",).scale(0.8).next_to(eq3, RIGHT)
        rhs3a = MathTex(r"\displaystyle  \left( 6\sum_{i=1}^n \left( \frac{2}{n}i\right)^3 - 9\frac{4}{n^2}\sum_{i=1}^n (i^2) + 3n  \right)\frac{2}{n}",).scale(0.8).next_to(eq3, RIGHT)
        rhs3b = MathTex(r"\displaystyle  \left( 6\frac{8}{n^3}\sum_{i=1}^n (i^3) - 9\frac{4}{n^2}\sum_{i=1}^n (i^2) + 3n  \right)\frac{2}{n}",).scale(0.8).next_to(eq3, RIGHT)
        rhs3c = MathTex(r"\displaystyle   6\frac{8\cdot 2}{n^3\cdot n}\sum_{i=1}^n (i^3) - 9\frac{4\cdot 2}{n^2\cdot n}\sum_{i=1}^n (i^2) + 3n\frac{2}{n}  ",).scale(0.8).next_to(eq3, RIGHT)
        rhs3d = MathTex(r"\displaystyle   \frac{96}{n^4}\sum_{i=1}^n (i^3) - \frac{72}{n^3}\sum_{i=1}^n (i^2) + 6  ",).scale(0.8).next_to(eq3, RIGHT)
        rhs3e = MathTex(r"\displaystyle   \frac{96}{n^4}\sum_{i=1}^n (i^3) - \frac{72}{n^3} \frac{n(n+1)(2n+1)}{6} + 6  ",).scale(0.8).next_to(eq3, RIGHT)
        rhs3f = MathTex(r"\displaystyle   \frac{96}{n^4}\frac{n^2(n+1)^2}{4} - \frac{72}{n^3} \frac{n(n+1)(2n+1)}{6} + 6  ",).scale(0.8).next_to(eq3, RIGHT)
        rhs3g = MathTex(r"\displaystyle   24\frac{n^4+2n^3+n^2}{n^4} - 12 \frac{2n^3+3n^2+n}{n^3} + 6  ",).scale(0.8).next_to(eq3, RIGHT)
        



        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1)), 
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(2)
        self.play(Transform(rhs1, rhs1a))
        self.wait(3)
        self.play(Wiggle(title1[1]))
        self.play(Transform(rhs1, rhs1b), )
        self.wait(4)
        self.play(Transform(rhs1, rhs1c))
        self.wait(4)
        self.play(Transform(rhs1, rhs1d))
        self.wait(4)
        self.play(Transform(rhs1, rhs1e))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(FadeOut(rhs2), rhs3.animate.next_to(eq2, RIGHT), Write(rhs3a))
        self.wait(5)
        self.play(FadeOut(rhs3), rhs3a.animate.next_to(eq2, RIGHT), Write(rhs3b))
        self.wait(5)
        self.play(FadeOut(rhs3a), rhs3b.animate.next_to(eq2, RIGHT), Write(rhs3c))
        self.wait(5)
        self.play(FadeOut(rhs3b), rhs3c.animate.next_to(eq2, RIGHT), Write(rhs3d))
        self.wait(5)
        self.play(FadeOut(rhs3c), rhs3d.animate.next_to(eq2, RIGHT), Write(rhs3e))
        self.wait(5)
        self.play(FadeOut(rhs3d), rhs3e.animate.next_to(eq2, RIGHT), Write(rhs3f))
        self.wait(5)
        self.play(FadeOut(rhs3e), rhs3f.animate.next_to(eq2, RIGHT), Write(rhs3g))
        self.wait(3)
        self.play(FadeOut(rhs3f), rhs3g.animate.next_to(eq2, RIGHT), FadeOut(eq3))
        self.wait(5)


class FindArea(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the area bound by } y=6x^3-9x^2+3, y=0 \text{ on }", " [0, 2].", color=TEAL).scale(0.8).to_edge(UP)      
        caption1 = MathTex(r"\text{The area is }6.", color=ORANGE).scale(0.8).to_edge(DOWN)        
        
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"\displaystyle \int_0^2 6x^3-9x^2+3 dx").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \lim_{n\to \infty}R_n",).scale(0.8).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"\displaystyle  \lim_{n\to \infty}\Biggl(24{",  r" n^4", r"+2n^3+n^2 \over ", r" n^4 }", r" - 12 ", r"{2n^3 ", r"+3n^2+n \over ", r" n^3 ", r" } + 6 \Biggr)",).scale(0.8).next_to(eq2, RIGHT)

        rhs3 = MathTex(r"24(1)-12(2)+6",).scale(0.8).next_to(eq3, RIGHT)
        rhs4 = MathTex(r"6.",).scale(0.8).next_to(eq4, RIGHT)

        



        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1)), 
        self.wait(3)
        self.play(Write(eq1), Write(rhs1))
        self.wait(5)
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Wiggle(rhs2[1]), Wiggle(rhs2[3]), )
        self.play(rhs2[1].animate.set_color(RED), rhs2[3].animate.set_color(RED))
        self.wait(2)
        self.play(Wiggle(rhs2[5]), Wiggle(rhs2[7]),)
        self.play( rhs2[5].animate.set_color(RED), rhs2[7].animate.set_color(RED))
        self.wait(2)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Write(caption1))
        self.wait(10)        

       





        
        



        


        
        



        



  
       