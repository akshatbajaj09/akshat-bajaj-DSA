class Solution:
    def isValid(self, s: str) -> bool:
        # For every bracket to make a pair, the length of s must be even:
        if len(s) % 2 != 0:
            return False
        st = []
        for char in s:
            # Opening brackets:
            if char in "({[":
                st.append(char)
            # Closing brackets:
            else:
                # Closing bracket in the beginning:
                if len(st) == 0:
                    return False
                top = st.pop()
                # Closing bracket does not match with opening bracket:
                if char == ")" and top != "(":
                    return False
                elif char == "}" and top != "{":
                    return False
                elif char == "]" and top != "[":
                    return False
        # If stack is non-empty it means all opening brackets were not paired:
        return len(st) == 0
