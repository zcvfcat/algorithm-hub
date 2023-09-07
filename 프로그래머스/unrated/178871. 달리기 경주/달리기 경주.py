def solution(players, callings):
    # hash, 시간 복잡도 O(1)
    player_dict = {player: rank for rank, player in enumerate(players)}
    rank_dict = {rank: player for rank, player in enumerate(players)}

    for call in callings:
        rank = player_dict[call]

        player_dict[rank_dict[rank - 1]], player_dict[rank_dict[rank]] = player_dict[rank_dict[rank]], player_dict[rank_dict[rank - 1]]
        rank_dict[rank - 1], rank_dict[rank] = rank_dict[rank], rank_dict[rank - 1]
    
    return [*rank_dict.values()]