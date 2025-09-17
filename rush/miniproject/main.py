#!/usr/bin/env python3
from checkmate import validate_board, is_king_checked

if __name__ == "__main__":
    board = [
        "R.......",
        ".K......",
        "..P.....",
        "........",
        "........",
        "........",
        "........",
        "........"
    ]
    
    if validate_board(board):
        is_king_checked(board)
