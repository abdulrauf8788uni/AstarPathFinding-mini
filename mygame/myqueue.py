class myPriorityQueue():

    def __init__(self):
        self.queue = []

    def insert(self, value, priority):
        item = (value, priority) 
        self.queue.append(item)

    def get(self):
        item = self.get_least()
        if item[0]:
            self.queue.remove(item)
        return item

    def get_highest_priority(self):
        item = self.get_heighest()
        return item[0]

    def delete_highest_priority(self):
        item = self.get_heighest()
        if item[0]:
            self.queue.remove(item)

    # helper functions

    def get_least(self):
        if not self.is_empty():
            min_val = float("inf")
            min_item = None

            for val, prior in self.queue:
                if prior < min_val:
                    min_val = prior

            for item in self.queue:
                if item[1] == min_val:
                    return item
        else:
            return None, None

    def get_heighest(self):
        if not self.is_empty():
            max_val = 0
            max_item = None
            for val, prior in self.queue:
                if prior > max_val:
                    max_val = prior

            # return the latest item (item recently inserted), in case of same priority. 
            # for item in self.queue:
            #     if item[1] == max_val:
            #         max_item = item 
            # return max_item 

            # returns the item which was added first (in case of same proirity).  
            for item in self.queue:
                if item[1] == max_val:
                    return item
        else:
            return None, None
      

    def is_empty(self):
        return len(self.queue) == 0



if __name__ == "__main__":
    q = myPriorityQueue()
    q.insert("Apple", 4)
    q.insert("Mango", 4)
    q.insert("grapes", 3)
    q.insert("banana", 5)
    print(q.get())
    print(q.get())
    print(q.get())
