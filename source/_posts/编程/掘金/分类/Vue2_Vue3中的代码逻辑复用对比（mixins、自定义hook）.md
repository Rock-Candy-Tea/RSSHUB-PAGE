
---
title: 'Vue2_Vue3中的代码逻辑复用对比（mixins、自定义hook）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59cf63cef8cf4ae2a3f52b03416a1eb2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Apr 2021 22:40:04 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59cf63cef8cf4ae2a3f52b03416a1eb2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>mixins是Vue2.x Options API中常用的代码逻辑抽离手段，在Vue3.x中也同样可以使用。</p>
<p>虽然好用，但其仍有一些比较显著的缺点，而Vue3.x引入的Composition API中的自定义hook</p>
<p>很好的解决了mixins带来的一些问题，本文将简单的对比一下这两种实现手段。</p>
<h2 data-id="heading-1">mixins是什么？</h2>
<p>我们在开发组件的过程中，常常会遇到一些具有相同逻辑和功能的组件。</p>
<p>如果每个组件各写一套方法会导致代码冗余，后期更改的时候也要一个个的改非常的浪费时间和精力。</p>
<p>mixins就是将这些多个相同的逻辑抽离出来，各个组件只需要引入mixins，就能实现一次写代码，多组件受益的效果。</p>
<p><img alt="1.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59cf63cef8cf4ae2a3f52b03416a1eb2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">mixins如何使用？</h2>
<p><strong>基本使用步骤：</strong>
1.用一个js文件将vue的script部分抽离出来，如下示例（选项可以自由选择）</p>
<pre><code class="copyable">export default &#123;
  data()&#123;
    return &#123;&#125;
  &#125;,
  methods:&#123;&#125;,
  computed:&#123;&#125;,
  filters:&#123;&#125;,
  created()&#123;&#125;,
  mounted()&#123;
    console.log("我是mixins");
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.需要引入mixins的组件引入即可：</p>
<p><img alt="1.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de1eb0734cd448ed9b4aef4ba36c26dd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">mixins的一些特性：</h2>
<p><strong>1.mixins中的生命周期会与引入mixins的组件的生命周期整合在一起调用</strong></p>
<p><img alt="1.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c9920f96241416c9306fa998811c2b8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>2.组件的data、methods、filters会覆盖mixins里的同名data、methods、filters。</strong></p>
<pre><code class="copyable">组件的同名data 会覆盖 mixins的同名data
组件的同名methods 会覆盖 mixins的同名methods
组件的同名filters 会覆盖 mixins的同名filters

虽然是具有相同逻辑的组件，但是每个组件肯定不可能完全100%相同，会有不同的属性或者不同的methods或者filters等。

所以如果组件里没有写data/methods/filters……等的话，
会自动继承mixins里的data/methods/filters……。如果写了就会以组件里定义的data/methods/filters……为准。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.不同mixin里的同名方法，按照引进的顺序，最后的覆盖前面的同名方法。</strong></p>
<pre><code class="copyable">比如两个文件mixin1.js、mixin2.js
都有同名方法： test()
且我们的引入顺序是：[mixin1,mixin2]
那么最终执行的方法就是mixin2里的 test()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">mixins的缺点：</h2>
<p>1.变量来源不明确（隐式传入），不利于阅读，使代码变得难以维护。</p>
<pre><code class="copyable">组件里可以引入多个mixin，并直接隐式调用mixin里的变量/方法，
这会让我们有时候混乱 这些变量/方法 分别是哪个mixin里的？
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.多个mixins的生命周期会融合到一起运行，但是同名属性、同名方法无法融合，可能会导致冲突。</p>
<pre><code class="copyable">比如组件1中的方法要输出属性info，
但是组件2中也有同名属性info，且覆盖了组件1中的属性info，
那么当执行组件1中的方法时，输出的确实组件2中的属性，
这个我们可以避免，但是一不小心就会导致冲突，很容易制造混乱。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.mixins和组件可能出现多对多的关系，复杂度较高（即一个组件可以引用多个mixins，一个mixins也可以被多个组件引用）。</p>
<p>注：VUE3提出的Composition API旨在解决这些问题。mixins 的缺点是 Composition API 背后的主要动因之一，Composition API 受到 React Hooks 的启发。</p>
<h2 data-id="heading-5">Vue3.x中的自定义hook函数是什么？</h2>
<ul>
<li>
<p>使用Vue3的组合API封装的可复用的功能函数</p>
</li>
<li>
<p>自定义hook的作用类似于vue2中的mixin技术</p>
</li>
<li>
<p>自定义Hook的优势: 很清楚复用功能代码的来源, 更清楚易懂</p>
</li>
</ul>
<h2 data-id="heading-6">mixins和Composition API hook解决的区别：</h2>
<p>这里以一个简单的计数器为例来讲解Options API mixins和Composition API 自定义hook在写法和使用上的区别。</p>
<p><img alt="1.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4382929ac814c2f815d82d65b32ab3e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            