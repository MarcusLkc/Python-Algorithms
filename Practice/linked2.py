class Node(object):

	def __init__(self,data):

		self.data = data
		self.next_node = None

	def get_data(self):

		return self.data

	def set_data(self):

		self.data = data

	def get_next(self):

		return self.next_node

	def set_next(self,new_next):

		self.next_node = new_next


class LinkedList(object):

	def __init__(self,head = None):

		self.head = head
		self.size = size

	def get_size(self):

		return self.size

	def find(self,data):

		current = self.head

		while current:
			if current.get_data() == data:
				print("Data was found")
				return data
			else:
				current = current.get_next()

		return False

	def add(self,data):

		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
		self.size += 1

	def remove(self,data):

		current = self.head
		previous = None

		while current:
			if current.get_data() == data:
				if previous:
					previous.set_next(current.get_next())
				else:
					self.root = current.get_next()
					self.size -= 1

				return True
			else:
				previous = current
				current = current.get_next()
		return False







