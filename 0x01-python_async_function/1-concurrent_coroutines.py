#!/usr/bin/env python3
"""..."""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Create a list of tasks that call wait_random with the given max_delay"""

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Wait for the tasks to complete and retrieve their results
    delays = [await task for task in asyncio.as_completed(tasks)]

    # Return the list of delays in ascending order
    return delays
