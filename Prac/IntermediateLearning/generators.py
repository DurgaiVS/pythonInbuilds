# Generators can be very useful, as it only consumes less memory
# than the normal or actual method. So it can be used for performance
# optimization. This works same as the queue.

# The best use case for generators is that when you create a password
# cracker with a set of characters and create random characters.
# You don't have to store values on the memory, it is highly
# volatile and fast.

import memory_profiler
from queue import Queue

print(f'memory usage before is {memory_profiler.memory_usage()}')


def sq_num(nums):
    res = []
    for i in range(nums):
        res.append(i * i)
    return res


def sq_num_q(nums):
    q = Queue()
    for i in range(nums):
        q.put(i * i)
    return q


def sq_num_generators(nums):
    for i in range(nums):
        yield i*i


def sq_gene_creator(start, end = float('inf')):
    curr = start
    while curr <= end:
        yield curr * curr
        curr += 1


my_sq_gen = sq_num_generators(1000000)
# for num in my_sq_gen:
#    print(num)
# or
# print(list(my_sq_gen))

my_sq_gen_comp = (i * i for i in range(1000000))
# for num in my_sq_gen_comp:
#     print(num)
# or
# print(list(my_sq_gen_comp))

my_sq_gen_creator = sq_gene_creator(1)

print(f'memory usage after generator is {memory_profiler.memory_usage()}')

my_sq_q = sq_num_q(1000000)

print(f'memory usage after q is {memory_profiler.memory_usage()}')


my_sq = sq_num(1000000)

my_sq_comprehension = [i * i for i in range(1000000)]

print(f'memory usage after normal method is {memory_profiler.memory_usage()}')
