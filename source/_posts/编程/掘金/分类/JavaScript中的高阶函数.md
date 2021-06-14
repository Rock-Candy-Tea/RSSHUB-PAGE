
---
title: 'JavaScript中的高阶函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dfc174a4e164f1f88b611a138e39268~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 20:20:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dfc174a4e164f1f88b611a138e39268~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第三天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">高阶函数  JavaScript</h1>
<p>高阶函数是指以函数作为参数的函数，并且可以将函数作为结果返回的函数。</p>
<h2 data-id="heading-1">1. 高阶函数</h2>
<ul>
<li>接受一个或多个函数作为输入</li>
<li>输出一个函数</li>
</ul>
<p>至少满足以上一个条件的函数</p>
<p>在js的内置对象中同样存在着一些高阶函数，像数组的<code>map</code>，<code>filter</code>，<code>reduce</code>方法等，它们接受一个函数作为参数，并应用这个函数到列表的每一个元素</p>
<h3 data-id="heading-2">1.1 map</h3>
<p><code>map</code>方法接收一个函数作为参数 ，遍历数组，并且返回一个新的数组，新的数组里的每个元素都执行<code>map</code>传入的函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">let</span> arr1 = arr.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item * <span class="hljs-number">2</span>)
<span class="hljs-built_in">console</span>.log(arr1);<span class="hljs-comment">// [2, 4, 6, 8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回的是一个新数组<code>arr1</code>，==不改变原数组==</p>
<p><code>注意</code>：如果传入的参数没有返回值，则数组的每一项都会是<code>undefind</code></p>
<h4 data-id="heading-3"><strong>经典题目</strong></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log([<span class="hljs-string">'1'</span>,<span class="hljs-string">'2'</span>,<span class="hljs-string">'3'</span>].map(<span class="hljs-built_in">parseInt</span>)); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来看看上面这个代码输出什么</p>
<p><strong>答案</strong>：<code>[1, NaN, NaN]</code></p>
<p><strong>解析</strong></p>
<p><code>parseInt()</code> 函数可解析一个字符串，并返回一个整数。</p>
<p>当参数 radix 的值为 0，或没有设置该参数时，<code>parseInt() </code>会根据该字符串来判断数字的基数。</p>
<p>当忽略参数 radix , 默认的基数如下:</p>
<ul>
<li>如果 字符串 以 "0x" 开头，<code>parseInt()</code> 会把 其余部分解析为十六进制的整数。</li>
<li>如果字符串以 0 开头，把其余部分解析为八进制或十六进制的数字。</li>
<li>如果字符串以 1 ~ 9 的数字开头，<code>parseInt()</code>将把它解析为十进制的整数</li>
</ul>
<p><code>注意</code>：基数<strong>可不是</strong>默认十进制噢！</p>
<p>当我们把数组传入<code>parseInt</code>时，由于接收2个参数，会将数组的索引作为基数传个<code>parseInt</code>，所以实质上进行的是以下几步</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'1'</span>, <span class="hljs-number">0</span>)
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'2'</span>, <span class="hljs-number">1</span>)
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'3'</span>, <span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注意</code>：如果字符串的第一个字符不能被转换为数字，那么<code>parseInt()</code>会返回 NaN。</p>
<p><strong>小tips</strong>：</p>
<p><code>parseInt()</code>还有很多值得注意的问题，可以使用搜索引擎再了解以下</p>
<h3 data-id="heading-4">1.2 filter</h3>
<p><strong>用于筛选数组</strong></p>
<p><code>filter</code>方法接收一个函数作为参数，通过这个函数来指定筛选数组的规则，最后返回满足规则的新数组</p>
<p>在传入的函数中有3个参数可选</p>





















