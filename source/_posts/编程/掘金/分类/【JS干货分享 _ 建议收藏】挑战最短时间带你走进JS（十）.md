
---
title: '【JS干货分享 _ 建议收藏】挑战最短时间带你走进JS（十）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/414046e7a96e401d915f2ac8599a4a96~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 17:37:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/414046e7a96e401d915f2ac8599a4a96~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 25 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p><strong>感激相遇 你好 我是阿ken</strong></p>
<blockquote>
<p>作者：请叫我阿ken<br>
链接：<a href="https://juejin.cn/user/1091187754155048/posts" title="https://juejin.cn/user/1091187754155048/posts" target="_blank">juejin.cn/user/109118…</a><br>
来源：掘金<br>
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。</p>
</blockquote>
<h1 data-id="heading-0"><strong>🌊🌈关于前言：</strong></h1>
<p><strong>文章部分内容及图片出自网络，如有问题请与我本人联系(主页介绍中有公众号)</strong></p>
<p><strong>本博客暂适用于刚刚接触<code>JS</code>以及好久不看想要复习的小伙伴。</strong></p>
<h1 data-id="heading-1"><strong>🌊🌈关于内容：</strong></h1>
<h2 data-id="heading-2"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.5_数组对象</h2>
<p><strong>JavaScript 中的数组对象可以使用 new Array 或字面量“[ ]” 来创建。</strong></p>
<h2 data-id="heading-3"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.5.1_数组类型检测</h2>
<p>在开发中，有时候需要检测变量的类型是否为数组。<del>例如， 在两数中。要求华人的参数必须是一一个数组，不能传入其他类型的值，否则会出错，所以这时候可以在函数中检测参数的类型是否为数组。</del> 数组类型检测有两种常用的方式，分别是使用 instanceof 运算符和使用Array.isArray() 方法。</p>
<p>示例代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [];
<span class="hljs-keyword">var</span> obj = &#123; &#125;;
<span class="hljs-comment">// 第1种方式</span>
<span class="hljs-built_in">console</span>.log ( arr <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span> );
<span class="hljs-comment">// 输出结果:true</span>
<span class="hljs-built_in">console</span>.log ( obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span> );
<span class="hljs-comment">// 输出结果:false</span>
<span class="hljs-comment">//第2种方式</span>
<span class="hljs-built_in">console</span>.log ( <span class="hljs-built_in">Array</span>.isArray(arr) );
<span class="hljs-comment">// 输出结果:true</span>
<span class="hljs-built_in">console</span>.log ( <span class="hljs-built_in">Array</span>.isArray(obj) );
<span class="hljs-comment">// 输出结果:false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，如果检测结果为true，表示给定的变量是一个数组， 如果检测结果为false，则表示给定的变量不是数组。</p>
<h2 data-id="heading-4"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.5.2_添加或删除数组元素</h2>
<p>JavaScript 数组对象提供了添加或删除元素的方法，<strong>可以实现在在数组的末尾或开头添加新的数组元素，或在数组的末尾或开头移出数组元素。</strong></p>
<p>添加或删除数组元素：</p>






























