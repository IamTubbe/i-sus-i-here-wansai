#!/usr/bin/env python3
import sys
from checkmate import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file1.chess> [file2.chess ...] | cat -e$")
        sys.exit(1)

    for file_path in sys.argv[1:]:
        board = read_board(file_path)
        print(process_board(board))