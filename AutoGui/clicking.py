import pyautogui



x,y = pyautogui.position()
currentposition = pyautogui.position()
lastposition = pyautogui.position()
while True:
	currentposition = pyautogui.position()
	if currentposition != lastposition:

		x,y = pyautogui.position()
		print(currentposition)
		print(pyautogui.pixel(x,y))
		lastposition = currentposition

	


