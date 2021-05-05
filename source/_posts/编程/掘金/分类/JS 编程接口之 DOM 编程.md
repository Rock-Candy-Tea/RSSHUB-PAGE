
---
title: 'JS 编程接口之 DOM 编程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8ad99e9b13a49b896bbc1379ed82ac7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 04 May 2021 06:39:31 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8ad99e9b13a49b896bbc1379ed82ac7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">DOM 简介</h2>
<h3 data-id="heading-1">网页其实是一棵树</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8ad99e9b13a49b896bbc1379ed82ac7~tplv-k3u1fbpfcp-watermark.image" alt="image-20210503211900220.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed3e95f876c045eea1ecdf364d52c907~tplv-k3u1fbpfcp-watermark.image" alt="image-20210503211930116.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">JS如何操作这棵树</h3>
<p>浏览器往window上加一个document即可，JS用document操作网页，这就是<strong>Document Object Model 文档对象模型</strong>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9da2d5e820e347ceb5078bf6bc5e5053~tplv-k3u1fbpfcp-watermark.image" alt="image-20210503212452890.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">API</h2>
<h3 data-id="heading-4">获取元素，也叫标签</h3>
<h4 data-id="heading-5">有很多API</h4>
<pre><code class="copyable">window.idxxx//或直接 idxxx，最简单的方法，但有时会有冲突

document.getElementByld('idxxx')
document.getElementsByTagName('div')[0]
document.getElementsByClassName('red')[0]//这三种方法复杂不常用