<table><thead><tr><th>方法名</th><th>功能描述</th><th>返回值</th></tr></thead><tbody><tr><td>push( 参数1… )</td><td>数组末尾添加一个或多个元素， 会修改原数组</td><td>返回数组的新长度</td></tr><tr><td>unshift( 参数1… )</td><td>数组开头添加一个或多个元素， 会修改原数组</td><td>返回数组的新长度</td></tr><tr><td>pop()</td><td>删除数组的最后一个元素，若是空数组则返回 undefined，会修改原数组</td><td>返回删除的元素的值</td></tr><tr><td>shift()</td><td>删除数组的第一个元素，若是空数组则返回undefined，会修改原数组</td><td>返回第一个元素的值</td></tr></tbody></table>
<p>需要注意的是，push() 和 unshift() 方法的返回值是新数组的长度，而 pop()和 shift()方法返回的是移出的数组元素。</p>
<p>案例： 演示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'Rose'</span>, <span class="hljs-string">'Lily'</span>];
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'原数组:'</span>+ arr);
<span class="hljs-keyword">var</span> last = arr.pop();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'在末尾移出元素:'</span>+ last + <span class="hljs-string">'- 移出后数组:'</span> + arr);
<span class="hljs-keyword">var</span> len = arr.push(<span class="hljs-string">'Tulip'</span>, <span class="hljs-string">'Jasmine'</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'在末尾添加元素后长度变为:'</span>+ len + <span class="hljs-string">'- 添加后数组:'</span>+ arr);
<span class="hljs-keyword">var</span> first = arr.shift();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'在开头移出元素:'</span>+ first + <span class="hljs-string">' - 移出后数组:'</span> + arr);
len = arr.unshift(<span class="hljs-string">'Balsam'</span>, <span class="hljs-string">'sunflower'</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'在开头添加元素后长度变为:'</span> + len + <span class="hljs-string">'- 添加后数组:'</span> + arr);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/414046e7a96e401d915f2ac8599a4a96~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上述代码可以看出，<strong>push() 和 unshift() 方法可以为指定数组在末尾或开头添加一个或多个元素，而 pop() 和 shift() 方法则只能移出并返回指定数组在未尾或开头的一个元素。</strong></p>
<h2 data-id="heading-5"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.5.3_[案例] 筛选数组</h2>
<p>案例：要求在包含工资的数组中，剔除工资达到2000或以上的数据，把小于2000的数重新放到创新的数组里面。 其中数组为[1500，1200，2000， 2100， 1800]。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = (<span class="hljs-number">1500</span>, <span class="hljs-number">1200</span>, <span class="hljs-number">2000</span>, <span class="hljs-number">2100</span>, <span class="hljs-number">1800</span>];
<span class="hljs-keyword">var</span> newArr = [];

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
<span class="hljs-keyword">if</span> (arr[i] < <span class="hljs-number">2000</span>) &#123;
newArr.push(arr[<span class="hljs-number">1</span>);
<span class="hljs-comment">// 相当于: newArr (newArr.length] = arr[i];</span>
&#125;
&#125;

<span class="hljs-built_in">console</span>.log(newArr);
<span class="hljs-comment">// 输出结果: (3) [1500, 1200, 1800]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，第 1 行代码为原数组 arr。第 2 行代码定义了新数组 newArr，存放工资低于 2000 的数据。第 3 行代码在 for 循环语句中通过 if 语句进行判断，如果符合要求则使用 push() 方法，存储到新数组 newArr 中。</p>
<h2 data-id="heading-6"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.5.4_数组排序</h2>
<p><strong>数组排序可以实现数组元素排序或者颠倒数组元素的顺序等。</strong></p>
<p>排序方法：</p>

















<table><thead><tr><th>方法名</th><th>功能描述</th></tr></thead><tbody><tr><td>reverse()</td><td>颠倒数组中元素的位置，该方法会改变原数组，返回新数组</td></tr><tr><td>sort()</td><td>对数组的元素进行排序，该方法会改变原数组，返回新数组</td></tr></tbody></table>
<p>需要注意的是，<strong>reverse() 和 sort() 方法的返回值是新数组的长度。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//反转数组</span>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'red'</span>, <span class="hljs-string">'green'</span>, <span class="hljs-string">'blue'</span>];
arr.reverse();
<span class="hljs-built_in">console</span>.log(arr);<span class="hljs-comment">//输出结果:(3) ["blue", "green","red"]</span>
<span class="hljs-comment">//上述演示了 reverse() 方法的使用，实现数组元素的反转。</span>
<span class="hljs-comment">//数组排序</span>
<span class="hljs-keyword">var</span> arr1 = [<span class="hljs-number">13</span>, <span class="hljs-number">4</span>, <span class="hljs-number">77</span>, <span class="hljs-number">1</span>, <span class="hljs-number">7</span>];
arrl.sort(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a, b</span>) 
<span class="hljs-title">return</span> <span class="hljs-title">b</span> - <span class="hljs-title">a</span></span>;<span class="hljs-comment">//按降序的顺序排列</span>
&#125;);
<span class="hljs-built_in">console</span>.log(arr1);<span class="hljs-comment">//输出结果: (5) [77,13,7,4,1]</span>
<span class="hljs-comment">//上述演示了 sort() 方法的使用，实现数组元素从大到小进行排序。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf8640dce1e846579bd0be3e714b7b97~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">return</span> a - b;<span class="hljs-comment">// 按升序的顺序排列</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de3ea69b56a34c458666b0a2252758ab~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.5.5_数组索引</h2>
<p>在开发中，<strong>若要查找指定的元素在数组中的位置，则可以利用 Array 对象提供的检索方法。</strong></p>
<p>检索方法：</p>

















<table><thead><tr><th>方法名</th><th>功能描述</th></tr></thead><tbody><tr><td>indexOf()</td><td>返回在数组中可以找到到给定值的第一个索引，如果不存在，则返回-1</td></tr><tr><td>lastIndexOf()</td><td>返回指定元素在数组中的最后一个的索引，如果不存在则返回-1</td></tr></tbody></table>
<p>上述方法中，默认都是从指定数组索引的位置开始检索，并且检索方式与运算符 " === " 相同，即只有全等时才会返回比较成功的结果。</p>
<p>案例：演示，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'red'</span>, <span class="hljs-string">'green'</span>, <span class="hljs-string">'blue'</span>, <span class="hljs-string">'pink'</span>, <span class="hljs-string">'blue'</span>];
<span class="hljs-built_in">console</span>.log( arr.indexOf(<span class="hljs-string">'blue'</span>) );    <span class="hljs-comment">//输出结果:2</span>
<span class="hljs-built_in">console</span>.log( arr.lastIndexOf(<span class="hljs-string">'blue'</span>) );<span class="hljs-comment">//输出结果:4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，<strong>lastIndexOf() 方法用于在数组中从指定下标位置检索到最后一个给定值的下标。与 indexOf() 检索方式不同的是，lastIndexOf() 方法默认逆向检索，即从数组的末尾向数组的开头检索。</strong></p>
<h2 data-id="heading-8"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.5.6_[案例] 数组去除重复元素</h2>
<p>接下来我们通过一个案例来演示数组索引的使用。 要求在一组数据中，去除重复的元素。其中数组为 [‘blue’, ‘green’, ‘blue’] 。示例代码如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique</span>(<span class="hljs-params">arr</span>) </span>&#123;
<span class="hljs-keyword">var</span> newArr = [];
<span class="hljs-comment">// 用来存放数组中不重复的元素</span>

