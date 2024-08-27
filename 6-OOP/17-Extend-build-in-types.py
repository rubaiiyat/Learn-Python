class Text(str):
    def duplicate(
        self,
    ):
        return self + self


txt = Text("Python")
print(txt.duplicate())