document.querySelector('#idxxx') //注意加#号
document.querySelectorAll('.red')[0]//这两种方法是常用的
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">获取特定元素</h4>
<h5 data-id="heading-7">获取html元素</h5>
<p><code>document.ducumentElement</code></p>
<h5 data-id="heading-8">获取head元素</h5>
<p><code>document.head</code></p>
<h5 data-id="heading-9">获取body元素</h5>
<p><code>document.body</code></p>
<h5 data-id="heading-10">获取窗口（窗口不是元素）</h5>
<p><code>window</code></p>
<h5 data-id="heading-11">获取所有元素</h5>
<p><code>document.all</code></p>
<p><code>document.all</code>是ie发明的，是第6个falsy值。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2779bbda9274abf9bc5ff94e6f7276b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210503214348364.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">元素的6层原型链</h4>
<p>我们获取到的元素是一个对象，所以需要搞清楚它的原型。</p>
<p>console.dir(div1)看原型链——</p>
<h5 data-id="heading-13">第一层原型</h5>
<p><code>HTMLDivElement.prototype</code>，这里面是所有div共有的属性。</p>
<h5 data-id="heading-14">第二层原型</h5>
<p><code>HTMLElement.prototype</code>，这里面是所有HTML标签共有的属性。</p>
<h5 data-id="heading-15">第三层原型</h5>
<p><code>Element.prototype</code>，这里面是所有XML、HTML标签的共有属性（浏览器不止展示HTML）</p>
<h5 data-id="heading-16">第四层原型</h5>
<p><code>Node.prototype</code>，这里面是所有节点的共有属性，节点包括XML标签文本注释、HTML标签文本注释等等。</p>
<h5 data-id="heading-17">第五层原型</h5>
<p><code>EventTarget.prototype</code>，里面最重要的函数属性是<code>addEvenListener</code></p>
<h5 data-id="heading-18">第六层原型</h5>
<p><code>Object.prototype</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f29b77743e9e496196c4c00f69c90fa5~tplv-k3u1fbpfcp-zoom-1.image" alt="div 原型链" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">节点</h3>
<h4 data-id="heading-20">节点和元素的区别</h4>
<p>Node？Element？</p>
<p><strong>节点Node包括以下几种，其中就包括Element</strong></p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Node/nodeType" target="_blank" rel="nofollow noopener noreferrer">MDN有完整描述</a>，<code>x.nodeType</code>得到一个数字。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90738acdfb784c1e90503906c645ce2b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210503220502942.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-21">节点的增删改查</h4>
<h5 data-id="heading-22">增</h5>
<ul>
<li>
<p>创建一个标签节点</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> div1 = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'style'</span>)
<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>)
<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'li'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>创建一个文本节点</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">text1 = <span class="hljs-built_in">document</span>.createTextnode(<span class="hljs-string">'你好'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>标签里面插入文本</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">div1.appendChild(text1)
div1.innerText=<span class="hljs-string">'你好'</span>
或
div1.textContent=<span class="hljs-string">'你好'</span>
<span class="hljs-comment">//不能用 div1.appenChild('你好')</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>插入页面中</p>
<p>创建的标签默认处于JS线程中，必须把它插到head后者body里面，它才会生效。</p>
<p><code>document.body.appendChild(div)</code></p>
<p>或者</p>
<p><code>已在页面中的元素.appendChild(div)</code></p>
</li>
</ul>
<blockquote>
<p>appendChild题目</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">页面中有 div#test1 和 div#test2
<span class="hljs-keyword">let</span> div = <span class="hljs-built_in">document</span>.createElemnt(<span class="hljs-string">'div'</span>)
test1.appendChild(div)
test2.appendChild(div)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请问最终div出现在哪里？</p>
<p>=> test2 里面，一个元素不能同时出现在两个地方，除非复制一份。</p>
</blockquote>
<h5 data-id="heading-23">删</h5>
<ul>
<li>
<p>两种方法</p>
<p>旧方法：<code>parentNode.removeChild(childNode)</code></p>
<p>新方法：<code>childNode.remove()</code>//ie不支持</p>
</li>
<li>
<p>思考</p>
<p>如果一个node被移出页面（DOM树），那么它还能再次返回页面中吗？</p>
<p>可以。</p>
<p>怎样删除node呢？</p>
<p>div = null</p>
</li>
</ul>
<h5 data-id="heading-24">改</h5>
<ul>
<li>
<p>改属性</p>
<ul>
<li>
<p>改标准属性</p>
<ul>
<li>
<p>改id</p>
<pre><code class="copyable">div1.id = 'div1'
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>改class</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//class是JS保留字，不能直接用div1.class</span>
div1.className = <span class="hljs-string">'blue'</span><span class="hljs-comment">//会全覆盖，想再添加只能 div1.className += ' red'</span>
div1.classList.add(<span class="hljs-string">'green'</span>)<span class="hljs-comment">//class = "blue red green"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>改style</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">div1.style = <span class="hljs-string">'width: 100px; color: blue;'</span>
div1.style.width = <span class="hljs-string">'200px'</span><span class="hljs-comment">//改style的一部分</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当改动类似于<code>background-color</code>这种有中划线的属性时，改写为<code>div1.style.backgroundColor</code>就可以执行。</p>
</li>
<li>
<p>改data-* 属性</p>
<pre><code class="copyable">div1.dataset.x='river'
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>读标准属性</p>
<pre><code class="copyable">div.classList / a.href
div.getAttribute('class') / a.getAttribute('href')
//两种方法都可以，但是值可能稍微不同
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>改时间处理函数</p>
<ul>
<li>
<p>div.onclick默认为null</p>
<p>默认点击div不会有任何事情发生</p>
<p>但是如果你把div.onclick改为一个函数fn，那么点击div的时候，浏览器就会调用这个函数</p>
<p>并且是这样调用的 <code>fn.call(div,event)</code></p>
<p>div会被当做this，event则包含了点击事件的所有信息，如坐标</p>
</li>
<li>
<p>div.addEventListener</p>
<p>是<code>div.onclick</code>的升级版</p>
</li>
</ul>
</li>
<li>
<p>改内容</p>
<ul>
<li>
<p>改文本内容</p>
<pre><code class="copyable">div.innerText = 'xxx'
div.textContent = 'xxx'
//两者几乎没有区别
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>改HTML内容</p>
<pre><code class="copyable">div.innerHTML = '<strong>重要内容</strong>'
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>改标签</p>
<pre><code class="copyable">div.innerHTML = ''//空字符串，先清空
div.appendChild(div2)//再改内容
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>改爸爸</p>
<pre><code class="copyable">newParent.appendChild(div)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h5 data-id="heading-25">查</h5>
<ul>
<li>
<p>查爸爸</p>
<pre><code class="copyable">node.parentNode
或
node.parentElement
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>查爷爷</p>
<pre><code class="copyable">node.parentNode.parentNode
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>查子代</p>
<pre><code class="copyable">node.childNodes
或者
node.children
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>第一个问题：</p>
<p>下面<code>console.log(test.childNodes.length)</code>打印结果为7，依次为text，li，text，li，text，li，text。</p>
<p>text是回车+空格</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2df8a97b248740b0ad3150572ca6689f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210503235941641.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因此下面这个打印结果就是3</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/079069e1bc3846e7b9174fc0ab2d9984~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504000158570.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>用children就可以避免这种情况，多用children！！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20b634053f154da9ac6f4f17d8bca475~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504000252183.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>第二个问题：</p>
<p>当子代变化时，两者也会实时变化吗？</p>
<p>会实时变化。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57df1b84488e429eb023afeb272641a5~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504000523276.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc636b6dfbb34cce80beaa2a7ed3f9a3~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504000544775.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而<code>document.querySelectorAll('li')</code>就不会实时变化</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c70707d47d44d27af1c934ae2f44c1c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504000733992.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
</li>
<li>
<p>查兄弟姐妹</p>
<pre><code class="copyable">node.parentNode.childNodes//还要排除自己
node.parentNode.children//还要排除自己
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是要做两件事情，第一件是上面的找到parent的孩子，第二件就是遍历这个数组并且排除自己。</p>
<p>操作示例：</p>
<p>div1的parent共有35个孩子</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2cdb1cba80c4dd39af2acb9ee831ebb~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504001320239.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过遍历并排除掉div1自己，得到自己的兄弟姐妹数组siblings</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a132761012fd4723a4a147f0a84a65c7~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504001425762.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>查看老大</p>
<pre><code class="copyable">node.firstChild
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>查看老幺</p>
<pre><code class="copyable">node.lastChild
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>查看上一个哥哥/姐姐</p>
<pre><code class="copyable">node.previousSibling//有可能会查看到文本节点
node.previousElementSibling
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>查看下一个弟弟/妹妹</p>
<pre><code class="copyable">node.nextSibling
node.nextElementSibling
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>遍历一个div里面的所有元素</p>
<pre><code class="copyable">travel = (node,fn) => &#123;
fn(node)
if(node.children)&#123;
for(let i = 0; i < node.children.length; i++)&#123;
travel(node.children[i],fn)
&#125;
&#125;
&#125;
travel(div1,(node) => console.log(node))
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-26">DOM 操作是跨线程的</h2>
<p>浏览器功能分为渲染引擎和JS引擎，渲染引擎用来渲染HTML和CSS，JS引擎来操作JS。</p>
<h3 data-id="heading-27">跨线程操作</h3>
<h4 data-id="heading-28">各线程各司其职</h4>
<p>JS引擎不能操作页面，只能操作JS</p>
<p>渲染引擎不能操作JS，只能操作页面</p>
<p>那<code>document.body.appendChild(div1)</code>这句话是如何改变页面的呢？</p>
<h4 data-id="heading-29">跨线程通信</h4>
<p>当浏览器发现JS在body里面加了个<code>div1</code>对象</p>
<p>浏览器就会通知渲染引擎在页面里也新增一个<code>div</code>元素</p>
<p>新增的<code>div</code>元素所有属性都照抄<code>div1</code>对象</p>
<p>注意：一个是对象，一个是元素。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71eb09c30b874b9992d53916be2715f2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504002943572.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-30">插入新标签的完整过程</h3>
<h4 data-id="heading-31">在div1放入页面之前</h4>
<p>对div1所有的操作都属于JS线程内的操作</p>
<h4 data-id="heading-32">把div1放入页面之时</h4>
<p>浏览器发现JS的意图，就会通知渲染线程在页面中渲染div1对应的元素</p>
<h4 data-id="heading-33">把div1放入页面之后</h4>
<p>你对div1的操作都<strong>有可能</strong>会触发重新渲染</p>
<p><code>div1.id='newId'</code>可能会重新渲染，也可能不会</p>
<p><code>div1.title='new'</code><strong>可能会重新渲染</strong>，也可能不会</p>
<p>如果连续对div1多次操作，浏览器可能会<strong>合并成一次操作</strong>，也可能不会，就比如下面这个例子，如果不加<code>test.clientWidth</code>，那JS就会默认合并导致动画无法显示。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09ea5eb86d2d40d2a06323aceadf2fa9~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504003554460.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-34">属性同步</h3>
<h4 data-id="heading-35">标准属性</h4>
<p>对div1的标准属性修改，会被浏览器同步到页面中</p>
<p>比如id、className、title等</p>
<h4 data-id="heading-36">data-* 属性</h4>
<p>同上</p>
<h4 data-id="heading-37">非标准属性</h4>
<p>对非标准属性的修改，则只会停留在JS线程中，不会同步到页面里</p>
<p>比如x属性，<a href="http://js.jirengu.com/meviw/2/edit?html,js,output" target="_blank" rel="nofollow noopener noreferrer">示例代码</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40a8e9e8f5cd49c786e036d52f0a4949~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504004540231.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-38">启示</h4>
<p>如果你有自定义属性，又想被同步到页面中，请使用<code>data-</code>作为前缀</p>
<h3 data-id="heading-39">Property V.S. Attribute</h3>
<h4 data-id="heading-40">property 属性</h4>
<p>JS线程中div1的所有属性，叫做div1的property</p>
<h4 data-id="heading-41">attribute属性</h4>
<p>渲染引擎中div1对应标签的属性，叫做attribute</p>
<h4 data-id="heading-42">区别</h4>
<p>大部分时候，同名的property 和 attribute 值相等</p>
<p>但如果不是标准属性，那么它俩只会在一开始时相等</p>
<p>但注意attribute只支持字符串</p>
<p>而property支持字符串、布尔等类型</p>
<h2 data-id="heading-43">什么叫封装</h2>
<h3 data-id="heading-44">举例</h3>
<p>电脑笔记本就是CPU、内存、硬盘、主板、显卡的封装，用户只需要接触显示器、键盘、鼠标、触控板等设备，即可操作复杂的计算机。</p>
<h3 data-id="heading-45">接口</h3>
<p>被封装的东西需要暴露一些功能给外部，这些功能就是接口，如USB接口、HDMI接口。</p>
<p>设备只要支持这些接口，即可与被封装的东西通讯，比如键盘、鼠标支持USB接口，显示器支持HDMI接口。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d970fa955dc544a1893c56ecdd46e051~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504014710620.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48db62a3bbbb4cd980691371d811bf4d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210504014719342.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-46">术语</h3>
<h4 data-id="heading-47">库</h4>
<p>我们把提供给其他人用的工具代码叫做库，比如JQuery、Underscore</p>
<h4 data-id="heading-48">API</h4>
<p>库暴露出来的函数或属性就叫做API（应用编程接口）</p>
<h4 data-id="heading-49">框架</h4>
<p>当库变得很大，并且需要学习才能看懂，那么这个库就是框架，比如Vue 、React</p>
<h2 data-id="heading-50">DOM封装</h2>
<p><a href="https://juejin.cn/post/undefined">源码</a></p></div>  
</div>
            