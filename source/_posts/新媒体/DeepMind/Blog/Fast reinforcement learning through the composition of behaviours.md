
---
title: 'Fast reinforcement learning through the composition of behaviours'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=5306'
author: DeepMind
comments: false
date: Mon, 12 Oct 2020 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5306'
---

<div>   
<h4><strong>The compositional nature of intelligence</strong></h4>
<p>Imagine if you had to learn how to chop, peel and stir all over again every time you wanted to learn a new recipe. In many machine learning systems, agents often have to learn entirely from scratch when faced with new challenges. It’s clear, however, that people learn more efficiently than this: they can combine abilities previously learned. In the same way that a finite dictionary of words can be reassembled into sentences of near infinite meanings, people repurpose and re-combine skills they already possess in order to tackle novel challenges.</p>
<p>In nature, learning arises as an animal explores and interacts with its environment in order to gather food and other rewards. This is the paradigm captured by <a href="http://incompleteideas.net/book/the-book-2nd.html">reinforcement learning</a> (RL): interactions with the environment reinforce or inhibit particular patterns of behavior depending on the resulting reward (or penalty). Recently, the combination of RL with <a href="https://www.nature.com/articles/nature14539">deep learning</a> has led to impressive results, such as agents that can learn how to play boardgames like <a href="https://deepmind.com/blog/article/alphazero-shedding-new-light-grand-games-chess-shogi-and-go">Go</a> and <a href="https://arxiv.org/abs/1911.08265">chess</a>, the full spectrum of <a href="https://deepmind.com/blog/article/Agent57-Outperforming-the-human-Atari-benchmark">Atari</a> games, as well as more modern, difficult video games like <a href="https://openai.com/projects/five/">Dota</a> and <a href="https://deepmind.com/blog/article/alphastar-mastering-real-time-strategy-game-starcraft-ii">StarCraft II</a>.</p>
<p>A major limitation in RL is that current methods require vast amounts of training experience. For example, in order to learn how to play a single Atari game, an RL agent typically consumes an amount of data corresponding to several weeks of uninterrupted playing. A <a href="http://gershmanlab.webfactional.com/pubs/Tsividis17.pdf">study</a> led by researchers at MIT and Harvard indicated that in some cases, humans are able to reach the same performance level in just fifteen minutes of play.</p>
<p>One possible reason for this discrepancy is that, unlike humans, RL agents usually learn a new task from scratch. We would like our agents to leverage knowledge acquired in previous tasks to learn a new task more quickly, in the same way that a cook will have an easier time learning a new recipe than someone who has never prepared a dish before. In <a href="https://www.pnas.org/content/early/2020/08/13/1907370117">an article</a> recently published in the Proceedings of the National Academy of Sciences (PNAS), we describe a framework aimed at endowing our RL agents with this ability.</p>
<p><strong>Two ways of representing the world</strong></p>
<p>To illustrate our approach, we will explore an example of an activity that is (or at least used to be) an everyday routine: the commute to work. Imagine the following scenario: an agent must commute every day from its home to its office, and it always gets a coffee on the way. There are two cafes between the agent's house and the office: one has great coffee but is on a longer path, and the other one has decent coffee but a shorter commute (Figure 1). Depending on how much the agent values the quality of the coffee versus how much of a rush it is in on a given day, it may choose one of two routes (the yellow and blue paths on the map shown in Figure 1).</p>  
</div>
            