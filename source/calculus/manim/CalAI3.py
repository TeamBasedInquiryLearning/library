from manim import *



class ShowSolidxW(ThreeDScene):
    def func(self, u, v):
        return np.array([u,v, 3*v**2-2*u])
    
    def construct(self):
     #3d stuff   
        title = MathTex(r"\text{Region bounded by }", r"y=\frac{x}{2}, ", r" y=\sqrt{x}", r"\text{ rotated about the }x\text{-axis.}").scale(0.8)         
        title.to_edge(DOWN)
        title[1].set_color(BLUE)
        title[2].set_color(GREEN)

        caption = MathTex(r"\text{Area }=\displaystyle  \pi R_O^2-\pi R_I^2.", color=ORANGE).scale(0.8).to_edge(UP)   


        axes = ThreeDAxes()
        axes_labels = axes.get_axis_labels()
        surface1 = Surface(
            lambda u, v: np.array([u, u**(1/2)*np.cos(v), u**(1/2)*np.sin(v)]),
            u_range=[0.01, 4],
            v_range=[0, 2*PI],
            resolution=15,


        )
        surface1.set_fill_by_checkerboard(GREEN, GREEN, opacity=0.4)

        surface2 = Surface(
            lambda u, v: np.array([u, u*np.cos(v)/2, u*np.sin(v)/2]),
            u_range=[0.01, 4],
            v_range=[0, 2*PI],
            resolution=15,


        )
        surface2.set_fill_by_checkerboard(BLUE, BLUE, opacity=0.4)
        

        curve1 = ParametricFunction(
            lambda u: np.array([
                u,
                u**(1/2),
                0
            ]) , color=GREEN, t_range=[0,4],
        ).set_shade_in_3d(True)

        curve2 = ParametricFunction(
            lambda u: np.array([
                u,
                u/2,
                0
            ]) , color=BLUE, t_range=[0,4],
        ).set_shade_in_3d(True)


        washer = Surface(
            lambda u, v: np.array([1, u*1*np.cos(v) +(1-u)*np.cos(v)/2, u*1*np.sin(v) +(1-u)*np.sin(v)/2]),
            u_range=[0, 1],
            v_range=[0, 2*PI],
            resolution=15,


        ).set_fill_by_checkerboard(RED, RED, opacity=1)

        tracker=ValueTracker(1)


        P1=Dot([0,0,0], color=RED)
        label1 = MathTex(r"(0,0)", color=RED).scale(0.5).next_to(P1, DOWN/1.4+LEFT/1.4)

        P2=Dot([4,2,0], color=RED)
        label2 = MathTex(r"(4,2)", color=RED).scale(0.5).next_to(P2, UP/1.4+RIGHT/1.4)

        
        
        def update(mob):
            mob.become(
                Surface(
            lambda u, v: np.array([tracker.get_value(), u*(tracker.get_value())**(1/2)*1*np.cos(v) +(1-u)*(tracker.get_value())*np.cos(v)/2, 
                u*(tracker.get_value())**(1/2)*1*np.sin(v) +(1-u)*(tracker.get_value())*np.sin(v)/2]),
            u_range=[0, 1],
            v_range=[0, 2*PI],
            resolution=15,


        ).set_fill_by_checkerboard(RED, RED, opacity=1)
                
        )
        

        washer.add_updater(update)

        

        



        self.add_fixed_in_frame_mobjects(title)
        self.set_camera_orientation(theta=270 * DEGREES, phi=0 * DEGREES, zoom=0.7)
        self.add(axes, axes_labels)
        self.play(Create(curve1))
        self.play(Create(curve2))
        self.wait(5)
        self.play(Create(P1), Create(P2), Write(label1), Write(label2))
        self.wait(5)
        self.move_camera(theta=270 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.play(Create(surface2))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        
        self.move_camera(theta=270 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.play(Create(surface1))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=300 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.wait(5)
        self.play(Create(washer))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=300 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.play(tracker.animate.set_value(0.01), run_time=1)
        self.wait(3)
        self.play(tracker.animate.set_value(4), run_time=6)
        self.wait(3)
        self.play(tracker.animate.set_value(0.01), run_time=2)
        self.move_camera(theta=0 * DEGREES, phi=90 * DEGREES, zoom=0.7)
        self.add_fixed_in_frame_mobjects(caption)
        self.play(tracker.animate.set_value(4), run_time=3)
        self.play(tracker.animate.set_value(0.01), run_time=3)
        self.move_camera(theta=300 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.play(tracker.animate.set_value(2), run_time=0.5)


        self.wait(5)







class FindVxW(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the volume of the region  bounded by }", r"y=\frac{x}{2}, ", r" y=\sqrt{x}", r"\text{ rotated about the }x\text{-axis.}", color=TEAL).scale(0.6).to_edge(UP)        
        
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"V").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \int_0^4 \text{Area}\,dx",).scale(0.8).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"\displaystyle \int_0^4 \pi R_O^2-\pi R_I^2\,dx",).scale(0.8).next_to(eq1, RIGHT)
        rhs1b = MathTex(r"\displaystyle \int_0^4 \pi \left(\sqrt{x}\right)^2-\pi \left( \frac{x}{2}\right)^2\,dx",).scale(0.8).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"\pi \displaystyle \int_0^4  \frac{1}{4} x^2 -x\,dx",).scale(0.8).next_to(eq2, RIGHT)
        rhs3 = MathTex(r"\pi \left( \frac{1}{2}x^2- \frac{1}{12} x^3  \mid_{x=0}^{x=4} \right)",).scale(0.8).next_to(eq3, RIGHT)

        rhs4 = MathTex(r"\pi \left( \left( \frac{1}{2}4^2 - \frac{1}{12} 4^3  \right) -0 \right)",).scale(0.8).next_to(eq4, RIGHT)
        rhs4a = MathTex(r" \frac{8}{3} \pi ",).scale(0.8).next_to(eq4, RIGHT)
        

        



        
        self.add(title1)
        self.wait(3)
        self.play(Write(lhs1)), 
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(4)
        self.play(Transform(rhs1, rhs1a))
        self.wait(4)
        self.play(Transform(rhs1, rhs1b))
        self.wait(5) 
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10) 


        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4))        

