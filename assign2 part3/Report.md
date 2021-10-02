### Team name: Learn_from_scratch
### Team_no : 27
### Assignment 2 Part 3
### Members: Shivang Gupta : 2019101117, Keshav Bansal: 2019101019

#### Q1 Procedure of making A matrix

For every state, we are first finding the possible actions and for every possible action we are adding a new column to the matrix where we are adding values to the previous value of a state action pair for outgoing states and adding negative values according to the probability to the states where the action is incoming, i.e. we are adding positive values to the current state and on taking actions, the states that would be reached are given negative values according to their probabilities.
We are passing five variables to the function getrows(a,b,c,d,e) which returns the row number by this formula: 
a * mat * arrow * states * health+b * arrow * states * health+c * states * health+d*health+e

#### Q2: Procedure of Finding the policy and analyzing the results:

Every value in X vector gives us the expected number of times that action is taken for that particular state-action pair. In the X vector thus obtained, for every state, there are multiple entries in the x vector corresponding to every state and we are taking the maximum of those values which would give us the action for that state which has the maximim value in x vector. 
Analysis:
* When the person is at a health of 25, we see more number of HIT  actions and SHOOT actions as final state would be attained if MM dies.
* When the player is at a position EAST we see more number of lefts to avoid being hit by MM and thus follows a risk aversion policy as it reduces the reward by -40(given). 
* Also, when the player is at EAST position more number of HIT and SHOOT actions are there as the player wants to reach the final state as soon as possible as there are more chances of being hit and getting a negative reward.
* At North and South we see more number of STAY and CRAFT and GATHER actions to avoid the risk of getting damaged.
* At West, we see more number of SHOOT and STAY actions for the same reason of reaching the final state earlier and avoid the risk of getting hit.




### Q3.)

Yes there can be multiple policies that can be generated for a MDP.
1.) In order to select an optimal action to be taken in a state, we select the one with the maximum value for expected number of times the action will be taken in that state.
2.) Changing the reward/step-cost for each state can also result in a change in the policy. Since if the penalty is higher (stepcost is lower) the agent will want to and try to reach the terminal state faster with a greater reward. To get a positive reward and therefore a better utility agent will try to reach terminal state faster.
3.) Alpha vector represents the start states. So as the start state varies , the policy varies.
4.) changing values of parameters such as the probabilities of taking various different actions, the rewards/penalties received at each state ie changing the A matrix , changing reward matrix will also change the policy since the state diagram will change and therefore the actions will change and hence the policy will change.










              