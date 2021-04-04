
---
title: '详细剖析JavaScript原型和原型链机制并重写new与Object.create'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b4478a23a64960aa514d65aa4bc3a4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 08:07:11 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b4478a23a64960aa514d65aa4bc3a4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>承接上一篇<a href="https://juejin.cn/post/6943593611355226142/#heading-13" target="_blank">面向对象基础知识——原型与原型链基础知识</a></p>
<p>下面从两个角度分析解释原型是什么，原型链机制又是如何运作的</p>
<h2 data-id="heading-0">从两个角度先说说概念</h2>
<h3 data-id="heading-1">从<strong>函数数据类型</strong>角度分析</h3>
<p>大部分<strong>函数数据类型</strong>的值都具备<code>prototype</code>（原型/显式原型）属性，属性值本身是一个对象。浏览器会默认为其开辟一个堆内存，用来存储当前类所属实例可以调用的公共的属性和方法。在浏览器默认开辟的这个堆内存（原型对象）中，有一个默认的属性 <code>constructor</code>（构造函数/构造器），属性值是当前函数/类本身。</p>
<h4 data-id="heading-2">函数数据类型分类</h4>
<ul>
<li>普通函数（实名或者匿名函数）</li>
<li>箭头函数</li>
<li>构造函数/类「内置类/自定义类」</li>
<li>生成器函数 <code>Generator</code></li>
<li>...</li>
</ul>
<h4 data-id="heading-3">不具备<code>prototype</code>的函数</h4>
<ul>
<li>箭头函数  <code>const fn=()=>&#123;&#125;</code></li>
<li>基于ES6给对象某个成员赋值函数值的快捷操作
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> obj = &#123;
     <span class="hljs-attr">fn1</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 常规写法  具备prototype属性</span>
     &#125;,
     <span class="hljs-function"><span class="hljs-title">fn2</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 快捷写法  不具备prototype属性</span>
     &#125;
  &#125;;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Fn</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span> &#123;&#125; <span class="hljs-comment">//这样的也不具备prototype属性</span>
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-4">从<strong>对象数据类型值</strong>角度分析</h3>
<p>每一<strong>对象数据类型</strong>的值都具备一个属性<code>__proto__</code>（原型链/隐式原型），属性值指向<strong>自己所属类的原型
<code>prototype</code></strong>。</p>
<p>ps：这里先不考虑函数类型的对象</p>
<h4 data-id="heading-5">对象数据类型值分类</h4>
<ul>
<li>普通对象</li>
<li>特殊对象：数组、正则、日期、<code>Math</code>、<code>Error</code>...</li>
<li>函数对象</li>
<li>实例对象</li>
<li>构造函数。prototype</li>
</ul>
<p>面向对象的底层都是基于这两个角度：类（构造函数）和实例对象</p>
<h3 data-id="heading-6">总结</h3>
<p>记住这两个最重要的概念：</p>
<ol>
<li>大部分<strong>函数数据类型</strong>的值都具备<code>prototype</code>（原型/显式原型）属性，属性值本身是一个对象。浏览器会默认为其开辟一个堆内存，用来存储当前类所属实例可以调用的公共的属性和方法。在浏览器默认开辟的这个堆内存（原型对象）中，有一个默认的属性 <code>constructor</code>（构造函数/构造器），属性值是当前函数/类本身</li>
<li>每一<strong>对象数据类型</strong>的值都具备一个属性<code>__proto__</code>（原型链/隐式原型），属性值指向<strong>自己所属类的原型 <code>prototype</code></strong>。</li>
</ol>
<h2 data-id="heading-7">举例理解概念</h2>
<p>举例一个内置类（数组类<code>Array</code>和其实例）来理解以上概念</p>
<h3 data-id="heading-8">函数数据类型角度理解</h3>
<p>我们知道，任何函数在内存中会存在：作用域，代码字符串，属性键值对，那我们来看看<code>Array</code></p>
<ol>
<li>
<p>作用域
<img alt="image。png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b4478a23a64960aa514d65aa4bc3a4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>因为是内置的，作用域不清楚，但是是有作用域的</p>
</li>
<li>
<p>代码字符串
<img alt="image。png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e56e2777bab47b0a0473a18205c5c00~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>[native code]</code> 为代码字符串，可能为C++写的，浏览器内置代码不让我们不看</p>
</li>
<li>
<p>属性键值对中的<code>proptotype</code>属性
每一个函数都天生具备一个<code>proptotype</code>，所以<code>Array</code>中也是有的</p>
<p><img alt="image。png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e29734a16a6412ab2e62929346c4bfa~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>并且<code>proptotype</code>对象中有一个<code>constructor</code>属性指向函数本身，另外包含很多<code>Array</code>的公共属性（<code>concat</code>,<code>forEach</code>等），如图：</p>
<p><img alt="image。png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6423d96e9aa495c8ec1d27284c6cfeb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>总结：</p>
<p><img alt="image。png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60bb856754d04103be9934269410827e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ol>
<p>同样，<code>Object</code>函数也是一样</p>
<p><img alt="image。png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec84687513594aad9bd312eb0947fee3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">对象数据类型角度理解</h3>
<p>ps：函数也是对对象，关于<strong>函数多种角色</strong>的问题这里暂时先不讨论,后面写文章进行补充</p>
<p>实例对象，<code>prototype</code>（原型对象），函数对象，都是对象，所有的对象都有<code>__proto__</code>属性，这个属性指向所属类的原型对象。</p>
<p>指向关系如下</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52b4cdae7f2f4b9b842620cd6cbe0d1f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>注意容易混淆的点：</p>
<p>原型对象并不是他所属的构造函数的一个实例，比如<code>Array.prototype</code>不是<code>Array</code>的一个实例。因为既然作为原型，他是所有实例用来共享属性和方法的对象，所以不会是其中的一个实例。只有<code>new</code>出来的才算是某个构造函数的实例。<code>Array</code>的原型对象是浏览器默认开辟出来的，这里不是<code>Array</code>构造函数的实例。
<img alt="image。png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6afcbce8d5bc497ebcef9e0f7c04d192~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过浏览器我们发现<code>Array.prototype.__proto__</code>指向<code>Object.proptotype</code>，所以<code>Array.prototype</code>是<code>Object</code>的实例</p>
<p><img alt="image。png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be667c305fd445fa8c176912228bd4fe~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>注意更加特殊的<code>Object.prototype.__proto__</code>，指向<code>null</code>。因为<code>Object</code>是所有对象的基类，<code>Object.prototype</code>本身就是一个对象，<code>Object.prototype.__proto__</code>最后只能指向自己，即<code>Object.prototype</code>，这是没有意义的，所以最后浏览器让其指向<code>null</code>，这样也更合理一点。</p>
<p><img alt="image。png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22c64128588a4067a8c7b483454cbd43~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image。png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c78100b75323405ca9064b59046a5c55~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="image。png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1df48482291b48f08452f955238d00ff~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>那么以上原型链机制的定义明确了以后，平常是怎么运作的呢？举个例子理解：</p>
<p>执行<code>arr.length</code>，查看<code>arr</code>的属性<code>length</code>，或者执行<code>arr.push</code>的过程：</p>
<p>首先访问自己的私有属性，如果私有属性中是存在的，则直接使用。如果访问的成员在私有属性中没有，默认会基于<code>__proto__</code>找到所属类的<code>prototype</code>上的属性/方法。</p>
<p>所以<code>Array.prototype</code>上的方法，例如<code>push</code>等，相对于<code>Array</code>的实例来说，算是共有属性</p>
<p>执行或使用<code>arr.hasOwnProperty</code>的过程：</p>
<p>私有没有，<code>Array.prototype</code>上也没有，所以会继续基于<code>Array.prototype.__proto__</code>继续往上寻找，最终在<code>Object.prototype</code>上找到该方法，如果再找不到就返回<code>undefined</code>。</p>
<p>我们把上面这种成员访问的查找机制叫做<strong>原型链机制</strong></p>
<p>如下图：</p>
<p><img alt="image。png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/586aa3f24fb54fdf9bc51f58b0c6ba5a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>以上是最常用的成员访问机制，还有一些其他方法进行成员访问：</p>
<p>例如<code>arr.forEach()</code>,除了直接这样使用,还可以:</p>
<ol>
<li>可以直接使用<code>arr.__proto__.forEach()</code>这样可以直接跳过私有属性的查找，直接使用原型对象上的方法（此方法平时一般不会自己手动操作，因为ie浏览器没法使用这个方法，ie将其保护起来，不允许我们访问）</li>
<li>也可以<code>Array.prototype.forEach()</code>，也可以直接使用原型对象上的方法</li>
</ol>
<p>那么这几种方法的区别是什么？三者都是找到<code>Array.prototype.forEach</code>，并且让其执行，区别在于<code>forEach</code>方法中的<code>this</code>指向不一样。谁调用了方法，点前面是什么，<code>this</code>就是什么。以上三种方式的<code>this</code>分别是<code>arr</code>,<code>arr__proto__</code>，<code>Array。prototype</code></p>
<p>如下例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">10</span>, <span class="hljs-number">20</span>, <span class="hljs-number">30</span>];
<span class="hljs-built_in">console</span>.log(arr.hasOwnProperty(<span class="hljs-string">'forEach'</span>)); <span class="hljs-comment">//->false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单来看，上面的代码是 验证<code>forEach</code>是否为<code>arr</code>对象的私有属性</p>
<p>那么整个的执行过程实际上是：</p>
<p><code>arr</code>按照原型链查找机制，找到的是<code>Object.prototype.hasOwnProperty</code>方法「@A」，并且把找到的@A执行，注意：</p>
<ul>
<li>@A方法中的<code>this</code>应该是<code>arr</code>「我们要操作的对象」</li>
<li>传递的实参应该是<code>forEach</code>「我们要验证的属性」
@A方法的作用是，验证“实参”是否为当前<code>this</code>的一个私有属性
，那么最终同等效果的执行方式为：===> <code>Object.prototype.hasOwnProperty.call(arr,'forEach')</code></li>
</ul>
<h4 data-id="heading-10">公有属性和私有属性的"相对"</h4>
<p>另外需要注意的点：公有属性和私有属性是"相对"的。</p>
<p>例如相对于<code>arr</code>这个实例对象，<code>Array.prototype</code>这个对象里面的<code>push</code>等方法是各个<code>arr</code>实例的公有属性。而<code>Array.prototype</code>他自己本身就是一个对象，<code>push</code>在他这里就是他自己的私有方法，所以对象上的属性是共有还是私有，得要相对来说。当做公有属性，是相对于类的实例来说，当做私有属性是相对于自身来说</p>
<p><img alt="image。png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f55fa9dea41e41e985eca2aa237b7505~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image。png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19b49faf9a344ca9a87142f590c670e6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>所以没有公有属性，私有属性这个严格的概念，而只是相对来说，当不同的角色有了不同的功能，最后才区分了公有，私有的概念。</p>
<p>这样明白以后，我们在写代码进行操作的时候，例如我们做一个字符串截取工作，那么我们可以直接查看<code>String.prototype</code>上有什么公有方法可以直接调用来使用，然后还可以顺着<code>__proto__</code>继续往上找公有方法，按照原型连一级级往上找，只要出现在原型链上的方法都可以使用。</p>
<p>例如我们一直往上找<code>document.body</code>实例的方法，发现其有事件相关的方法</p>
<p><img alt="image。png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dae118cb319546a590f44f28b187d589~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这样我们就可以使用<code>document.body.addEventListener</code>，再例如dom操作都有的<code>classList</code>方法，用来操作class</p>
<p><img alt="image。png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9ab6dfddecd404b991e73975350fe1f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>都可以找到相关的方法</p>
<p>所以，整个JS就是基于面向对象思想构建的</p>
<h4 data-id="heading-11">加深理解的例子</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.x = <span class="hljs-number">100</span>;
    <span class="hljs-built_in">this</span>.y = <span class="hljs-number">200</span>;
    <span class="hljs-built_in">this</span>.getX = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.x);
    &#125;;
