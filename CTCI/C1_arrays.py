# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
def checkunique(string1):
     set_string = set(string1)
     if len(set_string) == len(string1):
         return "Yes, all unique"
     else:
         return "No, there are duplicates"
         
  
