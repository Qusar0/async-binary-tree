from tree_node import TreeNode

class AsyncIteratorWithoutGenerator:
    """Реализация без использования асинхронного генератора."""

    def __init__(self, root: TreeNode):
        """Инициализация."""
        self.stack = []
        self.root = root
        self.last_visited = None
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        """Асинхронный обход дерева в post-order порядке."""
        while self.stack or self.root:
            if self.root:
                self.stack.append(self.root)
                self.root = self.root.left
            else:
                peek_node = self.stack[-1]
                if peek_node.right and self.last_visited != peek_node.right:
                    self.root = peek_node.right
                else:
                    self.last_visited = self.stack.pop()
                    return await self.last_visited.get_value()

        raise StopAsyncIteration

