import random

class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit
        self.name = str(num)+suit
    
    def __lt__(self, other):
        return self.num < other.num
    
    def __eq__(self, other):
        return self.num == other.num

class Deck:
    def __init__(self, cards):
        self.cards = cards
    def draw(self):
        return self.cards.pop()
    def shuffle(self):
        random.shuffle(self.cards)
    def FillStandardDeck(self):
        self.cards = [Card(num, suit) for num in range(1, 14) for suit in ['S', 'H', 'D', 'C']]
        self.shuffle()
    def add(self, card):
        self.cards.append(card)
    
class Hand(Deck):
    def __init__(self, cards):
        super().__init__(cards)

class Player:
    def __init__(self, hand, cash):
        self.hand = hand
        self.cash = cash
        self.status = "human"
        self.hasFolded = False
        self.currentBet = 0
        self.roundsWon = 0
        self.totalWinnings = 0
    
    def raiseCash(self, amount):
        self.cash -= amount
        self.currentBet += amount
        return amount
    
    def fold(self):
        self.hasFolded = True
    
    def call(self, amount):
        callAmount = amount - self.currentBet
        if callAmount > 0:
            self.cash -= callAmount
            self.currentBet += callAmount
            return callAmount
        return 0
    
    def check(self):
        pass
    
    def resetForNewRound(self):
        """Reset player state for a new round"""
        self.hasFolded = False
        self.currentBet = 0
        self.hand = Hand([])

class Robot(Player):
    def __init__(self, hand, cash):
        super().__init__(hand, cash)
        self.status = "robot"
    
    def willRaise(self, currentBet):
        if random.random() < 0.3:  # 30% chance to raise
            raiseAmount = random.randint(currentBet + 1, min(30, self.cash))
            if raiseAmount <= self.cash:
                return self.raiseCash(raiseAmount)
        return 0
    
    def willCall(self, currentBet):
        if random.random() < 0.6:  # 60% chance to call
            return self.call(currentBet)
        return 0
    
    def willFold(self):
        if random.random() < 0.2:  # 20% chance to fold
            self.fold()
            return True
        return False

class Flop(Deck):
    def __init__(self):
        super().__init__([])
    
    def dealFlop(self, deck):
        """Deal 3 community cards"""
        self.cards = [deck.draw() for _ in range(3)]
        return self.cards
    
    def dealTurn(self, deck):
        """Deal 1 more community card"""
        self.cards.append(deck.draw())
        return self.cards
    
    def dealRiver(self, deck):
        """Deal the final community card"""
        self.cards.append(deck.draw())
        return self.cards

def evaluateHand(holeCards, communityCards):
    """Evaluate a poker hand and return (handRank, handValue, handName)"""
    allCards = holeCards + communityCards
    
    # Count cards by rank and suit
    rankCount = {}
    suitCount = {}
    
    for card in allCards:
        rankCount[card.num] = rankCount.get(card.num, 0) + 1
        suitCount[card.suit] = suitCount.get(card.suit, 0) + 1
    
    # Get sorted ranks for straight checking
    ranks = sorted(rankCount.keys())
    
    # Check for flush
    flush = False
    flushSuit = None
    for suit, count in suitCount.items():
        if count >= 5:
            flush = True
            flushSuit = suit
    
    # Check for straight
    straight = False
    straightHigh = 0
    for i in range(len(ranks) - 4):
        if ranks[i+4] - ranks[i] == 4:
            straight = True
            straightHigh = ranks[i+4]
    
    # Check for straight flush and royal flush
    if flush and straight:
        flushCards = [card for card in allCards if card.suit == flushSuit]
        flushRanks = sorted([card.num for card in flushCards])
        for i in range(len(flushRanks) - 4):
            if flushRanks[i+4] - flushRanks[i] == 4:
                if flushRanks[i+4] == 13:  # Ace high
                    return (10, 13, "Royal Flush")
                else:
                    return (9, flushRanks[i+4], "Straight Flush")
    
    # Check for four of a kind
    for rank, count in rankCount.items():
        if count == 4:
            kicker = max([r for r in ranks if r != rank])
            return (8, rank * 100 + kicker, f"Four of a Kind ({rank}s)")
    
    # Check for full house
    threeRank = None
    twoRank = None
    for rank, count in rankCount.items():
        if count == 3 and threeRank is None:
            threeRank = rank
        elif count >= 2 and twoRank is None:
            twoRank = rank
    
    if threeRank and twoRank:
        return (7, threeRank * 100 + twoRank, f"Full House ({threeRank}s over {twoRank}s)")
    
    # Check for flush
    if flush:
        flushCards = [card for card in allCards if card.suit == flushSuit]
        flushRanks = sorted([card.num for card in flushCards], reverse=True)
        return (6, sum(flushRanks[:5]), f"Flush ({flushSuit})")
    
    # Check for straight
    if straight:
        return (5, straightHigh, "Straight")
    
    # Check for three of a kind
    for rank, count in rankCount.items():
        if count == 3:
            kickers = sorted([r for r in ranks if r != rank], reverse=True)[:2]
            return (4, rank * 10000 + kickers[0] * 100 + kickers[1], f"Three of a Kind ({rank}s)")
    
    # Check for two pair
    pairs = [rank for rank, count in rankCount.items() if count == 2]
    if len(pairs) >= 2:
        pairs.sort(reverse=True)
        kicker = max([r for r in ranks if r not in pairs])
        return (3, pairs[0] * 10000 + pairs[1] * 100 + kicker, f"Two Pair ({pairs[0]}s and {pairs[1]}s)")
    
    # Check for one pair
    for rank, count in rankCount.items():
        if count == 2:
            kickers = sorted([r for r in ranks if r != rank], reverse=True)[:3]
            return (2, rank * 1000000 + sum([k * (100 ** i) for i, k in enumerate(kickers)]), f"One Pair ({rank}s)")
    
    # High card
    highCards = sorted(ranks, reverse=True)[:5]
    return (1, sum([c * (100 ** i) for i, c in enumerate(highCards)]), f"High Card ({highCards[0]})")

