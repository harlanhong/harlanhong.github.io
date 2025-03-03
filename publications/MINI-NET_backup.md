---
title: "MINI-Net: Multiple Instance Ranking Network for Video Highlight Detection"
collection: publications
permalink: /publication/MINI_NET
excerpt: 'We address the weakly supervised video highlight detectionproblem for learning to detect the segments that are more attractivein training videos given their video event label but without expensivesupervision of manually annotating highlight segments.'
date: 2020-7-3
venue: 'European Conference on Computer Vision'
paperurl: ''
citation: 'Fa-Ting Hong, Xuanteng Huang, Wei-Hong Li, and Wei-Shi Zheng. MINI-Net: Multiple Instance Ranking Networkfor Video Highlight Detection. In European Conference on Computer Vision (ECCV), 2020.'
---
<!-- <img src='/Projects/Learning-to-Rank/1842-framework.jpg'> -->
![avatar](/Projects/MINI-NET/1880-framework.pdf)
## Abstract
We address the weakly supervised video highlight detectionproblem for learning to detect the segments that are more attractivein training videos given their video event label but without expensivesupervision of manually annotating highlight segments. While averting lo-calizing highlight segments manually, such a weakly supervised modellingis challenging because a video in our daily life could contain highlightsegments with multiple event types,e.g., skiing and surfing. In this work,we  propose  to  cast  such  weakly  supervised  video  highlight  detectionmodelling for a given specific event as a multiple instance ranking net-work (MINI-Net) learning. We consider each video as a bag of segments,and therefore the proposed MINI-Net learns to enforce higher highlightscore for a positive bag that contains highlight segments of a specificevent than the ones for negative bags that are irrelevant. In particular,we form a max-max ranking loss in order to acquire a reliable relativecomparison between the most likely positive segment instance and themost hard negative segment instance. With such max-max ranking loss,our MINI-Net leverages all segment information effectively to acquirea more distinct video feature representation for localizing the highlightsegments of a specific event in a video. The extensive experimental resultson three challenging public benchmarks clearly validate the efficacy ofour multiple instance ranking approach for solving the problem.  


<!-- Paper is coming soon!!   -->
[Download paper here](https://arxiv.org/pdf/2007.09833.pdf) 



Recommended citation: Fa-Ting Hong, Xuanteng Huang, Wei-Hong Li, and Wei-Shi Zheng. MINI-Net: Multiple Instance Ranking Networkfor Video Highlight Detection. In European Conference on Computer Vision (ECCV), 2020.