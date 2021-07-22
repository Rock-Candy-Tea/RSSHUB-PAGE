
---
title: 'JS 对象遍历知多少？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 16:18:23 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>张宇航，微医前端技术部医保支撑组，一个不文艺的处女座程序员。</p>
</blockquote>
<p><a name="user-content-K7I9z" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-0">写在最前面</h2>
<p>本文主要是对 JS 对象(不含数组、Map、Set 结构)的 <strong>7</strong>个遍历方法进行总结归纳，写该文章的这天恰好是我最喜爱的球星艾弗森的 45 周岁生日，因此本文会以艾弗森的基本资料为模板生成一个 JS 对象并对其进行遍历 。
<a name="user-content-lCJZb" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-1">定义对象</h2>
<p>首先让我们定义如以下代码所示的对象 player：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> player = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Allen  Iverson'</span>,
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'birthday'</span>)]: <span class="hljs-string">'1975/06/07'</span>,
&#125;;
<span class="hljs-built_in">Object</span>.defineProperties(player, &#123;
    <span class="hljs-attr">isHallofFame</span>: &#123;
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-literal">true</span>,
    &#125;,
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'ScoreKingTime'</span>)]: &#123;
        <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">false</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-number">4</span>,
    &#125;,
&#125;);
<span class="hljs-built_in">Object</span>.defineProperties(player.__proto__, &#123;
    <span class="hljs-attr">university</span>: &#123;
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-string">'Georgetown'</span>,
    &#125;,
    <span class="hljs-attr">team</span>: &#123;
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-string">'76ers'</span>,
    &#125;,
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'country'</span>)]: &#123;
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-string">'USA'</span>,
    &#125;,
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'hometown'</span>)]: &#123;
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-string">'Virginia'</span>,
    &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上述代码所示，定义了一个 player 的对象，其共有以下 8 个属性：</p>




































































<table><thead><tr><th></th><th>原型属性</th><th>可枚举</th><th>Symbol 属性</th><th>值</th></tr></thead><tbody><tr><td>name</td><td>否</td><td>是</td><td>否</td><td>Allen  Iverson</td></tr><tr><td>birthday</td><td>否</td><td>是</td><td>是</td><td>1975/06/07</td></tr><tr><td>isHallofFame</td><td>否</td><td>否</td><td>否</td><td>true</td></tr><tr><td>ScoreKingTime</td><td>否</td><td>否</td><td>是</td><td>4</td></tr><tr><td>university</td><td>是</td><td>是</td><td>否</td><td>Georgetown</td></tr><tr><td>team</td><td>是</td><td>否</td><td>否</td><td>76ers</td></tr><tr><td>country</td><td>是</td><td>是</td><td>是</td><td>USA</td></tr><tr><td>hometown</td><td>是</td><td>否</td><td>是</td><td>Virginia</td></tr></tbody></table>
<p>通过控制台的输出观察也更直观：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/011fee62462142c488939f951a96abe6~tplv-k3u1fbpfcp-zoom-1.image" alt="answer.png" loading="lazy" referrerpolicy="no-referrer"><br>其中浅颜色的属性都是不可枚举的属性，__proto__下的属性则为其原型上(即 Object.prototype)的属性，Symbol 类型的值自然为 Symbol 属性
<a name="user-content-QOwJ2" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-2">for...in</h2>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor...in" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in" ref="nofollow noopener noreferrer">MDN</a>：The <strong>for...in statement</strong> iterates over all <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FEnumerability_and_ownership_of_properties" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Enumerability_and_ownership_of_properties" ref="nofollow noopener noreferrer">enumerable properties</a> of an object that are keyed by strings (ignoring ones keyed by <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FSymbol" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol" ref="nofollow noopener noreferrer">Symbol</a>s), including inherited enumerable properties.</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> name <span class="hljs-keyword">in</span> player) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'name:'</span>, name);
&#125;
<span class="hljs-comment">// name: name</span>
<span class="hljs-comment">// name: university</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>for...in 循环是我们较为常用的遍历对象方法了，结合 MDN 里所言以及输出结果不难得出其遍历的属性，<strong>包含自身以及原型上所有可枚举的属性，不包含 Symbol 属性</strong>。因为其可遍历到原型上可枚举的属性，因此我们的代码中通常会多出一句这样的判断（如果我们不需要原型上的属性）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> name <span class="hljs-keyword">in</span> player) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(player, name)) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'name:'</span>, name);
    &#125;
    
