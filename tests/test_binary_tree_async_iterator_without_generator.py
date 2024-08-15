import unittest
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

    async def test_post_order_async_for(self):
        expected_result = [5, 4, 3, 2, 1]
        result = [item async for item in AsyncIteratorWithoutGenerator(self.root)]

        self.assertEqual(expected_result, result)

    async def test_async_for(self):
        expected_count = 5
        count = 0
        async for _ in AsyncIteratorWithoutGenerator(self.root):
            count += 1
            
        self.assertEqual(expected_count, count)

    async def test_post_order_anext(self):
        iterator = AsyncIteratorWithoutGenerator(self.root)
        expected_result = [5, 4, 3, 2, 1]
        result = [await anext(iterator) for _ in range(len(expected_result))]

        self.assertEqual(expected_result, result)

    async def test_anext(self):
        iterator = AsyncIteratorWithoutGenerator(self.root)

        with self.assertRaises(StopAsyncIteration):
            while True:
                await anext(iterator)

    async def test_empty_tree(self):
        empty_root = None
        iterator = AsyncIteratorWithoutGenerator(empty_root)

        with self.assertRaises(StopAsyncIteration):
            await anext(iterator)

    async def test_single_node_tree(self):
        single_node_tree = TreeNode(42)
        iterator = AsyncIteratorWithoutGenerator(single_node_tree)

        value = await anext(iterator)
        self.assertEqual(value, 42)

        with self.assertRaises(StopAsyncIteration):
            await anext(iterator)


if __name__ == '__main__':
    unittest.main()
