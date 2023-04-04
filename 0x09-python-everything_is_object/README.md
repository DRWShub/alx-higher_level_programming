# 0x09. Python - Everything is object
* Definitions
Mutable object: Object that can be changed after creating it.
Immutable object: Object that cannot be changed after creating it.

In Python if you change the value of the immutable object it will create a new object.
Mutable Objects

* Here are the objects in Python that are of mutable type:

    list
    Dictionary
    Set
    bytearray
    user defined classes

* Immutable Objects

* Here are the objects in Python that are of immutable type:

    int
    float
    decimal
    complex
    bool
    string
    tuple
    range
    frozenset
    bytes

* Some Unanswered Questions

* Question: Is string an immutable type?
Answer: yes it is, but can you explain this: Proof 1:

a = "Hello"
a +=" World"
print a

Output

"Hello World"

* In the above example the string got once created as "Hello" then changed to "Hello World". This implies that the string is of the mutable type. But it is not when we check its identity to see whether it is of a mutable type or not.

a = "Hello"
identity_a = id(a)
a += " World"
new_identity_a = id(a)
if identity_a != new_identity_a:
    print "String is Immutable"

Output

* String is Immutable

Proof 2:

a = "Hello World"
a[0] = "M"

Output

TypeError 'str' object does not support item assignment

Question: Is Tuple an immutable type?
Answer: yes, it is. Proof 1:

tuple_a = (1,)
tuple_a[0] = (2,)
print a

Output

'tuple' object does not support item assignment
