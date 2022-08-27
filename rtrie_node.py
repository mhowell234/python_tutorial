from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass, field

R: int = 26


@dataclass
class RTrieNode:
    value: int
    size: int = R
    next_: List[RTrieNode] = field(default_factory=lambda: [None] * R)

    def __post_init__(self):
        if len(self.next_) != self.size:
            raise ValueError(f"Invalid length provided for next list")


def init_children() -> List[Optional[RTrieNode]]:
    return [None] * R


if __name__ == '__main__':
    s = RTrieNode(value=5)

    kids = init_children()
    kids[0] = s

    r = RTrieNode(value=4, next_=kids)

    print(r)