<span class="hljs-comment">// 遍历一遍数组，如果数组内某一元素重复出现则放入新数组中</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
<span class="hljs-keyword">if</span>(newArr.indexOf(arr[i]) == -<span class="hljs-number">1</span>) &#123;
newArr.push(arr[i]);
&#125;
&#125;

<span class="hljs-keyword">return</span> newArr;
&#125;

<span class="hljs-keyword">var</span> demo = unique([<span class="hljs-string">'blue'</span>, <span class="hljs-string">'green'</span>, <span class="hljs-string">'blue'</span>]);
<span class="hljs-built_in">console</span>.log(demo);
<span class="hljs-comment">// 输出结果: (4) ["blue","green"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>出现过，那么就添加到新数组中，否则不添加。其中第4行代码如果该元素判断如果返回值为-1就说明新数组里面没有该元素。</p>
<p>3利用新数组的在新数组中没有</p>
<h2 data-id="heading-9"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.5.7_数组转换为字符串</h2>
<p><strong>若需要将数组转换为字符串，可以利用数组对象的 join() 和 toString() 方法实现。</strong></p>
<p>数组转换为字符串：</p>

















<table><thead><tr><th>方法名称</th><th>功能描述</th></tr></thead><tbody><tr><td>toString()</td><td>把数组转换为字符串，逗号分隔每一项</td></tr><tr><td>join (’ 分隔符 ')</td><td>将数组的所有元素连接到一个字符串中</td></tr></tbody></table>
<p>案例：演示，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用toString()</span>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>];
<span class="hljs-built_in">console</span>.log ( arr.toString() );
<span class="hljs-comment">// 输出结果:a,b,c</span>

