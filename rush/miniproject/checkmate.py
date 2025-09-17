def validate_board(board):

    n = len(board)

    if not all(len(row) == n for row in board):
        print("Board is not square")
        return False

    king_count = sum(row.count('K') for row in board)
    if king_count == 0:
        print("No King on the board")
        return False
    elif king_count > 1:
        print("Must have 1 King on the board")
        return False

    piece_counts = {
        'P': 0,
        'B': 0,
        'R': 0,
        'Q': 0,
        'K': 0
    }

    for row in board:
        for cell in row:
            if cell in piece_counts:
                piece_counts[cell] += 1
            elif cell != '.':
                print("Only P, B, R, Q, K, and . are allowed.")
                return False

    if piece_counts['Q'] > 1:
        print("There must be exactly one Queen or fewer.")
        return False
    if piece_counts['B'] > 2:
        print("There must be exactly two Bishops or fewer.")
        return False
    if piece_counts['P'] > 8:
        print("There must be exactly eight Pawns or fewer.")
        return False
    if piece_counts['R'] > 2:
        print("There must be exactly two Rooks or fewer.")
        return False

    return True

def is_king_checked(board):
    
    n = len(board)

    king_pos = None
    for i, row in enumerate(board):
        if 'K' in row:
            king_pos = (i, row.index('K'))
            break

    kx, ky = king_pos

    def is_in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    pawn_dirs = [(1, 1), (1, -1)]
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queen_dirs = bishop_dirs + rook_dirs

    for dx, dy in pawn_dirs:
        nx, ny = kx + dx, ky + dy
        if is_in_bounds(nx, ny) and board[nx][ny] == 'P':
            print("Success")
            return

    for piece, directions in [('B', bishop_dirs), ('R', rook_dirs), ('Q', queen_dirs)]:
        for dx, dy in directions:
            x, y = kx, ky
            while True:
                x, y = x + dx, y + dy
                if not is_in_bounds(x, y):
                    break
                if board[x][y] == piece:
                    print("Success")
                    return
                elif board[x][y] != '.':
                    break

    print("Fail")