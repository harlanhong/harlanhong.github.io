---
title: "Hybrid Dynamic-static Context-aware Attention Network for Action Assessment in Long Videos"
collection: publications
permalink: /publication/ACTION_NET
excerpt: 'In this work, we present a novel hybrid dynAmic-static Context-aware attenTION NETwork (ACTION-NET) for action assessment in long videos'
date: 2020-7-26
venue: 'ACM International Conference on Multimedia'
paperurl: ''
citation: 'Ling-An Zeng, Fa-Ting Hong, Wei-Shi Zheng, Qi-Zhi Yu, Wei Zeng, Yao-Wei Wang, and Jian-Huang Lai. Hybrid Dynamic-static Context-aware Attention Network for Action Assessment in Long Videos. Proc. of ACM International Conference on Multimedia (ACM MM), 2020.'
---
<!-- <img src='/Projects/Learning-to-Rank/1842-framework.jpg'> -->
![avatar](/Projects/ACTION-NET/pipeline.pdf)
## Abstract
The objective of action quality assessment is to score sports videos. However, most existing works focus only on video dynamic information (\ie, motion information) but ignore the specific postures that an athlete is performing in a video, which could be important for action assessment in long videos. In this work, we present a novel hybrid dynAmic-static Context-aware attenTION NETwork (ACTION-NET) for action assessment in long videos. To learn more discriminative representations for videos, we not only learn the video dynamic information but also focus on the static postures of the detected athletes in specific frames, which represent the action quality at certain moments, with the help of the proposed hybrid dynamic-static architecture. Moreover, we leverage a context-aware attention module consisting of a temporal instance-wise graph convolutional network (GCN) unit and an attention unit, the former for exploring the relations between instances and the latter for assigning a proper weight to each instance, for both streams to extract more robust stream features. Finally, we combine the features of the two streams to regress the final video score, supervised by ground-truth scores given by experts. Additionally, we have collected and annotated the new Rhythmic Gymnastics dataset, which contains videos of four different types of gymnastics routines, to support research on action quality assessment in long videos. Extensive experimental results reveal the efficacy of our proposed method, which outperforms all previous approaches. 


Paper and Code!  
[Download paper here](https://arxiv.org/abs/2008.05977)  
[View code here](https://github.com/lingan1996/ACTION-NET)




Recommended citation: Ling-An Zeng, Fa-Ting Hong, Wei-Shi Zheng, Qi-Zhi Yu, Wei Zeng, Yao-Wei Wang, and Jian-Huang Lai. Hybrid Dynamic-static Context-aware Attention Network for Action Assessment in Long Videos. Proc. of ACM International Conference on Multimedia (ACM MM), 2020.