class Solution:
    def sortPeople(self, names, heights):
        # Sort the zipped list of names and heights by heights in descending order
        # and return the sorted names
        return [
            x for x, y in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        ]
