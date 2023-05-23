import bisect

arr=[1, 2, 10, 5, 8, 10, 10, 10, 20, 1, 100, 5, 5, 123,12]
indexes=[i for i in range(len(arr))]
arr.sort()

print(arr)
print(indexes)

target=10
#Time complexity O(logn)
print(f"{target} sayısının en soldaki index numarası", bisect.bisect_left(arr,target)) #bisect left methodu girilen elemanı arar ve o elemana eşit veya o elemandan buyuk en küçük sayıyı bastırır.
#yani eğer varsa aradağımı sayının en soldaki index numarasını bastırır. Eğer yok ise o sayıdan büyük,  en küçük sayının index numarasını bastırır.

target=9
#Time complexity O(logn)
print(f"{target} sayısının en soldaki index numarası", bisect.bisect_left(arr,target)) #bisect left methodu girilen elemanı arar ve o elemana eşit veya o elemandan buyuk en küçük sayıyı bastırır.
#yani eğer varsa aradağımı sayının en soldaki index numarasını bastırır. Eğer yok ise o sayıdan büyük,  en küçük sayının index numarasını bastırır.

target=2
#Time complexity O(logn)
print(f"{target} sayısının en sağdaki index numarası", bisect.bisect_right(arr,target)) #bisect right methodu ise girilen sayıdan büyük (sayıya eşit değil) en küçük sayının indexini bastırır.


target=10
#Time complexity O(logn)
print(f"{target} sayısının en sağdaki index numarası", bisect.bisect_right(arr,target)) #bisect right methodu ise girilen sayıdan büyük (sayıya eşit değil) en küçük sayının indexini bastırır.


#ornegin bir sayinin arrayin icinde olup olmadigini bulmak istiyoruz.
target=9
left_index=bisect.bisect_left(arr,target)
if(left_index!=len(arr) and arr[left_index]==target):
    print(f"{target} sayısı array'in içinde var")
else:
    print(f"{target} sayısı array'in içinde yok")

#ornegin bir sayinin arrayin icinde olup olmadigini bulmak istiyoruz.
target=10
left_index=bisect.bisect_left(arr,target)
if(left_index!=len(arr) and arr[left_index]==target):
    print(f"{target} sayısı array'in içinde var")
else:
    print(f"{target} sayısı array'in içinde yok")

#veya bir sayının arrayin içinde kaç defa geçtiğini bulmak istiyoruz.
target=10
left_index=bisect.bisect_left(arr,target)
right_index=bisect.bisect_right(arr,target)
if(left_index!=len(arr) and arr[left_index]==target):
    print(f"{right_index-left_index} tane {target} sayısı array'in içinde var")
else:
    print(0)

bisect.insort(arr,3) # verilen elemanı sorted sıralamayı bozmadan ekler. Time complexity O(N)

print(3,"array'in içine eklendi. Yeni array: ", arr)