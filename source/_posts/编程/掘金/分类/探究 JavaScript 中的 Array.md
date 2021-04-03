
---
title: '探究 JavaScript 中的 Array'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d0ad76f2f3432c85884716420460ca~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 01:11:06 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d0ad76f2f3432c85884716420460ca~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>本文探究一下 <code>Array</code> ，并实现 Vue 中对数组下标操作进行响应式化， Vue 中的数组操作可看这篇文章 <a href="https://juejin.cn/post/6941348666422919204" target="_blank">Vue 数组操作及源码分析</a></p>
<h2 data-id="heading-1">什么是 Array</h2>
<blockquote>
<p>JavaScript的 <code>Array</code> 对象是用于构造数组的全局对象，数组是类似于列表的高阶对象。</p>
</blockquote>
<p>数组是引用数据类型,可通过字面量和 <code>Array()</code> 构造函数来创建，其中使用 <code>Array()</code> 构造函数时，若值传入一个实参，且为数字时，则生成一个 <code>length</code> 为该实参的空数组。</p>
<p><img alt="数组1.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d0ad76f2f3432c85884716420460ca~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">Array 下标操作</h2>
<p><img alt="数组2.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f10024534903463391ce69a92bb336ad~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>备注： 这里我在写示例时有一个小插曲，我是在 chrome 的 console 中，将代码全部执行完之后然后再打开折叠的输出内容，所以 chrome 应该是在我点击哪个三角形之后去读取变量 <code>a</code> 的内容，所以导致打印出来的内容一样，与 <code>Array</code> 无关，也没什么用，只是记录一下</p>
<h2 data-id="heading-3">Array 的方法</h2>
<p>Array 的方法在 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array#%E8%AF%AD%E6%B3%95" target="_blank" rel="nofollow noopener noreferrer">MDN</a> 中已经讲的非常清楚了，这里我作一些理解和总结</p>
<ol>
<li>数组也是对象，数组的原型对象为 <code>Array.prototype</code> ，拥有 <code>length</code> 属性。</li>
</ol>
<p><img alt="数组3.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b57b71cb64241e08aeb9ba684e39a54~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>备注： 这里我使用字面量定义数组 <code>a</code> 时，键名是数字 <code>1</code> ，但是也并没有报错，应该是自动转成字符串了，虽然没报错，但是不建议这样使用，不符合命名规范，记一下</p>
<ol start="2">
<li>数组的下标其实是字符串，这个知识点从上面的例子可以看出，所以我们定义一个拥有 <code>length</code> 的对象，然后将原型改为<code> Array.prototype</code> 也可以获得一个数组对象，但是其与使用字面量或构造函数定义的数组还是不同的，可以通过一些例子来证明</li>
</ol>
<p><img alt="数组4.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87781429581d47a0a35f9218171406f2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从图中可以看出，我们通过字面量定义数组 <code>a</code> ，我们按照 <code>1</code> 中的说法将 <code>a</code> 变成数组，但是我们操作 <code>length</code> 时，下标为 <code>10</code> 的属性并没有因为 <code>length</code> 的改变而被截掉，而是作为对象的属性 （这是 chrome 浏览器中的表现，其他引擎没有试，因为这个区别反正也是无用的知识，突发奇想测试出来的）</p>
<ol start="3">
<li>数组的长度是 <code>length</code> ，而不是里面存了多少元素，当然，数组中的元素数小于 <code>length</code> ，使用一些涉及到数组长度的方法是根据 <code>length</code> 来操作的，比如 <code>pop</code> 弹出的是 <code>[length -1]</code> 元素，如果该下标元素为空，则返回 <code>undefined</code></li>
</ol>
<h2 data-id="heading-4">Vue2 中响应式化下标操作的简单实现</h2>
<p>根据前面的学习，数组中的元素其实也可以类比键值对形式，而 Vue 中的响应式化就是通过 <code>Object.defineProperties()</code> 来将属性描述符设置为访问器描述符，即重写属性的 <code>get()</code> 和 <code>set()</code> ,而我们通过对下标进行响应式化即可监听对数组的下标操作，即重写下标的 <code>get()</code> 和 <code>set()</code> 即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Observer = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Observer</span> (<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.value = value;
  <span class="hljs-built_in">this</span>.dep = <span class="hljs-keyword">new</span> Dep();
  <span class="hljs-built_in">this</span>.vmCount = <span class="hljs-number">0</span>;
  def(value, <span class="hljs-string">'__ob__'</span>, <span class="hljs-built_in">this</span>);
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123;
    <span class="hljs-keyword">if</span> (hasProto) &#123;
      protoAugment(value, arrayMethods);
    &#125; <span class="hljs-keyword">else</span> &#123;
      copyAugment(value, arrayMethods, arrayKeys);
    &#125;
    <span class="hljs-comment">// this.observeArray(value);</span>
    <span class="hljs-built_in">this</span>.walkArray(value)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">this</span>.walk(value);
  &#125;
&#125;;

Observer.prototype.walkArray = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">walkArray</span> (<span class="hljs-params">obj</span>) </span>&#123;
  obj.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
    defineReactive$$1(obj, index) <span class="hljs-comment">// 在这里对其下标进行响应式化</span>
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="数组6.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cb1a976ff7248bf858e4c7953518c40~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>但是 <code>length</code> 无法进行响应式化，因为 <code>length</code> 的属性描述符不允许被修改</p>
<p><img alt="数组5.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bebc6a53d35c4e9f8a1357cc383a1590~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            