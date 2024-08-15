from binary_tree_async_iterator.tree_node import TreeNode


async def postorder_generator(root: TreeNode):
    """ Асинхронный генератор."""
    if root is not None:
        if root.left:
            async for value in postorder_generator(root.left):
                yield value
        
        if root.right:
            async for value in postorder_generator(root.right):
                yield value          

        yield await root.get_value()


class AsyncIteratorWithGenerator:
    """Реализация с использованием асинхронного генератора."""

    def __init__(self, root: TreeNode):
        """Инициализация."""
        self.root = root
        self.__generator = postorder_generator(root)
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        try:
            return await self.__generator.__anext__()
        except StopAsyncIteration:
            raise
    
