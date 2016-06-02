LED_MAX = 100
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3
 
import wiringpi

class LEDBorg:

	color = (0, 0, 0)

	def __init(self):
		self.gpio = wiringpi.wiringPiSetup()		
		wiringpi.softPwmCreate(PIN_RED,   0, LED_MAX)
		wiringpi.softPwmCreate(PIN_GREEN, 0, LED_MAX)
		wiringpi.softPwmCreate(PIN_BLUE,  0, LED_MAX)
		self.off()

	def _set_color(self, color):
		self.color = color
		wiringpi.softPwmWrite(PIN_RED,   color[0])
		wiringpi.softPwmWrite(PIN_GREEN, color[1])
		wiringpi.softPwmWrite(PIN_BLUE,  color[2])

	def on(self):	
		self._set_color((0, 0, 0))

	def off(self):
		self._set_color((0, 0, 0))
		
