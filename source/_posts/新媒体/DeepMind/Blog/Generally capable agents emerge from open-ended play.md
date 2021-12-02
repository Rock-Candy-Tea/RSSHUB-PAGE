
---
title: 'Generally capable agents emerge from open-ended play'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=7736'
author: DeepMind
comments: false
date: Tue, 27 Jul 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7736'
---

<div>   
<p>In recent years, artificial intelligence agents have succeeded in a range of complex game environments. For instance, <a href="https://deepmind.com/blog/article/alphazero-shedding-new-light-grand-games-chess-shogi-and-go" rel="noopener" target="_blank">AlphaZero</a> beat world-champion programs in chess, shogi, and Go after starting out with knowing no more than the basic rules of how to play. Through <a href="https://en.wikipedia.org/wiki/Reinforcement_learning" rel="noopener" target="_blank">reinforcement learning</a> (RL), this single system learnt by playing round after round of games through a repetitive process of trial and error. But AlphaZero still trained separately on each game — unable to simply learn another game or task without repeating the RL process from scratch. The same is true for other successes of RL, such as <a href="https://deepmind.com/blog/article/Agent57-Outperforming-the-human-Atari-benchmark" rel="noopener" target="_blank">Atari</a>, <a href="https://deepmind.com/blog/article/capture-the-flag-science" rel="noopener" target="_blank">Capture the Flag</a>, <a href="https://deepmind.com/blog/article/AlphaStar-Grandmaster-level-in-StarCraft-II-using-multi-agent-reinforcement-learning" rel="noopener" target="_blank">StarCraft II</a>, <a href="https://openai.com/projects/five/" rel="noopener" target="_blank">Dota 2</a>, and <a href="https://openai.com/blog/emergent-tool-use/" rel="noopener" target="_blank">Hide-and-Seek</a>. DeepMind’s mission of solving intelligence to advance science and humanity led us to explore how we could overcome this limitation to create AI agents with more general and adaptive behaviour. Instead of learning one game at a time, these agents would be able to react to completely new conditions and play a whole universe of games and tasks, including ones never seen before.</p>
<p>Today, we published "<a href="https://deepmind.com/research/publications/open-ended-learning-leads-to-generally-capable-agents" rel="noopener" target="_blank">Open-Ended Learning Leads to Generally Capable Agents</a>," a preprint detailing our first steps to train an agent capable of playing many different games without needing human interaction data. We created a vast game environment we call XLand, which includes many multiplayer games within consistent, human-relatable 3D worlds. This environment makes it possible to formulate new learning algorithms, which dynamically control how an agent trains and the games on which it trains. The agent’s capabilities improve iteratively as a response to the challenges that arise in training, with the learning process continually refining the training tasks so the agent never stops learning. The result is an agent with the ability to succeed at a wide spectrum of tasks — from simple object-finding problems to complex games like hide and seek and capture the flag, which were not encountered during training. We find the agent exhibits general, heuristic behaviours such as experimentation, behaviours that are widely applicable to many tasks rather than specialised to an individual task. This new approach marks an important step toward creating more general agents with the flexibility to adapt rapidly within constantly changing environments.</p>  
</div>
            