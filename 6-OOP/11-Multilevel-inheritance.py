class A:
    def __init__(self) -> None:
        print("This is class A")


class B(A):
    def __init__(self) -> None:
        print("This is class B")


class C(B):
    def __init__(self) -> None:
        super().__init__()
        print("This is class C")


obj = C()
obj.__init__()
