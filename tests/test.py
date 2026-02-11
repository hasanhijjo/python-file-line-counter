import os
from file_counter import file_counter

def run_tests():

    file_path = "testdata/file_with_5_lines.txt"

    if os.path.exists(file_path):
        print("Test 0 (File Exists): PASSED")
    else:
        print("Test 0: FAILED - File does not exist")
        return

    result1 = file_counter.count_lines(file_path)
    assert result1 == 5
    print("Test 1 (Exact Line Count): PASSED")

    result2 = file_counter.count_lines(file_path)
    assert result2 > 0
    print("Test 2 (File Not Empty): PASSED")

    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    run_tests()

