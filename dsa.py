# import all the modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mp
import numpy as np
import random

# merge sort function to divide the array
def mergesort(A, start, end):
	if end <= start:
		return

	mid = start + ((end - start + 1) // 2) - 1

	# yield from statement is used to yield the array from the merge function
	yield from mergesort(A, start, mid)
	yield from mergesort(A, mid + 1, end)
	yield from merge(A, start, mid, end)

# function to merge the array in order to iterate it 
def merge(A, start, mid, end):
	merged = []
	leftIdx = start
	rightIdx = mid + 1

	while leftIdx <= mid and rightIdx <= end:
		if A[leftIdx] < A[rightIdx]:
			merged.append(A[leftIdx])
			leftIdx += 1
		else:
			merged.append(A[rightIdx])
			rightIdx += 1

	while leftIdx <= mid:
		merged.append(A[leftIdx])
		leftIdx += 1

	while rightIdx <= end:
		merged.append(A[rightIdx])
		rightIdx += 1

	for i in range(len(merged)):
		A[start + i] = merged[i]
		yield A

# function to plot bars
def showGraph():

	# for random unique values
	n = int(input("enter array size\n"))
	a = [i for i in range(1, n + 1)]
	random.shuffle(a)
	datasetName = 'Random'

	# generator object returned by the function
	generator = mergesort(a, 0, len(a)-1)
	algoName = 'Merge Sort'

	# style of the chart
	plt.style.use('fivethirtyeight')

	# set colors of the bars
	data_normalizer = mp.colors.Normalize()
	color_map = mp.colors.LinearSegmentedColormap(
		"my_map",
		{
			"red": [(0, 1.0, 1.0),
					(1.0, .5, .5)],
			"green": [(0, 0.5, 0.5),
					(1.0, 0, 0)],
			"blue": [(0, 0.50, 0.5),
					(1.0, 0, 0)]
		}
	)

	fig = plt.figure()
	ax = fig.add_subplot(projection = '3d')

	# z values and posistions of the bars
	z = np.zeros(n)
	dx = np.ones(n)
	dy = np.ones(n)
	dz = [i for i in range(len(a))]

	# Poly3dCollection returned into variable rects
	rects = ax.bar3d(range(len(a)), a, z, dx, dy, dz,
					color = color_map(data_normalizer(range(n))))

	# setting and x and y limits equal to the length of the array
	ax.set_xlim(0, len(a))
	ax.set_ylim(0, int(1.1 * len(a)))
	ax.set_title("ALGORITHM : " + algoName + "\n" + "DATA SET : " +
				datasetName, fontdict = {'fontsize' : 13,
										'fontweight' : 'medium',
										'color' : '#E4365D'})

	# text to plot on the chart
	text = ax.text2D(0.1, 0.95, "", horizontalalignment ='center',
					verticalalignment ='center',
					transform = ax.transAxes, color ="#E4365D")
	iteration = [0]

	# animation function to be repeatedly called
	def animate(A, rects, iteration):

		# to clear the bars from the Poly3DCollection object
		ax.collections.clear()
		ax.bar3d(range(len(a)), A, z, dx, dy, dz,
				color = color_map(data_normalizer(range(n))))
		iteration[0] += 1
		text.set_text("iterations : {}".format(iteration[0]))
			
	# animate function is called here and the generator object is passed
	anim = FuncAnimation(fig, func = animate,
		fargs =(rects, iteration), frames = generator, interval = 50,
		repeat = False)
	plt.show()

showGraph()