class ShowSolidxS(ThreeDScene):
    def func(self, u, v):
        return np.array([u,v, 3*v**2-2*u])
    
    def construct(self):
     #3d stuff   
        title = MathTex(r"\text{Region bounded by }", r"y=\frac{x}{2}, ", r" y=\sqrt{x}", r"\text{ rotated about the }x\text{-axis.}").scale(0.8)         
        title.to_edge(DOWN)
        title[1].set_color(BLUE)
        title[2].set_color(GREEN)

        caption = MathTex(r"\text{Area }=\displaystyle  2\pi R(H_U-H_D).", color=ORANGE).scale(0.8).to_edge(UP)   


        axes = ThreeDAxes()
        axes_labels = axes.get_axis_labels()
        surface1 = Surface(
            lambda u, v: np.array([u, u**(1/2)*np.cos(v), u**(1/2)*np.sin(v)]),
            u_range=[0.01, 4],
            v_range=[0, 2*PI],
            resolution=15,


        )
        surface1.set_fill_by_checkerboard(GREEN, GREEN, opacity=0.4)

        surface2 = Surface(
            lambda u, v: np.array([u, u*np.cos(v)/2, u*np.sin(v)/2]),
            u_range=[0.01, 4],
            v_range=[0, 2*PI],
            resolution=15,


        )
        surface2.set_fill_by_checkerboard(BLUE, BLUE, opacity=0.4)
        

        curve1 = ParametricFunction(
            lambda u: np.array([
                u,
                u**(1/2),
                0
            ]) , color=GREEN, t_range=[0,4],
        ).set_shade_in_3d(True)

        curve2 = ParametricFunction(
            lambda u: np.array([
                u,
                u/2,
                0
            ]) , color=BLUE, t_range=[0,4],
        ).set_shade_in_3d(True)


        shell = Surface(
            lambda u, v: np.array([ u*(1)**2+(1-u)*2*(1), 
                1*np.cos(v),             
                1*np.sin(v)]),
            u_range=[0, 1],
            v_range=[0, 2*PI],
            resolution=15,


        ).set_fill_by_checkerboard(RED, RED, opacity=1)

        tracker=ValueTracker(1)


        P1=Dot([0,0,0], color=RED)
        label1 = MathTex(r"(0,0)", color=RED).scale(0.5).next_to(P1, DOWN/1.4+LEFT/1.4)

        P2=Dot([4,2,0], color=RED)
        label2 = MathTex(r"(4,2)", color=RED).scale(0.5).next_to(P2, UP/1.4+RIGHT/1.4)

        
        
        def update(mob):
            mob.become(
                Surface(
            lambda u, v: np.array(
                [u*(tracker.get_value())**2+(1-u)*2*(tracker.get_value()), 
                tracker.get_value()*np.cos(v),                 
                tracker.get_value()*np.sin(v)]),
            u_range=[0, 1],
            v_range=[0, 2*PI],
            resolution=15,


        ).set_fill_by_checkerboard(RED, RED, opacity=1)
                
        )
        

        shell.add_updater(update)

        

        



        self.add_fixed_in_frame_mobjects(title)
        self.set_camera_orientation(theta=270 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.add(axes, axes_labels)
        self.play(Create(curve1), Create(curve2), Create(P1), Create(P2), 
            Write(label1), Write(label2), Create(surface2), Create(surface1))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=300 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.wait(5)
        self.play(Create(shell))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=300 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.play(tracker.animate.set_value(0.01), run_time=1)
        self.wait(3)
        self.play(tracker.animate.set_value(2), run_time=6)
        self.wait(3)
        self.play(tracker.animate.set_value(0.01), run_time=2)
        self.move_camera(theta=0 * DEGREES, phi=90 * DEGREES, zoom=0.7)
        self.add_fixed_in_frame_mobjects(caption)
        self.play(tracker.animate.set_value(2), run_time=3)
        self.play(tracker.animate.set_value(0.01), run_time=3)
        self.move_camera(theta=270 * DEGREES, phi=90 * DEGREES, zoom=0.7)
        self.play(tracker.animate.set_value(2), run_time=3)
        self.play(tracker.animate.set_value(0.01), run_time=3)
        self.move_camera(theta=300 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.play(tracker.animate.set_value(1), run_time=0.5)


        self.wait(5)        


class FindVxS(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the volume of the region  bounded by }", r"y=\frac{x}{2}, ", r" y=\sqrt{x}", r"\text{ rotated about the }x\text{-axis.}", color=TEAL).scale(0.6).to_edge(UP)        
        title1a = MathTex(r"\text{Find the volume of the region  bounded by }", r"x=2y, ", r" x=y^2", r"\text{ rotated about the }x\text{-axis.}", color=TEAL).scale(0.6).to_edge(UP)        
        title1a[1].set_color(RED)
        title1a[2].set_color(RED)

        
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"V").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \int_0^2 \text{Area}\,dy",).scale(0.8).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"\displaystyle \int_0^2 2\pi R(H_U-H_D)\,dy",).scale(0.8).next_to(eq1, RIGHT)
        rhs1b = MathTex(r"\displaystyle \int_0^2 2\pi y(H_U-H_D)\,dy",).scale(0.8).next_to(eq1, RIGHT)
        rhs1c = MathTex(r"\displaystyle \int_0^2 2\pi y(2y-y^2)\,dy",).scale(0.8).next_to(eq1, RIGHT)


        rhs2 = MathTex(r"2\pi \displaystyle \int_0^2  2y^{2} -y^3 \,dy",).scale(0.8).next_to(eq2, RIGHT)
        rhs3 = MathTex(r"2\pi \left( \frac{2}{3}y^3- \frac{1}{4} y^4  \mid_{y=0}^{y=2} \right)",).scale(0.8).next_to(eq3, RIGHT)

        rhs4 = MathTex(r"2\pi \left( \left( \frac{2}{3}2^3 - \frac{1}{4} 2^4  \right) -0 \right)",).scale(0.8).next_to(eq4, RIGHT)
        rhs4a = MathTex(r" \frac{8}{3} \pi ",).scale(0.8).next_to(eq4, RIGHT)
        

        



        
        self.add(title1)
        self.wait(5)
        self.play(Wiggle(title1[1]), Wiggle(title1[2]))
        self.play(Transform(title1, title1a))
        self.wait(3)
        self.play(Write(lhs1)), 
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(4)
        self.play(Transform(rhs1, rhs1a))
        self.wait(4)
        self.play(Transform(rhs1, rhs1b))
        self.wait(4) 
        self.play(Transform(rhs1, rhs1c))
        self.wait(5) 
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10) 


        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4))    






