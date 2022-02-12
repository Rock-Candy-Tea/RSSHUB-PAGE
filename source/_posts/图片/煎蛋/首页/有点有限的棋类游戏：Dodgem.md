
---
title: '有点有限的棋类游戏：Dodgem'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom'
author: 煎蛋
comments: false
date: Wed, 09 Feb 2022 15:58:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom'
---

<div>   
<blockquote><p>“有点有限”是一个数学概念</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom" referrerpolicy="no-referrer"><p>去年最后一期的脑力小体操，本来是想介绍一个我以前玩过的棋类游戏。这个棋的特定就是规则简单，但当规模变大时，又有最够的深度；可以在有限步内结束，同时保证不会平局——必有胜负。但当时其中一条规则怎么也想不起来了。之后凭记忆查了资料，总算功夫不负有心人。</p>
<p>专栏作家Colin Vout发明了一种棋类游戏，名字叫Dodgem。棋盘是n×n个格子，两边各有n-1个棋子。下图就是3×3的棋盘。</p>
<p><img src="https://cors.zfour.workers.dev/?http://wx4.sinaimg.cn/mw690/a1262f29ly1gz7m8d32xwj208p099weg.jpg" alt="有点有限的棋类游戏：Dodgem" referrerpolicy="no-referrer"></p>
<p>两个玩家不是坐对面，而是邻座。游戏目标是，白棋从上走出棋盘，黑棋从最右边走出棋盘。谁先全部走完谁胜利。</p>
<p>两边轮流走棋，一次一步。每个棋子可以向邻近的格子移动。但除了从规定的边沿走出棋盘外，不可以走出棋盘。也不能走到已被其它棋子占据的格子里。</p>
<p>每方的棋子，按玩家的视角，都不可以后退。也就是至多有三个选项——往前/往左/往右挪动一步。</p>
<p>上面的规则保证游戏是有限的：可在有限步内结束。</p>
<p>另外还有一个特殊的规则：<strong>用黑棋举例，如轮到白方走棋，但黑方棋子阻隔导致白方当轮无法移动任何一个棋子时，白棋直接获胜。反之，白方若导致黑棋无法挪动，则黑方直接获胜</strong>。</p>
<p>显而易见，这个游戏不会出现平局。</p>
<p>两边轮流行动、彼此信息公开(任何策略和行动都反应在棋盘上，彼此可见)、有限步骤内可以结束的，且不会出现平局的游戏，这就叫<strong>somewhat finite game</strong>。后者在combinatorial game theory是比较有价值的考察对象，比如说可以构造超游戏Hypergame，乃至引出超游戏悖论The Hypergame Paradox。悖论具体为何，有机会再说。</p>
<p>目前，已知仅有3×3的Dodgem被完整分析过。可以证明先手必胜。</p>
<p>按文献，康威和盖在他们的名著《稳操胜券》一书里，分析了3×3的Dodgem。所以人们仍不知道，或者说没有动力去了解其他阶的Dodgem的完整策略。</p>  
</div>
            