
---
title: '对 Vue 数据响应式的理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9898dd72ce2f4bb6b85c4ae1ada5c92a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 07:13:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9898dd72ce2f4bb6b85c4ae1ada5c92a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">什么是数据响应式</h3>
<p>数据响应式是指，<strong>在改变数据的时候，视图也会跟着更新</strong>。</p>
<p>当修改 <code>Vue</code> 实例中的数据式，视图就会重新渲染，出现新的内容。这就是 <code>Vue</code> 的数据响应式。</p>
<p><code>Vue</code> 是利用 <code>Object.defineProperty</code> 的方法里面的 <code>getter</code> 与 <code>setter</code> 方法的<strong>观察者模式</strong>来实现数据响应式的</p>
<h4 data-id="heading-1"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Freactivity.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/reactivity.html" ref="nofollow noopener noreferrer">官方解释</a></h4>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9898dd72ce2f4bb6b85c4ae1ada5c92a~tplv-k3u1fbpfcp-watermark.image" height="350px" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>总结：</li>
</ul>
<ol>
<li>任何一个 <code>Vue Component</code> 都有一个与之对应的 <code>Watcher</code> 实例。</li>
<li><code>Vue</code> 的 <code>data</code> 上的属性会被添加 <code>getter</code> 和 <code>setter</code> 属性。</li>
<li>当 <code>Vue Component</code> <code>render</code> 函数被执行的时候, <code>data</code> 上会被 <strong>触碰</strong>( <code>touch</code> ), 即被 <strong>读</strong> , <code>getter</code> 方法会被调用, 此时 <code>Vue</code> 会去记录此 <code>Vue component</code> 所依赖的所有 <code>data</code>。(这一过程被称为依赖收集)</li>
<li><code>data</code> 被改动时（主要是用户操作）, 即被 <strong>写</strong> , <code>setter</code> 方法会被调用, 此时 <code>Vue</code> 会去通知所有依赖于此 <code>data</code> 的组件去调用他们的 <code>render</code> 函数进行更新。</li>
</ol>
<blockquote>
<p>本文参考摘录了：</p>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F88648401" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/88648401" ref="nofollow noopener noreferrer">最简化 VUE的响应式原理---daisy</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F339293940" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/339293940" ref="nofollow noopener noreferrer">说说你对 Vue 数据响应式的理解---lanycsq</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.njleonzhang.com%2F2018%2F09%2F26%2Fvue-reactive.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.njleonzhang.com/2018/09/26/vue-reactive.html" ref="nofollow noopener noreferrer">Vue 响应式原理白话版</a></li>
</ol>
</blockquote></div>  
</div>
            