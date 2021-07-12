
---
title: 'MuZero_ Mastering Go, chess, shogi and Atari without rules'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=7904'
author: DeepMind
comments: false
date: Wed, 23 Dec 2020 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7904'
---

<div>   
<p><strong>In 2016, we introduced <a href="https://deepmind.com/research/case-studies/alphago-the-story-so-far" rel="noopener" target="_blank">AlphaGo</a>, the first artificial intelligence (AI) program to defeat humans at the ancient game of Go. Two years later, its successor - <a href="https://deepmind.com/blog/article/alphazero-shedding-new-light-grand-games-chess-shogi-and-go" rel="noopener" target="_blank">AlphaZero</a> - learned from scratch to master Go, chess and shogi. Now, <a href="https://rdcu.be/ccErB">in a paper in the journal Nature</a>, we describe MuZero, a significant step forward in the pursuit of general-purpose algorithms. MuZero masters Go, chess, shogi and Atari without needing to be told the rules, thanks to its ability to plan winning strategies in unknown environments.</strong></p>
<p>For many years, researchers have sought methods that can both learn a model that explains their environment, and can then use that model to plan the best course of action. Until now, most approaches have struggled to plan effectively in domains, such as Atari, where the rules or dynamics are typically unknown and complex.</p>
<p>MuZero, first introduced in a <a href="https://deepmind.com/research/publications/Mastering-Atari-Go-Chess-and-Shogi-by-Planning-with-a-Learned-Model" rel="noopener" target="_blank">preliminary paper in 2019</a>, solves this problem by learning a model that focuses only on the most important aspects of the environment for planning. By combining this model with AlphaZero’s powerful lookahead tree search, MuZero set a new state of the art result on the Atari benchmark, while simultaneously matching the performance of AlphaZero in the classic planning challenges of Go, chess and shogi. In doing so, MuZero demonstrates a significant leap forward in the capabilities of reinforcement learning algorithms.</p>  
</div>
            