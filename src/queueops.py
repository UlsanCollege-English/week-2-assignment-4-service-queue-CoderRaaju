from typing import List, Tuple


def take_next(queue: List[str]) -> Tuple[str | None, List[str]]:
    """Return (next_name, remaining_queue).

    If queue is empty, return (None, []).
    """
    if not queue:
        return None, []
    return queue[0], queue[1:]


def move_to_back(queue: List[str], name: str) -> List[str]:
    """Return a new queue where the first occurrence of `name` is moved to the back.

    If `name` is not present, return the queue unchanged (new list).
    """
    new_queue = queue.copy()
    if name in new_queue:
        new_queue.remove(name)   # remove first occurrence
        new_queue.append(name)   # add to back
    return new_queue


def interleave(q1: List[str], q2: List[str]) -> List[str]:
    """Return an interleaved queue: q1[0], q2[0], q1[1], q2[1], ...

    After the shorter queue runs out, append the rest.
    """
    result = []
    min_len = min(len(q1), len(q2))

    # interleave pairs
    for i in range(min_len):
        result.append(q1[i])
        result.append(q2[i])

    # append remaining from longer queue
    result.extend(q1[min_len:])
    result.extend(q2[min_len:])

    return result