class ShowSolidyW(ThreeDScene):
    def func(self, u, v):
        return np.array([u,v, 3*v**2-2*u])
    
    def construct(self):
     #3d stuff   
        title = MathTex(r"\text{Region bounded by }", r"y=\frac{x}{2}, ", r" y=\sqrt{x}", r"\text{ rotated about the }y\text{-axis.}").scale(0.8)         
        title.to_edge(DOWN)
        title[1].set_color(BLUE)
        title[2].set_color(GREEN)

        caption = MathTex(r"\text{Area }=\displaystyle  \pi R_O^2-\pi R_I^2.", color=ORANGE).scale(0.8).to_edge(UP)   


        axes = ThreeDAxes()
        axes_labels = axes.get_axis_labels()
        surface1 = Surface(
            lambda u, v: np.array([u**(2)*np.cos(v), u, u**(2)*np.sin(v)]),
            u_range=[0.01, 2],
            v_range=[0, 2*PI],
            resolution=15,


        )
        surface1.set_fill_by_checkerboard(GREEN, GREEN, opacity=0.4)

        surface2 = Surface(
            lambda u, v: np.array([u*np.cos(v)*2, u, u*np.sin(v)*2]),
            u_range=[0.01, 2],
            v_range=[0, 2*PI],
            resolution=15,


        )
        surface2.set_fill_by_checkerboard(BLUE, BLUE, opacity=0.4)
        

        curve1 = ParametricFunction(
            lambda u: np.array([
                u,
                u**(1/2),
                0
            ]) , color=GREEN, t_range=[0,4],
        ).set_shade_in_3d(True)

        curve2 = ParametricFunction(
            lambda u: np.array([
                u,
                u/2,
                0
            ]) , color=BLUE, t_range=[0,4],
        ).set_shade_in_3d(True)


        washer = Surface(
            lambda u, v: np.array(
                [u*(1)**(2)*np.cos(v) +(1-u)*np.cos(v)*2, 
                1,
                u*(1)**(2)*np.sin(v) +(1-u)*np.sin(v)*2]),
            u_range=[0, 1],
            v_range=[0, 2*PI],
            resolution=15,


        ).set_fill_by_checkerboard(RED, RED, opacity=1)

        tracker=ValueTracker(1)


        P1=Dot([0,0,0], color=RED)
        label1 = MathTex(r"(0,0)", color=RED).scale(0.5).next_to(P1, DOWN/1.4+LEFT/1.4)

        P2=Dot([4,2,0], color=RED)
        label2 = MathTex(r"(4,2)", color=RED).scale(0.5).next_to(P2, UP/1.4+RIGHT/1.4)

        
        
        def update(mob):
            mob.become(
                Surface(
            lambda u, v: np.array(
                [u*(tracker.get_value())**(2)*np.cos(v) +(1-u)*tracker.get_value()*np.cos(v)*2, 
                tracker.get_value(),
                u*(tracker.get_value())**(2)*np.sin(v) +(1-u)*tracker.get_value()*np.sin(v)*2]),
            u_range=[0, 1],
            v_range=[0, 2*PI],
            resolution=15,


        ).set_fill_by_checkerboard(RED, RED, opacity=1)
                
        )
        

        washer.add_updater(update)

        

        



        self.add_fixed_in_frame_mobjects(title)
        self.set_camera_orientation(theta=270 * DEGREES, phi=0 * DEGREES, zoom=0.7)
        self.add(axes, axes_labels)
        self.play(Create(curve1))
        self.play(Create(curve2))
        self.play(Create(P1), Create(P2), Write(label1), Write(label2))
        self.wait(5)
        self.move_camera(theta=270 * DEGREES, phi=60 * DEGREES, zoom=0.7)
        self.play(Create(surface2))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        
        self.move_camera(theta=45 * DEGREES, phi=60 * DEGREES, zoom=0.7)
        self.play(Create(surface1))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=45 * DEGREES, phi=60 * DEGREES, zoom=0.7)
        self.wait(5)
        self.play(Create(washer))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=45 * DEGREES, phi=60 * DEGREES, zoom=0.7)
        self.play(tracker.animate.set_value(0.01), run_time=1)
        self.wait(3)
        self.play(tracker.animate.set_value(2), run_time=6)
        self.wait(3)
        self.play(tracker.animate.set_value(0.01), run_time=2)
        self.move_camera(theta=90 * DEGREES, phi=90 * DEGREES, zoom=0.6)
        self.add_fixed_in_frame_mobjects(caption)
        self.play(tracker.animate.set_value(2), run_time=3)
        self.play(tracker.animate.set_value(0.01), run_time=3)
        self.move_camera(theta=45 * DEGREES, phi=60 * DEGREES, zoom=0.7)
        self.play(tracker.animate.set_value(1), run_time=0.5)


        self.wait(5)       



