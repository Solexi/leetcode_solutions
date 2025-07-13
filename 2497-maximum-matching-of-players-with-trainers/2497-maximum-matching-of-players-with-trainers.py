class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        matches = 0
        player_i = 0
        trainer_j = 0
        
        while player_i < len(players) and trainer_j < len(trainers):
            if players[player_i] <= trainers[trainer_j]:
                matches += 1
                player_i += 1
                trainer_j += 1  
            else:
                trainer_j += 1
        
        return matches
        # players.sort()
        # trainers.sort()
        
        # matches = {}
        # used_trainers = set()
        
        # for player in players:
        #     for trainer in trainers:
        #         if trainer in used_trainers:
        #             continue
        #         if player <= trainer:
        #             matches[player] = trainer
        #             used_trainers.add(trainer)
        #             break
        # return len(matches)
                    