# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

# Counter: A subclass of dict that counts hashable objects.
a = "aaaasvfbdsfffbbbbddddvvs"
my_Counter = Counter(a)

# Counter object and methods
print("Counter:", my_Counter)
print("Items in Counter:", my_Counter.items())
print("Keys in Counter:", my_Counter.keys())
print("Values in Counter:", my_Counter.values())

# Most common elements
print("Most common 2 elements:", my_Counter.most_common(2))
print("Most common element:", my_Counter.most_common(2)[0])
print("Most common element key:", my_Counter.most_common(2)[0][0])

# List all elements
print("All elements in Counter:", list(my_Counter.elements()))

from collections import namedtuple

# namedtuple: Factory function to create tuple subclasses with named fields.
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)

# Accessing fields in namedtuple
print("Named tuple:", pt)
print("Named tuple fields:", pt.x, pt.y)

from collections import OrderedDict

# OrderedDict: A dictionary subclass that remembers the order in which its contents are added.
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

# OrderedDict maintains insertion order
print("OrderedDict:", ordered_dict)

from collections import defaultdict

# defaultdict: A dictionary subclass that calls a factory function to supply missing values.
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3

# Accessing existing and non-existing keys
print("Value of key 'b':", d['b'])
print("Value of key 'v' (default):", d['v'])  # Key 'v' does not exist, returns default int() -> 0

from collections import deque

# deque: A double-ended queue that supports adding and removing elements from either end.
d = deque()

# Append elements to the deque
d.append(1)
d.append(2)
d.appendleft(3)

print("Deque after appending elements:", d)

# Pop elements from deque
d.pop()
print("Deque after pop:", d)

d.popleft()
print("Deque after popleft:", d)

# Extend deque with iterable
d.extend([4, 5, 6])
print("Deque after extend:", d)

d.extendleft([7, 8, 9])
print("Deque after extendleft:", d)

# Remove a specific element
d.remove(7)
print("Deque after removing 7:", d)

# Rotate the deque
d.rotate(1)
print("Deque after rotating right by 1:", d)

d.rotate(-1)
print("Deque after rotating left by 1:", d)

# Clear the deque
d.clear()
print("Deque after clearing:", d)


# Explanation of Key Concepts:

# Counter:
# Counter is a subclass of dict used for counting hashable objects. It automatically counts the occurrences of each element in a collection.

# namedtuple:
# namedtuple is a factory function for creating tuple subclasses with named fields, providing a lightweight, immutable data structure with readable field names.

# OrderedDict:
# OrderedDict is a dictionary subclass that remembers the order of insertion of keys. Even though in Python 3.7+ regular dictionaries maintain insertion order, OrderedDict provides additional functionalities like move_to_end().

# defaultdict:
# defaultdict is a dictionary subclass that calls a factory function to provide default values for missing keys, preventing KeyError.

# deque:
# deque (double-ended queue) supports fast O(1) operations for adding and removing elements from both ends of the queue, making it ideal for implementing queues and stacks efficiently.