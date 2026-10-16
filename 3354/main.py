"""Hint"""

def check(op, val, target):
    """check condition"""
    ops = {
        '==': val == target,
        '>': val > target,
        '<': val < target,
        '>=': val >= target,
        '<=': val <= target,
        '!=': val != target
    }
    return ops.get(op, False)

def main():
    """main"""
    u_op, u_val = input().split()
    t_op, t_val = input().split()
    h_op, h_val = input().split()
    u_val, t_val, h_val = int(u_val), int(t_val), int(h_val)

    h_list = [h for h in range(10) if check(h_op, h, h_val)]
    t_list = [t for t in range(10) if check(t_op, t, t_val)]
    u_list = [u for u in range(10) if check(u_op, u, u_val)]

    for h in h_list:
        for t in t_list:
            for u in u_list:
                print(f"{h}{t}{u}")

if __name__ == '__main__':
    main()
