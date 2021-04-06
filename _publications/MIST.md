---
title: "MIST: Multiple Instance Self-Training Framework for Video Anomaly Detection"
collection: publications
permalink: /publication/MIST
excerpt: 'In this work, we develop a multiple instance self-training framework (MIST) to efficiently refine task-specific discriminative representations with only video-level annotations.'
date: 2021-4-05
venue: 'IEEE International Conference on Computer Vision and Pattern Recognition. 2021.'
paperurl: ''
citation: 'Jia-Chang Feng, Fa-Ting Hong and Wei-Shi Zheng. “MIST: Multiple Instance Self-Training Framework for Video Anomaly Detection, Proceedings of the IEEE International Conference on Computer Vision and Pattern Recognition. 2021.'
---
<!-- <img src='/Projects/Learning-to-Rank/1842-framework.jpg'> -->
![avatar](/Projects/MIST/framework.pdf)
## Abstract
Weakly supervised video anomaly detection (WS-VAD) is to distinguish anomalies from normal events based on discriminative representations. Most existing works are limited in insufficient video representations. In this work, we develop a multiple instance self-training framework (MIST) to efficiently refine task-specific discriminative representations with only video-level annotations. In particular, MIST is composed of 1) a multiple instance pseudo label generator, which adapts a sparse continuous sampling strategy to produce more reliable clip-level pseudo labels, and 2) a self-guided attention boosted feature encoder that aims to automatically focus on anomalous regions in frames while extracting task-specific representations. Moreover, we adopt a self-training scheme to optimize both components and finally obtain a task-specific feature encoder. Extensive experiments on two public datasets demonstrate the efficacy of our method, and our method performs comparably to or even better than existing supervised and weakly supervised methods, specifically obtaining a frame-level AUC 94.83% on ShanghaiTech.



Paper and Code!  
[Download paper here](https://arxiv.org/abs/2104.01633)  
<!-- [View code here](https://github.com/lingan1996/ACTION-NET) -->




Recommended citation: 
Jia-Chang Feng, Fa-Ting Hong and Wei-Shi Zheng. “MIST: Multiple Instance Self-Training Framework for Video Anomaly Detection Proceedings of the IEEE International Conference on Computer Vision and Pattern Recognition. 2021.

Bib:
@inproceedings{feng2021mist,
title={MIST: Multiple Instance Self-Training Framework for Video Anomaly Detection},
author={Feng, Jia-Chang and Hong, Fa-Ting and Zheng, Wei-Shi},
booktitle={Proceedings of the IEEE International Conference on Computer Vision and Pattern Recognition}, year={2021}
}

https://harlanhong.github.io/publication/MIST