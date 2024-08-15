import unittest
from binary_tree_async_iterator.async_iterator_with_generator import AsyncIteratorWithGenerator
from binary_tree_async_iterator.async_iterator_without_generator import AsyncIteratorWithoutGenerator
from binary_tree_async_iterator.tree_node import TreeNode


class TestAsyncIteratorWithoutGenerator(unittest.IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls):
        cls.root = TreeNode(1)
        cls.root.right = TreeNode(2)
        cls.root.left = TreeNode(3)
        cls.root.left.right = TreeNode(4)
        cls.root.left.left = TreeNode(5)


    async def test_post_order(self):
        expected_result = [5, 4, 3, 2, 1]
        result = [item async for item in AsyncIteratorWithoutGenerator(self.root)]

        self.assertEqual(expected_result, result)

    async def test_anext(self):
        iterator = AsyncIteratorWithoutGenerator(self.root)

        with self.assertRaises(StopAsyncIteration):
            while True:
                await anext(iterator)

    async def test_async_for(self):
        async for _ in AsyncIteratorWithoutGenerator(self.root):
            pass


if __name__ == '__main__':
    unittest.main()
