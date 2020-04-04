import random
import discord
import emoji
class TicTacToe:
    def __init__(self, message):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.PLAYER_ICON = "X"
        self.COMP_ICON = "O"
        self.EMOJIS = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

        self.DICT_OF_EMOJIS = {k: v for k,v in zip(self.EMOJIS, range(1, 10))} # creating emoji to number dict
        self.DICT_OF_NUM = {v: k for k, v in self.DICT_OF_EMOJIS.items()} # inverted DICT_OF_EMOJIS
        self.PLAYER = message.author
        self.message = message
        self.game_over = False


    async def create_board(self): #creates the board
        message_to_send = "```\n" #first line to start a code block
        for row in self.board:
            message_to_send += " "
            for spot in row:
                message_to_send += spot + "     "
            message_to_send += "\n" + "---   "*3 + "\n"
        message_to_send += "```" # last line to end a codeblock
        self.message = await self.message.channel.send(message_to_send)

        reactions = []
        for row, col in self.get_possible_moves():
            reaction = self.EMOJIS[row*3 + col]
            reactions.append(reaction)
            await self.message.add_reaction(reaction)


    async def do_move(self, reaction):
        if self.game_over:
            return
        num = self.DICT_OF_EMOJIS[reaction.emoji] # turns num to emoji
        row = (num-1) // 3 # calculates row position
        col = (num-1) % 3  # calculates col position

        if self.is_move_valid(row, col):
            self.board[row][col] = self.PLAYER_ICON
            await self.update_board()
        else: # move was not valid, so do nothing
            return

        if self.check_win(): #if player won
            await self.message.channel.send(f"@{self.PLAYER} won ):")
            await self.message.clear_reactions()
            self.game_over = True
            return

        if ' ' not in [j for sub in self.board for j in sub]: # if no spots left
            await self.message.channel.send("Nobody won ):")
            await self.message.clear_reactions()
            self.game_over = True
            return

        else:
            c_row, c_col = random.choice(self.get_possible_moves()) # get comp choice
            self.board[c_row][c_col] = self.COMP_ICON
            await self.update_board()
            if self.check_win(): # if computer wins
                await self.message.channel.send("Yay! I won.")
                self.game_over = True

        await self.update_reactions()


    async def update_board(self):
        message_to_send = "```\n" # to start a code block (for monospace font)
        for row in self.board:
            message_to_send += " "
            for spot in row:
                message_to_send += spot + "     "
            message_to_send += "\n" + "---   "*3 + "\n"
        message_to_send += "```" # to end a codeblock
        await self.message.edit(content=message_to_send)


    async def update_reactions(self):
        reactions = list()
        for row, col in self.get_possible_moves():
            reaction = self.EMOJIS[row*3 + col]
            reactions.append(reaction)

        # clears impossible moves from reactions
        not_possible_moves = [num for num in self.EMOJIS if num not in reactions]  
        for reaction in not_possible_moves:
            await self.message.clear_reaction(reaction)


    def is_move_valid(self, row, col):
        if (row, col) in self.get_possible_moves():
            return True
        return False


    def get_possible_moves(self):
        possible_moves = list()
        for row in range(3):
            for col in range(3):
                if self.board[row][col] != "X" and self.board[row][col] != "O":
                    possible_moves.append((row, col))
        return possible_moves


    def check_win(self):
        for row in self.board: #check for horizontal win
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return True

        #checks for vertical win
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] \
               and self.board[0][col] != ' ':
                return True
        
        #checks for diagonal win 
        if self.board[0][0] == self.board[1][1] == self.board[2][2] \
           and self.board[0][0] != ' ':
            return True

        #checks for other diagonal win
        if self.board[2][0] == self.board[1][1] == self.board[0][2] \
           and self.board[2][0] != ' ':
            return True
        return False
