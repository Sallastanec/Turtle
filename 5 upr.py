import turtle as t

b=25
t.shape('turtle')
for y in range(1, 11):
	t.penup()
	t.goto((b*-y),(b*-y))
	t.pendown()
	for i in range (4):
		t.forward(b*(y*2))
		t.left(90)