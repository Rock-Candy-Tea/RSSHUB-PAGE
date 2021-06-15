
---
title: 'Vue.js 源码（11）—— 优化器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5443'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 07:57:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=5443'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第11天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>前面我们学习了模板编译中的解析器，这次我们将学习优化器。</p>
<h2 data-id="heading-1">优化器</h2>
<blockquote>
<p>解析器的作用是将HTML模板解析成AST，而优化器的作用是在AST中找出静态子树并打上标记。</p>
</blockquote>
<h3 data-id="heading-2">什么是静态子树？</h3>
<p><code>静态子树</code>指的是那些在 <code>AST</code> 中永远都不会发生变化的节点。例如，一个纯文本节点就是静态子树，而带变量的文本节点就不是静态子树，因为它会随着变量的变化而变化。</p>
<h3 data-id="heading-3">好处</h3>
<p>标记静态子树有两点好处：</p>
<ul>
<li>每次重新渲染时，不需要为静态子树创建新节点</li>
<li>在<code>虚拟DOM</code> 中打补丁（patching）的过程可以跳过</li>
</ul>
<h4 data-id="heading-4">为什么重新渲染时，不需要为静态子树创建新节点？</h4>
<p>前面我们有讲过<code>克隆节点</code>。在生成VNode的过程中，如果发现一个节点被标记为静态子树，那么除了首次渲染会生成节点之外，在重新渲染时并不会生成新的子节点树，而是克隆已存在的静态子树。</p>
<h4 data-id="heading-5">为什么在 patch 阶段可以跳过？</h4>
<p>如果两个节点都是静态子树，就不需要进行对比与更新 DOM 的操作，直接跳过。因为静态子树是不可变的，不需要对比就知道它不可能发生变化。此外，直接跳过后续的各种对比可以节省 JavaScript 的运算成本。</p>
<h2 data-id="heading-6">内部实现</h2>
<p>优化器的内部实现主要分为两个步骤：</p>
<ul>
<li>在AST中找出所有<code>静态节点</code>并打上标记</li>
<li>在AST中找出所有<code>静态根节点</code>并打上标记</li>
</ul>
<p>类似下面的节点就是静态节点:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是静态节点<span class="hljs-tag"><<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应到 AST 中，就是节点的<code>static</code> 为 <code>true</code>，如果是静态根节点，<code>staticRoot</code> 也为<code>true</code>。</p>
<h2 data-id="heading-7">找出所有静态节点并标记</h2>
<p>递归 AST，使用 <code>isStatic</code> 函数来判断节点是否是静态节点，然后如果节点的类型等于<code>1</code>，说明节点是<code>元素节点</code>，那么循环该节点的子节点，调用 <code>markStatic</code> 函数用同样的处理逻辑来处理子节点：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">markStatic</span>(<span class="hljs-params">node</span>)</span>&#123;
    node.static = isStatic(node);
    <span class="hljs-keyword">if</span> (node.type === <span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = node.children.length; i<l;i++)&#123;
            <span class="hljs-keyword">const</span> child = node.children[i];
            markStatic(child);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">什么样的节点是静态节点？</h3>
<p>当模板被解析器解析成AST时，会根据不同元素类型设置不同的type值</p>





















<table><thead><tr><th>type</th><th>说明</th></tr></thead><tbody><tr><td>1</td><td>元素节点</td></tr><tr><td>2</td><td>带变量的动态文本节点</td></tr><tr><td>3</td><td>不带变量的纯文本节点</td></tr></tbody></table>
<p>显而易见，没有变量的文本节点肯定是静态节点，然后没有使用<code>v-if</code>、<code>v-else</code>、<code>v-for</code>，或没有使用<code>v-bind</code>也是静态节点。</p>
<p>自定义组件或者内置组件也不会是静态节点。</p>
<p>由于递归是从上向下依次标记的，如果父节点被标记为静态节点之后，子节点却被标记为动态节点，这时就会发生矛盾。因为静态子树中不应该只有它自己是静态节点，静态子树的所有子节点应该都是静态节点。因此，我们需要在子节点被打上标记之后重新校对当前节点的标记是否准确。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">markStatic</span>(<span class="hljs-params">node</span>)</span>&#123;
    node.static = isStatic(node);
    <span class="hljs-keyword">if</span> (node.type === <span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = node.children.length; i<l;i++)&#123;
            <span class="hljs-keyword">const</span> child = node.children[i];
            markStatic(child);
            <span class="hljs-comment">// 新增</span>
            <span class="hljs-keyword">if</span>(!child.static)&#123;
                node.static = <span class="hljs-literal">false</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要判断它是否是静态节点，如果不是，那么它的父节点也不可能是静态节点。</p>
<h2 data-id="heading-9">找出所有静态根节点并标记</h2>
<p>找出静态根节点的过程与找出静态节点的过程类似，都是使用<strong>递归</strong>的方式。如果一个节点被判定为静态根节点，那么将不会继续向它的子级继续寻找。</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph 
    root((root)) --找到--> a((静态))
    root --没找到--> b((b))
    b --找到--> c((静态))
    
    a --> d((静态))
    a --> e((静态))
    
    c --> f((静态))
    c --> g((静态))
</code></pre>
<p><strong>有一种情况，即便它真的是静态根节点，也不会被标记为静态根节点</strong>，因为其优化成本大于收益。这种情况是一个元素节点只有一个文本节点。</p>
<p>例如：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是静态节点<span class="hljs-tag"><<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>p元素只有一个文本子节点，此时即便它是静态根节点，也不会被标记。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">markStaticRoots</span>(<span class="hljs-params">node</span>)</span>&#123;
    <span class="hljs-keyword">if</span> (node.type === <span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">if</span> (node.static && node.children.length && !(node.children.length === <span class="hljs-number">1</span> && node.children[<span class="hljs-number">0</span>].type === <span class="hljs-number">3</span>))&#123;
            node.staticRoot = <span class="hljs-literal">true</span>;
            <span class="hljs-keyword">return</span>;
        &#125; <span class="hljs-keyword">else</span> &#123;
            node.staticRoot = <span class="hljs-literal">false</span>;
        &#125;
        <span class="hljs-keyword">if</span> (node.children) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = node.children.length; i<l;i++)&#123;
                markStaticRoots(node.children[i])
            &#125;
        &#125;
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">总结</h2>
<p>本文，我们学习了优化器的作用和原理，后面我们将学习模板编译的第三部分——<strong>代码生成器</strong>。</p></div>  
</div>
            