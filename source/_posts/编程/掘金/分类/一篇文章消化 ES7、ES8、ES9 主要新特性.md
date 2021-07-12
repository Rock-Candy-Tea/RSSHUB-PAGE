
---
title: '一篇文章消化 ES7、ES8、ES9 主要新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2788'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 03:17:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=2788'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">点击查看：后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p>这里收集了某段时间前准备面试用的材料，方便更好的理解， 并整理出了一些 ES7至ES9 的常用新特性，在这做下分享，巩固记忆。</p>
<h3 data-id="heading-0">ES7 新特性</h3>
<h4 data-id="heading-1">includes()-判断数组是否含有特定的值</h4>
<p>如果需要判断数组中是否含有某个特定的值，以往可能更多的是使用<code>indexOf</code>的方式，有则返回查找值的下标，没有则返回-1，这在判断值是否存在，并需要获取值下标的场景比较友好。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
arr.indexOf(<span class="hljs-number">2</span>) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而<code>includes</code>则直接返回 Boolean 值，不返还值的下标，更纯粹的用于判断值的数组包含与否。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
arr.includes(<span class="hljs-number">2</span>) <span class="hljs-comment">// true</span>
arr.includes(<span class="hljs-number">4</span>) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2"><code>**</code>-指数操作符</h4>
<p>如果需要进行指数的计算，在以往需要怎么实现？
例如，输出2的10次方，除了自定义递归方法去实现之外，可以用<code>Math.pow</code>函数实现。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">2</span>, <span class="hljs-number">10</span>) <span class="hljs-comment">// 1024</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 ES7 中，新增了指数的操作运算符<code>**</code>，可以更方便地去进行指数运算。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">2</span>**<span class="hljs-number">10</span> <span class="hljs-comment">// 1024</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">ES8 新特性</h3>
<h4 data-id="heading-4">async/await-异步操作关键字</h4>
<p>为了解决回调地狱的问题，Promise 是个不错的解决方案，但在处理复杂流程的场景，Promise 欠缺了一定的语义化，各个流程通过 .then 连接，读起代码来较为恶心。</p>
<p>设想一个实际场景：用户登录的操作，在用户请求完登录接口并验证通过后，再请求用户信息接口获取用户信息，Promise 实现方式如下：</p>
<pre><code class="hljs language-js copyable" lang="js">userLogin(data)
.then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
<span class="hljs-keyword">return</span> getUserInfo(res.token)
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
<span class="hljs-built_in">console</span>.log(res)
&#125;)
.catch(<span class="hljs-function"><span class="hljs-params">err</span>=></span>&#123;
<span class="hljs-built_in">console</span>.error(err)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果流程更复杂的话，then 连接会更多，直到最后的 catch，这对于代码维护增加了不少阅读成本，不能够很好的表达执行流程。</p>
<p>于是便有了 async/await， 既可以用同步代码的方式去实现，又可以异步处理的关键字，还支持 try catch 捕获异常，两者不能脱离开来单独使用，await 后面一定得是 Promise 对象，否则，它将会自动的包装成一个 Promise 对象。</p>
<p>使用 async/await 的实现如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">let</span> loginRes = <span class="hljs-keyword">await</span> userLogin(data)
    <span class="hljs-keyword">let</span> res = <span class="hljs-keyword">await</span> getUserInfo(loginRes.token)
    <span class="hljs-built_in">console</span>.log(res)
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.error(err)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">values()/entries()-遍历对象新方式</h4>
<p>ES7 新增了两个对象遍历方法，<code>Object.values()</code>和<code>Object.entries()</code>。
<code>Object.values()</code>返回一个数组，包含对象自身的所有可遍历的属性值，示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> user = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">"Sam"</span>, <span class="hljs-attr">age</span>: <span class="hljs-string">"25"</span>&#125;
<span class="hljs-built_in">Object</span>.values(user) <span class="hljs-comment">// ["Sam", "25"]</span>

<span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-number">100</span>: <span class="hljs-string">'a'</span>, <span class="hljs-number">2</span>: <span class="hljs-string">'b'</span>, <span class="hljs-number">7</span>: <span class="hljs-string">'c'</span> &#125;;
<span class="hljs-built_in">Object</span>.values(obj) <span class="hljs-comment">// ["b", "c", "a"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>需要注意的是，如果属性名为数值的属性，是按照数值大小，从小到大遍历的，因此返回的顺序是 b、c、a。</p>
</blockquote>
<p><code>Object.entries()</code> 同样返回一个数组，包含对象自身的所有可比案例的键值和属性的成组，示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> user = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">"Sam"</span>, <span class="hljs-attr">age</span>: <span class="hljs-string">"25"</span>&#125;
<span class="hljs-built_in">Object</span>.entries(user) <span class="hljs-comment">// [["name", "Sam"], ["age", "25"]]</span>

<span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-number">100</span>: <span class="hljs-string">'a'</span>, <span class="hljs-number">2</span>: <span class="hljs-string">'b'</span>, <span class="hljs-number">7</span>: <span class="hljs-string">'c'</span> &#125;;
<span class="hljs-built_in">Object</span>.entries(obj) <span class="hljs-comment">// [["2", "b"], ["7", "c"], ["100", "a"]]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">String padding-字符串填充</h4>
<p>ES8 中对 String 新增了两个实例函数，分别是<code>padStart</code>和<code>padEnd</code>，意味将字符创添加到原始字符串的开头或结尾。
<code>padStart</code>和<code>padEnd</code>都允许接受两个参数：</p>
<ul>
<li>targetLength：当前字符串需要填充到的目标长度。如果这个数值小于当前字符串的长度，则返回当前字符串本身。</li>
<li>padString：(可选)填充字符串。如果字符串太长，使填充后的字符串长度超过了目标长度，则只保留最左侧的部分，其他部分会被截断，此参数的缺省值为 " "。</li>
</ul>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'Sam'</span>
str.padStart(<span class="hljs-number">6</span>,<span class="hljs-string">'its'</span>)<span class="hljs-comment">// 'itsSam'</span>
str.padEnd(<span class="hljs-number">6</span>,<span class="hljs-string">'its'</span>)<span class="hljs-comment">// 'Samits'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">getOwnPropertyDescriptors-返回元素自身属性描述</h4>
<p>如果想获取某个元素的自身属性描述，可以使用<code>Object.getOwnPropertyDescriptors()</code>如果没有任何属性，则会返回空对象。</p>
<p>使用其可以解决<code>Object.assign()</code>无法正确拷贝 get 和 set 的问题。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">"Sam"</span>&#125;
<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptors(obj)

<span class="hljs-comment">// name:</span>
<span class="hljs-comment">// configurable: true</span>
<span class="hljs-comment">// enumerable: true</span>
<span class="hljs-comment">// value: "Sam"</span>
<span class="hljs-comment">// writable: true</span>
<span class="hljs-comment">// __proto__: Object</span>
<span class="hljs-comment">// __proto__: Object</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">ES9 新特性</h3>
<h4 data-id="heading-9">for await of-异步迭代器</h4>
<p>如果在 <code>async/await</code>中使用循环中去调用异步函数，则不会正常执行，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">demo</span>(<span class="hljs-params">arr</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> arr) &#123;
    <span class="hljs-keyword">await</span> handleDo(i);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该示例中，循环本身仍然保持着同步操作，并在内部异步函数之前，全部调用完成结束。</p>
<p>为了解决该问题，ES9 中引入了异步迭代器，允许在循环中去调用异步函数，示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">demo</span>(<span class="hljs-params">arr</span>) </span>&#123;
  <span class="hljs-keyword">for</span> <span class="hljs-keyword">await</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> arr) &#123;
    handleDo(i);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">Promise.finally()-Promise 结束触发</h4>
