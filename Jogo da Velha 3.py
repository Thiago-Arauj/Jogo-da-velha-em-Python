# Jogo da Velha

Table = [['0/0', '0/1', '0/2'],
         ['1/0', '1/1', '1/2'],
         ['2/0', '2/1', '2/2']]

Char = (" X ", " O ")

Historico = []

Modo_de_Jogo = int(input('''
   =======================
    Como deseja jogar?
    [1] Single Player
    [2] Multiplayer
    [0] Não quero jogar
   =======================
     '''))

# ============================================================================
#  Acima definimos variavéis importantes para o jogo num geral
# =============================================================================


def CheckWin2P (Table):

    if Table[0][0] == Table[0][1] == Table[0][2]:
        Modo_de_Jogo = 3

    elif Table[1][0] == Table[1][1] == Table[1][2]:
        Modo_de_Jogo = 3

    elif Table[2][0] == Table[2][1] == Table[2][2]:
        Modo_de_Jogo = 3

    elif Table[0][0] == Table[1][0] == Table[2][0]:
        Modo_de_Jogo = 3

    elif Table[0][1] == Table[1][1] == Table[2][1]:
        Modo_de_Jogo = 3

    elif Table[0][2] == Table[1][2] == Table[2][2]:
        Modo_de_Jogo = 3

    elif Table[0][0] == Table[1][1] == Table[2][2]:
        Modo_de_Jogo = 3

    elif Table[0][2] == Table[1][1] == Table[2][0]:
        Modo_de_Jogo = 3

    else:
        Modo_de_Jogo = 2

    return Modo_de_Jogo

# ==============================================================================
# Acima definimos a função que checa se o jogo tem um vencedor ou se foi empate
# caso nenhum dos dois seja verdadeiro o jogo segue
# ==============================================================================
    

def SelecChar (Char):
    P1_Char = input("X ou O? ").upper()
    P1_Char = P1_Char.center(3, " ")

    if P1_Char == Char[0]:
        P2_Char = Char[1]
    elif P1_Char == Char[1]:
        P2_Char = Char[0]

    return P1_Char, P2_Char


# ===========================================================================
# Acima temos a função que define quem será X ou O
# ===========================================================================

def Jogada1 (Table, P2_Char):

    if Table[0][0] not in Char:
        Table[0][0] = P2_Char

    elif Table[2][2] not in Char:
        Table [2][2] = P2_Char

    elif Table[2][0] not in Char:
        Table [2][0] = P2_Char

    elif Table[0][2] not in Char:
        Table [0][2] = P2_Char
    
    return Table

# ===========================================================================
# Acima temos a função que define a primeira jogada do Bot, onde ele
# vai conferir se pode jogar nos cantos
# ===========================================================================
# Abaixo temos as funções que irão checar todas as posições de P1 para a 
# segunda jogada do bot, buscando impedir uma vitória do jogador.
# ===========================================================================
def ChecarColunas(Table, P1_Char, P2_Char):

    coluna = 0

    while coluna < 3:
        qntd_P1 = 0
        qntd_P2 = 0

        for i in range(3):
            if Table[i][coluna] == P2_Char:
                qntd_P2 += 1
            elif Table[i][coluna] == P1_Char:
                qntd_P1 += 1

        if qntd_P1 == 2 and qntd_P2 == 0:
            for i in range(3):
                if Table[i][coluna] not in Char:
                    Table[i][coluna] = P2_Char
        elif qntd_P1 == 2 and qntd_P2 == 1:
            Jogada1(Table, P2_Char)

        coluna += 1
    
    return Table

def ChecarLinha (Table, P1_Char, P2_Char):

    linha = 0

    while linha < 3:
        qntd_P1 = 0
        qntd_P2 = 0

        for i in range(3):
            if Table[linha][i] == P2_Char:
                qntd_P2 += 1
            elif Table[linha][i] == P1_Char:
                qntd_P1 += 1

        if qntd_P1 == 2 and qntd_P2 == 0:
            for i in range(3):
                if Table[linha][i] not in Char:
                    Table[linha][i] = P2_Char
        elif qntd_P1 == 2 and qntd_P2 == 1:
            Jogada1(Table, P2_Char)

        linha += 1
    
    return Table

