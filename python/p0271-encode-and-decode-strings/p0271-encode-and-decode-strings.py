class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        # Encode strings as "<length_of_s>,s"
        encoding = ""
        for s in strs:
            encoding += str(len(s)) + "," + s

        return encoding

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        i = 0
        decoding = []
        while i < len(s):
            length = int(s[i:s.index(",", i)])
            decoding.append(s[s.index(",", i) + 1:s.index(",", i) + length + 1])
            i = s.index(",", i) + length + 1

        return decoding


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
