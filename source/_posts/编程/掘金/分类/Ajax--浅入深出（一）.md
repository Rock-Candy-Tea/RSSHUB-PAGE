
---
title: 'Ajax--浅入深出（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/082f2d01f538442886bc185576f59c7c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 02:47:12 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/082f2d01f538442886bc185576f59c7c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/post/7001059799659970574/" target="_blank" title="https://juejin.cn/post/7001059799659970574/"> Ajax--浅入深出（二）</a></h2>
<h1 data-id="heading-1">1. Ajax概述</h1>
<h2 data-id="heading-2">1.1 AJAX 简介</h2>
<ul>
<li>AJAX 全称为Asynchronous JavaScript And XML，就是异步的JS 和XML</li>
<li>通过AJAX 可以在浏览器中向服务器发送异步请求，最大的优势：无刷新获取数据</li>
<li>AJAX 不是新的编程语言，而是一种将现有的标准组合在一起使用的新方式</li>
</ul>
<h2 data-id="heading-3">1.2 XML 简介</h2>
<ul>
<li>XML 可扩展标记语言。</li>
<li>XML 被设计用来传输和存储数据,HTML用来展示数据。</li>
<li>XML 和HTML 类似，不同的是HTML 中都是预定义标签，而XML 中没有预定义标签，</li>
<li>全都是自定义标签，用来表示一些数据。</li>
</ul>
<p>比如说我有一个学生数据：</p>
<pre><code class="copyable">name = “孙悟空” ; age = 18 ; gender = “男” ;

