class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded += f"{len(string)}#{string}"
        return encoded

    def decode(self, string: str) -> List[str]:
        # 5#Hello5#World

        
        decoded = []
        

        i = 0

        while i < len(string):

            # read the length
            length = ""
            while string[i] != "#":
                length = length + string[i]
                i += 1
            print(length)

            # skip '#'
            i += 1

            # read exactly `length` characters
            decoded.append(string[i:i + int(length)])

            # jump past that word
            i += int(length)

        print(decoded)
        return decoded
            

            
