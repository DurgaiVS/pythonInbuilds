x = 123
if type(x) == int:
    # print(x)
    pass
arr = [1,1,3,1]
def fn(arr):
    if arr[0] == arr[1]:
        # print('yews')
        for i in arr:
            if i != arr[0]:
                return i
    elif arr[1] == arr[2]: 
        return arr[0]
    else: return arr[1]
# print(fn(arr))

# i = input('Enter: ')
# print("".join(sorted(i, reverse=True)))
# y.sort(reverse=True)
# print(y, 'y')
# z = ''
# for i in y:
    # z += i
# print(int(z), 'z')

def get_count(sentence):
    return sum(1 for i in sentence if i in 'aeiouAEIOU')
print(get_count('aeiouaeiouaeiouAEIOUAEIOU'))

op = ''
s = 'abcde'
# for i in range(len(s)):
#     if len(op) != 0: op = op + '-' 
#     op = op + (s[i] * (i+1) ).capitalize()
# print(op) 
# print('-'.join(a.upper() + a.lower() * i for i,a in enumerate(s)))

sentence = 'Heyey'
arr = sentence.split(" ")
rra = [a[::-1] if len(a) >= 5 else a for a in arr]
print(" ".join(rra))