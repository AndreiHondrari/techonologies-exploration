import attr


@attr.s(kw_only=True)
class SomeClass:
    a: str = attr.ib(converter=str)


if __name__ == '__main__':
    o1 = SomeClass(a=123)
    print("o1", o1)
