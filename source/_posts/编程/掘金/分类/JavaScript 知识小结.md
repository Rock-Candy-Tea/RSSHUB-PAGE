
---
title: 'JavaScript 知识小结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3d031c61e294cb795687fd7d8428e56~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 04 May 2021 06:08:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3d031c61e294cb795687fd7d8428e56~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">三个重要知识</h2>
<h3 data-id="heading-1">JS公式</h3>
<p><code>对象.__proto__ === 其构造函数.prototype</code></p>
<h3 data-id="heading-2">根公理</h3>
<p><code>Object.prototype</code>是所有对象的（直接或间接）原型</p>
<h3 data-id="heading-3">函数公理</h3>
<p>所有函数都是由Function构造的</p>
<p><code>任何函数.__proto__ === Function.prototype</code></p>
<p>任意函数有 Object / Array / Function</p>
<h2 data-id="heading-4">拨乱反正</h2>
<h3 data-id="heading-5">疑惑一</h3>
<h4 data-id="heading-6">xxx 的原型</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'frank'</span>&#125; 的原型<span class="hljs-comment">//Object.prototype</span>
[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>] 的原型<span class="hljs-comment">//Array.prototype</span>
<span class="hljs-built_in">Object</span> 的原型<span class="hljs-comment">//Function.prototype</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">解读</h4>
<p><code>Object</code> 的原型是 <code>Object.__proto__</code>：对
<code>Object</code> 的原型是 <code>Object.prototype</code> ：错</p>
<h4 data-id="heading-8">错在哪</h4>
<p>「的原型」等价于「<code>.__proto</code>__」
中文的「原型」无法区分<code> __proto__</code> 和 <code>prototype</code>
所以我们只能约定，原型默认表示 <code>__proto__ </code>
只不过<code>__proto__</code>正好等于某个函数的 <code>prototype</code></p>
<h3 data-id="heading-9">疑惑二</h3>
<h4 data-id="heading-10">矛盾</h4>
<p><code>[1,2,3]</code> 的原型是 <code>Array.prototype</code>
你有说 <code>Object.prototype</code> 是所有对象的原型
那为什么 <code>Object.prototype</code> 不是 <code>[1,2,3]</code> 的原型</p>
<h4 data-id="heading-11">错在哪</h4>
<p>原型分两种：直接原型和间接原型
对于普通对象来说，<code>Object.prototype</code> 是直接原型
对于数组、函数来说，<code>Object.prototype</code> 是间接原型</p>
<h3 data-id="heading-12">疑惑三</h3>
<p>Object.prototype 不是根对象</p>
<h4 data-id="heading-13">理由</h4>
<p><code>Object.prototype</code> 是所有对象的原型
<code>Object</code> 是 <code>Function</code> 构造出来的
所以，<code>Function</code> 构造了 <code>Object.prototype</code>
推论，<code>Function</code> 才是万物之源啊！</p>
<h4 data-id="heading-14">错在哪</h4>
<p><code>Object.prototype</code> 和 <code>Object.prototype</code> 对象的区别，虽然<code>Object.prototype</code>是Function构造出来的，但是<code>Object.prototype</code>对象不是Function构造出来的。
对象里面从来都不会包含另一个对象
接下来我们要把 JS 世界的建造顺序理清楚</p>
<h2 data-id="heading-15">JS世界的构造顺序</h2>
<ol>
<li>创建根对象 #101(toString)，根对象没有名字</li>
<li>创建函数的原型 #208(call /apply)，原型  <code>__proto__</code> 为 #101</li>
<li>创建数组的原型 #404(push/pop)，原型  <code>__proto__</code>  为 #101</li>
<li>创建 Function #342，原型 <code>__proto__</code> 为 #208__</li>
<li>用 Function.prototype <strong>存储函数的原型</strong>，等于 #208</li>
<li>此时发现 Function 的 <code>__proto__</code> 和 prototype 都是 #208</li>
<li>用 Function 创建 Object</li>
<li>用 Object.prototype 存储对象的原型，等于 #101</li>
<li>用 Function 创建 Array</li>
<li>用 Array.prototype 存储数组的原型，等于 #404</li>
<li>创建 window 对象</li>
<li>用 window 的 'Object' 'Array' 属性将 7 和 9 中的函数命名</li>
<li>记住一点，JS 创建一个对象时，不会给这个对象名字的</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3d031c61e294cb795687fd7d8428e56~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501170626427.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>用 <code>new Object()</code> 创建 <code>obj1</code></p>
</li>
<li>
<p><code>new</code> 会将 <code>obj1</code> 的原型 <code>__proto__</code>设置为 <code>Object.prototype</code>，也就是 #101</p>
</li>
<li>
<p>用 <code>new Array()</code> 创建 <code>arr1</code></p>
</li>
<li>
<p><code>new</code> 会将 <code>arr1</code> 的原型 <code>__proto__</code> 设置为 <code>Array.prototype</code>，也就是 #404</p>
</li>
<li>
<p>用 <code>new Function</code> 创建 f1</p>
</li>
<li>
<p><code>new</code> 会将 <code>f1</code> 的原型 <code>__proto__</code> 设置为 <code>Function.prototype</code>，也就是 #208</p>
</li>
<li>
<p>自己定义构造函数 Person，函数里给 this 加属性</p>
</li>
<li>
<p>Person 自动创建 prototype 属性和对应的对象 #502</p>
</li>
<li>
<p>在 Person.prototype #502 上面加属性</p>
</li>
<li>
<p>用 new Person() 创建对象 p</p>
</li>
<li>
<p>new 会将 p 的原型 <code>__proto__</code> 设为 #502</p>
</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/077f36d5e2374de88398ab336f733b77~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501211603251.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>Object.prototype</code>的原型是什么？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c117bd1ce7344e3e870abd922044ddf8~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501212703990.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p><code>Function.prototype</code>的原型是什么？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0aa4e58339f14b129f97f781dfb9e589~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501213003313.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p><code>var f = () => &#123;&#125;</code>，<code>f</code>的原型是什么？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/434de135c0b2464ca7470a02fc03509e~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501215357008.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p><code>Function</code>的原型是什么？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa33af8e0ce444378967b9c5d7bf3295~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501215929100.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p><code>Array.prototype.toString</code>的原型是什么？</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/493fcc0321f343e3b79a198b0a7656a8~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501222344306.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p><code>Object</code>的原型是什么？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b4191fd32624baa82799bcdb6cd247c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501222517405.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote></div>  
</div>
            