class FindVyW(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the volume of the region  bounded by }", r"y=\frac{x}{2}, ", r" y=\sqrt{x}", r"\text{ rotated about the }y\text{-axis.}", color=TEAL).scale(0.6).to_edge(UP)
        title1a = MathTex(r"\text{Find the volume of the region  bounded by }", r"x=2y, ", r" x=y^2", r"\text{ rotated about the }x\text{-axis.}", color=TEAL).scale(0.6).to_edge(UP)        
        title1a[1].set_color(RED)
        title1a[2].set_color(RED)
        
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"V").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \int_0^2 \text{Area}\,dy",).scale(0.8).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"\displaystyle \int_0^2 \pi R_O^2-\pi R_I^2\,dy",).scale(0.8).next_to(eq1, RIGHT)
        rhs1b = MathTex(r"\displaystyle \int_0^2 \pi \left(2y\right)^2-\pi \left( y^2 \right)^2\,dx",).scale(0.8).next_to(eq1, RIGHT)

        rhs2 = MathTex(r"\pi \displaystyle \int_0^2  4y^2 -y^4\,dx",).scale(0.8).next_to(eq2, RIGHT)
        rhs3 = MathTex(r"\pi \left( \frac{4}{3}y^3- \frac{1}{5} y^5  \mid_{y=0}^{y=2} \right)",).scale(0.8).next_to(eq3, RIGHT)

        rhs4 = MathTex(r"\pi \left( \left( \frac{4}{3}2^3- \frac{1}{5} 2^5  \right) -0 \right)",).scale(0.8).next_to(eq4, RIGHT)
        rhs4a = MathTex(r" \frac{64}{15} \pi ",).scale(0.8).next_to(eq4, RIGHT)
        

        



        
        self.add(title1)
        self.wait(5)
        self.play(Wiggle(title1[1]), Wiggle(title1[2]))
        self.play(Transform(title1, title1a))
        self.wait(5)
        self.play(Write(lhs1)), 
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(4)
        self.play(Transform(rhs1, rhs1a))
        self.wait(4)
        self.play(Transform(rhs1, rhs1b))
        self.wait(5) 
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10) 


        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4))          



