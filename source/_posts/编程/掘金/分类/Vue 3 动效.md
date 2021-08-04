
---
title: 'Vue 3 动效'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1b6a424d42744ce8cfe95b8ddcaa1d8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 23:40:20 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1b6a424d42744ce8cfe95b8ddcaa1d8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<hr>
<h2 data-id="heading-0">系列文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6992194951492665374" target="_blank" title="https://juejin.cn/post/6992194951492665374">Vue 3 基础</a></li>
<li><a href="https://juejin.cn/post/6992476452721524750" target="_blank" title="https://juejin.cn/post/6992476452721524750">Vue 3 动效</a></li>
</ul>
<hr>
<p>本文介绍 Vue 3 的元素进入（显示）/离开（隐藏）和列表（重排）的过渡动效实现方法，主要针对 🎉 <em>与 Vue 2 的不同点</em>。</p>
<p>Vue 支持的过渡动效主要是针对元素素进入（显示）/离开（隐藏）和列表（重排）的情况，基于 CSS3 的 <code>transition</code> 和 <code>animation</code> 属性实现的。</p>
<p>💡 对于其他过渡动效，以及在 web 上创建流畅的动画所需考虑的性能因素，可以参考官方文章<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.vuejs.org%2Fguide%2Ftransitions-overview.html" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.vuejs.org/guide/transitions-overview.html" ref="nofollow noopener noreferrer">这一章</a>。</p>
<p>Vue 中常见的触发动画的情况：</p>
<ul>
<li>条件渲染 <code>v-if</code> 或 <code>v-show</code> 切换，动态组件属性 <code>is</code> 切换</li>
<li>列表更新</li>
<li>状态更新</li>
</ul>
<h2 data-id="heading-1">元素进入/离开过渡</h2>
<p>Vue 提供内置组件 <strong><code><transition name="animationType"></transition></code> 作为容器</strong>，然后就可以有多种方法为包裹在其中的（直接子元素）元素设置进入/离开时的动画：</p>
<ul>
<li>自动为发生过渡的元素添加特定的 <code>class</code>（并在结束后移除相应的 <code>class</code> 属性），可以基于这些 <code>class</code> 属性使用 CSS 实现动画。而且可以定制 <code>class</code> 的属性值，便于集成第三方 CSS 动画库，如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fanimate.style%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://animate.style/" ref="nofollow noopener noreferrer">animate.css</a></li>
<li>在发生过渡同时触发相应的过渡钩子函数，便于通过 JS 实现动画，也可以集成第三方 JavaScript 动画库</li>
</ul>
<h3 data-id="heading-2">CSS 过渡</h3>
<p><strong>Vue 会在过渡的不同阶段，为元素插入 6 种不同后缀的 <code>class</code> 属性</strong>，可以使用这些 <code>class</code> 作为选择器，更精细地设置元素的在不同过渡阶段的样式：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1b6a424d42744ce8cfe95b8ddcaa1d8~tplv-k3u1fbpfcp-watermark.image" alt="transitions.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>🎉 <em><code>v-enter-from</code> 定义进入过渡的开始状态</em>，在元素被插入之前生效，在元素被插入之后的下一帧移除。</li>
<li><code>v-enter-active</code> 在整个进入过渡的阶段中应用，在过渡/动画完成之后移除。可以使用这个类名作为 CSS 选择器设置过渡效果，例如通过设置 CSS 属性 <code>transition</code> 定义进入过渡的过程时间，延迟或曲线函数。</li>
<li><code>v-enter-to</code> 定义进入过渡的结束状态。在元素被插入之后下一帧生效 (与此同时 <code>v-enter-from</code> 被移除)，在过渡/动画完成之后移除。</li>
<li>🎉 <em><code>v-leave-from</code> 定义离开过渡的开始状态</em>，在离开过渡被触发时立刻生效，下一帧被移除。</li>
<li><code>v-leave-active</code> 在整个离开过渡的阶段中应用，在过渡/动画完成之后移除。可以使用这个类名作为 CSS 选择器设置过渡效果，例如通过设置 CSS 属性 <code>transition</code> 定义离开过渡的过程时间，延迟和曲线函数。</li>
<li><code>v-leave-to</code>：离开过渡的结束状态。在离开过渡被触发之后下一帧生效 (与此同时 <code>v-leave-from</code> 被删除)，在过渡/动画完成之后移除。</li>
</ul>
<p>💡 以上 6 种不同后缀的 <code>class</code> 属性都使用了 <code>v-</code> 作为默认前缀，如果容器标签设置了属性 <code>name</code> 即 <code><transition name="animationType"></code>，则动态插入的 <code>class</code> 属性名称就会以 <code>animationType-</code> 为前缀，即 <code>v-enter</code> 会替换为 <code>animationType-enter</code>，记得设置样式时使用相应的前缀，而不是默认前缀 <code>v-</code>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"show = !show"</span>></span>
    Toggle show
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"slide-fade"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"show"</span>></span>hello<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Demo = &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;

