
---
title: '全自动jQuery与渣男的故事'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c162d5e116914e4dba3b77330e13f1ec~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 01:24:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c162d5e116914e4dba3b77330e13f1ec~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是卡颂。</p>
<p>我是个恋旧的人，<code>Github</code>头像还是上古时期端游<strong>仙剑奇侠传</strong>的截图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c162d5e116914e4dba3b77330e13f1ec~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于前端，如果能<code>jQuery</code>一把梭，我是很开心的。</p>
<p><code>React</code>、<code>Vue</code>的普及让大家习惯了<code>虚拟DOM</code>的存在。但是<code>虚拟DOM</code>一定是最优解么？</p>
<p>举个例子，要进行如下<code>DOM</code>移动操作：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 变化前</span>
abcd
<span class="hljs-comment">// 变化后</span>
dabc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用<code>jQuery</code>时调用<code>insertBefore</code>把<code>d</code>挪到<code>a</code>前面就行。而<code>React</code>基于<code>虚拟DOM</code>的<code>Diff</code>会依次对<code>abc</code>执行<code>appendChild</code>，将他们依次挪到最后。</p>
<p>1次<code>DOM</code>操作 vs 3次<code>DOM</code>操作，显然前者更高效。</p>
<p>那么有没有框架能砍掉<code>虚拟DOM</code>，直接对<code>DOM</code>节点执行操作，实现全自动<code>jQuery</code>？</p>
<p>有的，这就是最近出的<code>petite-vue</code>。</p>
<p>阅读完本文，你会从原理层面了解该框架，如果你还有精力，可以在此基础上深入框架源码。</p>
<h2 data-id="heading-0">全自动jQuery的实现</h2>
<p>可以将原理概括为一句话：</p>
<blockquote>
<p>建立<code>状态</code>与<code>更新DOM的方法</code>之间的联系</p>
</blockquote>
<p>比如，对于如下<code>DOM</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"showName"</span>></span>我是卡颂<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>期望<code>showName</code>状态的变化能影响<code>p</code>的显隐（通过改变<code>diaplay</code>）。</p>
<p>实际是建立<strong>showName的变化</strong>与<strong>调用如下方法</strong>的联系：</p>
<pre><code class="hljs language-js copyable" lang="js">() => &#123;
  el.style.display = get() ? initialDisplay : <span class="hljs-string">'none'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>el</code>代表<code>p</code>，<code>get()</code>获取<code>showName</code>当前值。</p>
<p>再比如，对于如下<code>DOM</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-text</span>=<span class="hljs-string">"name"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>name</code>改变后<code>p</code>的<code>textContent</code>会变为对应值。</p>
<p>实际是建立<strong>name的变化</strong>与<strong>调用如下方法</strong>的联系：</p>
<pre><code class="hljs language-js copyable" lang="js">() => &#123;
  el.textContent = toDisplayString(get())
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，整个框架的工作原理呼之欲出：初始化时遍历所有<code>DOM</code>，根据各种<code>v-xx</code>属性建立<code>DOM</code>与<strong>操作DOM的方法</strong>之间的联系。</p>
<p>当改变状态后，会自动调用与其有关的<strong>操作DOM的方法</strong>，简直就是全自动<code>jQuery</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/769858bdfe9b450d8a1f0b32e4b18fde~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，框架的核心在于：如何建立联系？</p>
<h2 data-id="heading-1">一个渣男的故事</h2>
<p>这部分源码都收敛在<code>@vue/reactivity</code>库中。我并不想带你精读源码，因为这样很没意思，看了还容易忘。</p>
<p>接下来我会通过一个故事为你展示其工作原理，当你了解原理后如果感兴趣可以自己去看源码。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9f64239e92c409aa7d4a53eb3646b56~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们的目标是描述：<strong>状态变化</strong>与<strong>更新DOM的方法</strong>之间的联系。说得再宽泛点，是建立<code>状态</code>与<code>副作用</code>之间的联系。</p>
<p>即：状态变化 -> 执行副作用</p>
<p>对于一段关系，可以从当事双方的角度描述，比如：</p>
<p>男生指着女生说：这是我女朋友。</p>
<p>接着女生指着男生说：这是我男朋友。</p>
<p>你作为旁观者，通过双方的描述就知道他们处于一段恋爱关系。</p>
<p>推广到<code>状态</code>与<code>副作用</code>，则是：</p>
<p><code>副作用</code>指着<code>状态</code>说：我依赖这个<code>状态</code>，他变了我就会执行。</p>
<p><code>状态</code>指着<code>副作用</code>说：我订阅了这个<code>副作用</code>，当我变了后我会通知他。</p>
<blockquote>
<p>可以看到，发布订阅其实是对一段关系站在双方视角的阐述</p>
</blockquote>
<p>举个例子，如下<code>DOM</code>结构：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>=<span class="hljs-string">"&#123;num: 0&#125;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"num++"</span>></span>add 1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"num%2"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-text</span>=<span class="hljs-string">"num"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过<code>petite-vue</code>遍历后的关系图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90955f5cf3bb43e1ad0381bbb49ff56d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>框架的交互流程为：</p>
<ol>
<li>
<p>触发点击事件，状态<code>num</code>变化</p>
</li>
<li>
<p>通知其订阅的<code>副作用</code>（<code>effect1</code>与<code>effect2</code>），执行对应<code>DOM</code>操作</p>
</li>
</ol>
<p>如果从情侣关系角度解读，就是：</p>
<p><code>num</code>指着<code>effect1</code>说：这是我女朋友。</p>
<p><code>effect1</code>指着<code>num</code>说：这是我男朋友。</p>
<p><code>num</code>指着<code>effect2</code>说：这是我女朋友。</p>
<p><code>effect2</code>指着<code>num</code>说：这是我男朋友。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9d43387c01c47d58390add774f28e65~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">总结</h2>
<p>今天我们学习了一个框架<code>petite-vue</code>，他的底层实现由多段混乱的男女关系组成，上层是一个个直接操作<code>DOM</code>的方法。</p>
<p>不知道看完后你有没有兴趣深入了解下这种关系呢？</p>
<p>感兴趣的话可以看看<code>Vue Mastery</code>的<code>Vue 3 Reactivity</code>课程。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0275a1628a5443d88c20a034e85694a3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            