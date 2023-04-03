#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    """
    s = time.time()
    await wait_n(n, max_delay)
    elapsed = time.time() - s
    return (elapsed / n)
