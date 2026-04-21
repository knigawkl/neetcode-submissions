class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = str(n)

        while cur not in seen:
            seen.add(cur)
            suma = 0
            for digit in cur:
                digit = int(digit)
                suma += digit ** 2

            if suma == 1:
                return True
            cur = str(suma)

        return False