<p>当我们调用 Promise 时，下一个结果要么是<code>.then()</code>，要么是失败触发<code>.catch()</code>。这样导致有些代码需要在这两处重复写两遍，导致代码冗余，如果希望 Promise 不管是成功还是失败，都执行同样的代码，可以使用<code>.finally()</code>，它允许你在执行结束后触发。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">login</span>(<span class="hljs-params"></span>) </span>&#123;
  userLogin()
  .then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(res);
&#125;)
  .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
  &#125;)
.finally(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'finally'</span>);
&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">Rest/Spread 属性</h4>
<p>Rest参数语法允许我们将一个不定数量的参数表示为一个数组。示例：</p>
<pre><code class="hljs language-js copyable" lang="js">restParam(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">restParam</span>(<span class="hljs-params">p1, p2, ...p3</span>) </span>&#123;
  <span class="hljs-comment">// p1 = 1</span>
  <span class="hljs-comment">// p2 = 2</span>
  <span class="hljs-comment">// p3 = [3, 4, 5]</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES9为对象解构提供了和数组一样的Rest参数和展开操作符，示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Obj = &#123;<span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">3</span>&#125;;
<span class="hljs-keyword">const</span> &#123; a, ...x &#125; = Obj;<span class="hljs-comment">// a = 1,x = &#123; b: 2, c: 3 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">正则表达式新特性</h4>
<h5 data-id="heading-13">s (dotAll) 标志</h5>
<p>s(dotAll)flag 正则表达式中，点（.）是一个特殊字符，代表任意的单个字符，但是有两个例外。一个是四个字节的 UTF-16 字符，这个可以用 u 修饰符解决；另一个是行终止符, 如换行符 (n) 或回车符 (r), 这个可以通过 ES9 的 s(dotAll)flag，在原正则表达式基础上添加 s 表示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-regexp">/foo.bar/</span>.test(<span class="hljs-string">'foo\nbar'</span>)) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-regexp">/foo.bar/</span>s.test(<span class="hljs-string">'foo\nbar'</span>)) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那如何判断当前正则是否使用了 dotAll 模式呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> re = <span class="hljs-regexp">/foo.bar/</span>s <span class="hljs-comment">// Or, `const re = new RegExp('foo.bar', 's');`.</span>
<span class="hljs-built_in">console</span>.log(re.test(<span class="hljs-string">'foo\nbar'</span>)) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(re.dotAll) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(re.flags) <span class="hljs-comment">// 's'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">命名捕获组</h5>
<p>在一些正则表达式模式中，使用数字进行匹配可能会令人混淆。因为美式英语中的日期表示法和英式英语中的日期表示法不同，所以很难区分哪一组表示日期，哪一组表示月份：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> re = <span class="hljs-regexp">/(\d&#123;4&#125;)-(\d&#123;2&#125;)-(\d&#123;2&#125;)/</span>;
<span class="hljs-keyword">const</span> match= re.exec(<span class="hljs-string">'2019-01-01'</span>);
<span class="hljs-built_in">console</span>.log(match[<span class="hljs-number">0</span>]); <span class="hljs-comment">// → 2019-01-01</span>
<span class="hljs-built_in">console</span>.log(match[<span class="hljs-number">1</span>]); <span class="hljs-comment">// → 2019</span>
<span class="hljs-built_in">console</span>.log(match[<span class="hljs-number">2</span>]); <span class="hljs-comment">// → 01</span>
<span class="hljs-built_in">console</span>.log(match[<span class="hljs-number">3</span>]); <span class="hljs-comment">// → 01</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES9 引入了命名捕获组，允许为每一个组匹配指定一个名字，既便于阅读代码，又便于引用。示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> re = <span class="hljs-regexp">/(?<year>\d&#123;4&#125;)-(?<month>\d&#123;2&#125;)-(?<day>\d&#123;2&#125;)/</span>;
<span class="hljs-keyword">const</span> match = re.exec(<span class="hljs-string">'2019-01-01'</span>);
<span class="hljs-built_in">console</span>.log(match.groups); <span class="hljs-comment">// → &#123;year: "2019", month: "01", day: "01"&#125;</span>
<span class="hljs-built_in">console</span>.log(match.groups.year); <span class="hljs-comment">// → 2019</span>
<span class="hljs-built_in">console</span>.log(match.groups.month); <span class="hljs-comment">// → 01</span>
<span class="hljs-built_in">console</span>.log(match.groups.day); <span class="hljs-comment">// → 01</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">写在最后</h3>
<p>写作不易，希望可以获得你的一个「赞」。如果文章对你有用，可以选择「收藏」。
如有文章有错误或建议，欢迎评论指正，谢谢你。❤️</p>
<h4 data-id="heading-16">欢迎阅读其它文章</h4>
<ul>
<li><a href="https://juejin.cn/post/6975770170413776926" target="_blank" title="https://juejin.cn/post/6975770170413776926">实战：用 Vue3 实现一个 Message 消息组件</a></li>
<li><a href="https://juejin.cn/post/6981232153233195039" target="_blank" title="https://juejin.cn/post/6981232153233195039">实战：用 Vue3 实现 Image 组件，顺便支持懒加载</a></li>
<li><a href="https://juejin.cn/post/6968352814858764296" target="_blank" title="https://juejin.cn/post/6968352814858764296">One Piece，Vue.js 3.0 带来了哪些更新</a></li>
<li><a href="https://juejin.cn/post/6983626263327932429/" target="_blank" title="https://juejin.cn/post/6983626263327932429/">上手后才知道 ，Vue3 的 script setup 语法糖是真的爽</a></li>
<li><a href="https://juejin.cn/post/6979053938087723021" target="_blank" title="https://juejin.cn/post/6979053938087723021">技术团队普遍存在的问题和解决方案</a></li>
<li><a href="https://juejin.cn/post/6844903618810757128" target="_blank" title="https://juejin.cn/post/6844903618810757128">ES6中常用的10个新特性讲解</a></li>
</ul></div>  
</div>
            