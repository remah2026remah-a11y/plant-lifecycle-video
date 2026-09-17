from manim import *

BG = "#071A2B"
SOIL = "#6B4423"
GREEN = "#4ADE80"
YELLOW = "#FACC15"
BLUE = "#60A5FA"
PINK = "#F472B6"
WHITE = "#F8FAFC"


def title(text):
    return Text(text, font_size=40, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)


def soil_patch():
    return Rectangle(width=13.2, height=2.15, fill_color=SOIL, fill_opacity=1, stroke_width=0).to_edge(DOWN, buff=0)


def seed(scale=1.0):
    return Ellipse(width=0.7 * scale, height=0.95 * scale, color=YELLOW, fill_color="#B7791F", fill_opacity=1, stroke_width=3)


class SeedStage(Scene):
    # Target: 21.44s (from scene1.wav)
    def construct(self):
        self.camera.background_color = BG
        head = title("١. البذرة: بداية الحياة")
        ground = soil_patch()
        s = seed().move_to(DOWN * 1.65)
        water = VGroup(*[Ellipse(width=0.18, height=0.35, color=BLUE, fill_color=BLUE, fill_opacity=0.8).rotate(-20).move_to(p) for p in [LEFT * 2.2 + UP * 2.2, LEFT * 1.7 + UP * 2.55, LEFT * 1.2 + UP * 2.15]])
        sun = VGroup(Circle(radius=0.42, color=YELLOW, fill_color=YELLOW, fill_opacity=1), *[Line(UP * 0.62, UP * 0.88, color=YELLOW).rotate(a) for a in np.arange(0, TAU, PI / 4)]).move_to(RIGHT * 4.9 + UP * 2.5)
        label = Text("ماء + هواء + دفء", font_size=28, color=BLUE).next_to(sun, DOWN, buff=0.35)
        question = Text("هل تبدأ الرحلة؟", font_size=30, color=YELLOW).next_to(s, UP, buff=0.55)
        self.play(FadeIn(head), FadeIn(ground), FadeIn(s), run_time=2.0)
        self.play(FadeIn(sun), FadeIn(water), FadeIn(label), run_time=3.0)
        self.play(Write(question), run_time=2.0)
        self.wait(3.0)
        self.play(Indicate(s, color=YELLOW), run_time=2.0)
        self.play(question.animate.set_color(GREEN), run_time=1.5)
        self.wait(3.0)
        self.play(FadeOut(question), FadeOut(label), run_time=1.5)
        self.play(s.animate.scale(1.15), run_time=1.5)
        self.wait(2.0)


class GerminationStage(Scene):
    # Target: 18.96s (from scene2.wav)
    def construct(self):
        self.camera.background_color = BG
        head = title("٢. الإنبات: إلى الأسفل وإلى الأعلى")
        ground = soil_patch()
        boundary = Line(LEFT * 6.5 + DOWN * 0.55, RIGHT * 6.5 + DOWN * 0.55, color="#D6A15D", stroke_width=3)
        s = seed().move_to(DOWN * 0.95)
        root = VGroup(Line(DOWN * 1.15, DOWN * 2.35, color=WHITE, stroke_width=8), Line(DOWN * 1.75, DOWN * 2.15 + LEFT * 0.35, color=WHITE, stroke_width=4), Line(DOWN * 1.85, DOWN * 2.2 + RIGHT * 0.35, color=WHITE, stroke_width=4)).move_to(DOWN * 0.2)
        stem = Line(UP * 0.15, UP * 1.75, color=GREEN, stroke_width=9).move_to(UP * 0.65)
        bud = Dot(UP * 1.6, radius=0.18, color=GREEN)
        down_label = Text("الجذر يمتص الماء", font_size=27, color=BLUE).to_edge(LEFT, buff=0.5).shift(DOWN * 2.7)
        up_label = Text("الساق نحو الضوء", font_size=27, color=GREEN).to_edge(RIGHT, buff=0.5).shift(UP * 1.8)
        self.play(FadeIn(head), FadeIn(ground), Create(boundary), FadeIn(s), run_time=2.0)
        self.play(GrowFromPoint(root, s.get_center()), run_time=4.0)
        self.play(Write(down_label), run_time=2.0)
        self.play(GrowFromPoint(stem, s.get_center()), FadeIn(bud), run_time=4.0)
        self.play(Write(up_label), run_time=2.0)
        self.wait(2.0)
        self.play(Indicate(root, color=BLUE), Indicate(stem, color=GREEN), run_time=1.96)
        self.wait(1.0)


