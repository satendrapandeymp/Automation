import keyboard, time, easygui

flag = 0

def mouse():
	while True:

		time.sleep(1)

		if keyboard.is_pressed('select'):

			if flag  == 0:
				flag = 1
				keyboard.press('shift')
				easygui.msgbox('shift has been pressed', title="alert")
			
			else:
				flag = 0
				keyboard.release('shift')
				easygui.msgbox('shift has been released', title="alert")
