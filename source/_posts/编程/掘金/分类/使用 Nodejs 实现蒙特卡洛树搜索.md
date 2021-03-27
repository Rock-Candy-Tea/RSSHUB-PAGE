
---
title: '使用 Node.js 实现蒙特卡洛树搜索'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc3694635134486f961be404c10a25ff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 00:04:23 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc3694635134486f961be404c10a25ff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://medium.com/@quasimik/implementing-monte-carlo-tree-search-in-node-js-5f07595104df" target="_blank" rel="nofollow noopener noreferrer">Implementing Monte Carlo Tree Search in Node.js</a></li>
<li>原文作者：<a href="https://medium.com/@quasimik" target="_blank" rel="nofollow noopener noreferrer">Michael Liu</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2020/implementing-monte-carlo-tree-search-in-node-js.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/zenblo" target="_blank" rel="nofollow noopener noreferrer">zenblo</a></li>
<li>校对者：<a href="https://github.com/PassionPenguin" target="_blank" rel="nofollow noopener noreferrer">PassionPenguin</a>、<a href="https://github.com/chzh9311" target="_blank" rel="nofollow noopener noreferrer">chzh9311</a></li>
</ul>
</blockquote>
<h1 data-id="heading-0">使用 Node.js 实现蒙特卡洛树搜索</h1>
<p><img alt="11.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc3694635134486f961be404c10a25ff~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>本文是<a href="https://medium.com/@quasimik/monte-carlo-tree-search-applied-to-letterpress-34f41c86e238" target="_blank" rel="nofollow noopener noreferrer">上一篇文章</a>的后续，我会提供足够的背景知识，也顺便提一下这篇文章。要注意的是，本文的技术含量会比较高。本文所有代码都可以在 <a href="https://github.com/quasimik/medium-mcts/" target="_blank" rel="nofollow noopener noreferrer">GitHub 仓库</a>中找到。</p>
<p>与上一篇文章一样，本文也假设读者具备一定的计算机科学知识，尤其是数据结构中关于<strong>树结构</strong>的工作原理，还需要具备 <strong>JavaScript</strong>（ES6+）的中级知识。</p>
<p>本文的目标很简单：</p>
<p>实现蒙特卡洛树搜索（MCTS）算法来玩一个给定规则的游戏。</p>
<p>这整个过程将是指导性和实践性的，并且忽略掉性能优化的部分。我将会对链接的代码片段进行简要解释，希望你能跟上我的脚步并花一些时间理解代码中复杂难懂的部分。</p>
<p>让我们开始吧！</p>
<h2 data-id="heading-1">创建骨架文件</h2>
<p>在 <code>game.js</code> 文件中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** 代表游戏棋盘的类。 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Game</span> </span>&#123;

  <span class="hljs-comment">/** 生成并返回游戏的初始状态。 */</span>
  <span class="hljs-function"><span class="hljs-title">start</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-keyword">return</span> state
  &#125;

  <span class="hljs-comment">/** 返回当前玩家在给定状态下的合法移动。 */</span>
  <span class="hljs-function"><span class="hljs-title">legalPlays</span>(<span class="hljs-params">state</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-keyword">return</span> plays
  &#125;

  <span class="hljs-comment">/** 将给定的状态提前并返回。 */</span>
  <span class="hljs-function"><span class="hljs-title">nextState</span>(<span class="hljs-params">state, move</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-keyword">return</span> newState
  &#125;

  <span class="hljs-comment">/** 返回游戏的胜利者。 */</span>
  <span class="hljs-function"><span class="hljs-title">winner</span>(<span class="hljs-params">state</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-keyword">return</span> winner
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = Game
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>monte-carlo.js</code> 文件中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** 表示蒙特卡洛树搜索的类。 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MonteCarlo</span> </span>&#123;

  <span class="hljs-comment">/** 从给定的状态中，反复运行 MCTS 来建立统计数据。 */</span>
  <span class="hljs-function"><span class="hljs-title">runSearch</span>(<span class="hljs-params">state, timeout</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
  &#125;

  <span class="hljs-comment">/** 从现有的统计数据中获取最佳的移动。 */</span>
  <span class="hljs-function"><span class="hljs-title">bestPlay</span>(<span class="hljs-params">state</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// return play</span>
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = MonteCarlo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>index.js</code> 文件中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Game = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./game.js'</span>)
<span class="hljs-keyword">const</span> MonteCarlo = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./monte-carlo.js'</span>)

<span class="hljs-keyword">let</span> game = <span class="hljs-keyword">new</span> Game()
<span class="hljs-keyword">let</span> mcts = <span class="hljs-keyword">new</span> MonteCarlo(game)

<span class="hljs-keyword">let</span> state = game.start()
<span class="hljs-keyword">let</span> winner = game.winner(state)

<span class="hljs-comment">// 从初始状态开始轮流进行游戏，直到有玩家胜利为止</span>
<span class="hljs-keyword">while</span> (winner === <span class="hljs-literal">null</span>) &#123;
  mcts.runSearch(state, <span class="hljs-number">1</span>)
  <span class="hljs-keyword">let</span> play = mcts.bestPlay(state)
  state = game.nextState(state, play)
  winner = game.winner(state)
&#125;

<span class="hljs-built_in">console</span>.log(winner)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先花点时间梳理一下代码吧。在脑海中搭建一个子版块的脚手架，然后尝试去明白一下这个东西。这是一个思维上的检查点，先确保你明白它是如何组合在一起的，如果感到无法理解，就请留言吧，让我看看我能为你做些什么。</p>
<h2 data-id="heading-2">找到合适的游戏</h2>
<p>在开发一个 MCTS 游戏智能体的背景下，我们可以把我们真正的程序看作是实现 MCTS 框架的代码，也就是 <code>monte-carlo.js</code> 文件中的代码。在 <code>game.js</code> 文件中的游戏专用代码是可以互换并且即插即用的，它是我们使用 MCTS 框架的接口。我们主要是想做 MCTS 背后的大脑，它应该真的能在任何游戏上运行。毕竟，我们感兴趣的是一般性的游戏玩法。</p>
<p>不过，为了测试我们的 MCTS 框架，我们需要选择一个特定的游戏，并使用该游戏运行我们的框架。我们希望看到 MCTS 框架在每个步骤中都做出对我们选择的游戏有意义的决策。</p>
<p>做一个井字游戏（<code>Tic-Tac-Toe</code>）怎么样呢？几乎所有的游戏入门教学都会用到它，它还有着一些非常令我们满意的特性：</p>
<ul>
<li>大家之前都玩过。</li>
<li>它的规则很简单，可以用算法实现。</li>
<li>它具有一份确定的<a href="https://en.wikipedia.org/wiki/Perfect_information" target="_blank" rel="nofollow noopener noreferrer">完善的信息</a>。</li>
<li>它是一款对抗性的双人游戏。</li>
<li>状态空间很简单，可以在心理上进行建模。</li>
<li>状态空间的复杂程度足以证明算法的强大。</li>
</ul>
<p>但是，井字游戏真的很无聊，不是吗？另外，你大概已经知道井字游戏的最佳策略，这就失去了一些吸引力。有这么多游戏可以选择，我们再选一个：四子棋（<strong><code>Connect Four</code></strong>）怎么样？除了可能比井字游戏享有更低的人气外，它不仅有上面所列举的特性，还可能让玩家不那么容易地建立四子棋状态空间的心理模型。</p>
<p><img alt="22.jpg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/244979518456480fad1adb5420c543a2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在我们的实现中，我们将使用 Hasbro（孩之宝：美国著名玩具公司）的尺寸和规则，即是 6 行 7 列，其中垂直、水平和对角线棋子数相连为 4 就算胜利。棋子会从上方落下，并借助重力落在自底向上数的第一个空槽。</p>
<p>不过在我们继续讲述之前，要先说明一下。如果你有信心，你可以自己去实现任何你想要的游戏，只要它遵守给定的游戏 API。只是当你搞砸了，不能用的时候不要来抱怨。请记住，像国际象棋和围棋这样的游戏太复杂了，即使是 MCTS 也无法（有效地）独自解决；谷歌在 <a href="https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf" target="_blank" rel="nofollow noopener noreferrer">AlphaGo</a> 中通过向 MCTS 添加有效的机器学习策略来解决这个问题。如果你想玩自己的游戏，你可以跳过接下来的两个部分。</p>
<h2 data-id="heading-3">实现四子棋游戏</h2>
<p>现在，直接将 <code>game.js</code> 改名为 <code>game-c4.js</code>，将类改名为 <code>Game_C4</code>。同时，创建两个新类：<code>State_C4</code> 在 <code>state-c4.js</code> 中表示游戏状态，<code>Play_C4</code> 在 <code>play-c4.js</code> 中表示状态转换。</p>
<p>虽然这不是本文的主要内容，但是你自己会如何构建呢？</p>
<ul>
<li>你会如何在 <code>State_C4</code> 中表示一个游戏状态呢？</li>
<li>在 <code>Play_C4</code> 中，你将如何表示一个状态转换（例如一个动作）呢？</li>
<li>你会如何把 <code>State_C4</code>、<code>Play_C4</code> 和四子棋游戏规则 —— 用冰冷的代码放在 <code>Game_C4</code> 中吗？</li>
</ul>
<p>注意，我们需要通过骨架文件 <code>game-c4.js</code> 中定义的高级 API 方法所要求的形式实现四子棋游戏。</p>
<p>你可以独立思考完成或者直接使用我完成的 <a href="https://github.com/quasimik/medium-mcts/blob/master/play-c4.js" target="_blank" rel="nofollow noopener noreferrer"><code>play-c4.js</code></a>、<a href="https://github.com/quasimik/medium-mcts/blob/master/state-c4.js" target="_blank" rel="nofollow noopener noreferrer"><code>state-c4.js</code></a> 和 <a href="https://github.com/quasimik/medium-mcts/blob/master/game-c4.js" target="_blank" rel="nofollow noopener noreferrer"><code>game-c4.js</code></a> 文件。</p>
<hr>
<p>这是一个工作量很大的活，不是吗？至少对我来说是这样的。这段代码需要一些 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference" target="_blank" rel="nofollow noopener noreferrer">JavaScript</a> 知识，但应该还是很容易读懂的。最重要的工作在 <code>Game_C4.winner()</code> 中 —— 它用于在四个独立的棋盘中建立积分系统，而所有的棋盘都在 <code>checkBoards</code> 里面。每个棋盘都有一个可能的获胜方向（水平、垂直、左对角线或右对角线）。我们需要确保棋盘的三个面比实际棋盘大，方便为算法提供零填充。</p>
<p>我相信还有更好的方法。<code>Game.winner()</code> 的运行时性能并不是很好，具体来说，在<a href="http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/BigONotation.html" target="_blank" rel="nofollow noopener noreferrer">大 O 表示法</a>中，它是 <code>O(rows * cols)</code>，所以性能并不是很好。通过在状态对象中存储 <code>checkBoards</code>，并且只更新 <code>checkBoards</code> 中最后改变状态的单元格（也会包含在状态对象中），可以大幅改善运行时性能，也许你以后可以尝试这个优化方法。</p>
<h2 data-id="heading-4">运行四子棋游戏</h2>
<p>此时，我们将通过模拟 1000 次四子棋游戏来测试 <code>Game_C4</code>。点击获取 <a href="https://github.com/quasimik/medium-mcts/blob/master/test-game-c4.js" target="_blank" rel="nofollow noopener noreferrer"><code>test-game-c4.js</code></a> 文件。</p>
<p>在终端上运行 <code>node test-game-c4.js</code>。在一个相对现代的处理器和最新版本的 <code>Node.js</code> 上，运行 <code>1000</code> 次迭代应该会在一秒钟内完成：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> node test-game-c4.js</span>

[ [ 0, 0, 0, 0, 0, 0, 2 ],
  [ 0, 2, 0, 0, 0, 0, 2 ],
  [ 0, 1, 0, 1, 2, 1, 2 ],
  [ 0, 2, 1, 2, 2, 1, 2 ],
  [ 0, 1, 1, 2, 1, 2, 1 ],
  [ 0, 1, 2, 1, 1, 2, 1 ] ]
0.549
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二号棋手在内部用 <strong>-1</strong> 表示，这是为了方便 <code>game-c4.js</code> 的计算。用 <code>2</code> 代替 <code>-1</code> 的那段代码只是为了对齐棋盘输出结果。为了简便起见，程序只输出了一块棋盘，但它确实玩了另外的 <code>999</code> 次四子棋游戏。在单个棋盘输出之后，它应该输出一号棋手在所有 <code>1000</code> 盘棋中获胜的分数 —— 预计数值在 <code>55%</code> 左右，因为第一个棋手有先发优势。</p>
<h2 data-id="heading-5">分析现在的状况</h2>
<p>我们已经实现一个带有 API 方法并且可以运行的游戏，这些 API 方法可以与 <code>State</code> 对象表示的游戏状态协同运行。我们现在的状况如何？</p>
<blockquote>
<p>目标：实现蒙特卡洛树搜索（MCTS）算法来玩一个给定规则的游戏。</p>
</blockquote>
<p>当然，我们还没有达到目的。刚才我们完成了一件非常重要的事情：让它设立一个切实的目标，并组成测试我们实现 MCTS 的核心模块。现在，我们进入正题。</p>
<h2 data-id="heading-6">实现蒙特卡洛树搜索</h2>
<p>阅读<a href="https://medium.com/@quasimik/monte-carlo-tree-search-applied-to-letterpress-34f41c86e238" target="_blank" rel="nofollow noopener noreferrer">上一篇文章</a> —— 尤其是 MCTS 详解部分 —— 应该有助于理解本文的其他内容。在这里，我将按照 MCTS 详解中类似的组织方式，我也会在一些地方用自己的话来阐明某些观点。</p>
<h3 data-id="heading-7">实现搜索树节点</h3>
<p><img alt="33.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f91d5c00928b45e1a42234879c3c8d36~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>为了存储从这些模拟中获得的统计信息，MCTS 从头开始建立了自己的搜索树。</p>
</blockquote>
<p>现在请你回顾<a href="https://en.wikipedia.org/wiki/Tree_(data_structure)" target="_blank" rel="nofollow noopener noreferrer">树结构</a>知识。MCTS 是一个树结构搜索，因此我们需要使用树节点。我们将在 <code>monte-carlo-node.js</code> 的 <code>MonteCarloNode</code> 类中实现这些节点。然后，我们将在 <code>MonteCarlo</code> 中使用它来构建搜索树。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** 代表搜索树中一个节点的类。 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MonteCarloNode</span> </span>&#123;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">parent, play, state, unexpandedPlays</span>)</span> &#123;
    
    <span class="hljs-built_in">this</span>.play = play
    <span class="hljs-built_in">this</span>.state = state

    <span class="hljs-comment">// 蒙特卡洛的内容</span>
    <span class="hljs-built_in">this</span>.n_plays = <span class="hljs-number">0</span>
    <span class="hljs-built_in">this</span>.n_wins = <span class="hljs-number">0</span>

    <span class="hljs-comment">// 树结构的内容</span>
    <span class="hljs-built_in">this</span>.parent = parent
    <span class="hljs-built_in">this</span>.children = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> play <span class="hljs-keyword">of</span> unexpandedPlays) &#123;
      <span class="hljs-built_in">this</span>.children.set(play.hash(), &#123; <span class="hljs-attr">play</span>: play, <span class="hljs-attr">node</span>: <span class="hljs-literal">null</span> &#125;)
    &#125;
  &#125;

  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先再确认一下是否能够理解这些：</p>
<ul>
<li><code>parent</code> 是 <code>MonteCarloNode</code> 父节点。</li>
<li><code>play</code> 是指从父节点到这个节点所做的 <code>Play</code>。</li>
<li><code>state</code> 是指与该节点相关联的游戏 <code>State</code>。</li>
<li><code>unexpandedPlays</code> 是 <code>Plays</code> 的一个合法数组，可以从这个节点进行。</li>
<li><code>this.children</code> 是由 <code>unexpandedPlays</code> 创建的，是 <code>Plays</code> 指向子节点 <code>MonteCarloNodes</code> 的一个 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map" target="_blank" rel="nofollow noopener noreferrer">Map</a> 对象（不完全是，见下文）。</li>
</ul>
<p><code>MonteCarloNode.children</code> 是一个从游戏哈希到对象的映射，包含游戏对象和相关的子节点。我们在这里包含了游戏对象，以便从它们的哈希中恢复游戏对象。</p>
<p>重要的是，<code>Play</code> 和 <code>State</code> 应该提供 <code>hash()</code> 方法。我们将在一些地方使用这些哈希作为 JavaScript 的 Map 对象，比如在 <code>MonteCarloNode.children</code> 中。</p>
<p>请注意，两个 <code>State</code> 对象应该被 <code>State.hash()</code> 认为是不同的 —— 即使它们有相同的棋盘状态 —— 如果每个对象通过<strong>不同的下棋顺序</strong>达到相同的棋盘状态。考虑到这一点，我们可以简单地让 <code>State.hash()</code> 返回一个字符串化的 <code>Play</code> 对象的有序数组，代表为达到该状态而下的棋。如果你获取了我的 <code>state-c4.js</code>，这个已经完成了。</p>
<p>现在我们将为 <code>MonteCarloNode</code> 添加成员方法。</p>
<pre><code class="hljs language-js copyable" lang="js">  ...

  <span class="hljs-comment">/** 获取对应于给定游戏的 MonteCarloNode。 */</span>
  <span class="hljs-function"><span class="hljs-title">childNode</span>(<span class="hljs-params">play</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 MonteCarloNode</span>
  &#125;

  <span class="hljs-comment">/** 展开指定的 child play，并返回新的 child node。*/</span>
  <span class="hljs-function"><span class="hljs-title">expand</span>(<span class="hljs-params">play, childState, unexpandedPlays</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 MonteCarloNode</span>
  &#125;

  <span class="hljs-comment">/** 从这个节点 node 获取所有合法的 play。*/</span>
  <span class="hljs-function"><span class="hljs-title">allPlays</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 Play[]</span>
  &#125;

  <span class="hljs-comment">/** 从这个节点 node 获取所有未展开的合法 play。 */</span>
  <span class="hljs-function"><span class="hljs-title">unexpandedPlays</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 Play[]</span>
  &#125;

  <span class="hljs-comment">/** 该节点是否完全展开。 */</span>
  <span class="hljs-function"><span class="hljs-title">isFullyExpanded</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 bool</span>
  &#125;

  <span class="hljs-comment">/** 该节点 node 在游戏树中是否为终端，
    不包括因获胜而终止游戏。 */</span>
  <span class="hljs-function"><span class="hljs-title">isLeaf</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 bool</span>
  &#125;
  
  <span class="hljs-comment">/** 获取该节点 node 的 UCB1 值。 */</span>
  <span class="hljs-function"><span class="hljs-title">getUCB1</span>(<span class="hljs-params">biasParam</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 number</span>
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = MonteCarloNode
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法可真多!</p>
<p>特别是，<code>MonteCarloNode.expand()</code> 将 <code>MonteCarloNode.children</code> 中未展开的空节点替换为实节点。这个方法将是四阶段的 MCTS 算法中<strong>阶段二：扩展</strong>的一部分，其他方法自行理解。</p>
<p>通常你可以自己实现这些，也可以获取完成的 <a href="https://github.com/quasimik/medium-mcts/blob/master/monte-carlo-node.js" target="_blank" rel="nofollow noopener noreferrer"><code>monte-carlo-node.js</code></a>。即使你自己做，我也建议在继续之前对照我完成的程序进行检查，以确保正常运行。</p>
<p>如果你刚获取到我完成的程序，请快速浏览一下源代码，就当是另一个心理检查点，重新梳理你的整体理解。这些都是简短的方法，你会在短时间内看懂它们。</p>
<p><img alt="44.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50f3086df1d0481c92a3fdb591723ab7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>尤其是 <code>MonteCarloNode.getUCB1()</code> 几乎是将上面的公式直接翻译成代码。这整个公式在上一篇文章中有详细的解释，再去看一下吧，这并不难理解，也是值得看的。</p>
<h3 data-id="heading-8">更新蒙特卡洛的类</h3>
<p>目前的版本是 <a href="https://github.com/quasimik/medium-mcts/blob/master/monte-carlo-v1.js" target="_blank" rel="nofollow noopener noreferrer">monte-carlo-v1.js</a>，只是一个骨架文件。该类的第一个更新是增加 <code>MonteCarloNode</code>，并创建一个构造函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MonteCarloNode = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./monte-carlo-node.js'</span>)

<span class="hljs-comment">/** 表示蒙特卡洛搜索树的类。 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MonteCarlo</span> </span>&#123;
    
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">game, UCB1ExploreParam = <span class="hljs-number">2</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.game = game
    <span class="hljs-built_in">this</span>.UCB1ExploreParam = UCB1ExploreParam
    <span class="hljs-built_in">this</span>.nodes = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>() <span class="hljs-comment">// map: State.hash() => MonteCarloNode</span>
  &#125;

  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>MonteCarlo.nodes</code> 允许我们获取任何给定状态的节点，这将是有用的。至于其他的成员变量，将它们与 <code>MonteCarlo</code> 联系起来就很有意义了。</p>
<pre><code class="hljs language-js copyable" lang="js">  ...

  <span class="hljs-comment">/** 如果给定的状态不存在，就创建空节点。 */</span>
  <span class="hljs-function"><span class="hljs-title">makeNode</span>(<span class="hljs-params">state</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.nodes.has(state.hash())) &#123;
      <span class="hljs-keyword">let</span> unexpandedPlays = <span class="hljs-built_in">this</span>.game.legalPlays(state).slice()
      <span class="hljs-keyword">let</span> node = <span class="hljs-keyword">new</span> MonteCarloNode(<span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, state, unexpandedPlays)
      <span class="hljs-built_in">this</span>.nodes.set(state.hash(), node)
    &#125;
  &#125;

  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码让我们可以创建根节点，还可以创建任意节点，这可能很有用。</p>
<pre><code class="hljs language-js copyable" lang="js">  ...

  <span class="hljs-comment">/** 从给定的状态，反复运行 MCTS 来建立统计数据。 */</span>
  <span class="hljs-function"><span class="hljs-title">runSearch</span>(<span class="hljs-params">state, timeout = <span class="hljs-number">3</span></span>)</span> &#123;

    <span class="hljs-built_in">this</span>.makeNode(state)

    <span class="hljs-keyword">let</span> end = <span class="hljs-built_in">Date</span>.now() + timeout * <span class="hljs-number">1000</span>
    <span class="hljs-keyword">while</span> (<span class="hljs-built_in">Date</span>.now() < end) &#123;

      <span class="hljs-keyword">let</span> node = <span class="hljs-built_in">this</span>.select(state)
      <span class="hljs-keyword">let</span> winner = <span class="hljs-built_in">this</span>.game.winner(node.state)

      <span class="hljs-keyword">if</span> (node.isLeaf() === <span class="hljs-literal">false</span> && winner === <span class="hljs-literal">null</span>) &#123;
        node = <span class="hljs-built_in">this</span>.expand(node)
        winner = <span class="hljs-built_in">this</span>.simulate(node)
      &#125;
      <span class="hljs-built_in">this</span>.backpropagate(node, winner)
    &#125;
  &#125;

  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，我们来到了算法的核心部分。引用<a href="https://medium.com/@quasimik/monte-carlo-tree-search-applied-to-letterpress-34f41c86e238" target="_blank" rel="nofollow noopener noreferrer">第一篇文章</a>的内容，以下是过程描述：</p>
<ol>
<li>在第 (1) 阶段，利用现有的信息反复选择连续的子节点，直至搜索树的末端。</li>
<li>接下来，在第 (2) 阶段，通过增加一个节点来扩展搜索树。</li>
<li>然后，在第 (3) 阶段，模拟运行到最后，决定胜负。</li>
<li>最后，在第 (4) 阶段，所选路径中的所有节点都会用模拟游戏中获得的新信息进行更新。</li>
</ol>
<p>这四个阶段的算法反复运行，直至收集到足够的信息，产生一个好的移动结果。</p>
<pre><code class="hljs language-js copyable" lang="js">  ...

  <span class="hljs-comment">/** 从现有的统计数据中获得最佳的移动。 */</span>
  <span class="hljs-function"><span class="hljs-title">bestPlay</span>(<span class="hljs-params">state</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 play</span>
  &#125;

  <span class="hljs-comment">/** 第一阶段：选择。选择直到不完全展开或叶节点。 */</span>
  <span class="hljs-function"><span class="hljs-title">select</span>(<span class="hljs-params">state</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 node</span>
  &#125;

  <span class="hljs-comment">/** 第二阶段：扩展。随机展开一个未展开的子节点。 */</span>
  <span class="hljs-function"><span class="hljs-title">expand</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 childNode</span>
  &#125;

  <span class="hljs-comment">/** 第三阶段：模拟。游戏到终止状态，返回获胜者。 */</span>
  <span class="hljs-function"><span class="hljs-title">simulate</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
    <span class="hljs-comment">// 返回 winner</span>
  &#125;

  <span class="hljs-comment">/** 第四阶段：反向传播。更新之前的统计数据。 */</span>
  <span class="hljs-function"><span class="hljs-title">backpropagate</span>(<span class="hljs-params">node, winner</span>)</span> &#123;
    <span class="hljs-comment">// TODO</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来讲解四个阶段具体的实现方法，我们现在的版本是 <a href="https://github.com/quasimik/medium-mcts/blob/master/monte-carlo-v2.js" target="_blank" rel="nofollow noopener noreferrer">monte-carlo-v2.js</a>。</p>
<h3 data-id="heading-9">实现 MCTS 第一阶段：选择</h3>
<p><img alt="55.jpg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7dc5984a25cc4a12bba4e14085762c53~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>从搜索树的根节点开始，我们通过反复选择一个合法移动，前进到相应的子节点来向下移动。如果一个节点中的一个、几个或全部合法移动在搜索树中没有对应的节点，我们就停止选择。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  ...  

  <span class="hljs-comment">/** 第一阶段：选择。选择直到不完全展开或叶节点。 */</span>
  <span class="hljs-function"><span class="hljs-title">select</span>(<span class="hljs-params">state</span>)</span> &#123;

    <span class="hljs-keyword">let</span> node = <span class="hljs-built_in">this</span>.nodes.get(state.hash())
    <span class="hljs-keyword">while</span>(node.isFullyExpanded() && !node.isLeaf()) &#123;

      <span class="hljs-keyword">let</span> plays = node.allPlays()
      <span class="hljs-keyword">let</span> bestPlay
      <span class="hljs-keyword">let</span> bestUCB1 = -<span class="hljs-literal">Infinity</span>

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> play <span class="hljs-keyword">of</span> plays) &#123;
        <span class="hljs-keyword">let</span> childUCB1 = node.childNode(play)
                            .getUCB1(<span class="hljs-built_in">this</span>.UCB1ExploreParam)
        <span class="hljs-keyword">if</span> (childUCB1 > bestUCB1) &#123;
          bestPlay = play
          bestUCB1 = childUCB1
        &#125;
      &#125;
      node = node.childNode(bestPlay)
    &#125;
    <span class="hljs-keyword">return</span> node
  &#125;

  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该函数通过查询每个子节点的 UCB1 值，使用现有的 UCB1 统计。选择 UCB1 值最高的子节点，然后对所选子节点的子节点重复这个过程，以此类推。</p>
<p>当循环终止时，保证所选节点至少有一个未展开的子节点，除非该节点是叶子节点。这种情况是由调用函数 <code>MonteCarlo.runSearch()</code> 处理的，所以我们在这里不必担心。</p>
<h3 data-id="heading-10">实现 MCTS 第二阶段：扩展</h3>
<p><img alt="66.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd12b1e954d34ac796355016e5852865~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>停止选择后，搜索树中至少会有一个未展开的移动。现在，我们随机选择其中的一个，然后我们创建该移动对应的子节点（图中加粗）。我们将这个节点作为子节点添加到选择阶段最后选择的节点上，扩展搜索树。节点中的统计信息初始化为 <code>0</code> 次模拟中的 <code>0</code> 次胜利。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  ...

  <span class="hljs-comment">/** 第二阶段：扩展。随机展开一个未展开的子节点。 */</span>
  <span class="hljs-function"><span class="hljs-title">expand</span>(<span class="hljs-params">node</span>)</span> &#123;

    <span class="hljs-keyword">let</span> plays = node.unexpandedPlays()
    <span class="hljs-keyword">let</span> index = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * plays.length)
    <span class="hljs-keyword">let</span> play = plays[index]

    <span class="hljs-keyword">let</span> childState = <span class="hljs-built_in">this</span>.game.nextState(node.state, play)
    <span class="hljs-keyword">let</span> childUnexpandedPlays = <span class="hljs-built_in">this</span>.game.legalPlays(childState)
    <span class="hljs-keyword">let</span> childNode = node.expand(play, childState, childUnexpandedPlays)
    <span class="hljs-built_in">this</span>.nodes.set(childState.hash(), childNode)

    <span class="hljs-keyword">return</span> childNode
  &#125;

  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来看一下 <code>MonteCarlo.runSearch()</code>。扩展是在检查 <code>if (node.isLeaf() === false && winner === null)</code> 时完成的。很明显，如果在游戏树中没有可能的子节点 —— 例如，当棋盘满了的时候，是不可能进行扩展的。如果有赢家的话，我们也不想扩展 —— 这就像说当你的对手赢了的时候你应该停止玩游戏一样明显。</p>
<p>那么如果是叶子节点，会发生什么呢？我们只需用在该节点中获胜的人进行反向传播 —— 无论是玩家 <code>1</code>，玩家 <code>-1</code>，甚至是 <code>0</code>（平局）。同样，如果在任何节点上有一个非空的赢家，我们只需跳过扩展和模拟，并立即与该赢家（<code>1</code> 或 <code>-1</code> 或 <code>0</code>）进行反向传播。</p>
<p>反向传播 <code>0</code> 赢家是什么意思？用 MCTS 真的可以吗？真的可以用，后面再细讲。</p>
<h3 data-id="heading-11">实现 MCTS 第三阶段：模拟</h3>
<p><img alt="77.jpg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11fb945d1edd40e2ae354c7a8b05eb39~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>从扩张阶段新建立的节点开始，随机选择棋步，反复推进对局状态。这样重复进行，直到对局结束，出现赢家。在此阶段不创建新节点。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  ...
  
  <span class="hljs-comment">/** 第三阶段：模拟。游戏到终止状态，返回获胜者。 */</span>
  <span class="hljs-function"><span class="hljs-title">simulate</span>(<span class="hljs-params">node</span>)</span> &#123;

    <span class="hljs-keyword">let</span> state = node.state
    <span class="hljs-keyword">let</span> winner = <span class="hljs-built_in">this</span>.game.winner(state)

    <span class="hljs-keyword">while</span> (winner === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">let</span> plays = <span class="hljs-built_in">this</span>.game.legalPlays(state)
      <span class="hljs-keyword">let</span> play = plays[<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * plays.length)]
      state = <span class="hljs-built_in">this</span>.game.nextState(state, play)
      winner = <span class="hljs-built_in">this</span>.game.winner(state)
    &#125;

    <span class="hljs-keyword">return</span> winner
  &#125;

  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为这里没有保存任何东西，所以这主要涉及到 <code>Game</code>，而 <code>MonteCarloNode</code> 的内容不多。</p>
<p>再看一下 <code>MonteCarlo.runSearch()</code>，模拟是在与扩展一样的检查 <code>if (node.isLeaf() === false && winner === null)</code> 时完成的。原因是：如果这两个条件之一成立，那么最后的赢家就是当前节点的赢家，我们只是用这个赢家进行反向传播。</p>
<h3 data-id="heading-12">实现 MCTS 第四阶段：反转</h3>
<p><img alt="88.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db24e476cf7e4d00a298691a2d9c5f57~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>模拟阶段结束后，所有被访问的节点（图中粗体）的统计数据都会被更新。每个被访问的节点的模拟次数都会递增。根据哪个玩家获胜，其获胜次数也可能递增。在图中，<strong>蓝节点</strong>赢了，所以每个被访问的<strong>红节点</strong>的胜利数都会递增。这种反转是由于每个节点的统计数据是用于其<strong>父节点</strong>的选择，而不是它自己的。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  ...

  <span class="hljs-comment">/** 第四阶段：反向传播。更新之前的统计数据。 */</span>
  <span class="hljs-function"><span class="hljs-title">backpropagate</span>(<span class="hljs-params">node, winner</span>)</span> &#123;
    <span class="hljs-keyword">while</span> (node !== <span class="hljs-literal">null</span>) &#123;
      node.n_plays += <span class="hljs-number">1</span>
      <span class="hljs-comment">// 父节点的选择</span>
      <span class="hljs-keyword">if</span> (node.state.isPlayer(-winner)) &#123;
        node.n_wins += <span class="hljs-number">1</span>
      &#125;
      node = node.parent
    &#125;
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = MonteCarlo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是影响下一次迭代搜索中选择阶段的部分。请注意，这假设是一个两人游戏，允许在 <code>node.state.isPlayer(-winner)</code> 中进行反转。你也许可以把这个函数泛化为 <strong>n</strong> 人游戏，做成 <code>node.parent.state.isPlayer(winner)</code> 之类的。</p>
<p>想一想，反向传播 <code>0</code> 赢家是什么意思？这相当于一盘平局，每个访问节点的 <code>n_plays</code> 统计数据都会增加，而玩家 <code>1</code> 和玩家 <code>-1</code> 的 <code>n_wins</code> 统计数据都不会增加。这种更新的行为就像<strong>两败俱伤</strong>的游戏，将选择推向其他游戏。最后，以平局结束的游戏和以失败结束的游戏一样，都有可能得不到充分的开发。这并没有破坏任何东西，但它导致了当平局比输棋更可取时的次优发挥。一个快速的解决方法是在平局时将双方的 <code>n_wins</code> 递增一半。</p>
<h2 data-id="heading-13">实现最佳游戏选择</h2>
<p><img alt="99.jpg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e557ee6d64ac48e7919ba68aa30edf24~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>MCTS(UCT) 的妙处在于，由于它的不对称性，树的选择和成长逐渐趋向于更好的移动。最后，你得到模拟次数最多的子节点，那就是你根据 MCTS 的最佳移动结果。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  ...
  
  <span class="hljs-comment">/** 从现有的统计数据中获得最佳的移动结果。 */</span>  
  <span class="hljs-function"><span class="hljs-title">bestPlay</span>(<span class="hljs-params">state</span>)</span> &#123;

    <span class="hljs-built_in">this</span>.makeNode(state)

    <span class="hljs-comment">// 如果不是所有的子节点都被扩展，则信息不足</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.nodes.get(state.hash()).isFullyExpanded() === <span class="hljs-literal">false</span>)
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Not enough information!"</span>)

    <span class="hljs-keyword">let</span> node = <span class="hljs-built_in">this</span>.nodes.get(state.hash())
    <span class="hljs-keyword">let</span> allPlays = node.allPlays()
    <span class="hljs-keyword">let</span> bestPlay
    <span class="hljs-keyword">let</span> max = -<span class="hljs-literal">Infinity</span>

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> play <span class="hljs-keyword">of</span> allPlays) &#123;
      <span class="hljs-keyword">let</span> childNode = node.childNode(play)
      <span class="hljs-keyword">if</span> (childNode.n_plays > max) &#123;
        bestPlay = play
        max = childNode.n_plays
      &#125;
    &#125;

    <span class="hljs-keyword">return</span> bestPlay
  &#125;

  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，选择最佳玩法有不同的策略。这里所采用的策略在文献中叫做 <strong><code>robust child</code></strong>，选择最高的 <code>n_plays</code>。另一种策略是 <strong><code>max child</code></strong>，选择最高的胜率 <code>n_wins/n_plays</code>。</p>
<h2 data-id="heading-14">实现统计自检和显示</h2>
<p>现在，你应该可以在当前版本 <a href="https://github.com/quasimik/medium-mcts/blob/master/index-v1.js" target="_blank" rel="nofollow noopener noreferrer"><code>index-v1.js</code></a> 上运行 <code>node index.js</code>。但是，你不会看到很多东西。要想看到里面发生了什么，我们需要完成以下事情。</p>
<p>在 <code>monte-carlo.js</code> 文件中:</p>
<pre><code class="hljs language-js copyable" lang="js">  ...  
  
  <span class="hljs-comment">// 工具方法</span>

  <span class="hljs-comment">/** 返回该节点和子节点的 MCTS 统计信息 */</span>
  <span class="hljs-function"><span class="hljs-title">getStats</span>(<span class="hljs-params">state</span>)</span> &#123;

    <span class="hljs-keyword">let</span> node = <span class="hljs-built_in">this</span>.nodes.get(state.hash())
    <span class="hljs-keyword">let</span> stats = &#123; <span class="hljs-attr">n_plays</span>: node.n_plays, 
                  <span class="hljs-attr">n_wins</span>: node.n_wins, 
                  <span class="hljs-attr">children</span>: [] &#125;
    
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> child <span class="hljs-keyword">of</span> node.children.values()) &#123;
      <span class="hljs-keyword">if</span> (child.node === <span class="hljs-literal">null</span>) 
        stats.children.push(&#123; <span class="hljs-attr">play</span>: child.play, 
                              <span class="hljs-attr">n_plays</span>: <span class="hljs-literal">null</span>, 
                              <span class="hljs-attr">n_wins</span>: <span class="hljs-literal">null</span>&#125;)
      <span class="hljs-keyword">else</span> 
        stats.children.push(&#123; <span class="hljs-attr">play</span>: child.play, 
                              <span class="hljs-attr">n_plays</span>: child.node.n_plays, 
                              <span class="hljs-attr">n_wins</span>: child.node.n_wins&#125;)
    &#125;

    <span class="hljs-keyword">return</span> stats
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = MonteCarlo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这让我们可以查询一个节点及其直接子节点的统计数据。做完这些，我们就完成了 <code>MonteCarlo</code>。你可以用你所拥有的东西来运行，也可以选择获取我完成的 <a href="https://github.com/quasimik/medium-mcts/blob/master/monte-carlo.js" target="_blank" rel="nofollow noopener noreferrer"><code>monte-carlo.js</code></a>。请注意，在我完成的版本中，<code>bestPlay()</code> 上有一个额外的参数来控制使用的最佳玩法策略。</p>
<p>现在，将 <code>MonteCarlo.getStats()</code> 整合到 <code>index.js</code> 中，或者获取我的完整版 <a href="https://github.com/quasimik/medium-mcts/blob/master/index.js" target="_blank" rel="nofollow noopener noreferrer"><code>index.js</code></a> 文件。</p>
<p>接着运行 <code>node index.js</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> node index.js</span>

player: 1
[ [ 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0 ] ]
&#123; n_plays: 3996,
  n_wins: 1664,
  children: 
   [ &#123; play: Play_C4 &#123; row: 5, col: 0 &#125;, n_plays: 191, n_wins: 85 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 1 &#125;, n_plays: 513, n_wins: 287 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 2 &#125;, n_plays: 563, n_wins: 320 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 3 &#125;, n_plays: 1705, n_wins: 1094 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 4 &#125;, n_plays: 494, n_wins: 275 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 5 &#125;, n_plays: 211, n_wins: 97 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 6 &#125;, n_plays: 319, n_wins: 163 &#125; ] &#125;
chosen play: Play_C4 &#123; row: 5, col: 3 &#125;

player: 2
[ [ 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 1, 0, 0, 0 ] ]
&#123; n_plays: 6682,
  n_wins: 4239,
  children: 
   [ &#123; play: Play_C4 &#123; row: 5, col: 0 &#125;, n_plays: 577, n_wins: 185 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 1 &#125;, n_plays: 799, n_wins: 277 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 2 &#125;, n_plays: 1303, n_wins: 495 &#125;,
     &#123; play: Play_C4 &#123; row: 4, col: 3 &#125;, n_plays: 1508, n_wins: 584 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 4 &#125;, n_plays: 1110, n_wins: 410 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 5 &#125;, n_plays: 770, n_wins: 265 &#125;,
     &#123; play: Play_C4 &#123; row: 5, col: 6 &#125;, n_plays: 614, n_wins: 200 &#125; ] &#125;
chosen play: Play_C4 &#123; row: 4, col: 3 &#125;

...

winner: 2
[ [ 0, 0, 2, 2, 2, 0, 0 ],
  [ 1, 0, 2, 2, 1, 0, 1 ],
  [ 2, 0, 2, 1, 1, 2, 2 ],
  [ 1, 0, 1, 1, 2, 1, 1 ],
  [ 2, 0, 2, 2, 1, 2, 1 ],
  [ 1, 0, 2, 1, 1, 2, 1 ] ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完美！</p>
<h2 data-id="heading-15">总结</h2>
<p>本文主要讲述如何使用 Node.js 实现蒙特卡洛树搜索，希望大家喜欢。下一篇文章将介绍如何优化，以及蒙特卡洛树搜索（MCTS）的现状。</p>
<p>感谢你的阅读！</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            