def ChecarDiagonais (Table, P1_Char, P2_Char):

    qntd_P1 = 0
    qntd_P2 = 0

    # Checa a diagonal 1

    for i in range(3):
        if Table[i][i] == P1_Char:
            qntd_P1 += 1
        elif Table[i][i] == P2_Char:
            qntd_P2 += 1
    
    if qntd_P1 == 2 and qntd_P2 == 0:

        if Table[0][0] not in Char:
            Table[0][0] = P2_Char

        elif Table[1][1] not in Char:
            Table[1][1] = P2_Char

        elif Table[2][2] not in Char:
            Table[2][2] = P2_Char
            
    # Checa a diagonal 2

    elif Table[0][2] == Table[1][1] or Table[1][1] == Table[2][0] or Table[0][2] == Table[2][0]:
         
        if Table[0][2] not in Char:
            Table[0][2] = P2_Char

        elif Table[1][1] not in Char:
            Table[1][1] = P2_Char

        elif Table[2][0] not in Char:
            Table[2][0] = P2_Char
        
    elif qntd_P1 == 2 and qntd_P2 == 1:
            if Table[0][0] not in Char:
                Table[0][0] = P2_Char

            elif Table[1][1] not in Char:
                Table[1][1] = P2_Char

            elif Table[2][2] not in Char:
                Table [2][2] = P2_Char

            elif Table[2][0] not in Char:
                Table [2][0] = P2_Char

            elif Table[0][2] not in Char:
                Table [0][2] = P2_Char

    return Table

def Jogada2 (Table, P1_Char, P2_Char):

    # Função criada pra conter as outras 3 e melhorar visualização do código
    ChecarLinha(Table, P1_Char, P2_Char)   
    ChecarColunas(Table, P1_Char, P2_Char)
    ChecarDiagonais(Table, P1_Char, P2_Char)

    return Table

# ===========================================================================
# Abaixo temos a terceira jogada do bot, onde ele tentará encerrar o 
# jogo
# ===========================================================================

def FinalizarJogoC (Table, P1_Char, P2_Char):
    coluna = 0

    while coluna < 3:
        qntd_P1 = 0
        qntd_P2 = 0

        for i in range(3):
            if Table[i][coluna] == P2_Char:
                qntd_P2 += 1
            elif Table[i][coluna] == P1_Char:
                qntd_P1 += 1

        if qntd_P2 == 2 and qntd_P1 == 0:
            for i in range(3):
                if Table[i][coluna] not in Char:
                    Table[i][coluna] = P2_Char
        elif qntd_P2 == 2 and qntd_P1 == 1:
            Jogada1(Table, P2_Char)

        coluna += 1
    
    return Table

def FinalizarJogoL (Table, P1_Char, P2_Char):
    linha = 0

    while linha < 3:
        qntd_P1 = 0
        qntd_P2 = 0
        
        for i in range(3):
            if Table[linha][i] == P2_Char:
                qntd_P2 += 1
            elif Table[linha][i] == P1_Char:
                qntd_P1 += 1

        if qntd_P2 == 2 and qntd_P1 == 0:
            for i in range(3):
                if Table[linha][i] not in Char:
                    Table[linha][i] = P2_Char
        elif qntd_P2 == 2 and qntd_P1 == 1:
            Jogada1(Table, P2_Char)

        linha += 1
    
    return Table

def FinalizarJogoD (Table, P1_Char, P2_Char):
    qntd_P1 = 0
    qntd_P2 = 0

    # Checa a diagonal 1

    for i in range(3):
        if Table[i][i] == P1_Char:
            qntd_P1 += 1
        elif Table[i][i] == P2_Char:
            qntd_P2 += 1
    
    if qntd_P2 == 2 and qntd_P1 == 0:

        if Table[i][i] not in Char:
            Table[i][i] = P2_Char
        
        return Table, True
            
    elif qntd_P2 == 2 and qntd_P1 == 1:
        if Table[0][0] not in Char:
            Table[0][0] = P2_Char

        elif Table[1][1] not in Char:
            Table[1][1] = P2_Char

        elif Table[2][2] not in Char:
            Table [2][2] = P2_Char

        elif Table[2][0] not in Char:
            Table [2][0] = P2_Char

        elif Table[0][2] not in Char:
            Table [0][2] = P2_Char
            
        elif Table[0][1] not in Char:
            Table[0][1] = P2_Char

        elif Table[2][1] not in Char:
            Table[2][1] = P2_Char
            
        elif Table[1][0] not in Char:
            Table[1][0] = P2_Char
            
        elif Table[1][2] not in Char:
            Table[1][2] = P2_Char
        
        return Table, True

    # Checa a diagonal 2

    elif Table[0][2] == Table[1][1] or Table[1][1] == Table[2][0] or Table[0][2] == Table[2][0]:
         
        if Table[0][2] not in Char:
            Table[0][2] = P2_Char

        elif Table[1][1] not in Char:
            Table[1][1] = P2_Char

        elif Table[2][0] not in Char:
            Table[2][0] = P2_Char
        
        return Table, True
    
    else:
        return False

def Jogada3 (Table, P1_Char, P2_Char):

    FinalizarJogoC(Table, P1_Char, P2_Char)
    FinalizarJogoL(Table, P1_Char, P2_Char)
    FinalizarJogoD(Table, P1_Char, P2_Char)

    return Table
