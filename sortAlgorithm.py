import time # 시간 측정하기 위함
import sys # recursion limit 방지하기 위함

N100 = [i for i in range(100,0,-1)] # 100 99 98 ... 1
N1000 = [i for i in range(1000,0,-1)] # 1000 999 998 ... 1
N10000 = [i for i in range(10000,0,-1)] # 10000 9999 9998 ... 1
exTime = [] # 실행시간 저장 배열

# bubble sort
def bubbleSort(arr, n): # arr은 입력 배열, n은 배열의 크기(element 수)
    for i in range(n-1): # n(element 수)-1 만큼의 pass (1번째 pass ~ n-1번째 pass)
        for j in range(n-1-i): # i번째 pass에서는 (n-1)번 만큼 sorting
            if arr[j] > arr[j+1]: # 오름차순이므로 arr[j] > arr[j+1] 이면 서로 swap
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap
    
    return arr # bubble sort한 배열 arr 반환

# print(N100, end="\n\n")
# print("bubble sort: ")
# print(bubbleSort(N100, len(N100)))


# insertion sort
def insertionSort(arr, n): # arr은 입력 배열, n은 배열의 크기(element 수)
    for i in range(1,n): # 두번째 element(arr[1])부터 시작 ~ 끝 elemnt(arr[n-1])까지
        key = arr[i] # key에 해당 element 저장
        j = i-1 # arr[j]는 arr[i] 전 element
        while j>=0 and arr[j]>key: # j>0이고 arr[j]>key(arr[i])이면 (for(i)문이 돌 때까지 계속)
            arr[j+1] = arr[j] # shift the elements
            j -= 1 # j=j-1
        arr[j+1] = key # while문을 모두 거치고 arr[j+1]에 key(arr[i]) 저장
    
    return arr # insertion sort한 배열 arr 반환

# print(N100, end="\n\n")
# print("insertion sort: ")
# print(insertionSort(N100, len(N100)))


# merge sort
def mergeSort(arr, n):
    if n < 2: # arr 길이가 2보다 작으면 그대로 반환
        return arr
    
    mid = n//2 # arr 배열의 중간 index (arr배열 반으로 쪼개기)
    L1 = mergeSort(arr[:mid], len(arr[:mid])) # 0 ~ mid-1 번째의 arr 배열을 mergeSort
    L2 = mergeSort(arr[mid:], len(arr[mid:])) # mid ~ 끝 번째의 arr 배열을 mergeSort
    mergeArr = [] # 새롭게 담을 배열 생성
    l = r = 0 # 0으로 초기화
    while l < len(L1) and r < len(L2): # 다음과 같은 조건을 만족하면 계속 반복
        if L1[l] < L2[r]: # 왼쪽 배열의 l번째 element가 오른쪽 배열의 r번째 element보다 작으면
            mergeArr.append(L1[l]) # 작은 쪽 추가
            l += 1 # 추가 후 +=1
        else: # 반대이면
            mergeArr.append(L2[r]) # 작은 쪽인 오른쪽 배열의 r번째 element 추가
            r += 1 # 추가 후 +=1
    mergeArr += L1[l:] # 왼쪽 배열의 l번째부터 끝까지 (남은 element) 추가
    mergeArr += L2[r:] # 오른쪽 배열의 r번째부터 끝까지 (남은 element) 추가

    return mergeArr # merge sort한 배열 반환

# print(N100, end="\n\n")
# print("merge sort: ")
# print(mergeSort(N100, len(N100)))


