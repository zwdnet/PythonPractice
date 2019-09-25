# coding:utf-8
# 第10课 简约不简单的匿名函数 tkinter

from tkinter import Button, mainloop

button = Button(
	text = "This is a button",
	command = lambda : print("being pressed")
)
button.pack()
mainloop()