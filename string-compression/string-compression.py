class Solution:
    def compress(self, chars: List[str]) -> int:
        # Since we're modifying the input array and returning the length of new, we can just write over the old values
        # Use sliding window
        # Expand window until next character is != current char at left
        # Change left + 1 to size of sliding window. Should be string
        # Start window again at right + 1
        # This time, put character at right + 1 into left + 2 (maybe introduce a third pointer)
        # repeat process until end of array
        # Return pos of third pointer + 1
        
        left = right = 0
        ptr = 0
        while right < len(chars):
            # Make char at pointer == char at left pointer
            chars[ptr] = chars[left]
            # Increment ptr. This is where the number will go
            ptr += 1
            # Expand window until next char != current
            while right + 1 < len(chars) and chars[left] == chars[right + 1]:
                right += 1
                
            size = right - left + 1
            if size > 1:
                if size < 10:
                    chars[ptr] = str(size)
                else:
                    while size > 0:
                        if size < 100:
                            if size >= 10:
                                digit = size // 10
                                size %= 10
                                chars[ptr] = str(digit)
                                ptr += 1
                                if size == 0:
                                    chars[ptr] = "0"
                            else:
                                chars[ptr] = str(size)
                                size = 0
                        else:
                            digit = size // 100
                            size %= 100
                            chars[ptr] = str(digit)
                            ptr += 1
                            
                ptr += 1
                
            left = right + 1
            right = left
            
        return ptr
            