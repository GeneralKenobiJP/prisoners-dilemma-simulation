Simulation of the prisoner's dilemma in Python.

Inspired by the [Veritasium's video](https://www.youtube.com/watch?v=mScpHTIi-kM&t=370s&ab_channel=Veritasium)
and a browser game by Nicky Case called [The Evolution of Trust](https://ncase.me/trust/)

Instantiate the simulation object as specified in the constructor or call the suite function to run a series of simulations.

There are 2 modes of simulation:
* Round-robin, where all strategies play each other exactly once
* Evolution, where all strategies play a round-robin tournament and, 
afterwards, the bottom 10% of strategies get eliminated and replaced by the top 10%.

As a twist, I introduced a strategy called *machine learning*, which incorporates a q-learning algorithm

The list of strategies that have been implemented is as follows:
* *always cooperate* - always cooperates
* *always defect* - always defects
* *tit-for-tat* - picks what opponent picked in the previous turn
* *grudger* - cooperates until cheated
* *pick random* - 50/50
* *suspicious tit-for-tat* - tit-for-tat but starts with defecting
* *tit-for-two-tats* - defects if opponent defected twice in a row
* *two-tits-for-tat* - retaliates twice after being cheated once
* *pavlov* - if the opponent's move was the same in the last turn, cooperates, otherwise - defects
* *detective* - cooperate, defect, cooperate, cooperate, then always cooperate if not cheated, always defect otherwise
* *simpleton* - if the last move cause a point gain, repeat it, otherwise change it
* *coop-75* - cooperate with .75 probability
* *retaliate-75* - cooperate, unless cheated - then retaliate with .75 probability
* *machine learning* - utilizes q-learning. The model is instantiated from scratch every time the simulation object is created, so the learning process should happen through the *suite* function rather than reinstantiating the simulation

There are *duel* and *duel_all* functions that enable to just battle selected strategies. They can be used to analyze the machine learning model after the simulation(s).

I have analyzed mostly two sets of players: *exhaustive* - having each strategy once, *hostile* - focusing on strategies that want to cheat or backstab sneakily

My foundings:
* In exhaustive tournament, the machine learning strategy mostly defaulted to something akin
to the tit-for-tat strategy, in more extreme situation switching to the grudger
* Sometimes, the model would learn to cheat on the detective strategy in turn 7 to gain back what was lost in turn 2, which I found to be interesting
* In hostile environment, the model seemed to default to always defect

There are some .txt files that contain *duel_all* results of the machine learning strategy after some simulations.