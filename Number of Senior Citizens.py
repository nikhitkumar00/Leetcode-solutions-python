class Solution:
    def countSeniors(self, details):
        # Initialize the counter for seniors
        count = 0

        # Iterate over each detail in the list
        for detail in details:
            # Check if the age extracted from the detail is greater than 60
            if int(detail[11:13]) > 60:
                # Increment the counter if the condition is met
                count += 1

        # Return the final count of seniors
        return count