# ===========================================================================
# A função de finalizar o jogo usa a mesma lógica da segunda jogada
# porém ela checa por posições ocupadas pelo P2 pra tomar sua decisão
# ===========================================================================
# Aqui estão as jogadas dos jogadores humanos
# ===========================================================================

def MovePlayer1 (Table, P1_Char):

    TryAgain = 1
    
    while TryAgain > 0:

        Linha, Coluna = (input(f'''
    Jogador 1, digite o número da casa onde quer jogar
    da forma como está na tela:
   =============
    {Table[0][0]} {Table[0][1]} {Table[0][2]}
    {Table[1][0]} {Table[1][1]} {Table[1][2]}
    {Table[2][0]} {Table[2][1]} {Table[2][2]}
   =============
        ''').split("/"))
        
        Linha = int(Linha)
        Coluna = int(Coluna)
        
        if Table[Linha][Coluna] not in Char:
            Table[Linha][Coluna] = P1_Char
            TryAgain = 0
        else:
            TryAgain = 1
            print("Você selecionou uma casa inválida, tente de novo!")
    
    return Table

def MovePlayer2 (Table, P2_Char):
    
    TryAgain = 1
    
    while TryAgain > 0:

        Linha, Coluna = (input(f'''
    Jogador 2, digite o número da casa onde quer jogar
    da forma como está na tela:
   =============
    {Table[0][0]} {Table[0][1]} {Table[0][2]}
    {Table[1][0]} {Table[1][1]} {Table[1][2]}
    {Table[2][0]} {Table[2][1]} {Table[2][2]}
   =============
        ''').split("/"))
        
        Linha = int(Linha)
        Coluna = int(Coluna)
        
        if Table[Linha][Coluna] not in Char:
            Table[Linha][Coluna] = P2_Char
            TryAgain = 0
        else:
            TryAgain = 1
            print("Você selecionou uma casa inválida, tente de novo!")

    return Table

# ===========================================================================
# Acima temos o movimento dos dois jogadores para o multiplayer
# ============================================================================ 
# Abaixo temos o loop principal
# ===========================================================================

while Modo_de_Jogo > 0:
    Table = [['0/0', '0/1', '0/2'],
             ['1/0', '1/1', '1/2'],
             ['2/0', '2/1', '2/2']]
    
    P1_Char, P2_Char = SelecChar(Char)

    Play_Again = 1

    Verifica = []

    if Modo_de_Jogo == 1:
        MovePlayer1(Table, P1_Char)
        Jogada1(Table, P2_Char)
        MovePlayer1(Table, P1_Char)
        Jogada2(Table, P1_Char, P2_Char)

        while Modo_de_Jogo == 1:
            MovePlayer1(Table, P1_Char)
            Modo_de_Jogo = CheckWin2P(Table)
            if Modo_de_Jogo == 3:
                Historico.append("P1")
                break  

            Jogada3(Table, P1_Char, P2_Char)
            Modo_de_Jogo = CheckWin2P(Table)
            if Modo_de_Jogo == 3:
                Historico.append("P2 - Bot")
                break     

    
    while Modo_de_Jogo == 2:
        MovePlayer1(Table, P1_Char)
        Modo_de_Jogo = CheckWin2P(Table)
        if Modo_de_Jogo == 3:
            Historico.append("P1")
            break
        MovePlayer2(Table, P2_Char)
        Modo_de_Jogo = CheckWin2P(Table)
        if Modo_de_Jogo == 3:
            Historico.append("P2")
            break
    
    while Modo_de_Jogo == 3:
        a = 0
        b = 0

        for i in range(3):
            a += Table[i].count(' X ')
            b += Table[i].count(' O ')
        
        if a + b == 9:
            print("Deu velha!")
            Historico.append("Velha")
        else:
            print(f"O vencedor é {Historico[-1]}")
            print(f'''
    =============
        {Table[0][0]} {Table[0][1]} {Table[0][2]}
        {Table[1][0]} {Table[1][1]} {Table[1][2]}
        {Table[2][0]} {Table[2][1]} {Table[2][2]}
    =============
            ''')

        Checar_hist = int(input(f'''
   =======================
    Gostaria de ver o
    placar até agora?
    [1] Sim
    [0] Não
   =======================
     '''))
        
        if Checar_hist == 1:
            ordem = 1
            for nome in Historico:
                print(f"Partida {ordem}: O vencedor foi {nome}")
                ordem += 1

        Play_Again = int(input('''
   =======================
    Deseja jogar de novo?
    [1] Sim
    [0] Não
   =======================
       '''))

        if Play_Again ==  1:
            Modo_de_Jogo = int(input('''
   =======================
    Como deseja jogar?
    [1] Single Player
    [2] Multiplayer
    [0] Não quero jogar
   =======================
        '''))
            break
        elif Play_Again == 0:
            print("Tudo bem! Foi um bom jogo.")
            Modo_de_Jogo = 0
            break