class Solution(object):
    def find_median(self, output_whole_array, length):
        if length == 1:
            return output_whole_array[0]
        if length%2 == 0:
            print(output_whole_array[(length/2)-1], output_whole_array[length/2])
            return float(output_whole_array[(length/2)-1] + output_whole_array[length/2]) / 2
        else:
            return math.ceil(output_whole_array[length/2])
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num1_length = len(nums1)
        num2_length = len(nums2)
        output_whole_array = []
        output_array_length = num1_length + num2_length
        pointer_of_num1 = 0
        pointer_of_num2 = 0
        cnt = 0
        if num1_length == 0:
            return self.find_median(nums2, num2_length)
        elif num2_length == 0:
            return self.find_median(nums1, num1_length)
        while cnt <= output_array_length + 1:
            if nums1[pointer_of_num1] <= nums2[pointer_of_num2]:
                output_whole_array.append(nums1[pointer_of_num1])
                pointer_of_num1 += 1
            else:
                output_whole_array.append(nums2[pointer_of_num2])
                pointer_of_num2 += 1
            if pointer_of_num1 == num1_length:
                output_whole_array.extend(nums2[pointer_of_num2:])
                break
            elif pointer_of_num2 == num2_length:
                output_whole_array.extend(nums1[pointer_of_num1:])
                break
            cnt+= 1
        return self.find_median(output_whole_array, output_array_length)

def stringToIntegerList(input):
    return json.loads(input)

def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums1 = stringToIntegerList(line)
            line = lines.next()
            nums2 = stringToIntegerList(line)
            
            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = doubleToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