&#125;
Fn.prototype.getX = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.x);
&#125;;
Fn.prototype.getY = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.y);
&#125;;
<span class="hljs-keyword">let</span> f1 = <span class="hljs-keyword">new</span> Fn;
<span class="hljs-keyword">let</span> f2 = <span class="hljs-keyword">new</span> Fn;
<span class="hljs-built_in">console</span>.log(f1.getX === f2.getX);<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(f1.getY === f2.getY);<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(f1.__proto__.getY === Fn.prototype.getY);<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(f1.__proto__.getX === f2.getX);<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(f1.getX === Fn.prototype.getX);<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(f1.constructor);<span class="hljs-comment">//Fn</span>
<span class="hljs-built_in">console</span>.log(Fn.prototype.__proto__.constructor);<span class="hljs-comment">//Object</span>
f1.getX();<span class="hljs-comment">//100</span>
f1.__proto__.getX();<span class="hljs-comment">//undefined</span>
f2.getY();<span class="hljs-comment">//200</span>
Fn.prototype.getY();<span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image。png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aec4951c8c684edb80ab4d2c81e8d11c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
注：<code>new Fn()</code> 和<code>new Fn</code>是一样的效果，只是前者优先级是20，可传参数，后者优先级是19，不传参数</p>
<p>分析：</p>
<p>f1和f2都如下，迷惑点在于，其私有属性和原型上都有<code>getX</code>函数，两个私有属性地址不一样，返回false，而原型是同一个对象，其中的<code>getX</code>函数是同一个地址</p>
<p><code>__proto__</code>返回原型</p>
<p><img alt="image。png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/451e6d8f252542ceab2111594336f2c8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image。png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/158b11c24ffc456184a2d4c22d8a3fbe~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">重写内置<code>new</code></h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Dog</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
&#125;
Dog.prototype.bark = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'wangwang'</span>);
&#125;
Dog.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'my name is '</span> + <span class="hljs-built_in">this</span>.name);
&#125;
<span class="hljs-comment">/*
let sanmao = new Dog('三毛');
sanmao.sayName();
sanmao.bark();
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_new</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">//=>完成你的代码   </span>
&#125;
<span class="hljs-keyword">let</span> sanmao = _new(Dog, <span class="hljs-string">'三毛'</span>);
sanmao.bark(); <span class="hljs-comment">//=>"wangwang"</span>
sanmao.sayName(); <span class="hljs-comment">//=>"my name is 三毛"</span>
<span class="hljs-built_in">console</span>.log(sanmao <span class="hljs-keyword">instanceof</span> Dog); <span class="hljs-comment">//=>true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>new</code> 关键字做了什么：</p>
<ol>
<li>创建Ctor的一个实例对象（创建一个实例对象，并将实例对象的<code>__proto__</code>指向<code>Ctor.prototype</code>）</li>
<li>把构造函数当做普通函数执行，并且让方法中的<code>this</code>指向实例对象</li>
<li>确认方法执行的返回值。如果没有返回值或者返回的是原始值，让其默认返回实例对象即可。</li>
</ol>
<p>注：</p>
<ol>
<li>
<p>Ctor -> <code>constructor</code>缩写 构造函数</p>
</li>
<li>
<p>params -> 后期给Ctor传递的所有的实参信息</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_new</span>(<span class="hljs-params">Ctor, ...params</span>) </span>&#123;
    <span class="hljs-comment">// 1.创建Ctor的一个实例对象 </span>
    <span class="hljs-comment">// 实例.__proto__===Ctor.prototype</span>
    <span class="hljs-keyword">let</span> obj = &#123;&#125;;<span class="hljs-comment">//这里仅仅只创建了Object的一个实例对象 </span>
    obj.__proto__ = Ctor.prototype;

    <span class="hljs-comment">// 2.把构造函数当做普通函数执行「让方法中的THIS->实例对象」</span>
    <span class="hljs-keyword">let</span> result = Ctor.call(obj, ...params);

    <span class="hljs-comment">// 3.确认方法执行的返回值「如果没有返回值或者返回的是原始值，我们让其默认返回实例对象即可」</span>
    <span class="hljs-keyword">if</span> (result !== <span class="hljs-literal">null</span> && <span class="hljs-regexp">/^(object|function)$/</span>.test(<span class="hljs-keyword">typeof</span> result)) <span class="hljs-keyword">return</span> result;
    <span class="hljs-keyword">return</span> obj;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建Ctor的一个实例对象 如果用</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> obj = &#123;&#125;;<span class="hljs-comment">//这里仅仅只创建了Object的一个实例对象 </span>
    obj.__proto__ = Ctor.prototype;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这种方法不太好，下面说说新的方法</p>
<h2 data-id="heading-13"><code>Object.create()</code></h2>
<p><code>Object.create([obj])</code>：创建一个空对象，并且让<code>空对象.__proto__</code>指向 <code>obj</code> 。</p>
<p>官方解释：把<code>obj</code>作为新实例对象的原型。</p>
<p>也这样解读：以<code>obj</code>为原型，创造一个新对象</p>
<p>注意：</p>
<ul>
<li>参数<code>obj</code>可以是一个对象或者是<code>null</code>，但是不能是其他的值</li>
<li><code>Object.create(null)</code>  创建一个不具备<code>__proto__</code>属性的对象（不是任何类的实例）</li>
</ul>
<h3 data-id="heading-14">重写<code>Object.create()</code></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>._create = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">prototype</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (prototype !== <span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> prototype !== <span class="hljs-string">"object"</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Object prototype may only be an Object or null'</span>);
    <span class="hljs-keyword">var</span> <span class="hljs-built_in">Proxy</span> = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Proxy</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
    <span class="hljs-built_in">Proxy</span>.prototype = prototype;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：
<img alt="image。png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fc7751d13f8438d9afdc42a24798560~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>需要注意的是，我们自己写的这个<code>_create</code>，在传入<code>null</code>的时候是无法消除<code>__proto__</code>的</p>
<p><img alt="image。png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1afeb15b6cb4260be2c9632d530f579~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image。png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1471636644464977a07f5a4db750434d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<code>__proto__</code>是没办法消除的，无法删除，并且直接指向<code>Object</code></p>
<p><img alt="image。png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92fbe8773a254a64b832e92de73b478f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">允许使用<code>Object.create()</code>时重写<code>new</code></h3>
<p>使用<code>Object.create()</code>可替代重写<code>new</code>的第一步</p>
<p>将变量前置声明，更加规范，并注意一些校验规则
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bcf985047fa44a2b389f1692ad587df~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_new</span>(<span class="hljs-params">Ctor, ...params</span>) </span>&#123;
    <span class="hljs-keyword">let</span> obj,
        result,
        proto = Ctor.prototype,
        ct = <span class="hljs-keyword">typeof</span> Ctor;
    <span class="hljs-comment">// 构造函数的校验规则</span>
    <span class="hljs-comment">//前提不能是Symbol或者BigInt,然后Ctor不是函数或者proto不存在(箭头函数)就抛出一个类型错误</span>
    <span class="hljs-keyword">if</span> (Ctor === <span class="hljs-built_in">Symbol</span> || Ctor === BigInt || ct !== <span class="hljs-string">'function'</span> || !proto) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;Ctor&#125;</span> is not a constuctor!`</span>);
    
    <span class="hljs-comment">//符合规则后按逻辑来</span>
    <span class="hljs-comment">//1. </span>
    obj = <span class="hljs-built_in">Object</span>.create(Ctor.prototype);
    <span class="hljs-comment">//2. </span>
    result = Ctor.call(obj, ...params);
    <span class="hljs-comment">//3. </span>
    <span class="hljs-keyword">if</span> (result !== <span class="hljs-literal">null</span> && <span class="hljs-regexp">/^(object|function)$/</span>.test(<span class="hljs-keyword">typeof</span> result)) <span class="hljs-keyword">return</span> result;
    <span class="hljs-keyword">return</span> obj;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            