def determineWinner(players, communityCards):
    """Determine the winner(s) based on hand evaluation"""
    activePlayers = [p for p in players if not p.hasFolded]
    
    if len(activePlayers) == 1:
        return [activePlayers[0]]
    
    # Evaluate each player's hand
    playerHands = []
    for player in activePlayers:
        handRank, handValue, handName = evaluateHand(player.hand.cards, communityCards)
        playerHands.append((player, handRank, handValue, handName))
        print(f"Player {players.index(player) + 1} ({player.status}): {handName}")
    
    # Sort by hand rank (higher is better), then by hand value
    playerHands.sort(key=lambda x: (x[1], x[2]), reverse=True)
    
    # Find winners (players with the same best hand)
    bestRank = playerHands[0][1]
    bestValue = playerHands[0][2]
    winners = []
    
    for player, rank, value, name in playerHands:
        if rank == bestRank and value == bestValue:
            winners.append(player)
    
    return winners

def getPlayerAction(player, currentBet, pot, communityCards=None):
    """Get action from a player (human or robot)"""
    if player.hasFolded:
        return "folded", 0
    
    if player.status == "human":
        print(f"\nYour Hand: {player.hand.cards[0].name} {player.hand.cards[1].name}")
        if communityCards:
            print(f"Community Cards: {' '.join([card.name for card in communityCards])}")
        print(f"Your Cash: ${player.cash}, Current Bet: ${player.currentBet}")
        print(f"Pot: ${pot}, To Call: ${currentBet - player.currentBet}")
        
        if currentBet > player.currentBet:
            action = input("Action (call/fold/raise): ").lower()
            if "raise" in action:
                try:
                    # Extract amount from "raise X" format
                    amount = int(action.replace("raise", "").strip())
                    if amount > currentBet and amount <= player.cash:
                        return "raise", player.raiseCash(amount)
                    else:
                        print("Invalid raise amount. Calling instead.")
                        return "call", player.call(currentBet)
                except ValueError:
                    print("Invalid raise format. Calling instead.")
                    return "call", player.call(currentBet)
            elif action == "call":
                return "call", player.call(currentBet)
            elif action == "fold":
                player.fold()
                return "fold", 0
            else:
                print("Invalid action. Folding.")
                player.fold()
                return "fold", 0
        else:
            action = input("Action (check/fold/raise): ").lower()
            if action == "check":
                return "check", 0
            elif "raise" in action:
                try:
                    amount = int(action.replace("raise", "").strip())
                    if amount > currentBet and amount <= player.cash:
                        return "raise", player.raiseCash(amount)
                    else:
                        print("Invalid raise amount. Checking instead.")
                        return "check", 0
                except ValueError:
                    print("Invalid raise format. Checking instead.")
                    return "check", 0
            elif action == "fold":
                player.fold()
                return "fold", 0
            else:
                print("Invalid action. Checking.")
                return "check", 0
    else:
        # Robot player logic
        if currentBet > player.currentBet:
            # Robot needs to call, raise, or fold
            if player.willFold():
                return "fold", 0
            elif random.random() < 0.3:  # 30% chance to raise
                raiseAmount = random.randint(currentBet + 1, min(30, player.cash))
                if raiseAmount <= player.cash:
                    return "raise", player.raiseCash(raiseAmount)
            else:
                return "call", player.call(currentBet)
        else:
            # Robot can check or raise
            if random.random() < 0.2:  # 20% chance to raise
                raiseAmount = random.randint(1, min(20, player.cash))
                if raiseAmount <= player.cash:
                    return "raise", player.raiseCash(raiseAmount)
            return "check", 0