<span class="hljs-comment">// 使用join()</span>
<span class="hljs-built_in">console</span>.log ( arr.join() );
<span class="hljs-comment">// 输出结果:a,b,c</span>
<span class="hljs-built_in">console</span>.log ( arr.join(<span class="hljs-string">''</span>) );
<span class="hljs-comment">// 输出结果:abc</span>
<span class="hljs-built_in">console</span>.log ( arr.join(<span class="hljs-string">'-'</span>) );
<span class="hljs-comment">// 输出结果:a-b-c</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c1208223d7749b5acdcb1df7230216e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上述代码可知，<strong>join() 和 toString() 方法可将多维数组转为字符串，默认情况下使用逗号连接。不同的是，join() 方法可以指定连接数组元素的符号。另外，当数组元素为 undefined、null 或空数组时，对应的元素会被转换为空字符串。</strong></p>
<h2 data-id="heading-10"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.5.8_其他方法</h2>
<p>JavaScript 还提供了很多其他也比较常用的数组方法。例如，填充数组、连接数组、截取数组元素等。</p>
<p>其他方法：</p>

























<table><thead><tr><th>方法名</th><th>功能描述</th></tr></thead><tbody><tr><td>fill()</td><td>用一个固定值填充数组中指定下标范围内的全部元素</td></tr><tr><td>splice()</td><td>数组删除，参数为 splice(第几个开始，要删除个数)，返回被删除项目的新数组</td></tr><tr><td>slice()</td><td>数组截取，参数为 slice(begin, end)，返回被截取项目的新数组</td></tr><tr><td>concat()</td><td>连接两个或多个数组，不影响原数组，返回一个新数组</td></tr></tbody></table>
<p><strong>slice() 和 concat() 方法在执行后返回一个新的数组，不会对原数组产生影响，剩余的方法在执行后皆会对原数组产生影响。</strong></p>
<p>案例：splice() 方法在指定位置添加或删除数组元素，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'sky'</span>, <span class="hljs-string">'wind'</span>, <span class="hljs-string">'snow'</span>, <span class="hljs-string">'sun'</span>];
<span class="hljs-comment">// 从索引为2的位置开始，删除2个元索</span>
arr.splice(<span class="hljs-number">2</span>, <span class="hljs-number">2</span>);
<span class="hljs-built_in">console</span>.log (arr); 
<span class="hljs-comment">// 输出结果: (2) ["sky", "wind"]</span>

