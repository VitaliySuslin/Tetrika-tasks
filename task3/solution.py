from typing import Dict, List


def appearance(intervals: Dict[str, List[int]]) -> int:
    lesson_start, lesson_end = intervals["lesson"]

    pupil_intervals = parse_intervals(intervals["pupil"])
    tutor_intervals = parse_intervals(intervals["tutor"])

    pupil_merged = merge_and_clip(pupil_intervals, lesson_start, lesson_end)
    tutor_merged = merge_and_clip(tutor_intervals, lesson_start, lesson_end)

    overlaps = find_overlaps(pupil_merged, tutor_merged)

    total_overlap = sum(end - start for start, end in overlaps)

    return total_overlap


def parse_intervals(timestamps: List[int]) -> List[tuple]:
    return [(timestamps[i], timestamps[i + 1]) for i in range(0, len(timestamps), 2)]


def merge_and_clip(intervals: List[tuple], start_limit: int, end_limit: int) -> List[tuple]:
    if not intervals:
        return []

    sorted_intervals = sorted(intervals)

    merged = []
    current_start, current_end = sorted_intervals[0]

    for start, end in sorted_intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    clipped = []
    for start, end in merged:
        clip_start = max(start, start_limit)
        clip_end = min(end, end_limit)
        if clip_start < clip_end:
            clipped.append((clip_start, clip_end))

    return clipped


def find_overlaps(a: List[tuple], b: List[tuple]) -> List[tuple]:
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        start_a, end_a = a[i]
        start_b, end_b = b[j]

        overlap_start = max(start_a, start_b)
        overlap_end = min(end_a, end_b)

        if overlap_start < overlap_end:
            result.append((overlap_start, overlap_end))

        if end_a < end_b:
            i += 1
        else:
            j += 1

    return result