Vue.createApp(Demo).mount(<span class="hljs-string">'#demo'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 可以设置不同的进入和离开动画   */</span>
<span class="hljs-comment">/* 设置持续时间和动画函数        */</span>
<span class="hljs-selector-class">.slide-fade-enter-active</span> &#123;
  <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.3s</span> ease-out;
&#125;

<span class="hljs-selector-class">.slide-fade-leave-active</span> &#123;
  <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.8s</span> <span class="hljs-built_in">cubic-bezier</span>(<span class="hljs-number">1</span>, <span class="hljs-number">0.5</span>, <span class="hljs-number">0.8</span>, <span class="hljs-number">1</span>);
&#125;

<span class="hljs-selector-class">.slide-fade-enter-from</span>,
<span class="hljs-selector-class">.slide-fade-leave-to</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(<span class="hljs-number">20px</span>);
  <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要用第三方的 CSS 动画库，如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fanimate.style%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://animate.style/" ref="nofollow noopener noreferrer">Animate.css</a>，一般需要在 DOM 元素上插入特定的类名来应用相应的 CSS 样式，可以在标签 <code><transition></transition></code> 上使用如下列出的 attribute，这样 Vue 会<strong>在过渡的相应阶段为容器内的变更的（直接子元素）元素添加相应的自定义过渡类名</strong>：</p>
<ul>
<li>🎉 <em><code>enter-from-class="custom-class-name"</code> 在元素进入页面前添加的类名</em></li>
<li><code>enter-active-class="custom-class-name"</code></li>
<li><code>enter-to-class="custom-class-name"</code></li>
<li>🎉 <em><code>leave-from-class="custom-class-name"</code></em></li>
<li><code>leave-active-class="custom-class-name"</code></li>
<li><code>leave-to-class="custom-class-name"</code></li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span>
  <span class="hljs-attr">href</span>=<span class="hljs-string">"https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.0/animate.min.css"</span>
  <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span>
  <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>
/></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"show = !show"</span>></span>
    Toggle render
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">transition</span>
    <span class="hljs-attr">name</span>=<span class="hljs-string">"custom-classes-transition"</span>
    <span class="hljs-attr">enter-active-class</span>=<span class="hljs-string">"animate__animated animate__tada"</span>
    <span class="hljs-attr">leave-active-class</span>=<span class="hljs-string">"animate__animated animate__bounceOutRight"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"show"</span>></span>hello<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Demo = &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;

Vue.createApp(Demo).mount(<span class="hljs-string">'#demo'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果使用 <code>animation</code> 属性实现动效，而不是 <code>transition</code> 控制过渡，则不需要指定 <code>v-enter-from</code>/<code>v-leave-from</code> 或 <code>v-enter-to</code>/<code>v-leave-to</code> 的状态，只需要在 <code>v-enter-active/v-leave-active</code> 过渡中设定 CSS 属性 <code>animation</code> 即可，其中在<strong>关键帧中指定了 <code>0%</code> 和 <code>100%</code> 状态时的样式</strong>就是开始和结束的状态</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"show = !show"</span>></span>
    Toggle show
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"bounce"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"show"</span>></span>hello<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Demo = &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;

Vue.createApp(Demo).mount(<span class="hljs-string">'#demo'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.bounce-enter-active</span> &#123;
  <span class="hljs-attribute">animation</span>: bounce-in <span class="hljs-number">0.5s</span>;
&#125;
<span class="hljs-selector-class">.bounce-leave-active</span> &#123;
  <span class="hljs-attribute">animation</span>: bounce-in <span class="hljs-number">0.5s</span> reverse;
&#125;
<span class="hljs-keyword">@keyframes</span> bounce-in &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0</span>);
  &#125;
  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1.25</span>);
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 Vue 可以自动得出过渡效果的完成时机，以「拔除」添加到元素上的相关的 <code>class</code> 类名，但是如果（不推荐）<strong>同时使用了 CSS 的属性 <code>trasition</code> 和 <code>animation</code> 设置动画</strong>，可能会因为两种过渡时间不同，比如 <code>animation</code> 很快的被触发并完成了，而 <code>transition</code> 效果还没结束，而出现一些意想不到的动画 Bug，这时候可以<strong>为容器添加选项 <code>type</code></strong> 并设置值为 <code>animation</code> 或 <code>transition</code> 来<strong>显式地声明你需要 Vue 监听的过渡动画类型</strong>；也可以在容器元素上通过 prop <strong>显式地指定持续时间（以毫秒计）</strong> <code><transition :duration="1000"></code>。</p>
<p>💡 动效如果在初次加载页面时不生效，可以为元素 <code><transition></code> 添加属性 <code>appear</code> 设置节点初始渲染的过渡。</p>
<h3 data-id="heading-3">钩子函数</h3>
<p>Vue 会在过渡的不同阶段同时触发相应事件，可以在内置组件 <code><transition></code> 监听这些事件，然后通过 JS 在事件处理函数中「手动」控制动画，一般是设置元素的 attribute 样式，或「对接」其他动画框架，例如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgreensock.com%2Fgsap%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://greensock.com/gsap/" ref="nofollow noopener noreferrer">gsap</a>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition</span>
  @<span class="hljs-attr">before-enter</span>=<span class="hljs-string">"beforeEnter"</span>
  @<span class="hljs-attr">enter</span>=<span class="hljs-string">"enter"</span>
  @<span class="hljs-attr">after-enter</span>=<span class="hljs-string">"afterEnter"</span>
  @<span class="hljs-attr">enter-cancelled</span>=<span class="hljs-string">"enterCancelled"</span>
  @<span class="hljs-attr">before-leave</span>=<span class="hljs-string">"beforeLeave"</span>
  @<span class="hljs-attr">leave</span>=<span class="hljs-string">"leave"</span>
  @<span class="hljs-attr">after-leave</span>=<span class="hljs-string">"afterLeave"</span>
  @<span class="hljs-attr">leave-cancelled</span>=<span class="hljs-string">"leaveCancelled"</span>
  <span class="hljs-attr">:css</span>=<span class="hljs-string">"false"</span>
></span>
  <span class="hljs-comment"><!-- ... --></span>
<span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-attr">methods</span>: &#123;
  <span class="hljs-comment">/*
   * 元素进入
   */</span>
  <span class="hljs-function"><span class="hljs-title">beforeEnter</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;,
  <span class="hljs-comment">// 当与 CSS 结合使用时</span>
  <span class="hljs-comment">// 回调函数 done 是可选的</span>
  <span class="hljs-function"><span class="hljs-title">enter</span>(<span class="hljs-params">el, done</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
    done()
  &#125;,
  <span class="hljs-function"><span class="hljs-title">afterEnter</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">enterCancelled</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;,

  <span class="hljs-comment">/*
   * 元素离开
   */</span>
  <span class="hljs-function"><span class="hljs-title">beforeLeave</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;,
  <span class="hljs-comment">// 当与 CSS 结合使用时</span>
  <span class="hljs-comment">// 回调函数 done 是可选的</span>
  <span class="hljs-function"><span class="hljs-title">leave</span>(<span class="hljs-params">el, done</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
    done()
  &#125;,
  <span class="hljs-function"><span class="hljs-title">afterLeave</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;,
  <span class="hljs-comment">// leaveCancelled 只用于 v-show 中</span>
  <span class="hljs-function"><span class="hljs-title">leaveCancelled</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>@before-enter="beforeEnter(el)"</code> 可以传递执行动画的元素</li>
<li><code>@enter="enter(el, done)"</code> 需要在回调函数中，<strong>在动画执行执行完成时调用 <code>done()</code> 告知 Vue 动画结束</strong>，必须执行一次 <code>done()</code>，否则它们将被同步调用，过渡会立即完成。</li>
<li><code>@after-enter="afterEnter"</code></li>
<li><code>@enter-cancelled="enterCancelled"</code> 元素离开页面触发的事件</li>
<li><code>@before-leave="beforeLeave"</code></li>
<li><code>@leave="leave"</code> 需要在回调函数中，<strong>在动画执行执行完成时调用 <code>done()</code> 告知 Vue 动画结束</strong>，必须执行一次 <code>done()</code>，否则它们将被同步调用，过渡会立即完成。</li>
<li><code>@after-leave="afterLeave"</code></li>
<li><code>@leave-cancelled="leaveCancelled"</code></li>
</ul>
<p>💡 虽然这些钩子函数可以结合 CSS transitions/animations 使用，也可以单独使用。如果仅使用 JS 过渡，推荐为 <code><transition></code> 添加 <code>v-bind:css="false"</code> 属性绑定，Vue 会跳过 CSS 的检测，这也可以避免过渡过程中受 CSS 的影响。</p>
<h3 data-id="heading-4">多个元素间过渡</h3>
<p>在多元素过渡时，<strong>默认模式是两个元素的进入&离开是同时进行的</strong>，可能会导致页面布局乱掉，可以将过渡模式改成 <strong><code><transition mode="out-in"></transition></code> 让当前元素先进行过渡离开，完成之后新元素过渡进入</strong>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"fade"</span> <span class="hljs-attr">mode</span>=<span class="hljs-string">"out-in"</span>></span>
  <span class="hljs-comment"><!-- ... the buttons ... --></span>
<span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 对于使用 <code>v-if</code>/<code>v-else</code> 实现的<strong>多元素之间进行切换</strong>时，🎉 <em>Vue 3 已经默认为 <code>v-if</code>/<code>v-else</code>/<code>v-else-if</code> 的各分支项自动生成唯一的 <code>key</code></em>，因此这些元素的 <code>key</code> 属性不再必要了，如果自己添加 <code>key</code> 属性时需要设置唯一可区分的值，否则相同标签名的元素之间切换时只会替换内部的内容，而不会进行触发整个元素切换过渡。</p>
<h2 data-id="heading-5">列表重排过渡</h2>
<p><strong>使用组件 <code><transition-group></transition-group></code> 作为容器，其内可以有多个节点</strong>（而 <code><transition></code> 只允许一个根节点，虽然可以包裹多个元素，但是每次 <code>v-if</code> 或 <code>v-show</code> 切换后，都只能渲染一个根节点），要记得其内部的各个节点<strong>总是需要提供属性 <code>key</code></strong> 作为唯一标识。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition-group</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"list"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"p"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in items"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-item"</span>></span>
    &#123;&#123; item &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">transition-group</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue 也是在过渡的不同阶段，为元素插入以上所述的 6 个不同后缀 <code>class</code>，可以使用这些 <code>class</code> 作为选择器设置样式。</p>
<ul>
<li>🎉 <em><code>v-enter-from</code></em></li>
<li><code>v-enter-active</code></li>
<li><code>v-enter-to</code></li>
<li>🎉 <em><code>v-leave-from</code></em></li>
<li><code>v-leave-active</code></li>
<li><code>v-leave-to</code></li>
</ul>
<p>此外还特别针对性地<strong>新增了后缀为 <code>v-move</code></strong> 的 <code>class</code> 类属性（如果设置了 <code>name</code> 属性 <code><transition-group name="animationType"></transition-group></code>，则列表重排时插入到列表项的 <code>class</code> 类属性的前缀就会改变，即为 <code>animationType-move</code>；还可以像之前的类名一样，即通过 <code>move-class</code> attribute 手动设置）。一般会通过 <code>v-move</code> 这个选择器<strong>设置 CSS 属性 <code>transform</code></strong> ，指定过渡 timing 和 easing 曲线，然后 Vue 会<strong>将元素从之前的位置平滑过渡新的位置</strong>，实现一个称为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Faerotwist.com%2Fblog%2Fflip-your-animations%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://aerotwist.com/blog/flip-your-animations/" ref="nofollow noopener noreferrer">FLIP</a> 的动画效果。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.15/lodash.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"flip-list-demo"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"shuffle"</span>></span>Shuffle<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition-group</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"flip-list"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"ul"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in items"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item"</span>></span>
      &#123;&#123; item &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">transition-group</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Demo = &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">items</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>]
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">shuffle</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 使用 lodash 的 shuffle 对列表元素进行重排</span>
      <span class="hljs-built_in">this</span>.items = _.shuffle(<span class="hljs-built_in">this</span>.items)
    &#125;
  &#125;
&#125;

Vue.createApp(Demo).mount(<span class="hljs-string">'#flip-list-demo'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.flip-list-move</span> &#123;
  <span class="hljs-attribute">transition</span>: transform <span class="hljs-number">0.8s</span> ease;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 🎉 <em>在 Vue 3 中，<code><transition-group></code> 默认不再渲染根节点</em>，但可以通过<strong>属性 <code>tag</code></strong> 来设置，例如 <code>tag="div"</code> 将使用 <code><div></code> 元素作为容器包装列表。</p>
<p>💡 FLIP 动效对于 <code>display: inline</code> 元素无效，对于行内元素，如 <code><span></code>，可以设置为 <code>display: inline-block</code></p>
<h2 data-id="heading-6">动态过渡</h2>
<p>Vue 是数据驱动画面的，因此过渡动效的类型也是可以基于数据进行变化的，如通过 <strong><code><transition :name="transitionName"></code> 将属性 name 绑定到变量，就可以实时操作动效的类型</strong>，因为事件钩子是方法，它们可以访问任何上下文中的数据，这意味着根据组件的状态不同，过渡可以有不同的表现，例如实现轮播图点击左右箭头时可以实现切换方向和过渡的不同。</p>
<h2 data-id="heading-7">状态过渡</h2>
<p>对于元素的<strong>内容/数据本身</strong>的改变也可以设置过渡动效，包括数字和运算、颜色的显示、SVG 节点的位置、元素的大小和其他的 property。</p>
<p>一般以<strong>数值</strong>表示的样式属性都可以设置动效，可以结合 Vue 的响应式和组件系统，使用第三方库来实现切换元素的过渡状态，如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftweenjs%2Ftween.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tweenjs/tween.js" ref="nofollow noopener noreferrer">tween.js</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgreensock.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://greensock.com/" ref="nofollow noopener noreferrer">gsap</a></p></div>  
</div>
            