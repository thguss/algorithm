import time # 시간 측정용 import
import sys

N100 = [i for i in range(100,0,-1)] # 100 99 98 ... 1
N1000 = [i for i in range(1000,0,-1)] # 1000 999 998 ... 1
N10000 = [i for i in range(10000,0,-1)] # 10000 9999 9998 ... 1

# bubble sort
def bubbleSort(arr, n): # arr은 입력 배열, n은 배열의 크기(element 수)
    for i in range(n-1): # n(element 수)-1 만큼의 pass (1번째 pass ~ n-1번째 pass)
        for j in range(n-1-i): # i번째 pass에서는 (n-1)번 만큼 sorting
            if arr[j] > arr[j+1]: # 오름차순이므로 arr[j] > arr[j+1] 이면 서로 swap
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap
    
    return arr # bubble sort한 배열 arr 반환

print("bubble sort: ")

# N100: bubble sort 출력 및 시간 측정
start_time = time.time()
# print("N100: ", end="")
# print(bubbleSort(N100, len(N100)))
bubbleSort(N100, len(N100)
# end_bubble_100 = time.time() - start_time # bubble sort 실행 시간 for N100
# print(time.time() - start_time)
print(start_time)
# print(time.time())

# N1000: bubble sort 출력 및 시간 측정
start_time = time.time()
# print("N1000: ", end="")
# print(bubbleSort(N1000, len(N1000)))
bubbleSort(N1000, len(N1000))
end_bubble_1000 = time.time() - start_time # bubble sort 실행 시간 for N1000

# N10000: bubble sort 출력 및 시간 측정
start_time = time.time()
# print("N10000: ", end="")
# print(bubbleSort(N10000, len(N10000)))
bubbleSort(N10000, len(N10000))
end_bubble_10000 = time.time() - start_time # bubble sort 실행 시간 for N10000


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

# N100: insertion sort 출력 및 시간 측정
start_time = time.time()
# print(insertionSort(N100, len(N100)))
insertionSort(N100, len(N100))
end_insertion_100 = time.time() - start_time # insertion sort 실행 시간 for N100

# N1000: insertion sort 출력 및 시간 측정
start_time = time.time()
# print(insertionSort(N1000, len(N1000)))
insertionSort(N1000, len(N1000))
end_insertion_1000 = time.time() - start_time # insertion sort 실행 시간 for N1000

# N10000: insertion sort 출력 및 시간 측정
start_time = time.time()
sys.setrecursionlimit(10000)
# print(insertionSort(N10000, len(N10000)))
insertionSort(N10000, len(N10000))
end_insertion_10000 = time.time() - start_time # insertion sort 실행 시간 for N10000


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
            h += 1 # 추가 후 +=1
    mergeArr += L1[l:] # 왼쪽 배열의 l번째부터 끝까지 (남은 element) 추가
    mergeArr += L2[r:] # 오른쪽 배열의 r번째부터 끝까지 (남은 element) 추가

    return mergeArr # merge sort한 배열 반환

# N100: merge sort 출력 및 시간 측정
start_time = time.time()
# print(mergeSort(N100, len(N100)))
mergeSort(N100, len(N100))
end_merge_100 = time.time() - start_time # merge sort 실행 시간 for N100

# N1000: merge sort 출력 및 시간 측정
start_time = time.time()
# print(mergeSort(N1000, len(N1000)))
mergeSort(N1000, len(N1000))
end_merge_1000 = time.time() - start_time # merge sort 실행 시간 for N1000

# N10000: merge sort 출력 및 시간 측정
start_time = time.time()
# print(mergeSort(N10000, len(N10000)))
mergeSort(N10000, len(N10000))
end_merge_10000 = time.time() - start_time # merge sort 실행 시간 for N10000


# radix sort
def radixSort(arr, n):
    ten=1 # 자릿수 판단할 변수
    while max(arr)>ten: # 배열의 최댓값이 ten보다 크면 반복
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
        ten += 10 # 다음 자릿수
    
    return arr # radix sort한 배열 반환

# N100: radix sort 출력 및 시간 측정
start_time = time.time()
# print(radixSort(N100, len(N100)))
radixSort(N100, len(N100))
end_radix_100 = time.time() - start_time # radix sort 실행 시간 for N100

# N1000: radix sort 출력 및 시간 측정
start_time = time.time()
# print(radixSort(N1000, len(N1000)))
radixSort(N1000, len(N1000))
end_radix_1000 = time.time() - start_time # radix sort 실행 시간 for N1000

# N10000: radix sort 출력 및 시간 측정
start_time = time.time()
# print(radixSort(N10000, len(N10000)))
radixSort(N10000, len(N10000))
end_radix_10000 = time.time() - start_time # radix sort 실행 시간 for N10000


# quick sort
def quickSort(arr, s, e):
    def partition(arr, p, q):
        pivot = arr[p] # arr배열의 start position을 pivot으로 두기
        i = p # i = arr 배열의 첫원소 index
        for j in range(p+1, q): # 처음+1 ~ 끝
            if arr[j] <= pivot: # pivot 보다 작거나 같으면
                i += 1 # i+=1 한 상태에서
                arr[i], arr[j] = arr[j], arr[i] # arr[i]과 swap
        arr[p], arr[i] = arr[i], arr[p] # pivot 원소를 이하인 쪽과 큰 쪽의 경계점 자리(i)로 swap

        return i # pivot 자리 index 반환

    if len(arr) <= 1:
        return arr
    
    if s < e:
        q = partition(arr,s,e) # pivot 자리 index 구해서 q에 저장
        quickSort(arr,s,q-1) # pivot 원소 이하인 쪽의 배열 quickSort
        quickSort(arr,q+1,e) # pivot 원소보다 큰 쪽의 배열 quickSort
    
    return arr # quick sort한 배열 반환

# N100: quick sort 출력 및 시간 측정
start_time = time.time()
# print(quickSort(N100, 0, len(N100)))
quickSort(N100, 0, len(N100))
end_quick_100 = time.time() - start_time # quick sort 실행 시간 for N100

# N1000: quick sort 출력 및 시간 측정
start_time = time.time()
# print(quickSort(N1000, 0, len(N1000)))
quickSort(N1000, 0, len(N1000))
end_quick_1000 = time.time() - start_time # quick sort 실행 시간 for N1000

# N10000: quick sort 출력 및 시간 측정
start_time = time.time()
# print(quickSort(N10000, 0, len(N10000)))
quickSort(N10000, 0, len(N10000))
end_quick_10000 = time.time() - start_time # quick sort 실행 시간 for N10000


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

# N100: bucket sort 출력 및 시간 측정
start_time = time.time()
# print(bucketSort(N100, len(N100)))
bucketSort(N100, len(N100))
end_bucket_100 = time.time() - start_time # bucket sort 실행 시간 for N100

# N1000: bucket sort 출력 및 시간 측정
start_time = time.time()
# print(bucketSort(N1000, len(N1000)))
bucketSort(N1000, len(N1000))
end_bucket_1000 = time.time() - start_time # bucket sort 실행 시간 for N1000

# N10000: bucket sort 출력 및 시간 측정
start_time = time.time()
# print(bucketSort(N10000, len(N10000)))
bucketSort(N10000, len(N10000))
end_bucket_10000 = time.time() - start_time # bucket sort 실행 시간 for N10000


# print(end_bubble_100)
print(end_bubble_1000)
print(end_bubble_10000)

print(end_insertion_100)
print(end_insertion_1000)
print(end_insertion_10000)

print(end_merge_100)
print(end_merge_1000)
print(end_merge_10000)

print(end_radix_100)
print(end_radix_1000)
print(end_radix_10000)

print(end_quick_100)
print(end_quick_1000)
print(end_quick_10000)

print(end_bucket_100)
print(end_bucket_1000)
print(end_bucket_10000)