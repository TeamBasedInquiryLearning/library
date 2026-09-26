#%%manim -ql LIPoly

from manim import *







class EstimateLimit(Scene):
    def construct(self):
     #3d stuff

        
        title1 = MathTex(r"\text{Estimate  }\displaystyle \lim_{x\to 5} \frac{x^2+x-30}{x^2+10x-75}\text{ numerically.}", color=TEAL).scale(0.8)        
        title1.to_edge(UP)

        table1 = MathTex(r"\begin{array}{c|ccccccc}x & 4.9 & 4.99 & 4.999 & 5 & 5.001 & 5.01 & 5.01 \\ \hline f(x) &&&&&&& \end{array}").scale(0.8) 


        text1 = MathTex(r"f(x)=\frac{x^2+x-30}{x^2+10x-75}.", color=YELLOW).scale(0.8).shift(DOWN*1.5)

        text2 = MathTex(r"f(5)=?\frac{5^2+5-30}{5^2+10(5)-75}",r"=?\frac{0}{0}", r"\text{ is undefined.}", color=YELLOW).scale(0.8).shift(DOWN*1.5)        
        text2[2].set_color(RED)

        table2 = MathTex(r"\begin{array}{c|ccccccc}x & 4.9 & 4.99 & 4.999 & 5 & 5.001 & 5.01 & 5.1 \\ \hline f(x) &&&& \text{UND} &&& \end{array}").scale(0.8) 

        text3 = MathTex(r"f(4.9)=\frac{(4.9)^2+4.9-30}{(4.9)^2+10(4.9)-75}",r"\approx 0.5477", color=YELLOW).scale(0.8).shift(DOWN*1.5)
        table3 = MathTex(r"\begin{array}{c|ccccccc}x & 4.9 & 4.99 & 4.999 & 5 & 5.001 & 5.01 & 5.1 \\ \hline f(x) & 0.5477&&& \text{UND} &&& \end{array}").scale(0.8) 

        text4 = MathTex(r"f(4.99)=\frac{(4.99)^2+4.99-30}{(4.99)^2+10(4.99)-75}",r"\approx 0.5498", color=YELLOW).scale(0.8).shift(DOWN*1.5)
        table4 = MathTex(r"\begin{array}{c|ccccccc}x & 4.9 & 4.99 & 4.999 & 5 & 5.001 & 5.01 & 5.1 \\ \hline f(x) & 0.5477& 0.5498 && \text{UND} &&& \end{array}").scale(0.8)  

        text5 = MathTex(r"f(4.999)=\frac{(4.999)^2+4.999-30}{(4.999)^2+10(4.999)-75}",r"\approx 0.54998", color=YELLOW).scale(0.8).shift(DOWN*1.5)
        table5 = MathTex(r"\begin{array}{c|ccccccc}x & 4.9 & 4.99 & 4.999 & 5 & 5.001 & 5.01 & 5.1 \\ \hline f(x) & 0.5477& 0.5498 &0.54998& \text{UND} &&& \end{array}").scale(0.8)  

        text6 = MathTex(r"f(5.1)=\frac{(5.1)^2+5.1-30}{(5.1)^2+10(5.1)-75}",r"\approx 0.5522", color=YELLOW).scale(0.8).shift(DOWN*1.5)
        table6 = MathTex(r"\begin{array}{c|ccccccc}x & 4.9 & 4.99 & 4.999 & 5 & 5.001 & 5.01 & 5.1 \\ \hline f(x) & 0.5477& 0.5498 &0.54998& \text{UND} &&& 0.5522\end{array}").scale(0.8)  

        text7 = MathTex(r"f(5.01)=\frac{(5.01)^2+5.01-30}{(5.01)^2+10(5.01)-75}",r"\approx 0.5502", color=YELLOW).scale(0.8).shift(DOWN*1.5)
        table7 = MathTex(r"\begin{array}{c|ccccccc}x & 4.9 & 4.99 & 4.999 & 5 & 5.001 & 5.01 & 5.1 \\ \hline f(x) & 0.5477& 0.5498 &0.54998& \text{UND} &&0.5502& 0.5522\end{array}").scale(0.8)         

        text8 = MathTex(r"f(5.001)=\frac{(5.001)^2+5.001-30}{(5.001)^2+10(5.001)-75}",r"\approx 0.55002", color=YELLOW).scale(0.8).shift(DOWN*1.5)
        table8 = MathTex(r"\begin{array}{c|ccccccc}x & 4.9 & 4.99 & 4.999 & 5 & 5.001 & 5.01 & 5.1 \\ \hline f(x) & 0.5477& 0.5498 &0.54998& \text{UND} &0.55002&0.5502& 0.5522\end{array}").scale(0.8)         

        text9 = MathTex(r"\lim_{x\to 5} \frac{x^2+x-30}{x^2+10x-75}", r"\approx" , r"0.55" ,color=YELLOW).scale(0.8).shift(DOWN*1.5)
        text9[2].set_color(BLUE)
        

        



        



        #self.add_fixed_in_frame_mobjects(title)
        self.add(title1)
        self.wait(8)
        self.play(Write(table1))
        self.play(Write(text1))
        self.wait(5)
        self.play(FadeOut(text1), Write(text2[0]))
        self.wait(1)
        self.play(Write(text2[1]))
        self.wait(1)
        self.play(Write(text2[2]))
        self.play(Transform(table1, table2))
        self.wait(5)
        self.play(FadeOut(text2), Write(text3[0]))
        self.wait(1)
        self.play(Write(text3[1]))
        self.wait(1)
        self.play(Transform(table1, table3))
        self.wait(5)
        self.play(FadeOut(text3), Write(text4[0]))
        self.wait(1)
        self.play(Write(text4[1]))
        self.wait(1)
        self.play(Transform(table1, table4))
        self.wait(5)
        self.play(FadeOut(text4), Write(text5[0]))
        self.wait(1)
        self.play(Write(text5[1]))
        self.wait(1)
        self.play(Transform(table1, table5))
        self.wait(5)
        self.play(FadeOut(text5), Write(text6[0]))
        self.wait(1)
        self.play(Write(text6[1]))
        self.wait(1)
        self.play(Transform(table1, table6))
        self.wait(5)
        self.play(FadeOut(text6), Write(text7[0]))
        self.wait(1)
        self.play(Write(text7[1]))
        self.wait(1)
        self.play(Transform(table1, table7))
        self.wait(5)
        self.play(FadeOut(text7), Write(text8[0]))
        self.wait(1)
        self.play(Write(text8[1]))
        self.wait(1)
        self.play(Transform(table1, table8))
        self.wait(5)
        self.play(FadeOut(text8), Write(text9[0]))
        self.wait(1)
        self.play(Write(text9[1]))
        self.play(Write(text9[2]))
        


        self.wait(10)


        
        



        


        
        



        



  
       