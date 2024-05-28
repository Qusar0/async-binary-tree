import unittest
from binary_tree_async_iterator.async_postorder_binary_tree_iterator import (
    AsyncIteratorWithoutGenerator,
    AsyncIteratorWithGenerator,
    TreeNode,
)


class MyTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
