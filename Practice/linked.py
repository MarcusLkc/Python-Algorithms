class node(object):

	def __init__(self,data, next_node = None):
		self.data = data
		self.next_node = next_node

	def get_data(self):

		return self.data

	def get_next(self):

		return self.next_node

	def set_data(self,data):
		self.data = data

	def set_next(self,new_node):
		self.next_node = new_node

class LinkedList(object):

	def __init__(self,head=None):

		self.head = head
		self.size = 0

	def get_size(self):

		return self.size

	def add(self,data):

		new_node = node(data)
		new_node.set_next(self.head)
		self.head = new_node
		self.size += 1

	def search(self,data):

		current = self.head
		while current:
			if current.get_data() == data:
				print("Data Found")
				return data
			else:
				current = current.get_next()

		return None

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


		




