&#125;
<span class="hljs-comment">// name: name</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​<br>
<a name="user-content-JY7ja" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-3">Object.keys</h2>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fkeys" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys" ref="nofollow noopener noreferrer">MDN</a>：The <strong>Object.keys()</strong> method returns an array of a given object's own enumerable property <strong>names</strong>, iterated in the same order that a normal loop would.</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(player);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'keys:'</span>, keys);
<span class="hljs-comment">// keys: ["name"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Object.keys 大概是我们最常用的遍历方法了，如在 Vue 源码对 data 进行遍历响应式处理也是用这个方法。通过输出结果也表明：其返回的是<strong>所有自身可枚举的属性（不含 Symbol 属性）</strong>，不包含原型上的任何属性。
<a name="user-content-MNi4n" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-4">Object.getOwnPropertyNames</h2>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2FgetOwnPropertyNames" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames" ref="nofollow noopener noreferrer">MDN</a>：The <strong>Object.getOwnPropertyNames()</strong> method returns an array of all properties (including non-enumerable properties except for those which use Symbol) found directly in a given object.</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ownPropertyNames = <span class="hljs-built_in">Object</span>.getOwnPropertyNames(player);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ownPropertyNames:'</span>, ownPropertyNames);
<span class="hljs-comment">// ownPropertyNames: ["name", "isHallofFame"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Object.getOwnPropertyNames 返回的是<strong>所有自身的属性（包含不可枚举属性但不包含 Symbol 属性）</strong>，不包含原型上的任何属性。
<a name="user-content-PoiS4" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-5">Object.getOwnPropertySymbols</h2>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2FgetOwnPropertySymbols" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertySymbols" ref="nofollow noopener noreferrer">MDN</a>：The <strong>Object.getOwnPropertySymbols()</strong> method returns an array of all symbol properties found directly upon a given object.</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ownPropertySymbols  = <span class="hljs-built_in">Object</span>.getOwnPropertySymbols(player);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ownPropertySymbols:'</span>, ownPropertySymbols);
<span class="hljs-comment">// ownPropertySymbols: [Symbol(birthday), Symbol(ScoreKingTime)]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过输出不难得出 Object.getOwnPropertySymbols 返回的是<strong>自身的所有 Symbol 属性（包含不可枚举的）</strong>，但是不含原型上的任何属性。
<a name="user-content-F71du" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-6">Reflect.ownKeys</h2>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FReflect%2FownKeys" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/ownKeys" ref="nofollow noopener noreferrer">MDN</a>：The static <strong>Reflect.ownKeys()</strong> method returns an array of the target object's own property keys.</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ownKeys = <span class="hljs-built_in">Reflect</span>.ownKeys(player);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ownKeys:'</span>, ownKeys)
<span class="hljs-comment">// ownKeys: ["name", "isHallofFame", Symbol(birthday), Symbol(ScoreKingTime)]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Reflect.ownKeys 返回的是<strong>自身的所有属性（包含不可枚举的以及所有 Symbol 属性）</strong>，不包含原型 上的任何属性。
<a name="user-content-tvJva" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-7">Object.values</h2>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fvalues" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values" ref="nofollow noopener noreferrer">MDN</a>：The <strong>Object.values()</strong> method returns an array of a given object's own enumerable property values, in the same order as that provided by a <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor...in" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in" ref="nofollow noopener noreferrer">for...in</a> loop. (The only difference is that a for...in loop enumerates properties in the prototype chain as well.)</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> values = <span class="hljs-built_in">Object</span>.values(player);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'values:'</span>, values);
<span class="hljs-comment">// values: ["Allen  Iverson"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Object.values 同 Object.keys 一样，其遍历的是<strong>所有自身可枚举的属性（不含 Symbol 属性）</strong>，不包含原型上的任何属性。但与 Object.keys 不同的是：其返回的不再是 key 值而是 value 值集合。
<a name="user-content-Thj5K" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-8">Object.entries</h2>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fentries" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries" ref="nofollow noopener noreferrer">MDN</a>: The <strong>Object.entries()</strong> method returns an array of a given object's own enumerable string-keyed property [key, value] pairs, in the same order as that provided by a <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor...in" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in" ref="nofollow noopener noreferrer">for...in</a> loop. (The only important difference is that a for...in loop enumerates properties in the prototype chain as well).</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> entries =<span class="hljs-built_in">Object</span>.entries(player);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'entries:'</span>, entries);
<span class="hljs-comment">// entries: [["name", "Allen  Iverson"]]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其也同 Object.keys 一样，遍历的是<strong>所有自身可枚举的属性（不含 Symbol 属性）</strong>，不包含原型上的任何属性。不同的是，其返回值是 [key, value]的集合。Object.entries 在我们平时的开发中可能很少用到，但是其可配合<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2FfromEntries" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries" ref="nofollow noopener noreferrer">Object.fromEntries</a>一起使用：有以下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 对象转换</span>
<span class="hljs-keyword">const</span> object1 = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">3</span> &#125;;
<span class="hljs-keyword">const</span> object2 = <span class="hljs-built_in">Object</span>.fromEntries(
  <span class="hljs-built_in">Object</span>.entries(object1)
  .map(<span class="hljs-function">(<span class="hljs-params">[ key, val ]</span>) =></span> [ key, val * <span class="hljs-number">2</span> ])
);
<span class="hljs-built_in">console</span>.log(object2);
<span class="hljs-comment">// &#123; a: 2, b: 4, c: 6 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-g8lxp" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-9">总结</h2>
<p>结合文章中的代码输出结果可得到以下表格：</p>





























