<table><thead><tr><th align="left">参数</th><th align="left">描述</th></tr></thead><tbody><tr><td align="left"><em>currentValue</em></td><td align="left">必须。当前元素的值</td></tr><tr><td align="left"><em>index</em></td><td align="left">可选。当前元素的索引值</td></tr><tr><td align="left"><em>arr</em></td><td align="left">可选。当前元素属于的数组对象</td></tr></tbody></table>
<p><code>注意</code>：</p>
<ul>
<li>不会检测空数组</li>
<li>不会改变原始数组</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>]
<span class="hljs-keyword">let</span> arr1 = arr.filter(<span class="hljs-function"><span class="hljs-params">num</span> =></span> &#123;
    <span class="hljs-keyword">return</span> num > <span class="hljs-number">5</span>
&#125;)
<span class="hljs-built_in">console</span>.log(arr1);<span class="hljs-comment">// [6, 7, 8, 9]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.3 reduce</h3>
<p><code>reduce</code>能做的事情很多，但是我们平时都使用for循环之类的方法代替了，但是<code>reduce</code>真的<strong>高逼格</strong></p>
<pre><code class="hljs language-js copyable" lang="js">array.reduce(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">total, currentValue, currentIndex, arr</span>), <span class="hljs-title">initialValue</span>)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>w3school</code>中给出的reduce语法，这里我们常用的只有前面两个</p>

















<table><thead><tr><th align="left">参数</th><th align="left">描述</th></tr></thead><tbody><tr><td align="left"><em>total</em></td><td align="left">必需。<em>初始值</em>, 或者计算结束后的返回值。</td></tr><tr><td align="left"><em>currentValue</em></td><td align="left">必需。当前元素</td></tr></tbody></table>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]
<span class="hljs-keyword">let</span> sum = arr.reduce(<span class="hljs-function">(<span class="hljs-params">value, item</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(value, item);
    <span class="hljs-comment">// 1 2   3 3  6 4  </span>
    <span class="hljs-keyword">return</span> value + item
&#125;)
<span class="hljs-built_in">console</span>.log(sum);<span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从第四行的调试中可以看出<code>reduce</code>函数的执行过程，在没有初始值的情况下，将数组第一个值作为<code>value</code>第二个值作为<code>item</code>再依次往下遍历整个数组，将返回值作为<code>value</code>，数组的下一位作为<code>item</code>，直至遍历完成。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dfc174a4e164f1f88b611a138e39268~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>利用<code>ruduce</code>实现数组去重</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">4</span>];
<span class="hljs-keyword">let</span> unique = arr.reduce(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">prev, item</span>) </span>&#123;
    prev.indexOf(item) === -<span class="hljs-number">1</span> && prev.push(item);
    <span class="hljs-keyword">return</span> prev;
&#125;, []);
<span class="hljs-built_in">console</span>.log(unique); <span class="hljs-comment">// [1, 2, 3, 4, 5]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过将空数组作为<code>prev</code>初始值，再通过<code>indexOf</code>判断数组中是否包含<code>item</code>，如果没有就将<code>item</code>加入数组，最终返回数组</p>
<blockquote>
<p>关于<code>&&</code>运算符，第一条语句为true则执行第二条，否则不执行</p>
</blockquote>
<p><code>ruduce</code>的用法远不止这些，有兴趣的可以再了解以下~</p>
<hr>
<p>还有很多内置对象都是高阶函数，这里就不一一说明了，从上面的三个方法中，已经能很直观的感受到了函数接收函数作为参数，再返回值的过程，<strong>逼格很高也很好用</strong></p>
<h2 data-id="heading-6">2. AOP 面向切面编程</h2>
<p>当我们需要使用一个公共函数，并且需要在这个函数执行前后添加自己的逻辑，通常我们的做法不能是直接修改这个函数，因为它是<strong>公共函数</strong>，这时候我们可以通过AOP的方法利用高阶函数和原型链的特点进行处理</p>
<blockquote>
<p>把一些与业务无关的功能抽离出来，通过"动态植入"的方法，掺入到业务逻辑模块中。这样做的好处是保证业务逻辑模块的纯净和高内聚，其次可以方便的复用功能模块</p>
</blockquote>
<ul>
<li>下面我们要实现在函数执行前输出提示信息</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params">who</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(who + <span class="hljs-string">'：函数执行了'</span>);
&#125;
<span class="hljs-built_in">Function</span>.prototype.before = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
        callback()
        <span class="hljs-built_in">this</span>(...args)
    &#125;
&#125;
<span class="hljs-keyword">let</span> whoSay = say.before(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'你要被调用了'</span>);
&#125;)
whoSay(<span class="hljs-string">'ljc'</span>)
<span class="hljs-comment">// 你要被调用了</span>
<span class="hljs-comment">// ljc：函数执行了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要实现<strong>后置通知</strong>，只需要将6，7行换以下就可以了</p>
<p><strong>实现的原理</strong></p>
<p>在调用公共函数时，传入我们需要执行提前执行的函数，在内部函数执行前先调用该函数</p>
<h2 data-id="heading-7">3. 偏函数</h2>
<p>当一个函数有很多参数时，调用该函数就需要提供多个参数，如果可以减少参数的个数，就能简化该函数的调用,降低调用该函数的难度。</p>
<ul>
<li>实现3个数求和</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a, b, c</span>)</span>&#123;
<span class="hljs-keyword">return</span> a + b + c;
&#125;
sum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>) <span class="hljs-comment">// 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在调用时我们需要传入3个参数，好像有些许麻烦，下面我们用偏函数的做法</p>
<p>创建一个新的<code>partial</code>函数，这个新函数可以<strong>固定住原函数的部分参数</strong>，从而减少调用时的输入的参数，让我们的调用更加简单</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a, b, c</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b + c
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">partial</span>(<span class="hljs-params">sum, c</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
        <span class="hljs-keyword">return</span> sum(a, b, c)
    &#125;
&#125;
<span class="hljs-keyword">let</span> partialSum = partial(sum, <span class="hljs-number">3</span>)<span class="hljs-comment">// -> 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>高阶函数除了可以接收函数作为参数外，还可以将函数作为结果返回，偏函数就是固定了函数的一个或多个参数，返回一个新的函数接收剩下的参数，以此来简化函数的调用。</p>
</blockquote>
<p><code>Function.prototype.bind</code> 函数就是一个偏函数的典型代表，它接受的第二个参数开始，为预先添加到绑定函数的参数列表中的参数</p>
<h2 data-id="heading-8">4. 函数柯里化</h2>
<p>与偏函数不同，柯里化是把接收多个参数的函数转换成多个只接收一个参数的函数。</p>
<p>我们从一个简单的例子来认识<strong>函数柯里化</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>) <span class="hljs-comment">// 3  普通做法 一次传入两个参数</span>

<span class="hljs-comment">// 假设有一个 curring 函数可以做到柯里化</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curring</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
curring(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>) <span class="hljs-comment">// 我们通过这样的方式来接受参数，这样就实现了柯里化</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们来看看利用柯里化来实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curring</span>(<span class="hljs-params">x</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-params">y</span> =></span> x + y
&#125;
curring(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)  <span class="hljs-comment">// => 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">4.1 函数柯里化的作用</h3>
<p>要真正理解柯里化还是得看示例</p>
<h4 data-id="heading-10">4.1.1 参数复用</h4>
<p>我们先看一段短短的代码，这段代码中，实现了输入输出个人信息的功能，通过<code>myInfo</code>函数将参数拼接返回，这实际上很简单，但是当用很多很多的用户信息时，需要一直传递着<code>个人信息</code>这个参数，这样显然是不合理的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myInfo</span>(<span class="hljs-params">inf, name, age</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;inf&#125;</span>：<span class="hljs-subst">$&#123;name&#125;</span><span class="hljs-subst">$&#123;age&#125;</span>`</span>
&#125;
<span class="hljs-keyword">const</span> myInfo1 = myInfo(<span class="hljs-string">'个人信息'</span>, <span class="hljs-string">'ljc'</span>, <span class="hljs-string">'19'</span>)
<span class="hljs-built_in">console</span>.log(myInfo1); <span class="hljs-comment">// 个人信息：ljc19</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面我们通过柯里化技术来解决</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myInfoCurry</span>(<span class="hljs-params">inf</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">name, age</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;inf&#125;</span>：<span class="hljs-subst">$&#123;name&#125;</span><span class="hljs-subst">$&#123;age&#125;</span>`</span>
    &#125;
&#125;
<span class="hljs-keyword">let</span> myInfoName = myInfoCurry(<span class="hljs-string">'个人信息'</span>)
<span class="hljs-keyword">const</span> myInfo1 = myInfoName(<span class="hljs-string">'ljc'</span>, <span class="hljs-string">'19'</span>)
<span class="hljs-keyword">const</span> myInfo2 = myInfoName(<span class="hljs-string">'ljcc'</span>,<span class="hljs-string">'19'</span>)
<span class="hljs-built_in">console</span>.log(myInfo2); <span class="hljs-comment">// 个人信息：ljcc119</span>
<span class="hljs-built_in">console</span>.log(myInfo1); <span class="hljs-comment">// 个人信息：ljc19</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个就是柯里化技术的作用之一了，参数复用，个人感觉还是很好用的</p>
<p>在上面代码的基础上，我们可以继续扩展我们的信息，就像这样，利用一个函数就可以实现多个功能</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myInfoSex = myInfoCurry(<span class="hljs-string">'爱好'</span>)
<span class="hljs-keyword">const</span> myInfo3 = myInfoSex(<span class="hljs-string">'看球赛'</span>,<span class="hljs-string">'听歌'</span>)
<span class="hljs-built_in">console</span>.log(myInfo3); <span class="hljs-comment">// 爱好：看球赛听歌</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">4.1.2 提前返回</h4>
<p>这个特性是用来对浏览器的监听事件兼容性做一些判断并初始化，解决有些浏览器对<code>addEventListener</code>存在的兼容性问题，所以在使用之前做一次判断，之后就可以省略了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> whichEvent = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.addEventListener) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ele, type, listener, useCapture</span>) </span>&#123;
            ele.addEventListener(type, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
                listener.call(ele, e)
            &#125;, useCapture)
        &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.attachEvent) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ele, type, handler</span>) </span>&#123;
            ele.attachEvent(<span class="hljs-string">'on'</span> + type, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
                handler.call(ele, e)
            &#125;)
        &#125;
    &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于使用了立即执行函数，即使触发多次事件依旧只会触发一次if条件判断</p>
<h4 data-id="heading-12">4.1.3 延迟执行</h4>
<p>下面我们通过一道例题来了解</p>
<p>编写一个<code>add</code>函数实现下面的功能</p>
<blockquote>
<p>add(1)(2)(3) = 6</p>
<p>add(1, 2, 3)(4) = 10</p>
<p>add(1)(2)(3)(4)(5) = 15</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">...args</span>) </span>&#123;
    <span class="hljs-keyword">let</span> inner = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        args.push(...arguments);
        inner.toString = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> args.reduce(<span class="hljs-function">(<span class="hljs-params">prev, cur</span>) =></span> &#123;
                <span class="hljs-keyword">return</span> prev + cur
            &#125;)
        &#125;
        <span class="hljs-keyword">return</span> inner
    &#125;
    <span class="hljs-keyword">return</span> inner
&#125;
<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>)); <span class="hljs-comment">// f 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码中涵盖的知识面很多，核心的部分在于<code>inner.toString</code>这里，利用了当返回一个函数时返回的是它的字符串形式，所以我们可以利用这个特性来自定义我们的返回值</p>
<hr>
<p>以上就是关于高阶函数的全部内容了，这部分的知识有点难，可能理解的不够深入，如果有什么好的方法，可以留言讨论一下</p>
<blockquote>
<p>参考文献：JavaScript Web前端开发指南</p>
<p>部分代码实现学习于b站，以及GitHub等平台</p>
</blockquote></div>  
</div>
            