import abc
import typing
import time
import asyncio
import multiprocessing


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
    def getPointOne(noWork=None):
        return 0.1

    @staticmethod
    def fixError_MP(integer):
        return integer + 0.0000000000000001

    def getOne_MP(self):
        with multiprocessing.Pool(10) as Pool:
            result = sum(Pool.map(self.getPointOne, [[]] * 10))
        return result

    def onePlusOne_MP(self):
        firstOne = self.fixError_MP(self.getOne_MP())
        secondOne = self.fixError_MP(self.getOne_MP())
        result = firstOne + secondOne
        return int(result)

    async def getOne(self):
        futureObject = (await self.getLoop()).create_future()
        await self.setValue(futureObject, (self.getPointOne()) * 10)
        return futureObject

    async def onePlusOne(self, one: None = None, plus: None = None, one2: None = None) -> int:
        firstOne = await self.getOne()
        secondOne = await self.getOne()
        result = firstOne.result() + secondOne.result()
        return int(result)


def timer(func: typing.Callable) -> typing.Callable:
    def deco() -> any:
        StartTime = time.perf_counter()
        print(f"Start Function : {str(func.__name__)}")
        res = func()
        print(f"Done Function : took {time.perf_counter() - StartTime}s.")
        return res

    return deco


def main() -> None:
    onePlusOne = OnePlusOneImpl()

    @timer
    def firstResult_ASYNCIO():
        return asyncio.run(onePlusOne.onePlusOne())

    @timer
    def secondResult_MP():
        onePlusOne.onePlusOne_MP()

    firstResult = firstResult_ASYNCIO()
    secondResult = secondResult_MP()
    print(f"1+1 ASYNCIO Ver : {firstResult}")
    print(f"1+1 Multiprocessing Ver : {secondResult}")
    return


if __name__ == "__main__":
    main()
