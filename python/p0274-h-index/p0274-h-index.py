from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        frequency = [0] * (len(citations) + 1)
        for num in citations:
            frequency[min(num, len(citations))] += 1  # Count paper with more than n citations as n

        cum_citations, h = len(citations), 0  # cum_citations is number of papers with at least i citations
        for i, num in enumerate(frequency):
            h = max(h, min(i, cum_citations))
            cum_citations -= num

        return h
