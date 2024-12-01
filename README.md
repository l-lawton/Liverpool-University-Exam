# Liverpool-University-Exam
Implementing voting rules for a coding challenge.

Your task will be to implement various voting rules, given the preferences of voters.

Background:

In this assignment you will design and implement several voting rules. In a voting setting, we have a set of 
 agents/voters and a set of 
 alternatives/candidates. Every agent has a preference ordering 
 where 
 means that the agent prefers alternative 
 to alternative 
. A preference profile is a set of 
 preference orderings, one for every agent.

For example, if we have a voting setting with 4 agents and 4 alternatives, one possible preference profile could be the following:

Agent 1: 

Agent 2: 

Agent 3: 

Agent 4: 

A voting rule is a function that takes as input the preferences of a set of agents and outputs a winning alternative.

The preference object
Each of your functions will be passed a Preference object. The preference object has three functions:

candidates()	Returns a list of candidates/alternatives. This will be a list of candidates of the form [1,...,n].
voters()	Returns a list of voters/agents. This will be a list of distinct voters of the form [1,...,m].
get_preference(candidate, voter)	Returns the preference rank of the given candidate for the given voter. The highest rank candidate will return 0, and the lowest ranked candidate will return n-1.

The object will be a python object. The implementation may have other properties and functions to make it work, but you are only allowed to interact with it through these three methods.

While you may need to make your own Preferences object for testing purposes, you must not submit a Preferences object, the test suite will have its own implementation that will be passed to your functions. You can only be sure this object will have those three methods.

Your task
Your task is to implement the following functions:

dictatorship(preferences, agent) -> int

An agent is selected, and the winner is the alternative that this agent ranks first. For example, if the preference ordering of the selected agent is 
, then the winner is alternative 
.

The function should input:

a preference profile represented by a Preference class object as described above 
an integer corresponding to an agent to be the dictator.
The return of the function should be the winner according to the Dictatorship rule described above. If the integer given does not represent a valid agent then a ValueError should be raised.

scoring_rule(preferences, score_vector, tie_break): -> int
For every agent, the function assigns the highest score in the scoring vector to the most preferred alternative of the agent, the second highest score to the second most preferred alternative of the agent and so on, and the lowest score to the least preferred alternative of the agent. In the end, it returns the alternative with the highest total score, using the tie-breaking option to distinguish between alternatives with the same score.

The function should input
a preference profile represented by a Preference class object as described above 
a score vector of length 
, i.e., equal to the number of alternatives, i.e., a list of length 
 containing positive floating numbers. 
an integer denoting the tie breaking agent
The function should contain error-handling code for the case when the length of the scoring vector is not 
, in that case, a ValueError with a suitable message.

plurality (preferences, tie_break) -> int
The winner is the alternative that appears the most times in the first position of the agents' preference orderings. In the case of a tie, use a tie-breaking rule to select a single winner.
The function should input
a preference profile represented by a Preference class object as described above 
an integer denoting the tie breaking agent
The function should return the winner of the Plurality rule as described above, using the tie-breaking option to distinguish between possible winners.

veto (preferences, tie_break) -> int
Every agent assigns 0 points to the alternative that they rank in the last place of their preference orderings, and 1 point to every other alternative. The winner is the alternative with the most number of points. In the case of a tie, use a tie-breaking rule to select a single winner.
The function should input
a preference profile represented by a Preference class object as described above
an integer denoting the tie breaking agent
The function should return the winner of the Veto rule as described above, using the tie-breaking option to distinguish between possible winners.

borda (preferences, tie_break) -> int
Every agent assigns a score of 
 to the their least-preferred alternative (the one at the bottom of the preference ranking), a score of 
 to the second least-preferred alternative, ... , and a score of 
 to their favourite alternative. In other words, the alternative ranked at position 
 receives a score of 
. The winner is the alternative with the highest score. In the case of a tie, use a tie-breaking rule to select a single winner.
The function should input
a preference profile represented by a Preference class object as described above
an integer denoting the tie breaking agent
The function should return the winner of the Borda rule as described above, using the tie-breaking option to distinguish between possible winners.

STV (preferences, tie_break) -> int
The voting rule works in rounds. In each round, the alternatives that appear the least frequently in the first position of agents' rankings are removed, and the process is repeated. When the final set of alternatives is removed (one or possibly more), then this last set is the set of possible winners. If there are more than one, a tie-breaking rule is used to select a single winner.

Example:

Consider the preference profile of the example above. In the first round alternative (\delta is removed\) and we get the following new preference profile:

Agent 1: 

Agent 2: 

Agent 3: 

Agent 4: 

In the second round, both 
 and 
 are removed. In the third round, 
 is removed, and 
 is the winner.

The function should input
a preference profile represented by a Preference class object as described above
an integer denoting the tie breaking agent
The function should return the winner of the Single Transferable Vote rule as described above, using the tie-breaking option to distinguish between possible winners.

Tie-Breaking Rules:

Each function is given a special tie breaking agent 
. From the possible winning alternatives from the voting mechanism, select the one that agent 
 ranks the highest in his/her preference ordering. 

Instructions
In your program you should follow the specified, variable and method names and signatures, If you do not follow the specified function names and signatures, then the correctness of your program may not be able to be correctly determined; you may also lose marks for not following the brief.

You should submit a single file, named voting.py

You may write some test code in the main body, but this must not run if your file is imported into another module. If this is not ensured, the correctness of your program might not be able to be verified.

You are encouraged to submit repeatedly, so you can verify your code works on the visible test cases. There is no penalty for multiple submissions before the deadline.
