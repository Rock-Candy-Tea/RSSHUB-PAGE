
---
title: 'HTTP 协议入门（一）｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23a58d0648e7418dbda00033bd1ab97d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 22:30:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23a58d0648e7418dbda00033bd1ab97d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">WWW（World Wide Web）</h2>
<p>中文即万维网</p>
<p>万维网不等同于互联网，万维网只是互联网所能提供的服务其中之一，是靠着互联网运行的一项服务</p>
<p>WWW核心三个概念：</p>
<blockquote>
<p>URI：俗称网址<br>
HTTP：基于TCP/IP协议的网络(超文本)传输协议<br>
HTML：超文本标记语言，超文本就是指可以包含图片等非文字元素</p>
</blockquote>
<h2 data-id="heading-1">URI 与 URL 与 URN</h2>
<p>URI（Uniform Resource Identifier），统一资源标识符，就是方便找到资源，分为 URL 和 URN</p>
<p>URL( Uniform Resource Locator )，统一资源定位符，就是给我们一个地址，一般使用URL作为网址</p>
<p>URN( Uniform Resource Name )，统一资源名称，为每个资源取一个ISBN编号，如果要是用它，我们必须得知道这个编号，那么当然URL是首选</p>
<p>URL的常见组成如下：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23a58d0648e7418dbda00033bd1ab97d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>三者的关系如下：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e83f6b1506454fbf97de2c09a1175cb1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">DNS</h2>
<p>当输入网址后，不是说只输入网址就可以找到资源，需要找到资源对应的服务器，因为资源是从服务器获取的，必须找到该服务器的IP地址才能拿到资源，所以浏览器必须查找IP地址。</p>
<p>DNS就是进行网址/IP转化的。</p>
<p>如果没有DNS协议，那么大家就只能通过输入119.75.217.109来访问百度首页了。有了DNS我们直接输入<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fwww.baidu.com" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=http%3A//www.baidu.com" ref="nofollow noopener noreferrer">www.baidu.com</a>这个容易记的字母拼写即可访问。</p>
<p>DNS将网址翻译成对应的IP地地址，省去了直接记一串IP字母的麻烦。</p>
<p>DNS域名系统：输入网址后，浏览器首先发送给解析域名的服务器，这个服务器返回一串字符给客户端浏览器，然后浏览器才和服务器进行三次对话，对话结束后下载资源。</p>
<p>此外，可以通过命令行来找到百度的IP : nslookup <a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fbaidu.com" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=http%3A//baidu.com" ref="nofollow noopener noreferrer">baidu.com</a>：输出 Address: 220.181.57.216，百度有很多台服务器，所以每个人输出的地址都不一样，他会找离你最近的服务器。</p>
<h2 data-id="heading-3">服务器和浏览器沟通时 http在干啥</h2>
<p>Server + Client + http</p>
<ul>
<li>浏览器负责发起请求</li>
<li>服务器在 80 端口接收请求( http为80端口，https为443 )</li>
<li>服务器负责返回内容（响应）</li>
<li>浏览器负责下载响应内容</li>
</ul>
<p>HTTP 的作用就是指导浏览器和服务器如何进行沟通，HTTP负责规定请求报文上该怎么写，响应报文该怎么写，</p>
<p>当访问一个网页时，浏览器会向网页所在服务器发出请求，当浏览器接收并显示网页前，此网页所在的服务器会返回一个包含HTTP状态码的信息头（server header）用以响应浏览器的请求。</p>
<p>服务器有很多接口，每个接口有固定的用法。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c1594c706b7415bb9fb52bbbb6cbfc1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">请求的格式</h2>
<p>HTTP请求：请求行、请求头部、空行和请求数据四个部分组成。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4daeb494dc184bf09272ab7bd11c47f0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">1 动词 路径 协议/版本
2 Key1: value1
2 Key2: value2
2 Key3: value3
2 Content-Type: application/x-www-form-urlencoded
2 Host: www.baidu.com
2 User-Agent: curl/7.54.0
3 
4 要上传的数据
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>请求最多包含四部分，最少包含三部分。（也就是说第四部分可以为空）</li>
<li>第三部分永远都是一个回车（\n）用于区分第二部分和第四部分，第四部分可能是密码</li>
<li>动词有 GET POST PUT PATCH DELETE HEAD OPTIONS 等</li>
<li>put 整体更新，patch 局部更新</li>
<li>这里的路径包括「查询参数」，但不包括「锚点」</li>
<li>如果你没有写路径，那么路径默认为 /</li>
<li>第 2 部分中的 Content-Type 标注了第 4 部分的格式</li>
<li><code>Host</code>指出请求的目的地（主机域名）；<code>User-Agent</code>是客户端的信息，它是检测浏览器类型的重要信息，由浏览器定义，并且在每个请求中自动发送</li>
</ol>
<p>实例：</p>
<pre><code class="copyable">GET /mix/76.html?name=kelvin&password=123456 HTTP/1.1
Host: www.fishbay.cn
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6

