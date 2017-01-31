"""Sum of the nth term series."""

def series_sum(n):
    """Return the sum of following series upto nth term(parameter)."""
    seq = [1.00 / (1 + x * 3) for x in range(n)]
    return '%.2f' % sum(seq)