# radix sort
def radixSort(arr, n):
    ten=1 # 자릿수 판단할 변수
    while max(arr)//ten > 0: # 배열의 최댓값의 ten의 자릿수가 0보다 크면 계속
        output = [0]*n # ten의 자릿수에 따라 sort 해서 저장할 배열
        count = [0]*10 # 자릿수는 0~9까지기 때문에 길이가 10인 배열 생성
        for i in range(n):
            count[(arr[i]//ten)%10] += 1 # 자릿수(0~9) element 수 count해서 배열에 저장
        for i in range(1,10):
            count[i] += count[i-1] # 누적값 저장 (counting sort)
        for i in range(n-1,-1,-1):
            j = (arr[i]//ten)%10 # ten자리의 자릿수
            output[count[j]-1] = arr[i] # count[자릿수]-1 번째에 arr[i] 저장
            count[j] -= 1 # 저장하고 쓰인 count[j]-=1
        for i in range(n):
            arr[i] = output[i] # arr배열에 ten자릿수를 sorting한 순서대로 저장
        ten *= 10 # 다음 자릿수
    
    return arr # radix sort한 배열 반환

# print(N100, end="\n\n")
# print("radix sort: ")
# print(radixSort(N100, len(N100)))


# quick sort
def quickSort(arr,n):
    if n <= 1: # 배열 크기가 1보다 작으면 고대로 반환
        return arr
    pivot = arr[n // 2] # 중간값을 pivot으로
    left, mid, right = [], [], []
    for i in range(n):
        if arr[i] < pivot: # pivot보다 작으면 left에
            left.append(arr[i])
        elif arr[i] > pivot: # pivot보다 크면 right에
            right.append(arr[i])
        else: # pivot이랑 같으면
            mid.append(arr[i])
    return quickSort(left,len(left)) + mid + quickSort(right,len(right)) # quickSort한 왼쪽 배열 + 중간 배열(pivot) + quickSort한 오른쪽 배열 => quick Sort된 배열

# print(N100, end="\n\n")
# print("quick sort: ")
# print(quickSort(N100,len(N100)))

# bucket sort
def bucketSort(arr,n):
    B = [[] for _ in range(n)] # 초기화 된 B배열 생성 (create an array B of initiaaly empty buckets)
    for i in range(n):
        j = arr[i]*n // (max(arr)+1) 
        B[j].append(arr[i]) # scatter the objects of arr into B
    bucketArr = []
    for i in range(len(B)):
        bucketArr.extend(insertionSort(B[i],len(B[i]))) # sort the elements in each bucket && gather(.extend)
    
    return bucketArr

# print(N100, end="\n\n")
# print("bucket sort: ")
# print(bucketSort(N100,len(N100)))


# 실행 시간 측정

# bubble sort
start = time.time()
bubbleSort(N100, len(N100))
exTime.append(time.time()-start)

start = time.time()
bubbleSort(N1000, len(N1000))
exTime.append(time.time()-start)

start = time.time()
bubbleSort(N10000, len(N10000))
exTime.append(time.time()-start)

# insertion sort
start = time.time()
insertionSort(N100, len(N100))
exTime.append(time.time()-start)

start = time.time()
insertionSort(N1000, len(N1000))
exTime.append(time.time()-start)

start = time.time()
insertionSort(N10000, len(N10000))
exTime.append(time.time()-start)

# marge sort
start = time.time()
mergeSort(N100, len(N100))
exTime.append(time.time()-start)

start = time.time()
mergeSort(N1000, len(N1000))
exTime.append(time.time()-start)

start = time.time()
sys.setrecursionlimit(10000)
mergeSort(N10000, len(N10000))
exTime.append(time.time()-start)

# radix sort
start = time.time()
radixSort(N100, len(N100))
exTime.append(time.time()-start)

start = time.time()
radixSort(N1000, len(N1000))
exTime.append(time.time()-start)

start = time.time()
radixSort(N10000, len(N10000))
exTime.append(time.time()-start)

# quick sort
start = time.time()
quickSort(N100, len(N100))
exTime.append(time.time()-start)

start = time.time()
quickSort(N1000, len(N1000))
exTime.append(time.time()-start)

start = time.time()
sys.setrecursionlimit(10000)
quickSort(N10000, len(N10000))
exTime.append(time.time()-start)

# bucket sort
start = time.time()
bucketSort(N100, len(N100))
exTime.append(time.time()-start)

start = time.time()
bucketSort(N1000, len(N1000))
exTime.append(time.time()-start)

start = time.time()
bucketSort(N10000, len(N10000))
exTime.append(time.time()-start)

# size와 sort algorithm 이름 배열
sort = ["[size]", "[bubble sort]", "[insertion sort]", "[merge sort]", "[radix sort]", "[quick sort]", "[bucket sort]"]
for s in sort: # 가운데정렬로 size와 이름 정렬 
    print(s.center(25), end="")

# row1: 크기가 100인 입력값의 실행시간 / row2: 크기가 1000인 입력값의 실행시간 / row3: 크기가 10000인 입력값의 실행시간
row1 = [100, exTime[0], exTime[3], exTime[6], exTime[9], exTime[12], exTime[15]]
row2 = [1000, exTime[1], exTime[4], exTime[7], exTime[10], exTime[13], exTime[16]]
row3 = [10000, exTime[2], exTime[5], exTime[8], exTime[11], exTime[14], exTime[17]]

# 가운데 정렬로 size(크기)별로 실행시간 출력
print()
for r in row1:
    print(str(r).center(25), end="")
print()
for r in row2:
    print(str(r).center(25), end="")
print()
for r in row3:
    print(str(r).center(25), end="")
