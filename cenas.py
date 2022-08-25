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

class GeometriaPlana(Scene):
    def construct(self):
        #Apresentação de um exercício da UFPE
        texto_superior = VGroup(
            Tex(r'A figura abaixo ilustra uma região triangular $ABC$. O lado $AB$'),
            Tex(r'foi dividido em quatro segmentos de mesma medida, um dos'),
            Tex(r'quais sendo $DE$, e o lado $BC$ foi dividido em cinco segmentos'),
            Tex(r'de mesma medida, sendo $F$ um dos pontos da divisão.')
        ).arrange(DOWN, aligned_edge=LEFT)

        #triangulos
        vertices = [
            [0, 2.5, 0], # A
            [-2, 0, 0], #B
            [3, 0, 0] #C
        ]
        v_sup = [v for v in vertices]

        pointsAB = [
            # A + AB*n/4 com n de 1 a 3
            [vertices[0][0] + (vertices[1][0] - vertices[0][0])*n/4,
            vertices[0][1] + (vertices[1][1] - vertices[0][1])*n/4,
            0] for n in range(1, 4)
        ]
        pointsBC = [
            # B + BC*n/4 com n de 1 a 4
            [vertices[1][0] + (vertices[2][0] - vertices[1][0])*n/5,
            vertices[1][1] + (vertices[2][1] - vertices[1][1])*n/5,
            0] for n in range(1, 5)
        ]

        v_inf = [pointsAB[1], pointsAB[2], pointsBC[2]]
        
        triangulo_maior = Polygon(*v_sup).set_color(PINK)
        triangulo_menor = Polygon(*v_inf).set_fill(BLUE_A, opacity=.3)

        conj_tri = VGroup(
            triangulo_maior,
            *[Circle(radius=.05).move_to(p) for p in pointsAB], # "pontos" subdividindo os lados desejados
            *[Circle(radius=.05).move_to(p) for p in pointsBC], # "pontos" subdividindo os lados desejados
            triangulo_menor
        ).scale(1.5).align_on_border(DOWN)

        texto_inferior = Tex(r'Qual é a razão entre as áreas do triângulo $ABC$ e do triângulo $DEF$?')
        self.play(Write(texto_superior, rate_functions.ease_in_out_sine), run_time = 7)
        self.play(texto_superior.animate().align_on_border(UP))
        
        self.play(Create(conj_tri), run_time=3, rate_func = rate_functions.ease_out_quint)

        self.wait(3)