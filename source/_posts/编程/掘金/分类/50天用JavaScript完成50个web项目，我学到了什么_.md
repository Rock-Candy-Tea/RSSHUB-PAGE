
---
title: '50天用JavaScript完成50个web项目，我学到了什么_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/284576a9dece49eeb3011432276362d6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 00:48:48 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/284576a9dece49eeb3011432276362d6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1.Expanding Cards</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/284576a9dece49eeb3011432276362d6~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F59" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/59" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F59" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/59" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:弹性盒子布局中的<code>flex</code>属性:让所有弹性盒模型对象的子元素都有相同的长度，且忽略它们内部的内容。</li>
<li>JavaScript:利用<code>[].filter.call()</code>方法可快速实现简单的选项卡切换。如上述示例源码:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> panelItems = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">".container > .panel"</span>);
panelItems.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    item.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function">() =></span> &#123;
        [].filter.call(item.parentElement.children,<span class="hljs-function"><span class="hljs-params">el</span> =></span> el !== item).forEach(<span class="hljs-function"><span class="hljs-params">el</span> =></span> el.classList.remove(<span class="hljs-string">'active'</span>));
        item.classList.add(<span class="hljs-string">'active'</span>)
    &#125;);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">2.Progress Steps</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cfc00bec03b4588a204dd901c006f84~tplv-k3u1fbpfcp-watermark.image" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F60" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/60" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F60" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/60" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>变量的用法以及弹性盒子垂直水平居中外加伪元素的用法。</li>
<li>JavaScript:计算进度条的宽度，类名的操作。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClass</span>(<span class="hljs-params">el</span>)</span>&#123;
    <span class="hljs-keyword">let</span> methods = &#123;
        addClass,
        removeClass
    &#125;;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addClass</span>(<span class="hljs-params">c</span>)</span>&#123;
        el.classList.add(c);
        <span class="hljs-keyword">return</span> methods;
    &#125;;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeClass</span>(<span class="hljs-params">c</span>)</span>&#123;
        el.classList.remove(c);
        <span class="hljs-keyword">return</span> methods;
    &#125;
    <span class="hljs-keyword">return</span> methods
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3.Rotating Navigation Animation</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56cdf0c1582b426784d213c330e4b8c8~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F61" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/61" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F61" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/61" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:CSS弹性盒子布局加<code>rotate</code>动画。</li>
<li>JavaScript:添加和移除类名的操作。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> addClass = <span class="hljs-function">(<span class="hljs-params">el,className</span>) =></span> el.classList.add(className);
<span class="hljs-keyword">const</span> removeClass = <span class="hljs-function">(<span class="hljs-params">el,className</span>) =></span> el.classList.remove(className);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">4.hidden-search-widget</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac9c30dc348f4aa1bd3781199de59eea~tplv-k3u1fbpfcp-watermark.image" alt="4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F62" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/62" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F62" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/62" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:CSS过渡动画 + 宽度的更改 + <code>input</code>的<code>placeholder</code>样式。</li>
<li>JavaScript:添加和移除类名的操作。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.search</span><span class="hljs-selector-class">.active</span> > <span class="hljs-selector-class">.input</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">240px</span>;
&#125;
<span class="hljs-selector-class">.search</span><span class="hljs-selector-class">.active</span> > <span class="hljs-selector-class">.search-btn</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(<span class="hljs-number">238px</span>);
&#125;
<span class="hljs-selector-class">.search</span> > <span class="hljs-selector-class">.search-btn</span>,<span class="hljs-selector-class">.search</span> > <span class="hljs-selector-class">.input</span> &#123;
    <span class="hljs-attribute">border</span>: none;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">45px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">45px</span>;
    <span class="hljs-attribute">outline</span>: none;
    <span class="hljs-attribute">transition</span>: all .<span class="hljs-number">3s</span> <span class="hljs-built_in">cubic-bezier</span>(<span class="hljs-number">0.25</span>, <span class="hljs-number">0.46</span>, <span class="hljs-number">0.45</span>, <span class="hljs-number">0.94</span>);
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">8px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">searchBtn.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function">() =></span> &#123;
    searchContainer.classList.toggle(<span class="hljs-string">'active'</span>);
    searchInput.focus();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">5.Blurry Loading</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3734818e0d9844bdb98b8e975945ed99~tplv-k3u1fbpfcp-watermark.image" alt="5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F63" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/63" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F63" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/63" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS filter</code>属性的用法;。</li>
<li>JavaScript:定时器加动态设置样式。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> load = <span class="hljs-number">0</span>;
<span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">let</span> blurryLoadingHandler = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    load++;
    <span class="hljs-keyword">if</span>(load > <span class="hljs-number">99</span>)&#123;
        <span class="hljs-built_in">clearTimeout</span>(timer)
    &#125;<span class="hljs-keyword">else</span>&#123;
        timer = <span class="hljs-built_in">setTimeout</span>(blurryLoadingHandler,<span class="hljs-number">20</span>);
    &#125;
    text.textContent = <span class="hljs-string">`页面加载<span class="hljs-subst">$&#123; load &#125;</span>%`</span>;
    text.style.opacity = scale(load,<span class="hljs-number">0</span>,<span class="hljs-number">100</span>,<span class="hljs-number">1</span>,<span class="hljs-number">0</span>);
    bg.style.filter = <span class="hljs-string">`blur(<span class="hljs-subst">$&#123;scale(load,<span class="hljs-number">0</span>,<span class="hljs-number">100</span>,<span class="hljs-number">20</span>,<span class="hljs-number">0</span>)&#125;</span>px)`</span>;
&#125;
blurryLoadingHandler();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有一个非常重要的工具函数(后续有好几个示例都用到了这个工具函数)，如下所示:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> scale = <span class="hljs-function">(<span class="hljs-params">n,inMin,inMax,outerMin,outerMax</span>) =></span> (n - inMin) * (outerMax - outerMin) / (inMax - inMin) + outerMin;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个工具函数的作用就是将一个范围数字映射到另一个数字范围。比方说，将<code>1 ~ 100</code>的数字范围映射到<code>0 ~ 1</code>之间。
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F10756313%2Fjavascript-jquery-map-a-range-of-numbers-to-another-range-of-numbers" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/10756313/javascript-jquery-map-a-range-of-numbers-to-another-range-of-numbers" ref="nofollow noopener noreferrer">详情</a>。</p>
<h1 data-id="heading-5">6.Scroll Animation</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dec05e2090714cf984166342c683b86b~tplv-k3u1fbpfcp-watermark.image" alt="6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F64" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/64" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F64" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/64" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>位移动画。</li>
<li>JavaScript:动态创建元素+元素滚动事件监听+视图可见区域的判断 + 防抖函数。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn,time = <span class="hljs-number">100</span></span>)</span>&#123;
    <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">if</span>(timer)<span class="hljs-built_in">clearTimeout</span>(timer);
        timer = <span class="hljs-built_in">setTimeout</span>(fn,time);
    &#125;
