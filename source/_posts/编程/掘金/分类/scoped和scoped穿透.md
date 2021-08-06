
---
title: 'scoped和scoped穿透'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4242'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 20:57:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=4242'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.什么是scoped</h3>
<pre><code class="copyable">在Vue文件中的style标签上有一个特殊的属性，scoped。当一个style标签拥有scoped属性时候，它的css样式只能用于当前的Vue组件，可以使组件的样式不相互污染。如果一个项目的所有style标签都加上了scoped属性，相当于实现了样式的模块化。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2.scoped的实现原理</h3>
<p>Vue中的scoped属性的效果主要是通过PostCss实现的。以下是转译前的代码:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span>></span><span class="css">
    <span class="hljs-selector-class">.example</span>&#123;
        <span class="hljs-attribute">color</span>:red;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"example"</span>></span>scoped测试案例<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转译后:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span>></span><span class="css">
    <span class="hljs-selector-class">.example</span><span class="hljs-selector-attr">[data-v-5558831a]</span> &#123;
    <span class="hljs-attribute">color</span>: red;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"example"</span> <span class="hljs-attr">data-v-5558831a</span>></span>scoped测试案例<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既:PostCSS给一个组件中的所有dom添加了一个独一无二的动态属性，给css选择器额外添加一个对应的属性选择器，来选择组件中的dom,这种做法使得样式只作用于含有该属性的dom元素(组件内部的dom)。</p>
<blockquote>
<p>总结：scoped的渲染规则：</p>
</blockquote>
<pre><code class="copyable">1. 给HTML的dom节点添加一个不重复的data属性(例如: data-v-5558831a)来唯一标识这个dom 元素;
2. 在每句css选择器的末尾(编译后生成的css语句)加一个当前组件的data属性选择器(例如：[data-v-5558831a])来私有化样式;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3.scoped穿透</h3>
<p>scoped看起来很好用，当时在Vue项目中，当我们引入第三方组件库时(如使用vue-awesome-swiper实现移动端轮播)，需要在局部组件中修改第三方组件库的样式，而又不想去除scoped属性造成组件之间的样式覆盖。这时我们可以通过特殊的方式穿透scoped。</p>
<ul>
<li>stylus的样式穿透 使用<code>>>></code></li>
</ul>
<pre><code class="hljs language-stylus copyable" lang="stylus">外层 >>> 第三方组件 
    样式
    
<span class="hljs-selector-class">.wrapper</span> >>> <span class="hljs-selector-class">.swiper-pagination-bullet-active</span>
<span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>sass和less的样式穿透 使用<code>/deep/</code></li>
</ul>
<pre><code class="hljs language-less copyable" lang="less">外层 /<span class="hljs-selector-tag">deep</span>/ 第三方组件 &#123;
        样式
    &#125;
    <span class="hljs-selector-class">.wrapper</span> /<span class="hljs-selector-tag">deep</span>/ <span class="hljs-selector-class">.swiper-pagination-bullet-active</span>&#123;
      <span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span>;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4.在组件中修改第三方组件库样式的其它方法</h3>
<p>上面我们介绍了在使用scoped 属性时，通过scopd穿透的方式修改引入第三方组件库样式的方法，下面我们介绍其它方式来修改引入第三方组件库的样式</p>
<ol>
<li>在vue组件中不使用scoped属性;</li>
<li>在vue组建中使用两个style标签，一个加上scoped属性，一个不加scoped属性，把需要覆盖的css样式写在不加scoped属性的style标签里;</li>
<li>建立一个reset.css(基础全局样式)文件，里面写覆盖的css样式，在入口文件main.js 中引入;</li>
</ol>
<blockquote>
<p>参考链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000015932467" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000015932467" ref="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p>
</blockquote></div>  
</div>
            