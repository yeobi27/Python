def convert_to_celsius(fah: float) -> float:
    """화씨와 동일한 섭씨를 반환합니다.

    >>> convert_to_celsius(75)
    23.88888....
    """
    return (fah - 32.0) * 5.0 / 9.0


def above_freezing(cel: float) -> bool:
    """cel가 어는점보다 높으면 True 를 반환
    >>> above_freezing(5.2)
    """
    return cel > 0
