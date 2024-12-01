def dictatorship(preferences, agent):
    """
    Returns the top choice of the specified agent.
    
    Args:
        preferences: Preference object with candidates(), voters(), get_preference()
        agent: Integer representing the dictator agent
    
    Returns:
        Integer representing the winning alternative
    
    Raises:
        ValueError: If agent is not a valid voter
    """
    voters = preferences.voters()
    if agent not in voters:
        raise ValueError("Invalid agent")
    
    candidates = preferences.candidates()
    for candidate in candidates:
        if preferences.get_preference(candidate, agent) == 0:
            return candidate


def scoring_rule(preferences, score_vector, tie_break_agent):
    """
    Applies scoring rule using provided score vector.
    
    Args:
        preferences: Preference object with candidates(), voters(), get_preference()
        score_vector: List of scores for each rank position
        tie_break_agent: Integer representing the tie-breaking agent
    
    Returns:
        Integer representing the winning alternative
    
    Raises:
        ValueError: If score_vector length doesn't match number of candidates
    """
    candidates = preferences.candidates()
    if len(score_vector) != len(candidates):
        raise ValueError("Score vector length must match number of candidates")
    
    scores = {candidate: 0 for candidate in candidates}
    
    for voter in preferences.voters():
        for candidate in candidates:
            rank = preferences.get_preference(candidate, voter)
            scores[candidate] += score_vector[rank]
    
    max_score = max(scores.values())
    winners = [c for c, s in scores.items() if s == max_score]
    
    if len(winners) == 1:
        return winners[0]
    
    best_rank = len(candidates)
    chosen_winner = winners[0]
    for winner in winners:
        rank = preferences.get_preference(winner, tie_break_agent)
        if rank < best_rank:
            best_rank = rank
            chosen_winner = winner
    
    return chosen_winner


def plurality(preferences, tie_break):
    """
    Implements plurality voting rule.
    
    Args:
        preferences: Preference object with candidates(), voters(), get_preference()
        tie_break: Integer representing the tie-breaking agent
    
    Returns:
        Integer representing the winning alternative
    """
    candidates = preferences.candidates()
    first_place_votes = {candidate: 0 for candidate in candidates}
    
    for voter in preferences.voters():
        for candidate in candidates:
            if preferences.get_preference(candidate, voter) == 0:
                first_place_votes[candidate] += 1
                break
    
    max_votes = max(first_place_votes.values())
    winners = [c for c, v in first_place_votes.items() if v == max_votes]
    
    if len(winners) == 1:
        return winners[0]
    
    best_rank = len(candidates)
    chosen_winner = winners[0]
    for winner in winners:
        rank = preferences.get_preference(winner, tie_break)
        if rank < best_rank:
            best_rank = rank
            chosen_winner = winner
    
    return chosen_winner


def veto(preferences, tie_break):
    """
    Implements veto voting rule.
    
    Args:
        preferences: Preference object with candidates(), voters(), get_preference()
        tie_break: Integer representing the tie-breaking agent
    
    Returns:
        Integer representing the winning alternative
    """
    candidates = preferences.candidates()
    points = {candidate: len(preferences.voters()) for candidate in candidates}
    
    for voter in preferences.voters():
        for candidate in candidates:
            if preferences.get_preference(candidate, voter) == len(candidates) - 1:
                points[candidate] -= 1
                break
    
    max_points = max(points.values())
    winners = [c for c, p in points.items() if p == max_points]
    
    if len(winners) == 1:
        return winners[0]
    
    best_rank = len(candidates)
    chosen_winner = winners[0]
    for winner in winners:
        rank = preferences.get_preference(winner, tie_break)
        if rank < best_rank:
            best_rank = rank
            chosen_winner = winner
    
    return chosen_winner


def borda(preferences, tie_break):
    """
    Implements Borda voting rule.
    
    Args:
        preferences: Preference object with candidates(), voters(), get_preference()
        tie_break: Integer representing the tie-breaking agent
    
    Returns:
        Integer representing the winning alternative
    """
    candidates = preferences.candidates()
    n = len(candidates)
    score_vector = [n - 1 - i for i in range(n)]
    return scoring_rule(preferences, score_vector, tie_break)


def STV(preferences, tie_break):
    """
    Implements Single Transferable Vote (STV) rule.
    
    Args:
        preferences: Preference object with candidates(), voters(), get_preference()
        tie_break: Integer representing the tie-breaking agent
    
    Returns:
        Integer representing the winning alternative
    """
    candidates = preferences.candidates()
    remaining = set(candidates)
    
    while remaining:
        first_place_votes = {candidate: 0 for candidate in remaining}
        
        for voter in preferences.voters():
            best_rank = len(candidates)
            best_candidate = None
            for candidate in remaining:
                rank = preferences.get_preference(candidate, voter)
                if rank < best_rank:
                    best_rank = rank
                    best_candidate = candidate
            if best_candidate is not None:
                first_place_votes[best_candidate] += 1
        
        min_votes = min(first_place_votes.values())
        losers = {c for c, v in first_place_votes.items() if v == min_votes}
        
        if len(losers) == len(remaining):
            best_rank = len(candidates)
            chosen_winner = next(iter(remaining))
            for candidate in remaining:
                rank = preferences.get_preference(candidate, tie_break)
                if rank < best_rank:
                    best_rank = rank
                    chosen_winner = candidate
            return chosen_winner
        
        remaining -= losers
    
    raise RuntimeError("No winner found in STV")
