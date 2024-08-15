import unittest
from binary_tree_async_iterator.tree_node import TreeNode
from binary_tree_async_iterator.async_iterator_with_generator import AsyncIteratorWithGenerator
import asyncio

class TestAsyncIteratorWithGenerator(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = TreeNode(1)
        cls.root.right = TreeNode(2)
        cls.root.left = TreeNode(3)
        cls.root.left.right = TreeNode(4)
        cls.root.left.left = TreeNode(5)

    @staticmethod
    async def collect_values(iterator):
        result = []
        async for value in iterator:
            result.append(value)
        return result

    async def test_post_order_async_for(self):
        iterator = AsyncIteratorWithGenerator(self.root)
        expected_result = [5, 4, 3, 2, 1]

        values = await self.collect_values(iterator)

        self.assertEqual(expected_result, values)

    async def test_async_for(self):
        expected_count = 5
        iterator = AsyncIteratorWithGenerator(self.root)

        count = len(await self.collect_values(iterator))

        self.assertEqual(expected_count, count)

    async def test_post_order_anext(self):
        iterator = AsyncIteratorWithGenerator(self.root)
        expected_result = [5, 4, 3, 2, 1]

        result = [await anext(iterator) for _ in range(len(expected_result))]

        self.assertEqual(expected_result, result)

    async def test_anext(self):
        iterator = AsyncIteratorWithGenerator(self.root)

        with self.assertRaises(StopAsyncIteration):
            while True:
                await anext(iterator)

    async def test_empty_tree(self):
        empty_root = None
        iterator = AsyncIteratorWithGenerator(empty_root)

        with self.assertRaises(StopAsyncIteration):
            await anext(iterator)

    async def test_single_node_tree(self):
        single_node_tree = TreeNode(13)
        iterator = AsyncIteratorWithGenerator(single_node_tree)

        value = await anext(iterator)
        self.assertEqual(value, 13)

        with self.assertRaises(StopAsyncIteration):
            await anext(iterator)


if __name__ == '__main__':
    unittest.main()
