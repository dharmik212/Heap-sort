import math
class MaxHeap:

    def __init__(self):
        self.Arr = []

    def parent(self,i):
        return (i-1) // 2

    def leftChild(self,i):
        return 2*i+1
    def rightChild(self,i):
        return 2*i+2

    def maxHeapify(self,i):
        largest = i
        left = self.leftChild(i)
        right = self.rightChild(i)

        # Compare with left child
        if left < len(self.Arr) and self.Arr[largest] < self.Arr[left]:
            largest = left
        # Compare with right child
        if right < len(self.Arr) and self.Arr[largest] < self.Arr[right]:
            largest = right

        # Change parent
        if largest != i:
            self.Arr[i], self.Arr[largest] = self.Arr[largest], self.Arr[i]
            # Recursive call
            self.maxHeapify(largest)

    def insert(self,rating):
        self.Arr.append(rating)
        i = len(self.Arr)-1
        while i>0 and self.Arr[i] > self.Arr[self.parent(i)]:
            self.Arr[i], self.Arr[self.parent(i)] = self.Arr[self.parent(i)],self.Arr[i]
            i = self.parent(i)

    # print nodes from top to down, left to right
   # def Print(self):

    # constructe a max heap from array
    def maxHeap(self,unsortArr):
        n = len(unsortArr)
        maxHeap = MaxHeap()
        for i in range(n):
            maxHeap.insert(unsortArr[i])
        return maxHeap

    def remove(self):
        if self.Arr == []:
            return None
        n = len(self.Arr)
        removed_element = self.Arr[0]
        self.Arr[0], self.Arr[n - 1] = self.Arr[n - 1], self.Arr[0]
        del self.Arr[n - 1]
        self.maxHeapify(0)
        return removed_element

#######################
def merge_sort(ratings):
    if len(ratings) <= 1:
        return ratings

    mid = len(ratings) // 2
    left = ratings[:mid]
    right = ratings[mid:]

    merge_sort(left)
    merge_sort(right)

def sort_movies_batch(names,ratings):
    n = len(ratings)
    rating_batch = ratings.copy()
    max_heap = MaxHeap()  # Create an instance of MaxHeap
    heap = max_heap.maxHeap(rating_batch)  # Call maxHeap method on the instance
    sorted_names_batch = []
    for i in range(n):
        maxValue = heap.remove()
        index = rating_batch.index(maxValue)
        sorted_names_batch.append(names[index])
        rating_batch[index] = -1
    return sorted_names_batch

def sort_movie_incre(names,ratings):
    n = len(ratings)
    ratings_incre = ratings.copy()
    heap = MaxHeap()
    sorted_names_incre = []
    for i in range(n):
        heap.insert(ratings_incre[i])
    for i in range(n):
        maxValue = heap.remove()
        index = ratings_incre.index(maxValue)
        sorted_names_incre.append(names[index])
        ratings_incre[index] = -1
    return sorted_names_incre