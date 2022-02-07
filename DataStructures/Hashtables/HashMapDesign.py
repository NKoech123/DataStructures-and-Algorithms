#Create a class for Bucket operations
class Bucket:
    def __init__(self):
        self.bucket = []
    
    '''
    1. bucket stores:(key,value)
    2.Iterate through the bucket, and find you find the target key, return the value
      associated with it. Otherwise, return -1 (if key doesn't exist)
    '''
    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        '''
        1. bucket stores:(key,value)
        2. Iterate the bucket, find the target key, then update the value 
           associated with that key. Then break the loop.
        3. If that key is not found, then append the (key,value) to the bucket
       
        '''
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]

#Create a hashmap class
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.key_space = 2069   #length of hash_table
        self.hash_table = [Bucket() for i in range(self.key_space)]   #hast_table


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        
        Use hash_key to generate an int that corresponds to the address or index in our main storage.
        The hash_key directs us to the bucket where the value should be stored.
        """
        hash_key = key % self.key_space  
        self.hash_table[hash_key].update(key, value)


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
        

