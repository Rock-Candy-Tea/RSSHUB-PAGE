
---
title: 'vue须知（1）—— v-if和v-for哪个优先级更高？如果两个同时出现，应该怎么优化得到更好的性能？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecda1292eb824605bf670573df306c49~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 24 May 2021 19:54:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecda1292eb824605bf670573df306c49~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>源码中找答案compiler/codegen/index.js
做个测试如下</p>
<pre><code class="hljs language-js copyable" lang="js"><p v-<span class="hljs-keyword">for</span>=<span class="hljs-string">"item in items"</span> v-<span class="hljs-keyword">if</span>=<span class="hljs-string">"condition"</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html> 
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span>></span> 
<span class="hljs-tag"><<span class="hljs-name">head</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Vue事件处理<span class="hljs-tag"></<span class="hljs-name">title</span>></span> 
<span class="hljs-tag"></<span class="hljs-name">head</span>></span> 
<span class="hljs-tag"><<span class="hljs-name">body</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span> 
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>v-for和v-if谁的优先级高？应该如何正确使用避免性能问题？<span class="hljs-tag"></<span class="hljs-name">h1</span>></span> 
        <span class="hljs-comment"><!-- <p v-for="child in children" v-if="isFolder">&#123;&#123;child.title&#125;&#125;</p> --></span> 
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"isFolder"</span>></span> 
            <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"child in children"</span>></span>&#123;&#123;child.title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span> 
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span> 
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript"> 
        <span class="hljs-comment">// 创建实例 </span>
        <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123; 
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#demo'</span>, 
            <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123; 
                <span class="hljs-keyword">return</span> &#123; 
                    <span class="hljs-attr">children</span>: [ 
                        &#123;<span class="hljs-attr">title</span>:<span class="hljs-string">'foo'</span>&#125;, 
                        &#123;<span class="hljs-attr">title</span>:<span class="hljs-string">'bar'</span>&#125;, 
                    ] 
                &#125; 
            &#125;, 
            <span class="hljs-attr">computed</span>: &#123; 
                <span class="hljs-function"><span class="hljs-title">isFolder</span>(<span class="hljs-params"></span>)</span> &#123; 
                    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.children && <span class="hljs-built_in">this</span>.children.length > <span class="hljs-number">0</span>                  
                &#125; 
            &#125;, 
        &#125;); 
        <span class="hljs-built_in">console</span>.log(app.$options.render); 
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span> 
<span class="hljs-tag"></<span class="hljs-name">body</span>></span> 
<span class="hljs-tag"></<span class="hljs-name">html</span>></span></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两者同级时，渲染函数如下：</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">anonymous</span>(<span class="hljs-params"> 
</span>) </span>&#123; 
<span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params"><span class="hljs-built_in">this</span></span>)</span>&#123;<span class="hljs-keyword">return</span> _c(<span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"demo"</span>&#125;&#125;,[_c(<span class="hljs-string">'h1'</span>,[_v(<span class="hljs-string">"v-for和v-if谁的优先 级高？应该如何正确使用避免性能问题？"</span>)]),_v(<span class="hljs-string">" "</span>), 
_l((children),<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">child</span>)</span>&#123;<span class="hljs-keyword">return</span> (isFolder)?_c(<span class="hljs-string">'p'</span>, 
[_v(_s(child.title))]):_e()&#125;)],<span class="hljs-number">2</span>)&#125; 
&#125;) 
<span class="hljs-comment">//包含了isFolder的条件判断 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两者不同级时，渲染函数如下</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">anonymous</span>(<span class="hljs-params"> 
</span>) </span>&#123; 
<span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params"><span class="hljs-built_in">this</span></span>)</span>&#123;<span class="hljs-keyword">return</span> _c(<span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"demo"</span>&#125;&#125;,[_c(<span class="hljs-string">'h1'</span>,[_v(<span class="hljs-string">"v-for和v-if谁的优先 级高？应该如何正确使用避免性能问题？"</span>)]),_v(<span class="hljs-string">" "</span>), 
(isFolder)?_l((children),<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">child</span>)</span>&#123;<span class="hljs-keyword">return</span> _c(<span class="hljs-string">'p'</span>, 
[_v(_s(child.title))])&#125;):_e()],<span class="hljs-number">2</span>)&#125; 
&#125;) 
<span class="hljs-comment">//先判断了条件再看是否执行_l </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecda1292eb824605bf670573df306c49~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结论：</p>
<ol>
<li>显然v-for优先于v-if被解析（把你是怎么知道的告诉面试官）</li>
<li>如果同时出现，每次渲染都会先执行循环再判断条件，无论如何循环都不可避免，浪费了性能</li>
<li>要避免出现这种情况，则在外层嵌套template，在这一层进行v-if判断，然后在内部进行v-for循环</li>
<li>如果条件出现在循环内部，可通过计算属性提前过滤掉那些不需要显示的项</li>
</ol></div>  
</div>
            