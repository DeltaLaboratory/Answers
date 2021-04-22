import abc
import asyncio


class OnePlusOneBase(abc.ABC):
    """
    OnePlusOne Abstract Class

    'This Class Have Super Cat Power'
    """
    __repl__ = """OnePlusOne Abstract Class"""
    __str__ = __repl__

    @abc.abstractmethod
    def onePlusOne(self, one: None = None, plus: None = None, one2: None = None) -> int:
        """
        :param one : nothing
        :param plus : nothing
        :param one2 : nothing
        """


class OnePlusOneImpl(OnePlusOneBase):
    """
    OnePlusOne Implement Class

    method : onePlusOne (StaticMethod) -> int

    'This Class Have Super Moo Power'
    """
    __repl__ = """OnePlusOne Implement Class"""
    __str__ = __repl__

    def __init__(self) -> None:
        print("OnePlusOneImpl Loaded")

    @staticmethod
    async def setValue(future, value):
        future.set_result(value)

    @staticmethod
    async def getLoop():
        return asyncio.get_running_loop()

    @staticmethod
    async def getPointOne():
        return 0.1

    async def getOne(self):
        futureObject = (await self.getLoop()).create_future()
        await self.setValue(futureObject, (await self.getPointOne()) * 10)
        return futureObject

    async def onePlusOne(self, one: None = None, plus: None = None, one2: None = None) -> int:
        firstOne = await self.getOne()
        secondOne = await self.getOne()
        result = firstOne.result() + secondOne.result()
        return int(result)


def main() -> None:
    onePlusOne = OnePlusOneImpl()
    result = asyncio.run(onePlusOne.onePlusOne())
    print(result)
    return


if __name__ == "__main__":
    main()
