def merge_count(left,right):
    merged = []
    i,j = 0,0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i #因为left和right都是已经排序好的，所以如果right[j]被添加到merged中，那么left中所有还没有被添加到merged中的元素都比right[j]要大，所以就有len(left) - i个这样的元素
    merged.extend(left[i:]) #注意要用extend而不是append，不然就是把剩下的所有元素作为一个列表整体添加进去而非逐元素添加进去了！
    merged.extend(right[j:])
    return merged,count

def sort_count(array):
    if len(array) <= 1: #告诉函数这时候就不要再调用自己了,即“到头了”
        return array,0
    else:
        left,count_left = sort_count(array[:len(array)//2])
        right,count_right = sort_count(array[len(array)//2:])
        merged,count_merge = merge_count(left,right)
        all_count = count_left + count_right + count_merge
        return merged,all_count #每一层都在等待自己下面的层完成
    
if __name__ == '__main__':
    with open('array.txt','r') as f:
        lines = f.readlines()
        array = [int(line.strip()) for line in lines]
        sorted_array,count = sort_count(array)
        print(count)