用XML 表示：
<student>
<name>孙悟空</name>
<age>18</age>
<gender>男</gender>
</student>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在已经被JSON 取代了。</p>
<pre><code class="copyable">&#123;"name":"孙悟空","age":18,"gender":"男"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">1.3 AJAX 的特点</h2>
<h3 data-id="heading-5">1.3.1 AJAX 的优点</h3>
<ol>
<li>可以<strong>无需刷新页面</strong>而与服务器端进行通信</li>
<li>允许你根据用户<strong>事件</strong>来更新部分页面内容</li>
</ol>
<h3 data-id="heading-6">1.3.2 AJAX 的缺点</h3>
<ol>
<li>没有浏览历史，不能回退</li>
<li>存在跨域问题(同源)</li>
<li>SEO 不友好</li>
</ol>
<h1 data-id="heading-7">2. HTTP相关问题</h1>
<h2 data-id="heading-8">2.1  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTTP%2FOverview" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Overview" ref="nofollow noopener noreferrer">MDN文档</a></h2>
<p><strong><a href="https://link.juejin.cn/?target=http%3A%2F%2Fnote.youdao.com%2Fnoteshare%3Fid%3D26d82e1a604a4094f066d6bb6a415bcf%26sub%3DBC4C9A8EF282472AA54752ACAD5891D0" target="_blank" rel="nofollow noopener noreferrer" title="http://note.youdao.com/noteshare?id=26d82e1a604a4094f066d6bb6a415bcf&sub=BC4C9A8EF282472AA54752ACAD5891D0" ref="nofollow noopener noreferrer">请求与响应笔记</a></strong></p>
<h2 data-id="heading-9">2.2 HTTP 请求交互的基本过程</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/082f2d01f538442886bc185576f59c7c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>前后应用从浏览器端向服务器发送HTTP 请求(请求报文)</li>
<li>后台服务器接收到请求后, 调度服务器应用处理请求, 向浏览器端返回HTTP响应(响应报文)</li>
<li>浏览器端接收到响应, 解析显示响应体/调用监视回调</li>
</ol>
<h2 data-id="heading-10">2.3 HTTP 请求报文</h2>
<h3 data-id="heading-11">1. 请求行</h3>
<pre><code class="copyable">method url
GET /product_detail?id=2
POST /login
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">2. 多个请求头</h3>
<pre><code class="copyable">Host: www.baidu.com
Cookie: BAIDUID=AD3B0FA706E; BIDUPSID=AD3B0FA706;
Content-Type: application/x-www-form-urlencoded 或者application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">3. 请求体</h3>
<pre><code class="hljs language-js copyable" lang="js">username=tom&pwd=<span class="hljs-number">123</span>
&#123;<span class="hljs-string">"username"</span>: <span class="hljs-string">"tom"</span>, <span class="hljs-string">"pwd"</span>: <span class="hljs-number">123</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">2.4 HTTP 响应报文</h2>
<h3 data-id="heading-15">1.响应状态行: status statusText</h3>
<h3 data-id="heading-16">2.多个响应头</h3>
<pre><code class="hljs language-js copyable" lang="js">Content-Type: text/html;charset=utf-<span class="hljs-number">8</span>
<span class="hljs-built_in">Set</span>-Cookie: BD_CK_SAM=<span class="hljs-number">1</span>;path=/
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">3.响应体</h3>
<pre><code class="hljs language-js copyable" lang="js">html 文本/json 文本/js/css/图片...
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">2.5 post 请求体参数格式</h2>
<p>1.<code>Content-Type: application/x-www-form-urlencoded;charset=utf-8</code><br>
用于键值对参数，参数的键值用=连接, 参数之间用&连接<br>
例如: name=%E5%B0%8F%E6%98%8E&age=12<br>
2.<code>Content-Type: application/json;charset=utf-8</code><br>
用于 json 字符串参数<br>
例如: &#123;"name": "%E5%B0%8F%E6%98%8E", "age": 12&#125;<br>
3.<code>Content-Type: multipart/form-data</code><br>
用于文件上传请求</p>
<h2 data-id="heading-19">2.6 常见的响应状态码</h2>
<ul>
<li>200 OK 请求成功。一般用于GET 与POST 请求</li>
<li>201 Created 已创建。成功请求并创建了新的资源</li>
<li>401 Unauthorized 未授权/请求要求用户的身份认证</li>
<li>404 Not Found 服务器无法根据客户端的请求找到资源</li>
<li>500 Internal Server Error 服务器内部错误，无法完成请求</li>
</ul>
<h2 data-id="heading-20">2.7 不同类型的请求及其作用</h2>
<ul>
<li>GET: 从服务器端读取数据（查）</li>
<li>POST: 向服务器端添加新数据 （增）</li>
<li>PUT: 更新服务器端已经数据 （改）</li>
<li>DELETE: 删除服务器端数据 （删）</li>
</ul>
<h2 data-id="heading-21">2.8 API 的分类</h2>
<p><strong>REST API: restful （Representational State Transfer (资源)表现层状态转化）</strong></p>
<ol>
<li>发送请求进行CRUD 哪个操作由请求方式来决定</li>
<li>同一个请求路径可以进行多个操作</li>
<li>请求方式会用到GET/POST/PUT/DELETE</li>
</ol>
<p><strong>非REST API: restless</strong></p>
<ol>
<li>请求方式不决定请求的CRUD 操作</li>
<li>一个请求路径只对应一个操作</li>
<li>一般只有GET/POST</li>
</ol>
<h2 data-id="heading-22">2.9 区别 一般http请求 与 ajax请求</h2>
<ul>
<li>ajax请求 是一种特别的 http请求</li>
<li>对服务器端来说, 没有任何区别, 区别在浏览器端</li>
<li>浏览器端发请求: 只有XHR 或fetch 发出的才是ajax 请求, 其它所有的都是非ajax 请求</li>
<li>浏览器端接收到响应</li>
</ul>
<p>(1) 一般请求: 浏览器一般会直接显示响应体数据, 也就是我们常说的刷新/跳转页面<br>
(2) ajax请求: 浏览器不会对界面进行任何更新操作, 只是调用监视的回调函数并传入响应相关数据</p>
<h1 data-id="heading-23">3. 原生AJAX 的基本使用 XHR</h1>
<h2 data-id="heading-24">3.0 准备工作</h2>
<h3 data-id="heading-25">3.0.1 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.cn/" ref="nofollow noopener noreferrer">安装node.js</a></h3>
<h3 data-id="heading-26">3.0.2 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.expressjs.com.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.expressjs.com.cn/" ref="nofollow noopener noreferrer">安装express（服务端框架）</a></h3>
<h4 data-id="heading-27">1.初始化环境</h4>
<pre><code class="hljs language-js copyable" lang="js">npm init --yes
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">2.下载express包</h4>
<pre><code class="copyable">npm install express --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">3.编写js代码</h4>
<pre><code class="copyable">// 1. 引入express
const express = require('express');

// 2. 创建应用对象
const app = express();

