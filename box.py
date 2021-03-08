import pygame
import random
import copy
import time

def insertion_sort(array):
	for j in range(1,len(array)):
		key = array.boxes[j].value
		i = j - 1
		while i >= 0 and key < array.boxes[i].value:
			array.boxes[i+1].value = array.boxes[i].value
			i -= 1
		array.boxes[i +1].value = key
		time.sleep(1)
	# return array	

pygame.init()
pygame.display.init()
pygame.font.init()
display = pygame.display.set_mode((700,600))
font = pygame.font.Font('freesansbold.ttf',22)
BLACK = (0, 0, 0)
def drawrect(box):
	pygame.draw.rect(display,BLACK, (box.x,box.y,box.LENGTH,box.HEIGHT))
	pygame.draw.rect(display,box.color, (box.x,box.y,box.LENGTH-1,box.HEIGHT-1))
	textobj = font.render(str(box.value),True,(0,0,0))
	textsurfobj = textobj.get_rect()
	textsurfobj.center = (box.x + 25 ,box.y + 25)
	display.blit(textobj, textsurfobj)
	# pygame.display.update()


class box:
	LENGTH = 50
	HEIGHT = 50
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	not_overlapping = []
	"""a class for displayed boxes"""
	def __init__(self,value,x,y,is_sorted = 1):
		self.x = x
		self.y = y
		self.value = value 
		self.__length = box.LENGTH
		self.__height = box.HEIGHT
		if is_sorted:
			self.color = box.GREEN
		else:
			self.color = box.RED

	def getval(self):
		return self.value

	def setval(self, val):
		self.value = val

	def change_color(self):
		if self.color == box.RED:
			self.color = box.GREEN
		else:
			self.color = box.RED


class BoxArray:
	def __init__(self, num , is_sorted, pos_x, pos_y):
		self.num = num
		self.is_sorted = is_sorted
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.boxes = []
		for i in range(num):
			self.boxes.append(box(random.randrange(11),(pos_x + i * box.LENGTH),pos_y ))
		self.begin = self.boxes[0]
		self.end = self.boxes[-1]
	
	def __len__(self):
		return len(self.boxes)


	def swap_by_index(self, a, b):
		temp = copy.deepcopy(self.boxes[a])
		self.boxes[a] = self.boxes[b]
		self.boxes[b] = temp



	def draw(self, display):
		for i in range(1,len(self.boxes)):
			if self.boxes[i].value < self.boxes[i-1].value:
				self.boxes[i].is_sorted = False
				self.boxes[i].color = box.RED
			else :
				self.boxes[i].is_sorted = True
				self.boxes[i].color = box.GREEN
		for i in self.boxes:
			drawrect(i)

	def insert_box(self, box):
		box.x = self.end.x + box.LENGTH
		box.y = self.end.y
		self.boxes.append(box)
		self.end = box




def main():
	pygame.init()
	pygame.display.set_caption("insertion sort visualization")

	boxarr = BoxArray(2, True, 60,70)
	boxarr2 = BoxArray(2, True, 60,140)
	boxarr3 = BoxArray(2, True, 60,210)
	boxarr4 = BoxArray(2, True, 60,280)
	boxarr5 = BoxArray(2, True, 60,350)
	boxarr6 = BoxArray(2, True, 60,420)

	# b1 = box(6 , 250 ,250)

	# boxarr.insert_box(copy.deepcopy(b1))
	# boxarr2.insert_box(b1)

	loop = True
	while loop:
		boxarr.draw(display)
		boxarr2.draw(display)
		boxarr3.draw(display)
		boxarr4.draw(display)
		boxarr5.draw(display)
		boxarr6.draw(display)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				print(len(boxarr2.boxes))
				# insertion_sort(boxarr)
				if len(boxarr.boxes) > 11:
					insertion_sort(boxarr)
					insertion_sort(boxarr2)
					insertion_sort(boxarr3)
					insertion_sort(boxarr4)
					insertion_sort(boxarr5)
					insertion_sort(boxarr6)
					# insertion_sort(boxarr)
					continue
				else:
					boxarr2.insert_box(box(random.randint(0,10),0,0))
					boxarr.insert_box(box(random.randint(1,10),0,0))
					boxarr3.insert_box(box(random.randint(0,10),0,0))
					boxarr4.insert_box(box(random.randint(1,10),0,0))
					boxarr5.insert_box(box(random.randint(0,10),0,0))
					boxarr6.insert_box(box(random.randint(1,10),0,0))
					pygame.event.clear()
					# boxarr.swap_by_index(2,5)
					# boxarr2.swap_by_index(1,4)
					# boxarr2.swap_by_index(3,7)
		pygame.display.flip()


main()
