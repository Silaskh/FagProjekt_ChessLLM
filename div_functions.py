def show_board(fen_position,source = r"./pieces"):
    boardImage = fenToImage(
        fen = fen_position,
        squarelength = 100,
        pieceSet=loadPiecesFolder(source),
        darkColor="#D18B47",
        lightColor="#FFCE9E"
    )
    boardImage.show()
    