// 3. 创建路由规则
// request 是对请求报文的封装
// response 是对响应报文的封装
app.get('/', (request, response) => &#123;
  //  设置响应
  response.send("Hello Express");
&#125;);

// 4. 监听端口，启动服务
app.listen(8000, () => &#123;
  console.log("服务已经启动, 8000 端口监听中...");
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">4.运行js程序</h4>
<pre><code class="hljs language-js copyable" lang="js">node express.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78da0572740b415bb7b598adb4a84faf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-31">5.打开网页输入<a href="https://link.juejin.cn/?target=http%3A%2F%2F127.0.0.1%3A8000%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://127.0.0.1:8000/" ref="nofollow noopener noreferrer">http://127.0.0.1:8000/</a> 显示页面</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/522720c9aaf44ff29edeb2b2a255d538~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-32">6.调试程序可以查看请求和响应</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/400425a1585b4aa3b39502dca59859ae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-33">3.0.3 安装node-dev自动重启工具</h3>
<p>文件内容有修改自动重新启动服务</p>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fnode-dev" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/node-dev" ref="nofollow noopener noreferrer">node-dev</a></strong></p>
<h4 data-id="heading-34">1.安装</h4>
<pre><code class="copyable">npm i node-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">2.启动服务</h4>
<pre><code class="copyable">node-dev server.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-36">3.1 理解</h2>
<ul>
<li>使用XMLHttpRequest (XHR)对象可以与服务器交互, 也就是发送ajax 请求</li>
<li>前端可以获取到数据，而无需让整个的页面刷新。</li>
<li>这使得Web 页面可以只更新页面的局部，而不影响用户的操作。</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest" ref="nofollow noopener noreferrer">XMLHttpRequest MDN</a><br>
<strong>XMLHttpRequest</strong>，AJAX 的所有操作都是通过该对象进行的</p>
<h2 data-id="heading-37">3.2 核心对象使用步骤</h2>
<h3 data-id="heading-38">3.2.1 创建XMLHttpRequest 对象</h3>
<p><code>var xhr = new XMLHttpRequest();</code></p>
<h3 data-id="heading-39">3.2.2 设置请求信息（请求方法和url）</h3>
<pre><code class="copyable">// 请求方式
xhr.open(method, url);
//可以设置请求头，一般不设置
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40">3.2.3 发送请求</h3>
<p><code>xhr.send(body) //get请求不传 body 参数，只有post请求使用</code></p>
<h3 data-id="heading-41">3.2.4 接收响应（事件绑定，处理服务端返回的结果）</h3>
<pre><code class="copyable">//xhr.responseXML 接收 xml格式 的响应数据
//xhr.responseText 接收 文本格式 的响应数据
    xhr.onreadystatechange = function () &#123;
                //判断 (服务端返回了所有的结果)
                if (xhr.readyState === 4) &#123;
                    //判断响应状态码 200  404  403 401 500
                    // 2xx 成功
                    if (xhr.status >= 200 && xhr.status < 300) &#123;
                        //处理结果  行 头 空行 体
                        //响应 
                        // console.log(xhr.status);//状态码
                        // console.log(xhr.statusText);//状态字符串
                        // console.log(xhr.getAllResponseHeaders());//所有响应头
                        // console.log(xhr.response);//响应体
                        //设置 result 的文本
                        result.innerHTML = xhr.response;
                    &#125; else &#123;

                    &#125;
                &#125;
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-42">3.3 使用案例</h2>
<h3 data-id="heading-43">3.3.1 GET 请求</h3>
<p>点击返回响应信息<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feb9ff46d7a24175946abdf0443896cb~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
创建两个文件，浏览器端使用的html文件和服务器端使用的js文件<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ea50994d2ad4bd58379f59f6fa638e1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-44">服务器端 server.js</h4>
<pre><code class="copyable">// 1. 引入express
const express = require('express');

// 2. 创建应用对象
const app = express();

// 3. 创建路由规则
app.get('/server', (request, response) => &#123;
  // 设置响应头 设置允许跨域
  response.setHeader('Access-Control-Allow-Origin', '*');
  // 设置响应体
  response.send("Hello Ajax");
&#125;);

// 4. 监听服务
app.listen(8000, () => &#123;
  console.log("服务已经启动, 8000 端口监听中...");
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-45">启动服务</h4>
<pre><code class="hljs language-js copyable" lang="js">node server.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/235c1270e7924da09f7621c7ec7dd5f2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-46">前端页面 html</h4>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AJAX GET 请求</title>
    <style>
        #result &#123;
            width: 200px;
            height: 100px;
            border: solid 1px #90b;
        &#125;
    </style>
</head>
<body>
    <button>点击发送请求</button>
    <div id="result"></div>

    <script>
        //获取button元素
        const btn = document.getElementsByTagName('button')[0];
        const result = document.getElementById("result");
        //绑定事件
        btn.onclick = function () &#123;
            //1. 创建对象
            const xhr = new XMLHttpRequest();
            //2. 初始化 设置请求方法和 url
            xhr.open('GET', 'http://127.0.0.1:8000/server?a=100&b=200&c=300');
            // 发送参数：在url地址后面加？，然后用&分隔不同参数
            //3. 发送
            xhr.send();
            //4. 事件绑定 处理服务端返回的结果
            // on  when 当....时候
            // readystate 是 xhr 对象中的属性, 表示状态 0 1 2 3 4
            // change  改变
            xhr.onreadystatechange = function () &#123;
                //判断 (服务端返回了所有的结果)
                if (xhr.readyState === 4) &#123;
                    //判断响应状态码 200  404  403 401 500
                    // 2xx 成功
                    if (xhr.status >= 200 && xhr.status < 300) &#123;
                        //处理结果  行 头 空行 体
                        //响应 
                        // console.log(xhr.status);//状态码
                        // console.log(xhr.statusText);//状态字符串
                        // console.log(xhr.getAllResponseHeaders());//所有响应头
                        // console.log(xhr.response);//响应体
                        //设置 result 的文本
                        result.innerHTML = xhr.response;
                    &#125; else &#123;

                    &#125;
                &#125;
            &#125;
        &#125;
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-47">GET 请求设置请求参数</h4>
<p><strong>设置url参数</strong></p>
<pre><code class="copyable">xhr.open('GET', 'http://127.0.0.1:8000/server?a=100&b=200&c=300');
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12e1c8951ac84192a7184d956e1430fc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-48">3.3.2 POST请求</h3>
<p>鼠标放到div中，发post请求，将响应体放在div中呈现</p>
<h4 data-id="heading-49">server.js添加post</h4>
<p>在之前的server.js中加入下方代码</p>
<pre><code class="hljs language-js copyable" lang="js">app.post(<span class="hljs-string">'/server'</span>, <span class="hljs-function">(<span class="hljs-params">request, response</span>) =></span> &#123;
  <span class="hljs-comment">// 设置响应头, 设置允许跨域</span>
  response.setHeader(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>);
  <span class="hljs-comment">// 设置响应体</span>
  response.send(<span class="hljs-string">"Hello Ajax POST"</span>);
&#125;);
<span class="hljs-comment">//可以接收任意类型的请求 </span>
app.all(<span class="hljs-string">'/server'</span>, <span class="hljs-function">(<span class="hljs-params">request, response</span>) =></span> &#123;
    <span class="hljs-comment">//设置响应头  设置允许跨域</span>
    response.setHeader(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>);
    <span class="hljs-comment">//响应头，可以自定义请求头</span>
    response.setHeader(<span class="hljs-string">'Access-Control-Allow-Headers'</span>, <span class="hljs-string">'*'</span>);
    <span class="hljs-comment">//设置响应体</span>
    response.send(<span class="hljs-string">'HELLO AJAX POST'</span>);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-50">post.html</h4>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AJAX POST 请求</title>
    <style>
        #result&#123;
            width:200px;
            height:100px;
            border:solid 1px #903;
        &#125;
    </style>
</head>
<body>
    <div id="result"></div>
    <script>
        //获取元素对象
        const result = document.getElementById("result");
        //绑定事件
        result.addEventListener("mouseover", function()&#123;
            //1. 创建对象
            const xhr = new XMLHttpRequest();
            //2. 初始化 设置类型与 URL
            xhr.open('POST', 'http://127.0.0.1:8000/server');
            //设置请求头
            xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
            xhr.setRequestHeader('name','zgc');
            //3. 发送
            xhr.send('a=100&b=200&c=300');
            // xhr.send('a:100&b:200&c:300');
            // xhr.send('1233211234567');
            
            //4. 事件绑定
            xhr.onreadystatechange = function()&#123;
                //判断
                if(xhr.readyState === 4)&#123;
                    if(xhr.status >= 200 && xhr.status < 300)&#123;
                        //处理服务端返回的结果
                        result.innerHTML = xhr.response;
                    &#125;
                &#125;
            &#125;
        &#125;);
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0603b571d19b4898adfeca1f25f7edfd~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-51">3.3.3设置请求头信息</h3>
<p>设置请求头信息在open（）之后，send（）之前，可以看上方post代码</p>
<pre><code class="copyable">// 设置请求体内容的类型
xhr.setRequesHeader('Content-Type','application/x-www-from-urlencoded');
// 自定义头信息
xhr.setRequesHeader('name', 'zgc');
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>server.js中设置响应头允许自定义请求头 post改成all</strong></p>
<pre><code class="hljs language-js copyable" lang="js">response.setHeader(<span class="hljs-string">'Access-Control-Allow-Header'</span>,<span class="hljs-string">'*'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5e2690a85cc41be97e070306d0a750a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-52">3.4 json数据请求</h2>
<p><strong>server.js</strong>
将下方代码加入到之前的server.js中</p>
<pre><code class="hljs language-js copyable" lang="js">app.all(<span class="hljs-string">'/json-server'</span>, <span class="hljs-function">(<span class="hljs-params">request, response</span>) =></span> &#123;
  <span class="hljs-comment">// 设置响应头, 设置允许跨域</span>
  response.setHeader(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>);
  <span class="hljs-comment">// 设置响应头, 设置允许自定义头信息</span>
  response.setHeader(<span class="hljs-string">'Access-Control-Allow-Headers'</span>, <span class="hljs-string">'*'</span>);
  <span class="hljs-comment">// 响应一个数据</span>
  <span class="hljs-keyword">const</span> data = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'atguigu'</span>
  &#125;;
  <span class="hljs-comment">// 对 对象 进行 字符串 转换</span>
  <span class="hljs-keyword">let</span> str = <span class="hljs-built_in">JSON</span>.stringify(data)
  <span class="hljs-comment">// 设置响应体 </span>
  response.send(str);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>index.html</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JSON响应</title>
    <style>
        #result&#123;
            width:200px;
            height:100px;
            border:solid 1px #89b;
        &#125;
    </style>
</head>
<body>
    <div id="result"></div>
    <script>
        const result = document.getElementById('result');
        //绑定键盘按下事件
        window.onkeydown = function()&#123;
            //发送请求
            const xhr = new XMLHttpRequest();
            
            //设置响应体数据的类型，自动转换成json对象
            xhr.responseType = 'json';
          
          //初始化
            xhr.open('GET','http://127.0.0.1:8000/json-server');
            //发送
            xhr.send();
            //事件绑定
            xhr.onreadystatechange = function()&#123;
                if(xhr.readyState === 4)&#123;
                    if(xhr.status >= 200 && xhr.status < 300)&#123;
                        
                        // console.log(xhr.response);
                        // result.innerHTML = xhr.response;
                        
                        // 1. 手动对数据转化
                        // let data = JSON.parse(xhr.response);
                        // console.log(data);
                        // result.innerHTML = data.name;
                        
                        // 2. 自动转换
                        console.log(xhr.response);
                        result.innerHTML = xhr.response.name;
                    &#125;
                &#125;
            &#125;
        &#125;
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-53">3.5 请求超时与网络异常</h2>
<p><strong>server.js</strong></p>
<p>将下方代码加入到之前的server.js中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//延时响应</span>
app.all(<span class="hljs-string">'/delay'</span>, <span class="hljs-function">(<span class="hljs-params">request, response</span>) =></span> &#123;
    <span class="hljs-comment">//设置响应头  设置允许跨域</span>
    response.setHeader(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>);
    response.setHeader(<span class="hljs-string">'Access-Control-Allow-Headers'</span>, <span class="hljs-string">'*'</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">//设置响应体</span>
        response.send(<span class="hljs-string">'延时响应'</span>);
    &#125;, <span class="hljs-number">3000</span>)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>请求超时与网络异常</title>
    <style>
        #result&#123;
            width:200px;
            height:100px;
            border:solid 1px #90b;
        &#125;
    </style>
</head>
<body>
    <button>点击发送请求</button>
    <div id="result"></div>
    <script>
        const btn = document.getElementsByTagName('button')[0];
        const result = document.querySelector('#result');

        btn.addEventListener('click', function()&#123;
            const xhr = new XMLHttpRequest();
            //超时设置 2s 设置
            xhr.timeout = 2000;
            //超时回调
            xhr.ontimeout = function()&#123;
                alert("网络异常, 请稍后重试!!");
            &#125;
            //网络异常回调
            xhr.onerror = function()&#123;
                alert("你的网络似乎出了一些问题!");
            &#125;

            xhr.open("GET",'http://127.0.0.1:8000/delay');
            xhr.send();
            xhr.onreadystatechange = function()&#123;
                if(xhr.readyState === 4)&#123;
                    if(xhr.status >= 200 && xhr.status< 300)&#123;
                        result.innerHTML = xhr.response;
                    &#125;
                &#125;
            &#125;
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-54">3.6 取消请求</h2>
<p><code>// 手动取消  xhr.abort()</code></p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>取消请求</title>
</head>
<body>
    <button>点击发送</button>
    <button>点击取消</button>
    <script>
        //获取元素对象
        const btns = document.querySelectorAll('button');
        let x = null;

        btns[0].onclick = function()&#123;
            x = new XMLHttpRequest();
            x.open("GET",'http://127.0.0.1:8000/delay');
            x.send();
        &#125;

        // abort
        btns[1].onclick = function()&#123;
            x.abort();
        &#125;
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-55">3.7 请求重复发送问题</h2>
<p>设置变量判断是否重复发送请求</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>重复请求问题</title>
</head>

<body>
    <button>点击发送</button>
    <script>
        //获取元素对象
        const btns = document.querySelectorAll('button');
        let x = null;
        //标识变量
        let isSending = false; // 是否正在发送AJAX请求

        btns[0].onclick = function () &#123;
            //判断标识变量
            if (isSending) x.abort();// 如果正在发送, 则取消该请求, 创建一个新的请求
            x = new XMLHttpRequest();
            //修改 标识变量的值
            isSending = true;
            x.open("GET", 'http://127.0.0.1:8000/delay');
            x.send();
            x.onreadystatechange = function () &#123;
                if (x.readyState === 4) &#123;
                    //修改标识变量
                    isSending = false;
                    if (x.status >= 200 && x.status < 300) &#123;
                        console.log(x.response);
                    &#125;
                &#125;
            &#125;
        &#125;

    </script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-56">3.8 解决 IE 缓存问题</h2>
<p>问题：在一些浏览器中(IE),由于缓存机制的存在，ajax 只会发送的第一次请求，剩余多次请求不会在发送给浏览器而是直接加载缓存中的数据。
解决方式：浏览器的缓存是根据url 地址来记录的，所以我们只需要修改url 地址即可避免缓存问题</p>
<p><strong>server.js</strong></p>
<p>将下方代码加入到之前的server.js中</p>
<pre><code class="copyable">//针对 IE 缓存
app.get('/ie', (request, response) => &#123;
    //设置响应头  设置允许跨域
    response.setHeader('Access-Control-Allow-Origin', '*');
    //设置响应体
    response.send('HELLO IE - 25');
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>index.html</strong></p>
<p>在xhr.open中加上时间戳参数</p>
<p><code> xhr.open("GET",'http://127.0.0.1:8000/ie?t='+Date.now());</code></p>
<h2 data-id="heading-57">3.9 AJAX 请求状态</h2>
<p>xhr.readyState 可以用来查看请求当前的状态 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest%2FreadyState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest/readyState" ref="nofollow noopener noreferrer">MDN</a></strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43813c3ef3cd475993fba1dd4abec4cf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>0: 表示XMLHttpRequest 实例已经生成，但是open()方法还没有被调用</li>
<li>1: 表示send()方法还没有被调用，仍然可以使用setRequestHeader()，设定HTTP请求的头信息</li>
<li>2: 表示send()方法已经执行，并且头信息和状态码已经收到</li>
<li>3: 表示正在接收服务器传来的body 部分的数据</li>
<li>4: 表示服务器数据已经完全接收，或者本次接收已经失败了</li>
</ul>
<h2 data-id="heading-58">3.10 API总结</h2>
<ul>
<li>XMLHttpRequest()：创建 XHR 对象的构造函数</li>
<li>status：响应状态码值，如 200、404</li>
<li>statusText：响应状态文本，如 ’ok‘、‘not found’</li>
<li>readyState：标识请求状态的只读属性 0-1-2-3-4</li>
<li>onreadystatechange：绑定 readyState 改变的监听</li>
<li>responseType：指定响应数据类型，如果是 ‘json’，得到响应后自动解析响应</li>
<li>response：响应体数据，类型取决于 responseType 的指定</li>
<li>timeout：指定请求超时时间，默认为 0 代表没有限制</li>
<li>ontimeout：绑定超时的监听</li>
<li>onerror：绑定请求网络错误的监听</li>
<li>open()：初始化一个请求，参数为：(method, url[, async])</li>
<li>send(data)：发送请求</li>
<li>abort()：中断请求 （发出到返回之间）</li>
<li>getResponseHeader(name)：获取指定名称的响应头值</li>
<li>getAllResponseHeaders()：获取所有响应头组成的字符串</li>
<li>setRequestHeader(name, value)：设置请求头</li>
</ul></div>  
</div>
            