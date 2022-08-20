from manim import *

class Intro(Scene):
    def construct(self):
        titulo = Text("A fórmula de Bhaskara", font="OpenDyslexic")
        equacao = MathTex(r"ax^2 + bx + c = 0 \iff x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}")
        VGroup(titulo, equacao).arrange(DOWN)
        self.play(Write(titulo), run_time=2)
        self.play(FadeIn(equacao, shift=DOWN))
        self.wait()

class Transformacoes(Scene):
    def construct(self):
        textoa = Text("uma coisa")
        textob = Text("outra coisa")

        eqa = MathTex(r'(a + b)(c + d)')
        eqb = MathTex(r'ac + bd + bc + bd')

        self.play(Write(textoa), run_time = 2)
        self.play(Transform(textoa, textob))
        self.wait()
        self.play(FadeOut(textoa), LaggedStart(FadeIn(eqa)))
        self.wait()
        self.play(Transform(eqa, eqb))
        self.wait(3)