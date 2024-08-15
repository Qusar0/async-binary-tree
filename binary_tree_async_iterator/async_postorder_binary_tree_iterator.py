import asyncio
from async_iterator_with_generator import AsyncIteratorWithGenerator
from async_iterator_without_generator import AsyncIteratorWithoutGenerator
from tree_node import TreeNode
from random import random


async def using_generator(root: TreeNode, generator: bool):
    if generator:
        async for item in AsyncIteratorWithGenerator(root):
            print(item, end=" ")
    else:
        async for item in AsyncIteratorWithoutGenerator(root):
            print(item, end=" ")


async def first_tree(with_generator: bool=False):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.right = TreeNode(4)
    root.left.left.left = TreeNode(5, get_value_timeout_in_seconds=1)

    await using_generator(root, with_generator)


async def second_tree(with_generator: bool=False):
    root = TreeNode(6)
    root.right = TreeNode(7)
    root.right.right = TreeNode(8, get_value_timeout_in_seconds=2)
    root.left = TreeNode(9)
    root.left.right = TreeNode(10)

    await using_generator(root, with_generator)


async def third_tree(with_generator: bool=False):
    root = TreeNode(11)
    root.right = TreeNode(12)
    root.right.right = TreeNode(13, get_value_timeout_in_seconds=3)
    root.right.right.right = TreeNode(14)
    root.right.right.left = TreeNode(15)

    await using_generator(root, with_generator)


async def main():
    print("Async iterator without generator")
    await asyncio.gather(first_tree(),
                         second_tree(),
                         third_tree())
    
    print("\n\nAsync iterator with generator")
    await asyncio.gather(first_tree(with_generator=True),
                         second_tree(with_generator=True),
                         third_tree(with_generator=True))


if __name__ == "__main__":
    asyncio.run(main())