<table><thead><tr><th></th><th>含原型属性</th><th>含不可枚举</th><th>含 Symbol 属性</th><th>返回值</th></tr></thead><tbody><tr><td>for...in</td><td>是</td><td>否</td><td>否</td><td>key</td></tr><tr><td>Object.keys</td><td>否</td><td>否</td><td>否</td><td>[key...]</td></tr><tr><td>Object.getOwnPropertyNames</td><td>否</td><td>是</td><td>否</td><td>[key...]</td></tr><tr><td>Object.getOwnPropertySymbols</td><td>否</td><td>是(只有 symbol)</td><td>是</td><td>[key...]</td></tr><tr><td>Reflect.ownKeys</td><td>否</td><td>是</td><td>是</td><td>[key...]</td></tr><tr><td>Object.values</td><td>否</td><td>否</td><td>否</td><td>[value...]</td></tr><tr><td>Object.entries</td><td>否</td><td>否</td><td>否</td><td>[[key,value]...]</td></tr></tbody></table>
<p>简而言之：</p>
<ul>
<li>只有 for...in 可以遍历到原型上的属性</li>
<li>Object.getOwnPropertyNames 和 Reflect.ownKeys 可获取到不可枚举的属性</li>
<li>Object.getOwnPropertySymbols 和 Reflect.ownKeys 可获取到 Symbol 属性</li>
</ul>
<h3 data-id="heading-10">推荐阅读</h3>
<ul>
<li><a href="https://juejin.cn/post/6965675731661783076" target="_blank" title="https://juejin.cn/post/6965675731661783076"> 站在潮流前沿，快速实现一个简易版 vite</a></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3683cbf95264e26bb5211f4ad8f1ee7~tplv-k3u1fbpfcp-watermark.image" alt="未命名_自定义px_2021-07-20-0.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            