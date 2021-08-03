
---
title: '前端知识链条中少不了的一环--Ajax｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4921'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 08:25:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=4921'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>当我们步入前端大门，走过HTML，看过CSS，翻过JavaScript，接下来你该遇到的，就是它了--Ajax。</p>
<p>这个也是前端与后端交互所必需的东西，非常之重要。所以才有了标题的说法，它是前端知识链条中少不了的一环。</p>
<h2 data-id="heading-1">什么是Ajax？</h2>
<p>Ajax的核心是JavaScript对象XmlHttpRequest，XmlHttp使我们可以使用JavaScript向服务器提出请求并处理响应，而不阻塞用户。</p>
<p>通过XMLHttpRequest对象，前端开发人员就可以在页面加载以后进行页面的局部更新等操作。</p>
<h2 data-id="heading-2">Ajax作用是什么？</h2>
<ul>
<li>通过异步模式，提升了用户体验</li>
<li>不在使用form表单提交（会出现跳转情况），提升了用户体验</li>
<li>Ajax可以实现局部刷新，不用在更新整个页面，传统的网页（不适用Ajax），想要更新内容必须重载整个页面。</li>
</ul>
<p>这就使得web应用程序能够更加敏捷的回应用户操作，避免了多次向服务端发送那些重复的数据。</p>
<h2 data-id="heading-3">详解Ajax创建请求步骤</h2>
<h3 data-id="heading-4">GET请求</h3>
<p>步骤如下：</p>
<ul>
<li>创建一个对象</li>
<li>设置请求参数</li>
<li>发送请求</li>
<li>监听请求成功后的状态变化</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest()
request.open(<span class="hljs-string">"GET"</span>, <span class="hljs-string">"url"</span>)
request.send()
request.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.readyState == <span class="hljs-number">4</span> && <span class="hljs-built_in">this</span>.status == <span class="hljs-number">200</span>) &#123;
    <span class="hljs-built_in">console</span>.log(request.responseText)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>open()</p>
<blockquote>
<p>​       open()方法创建了http请求，它有三个参数，第一个参数指定了提交的方式是POST还是GET，第二个参数是指定要提交的地址是哪，第三个参数是指定异步还是同步（true or false）【目前已经废弃第三个参数】</p>
</blockquote>
</li>
<li>
<p>send()</p>
<blockquote>
<p>send()方法表示着发送请求，不需要任何参数</p>
</blockquote>
</li>
<li>
<p>监听请求成功后的状态变化</p>
<blockquote>
<p>onreadystatechange：监听请求状态改变，readyState改变时会调用此方法，一般用于指定回调函数</p>
<p>readyState：共有五个状态</p>
<ul>
<li>0：未初始化</li>
<li>1：open方法成功调用后</li>
<li>2：服务器已经答应客户端的请求</li>
<li>3：交互中，http头信息已经接收，响应数据未接收</li>
<li>4：完成</li>
</ul>
<p>responseText：服务器端返回的文本内容，默认是字符串</p>
<p>status：服务器端返回的状态码</p>
<p>statusText：服务器端返回的状态码文本说明信息</p>
</blockquote>
</li>
</ul>
<h3 data-id="heading-5">POST请求</h3>
<p>步骤如下：</p>
<ul>
<li>创建一个对象</li>
<li>设置请求参数</li>
<li>设置请求头</li>
<li>发送请求</li>
<li>监听请求成功后的状态变化</li>
</ul>
<p>可以看出，post请求比get请求多出了一个设置请求头的步骤，也请大家记住，这个步骤千万不要忘记！</p>
<pre><code class="copyable">let XHR = new XMLHttpRequest(); 
XHR.open("POST", "url"); 
XHR.setRequestHeader("Content-type","application/x-www-form-urlencoded"); 
XHR.send(data);
XHR.onreadystatechange = function () &#123;
if (XHR.readyState == 4 && XHR.status == 200) &#123;
console.log(XHR.responseText); 
XHR = null; // 此处是为了释放对象，不写也行，js本身也会进行回收
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>send()：解释一下这里send里为什么有个data，这是我们通过Ajax发送post请求给服务器发送了一组data数据。</p>
</li>
<li>
<p>setRequestHeader()：设置请求头</p>
</li>
<li>
<p>readyState值说明 ：</p>
<ul>
<li>0.初始化,XHR对象已经创建,还未执行open</li>
<li>1.载入,已经调用open方法,但是还没发送请求</li>
<li>2.载入完成,请求已经发送完成</li>
<li>3.交互,可以接收到部分数据</li>
<li>4.数据全部返回</li>
</ul>
</li>
<li>
<p>status值说明:</p>
<ul>
<li>200：成功</li>
<li>404：没有发现文件、查询或url</li>
<li>500：服务器内部发生错误</li>
</ul>
</li>
</ul>
<h2 data-id="heading-6">Ajax中 GET与POST请求的区别</h2>
<ul>
<li>刚刚我们已经说过，get请求我们不用设置请求头，而post请求需要。</li>
<li>使用get请求的时候，参数在url中显示，而使用post方式则不会显示出来。</li>
<li>使用get请求发送的数据量小，post请求发送的数据量大。</li>
<li>get请求能够被缓存，post不进行缓存。get请求能够被保存在浏览器的历史记录中（密码等私密数据采用get方式提交，别人查看历史记录就能直接看到这些数据，造成数据泄漏）。</li>
<li>get产生一个TCP数据包，post产生两个tcp数据包。
<ul>
<li>对于get，浏览器会把header跟data一起发出去，服务器响应200，并返回数据。</li>
<li>对于post，浏览器先发送header，服务器响应continue，浏览器再发送data，服务器响应200，并返回数据。</li>
</ul>
</li>
</ul>
<h2 data-id="heading-7">最后</h2>
<p>都是一群为了自己未来拼命学习的人，希望未来的我们会因为当时的环境而感激在大一大二就开始耗费时光，开始奋斗的自己！</p>
<blockquote>
<p>每日一问：今天你卷了没？</p>
</blockquote></div>  
</div>
            