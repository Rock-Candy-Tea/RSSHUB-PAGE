
---
title: 'React 状态管理策略_ 不, 应该是 React 组件管理策略'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eab0d54f25d041b4964a00d33ceee735~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 00:20:58 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eab0d54f25d041b4964a00d33ceee735~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在我的前几篇文章中, 我提到了现行 React 状态管理策略上的失败, 和社区的混乱, 在这篇文章中, 我会进一步剖析为什么 React 状态管理诉求的本质, 以及现行官方和社区策略的不可取的原因, 以及关于我们团队对于状态管理策略的探索和最新实践.</p>
<h2 data-id="heading-1">正文</h2>
<h3 data-id="heading-2">React 状态管理诉求的本质</h3>
<p>如果我们只聊 React 状态管理, 可能多数人都会各抒己见, 对于不同的策略大家难以达成共识, 因此, 让我们换一个角度, 从管理诉求的本质出发.</p>
<p>首先之所以要对某些事物进行管理, 其本质诉求在于被管理事物的数量和变量过于复杂导致, 我们谈到管理这个词, 从广义上来说包含</p>
<ul>
<li>事物的自我管理</li>
<li>狭义上的管理, 管理者和被管理者</li>
</ul>
<p>对于 React 状态来说, 此处的事物约等于 React 组件. 而状态是该组件的一部分.</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ReactComponent</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [state, setState] = useState(<span class="hljs-string">'jacky'</span>)
    <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;state&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们知道如果一个团队只有一个人, 那通常我们会不要求设立管理者, 对于 React 组件来说同样适用, 单个 React 组件, 拥有自己的状态 <code>name</code>, 组件自己管理自己的状态, 例如修改这个 name, 通过自身的 <code>Button</code></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ReactComponent</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [state, setState] = useState(<span class="hljs-string">'jacky'</span>)
    onClick = <span class="hljs-function">() =></span> &#123;
        setState(<span class="hljs-string">'ann'</span>)
    &#125;
    <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;state&#125; <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onClick&#125;</span>></span> 修改 name = 'ann' <span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常这种自我管理的内聚状态是相对理想的. 换句话说, 如果变量和数量都来自于我们自身, 那么只要严于律己, 我们就不会出岔子. 在这个问题下, 最大的问题只是我们自己, 每个组件的状态管理策略倾向于, 自我严格.</p>
