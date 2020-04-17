class A:
    pass


class B(A):
    pass


class C:
    pass


print(issubclass(A, B))
print(issubclass(B, A))
print(issubclass(B, object))
print(issubclass(B, (A, C)))
print(issubclass(B, (A, B, C)))
