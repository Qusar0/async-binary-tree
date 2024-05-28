import asyncio


class TreeNode:
    """Узел бинарного дерева."""

    def __init__(self, val=0, left=None, right=None, get_value_timeout_in_seconds=0):
        """Инициализация."""
        self.__val = val
        self.get_value_timeout_in_seconds = get_value_timeout_in_seconds
        self.left = left
        self.right = right

    async def get_value(self):
        """Асинхронное получение значения узла дерева."""
        if self.get_value_timeout_in_seconds is not None:
            await asyncio.sleep(self.get_value_timeout_in_seconds)
        return self.__val


async def postorder_generator(root: TreeNode):
    """ Асинхронный генератор."""


class AsyncIteratorWithGenerator:
    """Реализация с использованием асинхронного генератора."""

    def __init__(self, root: TreeNode):
        """Инициализация."""


class AsyncIteratorWithoutGenerator:
    """Реализация без использования асинхронного генератора."""

    def __init__(self, root: TreeNode):
        """Инициализация."""


async def main():
    """ Демонстрируем одновременный проход по трем деревьям сначала с использованием класса AsyncIteratorWithGenerator,
        затем проход по тем же деревьм с помощью AsyncIteratorWithoutGenerator.
    """


if __name__ == "__main__":
    asyncio.run(main())