（data）
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">响应的格式</h2>
<p>HTTP响应也由四个部分组成，分别是：状态行、消息报头、空行和响应正文。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83ba4d16c1c544f6a53c5ba1fd93f3b8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">1 协议/版本号 状态码 状态解释
2 Key1: value1
2 Key2: value2
2 Content-Length: 17931
2 Content-Type: text/html 第四部分的格式
3
4 要下载的内容
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>GET 请求和 POST 请求对应的响应可以一样，也可以不一样</li>
<li>响应的第四部分可以很长很长很长</li>
<li>第 2 部分中的 Content-Type 标注了第 4 部分的格式</li>
<li>第 2 部分中的 Content-Type 遵循 MIME 规范</li>
<li>响应头是客户端可以使用的一些信息，如：<code>Date</code>（生成响应的日期）、<code>Content-Type</code>（MIME类型及编码格式）、<code>Connection</code>（默认是长连接）</li>
</ol>
<h2 data-id="heading-6">HTTP状态码</h2>
<p>状态码要背，是服务器对浏览器说的话。</p>
<p>具体如下：</p>
<ul>
<li>
<p>1xx（响应信息，表示HTTP请求已经接受，继续处理请求）</p>
<ul>
<li>101 switch protocol ：切换协议，服务器根据客户端的请求切换协议</li>
</ul>
</li>
<li>
<p>2XX（响应成功，表示HTTP请求已经处理完成）</p>
<ul>
<li><strong>200</strong> ok :服务器已经成功处理请求 <strong>（强缓存）</strong></li>
<li>201 created ：该请求已成功，并因此创建了一个新的资源。这通常是在PUT请求之后发送的响应。（用户新建或修改数据成功）</li>
<li>202 accept ：一个请求已经进入后台，但还未响应</li>
<li>204 no content : 服务器成功处理了请求，但不需要返回任何实体内容（用户删除成功）</li>
</ul>
</li>
<li>
<p>3XX（重定向，表示把请求访问的URL重定向到其他目录）</p>
<ul>
<li><strong>301 move permanently：永久重定向</strong></li>
<li><strong>302 Moved Temporarily：临时重定向</strong>，该资源原本确实存在，但已经被<strong>临时</strong>改变了位置</li>
<li><strong>304</strong> no modified：网页上次请求没有更新，使用缓存,节省带宽和开销 <strong>（协商缓存）</strong></li>
<li><strong>307</strong> 临时重定向，<strong>与302重定向有所区别的地方在于</strong>，收到307响应码后，客户端应保持请求方法不变向新的地址发出请求</li>
</ul>
</li>
<li>
<p>4XX（客户端请求出错，表示客户端出现错误）</p>
<ul>
<li>400 bad request ： 服务器不理解请求的语法</li>
<li><strong>401</strong> <strong>unauthorized : 用户没有权限</strong>（用户名，密码输入错误）</li>
<li><strong>403</strong> <strong>forbidden : 用户得到授权</strong>（401相反），但是访问被禁止</li>
<li><strong>404 not found : 服务器找不到请求的网页</strong></li>
<li>408 request timeout : 请求超时,客户端没有在服务器预备等待的时间内完成一个请求的发送。</li>
</ul>
</li>
<li>
<p>5XX（服务器发生内部错误，表示服务端出现错误）</p>
<ul>
<li><strong>500</strong> interval server error : <strong>服务器遇到未知错误</strong>，无法处理请求</li>
<li>501 not implemented :此请求方法不被服务器支持且无法被处理,只有<code>GET</code>和<code>HEAD</code>是要求服务器支持的</li>
<li>503 service unavailable : 服务器目前无法使用（超载或停机维护）</li>
<li>505 http version not support :服务器不支持请求的HTTP协议的版本，无法完成处理</li>
</ul>
</li>
</ul></div>  
</div>
            