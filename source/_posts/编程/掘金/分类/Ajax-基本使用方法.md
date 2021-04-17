
---
title: 'Ajax-基本使用方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7bc19aeb5d644449ed4e76035f3edc9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 00:37:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7bc19aeb5d644449ed4e76035f3edc9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>使用Ajax的五个步骤：</strong></p>
<ol>
<li>创建一个异步对象</li>
<li>设置请求方式和请求地址</li>
<li>发送请求</li>
<li>监听状态的变化</li>
<li>处理返回的结果</li>
</ol>
<h1 data-id="heading-0">1. 创建一个异步对象XMLHttpRequest</h1>
<p>IE5和IE6的创建方法：</p>
<pre><code class="copyable">var xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有现代浏览器（IE7+、Firefox、Chrome、Safari 以及 Opera）的创建方法:</p>
<pre><code class="copyable">var xmlhttp = new XMLHttpRequest;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那我们怎么处理浏览器兼容性问题呢？我们可以这样做：</p>
<pre><code class="copyable">var xmlhttp;
if (window.XMLHttpRequest)
  &#123;// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  &#125;
else
  &#123;// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">2. 设置请求方式和请求地址</h1>
<p>如需将请求发送到服务器，我们使用 XMLHttpRequest 对象的 open() 方法.</p>
<pre><code class="copyable">xmlhttp.open("GET","test1.txt",true);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">method：请求的类型；GET 或 POST
url：文件在服务器上的位置
async：true（异步）或 false（同步）
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3.发送请求</h1>
<pre><code class="copyable">     xmlhttp.send();
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">4. 监听状态的变化</h1>
<pre><code class="copyable">    xmlhttp.onreadystatechange = function (ev2) &#123;
       /*
       0: 请求未初始化
       1: 服务器连接已建立
       2: 请求已接收
       3: 请求处理中
       4: 请求已完成，且响应已就绪
       */
       if(xmlhttp.readyState === 4)&#123;
           // 判断是否请求成功
           // 状态码大于200小于300或等于304时才会请求成功
           if(xmlhttp.status >= 200 && xmlhttp.status < 300 ||xmlhttp.status === 304)&#123;
                5.处理返回的结果
               // console.log("接收到服务器返回的数据");
               success(xmlhttp);
               // 此处的sucess是封装Ajax函数里面的形参，后面的error也是如此。
           &#125;else&#123;
               // console.log("没有接收到服务器返回的数据");
               error(xmlhttp);
           &#125;
       &#125;
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">5.处理返回的结果</h1>
<p>处理方式在上一个步骤中已有
如果接收到数据则调用第一个函数，否则调用第二个函数。</p>
<h1 data-id="heading-5">6.浏览器兼容性问题</h1>
<h2 data-id="heading-6">6.1 Ajax缓存机制</h2>
<p>在IE浏览器中会出现此问题
在IE浏览器中，如果通过Ajax发送GET请求，那么IE浏览器认为同一个URL只有一个结果。</p>
<p><strong>解决办法：</strong>
每次请求的时候都给url一个不同的值
这个时候我们可以想到用<code>new Date().getTime()</code>方法获得一个值添加到url中。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7bc19aeb5d644449ed4e76035f3edc9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
改一下这里的url：
"text1.txt?t="+(new Date().getTime());</p>
<h2 data-id="heading-7">6.2 创建异步对象的不同</h2>
<pre><code class="copyable">var xmlhttp;
if (window.XMLHttpRequest)
  &#123;// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  &#125;
else
  &#123;// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">7.封装Ajax</h1>
<p>每次编写Ajax都会有5个步骤，因此这些代码是一样的，我们可以用一个函数把这些代码封装起来:</p>
<pre><code class="copyable">function obj2str(obj) &#123;
    obj = obj || &#123;&#125;; // 如果没有传参, 为了添加随机因子,必须自己创建一个对象
    obj.t = new Date().getTime();
    var res = [];
    for(var key in obj)&#123;
        // 在URL中是不可以出现中文的, 如果出现了中文需要转码
        // 可以调用encodeURIComponent方法
        // URL中只可以出现字母/数字/下划线/ASCII码
        res.push(encodeURIComponent(key)+"="+encodeURIComponent(obj[key])); // [userName=lnj, userPwd=123456];
    &#125;
    return res.join("&"); // userName=lnj&userPwd=123456
&#125;
function ajax(url, obj, timeout, success, error) &#123;
    // 0.将对象转换为字符串
    var str = obj2str(obj); // key=value&key=value;
    // 1.创建一个异步对象
    var xmlhttp, timer;
    if (window.XMLHttpRequest)
    &#123;// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    &#125;
    else
    &#123;// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    &#125;
    // 2.设置请求方式和请求地址
    /*
    method：请求的类型；GET 或 POST
    url：文件在服务器上的位置
    async：true（异步）或 false（同步）
    */
    xmlhttp.open("GET", url+"?"+str, true);
    // 3.发送请求
    xmlhttp.send();
    // 4.监听状态的变化
    xmlhttp.onreadystatechange = function (ev2) &#123;
        /*
        0: 请求未初始化
        1: 服务器连接已建立
        2: 请求已接收
        3: 请求处理中
        4: 请求已完成，且响应已就绪
        */
        if(xmlhttp.readyState === 4)&#123;
            clearInterval(timer);
            // 判断是否请求成功
            if(xmlhttp.status >= 200 && xmlhttp.status < 300 ||
                xmlhttp.status === 304)&#123;
                // 5.处理返回的结果
                // console.log("接收到服务器返回的数据");
                success(xmlhttp);
            &#125;else&#123;
                // console.log("没有接收到服务器返回的数据");
                error(xmlhttp);
            &#125;
        &#125;
    &#125;
    // 判断外界是否传入了超时时间
    if(timeout)&#123;
        timer = setInterval(function () &#123;
            console.log("中断请求");
            xmlhttp.abort();
            clearInterval(timer);
        &#125;, timeout);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            