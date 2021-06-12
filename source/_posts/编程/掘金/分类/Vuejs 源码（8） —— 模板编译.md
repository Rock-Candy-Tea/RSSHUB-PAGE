
---
title: 'Vue.js 源码（8） —— 模板编译'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1270'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 07:47:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=1270'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第8天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>大多数同学在使用 Vue.js 开发时，基本都还是使用的模板。</p>
<p>但是 Vue.js 中创建 html 并不是只有模板这一种途径，我们可以使用 render（渲染函数）来创建 html，或者使用 jsx 来创建 html。</p>
<p>我们经常使用的模板会被编译转换成渲染函数，渲染函数执行后，会得到一个虚拟节点树用于渲染。</p>
<p>下面，我们将一起学习模板转换成渲染函数的整体过程。</p>
<h2 data-id="heading-1">模板编译</h2>
<blockquote>
<p>将模板编译成渲染函数可以分为两个步骤，先将模板解析成 AST(Abstract Syntax Tree，抽象语法树)，然后再使用 AST 生成渲染函数。</p>
</blockquote>
<p>由于静态节点时不需要重新渲染的，所以在生成 AST后，还需要遍历一遍，给所有静态节点做一个标记。</p>
<p>模板编译分成三部分内容：</p>
<ul>
<li>将模板解析为 AST</li>
<li>遍历 AST 标记静态节点</li>
<li>使用 AST 生成渲染函数</li>
</ul>
<p>这三部分，分别对应三个模块</p>
<ul>
<li>解析器</li>
<li>优化器</li>
<li>代码生成器</li>
</ul>
<pre><code class="hljs language-mermaid" lang="mermaid">graph LR
    t[模板]
    subgraph 模板编译
        a[解析器] --> b[优化器] --> c[代码生成器]
    end
    r[渲染函数]
    t --> a
    c --> r
</code></pre>
<h3 data-id="heading-2">解析器</h3>
<p>在解析器内部，又分了很多小解析器，包括<code>过滤器解析器</code>、<code>文本解析器</code>和 <code>html 解析器</code>。</p>
<p>在使用模板时，我们可以在其中使用过滤器，而过滤器解析器的作用就是用来解析过滤器的。</p>
<p>文本解析器就是用来解析文本的，它的主要作用是用来解析带变量的文本，例如下面：</p>
<pre><code class="hljs language-text copyable" lang="text">Hello &#123;&#123;name&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不带变量的文本是一段纯文本，不需要使用文本解析器来解析。</p>
<p>最后也是最重要的是HTML解析器，它是解析器中最核心的模块，它的作用就是解析模板，每当解析到HTML标签的开始位置、结束位置、文本或者注释时，都会触发钩子函数，然后将相关信息通过参数传递出来，然后生成不同的 AST 节点。</p>
<p>AST 和 vnode 有点类似，都是使用 JavaScript 中的对象来表示节点。</p>
<h2 data-id="heading-3">优化器</h2>
<p>优化器的目标是遍历 AST，检测出所有<strong>静态子树</strong>（永远都不会发生变化的 DOM 节点）并给其
<strong>打标记</strong>。</p>
<p>当 AST 中的静态子树被打上标记后，每次重新渲染时，就不需要为打上标记的静态节点创建新的虚拟节点，而是直接克隆已存在的虚拟节点。在虚拟 DOM 的更新操作中，如果发现两个节点是同一个节点，正常情况下会对这两个节点进行更新，但是<strong>如果这两个节点是静态节点，则可以直接跳过更新节点的流程</strong>。</p>
<h2 data-id="heading-4">代码生成器</h2>
<p>代码生成器是模板编译的最后一步，它的作用是将AST转换成渲染函数中的内容，这个内容可以称为 <strong>“代码字符串”</strong>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"a"</span>></span>hello world<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成的代码字符串是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params"><span class="hljs-built_in">this</span></span>)</span> &#123;
        <span class="hljs-keyword">return</span> _c( <span class="hljs-comment">// $createElement</span>
            <span class="hljs-string">'p'</span>,
            &#123;
                <span class="hljs-attr">attrs</span>: &#123;
                    <span class="hljs-attr">align</span>: <span class="hljs-string">"center"</span>
                &#125;,
                <span class="hljs-attr">on</span>: &#123;
                    <span class="hljs-attr">click</span>: a
                &#125;
            &#125;,
            [_v(<span class="hljs-string">"hello world"</span>)]
        )
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一个代码字符串最终导出到外界使用时，会使用 <code>new Function(...)</code> 来创建函数，这个函数就叫作渲染函数。</p>
<h2 data-id="heading-5">总结</h2>
<p>本文，我们简单了解了模板编译的流程。</p>
<p>模板编译需要经过三个过程：</p>
<ul>
<li>将模板解析成 AST</li>
<li>遍历 AST 标记静态节点</li>
<li>使用 AST 生成代码字符串</li>
</ul>
<p>后面，我们会详细学习<strong>解析器</strong>是如果工作的，也就是第一个过程，<strong>如果把字符串模板解析成 AST</strong>。</p></div>  
</div>
            