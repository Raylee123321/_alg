def riemann_n_dim(f, bounds, segments):
    """
    f: 待積分函數
    bounds: 積分範圍，格式為 [(x1_min, x1_max), (x2_min, x2_max), ...]
    segments: 每個維度切幾份
    """
    n = len(bounds)
    dx = [(b - a) / segments for a, b in bounds]
    total_volume = 1
    for d in dx: total_volume *= d

    def compute_sum(dim, current_point):
        if dim == n:
            return f(*current_point)
        
        sum_val = 0
        a, b = bounds[dim]
        # 使用中點法則 (Midpoint Rule) 比較準確
        for i in range(segments):
            point_at_dim = a + (i + 0.5) * dx[dim]
            sum_val += compute_sum(dim + 1, current_point + [point_at_dim])
        return sum_val

    return compute_sum(0, []) * total_volume