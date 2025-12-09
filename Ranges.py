from abc import ABC, abstractmethod
from io import UnsupportedOperation
from numbers import Number
from typing import Iterable

def range_set(ranges):
    if len(ranges)==1:
        return ranges[0]
    else:
        return RangeSet(ranges)

class RangeLike(ABC):
    @abstractmethod
    def union(self, other):
        pass

    def __and__(self, other):
        return self.intersection(other)

    @abstractmethod
    def intersection(self, other):
        pass

    def __or__(self, other):
        return self.union(other)

class Range(RangeLike):
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.isEmpty = low>high

    def __repr__(self):
        if self.isEmpty:
            return "Φ"
        if self.high==self.low:
            return f"{'{'+str(self.high)+'}'}"
        return f"[{self.low}, {self.high}]"

    def __contains__(self, item):
        if isinstance(item, Number):
            return item>=self.low and item<=self.high
        if isinstance(item, Range):
            return item.low>=self.low and item.high<=self.high
        raise UnsupportedOperation
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.low == other and self.high ==other
        if not isinstance(other,Range):
            return False
        return (self.low == other.low and self.high == other.high) or (self.isEmpty and other.isEmpty)

    def __len__(self):
        #IMPORTANT: We assume ranges are discrete for this length
        if self.isEmpty:
            return 0
        return self.high-self.low+1

    def union(self, other):
        if self.isEmpty or other.isEmpty:
            return other
        if isinstance(other, RangeSet):
            return other.union(self)
        if self.intersection(other).isEmpty:
            return RangeSet([self, other])
        low = min(self.low, other.low)
        high = max(self.high, other.high)
        return Range(low, high)

    def intersection(self, other):
        if self.isEmpty:
            return self
        if other.isEmpty:
            return other
        low = max(self.low, other.low)
        high = min(self.high, other.high)
        return Range(low, high)


class RangeSet(RangeLike):
    def __init__(self, ranges: Iterable[Range]):
        self.ranges = list(ranges)
        self.ranges.sort(key=lambda s: s.low)

        prev_high = None
        for r in self.ranges:
            if prev_high is not None and r.low <= prev_high:
                if r.low < prev_high:
                    raise Exception("Ranges are not disjoint one to one. Use union of ranges")
                else:
                    raise Exception("Range can be simplified")
            prev_high = r.high

        self.isEmpty = len(self.ranges) == 0

    def __repr__(self):
        return f"{[str(r) for r in self.ranges]}"

    def __contains__(self, item):
        if isinstance(item, Number):
            for r in self.ranges:
                if item in r:
                    return True
            return False
        if isinstance(item, Range):
            r = self.copy()
            inter = r.intersection(item)
            return inter == item
        raise UnsupportedOperation

    def __eq__(self, other):
        if not isinstance(other,RangeSet):
            return False
        return self.ranges == other.ranges

    def union(self, other):
        if isinstance(other, Range):
            unused = []
            a = other
            while len(self.ranges)>0:
                b = self.ranges.pop(0)
                if b.low>a.high:
                    unused.append(a)
                    unused.append(b)
                    unused+=self.ranges
                    return range_set(unused)
                if a.intersection(b).isEmpty:
                    unused.append(b)
                else:
                    a = a.union(b)
            return range_set(unused+[a])
        if not isinstance(other, RangeSet):
            raise Exception("Can only perform union of Ranges or RangeSets")
        if self.isEmpty:
            return other
        unmatched_sets = []
        a = self.ranges.pop(0)
        while len(other.ranges) > 0 and other.ranges[0].intersection(a).isEmpty and other.ranges[0].high < a.low:
            # This puts in unmatched set all sets to the left of a
            unmatched_sets.append(other.ranges.pop(0))
        while True:
            if len(other.ranges)==0:
                if len(self.ranges) == 0:
                    return range_set(unmatched_sets+[a])
                while len(self.ranges)>0 and not a.intersection(self.ranges[0]).isEmpty:
                    a = a.union(self.ranges.pop(0))
                return range_set(unmatched_sets+[a]+self.ranges)
            if len(self.ranges)==0:
                while len(other.ranges)>0 and not a.intersection(other.ranges[0]).isEmpty:
                    a = a.union(other.ranges.pop(0))
                return range_set(unmatched_sets+[a]+other.ranges)
            if not a.intersection(self.ranges[0]).isEmpty:
                a = a.union(self.ranges.pop(0))
            elif not a.intersection(other.ranges[0]).isEmpty:
                a = a.union(other.ranges.pop(0))
            else:
                unmatched_sets.append(a)
                if other.ranges[0].low < self.ranges[0].low:
                    a = other.ranges.pop(0)
                else:
                    a = self.ranges.pop(0)

    def intersection(self, other):
        if isinstance(other, Range):
            intersect = []
            a = other
            while len(self.ranges) > 0:
                b = self.ranges.pop(0)
                if b.low>a.high:
                    return range_set(intersect)
                i = b.intersection(a)
                if not i.isEmpty:
                    intersect.append(a.intersection(b))
            return range_set(intersect)
        if not isinstance(other, RangeSet):
            raise Exception("Can only perform intersection of Ranges or RangeSets")
        i, j = (0,0)
        intersect = []
        while i < len(self.ranges) and j < len(other.ranges):
            a = self.ranges[i]
            b = other.ranges[j]

            inter = a.intersection(b)
            if not inter.isEmpty:
                intersect.append(inter)

            if a.high < b.high:
                i += 1
            else:
                j += 1
        return range_set(intersect)

    def copy(self):
        return RangeSet(self.ranges)
