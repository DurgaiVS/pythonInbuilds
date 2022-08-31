import memory_profiler
import time
print(f'Memory used bef: {memory_profiler.memory_usage()}')
# nums = [1, 2, 3]
#
# print(dir(nums))
#
# # We are making a list into an iterable
# i_nums = iter(nums)
#
# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break

time.sleep(1)


class MyRange:
    def __init__(self, start, end = float('inf')):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        else:
            curr = self.value
            self.value += 1
            return curr


my_range = MyRange(10)
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))

print(f'Memory used af: {memory_profiler.memory_usage()}')
