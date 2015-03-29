#Fill tetrahedron with water.
You have to implement a function with the following signature: `fill_tetrahedron(num)`.
- The argument num is of type integer.
- The function should return a float (double).

![Regular tetrahedron](http://upload.wikimedia.org/wikipedia/commons/7/70/Tetrahedron.gif)

`fill_tetrahedron(num)` takes one argument that is the edge length of a Regular tetrahedron in centimeters. It should return the amount of water that can be filled in the tetrahedron. Return that amount in liters.

You can use any language you know.

Examples:
```
>>> fill_tetrahedron(100)
117.85
```
You can fill Regular tetrahedron with edge of 100 cm with 117.85 liters of water.


#Tetrahedron filled with water.
You have to implement a function with the following signature: `tetrahedron_filled(tetrahedrons, water)`.
- The argument tetrahedrons is list of integers. Each is edge length of a Regular tetrahedron
- The argument water is an integer. It is the amount of water that we have in liters.
- The function should return a integer.

`tetrahedron_filled(tetrahedrons, water)`.It should return the maximum number of tetrahedrons that can be field with hater liters of water.

You can use any language you know.
You can use the previous function.

Examples:
```
>>> tetrahedron_filled([100, 20, 30], 10)
2
```

You can fill only 2 of this Regular tetrahedrons with 10 liters of water. First you are going to fill the second than the third tetrahedron. With the total amount of ~ 4 liters. You won't have water to fill the first tetrahedron.


# Caesar cipher

Caesar cipher is one of the simplest and most widely known encryption techniques. The method is named after Julius Caesar, who used it in his private correspondence.

You have the implement a function with the following signature: caesar_encrypt(str, n).
- The argument str is of type string
- The argument n is of type integer.
- The function should return an encrypted string

The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,..., Z = 25. Encryption of a letter x by a shift n can be described mathematically as,

![](http://upload.wikimedia.org/math/b/b/b/bbb819c72cda43180d98e6ade5cadb04.png)

`Do not` encrypt any non-alphabetical characters!

Example:

```
>>> caesar_encrypt("abc", 1)
"bcd"
>>> caesar_encrypt("ABC", 1)
"BCD"
>>> caesar_encrypt("abc", 2)
"cde"
>>> caesar_encrypt("aaa", 7)
"hhh"
>>> caesar_encrypt("xyz", 1)
"yza"
```