class ShowSolidyS(ThreeDScene):
    def func(self, u, v):
        return np.array([u,v, 3*v**2-2*u])
    
    def construct(self):
     #3d stuff   
        title = MathTex(r"\text{Region bounded by }", r"y=\frac{x}{2}, ", r" y=\sqrt{x}", r"\text{ rotated about the }y\text{-axis.}").scale(0.8)         
        title.to_edge(DOWN)
        title[1].set_color(BLUE)
        title[2].set_color(GREEN)

        caption = MathTex(r"\text{Area }=\displaystyle  2\pi R(H_U-H_D).", color=ORANGE).scale(0.8).to_edge(UP)   


        axes = ThreeDAxes()
        axes_labels = axes.get_axis_labels()
        surface1 = Surface(
            lambda u, v: np.array([u, u**(1/2)*np.cos(v), u**(1/2)*np.sin(v)]),
            u_range=[0.01, 4],
            v_range=[0, 2*PI],
            resolution=15,


        )
        

        surface1 = Surface(
            lambda u, v: np.array([u**(2)*np.cos(v), u, u**(2)*np.sin(v)]),
            u_range=[0.01, 2],
            v_range=[0, 2*PI],
            resolution=15,


        )
        surface1.set_fill_by_checkerboard(GREEN, GREEN, opacity=0.4)

        surface2 = Surface(
            lambda u, v: np.array([u*np.cos(v)*2, u, u*np.sin(v)*2]),
            u_range=[0.01, 2],
            v_range=[0, 2*PI],
            resolution=15,


        )
        surface2.set_fill_by_checkerboard(BLUE, BLUE, opacity=0.4)
        

        curve1 = ParametricFunction(
            lambda u: np.array([
                u,
                u**(1/2),
                0
            ]) , color=GREEN, t_range=[0,4],
        ).set_shade_in_3d(True)

        curve2 = ParametricFunction(
            lambda u: np.array([
                u,
                u/2,
                0
            ]) , color=BLUE, t_range=[0,4],
        ).set_shade_in_3d(True)


        shell = Surface(
            lambda u, v: np.array([ 
                (1)*np.cos(v),  
                u*(1)/2 + (1-u)*(1)**(1/2),            
                (1)*np.sin(v)]),
            u_range=[0, 1],
            v_range=[0, 2*PI],
            resolution=15,


        ).set_fill_by_checkerboard(RED, RED, opacity=1)

        tracker=ValueTracker(1)


        P1=Dot([0,0,0], color=RED)
        label1 = MathTex(r"(0,0)", color=RED).scale(0.5).next_to(P1, DOWN/1.4+LEFT/1.4)

        P2=Dot([4,2,0], color=RED)
        label2 = MathTex(r"(4,2)", color=RED).scale(0.5).next_to(P2, UP/1.4+RIGHT/1.4)

        
        
        def update(mob):
            mob.become(
                Surface(
            lambda u, v: np.array(
                [(tracker.get_value())*np.cos(v),  
                u*(tracker.get_value())/ 2 + (1-u)*(tracker.get_value())**(1/2),            
                (tracker.get_value())*np.sin(v)]),
            u_range=[0, 1],
            v_range=[0, 2*PI],
            resolution=15,


        ).set_fill_by_checkerboard(RED, RED, opacity=1)
                
        )
        

        shell.add_updater(update)

        

        



        self.add_fixed_in_frame_mobjects(title)
        self.set_camera_orientation(theta=270 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.add(axes, axes_labels)
        self.play(Create(curve1), Create(curve2), Create(P1), Create(P2), 
            Write(label1), Write(label2), Create(surface2), Create(surface1))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=45 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.wait(5)
        self.play(Create(shell))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=45 * DEGREES, phi=60 * DEGREES, zoom=0.6)
        self.play(tracker.animate.set_value(0.01), run_time=1)
        self.wait(3)
        self.play(tracker.animate.set_value(4), run_time=6)
        self.wait(3)
        self.play(tracker.animate.set_value(0.01), run_time=2)
        self.move_camera(theta=270 * DEGREES, phi=0 * DEGREES, zoom=0.7)
        self.add_fixed_in_frame_mobjects(caption)
        self.play(tracker.animate.set_value(4), run_time=3)
        self.play(tracker.animate.set_value(0.01), run_time=3)
        self.move_camera(theta=90 * DEGREES, phi=90 * DEGREES, zoom=0.6)
        self.play(tracker.animate.set_value(4), run_time=3)
        self.play(tracker.animate.set_value(0.01), run_time=3)
        self.move_camera(theta=45 * DEGREES, phi=60 * DEGREES, zoom=0.7)
        self.play(tracker.animate.set_value(2), run_time=0.5)


        self.wait(5)                                






