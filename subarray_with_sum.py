class Solution:
    @staticmethod
    def subarray_with_sum(arr, n, s):
        result = []
        for x in range(n):
            result.append(arr[x])
            while sum(result) > s:
                result.pop(0)
            if sum(result) == s:
                return f"{arr.index(result[0]) + 1} {arr.index(result[-1]) + 1}"
        return []


if __name__ == "__main__":
    solution = Solution()
    L = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93,
         183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
    print(solution.subarray_with_sum(L, 42, 468))
