class Codec:

    def encode(self, strs):
        # Initialize an empty string to store encoded result
        encoded = ""

        # Loop through each string in the list
        for s in strs:

            # Store the length of the string followed by a delimiter '#'
            encoded += str(len(s)) + "#" + s

        # Return the encoded string
        return encoded


    def decode(self, s):
        # List to store decoded strings
        res = []

        # Pointer to traverse the encoded string
        i = 0

        # Loop until we reach the end of the string
        while i < len(s):

            # Find the position of the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1

            # Extract the length of the string
            length = int(s[i:j])

            # Move pointer to start of the actual string
            i = j + 1

            # Extract the string using its length
            word = s[i:i + length]

            # Add the decoded string to result list
            res.append(word)

            # Move pointer forward for next iteration
            i += length

        # Return list of decoded strings
        return res