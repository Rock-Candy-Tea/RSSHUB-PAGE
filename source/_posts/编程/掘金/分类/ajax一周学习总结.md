
---
title: 'ajax一周学习总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/caaf2844ed1f4eed9d8a64727c1cd65e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 00:21:16 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/caaf2844ed1f4eed9d8a64727c1cd65e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>学习的视频还是在B站中黑马前端进阶教学。</p>
<h2 data-id="heading-0">一.初始Ajax</h2>
<p>1.什么是Ajax？
Ajax的全称是Asynchronous JavaScript And XML （异步 JavaScript 和 XML）。通俗的：理解在网页中利用XMLHttpRequest 和对象服务器进行数据交换的方式，就是Ajax。</p>
<p>2.了解jQuery中的Ajax。
jQuery 中发球Ajax请求最常用的三个方法：</p>
<p>$.get()  从服务器中获取数据</p>
<p>$.post() 从服务器中提交数据</p>
<p>$.ajax() 从服务器中获取或提交数据。</p>
<p>$.get()函数用法：</p>
<p>$.get('url',[data],[callback])  其中url 请求的地址 data 请求服务器的数据，callback 回调函数。
发起get不带参数的请求代码实现：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/caaf2844ed1f4eed9d8a64727c1cd65e~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>浏览器中实现：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8548d12705d440869368b68cefdd56b7~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发起get带参数的请求代码实现：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/428b644027bf4bc891fdb5f402ea0f84~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>浏览器中实现：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fe0182a969948f49136eca837335c67~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>$.post()函数用法：</p>
<p>$.get('url',[data],[callback])  其中url 提交数据的地址 data 提交服务器的数据，callback 回调函数。
发起post请求代码实现：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/894bdd7639ea4b2db3d9bc3ae88de028~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>浏览器中实现：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7ec43fd8b544cfe9ea7089615e5ded8~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>$.ajax()函数用法：</p>
<p>$.ajax(&#123;</p>
<pre><code class="copyable">type:'', // 请求得方式，GET 或者 POST
url：'', // 请求的url地址
data&#123;&#125;, // 这次请求携带的参数
success:function(res)&#123; // 请求成功后的回调函数
console.log(res)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;)</p>
<p>代码实现：
使用$.ajax()函数发起get请求：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e131329334745339ea1b9f79b34d6c6~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用$.ajax()函数发起post请求:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6e40de8eaa942ffb03117f467bed5ee~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后做了一个图书管理的案例：
CSS样式使用了bootstrap，JS使用了jQuery。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad5d3f63e95a4ae5990001e33b09b261~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体代码：
HTML和css</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/641f4d690f4d40fdb44f924d8e5daf59~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862863f30901485d911ad1d1b54c23bf~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>JavaScript部分：</p>
<p>获取图书列表代码
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f295432f41c445baac8169b95c2dc470~tplv-k3u1fbpfcp-watermark.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击删除图书代码：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9653d1189d7f4d54a3852bf60dcd99e3~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击添加图书代码:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11ce5527a61f4948906be3f7e1d65ced~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">总结</h2>
<p>跟着视频学习感觉并不是很难，代码还是要多加练习才会熟悉，把之前学习的html，css JavaScript 运用了一遍也顺带复习了。打代码最难的就是不够细心，经常会因为敲错字符，字母出现报错。这一段的ajax入门还算挺容易的，继续加油学习。</p></div>  
</div>
            