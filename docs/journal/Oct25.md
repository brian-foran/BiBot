# 2026-10-20: Joint Actuator Debate

## Goal
Over the past days, I have been researching and holding an internal debate over whether the scope of the robot's actuators needs to change. The original concept for this robot was just to be a personal project. Now that I am converting it into a thesis, I need to evaluate more intensely the Reinforcement Learning potential of the resulting Robot. 

### The debate - BLDC vs Servo

The original intention was to use basic 9g micro-servos for the 6 robot joints, as they are extremely easy to integrate into an arduino system, require no extra hardware, and are compact enough to fit the ~10in tall robot I was picturing. However, they lack feedback, back drive, and customizability. 

The other option that I have spent days investigating is brushless DC motors with FOC (field oriented control) drivers. These are much more common in modern joints, as they provide the aspects that I listed servos lack (feedback, back drive, and customizability). These aspects allow the robot joint to be controlled on a torque control loop, which opens the possibility of controlling the robot under a dynamic model, rather than a kinematic model. The use of a dynamic model is how modern robots achieve fluid and responsive movements.

However, BLDC motors, especially kits with the magnet, encoder, and driver included, are at minimum 80 euro a piece. And that is if they are ordered from china, which comes with an import tax and a ~month lead time.

### Summary Table
|      | Pros | Cons |
| --- | --- | --- |
| **Servo** | Simple Integration with Arduino<br>Low Voltage Low Current<br>Less peripheral electrical components<br>Cheaper<br>Faster Delivery | No dynamic model<br>No back drive<br>Lifespan may be shorter |
| **BLDC** | Dynamic Model<br>Tuning<br>Back Drive | More expensive<br>Longer delivery<br>More complicated<br>Higher power requirements<br>More additional electronics (encoder, driver, power step-down, etc.)<br>Necessitate larger robot<br>More complicated joint geometry |





## Work completed


## Observations

## Decisions or open questions

I think that a robot with BLDC motor joints could be a much more exciting build with more potential application, but it might require more time and resources than are possible for a master's thesis with no funding, especially as my PI and I determined that the robot should be built by February to leave sufficient time for all the Reinforcement Learning. That said, the final consideration to make is which design decision results in a robot that has the best potential for reinforcement learning. My intuition says that a dynamic robot will align closer to existing simulation methods because it works in forces, rather than absolute position. However, a kinematic model has a very defined state-space consisting only in the possible combination of joint angles, making value/policy tabulation straight forward. 


## Evidence

## Next steps
Make a final proposal budget for each joint option. 

Follow up with Andreu on the content of this debate to see what his input is for the timing, budget, and RL aspects.

