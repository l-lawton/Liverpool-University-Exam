import pytest
import voting

class Preferences:
    def __init__(self):
        self._candidates = [1, 2, 3]
        self._voters = [1, 2]
        # Preference rankings where index represents rank (0 is most preferred)
        self._preferences = {
            1: {1: 2, 2: 0, 3: 1},  # Voter 1 prefers: 2 > 3 > 1
            2: {1: 0, 2: 1, 3: 2}   # Voter 2 prefers: 1 > 2 > 3
        }
    
    def candidates(self):
        return self._candidates
    
    def voters(self):
        return self._voters
    
    def get_preference(self, candidate, voter):
        if voter not in self._voters or candidate not in self._candidates:
            raise ValueError("Not a valid voter or candidate")
        return self._preferences[voter][candidate]

def test_dictatorship():
    prefer = Preferences()
    assert voting.dictatorship(prefer, 1) == 2
    assert voting.dictatorship(prefer, 2) == 1
    
def test_dictatorship_invalid():
    prefer = Preferences()
    with pytest.raises(ValueError):
        voting.dictatorship(prefer, 3)

def test_plurality():
    prefer = Preferences()
    assert voting.plurality(prefer, 1) == 2  # Candidates 1 and 2 tied, tie-breaker prefers 2

def test_veto():
    prefer = Preferences()
    assert voting.veto(prefer, 1) == 2  # Candidate 3 gets most vetoes

def test_borda():
    prefer = Preferences()
    assert voting.borda(prefer, 1) == 2  # Should win with highest Borda count

def test_scoring_rule():
    prefer = Preferences()
    score_vector = [2, 1, 0]
    assert voting.scoring_rule(prefer, score_vector, 1) == 2

def test_STV():
    prefer = Preferences()
    assert voting.STV(prefer, 1) == 2  # Should eliminate 3, then 1
