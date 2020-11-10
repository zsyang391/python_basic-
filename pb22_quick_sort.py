"""
快速排序
"""

a = [54, 26, 93, 17, 77, 31, 44, 55, 20]


# 基准数(第一个元素)54 比54小的放在左边，比54大的放在右边
# low = 1
# high = n-1
def quick_sort(quick_list):
    if not quick_list:
        return []
    else:
        first = quick_list[0]
        less = quick_sort([l for l in quick_list[1:] if l < first])
        more = quick_sort([m for m in quick_list[1:] if m >= first])
        return less + [first] + more


print(quick_sort(a))
