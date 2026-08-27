"""overlap"""
x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())
if (
    x2 >= x1 + w1  # B อยู่ขวาเกินไป
    or x2 + w2 <= x1  # B อยู่ซ้ายเกินไป
    or y2 >= y1 + h1  # B อยู่สูงเกินไป
    or y2 + h2 <= y1 # B อยู่ต่ำเกินไป
):
    print("no overlapping")
else:
    overlap_w = min(x1 + w1, x2 + w2) - max(x1, x2)
    overlap_h = min(y1 + h1, y2 + h2) - max(y1, y2)
    print(overlap_w * overlap_h)
