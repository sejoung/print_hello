class Hello:  # pylint: disable=too-few-public-methods
    def __init__(self, name: str) -> None:
        self.name = name

    def print(self) -> None:
        print("Hello, world!, my name is", self.name)
