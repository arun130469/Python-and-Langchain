# Data Types Continued

## Sequences

- Immutable Sequence
  - Tuples
  - String
  - Bytes
- Mutable Sequences
  - Lists
    - List Comprehensions
  - Byte Array

## Sets

- Sets
- Frozen Sets

## Mappings

- Dictionaries
-
-


--------------------
## lists and tuples implementation
The difference between `PyObject **ob_item;` and `PyObject *ob_item[1];` is primarily about how **memory allocation** is handled for storing object references, which has implications for how these structures are used in CPython.

Let's break it down:

### 1. **`PyObject **ob_item;` (Used in Lists)**

This is a **pointer to a pointer**, specifically a pointer to an array of pointers to `PyObject`. It allows **dynamic allocation** and resizing of the array at runtime, which is necessary for mutable data structures like lists. Here’s what each part means:

- `PyObject **ob_item;` means `ob_item` is a pointer to an array of pointers. Each element in the array is a pointer to a `PyObject`, i.e., an object in Python.
- The key point here is that **`ob_item` does not have a fixed size** at the time of definition. The array of pointers that `ob_item` points to can be dynamically allocated, allowing the list to grow and shrink during its lifetime.
- **Dynamic memory allocation**: Since `ob_item` is a pointer to a pointer, the actual memory allocation for the array happens at runtime (using `malloc` or a similar mechanism in C). The size of the array can be adjusted dynamically, which is necessary for lists since they support operations like `append()`, `extend()`, and `pop()`.

For example:
```c
PyObject **ob_item = malloc(sizeof(PyObject*) * initial_size);
```
This dynamically allocates memory for an array of `initial_size` pointers to `PyObject`, which allows the list to grow and shrink by reallocating memory as needed.

### 2. **`PyObject *ob_item[1];` (Used in Tuples)**

This is an array of **one pointer** to a `PyObject`. However, in CPython's implementation, this is often used as a **trick** to allocate more memory than initially indicated, allowing tuples to store multiple object references without needing to dynamically resize. Here’s what each part means:

- `PyObject *ob_item[1];` declares an **array with a fixed size** of 1. It’s essentially a statically allocated array that holds one pointer to a `PyObject`. However, this is used as a **placeholder** or **flexible array member** in C to indicate that more memory can be allocated later.
  
- **Static size**: When a tuple is created, the actual memory allocation for `ob_item` is done for the exact number of elements the tuple will contain. The declaration as an array of size 1 is a way of defining the structure, but during tuple creation, enough memory is allocated to hold all the elements, not just one. So, while it looks like it only holds one element, additional space is allocated beyond the declared size to store the full tuple's contents.

For example:
```c
tuple = malloc(sizeof(PyTupleObject) + sizeof(PyObject*) * (n-1));
```
This allocates space for a tuple that holds `n` elements (the `n-1` part accounts for the fact that `ob_item` already declares space for 1 element).

- This method avoids the need for dynamic resizing since tuples are immutable, and their size is fixed upon creation.

### Why This Difference Exists

- **Lists** are mutable, so they need a flexible structure that allows for dynamic resizing. The `PyObject **ob_item;` declaration allows for **dynamic allocation** and resizing of the array of pointers as needed, making it possible to grow or shrink the list during its lifetime.

- **Tuples** are immutable, so their size is fixed when they are created. The `PyObject *ob_item[1];` declaration is a **trick** to allow for the flexible allocation of exactly the right amount of memory when the tuple is initialized, but no resizing is necessary afterward. The tuple’s size is known at the time of creation, so Python can allocate the exact amount of memory required.

### Memory Allocation Example:

#### For List (`PyObject **ob_item`):
When you create a list, memory is allocated dynamically based on how many elements are in the list, and it may over-allocate memory to allow for future `append()` operations:
```c
PyListObject *list = malloc(sizeof(PyListObject));
list->ob_item = malloc(sizeof(PyObject*) * initial_size);
```
If the list grows, `ob_item` can be reallocated:
```c
list->ob_item = realloc(list->ob_item, sizeof(PyObject*) * new_size);
```

#### For Tuple (`PyObject *ob_item[1]`):
When you create a tuple, Python allocates the exact memory needed for the tuple's elements:
```c
PyTupleObject *tuple = malloc(sizeof(PyTupleObject) + sizeof(PyObject*) * (n - 1));
```
Here, `n` is the number of elements in the tuple, and `sizeof(PyObject*) * (n - 1)` accounts for the fact that `ob_item` was declared with size 1 but needs space for `n` pointers.

### Summary of Differences:

- **`PyObject **ob_item;`** (used in lists):
  - A pointer to a dynamically allocated array of pointers.
  - Supports **dynamic resizing** (growth and shrinking).
  - Used for **mutable** data structures (like lists).

- **`PyObject *ob_item[1];`** (used in tuples):
  - A statically allocated array of pointers (though additional memory is allocated at creation).
  - **Fixed size**, does not support resizing.
  - Used for **immutable** data structures (like tuples).
  
In conclusion, `PyObject **ob_item;` allows lists to grow and shrink, while `PyObject *ob_item[1];` is a placeholder used in tuples to allocate the exact amount of memory when the tuple is created, ensuring efficient memory usage without the need for resizing.

