
---
title: '国外教授的讲义都是自己用 LaTeX 打出来的吗？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D%2C%5Cmathbb%7BC%7D'
author: 知乎
comments: false
date: Tue, 18 May 2021 18:02:58 GMT
thumbnail: 'https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D%2C%5Cmathbb%7BC%7D'
---

<div>   
lilyyyyz的回答<br><br><p>5.19 竟然有好多人看，那我就来补充点能提高效率的排版干货吧。（仅适用于<b>初学者</b> 因为我也是</p><p>想到啥就写啥了，顺序可能有点乱，大家见谅！</p><ul><li>针对于有理数集，无理数集等等（ <img src="https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D%2C%5Cmathbb%7BC%7D" alt="\mathbb&#123;R&#125;,\mathbb&#123;C&#125;" eeimg="1" referrerpolicy="no-referrer"> ...）这样打起来比较耗时的符号，可以一开始在文件开头定义其简化形式，比如说</li></ul><div class="highlight"><pre><code class="language-tex"><span><span class="k">\def\ZZ</span><span class="nb">&#123;&#123;</span><span class="k">\mathbb</span> Z<span class="nb">&#125;&#125;</span>
<span class="k">\def\RR</span><span class="nb">&#123;&#123;</span><span class="k">\mathbb</span> R<span class="nb">&#125;&#125;</span>
<span class="k">\def\CC</span><span class="nb">&#123;&#123;</span><span class="k">\mathbb</span> C<span class="nb">&#125;&#125;</span>
<span class="k">\def\QQ</span><span class="nb">&#123;&#123;</span><span class="k">\mathbb</span> Q<span class="nb">&#125;&#125;</span>
<span class="k">\def\EE</span><span class="nb">&#123;&#123;</span><span class="k">\mathbb</span> E<span class="nb">&#125;&#125;</span>
</span></code></pre></div><p>这也同样适用于别的math alphabets，只要确保定义的时候没有重复定义就可以了，先不一一列举了。</p><ul><li>刚刚翻阅自己field笔记的时候发现，经常会出现 "<>" 这个符号，个人感觉(强迫症)还是打成标准的写法舒服一点，<img src="https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D_5%5Bx%5D%2F%5Clangle+p%28x%29%5Crangle" alt="\mathbb&#123;Z&#125;_5[x]/\langle p(x)\rangle" eeimg="1" referrerpolicy="no-referrer"> 和 <img src="https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D_5%5Bx%5D%2F%3C+p%28x%29%3E" alt="\mathbb&#123;Z&#125;_5[x]/< p(x)>" eeimg="1" referrerpolicy="no-referrer"> 一比较，后者看起来太奇怪了。但是在写比较长的proof的时候，\langle \rangle 打起来太麻烦了，所以这个也可以简化一下，比如</li></ul><div class="highlight"><pre><code class="language-text"><span>\newcommand&#123;\la&#125;&#123;\langle&#125;
\newcommand&#123;\ra&#125;&#123;\rangle&#125;
</span></code></pre></div><ul><li>我个人喜欢在写pset的时候喜欢在proof或者是solution的最后加个小正方形，但是有时候会忘，所以可以直接定义一个新的environment。而且感觉\begin&#123;proof&#125; \end&#123;proof&#125;这个环境其实更有利于题目的定位啥的。下面的是我自己在用的：</li></ul><div class="highlight"><pre><code class="language-text"><span>\newenvironment&#123;proof&#125;&#123;\emph&#123;Proof.&#125;&#125;&#123;\hfill$\square$&#125;
</span></code></pre></div><ul><li>记不太清楚了，但是math writing用到的packages挺多的。印象里以前因为math package加的不全导致一些东西load不出来，不过方便起见，多塞点总没坏处。没管以下这些有没有duplicate的，我一直在modify之前自己的模版，所以我现在的模版里面放了这些东西 (to be updated)</li></ul><div class="highlight"><pre><code class="language-text"><span>\usepackage&#123;amsmath, amssymb&#125;  % standard packages for math writing
\usepackage&#123;listings&#125;   % include the contents of code files 
\usepackage&#123;mathpazo&#125; % a better font than the default
\usepackage&#123;mathtools&#125;
\usepackage&#123;enumitem&#125;
\usepackage&#123;amsthm&#125;
</span></code></pre></div><ul><li>这条算是第三条的一个补充，比较适用于写paper记笔记啥的，我看到蛮多textbooks也喜欢把definition或者theorem的内容斜体什么的（效果见下图），但是重复弄可能比较没有效率，所以也可以提前定义一下什么的。</li></ul><figure data-size="normal"><img src="https://pic2.zhimg.com/v2-95f83e2f5da61bb367766fa7df25cc7b_1440w.jpg" data-size="normal" data-rawwidth="832" data-rawheight="568" data-default-watermark-src="https://pic1.zhimg.com/v2-430d5a6475112d08442fc2b2f8bba27f_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic2.zhimg.com/v2-95f83e2f5da61bb367766fa7df25cc7b_r.jpg" referrerpolicy="no-referrer"><figcaption>从我大一spring的一门课的final project里面截的，请忽略内容。。。</figcaption></figure><p>code如下</p><div class="highlight"><pre><code class="language-text"><span>\newtheorem&#123;thm&#125;[equation]&#123;Theorem&#125;
\newtheorem&#123;cor&#125;[equation]&#123;Corollary&#125;
\newtheorem&#123;lemma&#125;[equation]&#123;Lemma&#125;
\newtheorem&#123;prop&#125;[equation]&#123;Proposition&#125;
\newtheorem&#123;conj&#125;[equation]&#123;Conjecture&#125;
\newtheorem&#123;definition&#125;[equation]&#123;Definition&#125;
\newtheorem&#123;remark&#125;[equation]&#123;Remark&#125;
\newtheorem&#123;example&#125;[equation]&#123;Example&#125;
</span></code></pre></div><ul><li>还有一些就是提高读者阅读质量的一些小心机，比如说给自己写的notes加点色彩什么的，效果请移步至我的文章，<a href="https://zhuanlan.zhihu.com/p/366956718" class="internal">大一实分析学习笔记｜（2）2019.9.4~2019.9.18</a>，当然我很难原创出这么好看的排版，很多想法是从大佬evan的笔记那里偷的。具体code我先挖个坑，到时候再补上。</li></ul><p>目前先写这么多！如果有想到的我会持续更新！</p><hr><p>我从高一刚接触latex的时候，打一篇两页的problem set 大概要整整一天，还是在非常专心的状态下。主要时间浪费在不熟悉math notation，不知道怎么enumerate，排版混乱，有时候不小心点到中文输入法（逗号，减号等等）搞的自己也不知道哪里错了。而且我那时候用的是最原始的编译器，所以debug速度很慢，经常乱码。</p><p>我觉得如果是入门的话，不妨用overleaf上面的模版，网上找一篇数学论文，你不用去理解它，照打，就像练打字一样，熟能生巧刚开始入门的问题就不会再犯了。也可以琢磨一些大佬的模版，尤其推荐Evan Chen的，可以在他的个人主页找到，是非常好的学习资料。</p><p>我刚开始上课用latex记笔记的时候，刚开始会存在跟不上教授讲课速度的问题。但不妨就先记上normal text，然后到课后再整理。熟练了以后上课跟记完全是没有什么问题的。我们平时的作业基本都要typeset，再加上一直在做很花里胡哨的指甲，完全不想写字，越用越习惯，比手写效率高多了。</p><p>ps：我目前大学的所有数学课教授的讲义确实是latex打的，都超好看，从中学了很多</p>  
</div>
            