def bettingRound(players, pot, currentBet, roundName, communityCards=None):
    """Handle a complete betting round"""
    print(f"\n=== {roundName} ===")
    if communityCards:
        print(f"Community Cards: {' '.join([card.name for card in communityCards])}")
    print(f"Pot: ${pot}, Current Bet: ${currentBet}")
    
    # Reset current bets for new round
    for player in players:
        if not player.hasFolded:
            player.currentBet = 0
    
    # Each player takes action
    for i, player in enumerate(players):
        if player.hasFolded:
            continue
            
        print(f"\nPlayer {i+1}'s turn ({player.status})")
        action, amount = getPlayerAction(player, currentBet, pot, communityCards)
        
        if action == "raise":
            print(f"Player {i+1} raises to ${amount}")
            currentBet = player.currentBet
            pot += amount
            
            # Ask all other players for their action after a raise
            print(f"\n--- Other players must respond to the raise ---")
            for j, otherPlayer in enumerate(players):
                if j != i and not otherPlayer.hasFolded:
                    print(f"\nPlayer {j+1}'s response ({otherPlayer.status})")
                    otherAction, otherAmount = getPlayerAction(otherPlayer, currentBet, pot, communityCards)
                    
                    if otherAction == "raise":
                        print(f"Player {j+1} re-raises to ${otherAmount}")
                        currentBet = otherPlayer.currentBet
                        pot += otherAmount
                        # This would trigger another round of responses, but for simplicity we'll continue
                    elif otherAction == "call":
                        print(f"Player {j+1} calls ${otherAmount}")
                        pot += otherAmount
                    elif otherAction == "fold":
                        print(f"Player {j+1} folds")
                    elif otherAction == "check":
                        print(f"Player {j+1} checks")
            
        elif action == "call":
            print(f"Player {i+1} calls ${amount}")
            pot += amount
        elif action == "fold":
            print(f"Player {i+1} folds")
        elif action == "check":
            print(f"Player {i+1} checks")
    
    return pot, currentBet

def playOneRound(players, roundNumber):
    """Play one complete poker round"""
    print(f"\n{'='*50}")
    print(f"ROUND {roundNumber}")
    print(f"{'='*50}")
    
    # Reset all players for new round
    for player in players:
        player.resetForNewRound()
    
    # Create new deck and deal cards
    deck = Deck([])
    deck.FillStandardDeck()
    
    # Deal cards and collect blinds
    smallBlind = 5
    for player in players:
        player.cash -= smallBlind
        player.currentBet = smallBlind
        for i in range(2):
            player.hand.add(deck.draw())
    
    playersStillIn = [p for p in players if not p.hasFolded]
    pot = smallBlind * len(players)
    currentBet = smallBlind
    
    print(f"Round started! Pot: ${pot}")
    print("Dealing hole cards...")
    
    # Pre-flop betting round
    pot, currentBet = bettingRound(players, pot, currentBet, "Pre-Flop")
    
    # Remove folded players
    playersStillIn = [p for p in players if not p.hasFolded]
    
    if len(playersStillIn) > 1:
        # Deal the flop
        flop = Flop()
        communityCards = flop.dealFlop(deck)
        print(f"\n*** FLOP ***")
        print(f"Community Cards: {' '.join([card.name for card in communityCards])}")
        
        # Flop betting round
        pot, currentBet = bettingRound(playersStillIn, pot, 0, "Flop", communityCards)
        
        # Remove folded players
        playersStillIn = [p for p in playersStillIn if not p.hasFolded]
        
        if len(playersStillIn) > 1:
            # Deal the turn
            communityCards = flop.dealTurn(deck)
            print(f"\n*** TURN ***")
            print(f"Community Cards: {' '.join([card.name for card in communityCards])}")
            
            # Turn betting round
            pot, currentBet = bettingRound(playersStillIn, pot, 0, "Turn", communityCards)
            
            # Remove folded players
            playersStillIn = [p for p in playersStillIn if not p.hasFolded]
            
            if len(playersStillIn) > 1:
                # Deal the river
                communityCards = flop.dealRiver(deck)
                print(f"\n*** RIVER ***")
                print(f"Community Cards: {' '.join([card.name for card in communityCards])}")
                
                # River betting round
                pot, currentBet = bettingRound(playersStillIn, pot, 0, "River", communityCards)
                
                # Remove folded players
                playersStillIn = [p for p in playersStillIn if not p.hasFolded]
    
    # Determine winner
    if len(playersStillIn) == 1:
        winner = playersStillIn[0]
        print(f"\nPlayer {players.index(winner) + 1} ({winner.status}) wins ${pot}!")
        winner.cash += pot
        winner.roundsWon += 1
        winner.totalWinnings += pot
    else:
        print(f"\n*** SHOWDOWN ***")
        print(f"Community Cards: {' '.join([card.name for card in communityCards])}")
        
        # Determine winner(s)
        winners = determineWinner(playersStillIn, communityCards)
        
        if len(winners) == 1:
            winner = winners[0]
            print(f"\nPlayer {players.index(winner) + 1} ({winner.status}) wins ${pot}!")
            winner.cash += pot
            winner.roundsWon += 1
            winner.totalWinnings += pot
        else:
            # Split pot among winners
            splitAmount = pot // len(winners)
            print(f"\nTie! {len(winners)} players split the pot of ${pot}")
            for winner in winners:
                winner.cash += splitAmount
                winner.roundsWon += 1
                winner.totalWinnings += splitAmount
                print(f"Player {players.index(winner) + 1} ({winner.status}) gets ${splitAmount}")
    
    # Show round results
    print(f"\n--- Round {roundNumber} Results ---")
    for i, player in enumerate(players):
        status = "Folded" if player.hasFolded else "Active"
        print(f"Player {i+1} ({player.status}): ${player.cash} - {status}")
    
    return players