class GrowthStage(Scene):
    # Target: 24.84s (from scene3.wav)
    def construct(self):
        self.camera.background_color = BG
        head = title("٣. النمو: النبات يصنع غذاءه")
        ground = soil_patch()
        stem = Line(DOWN * 1.4, UP * 1.35, color=GREEN, stroke_width=10)
        stem.shift(DOWN * 0.15)
        leaves = VGroup(Ellipse(width=1.55, height=0.58, color=GREEN, fill_color=GREEN, fill_opacity=1).rotate(25).move_to(LEFT * 0.75 + UP * 0.5), Ellipse(width=1.55, height=0.58, color=GREEN, fill_color=GREEN, fill_opacity=1).rotate(-25).move_to(RIGHT * 0.75 + UP * 0.95), Ellipse(width=1.3, height=0.52, color=GREEN, fill_color=GREEN, fill_opacity=1).rotate(18).move_to(LEFT * 0.6 + UP * 1.45))
        root = Line(DOWN * 1.35, DOWN * 2.45, color=WHITE, stroke_width=6)
        plant = VGroup(stem, leaves, root)
        sun = Circle(radius=0.48, color=YELLOW, fill_color=YELLOW, fill_opacity=1).to_corner(UR, buff=1.0)
        rays = VGroup(*[Line(UP * 0.7, UP * 1.0, color=YELLOW).rotate(a) for a in np.arange(0, TAU, PI / 4)]).move_to(sun)
        co2 = Text("CO₂", font_size=28, color=BLUE).move_to(LEFT * 4.1 + UP * 1.25)
        water = Text("H₂O", font_size=28, color=BLUE).move_to(LEFT * 4.1 + DOWN * 1.65)
        food = Text("غذاء", font_size=32, color=YELLOW).move_to(RIGHT * 3.7 + DOWN * 0.5)
        arrow1 = Arrow(co2.get_right(), plant.get_left() + UP * 0.8, color=BLUE)
        arrow2 = Arrow(water.get_right(), plant.get_left() + DOWN * 0.7, color=BLUE)
        arrow3 = Arrow(plant.get_right() + UP * 0.6, food.get_left(), color=YELLOW)
        caption = Text("البناء الضوئي", font_size=30, color=WHITE).next_to(food, DOWN, buff=0.4)
        self.play(FadeIn(head), FadeIn(ground), run_time=2.0)
        self.play(GrowFromCenter(plant), run_time=4.0)
        self.play(FadeIn(sun), Create(rays), run_time=2.5)
        self.play(FadeIn(co2), FadeIn(water), Create(arrow1), Create(arrow2), run_time=3.5)
        self.play(FadeIn(food), Create(arrow3), run_time=3.0)
        self.play(Write(caption), run_time=2.0)
        self.wait(3.0)
        self.play(Indicate(leaves, color=GREEN), Indicate(food, color=YELLOW), run_time=2.0)
        self.wait(2.84)


class FlowerCycleStage(Scene):
    # Target: 28.04s (from scene4.wav)
    def construct(self):
        self.camera.background_color = BG
        head = title("٤. الإزهار: بذور جديدة ودورة مستمرة")
        ground = soil_patch()
        stem = Line(DOWN * 1.3, UP * 1.6, color=GREEN, stroke_width=9)
        leaves = VGroup(Ellipse(width=1.4, height=0.55, color=GREEN, fill_color=GREEN, fill_opacity=1).rotate(25).move_to(LEFT * 0.8 + UP * 0.45), Ellipse(width=1.4, height=0.55, color=GREEN, fill_color=GREEN, fill_opacity=1).rotate(-25).move_to(RIGHT * 0.8 + UP * 0.9))
        flower_center = Circle(radius=0.25, color=YELLOW, fill_color=YELLOW, fill_opacity=1).move_to(UP * 1.7)
        petals = VGroup(*[Ellipse(width=0.48, height=0.85, color=PINK, fill_color=PINK, fill_opacity=1).move_to(UP * 2.25).rotate(a) for a in np.arange(0, TAU, TAU / 5)])
        plant = VGroup(stem, leaves, flower_center, petals)
        pollen = VGroup(*[Dot(LEFT * 2.0 + UP * (1.7 + i * 0.22), radius=0.09, color=YELLOW) for i in range(4)])
        fruit = Circle(radius=0.5, color=PINK, fill_color=PINK, fill_opacity=1).move_to(RIGHT * 3.0 + UP * 0.3)
        seeds = VGroup(*[seed(0.45).move_to(RIGHT * 3.0 + DOWN * 0.25 + RIGHT * (i - 1) * 0.35) for i in range(3)])
        cycle = Arc(radius=1.1, start_angle=0.2, angle=TAU - 0.5, color=YELLOW, stroke_width=5).move_to(RIGHT * 4.3 + DOWN * 1.65)
        cycle_arrow = Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1).scale(0.12).rotate(-0.7).move_to(cycle.point_from_proportion(0.98))
        cycle_label = Text("دورة مستمرة", font_size=25, color=YELLOW).next_to(cycle, DOWN, buff=0.2)
        self.play(FadeIn(head), FadeIn(ground), run_time=2.0)
        self.play(GrowFromCenter(plant), run_time=4.0)
        self.play(LaggedStart(*[FadeIn(p) for p in pollen], lag_ratio=0.25), run_time=2.5)
        self.play(pollen.animate.move_to(flower_center.get_center()), run_time=3.0)
        self.play(FadeIn(fruit), run_time=2.5)
        self.play(FadeIn(seeds), run_time=2.5)
        self.play(Create(cycle), FadeIn(cycle_arrow), Write(cycle_label), run_time=3.5)
        self.play(Indicate(seeds, color=YELLOW), run_time=2.0)
        self.wait(5.94)


# Scenes are rendered individually by the Manim CLI.
