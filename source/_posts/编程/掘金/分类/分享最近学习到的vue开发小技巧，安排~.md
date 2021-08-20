
---
title: '分享最近学习到的vue开发小技巧，安排~'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3945'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 23:29:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=3945'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><strong>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></h2>
<h3 data-id="heading-1">一、优雅的更新子组件props</h3>
<p>更新 prop 在业务中是很常见的需求，但在子组件中不允许直接修改 prop，因为这种做法不符合单向数据流的原则，在开发模式下还会报出警告。因此大多数人会通过 $emit 触发自定义事件，在父组件中接收该事件的传值来更新 prop。</p>
<p><strong>child.vue</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> defalut &#123;
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-built_in">String</span>  
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">changeTitle</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'change-title'</span>, <span class="hljs-string">'hello'</span>)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>parent.vue:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><child :title=<span class="hljs-string">"title"</span> @change-title=<span class="hljs-string">"changeTitle"</span>></child>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">title</span>: <span class="hljs-string">'title'</span>
        &#125;  
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">changeTitle</span>(<span class="hljs-params">title</span>)</span>&#123;
            <span class="hljs-built_in">this</span>.title = title
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种做法没有问题，我也常用这种手段来更新 prop。但如果你只是想单纯的更新 prop，没有其他的操作。那么 sync 修饰符能够让这一切都变得特别简单。</p>
<p>parent.vue:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><child :title.sync=<span class="hljs-string">"title"</span>></child>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>child.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> defalut &#123;
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-built_in">String</span>  
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">changeTitle</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'update:title'</span>, <span class="hljs-string">'hello'</span>)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只需要在绑定属性上添加 .sync，在子组件内部就可以触发 update:属性名 来更新 prop。可以看到这种手段确实简洁且优雅，这让父组件的代码中减少一个“没必要的函数”。</p>
<h3 data-id="heading-2">二、 provide/inject的使用</h3>
<p>这对选项需要一起使用，以允许一个祖先组件向其所有子孙后代注入一个依赖，不论组件层次有多深，并在其上下游关系成立的时间里始终生效。</p>
<p>简单来说，一个组件将自己的属性通过 provide 暴露出去，其下面的子孙组件 inject 即可接收到暴露的属性。</p>
<p>App.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">app</span>: <span class="hljs-built_in">this</span>
        &#125;
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>child.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">inject</span>: [<span class="hljs-string">'app'</span>],
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.app) <span class="hljs-comment">// App.vue实例</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 2.5.0+ 版本可以通过设置默认值使其变成可选项:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">inject</span>: &#123;
        <span class="hljs-attr">app</span>: &#123;
            <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> (&#123;&#125;)
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.app) 
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你想为 inject 的属性变更名称，可以使用 from 来表示其来源：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">inject</span>: &#123;
        <span class="hljs-attr">myApp</span>: &#123;
            <span class="hljs-comment">// from的值和provide的属性名保持一致</span>
            <span class="hljs-attr">from</span>: <span class="hljs-string">'app'</span>,
            <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> (&#123;&#125;)
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.myApp) 
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是 provide 和 inject 主要在开发高阶插件/组件库时使用。并不推荐用于普通应用程序代码中。但是某些时候，或许它能帮助到我们。</p>
<p><strong>前端路漫漫其修远兮，吾将上下而求索，一起加油，学习前端吧</strong></p>
<p><em>欢迎留言讨论~</em></p></div>  
</div>
            