<span class="hljs-comment">// 从索引为1的位置开始，删除1个元素后，再添加 snow 元素</span>
arr.splice(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-string">'snow'</span>);
<span class="hljs-comment">// 输出结果: (2) ["sky", "snow"]</span>
<span class="hljs-built_in">console</span>.log(arr);

<span class="hljs-comment">// 从索引为1的位置开始，添加数组元素</span>
arr.splice(<span class="hljs-number">1.0</span>, <span class="hljs-string">'hail'</span>, <span class="hljs-string">'sun'</span>);
<span class="hljs-built_in">console</span>.log(arr);
<span class="hljs-comment">// 输出结果: (4) ["sky", "hail", "sun", "snow"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码中，splice() 方法的第 1 个参数用于指定添加或删除的下标位置；第 2 个参数用于从指定下标位置开始，删除数组元素的个数，将其设置为0，则表示该方法只添加元素；剩余的参数表示要添加的数组元素，若省略则表示删除元素。</p>
<p><strong>今日入门学习暂时告一段落<br>
Peace</strong></p>
<h1 data-id="heading-11"><strong>🌊🌈往期回顾：</strong></h1>
<p><a href="https://juejin.cn/post/6987731486707286030" title="https://juejin.cn/post/6987731486707286030" target="_blank"><strong>阿ken的HTML、CSS的入门指南(一)_HTML基础</strong></a><br>
<a href="https://juejin.cn/post/6988080294242811918/" title="https://juejin.cn/post/6988080294242811918/" target="_blank"><strong>阿ken的HTML、CSS的入门指南(二)_HTML页面元素和属性</strong></a><br>
<a href="https://juejin.cn/post/6988714719125176351" title="https://juejin.cn/post/6988714719125176351" target="_blank"><strong>阿ken的HTML、CSS的入门指南(三)_文本样式属性</strong></a><br>
<a href="https://juejin.cn/post/6991276111527149605" title="https://juejin.cn/post/6991276111527149605" target="_blank"><strong>阿ken的HTML、CSS的入门指南(四)_CSS3选择器</strong></a><br>
<a href="https://juejin.cn/post/6991769219910074399" title="https://juejin.cn/post/6991769219910074399" target="_blank"><strong>阿ken的HTML、CSS的入门指南(五)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6992015827692159007" title="https://juejin.cn/post/6992015827692159007" target="_blank"><strong>阿ken的HTML、CSS的入门指南(六)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6992383017834512421" title="https://juejin.cn/post/6992383017834512421" target="_blank"><strong>阿ken的HTML、CSS的入门指南(七)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6992747291685699614" title="https://juejin.cn/post/6992747291685699614" target="_blank"><strong>阿ken的HTML、CSS的入门指南(八)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6993130330479656968#heading-6" title="https://juejin.cn/post/6993130330479656968#heading-6" target="_blank"><strong>阿ken的HTML、CSS的入门指南(九)_浮动与定位</strong></a><br>
<a href="https://juejin.cn/post/6993487356665790495" title="https://juejin.cn/post/6993487356665790495" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十)_浮动与定位</strong></a><br>
<a href="https://juejin.cn/post/6993855890856083487" title="https://juejin.cn/post/6993855890856083487" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十一)_浮动与定位</strong></a><br>
<a href="https://juejin.cn/post/6994207456041631780" title="https://juejin.cn/post/6994207456041631780" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十二)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6994610939089649678" title="https://juejin.cn/post/6994610939089649678" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十三)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6994995902825906207" title="https://juejin.cn/post/6994995902825906207" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十四)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6995318091039113253" title="https://juejin.cn/post/6995318091039113253" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十五)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6995721790550966302" title="https://juejin.cn/post/6995721790550966302" target="_blank"><strong>阿ken的HTML、CSS的入门指南（十六）_多媒体技术</strong></a><br>
<a href="https://juejin.cn/post/6996068586783506463" title="https://juejin.cn/post/6996068586783506463" target="_blank"><strong>阿ken的HTML、CSS的入门指南（十七）_多媒体技术</strong></a></p>
<p><a href="https://juejin.cn/post/6997535282757287950" title="https://juejin.cn/post/6997535282757287950" target="_blank"><strong>【HTML干货分享 | 建议收藏】挑战最短时间带你走进HTML（十八）</strong></a><br>
<a href="https://juejin.cn/post/6997953156730585119" title="https://juejin.cn/post/6997953156730585119" target="_blank"><strong>【HTML干货分享 | 建议收藏】挑战最短时间带你走进HTML（十九）</strong></a><br>
<a href="https://juejin.cn/post/6998293783968219149" title="https://juejin.cn/post/6998293783968219149" target="_blank"><strong>【HTML干货分享 | 建议收藏】挑战最短时间带你走进HTML（二十）</strong></a></p>
<p><a href="https://juejin.cn/post/6985072343257677855" title="https://juejin.cn/post/6985072343257677855" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（一）</strong></a><br>
<a href="https://juejin.cn/post/6987241984154927134" title="https://juejin.cn/post/6987241984154927134" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（二）</strong></a><br>
<a href="https://juejin.cn/post/6985456953661063204" title="https://juejin.cn/post/6985456953661063204" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（三）</strong></a><br>
<a href="https://juejin.cn/post/6996434668908183566" title="https://juejin.cn/post/6996434668908183566" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（四）</strong></a><br>
<a href="https://juejin.cn/post/6996819069504585736" title="https://juejin.cn/post/6996819069504585736" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（五）</strong></a><br>
<a href="https://juejin.cn/post/6997220640759496734" title="https://juejin.cn/post/6997220640759496734" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（六）</strong></a><br>
<a href="https://juejin.cn/post/6999229094839713822" title="https://juejin.cn/post/6999229094839713822" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（七）</strong></a><br>
<a href="https://juejin.cn/post/6999431171121610788" title="https://juejin.cn/post/6999431171121610788" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（八）</strong></a></p>
<h1 data-id="heading-12"><strong>🌊🌈关于后记：</strong></h1>
<p><strong>感谢阅读，希望能对你有所帮助 博文若有瑕疵请在评论区留言或在主页个人介绍中添加联系方式私聊我 感谢每一位小伙伴不吝赐教</strong></p>
<p>原创不易，<strong>「点赞」+「关注」</strong> 谢谢支持❤</p></div>  
</div>
            