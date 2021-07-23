
---
title: 'Composition over Inheritance 上篇：什么时候该用 Composition？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=3431'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 01:15:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=3431'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在学习编程的路上，尤其是学习面向对象（Object Oriented）之后，大家会接触一句话：</p>
<pre><code class="copyable">Composition over Inheritance
<span class="copy-code-btn">复制代码</span></code></pre>
<p>意为优先考略组合，而不是继承。有些程序员没懂，有些程序员把它奉为真理与黄金法则。</p>
<p>前日在做游戏开发（和我白天的工作无关，兴趣爱好而已），在对游戏对象建模时，我对这句话有了新的理解。Composition并不总是比Inheritance好。我领悟到了什么时候 Composition 好，什么时候 Inheritance 好。</p>
<p>本文讲述的例子和中心思想在Java、JavaScript、C++、Python、Go、C#等语言都适用。</p>
<p>先来想象这么一个场景，游戏中有不同的人（Person），不同的人可以用不同的职业（法师、战士等）。有些人并没有职业，就是最基础的人（普通村民）。</p>
<p>但是同一个人的职业是可以转换的。战士可以变成法师，或者变成普通村民。普通村民也可以变成战士。</p>
<p>如果没有经过太多思考，我们容易自然地觉得继承是一个不错的方案。</p>
<pre><code class="hljs language-TS copyable" lang="TS"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Fighter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>对于没有继承的语言，比如Go，来说，就是接口。这里的核心不是继承，而是多态。</p>
<p>这样利用多态的特性，我们可以将一个<code>Fighter</code>实例当作一个普通<code>Person</code>来用。比如游戏中所有人都可以喝水。</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">DrinkWater</span><span class="hljs-params">(Person p, Water w)</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么就可以有</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">var</span> f = <span class="hljs-built_in">new</span> Fighter()
DrinkWater(f, <span class="hljs-built_in">new</span> Water())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是多态的典型用法。这个特性有不同的表述方法。</p>
<ol>
<li>
<p>一个更具体类的实例，可以用在更抽象的地方。</p>
</li>
<li>
<p>如果把类理解为数学集合。那么派生类就是子集（元素少，更具体），基类就是超集（元素更多，更抽象）。一个函数如果接受某个集合的元素，那么必然接受该集合子集的元素。</p>
</li>
</ol>
<p>用游戏里的逻辑，就是所有人可以干的事情，战士都可以干。</p>
<p>目前来看用继承（多态）似乎是可行并且恰当的。</p>
<p>但是，当我想把一个普通村民升级为战士时，问题来了。继承只能让更大的实例被用作更小的实例（Type Shrinking），但是不能反过来！我唯一的办法是创建一个新的战士实例，将该村民的数据拷贝过去，再删除原村民的实例。</p>
<p>代码大致如此</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> f = <span class="hljs-keyword">new</span> Fighter()
f.data = person.data
<span class="hljs-keyword">delete</span> person
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的代码有至少两个问题：</p>
<ol>
<li>代码冗长，对于复杂的对象，需要更复杂的拷贝函数。容易出错。</li>
<li>更严重的问题是，程序中其他引用了原Person的地方不会被同时更新。如果删掉person实例，那些地方会出现空指针。如果不删，会出现数据不一致。</li>
</ol>
<p>由此可见，如果程序需要在运行时扩大一个对象的能力（比如将村民升级为战士），继承的结构是不利的。继承的能力传播是单向的，在运行时只能缩小一个对象的能力（战士当村民用），不能扩大。</p>
<p>同理，如下的封装虽然没有用继承，但是效果一样。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Fighter</span> </span>&#123;
  Person person;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个战士对象包含本身的人。这样本质上和<code>class Fighter extends Person</code>是一样的。都是基于</p>
<pre><code class="copyable">`Fighter`是一个大于`Person`的对象
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一个假设来建模的。</p>
<h2 data-id="heading-0">但是，真的是这样吗？</h2>
<p>如果我们同时想要动态扩大以及缩小的能力。需要另外一种建模思路。</p>
<p>战士是人的特殊数属性，而不是一种特殊的人。</p>
<p>这样我们可以得到完全相反的代码。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  Ability[] abilities;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Fighter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Ability</span> </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在普通村民包含了一个 Ability （能力）数组。战士只是一种能力而已。那么，当数组里有战士的实例，这个村民就可以做出战士的行为，如果没有，就不能。这也允许同一个村民拥有不同的职业和能力。我们能都知道多继承是多么恐怖，所以继承不适合类似逻辑的建模。</p>
<p>更加值得注意的一点是，<code>Ability</code>是不能单独实例化的，因为它是一个抽象的概念。可以用抽象类或者接口来实现。</p>
<p>所以，继承中的基类最好是无法单独实例化的，仅仅作为编译时的代码复用，而不是作为运行时的参与者。</p>
<h1 data-id="heading-1">总结</h1>
<p>如果程序需要让一个对象动态地增加能力，Composition（组合）是更好的方法。将这些“能力”数据化，作为可以被添加或者删除的对象。</p>
<p>如果程序仅仅需要动态地减少某对象的能力或者静态地代码复用，继承也许是非常不错的选择。我们下篇见。</p></div>  
</div>
            