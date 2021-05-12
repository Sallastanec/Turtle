def spider (n):
	"""Функция рисует паука. n - число лап. """
	import turtle as t
	long = 100
	t.shape('turtle')
	for i in range(0, n):
		t.right(360/n)
		t.forward(long)
		t.stamp()
		t.left(180)
		t.forward(long)
		t.left(180)

spider (12)
