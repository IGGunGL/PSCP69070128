"""มาเป็นทีม"""

def main():
    """main"""
    try:
        first_line = input().split()
        if len(first_line) != 2:
            print("Data Incorrect")
            return

        n = int(first_line[0])
        m = int(first_line[1])
        if not (1 <= n <= 10 and 1 <= m <= 20):
            print("Data Incorrect")
            return

        teams = []
        for _ in range(n):
            row_parts = input().split()
            if len(row_parts) != m:
                print("Data Incorrect")
                return
            row = []
            for val in row_parts:
                score = int(val)
                if score < 0 or score > 100:
                    print("Data Incorrect")
                    return
                row.append(score)
            teams.append(row)

        total_score = 0
        for i in range(n):
            scores = teams[i]
            avg = sum(scores) / m
            max_val = max(scores)
            total_score += sum(scores)
            print(f"Team {i + 1}: Average = {avg:.2f}, Max = {max_val}")

        print(f"Total Score of All Teams = {total_score}")
    except (ValueError, EOFError):
        print("Data Incorrect")

if __name__ == '__main__':
    main()