&#125;
<span class="hljs-keyword">let</span> triggerBottom = <span class="hljs-built_in">window</span>.innerHeight / <span class="hljs-number">5</span> * <span class="hljs-number">4</span>;
boxElements.forEach(<span class="hljs-function">(<span class="hljs-params">box,index</span>) =></span> &#123;
   <span class="hljs-keyword">const</span> top = box.getBoundingClientRect().top;
   <span class="hljs-keyword">if</span>(top <= triggerBottom)&#123;
       box.classList.add(<span class="hljs-string">'show'</span>);
   &#125;<span class="hljs-keyword">else</span>&#123;
      box.classList.remove(<span class="hljs-string">'show'</span>);
   &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">7. Split Landing Page</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/726230c209504ea39fae7b6092e7d3a3~tplv-k3u1fbpfcp-watermark.image" alt="7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F65" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/65" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F65" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/65" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>过渡特效 + 弹性盒子垂直水平居中 + <code>CSS</code>定位 + 宽度的更改。</li>
<li>JavaScript:鼠标悬浮事件 + 类名的操作。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">HTMLElement.prototype.addClass = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">className</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.classList.add(className);
&#125;;
HTMLElement.prototype.removeClass = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">className</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.classList.remove(className);
&#125;
<span class="hljs-keyword">const</span> on = <span class="hljs-function">(<span class="hljs-params">el,type,handler,useCapture = <span class="hljs-literal">false</span></span>) =></span> &#123;
    <span class="hljs-keyword">if</span>(el && type && handler) &#123;
        el.addEventListener(type,handler,useCapture);
    &#125;
&#125;
on(leftSplit,<span class="hljs-string">'mouseenter'</span>,<span class="hljs-function">() =></span> container.addClass(<span class="hljs-string">'hover-left'</span>));
on(leftSplit,<span class="hljs-string">'mouseleave'</span>,<span class="hljs-function">() =></span> container.removeClass(<span class="hljs-string">'hover-left'</span>));
on(rightSplit,<span class="hljs-string">'mouseenter'</span>,<span class="hljs-function">() =></span> container.addClass(<span class="hljs-string">'hover-right'</span>));
on(rightSplit,<span class="hljs-string">'mouseleave'</span>,<span class="hljs-function">() =></span> container.removeClass(<span class="hljs-string">'hover-right'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从这个示例，我也知道了<code>mouseenter、mouseleave</code>和<code>mouseover、mouseout</code>的区别，总结如下:</p>
<blockquote>
<ol>
<li>enter只触发1次，只有等到鼠标离开了目标元素之后再进入才会继续触发，同理leave也是如此理解。而over与out就是不断的触发。</li>
<li>enter进入子元素，通过e.target也无法区分是移入/移出子元素还是父元素，而over与out则可以区分。</li>
</ol>
</blockquote>
<h1 data-id="heading-7">8.Form Wave</h1>
<p>效果如图所示:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47a8afb5441b462b9678c4a5dd4bd721~tplv-k3u1fbpfcp-watermark.image" alt="8.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F66" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/66" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F66" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/66" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>渐变 + 弹性盒子垂直水平居中 + <code>CSS</code>过渡动画 + <code>CSS</code>位移变换 + 关注焦点伪类选择器与同级元素选择器的用法。</li>
<li>JavaScript:字符串替换成标签 + 动态创建元素。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> createLetter = <span class="hljs-function"><span class="hljs-params">v</span> =></span> v.split(<span class="hljs-string">""</span>).map(<span class="hljs-function">(<span class="hljs-params">letter,idx</span>) =></span> <span class="hljs-string">`<span style="transition-delay:<span class="hljs-subst">$&#123; idx * <span class="hljs-number">50</span> &#125;</span>ms"><span class="hljs-subst">$&#123; letter &#125;</span></span>`</span>).join(<span class="hljs-string">""</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">9.Sound Board</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3a26c5fd6914806a22c6863fadb451f~tplv-k3u1fbpfcp-watermark.image" alt="9.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F67" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/67" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F67" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/67" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>渐变 + 弹性盒子垂直水平居中 + 基本样式。</li>
<li>JavaScript:动态创建元素 + 播放音频(<code>audio</code>标签)。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">sounds.forEach(<span class="hljs-function"><span class="hljs-params">sound</span> =></span> &#123;
    <span class="hljs-keyword">const</span> btn = create(<span class="hljs-string">'button'</span>);
    btn.textContent = sound;
    btn.type = <span class="hljs-string">"button"</span>;
    <span class="hljs-keyword">const</span> audio = create(<span class="hljs-string">'audio'</span>);
    audio.src = <span class="hljs-string">"./audio/"</span> + sound + <span class="hljs-string">'.mp3'</span>;
    audio.id = sound;
    btn.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function">() =></span> &#123;
        stopSounds();
        $(<span class="hljs-string">'#'</span> + sound).play();
    &#125;);
    buttonContainer.appendChild(btn);
    buttonContainer.insertAdjacentElement(<span class="hljs-string">'beforebegin'</span>,audio);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">10. Dad Jokes</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7feaa758b4314fc2b838e12d39b34f18~tplv-k3u1fbpfcp-watermark.image" alt="10.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F68" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/68" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F68" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/68" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>渐变 + 弹性盒子垂直水平居中 + 基本样式。</li>
<li>JavaScript:事件监听 + <code>fetch API</code>请求接口。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> api = <span class="hljs-string">'https://icanhazdadjoke.com'</span>;
<span class="hljs-keyword">const</span> on = <span class="hljs-function">(<span class="hljs-params">el,type,handler,useCapture = <span class="hljs-literal">false</span></span>) =></span> &#123;
    <span class="hljs-keyword">if</span>(el && type && handler)&#123;
        el.addEventListener(type,handler,useCapture);
    &#125;
&#125;
on(getJokeBtn,<span class="hljs-string">'click'</span>,request);
request();
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> fetch(api,headerConfig);
    <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> res.json();
    content.innerHTML = data.joke;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">11. Event Keycodes</h1>
<p>效果如图所示:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7b656a9f96144d3b99e09765dcbb9e1~tplv-k3u1fbpfcp-watermark.image" alt="11.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F69" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/69" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F69" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/69" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>渐变 + 弹性盒子垂直水平居中 + 基本样式。</li>
<li>JavaScript:键盘事件监听 + 事件对象的属性。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#container'</span>);
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"keydown"</span>,<span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
    createKeyCodeTemplate(event);
&#125;);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createKeyCodeTemplate</span>(<span class="hljs-params">e</span>)</span>&#123;
    <span class="hljs-keyword">const</span> &#123; key,keyCode,code &#125; = e;
    <span class="hljs-keyword">let</span> template = <span class="hljs-string">""</span>;
    [
        &#123;
            <span class="hljs-attr">title</span>:<span class="hljs-string">"event.key"</span>,
            <span class="hljs-attr">content</span>:key === <span class="hljs-string">" "</span> ? <span class="hljs-string">"Space"</span> : key
        &#125;,
        &#123;
            <span class="hljs-attr">title</span>:<span class="hljs-string">"event.keyCode"</span>,
            <span class="hljs-attr">content</span>:keyCode
        &#125;,
        &#123;
            <span class="hljs-attr">title</span>:<span class="hljs-string">"event.code"</span>,
            <span class="hljs-attr">content</span>:code
        &#125;
    ].forEach(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        template += <span class="hljs-string">`<div class="key"><small><span class="hljs-subst">$&#123; value.title &#125;</span></small><span class="hljs-subst">$&#123; value.content &#125;</span></div>`</span>;
    &#125;);
    container.innerHTML = template;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">12. Faq Collapse</h1>
<p>效果如图所示:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39bba9c930ff4d72897853d59e2e3bff~tplv-k3u1fbpfcp-watermark.image" alt="12.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F70" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/70" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F70" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/70" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>font-awesome</code>字体库的使用 + 伪元素选择器 + 定位 + <code>CSS</code>渐变 + 基本样式。</li>
<li>JavaScript:动态创建元素 + 类名的切换 + 事件代理。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> faqs = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'.faq-container > .faq'</span>);
container.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
   <span class="hljs-keyword">if</span>(e.target.className.indexOf(<span class="hljs-string">'faq-icon'</span>) > -<span class="hljs-number">1</span>)&#123;
      faqs[[].indexOf.call(faqs,e.target.parentElement)].classList.toggle(<span class="hljs-string">'active'</span>);
   &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">13. Random Choice Picker</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19a6874d18cc43bbbd6b3a8a90c24450~tplv-k3u1fbpfcp-watermark.image" alt="13.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F71" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/71" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F71" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/71" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式。</li>
<li>JavaScript:动态创建元素 + 类名的切换 + 延迟定时器的用法 + 随机数 + 键盘事件的监听。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTags</span>(<span class="hljs-params">value,splitSymbol</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(!value || !value.length)<span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">const</span> words = value.split(splitSymbol).map(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v.trim()).filter(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v);
    tags.innerHTML = <span class="hljs-string">''</span>;
    words.forEach(<span class="hljs-function"><span class="hljs-params">word</span> =></span> &#123;
        <span class="hljs-keyword">const</span> tag = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'span'</span>);
        tag.classList.add(<span class="hljs-string">'tag'</span>);
        tag.innerText = word;
        tags.appendChild(tag);
    &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">randomTag</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> time = <span class="hljs-number">50</span>;
    <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">let</span> randomHighLight = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> randomTagElement = pickerRandomTag();
        highLightTag(randomTagElement);
        timer = <span class="hljs-built_in">setTimeout</span>(randomHighLight,<span class="hljs-number">100</span>);
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            unHighLightTag(randomTagElement);
        &#125;,<span class="hljs-number">100</span>);
    &#125;
    randomHighLight();
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">clearTimeout</span>(timer);
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">const</span> randomTagElement = pickerRandomTag();
            highLightTag(randomTagElement);
        &#125;,<span class="hljs-number">100</span>);
    &#125;,time * <span class="hljs-number">100</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pickerRandomTag</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> tagElements = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'#tags .tag'</span>);
    <span class="hljs-keyword">return</span> tagElements[<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * tagElements.length)];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">14. Animated Navigation</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/847bf226147146a59e83eb1c90fd4d06~tplv-k3u1fbpfcp-watermark.image" alt="14.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F72" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/72" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F72" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/72" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + 定位 + 位移变换以及角度旋转。</li>
<li>JavaScript:类名的切换。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">toggle.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function">() =></span> nav.classList.toggle(<span class="hljs-string">'active'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">15. Incrementing Counter</h1>
<p>效果如图所示:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b5ed7b0da0a4007b0f0e6cfdbed487b~tplv-k3u1fbpfcp-watermark.image" alt="15.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F73" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/73" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F73" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/73" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>渐变 + <code>font-awesome</code>字体库的使用。</li>
<li>JavaScript:动态创建元素 + 定时器实现增量相加。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateCounterHandler</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> counters_elements = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'.counter'</span>);
    counters_elements.forEach(<span class="hljs-function"><span class="hljs-params">element</span> =></span> &#123;
        element.textContent = <span class="hljs-string">'0'</span>;
        <span class="hljs-keyword">const</span> updateCounter = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">const</span> value = +element.getAttribute(<span class="hljs-string">'data-count'</span>);
            <span class="hljs-keyword">const</span> textContent = +element.textContent;
            <span class="hljs-keyword">const</span> increment = value / <span class="hljs-number">100</span>;
            <span class="hljs-keyword">if</span> (textContent < value) &#123;
                element.textContent = <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.ceil(increment + textContent)&#125;</span>`</span>;
                <span class="hljs-built_in">setTimeout</span>(updateCounter, <span class="hljs-number">10</span>);
            &#125; <span class="hljs-keyword">else</span> &#123;
                element.textContent = value;
            &#125;
        &#125;
        updateCounter();
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">16. Drink Water</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c33188cbb90e480a8da1f4069c0d5b2c~tplv-k3u1fbpfcp-watermark.image" alt="16.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F74" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/74" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F74" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/74" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>渐变 + <code>CSS</code>过渡特效。</li>
<li>JavaScript:正则表达式 + 循环 + 样式与内容的设置。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (actives.length === l) &#123;
                setHeightVisible(<span class="hljs-string">'0'</span>, <span class="hljs-string">'hidden'</span>, <span class="hljs-string">'350px'</span>, <span class="hljs-string">'visible'</span>);
                setTextContent(<span class="hljs-string">"100%"</span>, <span class="hljs-string">"0L"</span>);
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (actives.length === <span class="hljs-number">0</span>) &#123;
                setHeightVisible(<span class="hljs-string">'350px'</span>, <span class="hljs-string">'visible'</span>, <span class="hljs-string">'0'</span>, <span class="hljs-string">'hidden'</span>);
                setTextContent(<span class="hljs-string">"12.5%"</span>, <span class="hljs-string">"2L"</span>);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">const</span> h1 = unitHei * (l - actives.length) + <span class="hljs-string">'px'</span>;
                <span class="hljs-keyword">const</span> h2 = unitHei * actives.length + <span class="hljs-string">'px'</span>;
                setHeightVisible(h1, <span class="hljs-string">'visible'</span>, h2, <span class="hljs-string">'visible'</span>);
                <span class="hljs-keyword">const</span> t1 = (unitHei * actives.length / <span class="hljs-number">350</span>) * <span class="hljs-number">100</span> + <span class="hljs-string">"%"</span>;
                <span class="hljs-keyword">const</span> t2 = (cups[i].textContent.replace(<span class="hljs-regexp">/ml/</span>, <span class="hljs-string">""</span>).replace(<span class="hljs-regexp">/\s+/</span>, <span class="hljs-string">""</span>) - <span class="hljs-number">0</span>) * (l - actives.length) / <span class="hljs-number">1000</span> + <span class="hljs-string">'L'</span>;
                setTextContent(t1, t2);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">17. movie-app</h1>
<p>效果如图所示:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee7e72c965f4404983083abcbf87f49a~tplv-k3u1fbpfcp-watermark.image" alt="17.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F75" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/75" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F75" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/75" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>渐变 + <code>CSS</code>过渡特效 + 清除浮动。</li>
<li>JavaScript:接口请求 + 键盘事件的监听。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">search.addEventListener(<span class="hljs-string">'keydown'</span>,<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
        <span class="hljs-keyword">if</span>(e.keyCode === <span class="hljs-number">13</span>)&#123;
            <span class="hljs-keyword">let</span> value = e.target.value.replace(<span class="hljs-regexp">/\s+/</span>,<span class="hljs-string">""</span>);
            <span class="hljs-keyword">if</span>(value)&#123;
                getMovies(SEARCH_API + value);
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    e.target.value = <span class="hljs-string">""</span>;
                &#125;,<span class="hljs-number">1000</span>);
            &#125;<span class="hljs-keyword">else</span>&#123;
                <span class="hljs-built_in">window</span>.location.reload(<span class="hljs-literal">true</span>);
            &#125;
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>PS:这个示例效果由于接口访问受限，需要翻墙访问。</p>
</blockquote>
<h1 data-id="heading-17">18. background-slider</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/400ba732de6240d5a19c47ecb5d1a8e0~tplv-k3u1fbpfcp-watermark.image" alt="18.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F76" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/76" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F76" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/76" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>渐变 + 阴影效果 + 定位 + 伪元素选择器。</li>
<li>JavaScript:背景设置与类名的操作。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> currentActive = <span class="hljs-number">0</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setBackgroundImage</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> url = slideItems[currentActive].style.backgroundImage;
    background.style.backgroundImage = url;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setSlideItem</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> currentSlide = slideItems[currentActive];
    <span class="hljs-keyword">const</span> siblings = [].filter.call(slideItems,<span class="hljs-function"><span class="hljs-params">slide</span> =></span> slide !== currentSlide);
    currentSlide.classList.add(<span class="hljs-string">'active'</span>);
    siblings.forEach(<span class="hljs-function"><span class="hljs-params">slide</span> =></span> slide.classList.remove(<span class="hljs-string">'active'</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-18">19. theme-clock</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7c888ed0cf04567a0dcb5e05020bf00~tplv-k3u1fbpfcp-watermark.image" alt="19.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F77" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/77" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F77" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/77" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>变量 + 阴影效果 + 定位。</li>
<li>JavaScript:中英文的切换以及主题模式的切换，还有日期对象的处理。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setCurrentDate</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
    <span class="hljs-keyword">const</span> month = date.getMonth();
    <span class="hljs-keyword">const</span> day = date.getDay();
    <span class="hljs-keyword">const</span> time = date.getDate();
    <span class="hljs-keyword">const</span> hour = date.getHours();
    <span class="hljs-keyword">const</span> hourForClock = hour % <span class="hljs-number">12</span>;
    <span class="hljs-keyword">const</span> minute = date.getMinutes();
    <span class="hljs-keyword">const</span> second = date.getSeconds();
    <span class="hljs-keyword">const</span> amPm = hour >= <span class="hljs-number">12</span> ? langText[currentLang][<span class="hljs-string">'time-after-text'</span>] : langText[currentLang][<span class="hljs-string">'time-before-text'</span>];
    <span class="hljs-keyword">const</span> w = currentLang === <span class="hljs-string">'zh'</span> ? dayZHs : days;
    <span class="hljs-keyword">const</span> m = currentLang === <span class="hljs-string">'zh'</span> ? monthZHs : months;
    <span class="hljs-keyword">const</span> values = [
        <span class="hljs-string">`translate(-50%,-100%) rotate(<span class="hljs-subst">$&#123; scale(hourForClock,<span class="hljs-number">0</span>,<span class="hljs-number">11</span>,<span class="hljs-number">0</span>,<span class="hljs-number">360</span>) &#125;</span>deg)`</span>,
        <span class="hljs-string">`translate(-50%,-100%) rotate(<span class="hljs-subst">$&#123; scale(minute,<span class="hljs-number">0</span>,<span class="hljs-number">59</span>,<span class="hljs-number">0</span>,<span class="hljs-number">360</span>) &#125;</span>deg)`</span>,
        <span class="hljs-string">`translate(-50%,-100%) rotate(<span class="hljs-subst">$&#123; scale(second,<span class="hljs-number">0</span>,<span class="hljs-number">59</span>,<span class="hljs-number">0</span>,<span class="hljs-number">360</span>) &#125;</span>deg)`</span>
    ];
    [hourEl,minuteEl,secondEl].forEach(<span class="hljs-function">(<span class="hljs-params">item,index</span>) =></span> setTransForm(item,values[index]));
    timeEl.innerHTML = <span class="hljs-string">`<span class="hljs-subst">$&#123; hour &#125;</span>:<span class="hljs-subst">$&#123; minute >= <span class="hljs-number">10</span> ? minute : <span class="hljs-string">'0'</span> + minute &#125;</span>&nbsp;<span class="hljs-subst">$&#123; amPm &#125;</span>`</span>;
    dateEl.innerHTML = <span class="hljs-string">`<span class="hljs-subst">$&#123;w[day]&#125;</span>,<span class="hljs-subst">$&#123; m[month]&#125;</span><span class="circle"><span class="hljs-subst">$&#123; time &#125;</span></span><span class="hljs-subst">$&#123; langText[currentLang][<span class="hljs-string">'date-day-text'</span>] &#125;</span>`</span>;
    timer = <span class="hljs-built_in">setTimeout</span>(setCurrentDate,<span class="hljs-number">1000</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>PS:本示例也用到了与示例5一样的工具函数<code>scale</code>函数</p>
</blockquote>
<h1 data-id="heading-19">20. button-ripple-effect</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbaa67e77a494125a2cb71d6ca006f27~tplv-k3u1fbpfcp-watermark.image" alt="20.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F78" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/78" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F78" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/78" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>渐变 + <code>CSS</code>动画。</li>
<li>JavaScript:坐标的计算 + 偏移 + 定时器。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> x = e.clientX;
<span class="hljs-keyword">const</span> y = e.clientY;
<span class="hljs-keyword">const</span> left = <span class="hljs-built_in">this</span>.offsetLeft;
<span class="hljs-keyword">const</span> top = <span class="hljs-built_in">this</span>.offsetTop;

<span class="hljs-keyword">const</span> circleX = x - left;
<span class="hljs-keyword">const</span> circleY = y - top;
<span class="hljs-keyword">const</span> span = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'span'</span>);
span.classList.add(<span class="hljs-string">'circle'</span>);
span.style.left = circleX + <span class="hljs-string">'px'</span>;
span.style.top = circleY + <span class="hljs-string">'px'</span>;
<span class="hljs-built_in">this</span>.appendChild(span);
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> span.remove(),<span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">21. drawing-app</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91dd780d17b147efaab4c3078b08baa8~tplv-k3u1fbpfcp-watermark.image" alt="21.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F79" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/79" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F79" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/79" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式。</li>
<li>JavaScript:<code>canvas API</code> + <code>mouse</code>事件以及计算<code>x</code>与<code>y</code>坐标 + <code>ewColorPicker</code>的用法。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mouseDownHandler</span>(<span class="hljs-params">e</span>)</span>&#123;
    isPressed = <span class="hljs-literal">true</span>;
    x = e.offsetX;
    y = e.offsetY;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">fn,wait = <span class="hljs-number">100</span></span>)</span>&#123;
    <span class="hljs-keyword">let</span> done = <span class="hljs-literal">false</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(!done)&#123;
            fn.call(<span class="hljs-built_in">this</span>,args);
            done = <span class="hljs-literal">true</span>;
        &#125;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            done = <span class="hljs-literal">false</span>;
        &#125;,wait);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-21">22. drag-n-drop</h1>
<p>效果如图所示:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b133ab102e94d10af0fe764710c0004~tplv-k3u1fbpfcp-watermark.image" alt="22.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F80" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/80" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F80" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/80" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>渐变 + <code>CSS</code>弹性盒子布局。</li>
<li>JavaScript:<code>drag event API</code> + 随机生成图片。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onDragStart</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.classList.add(<span class="hljs-string">'drag-move'</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.className = <span class="hljs-string">"invisible"</span>,<span class="hljs-number">200</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onDragEnd</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.classList.add(<span class="hljs-string">"drag-fill"</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onDragOver</span>(<span class="hljs-params">e</span>)</span>&#123;
    e.preventDefault();
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onDragEnter</span>(<span class="hljs-params">e</span>)</span>&#123;
    e.preventDefault();
    <span class="hljs-built_in">this</span>.classList.add(<span class="hljs-string">'drag-active'</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onDragLeave</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.className = <span class="hljs-string">"drag-item"</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onDrop</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.className = <span class="hljs-string">"drag-item"</span>;
    <span class="hljs-built_in">this</span>.appendChild(dragFill);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-22">23. content-placholder</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbd2386b00154a00a5bcf86215e3eccc~tplv-k3u1fbpfcp-watermark.image" alt="23.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F81" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/81" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F81" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/81" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>渐变 + <code>CSS</code>卡片样式。</li>
<li>JavaScript:骨架屏加载效果。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">animated_bgs.forEach(<span class="hljs-function"><span class="hljs-params">bg</span> =></span> bg.classList.remove(<span class="hljs-string">"animated-bg"</span>));
animated_bgs_texts.forEach(<span class="hljs-function"><span class="hljs-params">text</span> =></span> text.classList.remove(<span class="hljs-string">"animated-bg-text"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-23">24. sticky-navbar</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/942be7751c724247a854634ef7a3664d~tplv-k3u1fbpfcp-watermark.image" alt="24.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F82" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/82" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F82" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/82" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>渐变 + 固定定位导航。</li>
<li>JavaScript:滚动事件。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"scroll"</span>,<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">window</span>.scrollY > nav.offsetHeight + <span class="hljs-number">100</span>) &#123;
        nav.classList.add(<span class="hljs-string">"active"</span>);
    &#125;<span class="hljs-keyword">else</span>&#123;
        nav.classList.remove(<span class="hljs-string">"active"</span>);
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>PS:这里也做了移动端的布局。</p>
</blockquote>
<h1 data-id="heading-24">25. double-slider</h1>
<p>效果如图所示:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6468e9459ba440b9c27dd5546927ceb~tplv-k3u1fbpfcp-watermark.image" alt="25.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F83" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/83" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F83" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/83" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>渐变 + 位移变换。</li>
<li>JavaScript:轮播图的实现思路，主要还是利用<code>transformY</code>移动端使用<code>transformX</code>。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setTransform</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> translate = isHorizontal() ? <span class="hljs-string">"translateX"</span> : <span class="hljs-string">"translateY"</span>;
    leftSlide.style.transform = <span class="hljs-string">`<span class="hljs-subst">$&#123; translate &#125;</span>(<span class="hljs-subst">$&#123;position * currentIndex&#125;</span>px)`</span>;
    rightSlide.style.transform = <span class="hljs-string">`<span class="hljs-subst">$&#123; translate &#125;</span>(<span class="hljs-subst">$&#123;-(position * currentIndex)&#125;</span>px)`</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-25">26. toast-notification</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f92a6fa1fc904f5f8b72d0c8ffdbe53a~tplv-k3u1fbpfcp-watermark.image" alt="26.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F84" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/84" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F84" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/84" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + 消息提示框的基本样式。</li>
<li>JavaScript:封装一个随机创建消息提示框。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createNotification</span>(<span class="hljs-params">&#123;message = <span class="hljs-literal">null</span>,type = <span class="hljs-literal">null</span>,auto = <span class="hljs-literal">false</span>,autoTime = <span class="hljs-number">1000</span>,left = <span class="hljs-number">0</span>,top = <span class="hljs-number">0</span>&#125;</span>)</span>&#123;
    <span class="hljs-keyword">const</span> toastItem = createEle(<span class="hljs-string">"div"</span>);
    <span class="hljs-keyword">let</span> closeItem = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">if</span>(!auto)&#123;
        closeItem = createEle(<span class="hljs-string">"span"</span>);
        closeItem.innerHTML = <span class="hljs-string">"&times;"</span>;
        closeItem.className = <span class="hljs-string">"toast-close-btn"</span>;
    &#125;
    toastItem.className = <span class="hljs-string">`toast toast-<span class="hljs-subst">$&#123;type&#125;</span>`</span>;
    toastItem.textContent = message;
    <span class="hljs-keyword">if</span>(closeItem)toastItem.appendChild(closeItem);
    container.appendChild(toastItem);
    <span class="hljs-keyword">const</span> leftValue = (left - toastItem.clientWidth) <= <span class="hljs-number">0</span> ? <span class="hljs-number">0</span> : left - toastItem.clientWidth - <span class="hljs-number">30</span>;
    <span class="hljs-keyword">const</span> topValue = (top - toastItem.clientHeight) <= <span class="hljs-number">0</span> ? <span class="hljs-number">0</span> : top - toastItem.clientHeight - <span class="hljs-number">30</span>;
    toastItem.style.left = leftValue + <span class="hljs-string">'px'</span>;
    toastItem.style.top = topValue + <span class="hljs-string">'px'</span>;
    <span class="hljs-keyword">if</span>(auto)&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            toastItem.remove();
        &#125;,autoTime);
    &#125;<span class="hljs-keyword">else</span>&#123;
        closeItem.addEventListener(<span class="hljs-string">"click"</span>,<span class="hljs-function">() =></span> &#123;
            toastItem.remove();
        &#125;);
    &#125;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>消息提示框实现思路可以参考<a href="https://juejin.cn/post/6844904152393318413" target="_blank" title="https://juejin.cn/post/6844904152393318413">这篇文章</a>。</p>
<h1 data-id="heading-26">27. github-profiles</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b456a2e61054e8bbdbd839a755359a5~tplv-k3u1fbpfcp-watermark.image" alt="27.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F85" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/85" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F85" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/85" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式。</li>
<li>JavaScript:<code>try-catch</code>处理异常语法 + <code>axios API</code>请求<code>github API</code> + <code>async-await</code>语法。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRepoList</span>(<span class="hljs-params">username</span>)</span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> &#123; data &#125; = <span class="hljs-keyword">await</span> axios(githubAPI + username + <span class="hljs-string">'/repos?sort=created'</span>);
        addRepoList(data);
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-keyword">if</span>(error.response.status == <span class="hljs-number">404</span>)&#123;
            createErrorCard(<span class="hljs-string">"查找仓库出错!"</span>);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-27">28. double-click-heart</h1>
<p>效果如图所示:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e74a6ea77f5241cb86d3e9371e768720~tplv-k3u1fbpfcp-watermark.image" alt="28.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F86" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/86" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F86" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/86" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>画爱心。</li>
<li>JavaScript:事件次数的计算。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clickHandler</span>(<span class="hljs-params">e</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(clickTime === <span class="hljs-number">0</span>)&#123;
        clickTime = <span class="hljs-built_in">Date</span>.now();
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Date</span>.now() - clickTime < <span class="hljs-number">400</span>)&#123;
            createHeart(e);
            clickTime = <span class="hljs-number">0</span>;
        &#125;<span class="hljs-keyword">else</span>&#123;
            clickTime = <span class="hljs-built_in">Date</span>.now();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-28">29. auto-text-effect</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40acc74bf03745c7966ce5209b8e5332~tplv-k3u1fbpfcp-watermark.image" alt="29.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F87" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/87" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F87" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/87" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式。</li>
<li>JavaScript:定时器 + 定时器时间的计算。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> time = <span class="hljs-number">300</span> / speed.value;
writeText();
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">writeText</span>(<span class="hljs-params"></span>)</span>&#123;
    text.innerHTML = string.slice(<span class="hljs-number">0</span>,idx);
    idx++;
    <span class="hljs-keyword">if</span>(idx > string.length)&#123;
        idx = <span class="hljs-number">1</span>;
    &#125;
    <span class="hljs-built_in">setTimeout</span>(writeText,time);
&#125;
speed.addEventListener(<span class="hljs-string">"input"</span>,<span class="hljs-function"><span class="hljs-params">e</span> =></span> time = <span class="hljs-number">300</span> / e.target.value);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-29">30. password generator</h1>
<p>效果如图所示:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c925deefdbe445438957859c56c62307~tplv-k3u1fbpfcp-watermark.image" alt="30.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F88" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/88" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F88" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/88" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式布局。</li>
<li>JavaScript:中英文切换 + 选择框事件监听 + 随机数 + <code>copy API</code>。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRandomLower</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// a ~ z 的code为 97 ~ 122</span>
    <span class="hljs-comment">// 可根据charCodeAt()方法获取</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">26</span>) + <span class="hljs-number">97</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRandomUpper</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// A ~ Z 的code为 65 ~ 90</span>
    <span class="hljs-comment">// 可根据charCodeAt()方法获取</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">26</span>) + <span class="hljs-number">65</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRandomNumber</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 0 ~ 9的code为48 ~ 57</span>
    <span class="hljs-comment">// 可根据charCodeAt()方法获取</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">10</span>) + <span class="hljs-number">48</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-30">31. good-cheap-fast</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/912aa5d48ee4400c8515c4991e4d218f~tplv-k3u1fbpfcp-watermark.image" alt="31.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F89" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/89" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F89" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/89" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>实现开关小组件样式 + 基本布局样式。</li>
<li>JavaScript:<code>input</code>的<code>change</code>事件的监听。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> checkBoxElements = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">".switch-container input[type='checkbox']"</span>);
checkBoxElements.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.addEventListener(<span class="hljs-string">"change"</span>,<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    <span class="hljs-keyword">const</span> index = <span class="hljs-built_in">Array</span>.from(checkBoxElements).indexOf(e.target);
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Array</span>.from(checkBoxElements).every(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v.checked))&#123;
        <span class="hljs-keyword">if</span>(index === <span class="hljs-number">0</span>)&#123;
            checkBoxElements[<span class="hljs-number">2</span>].checked = <span class="hljs-literal">false</span>;
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(index === <span class="hljs-number">1</span>)&#123;
            checkBoxElements[<span class="hljs-number">0</span>].checked = <span class="hljs-literal">false</span>;
        &#125;<span class="hljs-keyword">else</span>&#123;
            checkBoxElements[<span class="hljs-number">1</span>].checked = <span class="hljs-literal">false</span>;
        &#125;
    &#125;
&#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-31">32. notes-app</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ce021abf2404606a04bea3b02618f09~tplv-k3u1fbpfcp-watermark.image" alt="32.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F90" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/90" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F90" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/90" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + 卡片布局。</li>
<li>JavaScript:<code>marked.js</code>的使用 + <code>localStorage API</code>存储数据 + 鼠标光标位置的计算。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> on($(<span class="hljs-string">".edit"</span>, note), <span class="hljs-string">"click"</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
      <span class="hljs-keyword">const</span> isFocus = textarea.getAttribute(<span class="hljs-string">"data-focus"</span>);
      <span class="hljs-keyword">if</span> (isFocus === <span class="hljs-string">"false"</span>) &#123;
            textarea.setAttribute(<span class="hljs-string">"data-focus"</span>,<span class="hljs-string">"true"</span>);
            <span class="hljs-keyword">if</span>(textarea.classList.contains(<span class="hljs-string">"hidden"</span>))&#123;
                textarea.classList.remove(<span class="hljs-string">"hidden"</span>);
            &#125;
            <span class="hljs-keyword">if</span>(!focusStatus)&#123;
                textarea.value = notes[index].text;
            &#125;
            <span class="hljs-keyword">const</span> text = textarea.value.trim();
            <span class="hljs-comment">// console.log(text);</span>
            <span class="hljs-keyword">if</span> (textarea.setSelectionRange) &#123;
                textarea.focus();
                textarea.setSelectionRange(text.length, text.length);
            &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (textarea.createTextRange) &#123;
                <span class="hljs-keyword">const</span> range = textarea.createTextRange();
                range.collapse(<span class="hljs-literal">true</span>);
                range.moveEnd(<span class="hljs-string">'character'</span>, text.length);
                range.moveStart(<span class="hljs-string">'character'</span>, text.length);
                range.select();
            &#125;
     &#125; <span class="hljs-keyword">else</span> &#123;
        textarea.setAttribute(<span class="hljs-string">"data-focus"</span>,<span class="hljs-string">"false"</span>);
        notes[index].text = textarea.value;
        main.innerHTML = marked(notes[index].text);
        setData(<span class="hljs-string">"notes"</span>, notes);
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-32">33. animated-countdown</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4435d638702f4598bf6854bfb9e632fa~tplv-k3u1fbpfcp-watermark.image" alt="33.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F91" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/91" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F91" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/91" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + 位移、旋转、缩放动画。</li>
<li>JavaScript:动画事件 + 动画的创建与重置。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runAnimation</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> numArr = $$(<span class="hljs-string">"span"</span>,numGroup);
    <span class="hljs-keyword">const</span> nextToLast = numArr.length - <span class="hljs-number">1</span>;
    numArr[<span class="hljs-number">0</span>].classList.add(<span class="hljs-string">"in"</span>);
    numArr.forEach(<span class="hljs-function">(<span class="hljs-params">num,index</span>) =></span> &#123;
        num.addEventListener(<span class="hljs-string">"animationend"</span>,<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
            <span class="hljs-keyword">const</span> &#123;animationName&#125; = e;
            <span class="hljs-keyword">if</span>(animationName === <span class="hljs-string">"goIn"</span> && index !== nextToLast)&#123;
                num.classList.remove(<span class="hljs-string">"in"</span>);
                num.classList.add(<span class="hljs-string">"out"</span>);
            &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(animationName === <span class="hljs-string">"goOut"</span> && num.nextElementSibling)&#123;
                num.nextElementSibling.classList.add(<span class="hljs-string">"in"</span>);
            &#125;<span class="hljs-keyword">else</span>&#123;
                counter.classList.add(<span class="hljs-string">"hide"</span>);
                final.classList.add(<span class="hljs-string">"show"</span>);
            &#125;
        &#125;)
    &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resetAnimation</span>(<span class="hljs-params"></span>)</span>&#123;
    counter.classList.remove(<span class="hljs-string">"hide"</span>);
    final.classList.remove(<span class="hljs-string">"show"</span>);
    <span class="hljs-keyword">const</span> numArr = $$(<span class="hljs-string">"span"</span>,numGroup);
    <span class="hljs-keyword">if</span>(numArr)&#123;
        numArr.forEach(<span class="hljs-function"><span class="hljs-params">num</span> =></span> num.classList.value = <span class="hljs-string">''</span>);
        numArr[<span class="hljs-number">0</span>].classList.add(<span class="hljs-string">"in"</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-33">34. image-carousel</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da25bfc28ce044a8b363b8689e79c4c4~tplv-k3u1fbpfcp-watermark.image" alt="34.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F92" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/92" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F92" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/92" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式布局。</li>
<li>JavaScript:定时器实现轮播。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeCarouselItem</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">if</span>(currentIndex > carouselItems.length - <span class="hljs-number">1</span>)&#123;
        currentIndex = <span class="hljs-number">0</span>;
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(currentIndex < <span class="hljs-number">0</span>)&#123;
        currentIndex = carouselItems.length - <span class="hljs-number">1</span>;
    &#125;
        carousel.style.transform = <span class="hljs-string">`translateX(-<span class="hljs-subst">$&#123; currentIndex * carouselContainer.offsetWidth     &#125;</span>px)`</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>PS:这里额外踩了一个定时器的坑，也就是说，比如我们使用setTimeout模拟实现setInterval方法在这里是会出现问题的，我在js代码里添加了注释说明。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// let interval = mySetInterval(run,1000);</span>
<span class="hljs-comment">// Why use this method can't achieve the desired effect?</span>
<span class="hljs-comment">// Use this method as follow to replace window.setInterval,clicked the prev button more to get the stranger effect.</span>
<span class="hljs-comment">// Maybe this method does not conform to the specification,So make sure to use window.setInterval.</span>
<span class="hljs-comment">// function mySetInterval(handler,time = 1000)&#123;</span>
<span class="hljs-comment">//     let timer = null;</span>
<span class="hljs-comment">//     const interval = () => &#123;</span>
<span class="hljs-comment">//         handler();</span>
<span class="hljs-comment">//         timer = setTimeout(interval,time);</span>
<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">//     interval();</span>
<span class="hljs-comment">//     return &#123;</span>
<span class="hljs-comment">//         clearMyInterval()&#123;</span>
<span class="hljs-comment">//             clearTimeout(timer);</span>
<span class="hljs-comment">//         &#125;</span>
<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">// &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是因为我们用<code>setTimeout</code>实现的定时器并不符合规范，<code>setInterval</code>默认会有<code>10ms</code>的延迟执行。
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhtml.spec.whatwg.org%2Fmultipage%2Ftimers-and-user-prompts.html%23timers" target="_blank" rel="nofollow noopener noreferrer" title="https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timers" ref="nofollow noopener noreferrer">参考规范</a>。</p>
<h1 data-id="heading-34">35. hover board</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/606ebf17e4e14acf864a8c4d709bec0a~tplv-k3u1fbpfcp-watermark.image" alt="35.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F93" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/93" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F93" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/93" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式 + <code>CSS</code>渐变。</li>
<li>JavaScript:动态创建元素 + 悬浮事件。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setColor</span>(<span class="hljs-params">element</span>)</span>&#123;
    element.style.background = <span class="hljs-string">`linear-gradient(135deg, <span class="hljs-subst">$&#123; randomColor() &#125;</span> 10%, <span class="hljs-subst">$&#123; randomColor() &#125;</span> 100%)`</span>;
    element.style.boxShadow = <span class="hljs-string">`0 0 2px <span class="hljs-subst">$&#123; randomColor() &#125;</span>,0 0 10px <span class="hljs-subst">$&#123; randomColor() &#125;</span>`</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeColor</span>(<span class="hljs-params">element</span>)</span>&#123;
    element.style.background = <span class="hljs-string">`linear-gradient(135deg, #1d064e 10%, #10031a 100%)`</span>;
    element.style.boxShadow = <span class="hljs-string">`0 0 2px #736a85`</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-35">36. pokedex</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/722e945303454955af71d619e79874c8~tplv-k3u1fbpfcp-watermark.image" alt="36.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F94" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/94" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F94" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/94" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式布局 + <code>CSS</code>渐变。</li>
<li>JavaScript:<code>fetch API</code>接口请求 + 创建卡片。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPokemon</span>(<span class="hljs-params">pokemon</span>)</span>&#123;
    <span class="hljs-keyword">const</span> pokemonItem = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
    pokemonItem.classList.add(<span class="hljs-string">"pokedex"</span>);

    <span class="hljs-keyword">const</span> name = pokemon.name[<span class="hljs-number">0</span>].toUpperCase() + pokemon.name.slice(<span class="hljs-number">1</span>).toLowerCase();
    <span class="hljs-keyword">const</span> id = pokemon.id.toString().padStart(<span class="hljs-number">3</span>,<span class="hljs-string">"0"</span>);
    <span class="hljs-keyword">const</span> poke_types = pokemon.types.map(<span class="hljs-function"><span class="hljs-params">type</span> =></span> type.type.name);
    <span class="hljs-keyword">const</span> type = main_types.find(<span class="hljs-function"><span class="hljs-params">type</span> =></span> poke_types.indexOf(type) > -<span class="hljs-number">1</span>);
    <span class="hljs-keyword">const</span> color = colors[type];
    pokemonItem.style.background = <span class="hljs-string">`linear-gradient(135deg, <span class="hljs-subst">$&#123; color &#125;</span> 10%, <span class="hljs-subst">$&#123; randomColor() &#125;</span> 100%)`</span>;
    pokemonItem.innerHTML = <span class="hljs-string">`
    <div class="pokedex-avatar">
        <img src="https://pokeres.bastionbot.org/images/pokemon/<span class="hljs-subst">$&#123;pokemon.id&#125;</span>.png" alt="the pokemon">
    </div>
    <div class="info">
        <span class="number">#<span class="hljs-subst">$&#123; id &#125;</span></span>
        <h3 class="name"><span class="hljs-subst">$&#123; name &#125;</span></h3>
        <small class="type">Type:<span><span class="hljs-subst">$&#123; type &#125;</span></span></small>
    </div>`</span>;
    container.appendChild(pokemonItem);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>特别说明:接口似乎不太稳定，也许是我网络原因，图片没有加载出来。</p>
</blockquote>
<h1 data-id="heading-36">37. mobile-tab-navigation</h1>
<p>效果如图所示:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d841abeb5ff4db5b72a44cec20bf34d~tplv-k3u1fbpfcp-watermark.image" alt="37.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F95" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/95" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F95" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/95" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式布局 + <code>CSS</code>渐变实现手机布局。</li>
<li>JavaScript:感觉就是移动端实现一个轮播图切换，利用<code>opacity</code>的设置，没什么好说的。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hideAllElement</span>(<span class="hljs-params">nodeList</span>)</span>&#123;
    nodeList.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.classList.remove(<span class="hljs-string">"active"</span>));
&#125;
navItems.forEach(<span class="hljs-function">(<span class="hljs-params">item,index</span>) =></span> &#123;
    item.addEventListener(<span class="hljs-string">"click"</span>,<span class="hljs-function">() =></span> &#123;
        hideAllElement(navItems);
        hideAllElement(carouselItems);
        item.classList.add(<span class="hljs-string">"active"</span>);
        carouselItems[index].classList.add(<span class="hljs-string">"active"</span>);
    &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-37">38. password-strength-background</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4835cc104d074d13bcd8be4c4044fdc8~tplv-k3u1fbpfcp-watermark.image" alt="38.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F96" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/96" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F96" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/96" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:其实主要是使用<code>tailwind.css</code>这个原子化<code>CSS</code>框架。</li>
<li>JavaScript:监听输入框事件，然后改变背景模糊度。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">password.addEventListener(<span class="hljs-string">"input"</span>,<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; value &#125; = e.target;
    <span class="hljs-keyword">const</span> blur = <span class="hljs-number">20</span> - value.length * <span class="hljs-number">2</span>;
    background.style.filter = <span class="hljs-string">`blur(<span class="hljs-subst">$&#123; blur &#125;</span>px)`</span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-38">39. 3D-background-boxes</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efede501a23b49f09032447000b0ecc0~tplv-k3u1fbpfcp-watermark.image" alt="39.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F97" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/97" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F97" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/97" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>vw、vh</code>布局 + <code>skew</code>倾斜变换。</li>
<li>JavaScript:循环 + 背景图定位的设置。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createBox</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;i < <span class="hljs-number">4</span>;i++)&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>;j < <span class="hljs-number">4</span>;j++)&#123;
            <span class="hljs-keyword">const</span> box = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
            box.classList.add(<span class="hljs-string">"box"</span>);
            box.style.backgroundPosition = <span class="hljs-string">`<span class="hljs-subst">$&#123; -j * <span class="hljs-number">15</span> &#125;</span>vw <span class="hljs-subst">$&#123; -i * <span class="hljs-number">15</span> &#125;</span>vh`</span>;
            boxContainer.appendChild(box);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-39">40. Verify Your Account</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8df8e542e14d4451a38d55f49467d8e3~tplv-k3u1fbpfcp-watermark.image" alt="40.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F98" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/98" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F98" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/98" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式布局 + <code>input</code>的一些特别样式设置。</li>
<li>JavaScript:<code>JavaScript focus</code>事件。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.code-container</span> <span class="hljs-selector-class">.code</span><span class="hljs-selector-pseudo">:focus</span> &#123;
    <span class="hljs-attribute">border-color</span>: <span class="hljs-number">#2397ef</span>;
&#125;
<span class="hljs-selector-class">.code</span>::-webkit-outer-spin-button,
.code::-webkit-inner-spin-button &#123;
  -webkit-appearance: none;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;
<span class="hljs-selector-class">.code</span><span class="hljs-selector-pseudo">:valid</span> &#123;
    <span class="hljs-attribute">border-color</span>: <span class="hljs-number">#034775</span>;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">10px</span> <span class="hljs-number">10px</span> -<span class="hljs-number">5px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.25</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onFocusHandler</span>(<span class="hljs-params">nodeList</span>)</span>&#123;
    onFocus(nodeList[<span class="hljs-number">0</span>]);
    nodeList.forEach(<span class="hljs-function">(<span class="hljs-params">node,index</span>) =></span> &#123;
        node.addEventListener(<span class="hljs-string">"keydown"</span>,<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
            <span class="hljs-comment">// console.log(e.key);</span>
            <span class="hljs-keyword">if</span>(e.key >= <span class="hljs-number">0</span> && e.key <= <span class="hljs-number">9</span>)&#123;
                nodeList[index].value = <span class="hljs-string">""</span>;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> onFocus(nodeList[index + <span class="hljs-number">1</span>]),<span class="hljs-number">0</span>);
            &#125;<span class="hljs-keyword">else</span>&#123;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> onFocus(nodeList[index - <span class="hljs-number">1</span>]),<span class="hljs-number">0</span>);
            &#125;
        &#125;)
    &#125;);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onFocus</span>(<span class="hljs-params">node</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(!node)<span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">const</span> &#123; nodeName &#125; = node;
    <span class="hljs-keyword">return</span> nodeName && nodeName.toLowerCase() === <span class="hljs-string">"input"</span> && node.focus();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-40">41. live-user-filter</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dc2fc0531d54476b308181751ecbfcf~tplv-k3u1fbpfcp-watermark.image" alt="41.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F99" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/99" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F99" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/99" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式布局 + 滚动条样式。</li>
<li>JavaScript:<code>fetch API</code>接口请求 + <code>input</code>事件过滤数据。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">requestData</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">'https://randomuser.me/api?results=50'</span>);
    <span class="hljs-keyword">const</span> &#123; results &#125; = <span class="hljs-keyword">await</span> res.json();
    result.innerHTML = <span class="hljs-string">""</span>;

    results.forEach(<span class="hljs-function"><span class="hljs-params">user</span> =></span> &#123;
        <span class="hljs-keyword">const</span> listItem = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"li"</span>);
        filterData.push(listItem);
        <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">picture</span>:&#123; large &#125;,<span class="hljs-attr">name</span>:&#123; first,last &#125;,<span class="hljs-attr">location</span>:&#123; city,country &#125; &#125; = user;
        listItem.innerHTML = <span class="hljs-string">`
            <img src="<span class="hljs-subst">$&#123; large &#125;</span>" alt="<span class="hljs-subst">$&#123; first + <span class="hljs-string">' '</span> + last &#125;</span>" />
            <div class="user-info">
                <h4><span class="hljs-subst">$&#123; first &#125;</span>  <span class="hljs-subst">$&#123; last &#125;</span></h4>
                <p><span class="hljs-subst">$&#123; city &#125;</span>,<span class="hljs-subst">$&#123; country &#125;</span></p>
            </div>
        `</span>;
        result.appendChild(listItem);
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-41">42. feedback-ui-design</h1>
<p>效果如图所示:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3a1fda1b29f45e59eac426020a9919b~tplv-k3u1fbpfcp-watermark.image" alt="42.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F100" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/100" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F100" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/100" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>画爱心 + 基本样式布局。</li>
<li>JavaScript:选项卡切换功能的实现。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">ratingItem.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    item.addEventListener(<span class="hljs-string">"click"</span>,<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
        siblings(item).forEach(<span class="hljs-function"><span class="hljs-params">sib</span> =></span> sib.classList.remove(<span class="hljs-string">"active"</span>));
        item.classList.add(<span class="hljs-string">"active"</span>);
        selectRating = item.innerText;
    &#125;)
&#125;);
send.addEventListener(<span class="hljs-string">"click"</span>,<span class="hljs-function">() =></span> &#123;
    selectRatingItem.innerText = selectRating;
    sendPage.classList.add(<span class="hljs-string">"hide"</span>);
    receivePage.classList.remove(<span class="hljs-string">"hide"</span>);
&#125;);
back.addEventListener(<span class="hljs-string">"click"</span>,<span class="hljs-function">() =></span> &#123;
    selectRating = $(<span class="hljs-string">".rating.active"</span>).innerText;
    selectRatingItem.innerText = $(<span class="hljs-string">".rating.active"</span>).innerText;
    sendPage.classList.remove(<span class="hljs-string">"hide"</span>);
    receivePage.classList.add(<span class="hljs-string">"hide"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-42">43. custom-range-slider</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/419928799a434ecbafb2ceb50df32f1b~tplv-k3u1fbpfcp-watermark.image" alt="43.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F101" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/101" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F101" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/101" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>input</code>元素的样式设置(兼容写法) + 基本样式布局。</li>
<li>JavaScript:<code>input range</code>元素的<code>input</code>事件监听。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">input</span><span class="hljs-selector-attr">[type=<span class="hljs-string">"range"</span>]</span>::-webkit-slider-runnable-track &#123;
    background-image: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">135deg</span>, <span class="hljs-number">#E2B0FF</span> <span class="hljs-number">10%</span>, <span class="hljs-number">#9F44D3</span> <span class="hljs-number">100%</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">cursor</span>: pointer;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
&#125;
<span class="hljs-selector-tag">input</span><span class="hljs-selector-attr">[type=<span class="hljs-string">"range"</span>]</span>::-webkit-slider-thumb &#123;
    -webkit-appearance: none;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">25px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">25px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">135deg</span>, <span class="hljs-number">#d9e2e6</span> <span class="hljs-number">10%</span>, <span class="hljs-number">#e4e1e4</span> <span class="hljs-number">100%</span>);
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#b233e4</span>;
    <span class="hljs-attribute">cursor</span>: pointer;
    <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">6px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">range.addEventListener(<span class="hljs-string">"input"</span>,<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    <span class="hljs-comment">// string to the number</span>
    <span class="hljs-keyword">const</span> value = +e.target.value;
    <span class="hljs-keyword">const</span> label = e.target.nextElementSibling;

    <span class="hljs-keyword">const</span> range_width = getStyle(e.target,<span class="hljs-string">"width"</span>);<span class="hljs-comment">//XXpx</span>
    <span class="hljs-keyword">const</span> label_width = getStyle(label,<span class="hljs-string">"width"</span>);<span class="hljs-comment">//XXpx</span>

    <span class="hljs-comment">// Due to contain px,slice the width</span>
    <span class="hljs-keyword">const</span> num_width = +range_width.slice(<span class="hljs-number">0</span>,range_width.length - <span class="hljs-number">2</span>);
    <span class="hljs-keyword">const</span> num_label_width = +label_width.slice(<span class="hljs-number">0</span>,label_width.length - <span class="hljs-number">2</span>);

    <span class="hljs-keyword">const</span> min = +e.target.min;
    <span class="hljs-keyword">const</span> max = +e.target.max;

    <span class="hljs-keyword">const</span> left = value * (num_width / max) - num_label_width / <span class="hljs-number">2</span> + scale(value,min,max,<span class="hljs-number">10</span>,-<span class="hljs-number">10</span>);

    label.style.left = <span class="hljs-string">`<span class="hljs-subst">$&#123;left&#125;</span>px`</span>;
    label.innerHTML = value;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-43">44. netflix-mobile-navigation</h1>
<p>效果如图所示:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a31755e123f44a3caba0c30f4e6b2526~tplv-k3u1fbpfcp-watermark.image" alt="44.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F102" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/102" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F102" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/102" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:导航宽度的变化 + <code>CSS</code>渐变 + 基本样式布局。</li>
<li>JavaScript:点击按钮切换导航栏的显隐。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeNav</span>(<span class="hljs-params">type</span>)</span>&#123;
    navList.forEach(<span class="hljs-function"><span class="hljs-params">nav</span> =></span> nav.classList[type === <span class="hljs-string">"open"</span> ? <span class="hljs-string">"add"</span> : <span class="hljs-string">"remove"</span>](<span class="hljs-string">"visible"</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-44">45. quiz-app</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a249e26e6b1466999ad7b1674ea8f83~tplv-k3u1fbpfcp-watermark.image" alt="45.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F103" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/103" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F103" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/103" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:卡片布局 + 基本样式。</li>
<li>JavaScript:表单提交 + 选择题的计算。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">submit.addEventListener(<span class="hljs-string">"click"</span>,<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> answer = getSelected();
    <span class="hljs-keyword">if</span>(answer)&#123;
        <span class="hljs-keyword">if</span>(answer === quizData[currentQuestion].correct)&#123;
            score++;
        &#125;
        currentQuestion++;
        <span class="hljs-keyword">if</span>(currentQuestion > quizData.length - <span class="hljs-number">1</span>)&#123;
            quizContainer.innerHTML = <span class="hljs-string">`
                <h2>You answered <span class="hljs-subst">$&#123; score &#125;</span> / <span class="hljs-subst">$&#123; quizData.length &#125;</span> questions correctly!</h2>
                <button type="button" class="btn" onclick="location.reload()">reload</button>
            `</span>
        &#125;<span class="hljs-keyword">else</span>&#123;
            loadQuiz();
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-45">46. testimonial-box-switcher</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b238fc4381a54fe2b1a1fcf995eb8daf~tplv-k3u1fbpfcp-watermark.image" alt="46.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F105" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/105" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F105" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/105" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>动画 + 宽度的改变实现进度条 + <code>font-awesome</code>字体库的使用 + 基本样式布局。</li>
<li>JavaScript:定时器的用法,注意定时器的执行时间与设置进度条的执行动画时间一样。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.progress-bar</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">4px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">animation</span>: grow <span class="hljs-number">10s</span> linear infinite;
    <span class="hljs-attribute">transform-origin</span>: left;
&#125;
<span class="hljs-keyword">@keyframes</span> grow &#123;
    <span class="hljs-number">0%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scaleX</span>(<span class="hljs-number">0</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateTestimonial</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> &#123; text,name,position,photo &#125; = testimonials[currentIndex];
    <span class="hljs-keyword">const</span> renderElements = [testimonial,username,role];
    userImage.setAttribute(<span class="hljs-string">"src"</span>,photo);
    order.innerHTML = currentIndex + <span class="hljs-number">1</span>;
    [text,name,position].forEach(<span class="hljs-function">(<span class="hljs-params">item,index</span>) =></span> renderElements[index].innerHTML = item);
    currentIndex++;
    <span class="hljs-keyword">if</span>(currentIndex > testimonials.length - <span class="hljs-number">1</span>)&#123;
        currentIndex = <span class="hljs-number">0</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>特别说明:CSS也是可以实现进度条的。</p>
</blockquote>
<h1 data-id="heading-46">47. random-image-feed</h1>
<p>效果如图所示:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40543ddf186e4d60875295a02fb3ea54~tplv-k3u1fbpfcp-watermark.image" alt="47.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F106" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/106" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F106" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/106" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:图片布局 + 基本样式布局 + <code>CSS</code>提示框的实现(定位 + 伪元素) + <code>CSS</code>实现回到顶部效果。</li>
<li>JavaScript:随机数 + (滚动事件的监听)控制回到顶部按钮的显隐。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onLoad</span>(<span class="hljs-params">rows = <span class="hljs-number">5</span></span>) </span>&#123;
    container.innerHTML = <span class="hljs-string">""</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < rows * <span class="hljs-number">3</span>; i++) &#123;
        <span class="hljs-keyword">const</span> imageItem = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"img"</span>);
        imageItem.src = <span class="hljs-string">`<span class="hljs-subst">$&#123;refreshURL&#125;</span><span class="hljs-subst">$&#123;getRandomSize()&#125;</span>`</span>;
        imageItem.alt = <span class="hljs-string">"random image-"</span> + i;
        imageItem.loading = <span class="hljs-string">"lazy"</span>;
        container.appendChild(imageItem);
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRandomSize</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;getRandomValue()&#125;</span>x<span class="hljs-subst">$&#123;getRandomValue()&#125;</span>`</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRandomValue</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">10</span>) + <span class="hljs-number">300</span>;
&#125;
<span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;
    changeBtn.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">() =></span> onLoad());
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"scroll"</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> &#123; scrollTop, scrollHeight &#125; = <span class="hljs-built_in">document</span>.documentElement || <span class="hljs-built_in">document</span>.body;
        <span class="hljs-keyword">const</span> &#123; clientHeight &#125; = flexCenter;
        back.style.display = scrollTop + clientHeight > scrollHeight ? <span class="hljs-string">'block'</span> : <span class="hljs-string">'none'</span>;
    &#125;)
    onLoad();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-47">48. todo-list</h1>
<p>效果如图所示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/466975360dda47c8bf29b1b18028a9d2~tplv-k3u1fbpfcp-watermark.image" alt="48.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F107" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/107" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F107" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/107" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式布局 + <code>CSS</code>渐变。</li>
<li>JavaScript:<code>keydown</code>与<code>contextmenu</code>事件的监听 + <code>localStorage API</code>存储数据。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addTodo</span>(<span class="hljs-params">todo</span>)</span>&#123;
    <span class="hljs-keyword">let</span> inputValue = input.value;
    <span class="hljs-keyword">if</span>(todo)&#123;
        inputValue = todo.text;
    &#125;
    <span class="hljs-keyword">if</span>(inputValue)&#123;
        <span class="hljs-keyword">const</span> liItem = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"li"</span>);
        liItem.innerText = inputValue;
        <span class="hljs-keyword">if</span>(todo && todo.complete)&#123;
            liItem.classList.add(<span class="hljs-string">"complete"</span>);
        &#125;
        liItem.addEventListener(<span class="hljs-string">"click"</span>,<span class="hljs-function">() =></span> &#123;
            liItem.classList.toggle(<span class="hljs-string">"complete"</span>);
            updateList();
        &#125;);
        liItem.addEventListener(<span class="hljs-string">"contextmenu"</span>,<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
            e.preventDefault();
            liItem.remove();
            updateList();
        &#125;);
        todoList.appendChild(liItem);
        input.value = <span class="hljs-string">""</span>;
        updateList();
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateList</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> listItem = $$(<span class="hljs-string">"li"</span>,todoList);
    <span class="hljs-keyword">const</span> saveTodoData = [];
    listItem.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
        saveTodoData.push(&#123;
            <span class="hljs-attr">text</span>:item.innerText,
            <span class="hljs-attr">complete</span>:item.classList.contains(<span class="hljs-string">"complete"</span>)
        &#125;)
    &#125;);
    <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">"todoData"</span>,<span class="hljs-built_in">JSON</span>.stringify(saveTodoData));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-48">49. insect-catch-game</h1>
<p>效果如图所示:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b47d53e48be4ec6992f0c62624ba9ee~tplv-k3u1fbpfcp-watermark.image" alt="49.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2Fjs%2F108" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/js/108" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2Fjs%2F108" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/js/108" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:基本样式布局。</li>
<li>JavaScript:中英文切换 + 替换元素中的文本(不包含标签元素) + 定时器的用法。如上述示例部分源码如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">replaceText</span>(<span class="hljs-params">el,text,wrapSymbol = <span class="hljs-string">""</span></span>)</span>&#123;
    <span class="hljs-keyword">let</span> newText = [];
    <span class="hljs-keyword">if</span>(wrapSymbol)&#123;
        <span class="hljs-comment">// why not use split method?,because it can filter the wrap symbol.</span>
        <span class="hljs-keyword">const</span> getIndex = <span class="hljs-function">(<span class="hljs-params">txt</span>) =></span> txt.search(<span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"\\"</span> + wrapSymbol));
        <span class="hljs-keyword">let</span> searchIndex = getIndex(text),i = <span class="hljs-number">0</span>,len = text.length;
        <span class="hljs-keyword">while</span>(searchIndex !== -<span class="hljs-number">1</span>)&#123;
            newText.push(text.slice(i,searchIndex) + wrapSymbol);
            i = searchIndex;
            <span class="hljs-keyword">if</span>(getIndex(text.slice(searchIndex + <span class="hljs-number">1</span>)) === -<span class="hljs-number">1</span>)&#123;
                newText.push(text.slice(searchIndex + <span class="hljs-number">1</span>,len));
            &#125;
            searchIndex = getIndex(text.slice(searchIndex + <span class="hljs-number">1</span>));
        &#125;
    &#125;
    <span class="hljs-keyword">const</span> walk = <span class="hljs-function">(<span class="hljs-params">el,handler</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> children = <span class="hljs-built_in">Array</span>.from(el.childNodes);
        <span class="hljs-keyword">let</span> wrapIndex = children.findIndex(<span class="hljs-function"><span class="hljs-params">node</span> =></span> node.nodeName.toLowerCase() === <span class="hljs-string">"br"</span>);
        children.forEach(<span class="hljs-function">(<span class="hljs-params">node,index</span>) =></span> &#123;
            <span class="hljs-keyword">if</span>(node.nodeType === <span class="hljs-number">3</span> && node.textContent.replace(<span class="hljs-regexp">/\s+/</span>,<span class="hljs-string">""</span>))&#123;
                wrapSymbol ? handler(node,newText[index - wrapIndex < <span class="hljs-number">0</span> ? <span class="hljs-number">0</span> : index - wrapIndex]) : handler(node,text);;
            &#125;
        &#125;);
    &#125;
    walk(el,<span class="hljs-function">(<span class="hljs-params">node,txt</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> parent = node.parentNode;
        parent.insertBefore(<span class="hljs-built_in">document</span>.createTextNode(txt),node);
        parent.removeChild(node);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上工具函数的实现参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F12919074%2Fjs-replace-only-text-without-html-tags-and-codes" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/12919074/js-replace-only-text-without-html-tags-and-codes" ref="nofollow noopener noreferrer">这里来实现的</a>。</p>
<blockquote>
<p>特别说明:这个示例算是一个比较综合的示例了。</p>
</blockquote>
<h1 data-id="heading-49">50. kinetic-loader</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d1c88073253407882f145a5226c6c45~tplv-k3u1fbpfcp-watermark.image" alt="50.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2FCSS%2F6%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/CSS/6/" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2FCSS%2F6%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/CSS/6/" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:CSS旋转动画 + 基本样式布局。</li>
</ol>
<p>如上述示例部分源码如下:</p>
<pre><code class="hljs language-js copyable" lang="js">@keyframes rotateA &#123;
    <span class="hljs-number">0</span>%,<span class="hljs-number">25</span>% &#123;
        <span class="hljs-attr">transform</span>: rotate(0deg);
    &#125;
    <span class="hljs-number">50</span>%,<span class="hljs-number">75</span>% &#123;
        <span class="hljs-attr">transform</span>: rotate(180deg);
    &#125;
    <span class="hljs-number">100</span>% &#123;
        <span class="hljs-attr">transform</span>: rotate(360deg);
    &#125;
&#125;
@keyframes rotateB &#123;
    <span class="hljs-number">0</span>%,<span class="hljs-number">25</span>% &#123;
        <span class="hljs-attr">transform</span>: rotate(90deg);
    &#125;
    <span class="hljs-number">50</span>%,<span class="hljs-number">75</span>% &#123;
        <span class="hljs-attr">transform</span>: rotate(270deg);
    &#125;
    <span class="hljs-number">100</span>% &#123;
        <span class="hljs-attr">transform</span>: rotate(450deg);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一天，额外的实现了一个<code>404</code>效果，算是特别结尾吧，是不是很花哨(<code>^_^</code>)。这算是一个<code>CSS</code>动画的综合使用，如下所示:</p>
<h1 data-id="heading-50">51. 404 page</h1>
<p>效果如图所示:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79d56f5547444a73942ef0d35b91524b~tplv-k3u1fbpfcp-watermark.image" alt="51.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feveningwater%2Fmy-web-projects%2Ftree%2Fmaster%2FCSS%2F7%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eveningwater/my-web-projects/tree/master/CSS/7/" ref="nofollow noopener noreferrer">源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.eveningwater.com%2Fmy-web-projects%2FCSS%2F7%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.eveningwater.com/my-web-projects/CSS/7/" ref="nofollow noopener noreferrer">在线示例</a></li>
</ul>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 知识点总结:</li>
</ul>
<ol>
<li>CSS:<code>CSS</code>动画的用法 + 基本样式布局 + <code>svg</code>图标元素的样式设置。</li>
</ol>
<p>如上述示例部分源码如下:</p>
<pre><code class="hljs language-js copyable" lang="js">@keyframes background &#123;
    <span class="hljs-keyword">from</span> &#123;
        <span class="hljs-attr">background</span>: linear-gradient(135deg,#e0e0e0 <span class="hljs-number">10</span>%,#ffffff <span class="hljs-number">90</span>%);
    &#125;
    to &#123;
        <span class="hljs-attr">background</span>: linear-gradient(135deg,#ffffff <span class="hljs-number">10</span>%,#e0e0e0 <span class="hljs-number">90</span>%);
    &#125;
&#125;
@keyframes stampSlide &#123;
    <span class="hljs-number">0</span>% &#123;
        <span class="hljs-attr">transform</span>: rotateX(90deg) rotateZ(-90deg) translateZ(-200px) translateY(130px);
    &#125;
    <span class="hljs-number">100</span>% &#123;
        <span class="hljs-attr">transform</span>: rotateX(90deg) rotateZ(-90deg) translateZ(-200px) translateY(-4000px);
    &#125;
&#125;
@keyframes slide &#123;
    <span class="hljs-number">0</span>% &#123;
        <span class="hljs-attr">transform</span>: translateX(<span class="hljs-number">0</span>);
    &#125;
    <span class="hljs-number">100</span>% &#123;
        <span class="hljs-attr">transform</span>: translateX(-200px);
    &#125;
&#125;
@keyframes roll &#123;
    <span class="hljs-number">0</span>% &#123;
        <span class="hljs-attr">transform</span>: rotateZ(0deg);
    &#125;
    <span class="hljs-number">85</span>% &#123;
        <span class="hljs-attr">transform</span>: rotateZ(90deg);
    &#125;
    <span class="hljs-number">87</span>% &#123;
        <span class="hljs-attr">transform</span>: rotateZ(88deg);
    &#125;
    <span class="hljs-number">90</span>% &#123;
        <span class="hljs-attr">transform</span>: rotateZ(90deg);
    &#125;
    <span class="hljs-number">100</span>% &#123;
        <span class="hljs-attr">transform</span>: rotateZ(90deg);
    &#125;
&#125;
@keyframes zeroFour &#123;
    <span class="hljs-number">0</span>% &#123;
        <span class="hljs-attr">content</span>:<span class="hljs-string">"4"</span>;
    &#125;
    <span class="hljs-number">100</span>% &#123;
        <span class="hljs-attr">content</span>:<span class="hljs-string">"0"</span>;
    &#125;
&#125;
@keyframes draw &#123;
    <span class="hljs-number">0</span>% &#123;
        stroke-dasharray: <span class="hljs-number">30</span> <span class="hljs-number">150</span>;
        stroke-dashoffset: <span class="hljs-number">42</span>;
    &#125;
    <span class="hljs-number">100</span>% &#123;
        <span class="hljs-attr">stroke</span>:rgba(<span class="hljs-number">8</span>, <span class="hljs-number">69</span>, <span class="hljs-number">131</span>, <span class="hljs-number">0.9</span>);
        stroke-dasharray: <span class="hljs-number">224</span>;
        stroke-dashoffset: <span class="hljs-number">0</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            