from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
import kivy
from kivy.app import App
kivy.require('1.9.0')


Config.set('graphics', 'resizable', 1)


class CalcGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:

                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()


calcApp = CalculatorApp()
calcApp.run()
