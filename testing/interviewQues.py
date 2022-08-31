def BeautifulSequences(N):
    testingArr = [ 9, 19, 29, 39, 49, 59, 69, 79, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
                 109, 119, 129, 139, 149, 159, 169, 179, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 
                 209, 219, 229, 239, 249, 259, 269, 279, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299,
                 309, 319, 329, 339, 349, 359, 369, 379, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399,
                 409, 419, 429, 439, 449, 459, 469, 479, 489, 490 ]
    opVal = 0
    indexVal = 0 if N < 490 else None
    usingArr = []
    for i in testingArr:
        if i < N and testingArr[testingArr.index(i) + 1] > N:
            indexVal = testingArr.index(i)
            usingArr = testingArr[0:indexVal]

	x = '0' * indexVal
    temp = 0
    loopValue = pow(2, indexVal)
    
	for k in range(loopValue):
        x = string(bin(k))
        x = x[len(x)-indexVal:len(x)-1]
        y = 0
        for j in x:
        	if j == '1':
                temp += usingArr[y]
            y+=1
        if temp == N: opval += 1
        else: temp = 0
    return opVal


def main():
    N = int(raw_input().strip())

    result = BeautifulSequences(N)

    print(result)


if __name__ == "__main__":
    main()