<p><em><strong>但任何情况下, 我们都不可能只有我们自己, 同样, 一个 React 应用天然包含非常多的组件, 于是状态管理的诉求就产生了</strong></em></p>
<h3 data-id="heading-3">管理 ≠ 领导</h3>
<p>和真实的团队管理诉求不同, 对于团队, 管理者不仅仅是管理, 更重要的在于正确领导团队, 但对于 <code>状态管理</code> 这件事单纯的只是管理, 因此我们要抛去我们所理解的团队管理中关于领导部分的感性的东西, 理性的看待管理这件事.</p>
<p>将一个应用看成是一个团队的话, 那么对于管理者而言, 首先要做的是让团队成员达成共识, 对于 React 组件来说就是 <code>状态同步</code></p>
<p>React 社区对于状态同步的主流理解和官方提供的管理策略一致, 通常我们称为 <code>状态提升</code></p>
<p>为此我编写了一个代码示例, 虽然大家都明白什么是状态提升, 但为了后面的例子作对比, 我将这些示例都列出来了</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fpedantic-fog-jirz9%3Ffile%3D%2Fsrc%2Fexample4.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/pedantic-fog-jirz9?file=/src/example4.js" ref="nofollow noopener noreferrer">代码示例</a></p>
<p>在 example1 中, 演示了, 两个普通的 React 组件 A 和 B, 他们被包裹在 Example1 中, example2 解释了什么是 <code>状态提升</code>, 就是我们日常做的最多的事情, 将 A 和 B 的状态剥离出来, 放到 Container 里, 同时通过 props 将状态下发到 A 和 B, 如果用图表示大致是这么个过程</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eab0d54f25d041b4964a00d33ceee735~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果仅从 React 团队自己的技术角度出发, 这或许没什么问题, 听起来也比较合理, 状态消费组件变得纯粹, Stateless, 而控制组件则变得聪明 Smart.</p>
<p>但事实上如果将这种策略放到团队管理上来看, 你会发现这是 <strong>何其愚蠢</strong></p>
<p>因为这会导致一个显而易见的问题, 团队的所有成员都失去了脑子, 完全依赖团队管理者做信息同步, 在简单的场景下尚可维持, 但随着团队(应用)的规模日益庞大, 你需要为任何两个需要状态同步的节点提供一个提升节点 Container.</p>
<p>而事实上, 我们真实的诉求, 只是让 B 能够同步 A 的状态, 但为此付出的代价是, 一个额外的 Container, 一份不存在的职责(状态提升后的额外管理), 将原本能够使用 state 解决的问题变成了, state → props → state.</p>
<p>那么既然多 Container 不可行, 是不是统一到一个 Container 就阔以了?</p>
<p>事实上, 那会导致更大的问题.</p>
<p><strong>中心化的单一 Container 会成为整个应用的瓶颈.</strong></p>
<h3 data-id="heading-4">状态是组件的一部分, 不可分割, 就好像脑子和身体, 拆开管理是不现实的.</h3>
<p>在我之前的文章中, 我一直秉持, 状态是组件的一部分, 独立的状态管理策略是不存在的, 或者说, 将状态从应用和组件中剥离出来管理这种模式本身就是不可维系和持续的.</p>
<p>单纯的状态管理本身只包含两个问题</p>
<ul>
<li>状态的同步</li>
<li>状态的切分</li>
</ul>
<p>事实上, 脱离了组件的范畴, 这两件事单独做, 一件也做不好, 社区目前的状态管理策略全都建立在一个前提之上 <code>状态是独立于组件之外的一部分</code></p>
<p>基于这个前提, 就会导致上述两个问题的无解, 即</p>
<ul>
<li>状态的同步需要额外的节点来建立通信关系</li>
<li>状态的切分永远无法 match 组件的切分</li>
</ul>
<p>由于 2B 业务的复杂性, 我们抛弃了社区一贯的思维, 我们认为 <code>不存在状态管理, 只有组件管理</code></p>
<h3 data-id="heading-5">基于组件管理状态</h3>
<p>在我编写的示例中的 Example3 和 Example4 解释了这一观点, 当我们在技术上视状态和组件为一体, 我们找到了上述问题的新解法, 同时解决了我提出的那两个核心命题</p>
<ul>
<li>状态同步不依赖额外节点</li>
<li>状态的切分天然和组件切分 match</li>
</ul>
<p>对于状态同步, 我们通过一个被称为 linkable 的特性来解决不同组件之间的状态同步问题, 同时在 Example4 中演示了如何使用 connect 来操作组件从而实现状态的同步, 如果用图来解释这一策略的话, 类似这样</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16f6f0b4094142e5af588b1e1adf17bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可以对比我之前的那张图, 关键在于我们通过新的前提和新的管理策略实现了组件通信结构的变化, 从 <code>树</code> 变成了 <code>单链表</code></p>
<h2 data-id="heading-6">后话</h2>
<p>我们团队一直在致力于探索和实践复杂应用下基于 React 的应用框架研发, 这部分是我们最近实践和思考的一部分内容, 做个分享, 抛砖引玉, 欢迎交流, 目前仅开源框架的一部分库, 如果你对后续的进展感兴趣, 欢饮 Star 关注我们 😁 附上链接 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkinop112365362%2Fstructured-react-hook" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/kinop112365362/structured-react-hook" ref="nofollow noopener noreferrer">github.com/kinop112365…</a></p></div>  
</div>
            