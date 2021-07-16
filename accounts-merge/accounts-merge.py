import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Use two hash tables to keep track of name and emails
        # We need two because same name might not be same emails - aka key conflict
        # So we have one hash with key/val of a number and an array of respective emails
        # And a second hash with key/val of a name and an array of numbers, representing key for first hash
        # Maybe a third hash to keep track of seen emails and which number they went to
        
        # Helper func to combine lists
        def combine(arr):
            # arr will give us the keys to combine in sorted order.
            # We will combine everything with the first occurrence and delete the rest
            n = len(arr)
            ptr = 1
            
            while ptr < n:
                # Add everything from current pointer's email list to the one at 0th index
                for email in email_list[arr[ptr]]:
                    # Add email to lowest key value
                    email_list[arr[0]].append(email)
                    # Change tracker
                    tracker[email] = arr[0]
                
                # Now delete all traces of that key
                del email_list[arr[ptr]]
                del mapper[arr[ptr]]
                
                # Increment
                ptr += 1
            
                
        
        # Hash one - key is an ID with an array of emails that corresponds to that specific ID
        email_list = collections.defaultdict(list)
        
        # Hash two - correlates key values to its respective string name
        mapper = {}
        
        # Hash three - Keeps track of which ID the emails were sent to for quicker lookup
        tracker = {}
        
        # print("Hashes initialized")
        # Iterate through each array in accounts
        curr_key = 0
        for acc in accounts:
            # For each one, we want to separate name from emails
            name = acc[0]
            emails = acc[1:]
            
            # print("Account name: {}\nassociated emails: {}".format(name, emails))            
            # We need to iterate through every email in emails and see if it's already
            # placed into someone's account. If so, we place that value into key instead
            connect = []
            for email in emails:
                if email in tracker:
                    # print("Current email, {}, was found associated with another account key: {}"
                          # .format(email, tracker[email]))
                    if tracker[email] not in connect:
                        connect.append(tracker[email])
                        
            
            if len(connect) == 1:
                key = connect[0]
            elif len(connect) > 1:
                connect.sort()
                combine(connect)
                key = connect[0]
            else:
                key = curr_key
                
            # print("Our key is currently: {}".format(key))
            # Now we just need to place everything where it belongs
            # First place each email into email_list
            # As we do so, we'll add it to tracker, too
            for email in emails:
                # If it's in tracker, then we've already added it. No need to do it again
                if email not in tracker:
                    email_list[key].append(email)
                    tracker[email] = key
                    # print("Email, {}, added to list of account key: {}. Tracker added".format(email, key))
                
            # Then map the key to the name
            mapper[key] = name
            # print("Added key to map: {}".format(mapper))
            curr_key += 1
            
        # At end of this for loop, we should have everything in email list and mapper for name
        # Just make our answer array and return it
        ans = []
        # print("Formulating final answer array")
        for key in email_list:
            acc = []
            # First add the name
            acc.append(mapper[key])
            # print("Added name: {}".format(mapper[key]))
            # Then add the emails after sorting
            email_list[key].sort()
            acc += email_list[key]
            # print("Adding emails to acc. Acc is now: {}".format(acc))
            # Then add to ans
            ans.append(acc)
            # print("Appending to ans")
            
        return ans
        