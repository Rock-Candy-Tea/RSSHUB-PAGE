
---
title: 'Vue 全解：.sync 修饰符'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5424'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 18:17:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=5424'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li><code>Vue</code> 规定：在子组件中，不可以直接修改 <code>props</code> 外部数据。
<ul>
<li>但是我们常有在子组件中修改 <code>props</code> 的值并同步到父组件的需求，要实现这个需求，可以使用 JS 的发布、订阅功能(EventBus)。</li>
<li>看一个简单的例子： 在子组件 <code>child</code> 中，修改父组件 <code>father</code> 中的 <code>n </code>的值</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-comment">// child.vue</span>
   <tamplate>
       <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
           &#123;&#123;compData&#125;&#125;
           <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
           <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$emit('update:compData', compdata + 1)"</span>></span>n + 1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
       <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
   </tamplate>
   
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
       <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
           <span class="hljs-attr">props</span>: [<span class="hljs-string">"compData"</span>]
       &#125;
   </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// father.vue</span>
    <tamplate>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            父组件的 n：&#123;&#123;n&#125;&#125;
            <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
            <span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">:compData.sync</span>=<span class="hljs-string">"n"</span>/></span>
            <span class="hljs-comment"><!-- 扩展为：
            <Child :compData="n" @update:compData="n = $event"/>
            --></span> 
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    </tamplate>
    <script>
        <span class="hljs-keyword">import</span> Child <span class="hljs-keyword">from</span> <span class="hljs-string">'./child.vue'</span>
        <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
            <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">n</span>: <span class="hljs-number">100</span>
                &#125;
            &#125;,
            <span class="hljs-attr">components</span>: &#123;Child&#125;
        &#125;
    <script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>Vue</code> 封装了 <code>EventBus</code>
<ul>
<li>使用 <code>$emit</code> 定义并触发事件，并传参；事件名应为：<code>update:被监听的数据名</code></li>
<li>使用 <code>$event</code> 来获取其他组件中 <code>$emit</code> 的参数</li>
</ul>
</li>
<li>以上，修饰符 <code>.sync</code> 就是通过 <code>$event</code> 获取其他组件中 <code>$emit</code> 参数这一操作的简写，是一个语法糖</li>
</ul></div>  
</div>
            