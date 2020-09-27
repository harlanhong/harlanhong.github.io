---
title: 'CVPR2020: Progressive Relation Learning for Group Activity Recognition'
date: 2020-6-05
permalink: /posts/2020/06/PRL/
tags:
  - Group Activity Recogition
  - CVPR2020
---

## Progressive Relation Learning for Group Activity Recognition

Citation: Guyue Hu, Bo Cui, Yuan He, Shan Yu. Progressive Relation Learning for Group Activity Recognition. In Computer Vision and Pattern Recognition, 2020.

![avatar](/Projects/progressive-relation-learning-Hu/Abstract.pdf)

### My Summarization
In this work, authors mainly proposed a complex framework that contains three components to optimize the problem of group activity recognition. 1) Feature Distilling (FD) agent are used to select the distriminative frame by a markov decision process with the probalitity improvement of the groundtruth and shift result as supervision. 2)Given distilled feature, Semantic Relation Graph (SRG) infer the semantic relations among individuals iteratively. First, the CNN features of posture and apperance of persons were treated as nodes and the spatial distance vectors and direction vertor between each pairs of person are treated as edges. Second, each node updated their state by leveraging the edags conneted to it (message passing) and each edge enrolls message from updated sender and updataed receiver to update itself attributes. Finally, the global attribute was updated with the help of updated edges. 3) After constructing the sementic graph, Relation Gating (RG) agent utilize a markov process to discare several group-irrelevant relations by a noval structured sparsity loss and optimize by several rewards.  
This framework is too complex in implementation and the number of its parameters would be large, which is unfair compared with other methods with small number of parameters. In spite of its flaws, this work is noval enought as it combine the graph modelling and RL method to track the problem of group activity recognition. to the best of my knowledge, it's the first work the utilize RL to solve this task.

### Qustion
- Is there any particular purpose to using the LSTM in Sementic Relation Graph other than to memorize sequence information, why not mlp?
- More visualization results about the G in Relation Gating agent should be shown to prove that this agent is able to learn to select the group-relevant relations
- In the comparision with related methods, the backbone should be the same.

@me: I read this paper because I have been working on this filed recently. The text above is purely my personal thought, please correct me if there is any mistake. In terms of grammar, errors are inevitable due to limited ability.


