import timeit
import random
import sys

sys.setrecursionlimit(999999)

origin_list = []
list_start = timeit.default_timer()
for i in range(10000000):
    n = random.randint(1, 9999999999)
    origin_list.append(n)
list_end = timeit.default_timer()
list_time = round((list_end - list_start),3)
print('List time : %s' % list_time) 
print('Length of the list: ', len(origin_list))

from collections import deque ############## 归并排序
merge_list = origin_list

def merge_sort(merge_list):
    if len(merge_list) <= 1:
        return merge_list

    def merge(left, right):
        merged,left,right = deque(),deque(left),deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(merge_list) // 2)
    left = merge_sort(merge_list[:middle])
    right = merge_sort(merge_list[middle:])
    return merge(left, right)

start_time = timeit.default_timer() 
merge_sort(merge_list)
end_time = timeit.default_timer()
elapse_time = end_time- start_time
print("Merge Sort:  %s second " % (round(elapse_time, 3)))


heap_list = origin_list ############## 堆排序

def heap_sort(heap_list) :
    n = len(heap_list)
    first = int(n/2-1)
    for start in range(first,-1,-1) :
        max_heapify(heap_list,start,n-1)
    for end in range(n-1,0,-1):
        heap_list[end],heap_list[0] = heap_list[0],heap_list[end]
        max_heapify(heap_list,0,end-1)
    return heap_list

def max_heapify(heap_list,start,end):
    root = start
    while True :
        child = root*2 +1
        if child > end : break
        if child+1 <= end and heap_list[child] < heap_list[child+1] :
            child = child+1
        if heap_list[root] < heap_list[child] :
            heap_list[root],heap_list[child] = heap_list[child],heap_list[root]
            root = child
        else :
            break
heap_start_time = timeit.default_timer() 
heap_sort(heap_list)
heap_end_time = timeit.default_timer()
heap_elapse_time = heap_end_time - heap_start_time
print("Heap Sort:  %s second " % (round(heap_elapse_time, 3)))



bubble_list = origin_list ############## 冒泡排序


def bubble_sort(bubble_list):
    n = len(bubble_list) 
    for i in range(n):
        for j in range(1,n-i):
            if  bubble_list[j-1] > bubble_list[j] :  
                bubble_list[j-1], bubble_list[j] = bubble_list[j], bubble_list[j-1]
    return bubble_list
bubble_start_time = timeit.default_timer()
#bubble_sort(bubble_list)
bubble_end_time = timeit.default_timer()
bubble_elapse_time = bubble_end_time - bubble_start_time
#print("Bubble Sort:  %s second " % (round(bubble_elapse_time, 3)))
print('Bubble Sort: Too slow.............Skip it!')



insert_list = origin_list  ############## 插入排序

def insert_sort(insert_list):
    n = len(insert_list)
    for i in range(1,n):
        if insert_list[i] < insert_list[i-1]:
            temp = insert_list[i]
            index = i
            for j in range(i-1,-1,-1):
                if insert_list[j] > temp :
                    insert_list[j+1] = insert_list[j]
                    index = j
                else :
                    break
            insert_list[index] = temp
    return insert_list
insert_start_time = timeit.default_timer()
insert_sort(insert_list)
insert_end_time = timeit.default_timer()
insert_elapse_time = insert_end_time - insert_start_time
print("Insert Sort:  %s second " % (round(insert_elapse_time, 3)))


list_ = origin_list  ############## 快速排序

quick_sort_list = origin_list
def quick_sort(quick_sort_list):
    if len(quick_sort_list) <= 1: return quick_sort_list
    return quick_sort([x for x in quick_sort_list if x < quick_sort_list[0]]) + [x for x in quick_sort_list if x == quick_sort_list[0]] + quick_sort([x for x in quick_sort_list if x > quick_sort_list[0]])

start = timeit.default_timer()
#quick_sort(quick_sort_list)
end = timeit.default_timer()

quick_sort_elapse_time = end - start
#print("Quick Sort:  %s second " % (round(quick_sort_elapse_time, 3)))


select_list = origin_list  ############## 选择排序

def select_sort(select_list):
    n = len(select_list)
    for i in range(0,n):
        min = i 
        for j in range(i+1,n):
            if select_list[j] < select_list[min] :
                min = j 
        select_list[min],select_list[i] = select_list[i],select_list[min] 
    return select_list
select_start_time = timeit.default_timer()
select_sort(select_list)
select_end_time = timeit.default_timer()
select_elapse_time = select_end_time - select_start_time
print("Selection Sort:  %s second " % (round(select_elapse_time, 3)))
#print('Selection Sort: Too slow.............Skip it!')


shell_list = origin_list  ############## 希尔排序

def shell_sort(shell_list):
    n = len(shell_list)
    gap = round(n/2) 
    while gap > 0 :
        for i in range(gap,n): 
            temp = shell_list[i]
            j = i
            while ( j >= gap and shell_list[j-gap] > temp ): 
                shell_list[j] = shell_list[j-gap]
                j = j - gap
            shell_list[j] = temp
        gap = round(gap/2) 
    return shell_list
shell_start_time = timeit.default_timer()
shell_sort(shell_list)
shell_end_time = timeit.default_timer()
shell_elapse_time = shell_end_time - shell_start_time
print("Shell Sort:  %s second " % (round(shell_elapse_time, 3)))


heap_list = origin_list ############## 堆排序

def heap_sort(heap_list):
    n = len(heap_list)
    first = int(n/2-1) 
    for start in range(first,-1,-1) : 
        max_heapify(heap_list,start,n-1)
    for end in range(n-1,0,-1): 
        heap_list[end],heap_list[0] = heap_list[0],heap_list[end]
        max_heapify(heap_list,0,end-1)
    return heap_list

def max_heapify(heap_list,start,end):
    root = start
    while True :
        child = root*2 +1
        if child > end : break
        if child+1 <= end and heap_list[child] < heap_list[child+1] :
            child = child+1 
        if heap_list[root] < heap_list[child] :   
            heap_list[root],heap_list[child] = heap_list[child],heap_list[root]
            root = child
        else :
            break
heap_start_time = timeit.default_timer()
heap_sort(heap_list)
heap_end_time = timeit.default_timer()
heap_elapse_time = timeit.default_timer() - heap_start_time
print("Heap Sort:  %s second " % (round(heap_elapse_time, 3)))