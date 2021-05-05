
---
title: 'jQuery 中的设计模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78811d9cfd98415ebd9dee2cf5bed12a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 04 May 2021 06:42:33 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78811d9cfd98415ebd9dee2cf5bed12a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">链式风格</h3>
<h4 data-id="heading-1">也叫jQuery风格</h4>
<p><code>window.jQuery()</code>是我们提供的全局函数</p>
<h4 data-id="heading-2">特殊函数jQuery</h4>
<p>jQuery（选择器）用于获取对应的元素，但它却不返回这些元素。</p>
<p>相反，它返回一个对象，称为jQuery构造出来的对象，这个对象可以操作相应的元素。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78811d9cfd98415ebd9dee2cf5bed12a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504152456575.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ef98cae26bc4ed1a77334b4990b9fb9~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504152512743.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">jQuery是构造函数吗？</h3>
<h4 data-id="heading-4">是</h4>
<p>因为jQuery函数确实构造出了一个对象</p>
<h4 data-id="heading-5">不是</h4>
<p>因为不需要写<code>new jQuery()</code>就能构造一个对象</p>
<p>以前讲的构造函数都要结合new才行，比如<code>var obj = new Object()</code></p>
<h4 data-id="heading-6">结论</h4>
<p>jQuery是一个不需要加new的构造函数</p>
<p>jQuery不是常规意义上的构造函数</p>
<p>这是因为jQuery用了一些技巧</p>
<h3 data-id="heading-7">术语</h3>
<h4 data-id="heading-8">jQuery对象</h4>
<p>jQuery对象指代jQuery函数构造出来的对象，也就是那个api</p>
<p>jQuery对象不是说jQuery这个对象</p>
<h4 data-id="heading-9">举例</h4>
<p>Object是个函数，Object对象表示Object构造出的对象</p>
<p>Array是个函数，Array对象/数组对象表示Array构造出来的对象</p>
<p>Function是个函数，Function对象/函数对象表示Function构造出来的对象</p>
<h3 data-id="heading-10">手写jQuery</h3>
<p><a href="https://github.com/RiverCui/dom-2" target="_blank" rel="nofollow noopener noreferrer">源码</a></p>
<h4 data-id="heading-11">命名风格</h4>
<h5 data-id="heading-12">下面代码令人误解</h5>
<p><code>const div = $('div#test')</code></p>
<p>我们会误以为div是一个DOM，实际上div是jQuery构造的api对象</p>
<h5 data-id="heading-13">改成这样</h5>
<p><code>const $div = $('div#test')</code></p>
<p><code>$div.appendChild</code>不存在，因为它不是DOM对象</p>
<p><code>$div.find</code>存在，因为它是jQuery对象</p>
<h4 data-id="heading-14">链式风格</h4>
<h5 data-id="heading-15">增</h5>
<p><code>$('<div><span>1</span></div>')</code></p>
<p>返回值并不是新增的元素，而是api对象</p>
<p><code>$('<div><span>1</span></div>').appendTo(document.body)</code></p>
<p>appendTo可以把新增的元素放到另一个元素里，类似上面这样操作</p>
<h5 data-id="heading-16">总结</h5>
<p>感觉DOM是不可见的，不需要知道DOM的任何细节，只需要使用简洁的API即可</p>
<p>一个好的封装，能让使用者完全不知道内部细节，只是通过闭包实现的</p>
<h4 data-id="heading-17">如果想知道细节怎么办</h4>
<h5 data-id="heading-18">举例1</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> $div = $(<span class="hljs-string">'div#test'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>$div</code>并不是DOM对象，而是<code>jQuery</code>构造的api对象</p>
<p>如何从<code>$div</code>中得到<code>div</code>呢？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">$div.get(<span class="hljs-number">0</span>) 获取第<span class="hljs-number">0</span>个元素 <span class="hljs-comment">//div</span>
$div.get(<span class="hljs-number">1</span>) 获取第<span class="hljs-number">1</span>个元素 <span class="hljs-comment">//undefined</span>
$div.get(<span class="hljs-number">2</span>) 获取第<span class="hljs-number">2</span>个元素 <span class="hljs-comment">//undefined</span>
$div.size() 得到元素的个数
$div.length 也可以得到元素的个数
$div.get() 获取所有元素组成的数组 <span class="hljs-comment">//[div]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">举例2</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> $div = $(<span class="hljs-string">'.red'</span>) <span class="hljs-comment">//假设有3个div.red</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>$div</code>不是DOM对象们，而不是<code>jQuery</code>构造的api对象</p>
<p>如何从<code>$div</code>中得到<code>div</code>呢？</p>
<p>一样的</p>
<pre><code class="hljs language-js copyable" lang="js">$div.get(<span class="hljs-number">0</span>) 获取第<span class="hljs-number">0</span>个元素 <span class="hljs-comment">//div</span>
$div.get(<span class="hljs-number">1</span>) 获取第<span class="hljs-number">1</span>个元素 <span class="hljs-comment">//div</span>
$div.get(<span class="hljs-number">2</span>) 获取第<span class="hljs-number">2</span>个元素 <span class="hljs-comment">//div</span>
$div.size() 得到元素的个数
$div.length 也可以得到元素的个数
$div.get() 获取所有元素组成的数组 <span class="hljs-comment">//[div,div,div]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>$div.get(0)</code>太麻烦，使用更简单的<code>$div[0]</code></strong></p>
<h4 data-id="heading-20">重新开始写链式风格</h4>
<h5 data-id="heading-21">查</h5>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">'#xxx'</span>) <span class="hljs-comment">//返回值并不是元素，而是一个api对象</span>
$(<span class="hljs-string">'#xxx'</span>).find(<span class="hljs-string">'.red'</span>) <span class="hljs-comment">//查找#xxx里的.red元素</span>
$(<span class="hljs-string">'#xxx'</span>).parent() <span class="hljs-comment">//获取新爸爸</span>
$(<span class="hljs-string">'#xxx'</span>).children() <span class="hljs-comment">//获取儿子</span>
$(<span class="hljs-string">'#xxx'</span>).siblings() <span class="hljs-comment">//获取兄弟</span>
$(<span class="hljs-string">'#xxx'</span>).index() <span class="hljs-comment">//获取排行老几（从0开始）</span>
$(<span class="hljs-string">'#xxx'</span>).next() <span class="hljs-comment">//获取弟弟</span>
$(<span class="hljs-string">'#xxx'</span>).prev() <span class="hljs-comment">//获取哥哥</span>
$(<span class="hljs-string">'.red'</span>).each(fn) <span class="hljs-comment">//遍历并对每个元素执行fn</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">增</h5>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">'body'</span>) <span class="hljs-comment">// 获取document.body</span>
$(<span class="hljs-string">'body'</span>).append($<span class="hljs-string">'<div>1</div>'</span>) <span class="hljs-comment">//添加小儿子</span>
$(<span class="hljs-string">'body'</span>).append(<span class="hljs-string">'<div>1</div>'</span>) <span class="hljs-comment">//更方便</span>
$(<span class="hljs-string">'body'</span>).prepend(div或$div) <span class="hljs-comment">//添加大儿子</span>
$(<span class="hljs-string">'#test'</span>).after(div或$div) <span class="hljs-comment">//添个弟弟</span>
$(<span class="hljs-string">'#test'</span>).before(div或$div) <span class="hljs-comment">//添个哥哥</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-23">删</h5>
<pre><code class="hljs language-js copyable" lang="js">$div.remove()
$div.empty()
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-24">改</h5>
<pre><code class="hljs language-js copyable" lang="js">$div.text(?) <span class="hljs-comment">//读写文本内容</span>
$div.html(?) <span class="hljs-comment">//读写HTML内容</span>
$div.attr(<span class="hljs-string">'title'</span>,?) <span class="hljs-comment">//读写属性</span>
$div.css(&#123;<span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>&#125;) <span class="hljs-comment">//读写style //$div.style更好，但是jQuery是用的css</span>
$div.addClass(<span class="hljs-string">'blue'</span>)/removeClass/hasClass <span class="hljs-comment">// 添加 / 移除 / 检查是否有</span>
$div.on(<span class="hljs-string">'click'</span>,fn)
$div.off(<span class="hljs-string">'click'</span>,fn)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：<code>$div</code>可能对应了多个<code>div</code>元素</p>
<h4 data-id="heading-25">后续</h4>
<h5 data-id="heading-26">使用原型</h5>
<p>把共有属性（函数）全都放到<code>$.prototype</code></p>
<p><code>$.fn=$.prototype</code> //名字太长</p>
<p>然后让<code>api.__proto__</code>指向<code>$fn</code></p>
<h4 data-id="heading-27">设计模式</h4>
<h5 data-id="heading-28">jQuery用到了哪些设计模式</h5>
<p>不用new的构造函数，这个模式没有专门的名字</p>
<p>$(支持多种参数)，这个模式叫做重载</p>
<p>用闭包隐藏细节，这个模式没有专门的名字</p>
<p><code>$div.text()</code>既可读也可写，getter/setter</p>
<p><code>$.fn</code>是<code>$.prototype</code>的别名，这叫别名</p>
<p>jQuery针对不同浏览器使用不同代码，这叫适配器</p>
<h5 data-id="heading-29">设计模式是什么？</h5>
<p>设计模式就是对通用代码取个名字</p></div>  
</div>
            