def showGameStats(players, roundNumber):
    """Display current game statistics"""
    print(f"\n{'='*60}")
    print(f"GAME STATISTICS (After Round {roundNumber})")
    print(f"{'='*60}")
    print(f"{'Player':<8} {'Type':<8} {'Cash':<8} {'Rounds Won':<12} {'Total Won':<12}")
    print(f"{'-'*60}")
    
    for i, player in enumerate(players):
        print(f"{'Player '+str(i+1):<8} {player.status:<8} ${player.cash:<7} {player.roundsWon:<12} ${player.totalWinnings:<11}")
    
    # Find richest and poorest players
    richest = max(players, key=lambda p: p.cash)
    poorest = min(players, key=lambda p: p.cash)
    
    print(f"\nRichest: Player {players.index(richest) + 1} (${richest.cash})")
    print(f"Poorest: Player {players.index(poorest) + 1} (${poorest.cash})")
    
    # Check if game should continue
    activePlayers = [p for p in players if p.cash >= 5]  # Need at least $5 for small blind
    if len(activePlayers) < 2:
        print(f"\n⚠️  GAME OVER: Only {len(activePlayers)} player(s) can afford to play!")
        return False
    
    return True

def main():
    numPlayers = int(input("Number of Players: "))
    players = []
    
    # Create players (first player is human, rest are robots)
    for i in range(numPlayers):
        if i == 0:
            players.append(Player(Hand([]), 1000))
        else:
            players.append(Robot(Hand([]), 1000))
    
    print(f"\nGame started with {numPlayers} players!")
    print("Each player starts with $1000")
    print("Small blind: $5 per round")
    print("Game continues until someone runs out of money!")
    
    roundNumber = 1
    
    while True:
        # Play one round
        players = playOneRound(players, roundNumber)
        
        # Show game statistics
        if not showGameStats(players, roundNumber):
            break
        
        # Ask if player wants to continue (only for human player)
        if players[0].cash >= 5:  # Human player can still play
            continue_game = input(f"\nContinue to next round? (y/n): ").lower()
            if continue_game != 'y':
                print("\nGame ended by player choice.")
                break
        else:
            print(f"\nPlayer 1 (human) is out of money!")
            break
        
        roundNumber += 1
    
    # Final game results
    print(f"\n{'='*60}")
    print("FINAL GAME RESULTS")
    print(f"{'='*60}")
    
    # Sort players by final cash amount
    finalRanking = sorted(players, key=lambda p: p.cash, reverse=True)
    
    for i, player in enumerate(finalRanking):
        print(f"{i+1}. Player {players.index(player) + 1} ({player.status}): ${player.cash} - {player.roundsWon} rounds won")
    
    print(f"\nTotal rounds played: {roundNumber}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()



