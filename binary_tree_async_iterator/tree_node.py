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