class FindVyS(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Find the volume of the region  bounded by }", r"y=\frac{x}{2}, ", r" y=\sqrt{x}", r"\text{ rotated about the }y\text{-axis.}", color=TEAL).scale(0.6).to_edge(UP)        
        #title1a = MathTex(r"\text{Find the volume of the region  bounded by }", r"x=2y, ", r" x=y^2", r"\text{ rotated about the }x\text{-axis.}", color=TEAL).scale(0.6).to_edge(UP)        
        #title1a[1].set_color(RED)
        #title1a[2].set_color(RED)

        
        

        eq1 = MathTex(r"=").scale(0.8).shift(UP*2+LEFT*2)
        eq2 = MathTex(r"=").scale(0.8).next_to(eq1, DOWN*5)
        eq3 = MathTex(r"=",).scale(0.8).next_to(eq2, DOWN*5)
        eq4 = MathTex(r"=").scale(0.8).next_to(eq3, DOWN*5)

        lhs1 = MathTex(r"V").scale(0.8).next_to(eq1, LEFT)
        rhs1 = MathTex(r"\displaystyle \int_0^4 \text{Area}\,dx",).scale(0.8).next_to(eq1, RIGHT)
        rhs1a = MathTex(r"\displaystyle \int_0^4 2\pi R(H_U-H_D)\,dy",).scale(0.8).next_to(eq1, RIGHT)
        rhs1b = MathTex(r"\displaystyle \int_0^4 2\pi x(H_U-H_D)\,dy",).scale(0.8).next_to(eq1, RIGHT)
        rhs1c = MathTex(r"\displaystyle \int_0^4 2\pi x\left(\sqrt{x}-\frac{x}{2} \right)\,dy",).scale(0.8).next_to(eq1, RIGHT)


        rhs2 = MathTex(r"2\pi \displaystyle \int_0^4  x^{\frac{3}{2}} -\frac{1}{2}x^2 \,dy",).scale(0.8).next_to(eq2, RIGHT)
        rhs3 = MathTex(r"2\pi \left( \frac{2}{5}x^{\frac{5}{2}}- \frac{1}{6} x^3  \mid_{x=0}^{x=4} \right)",).scale(0.8).next_to(eq3, RIGHT)

        rhs4 = MathTex(r"2\pi \left( \left( \frac{2}{5}4^{\frac{5}{2}}- \frac{1}{6} 4^3   \right) -0 \right)",).scale(0.8).next_to(eq4, RIGHT)
        rhs4a = MathTex(r" \frac{64}{15} \pi ",).scale(0.8).next_to(eq4, RIGHT)
        

        



        
        self.add(title1)
        #self.wait(5)
        #self.play(Wiggle(title1[1]), Wiggle(title1[2]))
        #self.play(Transform(title1, title1a))
        self.wait(3)
        self.play(Write(lhs1)), 
        self.wait(2)
        self.play(Write(eq1), Write(rhs1))
        self.wait(4)
        self.play(Transform(rhs1, rhs1a))
        self.wait(4)
        self.play(Transform(rhs1, rhs1b))
        self.wait(4) 
        self.play(Transform(rhs1, rhs1c))
        self.wait(5) 
        self.play(Write(eq2), Write(rhs2))
        self.wait(5)
        self.play(Write(eq3), Write(rhs3))
        self.wait(5)
        self.play(Write(eq4), Write(rhs4))
        self.wait(5)
        self.play(Transform(rhs4, rhs4a))
        self.wait(10) 


        self.play(
            FadeOut(rhs1,lhs1, eq1, eq2, rhs2, eq3, rhs3, eq4, rhs4))    




