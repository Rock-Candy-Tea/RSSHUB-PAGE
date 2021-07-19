
---
title: 'HTTP系列：HTTP过程及网络层的前端性能优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1329984418254604b9a88643b746b952~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 06:08:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1329984418254604b9a88643b746b952~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>客户端和服务器之间的信息通信有多重方式：</p>
<ul>
<li>XMLHttpRequest/ajax/axios/$.ajax/fetch数据交互</li>
<li>跨域处理方案：ajax、fetch、jsonp、postMessage...</li>
<li>资源获取：（html/css/js/image/音视频...）</li>
<li>webscoket</li>
<li>...</li>
</ul>
<p>一次HTTP过程包括：</p>
<ul>
<li>客户端把信息传递给服务器或者向服务器发送请求（请求 Request）</li>
<li>服务器端接收客户端信息并且返回给客户端相关的内容（响应 Response）</li>
<li>请求+响应=一次HTTP事务</li>
</ul>
<p>客户端和服务器端之间传输的所有内容，统称为HTTP报文。一次HTTP报文包括以下信息：</p>
<ul>
<li>起始行：基本信息（包含HTTP的版本等）。
<ul>
<li>请求起始行   <code>'GET&#123;请求方式&#125; /res-min/themes/marxico.css&#123;请求地址&#125; HTTP/1.1&#123;HTTP版本号&#125;'</code> 。</li>
<li>响应起始行   <code>'HTTP/1.1&#123;HTTP版本号&#125; 200&#123;HTTP响应状态码&#125; OK&#123;状态码描述&#125;'</code></li>
</ul>
</li>
<li>首部（头）：请求头（客户端->服务器）、响应头（服务器->客户端）</li>
<li>主体：请求主体（客户端->服务器）、响应主体（服务器->客户端）</li>
</ul>
<p>客户端和服务器之间的数据传输，依托于网络（通信模式 TCP/UDP... & 传输协议 HTTP/HTTPS/FTP...）。那么，这个过程详细是怎么样的呢?</p>
<h2 data-id="heading-0">从输入URL地址到看到页面，中间都经历了什么？如何优化这一过程？</h2>
<p>老生常谈的问题</p>
<ol>
<li>URL解析（识别URL）</li>
<li>检查缓存（强缓存、协商缓存&#123;针对于资源文件请求&#125; & 本地存储&#123;针对于数据请求&#125;）</li>
<li>DNS服务器解析（域名解析：根据域名解析出服务器的外网IP）</li>
<li>TCP三次握手（建立客户端和服务器之间的网络连接通道）</li>
<li>基于HTTP/HTTPS等传输协议，实现客户端和服务器之间的信息通信</li>
<li>TCP四次挥手（把建立好的网络通道释放掉）</li>
<li>客户端渲染（呈现出页面和效果）</li>
</ol>
<p>下面详细说说每个过程</p>
<h3 data-id="heading-1">URL解析（识别URL）</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1329984418254604b9a88643b746b952~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>URI统一资源标识符，包括</p>
<ul>
<li>URL：统一资源定位符</li>
<li>URN：统一资源名称</li>
</ul>
<p>一段URL <code>'http://user:pass@www.baidu.cn:80/st/index.html?xxx=xxx&xxx=xxx#video'</code> ，结构分析如下：</p>
<h4 data-id="heading-2">传输协议</h4>
<p>传输协议：http / https / ftp ...</p>
<ul>
<li>HTTP超文本传输协议。即除了传输文本（例如字符串等）还可以传输其余的信息（例如：文件流、二进制或者Buffer格式再或者BASE64格式的数据）</li>
<li>HTTPS=HTTP+SSL 更加安全的HTTP。传输的内容经过加密处理，一般涉及支付类的产品都采用这种协议</li>
<li>FTP文件传输协议，一般用于直接基于一些FTP工具（例如filezilla），把开发的文件部署到服务器上</li>
<li>...</li>
</ul>
<h4 data-id="heading-3">登录认证信息</h4>
<p>用户名密码：user:pass，一般是不用的</p>
<h4 data-id="heading-4">域名</h4>
<p>域名：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.baidu.cn" target="_blank" rel="nofollow noopener noreferrer" title="http://www.baidu.cn" ref="nofollow noopener noreferrer">www.baidu.cn</a></p>
<ul>
<li>顶级域名 baidu.cn</li>
<li>一级域名 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.baidu.cn" target="_blank" rel="nofollow noopener noreferrer" title="http://www.baidu.cn" ref="nofollow noopener noreferrer">www.baidu.cn</a></li>
<li>二级域名 video.baidu.cn</li>
<li>三级域名 student.video.baidu.cn</li>
<li>...</li>
</ul>
<p>购买的是顶级域名，自己后期可以分配二级/三级域名。</p>
<p>域名的目的就是给对应的服务器外网IP起一个别名，方便用户记忆</p>
<p>域名和服务器都购买完成后，需要在DNS服务器上生成一条解析记录，用于以后的DNS解析</p>
<p>.com / .cn / .net / .org / .gov /不同的后缀也有一些不同的意义</p>
<p>协议、域名、端口号只要有一个不同，则为<strong>跨域</strong>。跨域的问题后面写文章单独讲。以下皆为跨域：</p>
<ul>
<li><code>'www.baidu.com'</code>  VS  <code>'www.qq.com'</code>  ：跨域</li>
<li><code>'www.baidu.com'</code>  VS  <code>'video.baidu.com'</code>  ：跨域（主域相同，但是子域不同）</li>
<li><code>' www.baidu.com:80'</code>  VS  <code>'www.baidu.com:443'</code> ：跨域</li>
<li><code>'http://www.baidu.com'</code>  VS  <code>'https://www.baidu.com'</code> ：跨域</li>
</ul>
<p>下面为同源：</p>
<p><code>'http://www.baidu.com:80/st.html'</code>  VS  <code>'http://www.baidu.com:80/index.html'</code> ：同源</p>
<h4 data-id="heading-5">端口号</h4>
<p>端口号：80。端口就是用来区分一台服务器上的多个项目的（每一个项目其实都是一个服务）。 取值范围 0~65535之间</p>
<p>默认端口号：在浏览器地址栏中输入地址，我们不写端口号，浏览器会帮助我们加上，传递给服务器的时候是带着端口号的。http->80 ， https->443，ftp->21。</p>
<h4 data-id="heading-6">请求资源的路径名称</h4>
<p>请求资源的路径名称：/st/index.html，可以基于路径找到客户端需要的资源文件。</p>
<p>用户看到的URL地址可能是重写后的（看到的地址在文件目录中不存在），例如ajax数据请求的接口地址为/api/list，后台可以根据这个不存在的地址返回其他相应的东西</p>
<h4 data-id="heading-7">问号参数信息（查询字符串）</h4>
<p>问号参数信息：?xxx=xxx&xxx=xxx</p>
<ul>
<li>把信息传递给服务器。GET系列请求一般都是这样传递参数 。 xxx=xxx&xxx=xxx这种格式叫做x-www-form-urlencoded格式</li>
<li>如果是页面跳转，查询字符串可以把信息传递给另外一个页面</li>
</ul>
<h4 data-id="heading-8">片段标识符（HASH值）</h4>
<p>HASH（哈希）值：#video
一般用作：</p>
<ul>
<li>锚点定位</li>
<li>HASH路由</li>
</ul>
<h4 data-id="heading-9">其他问题（URL编译问题）</h4>
<p>如果一段url如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> url = <span class="hljs-string">` http://www.xxx.com/index.html?lx=1&from=http://www.qq.com/'.
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>其中查询字符串from包含一个完整的域名，浏览其解析的时候就会出问题， <code>http://www.xxx.com/index.html?lx=1&from=</code> 会被解析为一个url， <code>http://www.qq.com/</code> 会被解析为另一个url。</p>
<p>所以我们要对整个url或者后面的查询字符串进行编码，让浏览器只识别成为一个url</p>
<p>编码分类：</p>
<ul>
<li><code>encodeURI</code>  &  <code>decodeURI</code> ：编译<strong>空格和中文</strong>，一般编译整个URL中的信息
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> url =  <span class="hljs-string">` http://www.xxx.com/s t/index.html?x=1&name=你好&from=http://www.qq.com `</span> 
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">encodeURI</span>(url))
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c7d34439d284e44b0fc9eb9061b41bb~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>空格和中文被编码</p>
<ul>
<li><code>encodeURIComponent</code>  &  <code>decodeURIComponent</code> ：编译<strong>空格和中文以及一些特殊符号</strong>，所以一般只是用来编译传递的信息值的，而不是整个URL，以解决URL解析不了或者传递信息的乱码等问题。
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> url =  <span class="hljs-string">` http://www.xxx.com/st/index.html?x=1&name=<span class="hljs-subst">$&#123;<span class="hljs-built_in">encodeURIComponent</span>(<span class="hljs-string">'你 好'</span>)&#125;</span>&from=<span class="hljs-subst">$&#123;<span class="hljs-built_in">encodeURIComponent</span>(<span class="hljs-string">'http://www.qq.com'</span>)&#125;</span> `</span> 
    <span class="hljs-built_in">console</span>.log(url)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f6b5abc9aa548fb9d65a60c3a2693bd~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>escape</code>  &  <code>unescape</code> :用于客户端页面信息传递或者一些信息的编译的「例如：cookie中的中文内容编译」
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">escape</span>(<span class="hljs-string">'你好'</span>));
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">encodeURIComponent</span>(<span class="hljs-string">'你好'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29dbe01d13c8469ea17aa95b703c6659~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">检查缓存</h3>
<p>缓存处理是基于HTTP网络层进行优化的一个非常重要的手段「针对的资源文件请求」</p>
<p>检查缓存的两种方式</p>
<ul>
<li>强缓存、协商缓存（针对于资源文件请求）</li>
<li>本地存储（针对于数据请求）</li>
</ul>
<h4 data-id="heading-11">缓存位置</h4>
<ul>
<li>Memory Cache : 内存缓存</li>
<li>Disk Cache：硬盘缓存</li>
</ul>
<p>区别：</p>
<ul>
<li>打开网页时：浏览器会首先查找 Disk Cache中是否有匹配的缓存，如有则使用，如没有则发送网络请求。</li>
<li>普通刷新 (F5)时：因TAB没关闭，因此Memory Cache是可用的，所以刷新时，如果内存中有缓存，会被优先使用，其次才去查找Disk Cache</li>
<li>强制刷新 (Ctrl + F5)：浏览器不使用缓存，因此发送的请求头部均带有 Cache-control: no-cache，服务器直接返回 200 和最新内容</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49e2f0b43517473abc8ed93b52171418~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50296e268fc1402b82b94c10e89bd046~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">强缓存</h4>
<p>强缓存：Expires / Cache-Control</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8d1bd2eda9c4f8c840f82a1faa5c0ea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>强缓存的作用过程是这样的：</p>
<ul>
<li>第一次请求资源时返回请求结果和<strong>缓存标识</strong>（响应头Expires/ Cache-Control），把请求结果和缓存表示存储在浏览器缓存当中</li>
<li>缓存标识的作用机理：
<ul>
<li>Expires：缓存过期时间，用来指定资源到期的时间（HTTP/1.0）</li>
<li>Cache-Control：会返回如下样子的响应头 <code>'Cache-Control： max-age=2592000'</code> ,意思为第一次拿到资源后的2592000秒内（30天），再次发送请求，读取缓存中的信息（HTTP/1.1）</li>
</ul>
</li>
<li>如果再次发送请求，会先检测缓存信息和缓存标识Expires/ Cache-Control，如果有，且未过期，那么客户端直接读取缓存的信息，不再发送请求给服务器</li>
<li>注意如果两者同时存在的话，Cache-Control优先级高于Expires</li>
</ul>
<p>问题：本地缓存了文件，但是服务对应的资源文件更新了，我们如何保证获取的是最新的内容？</p>
<ul>
<li>
<p>请求资源文件的时候设置时间戳</p>
<p>例如：第一次 <code><link href='index.css?20210224215800'></code> ,第二次 <code><link href='index.css?20210227000000'></code> 。如果服务器资源有更新，再次发请求，保证时间戳不一样，这样就不会走本地的强缓存了，而是从新拉取最新的资源</p>
</li>
<li>
<p>文件HASH名</p>
<p>例如：第一次 <code><link href='dasdasd43546.css'></code> ,如果服务器资源更新，文件名字重新HASH（webpack） <code><link href='75675675fsdff6.css'></code> ,这样就不会走本地的强缓存了</p>
</li>
</ul>
<p>所以HTML文件永远不会去做强缓存</p>
<p>第一次</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">'dasdasd43546.css'</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二次</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">'75675675fsdff6.css'</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">协商缓存</h4>
<p>协商缓存就是强制缓存失效后，浏览器携带缓存标识向服务器发起请求，由服务器根据缓存标识决定是否使用缓存的过程</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c1b15c5c2244f45b591374a7f96a95c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>协商缓存的作用过程是这样的（以Etag举例）：</p>
<ul>
<li>首先第一次发送请求，获得的响应包含响应头（假设为Etag:s35b56f）和响应主体，然后把内容缓存下来</li>
<li>第二次发送请求给后台，会携带缓存标识（If-Modfined-Since/If-None-Match）发送HTTP请求，例如请求头：If-Modfined-Since:s35b56f，这个标识就是第一次返回的Etag的一个标识</li>
<li>服务器根据Etag判断文件是否更新
<ul>
<li>没更新：返回304，不返回内容，通知客户端读取本地的缓存信息</li>
<li>更新了：返回200，以及最新的资源信息，以及Last-Modfined/Etag的新的值</li>
</ul>
</li>
<li>浏览器接收到返回的信息
<ul>
<li>如果是200：说明是最新的信息那就直接渲染，并且把最新的结果和表示缓存到本地</li>
<li>如果是304：就从本地缓存中获取内容进行渲染</li>
</ul>
</li>
</ul>
<p>Last-Modified / ETag的意义：</p>
<ul>
<li>Last-Modified:记录服务器资源文件最后一次更新的时间</li>
<li>ETag:只要服务器资源文件改变，会生成一个不同的标识</li>
</ul>
<p>协商缓存的意义：</p>
<ul>
<li>当强缓存失效(或者不存在)（例如：html）那就可以做协商缓存，然后校验协商缓存即可</li>
<li>每一次都会向服务器校验资源是否更新</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39a1f8a8fefa481f973de8a2ebff6851~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看一下百度某个css文件的缓存设置
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a112bd70b194979aae69417ae189575~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意：</p>
<p>强缓存还是协商缓存都是服务器端设置的，客户端浏览器自己会根据返回的一些信息，进行相关处理，无需前端单独设置</p>
<p>注意：<strong>强缓存没有发送请求</strong>，在发送请求之前发现有缓存就用了本地的缓存内容，而<strong>协商缓存发送了请求</strong>（因为要询问后台是否使用缓存，与后台协商），如果返回了304，就用本地的缓存。</p>
<h4 data-id="heading-14">本地存储缓存</h4>
<p>从这个角度来缓存，就需要使用js进行编码，逻辑处理</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92891855c9e74cc188fdaeeccb4fb46b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本地存储缓存的两种方式：</p>
<ul>
<li>页面不关闭，针对于不经常更新的数据，我们读取缓存数据，这种数据一般存在内存中，页面刷新，存储的数据就没有了</li>
<li>页面关闭，重新打开，我们也可以读取缓存中的数据,这种数据就是持久化存储，我们可以自己设置过期时间</li>
</ul>
<p>客户端存储数据的几种方案：</p>
<ul>
<li>(全局)变量存储「vuex/redux」：页面刷新或者关闭后重新打开，之前存储的数据都没有了（内存释放问题导致的）</li>
<li>cookie</li>
<li>webStorage：localStorage & sessionStorage</li>
<li>IndexedDB</li>
<li>Cache</li>
<li>Manifest 离线存储</li>
</ul>
<h4 data-id="heading-15">localStorage VS sessionStorage</h4>
<p>HTML5新增的API「不兼容IE8及以下浏览器」</p>
<ul>
<li>localStorage：持久化本地存储「没有过期时间」，页面关闭存储的内容也是在的，只有手动清除(或者卸载浏览器)才会清除</li>
<li>sessionStorage会话存储，页面关闭后，存储的信息会消失「但是页面刷新是不消失的」</li>
</ul>
<h4 data-id="heading-16">localStorage VS cookie</h4>
<p>地存储的数据是有同源访问限制的，只允许读取本源下存储的内容</p>
<ul>
<li>
<p>cookie只允许一个源下最多存储4KB内容，所以不能存储太多的数据。localStorage可以同源下存储5MB内容！</p>
</li>
<li>
<p>cookie是需要设置过期时间的，超过时间就失效了，并且有路径等限制。localStorage是持久化存储，没有过期时间，除非自己设定一些过期的处理机制。</p>
</li>
<li>
<p>cookie不稳定「一些浏览器自带的清除操作，有可能会把cookie清除掉；开启无痕浏览或者隐私模式，则不能存储cookie信息。但是localStorage不受这些操作的影响。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92ca1fd9aea14aec957e58104a61dfff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>cookie兼容低版本浏览器</p>
</li>
<li>
<p>cookie不算严格的本地存储，和服务器之间有很多的联系。客户端向服务器发送请求的时候，会默认把本地的cookie信息，基于请求头发送给服务器；并且如果服务器返回的响应头中有Set-Cookie字段，浏览器也会默认把这些信息在客户端本地存在cookie中。localStorage是严格本地存储，默认情况下和服务器没有关系。</p>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa10b80359b94046a8c892a15877802c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>用代码来演示本地缓存的使用原理</p>
<p>将缓存数据存在全局变量中（刷新缓存消失）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> submit = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#submit'</span>),
     runing = <span class="hljs-literal">false</span>;

<span class="hljs-keyword">let</span> serverData;
submit.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
   <span class="hljs-keyword">if</span> (runing) <span class="hljs-keyword">return</span>;<span class="hljs-comment">//简单的防抖处理</span>
   runing = <span class="hljs-literal">true</span>;

   <span class="hljs-keyword">if</span> (serverData) &#123;
      <span class="hljs-comment">// 如果有数据，直接使用缓存数据，无需从服务器获取</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求回来的数据是：'</span>, serverData);
      runing = <span class="hljs-literal">false</span>;
      <span class="hljs-keyword">return</span>;
   &#125;

   <span class="hljs-comment">// 从服务器拉去数据，并其存储到全局变量中</span>
   axios.get(<span class="hljs-string">'http://127.0.0.1:8888/home_banner'</span>).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求回来的数据是：'</span>, response.data);
      serverData = response.data;
      runing = <span class="hljs-literal">false</span>;
   &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>sessionStorage:</p>
<pre><code class="hljs language-js copyable" lang="js"> submit.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
   <span class="hljs-keyword">if</span> (runing) <span class="hljs-keyword">return</span>;
   runing = <span class="hljs-literal">true</span>;

   <span class="hljs-keyword">let</span> data = sessionStorage.getItem(<span class="hljs-string">'@A'</span>);
   <span class="hljs-keyword">if</span> (data) &#123;
      <span class="hljs-comment">// 如果有数据，直接使用缓存数据，无需从服务器获取</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求回来的数据是：'</span>, <span class="hljs-built_in">JSON</span>.parse(data));
      runing = <span class="hljs-literal">false</span>;
      <span class="hljs-keyword">return</span>;
   &#125;

   <span class="hljs-comment">// 从服务器拉去数据</span>
   axios.get(<span class="hljs-string">'http://127.0.0.1:8888/home_banner'</span>).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求回来的数据是：'</span>, response.data);
      sessionStorage.setItem(<span class="hljs-string">'@A'</span>, <span class="hljs-built_in">JSON</span>.stringify(response.data));
      runing = <span class="hljs-literal">false</span>;
   &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>localStorage持久化存储要加上过期时间。</p>
<pre><code class="hljs language-js copyable" lang="js">submit.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
   <span class="hljs-keyword">if</span> (runing) <span class="hljs-keyword">return</span>;
   runing = <span class="hljs-literal">true</span>;

   <span class="hljs-keyword">let</span> data = <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'@A'</span>);
   <span class="hljs-keyword">if</span> (data) &#123;
      data = <span class="hljs-built_in">JSON</span>.parse(data);
      <span class="hljs-comment">// 自己可以设定过期的标准 1小时</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() - data.time <= <span class="hljs-number">60</span> * <span class="hljs-number">60</span> * <span class="hljs-number">1000</span>) &#123;
         <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求回来的数据是：'</span>, data.data);
         runing = <span class="hljs-literal">false</span>;
         <span class="hljs-keyword">return</span>;
      &#125;
   &#125;

   <span class="hljs-comment">// 从服务器拉去数据，并其存储到全局变量中</span>
   axios.get(<span class="hljs-string">'http://127.0.0.1:8888/home_banner'</span>).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求回来的数据是：'</span>, response.data);
      <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'@A'</span>, <span class="hljs-built_in">JSON</span>.stringify(&#123;
         <span class="hljs-attr">time</span>: +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
         <span class="hljs-attr">data</span>: response.data
      &#125;));
      runing = <span class="hljs-literal">false</span>;
   &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">DNS服务器解析</h3>
<p>两种解析方法</p>
<ul>
<li>
<p>递归查询</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cc50a575e47483c8113394cb3f5849c~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>迭代查询
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1485b6f0ed254c73b8604a56fc3a6cf1~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>如果访问资源的域名的域名比较多，说明资源是部署到多台服务器上的，此时需要更多的DNS解析，导致消耗的时间会更多
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bc6162d5e814b76a14c6bba473adb05~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>多台服务器也有自己的好处：</p>
<ul>
<li>
<p>资源的合理利用，性能高的服务器就用来存储数据，性能不好的就用来存储静态资源，减少资金</p>
</li>
<li>
<p>抗压能力加强，多台服务器减少压力</p>
</li>
<li>
<p>提高HTTP并发，多台服务器可以提高总共服务器的并发请求
例如百度：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84dd71c2ab9849d6a90c7bfae379130a~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将不用的资源放到不同的服务器上</p>
</li>
</ul>
<p>DN解析优化：</p>
<p>每一次DNS解析时间预计在20~120毫秒，可以使用<strong>DNS预获取</strong>（DNS Prefetch）来减少DNS请求次数。</p>
<p>例如：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"x-dns-prefetch-control"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"on"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"dns-prefetch"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"//static。360buyimg。com"</span>/></span>

<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"dns-prefetch"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"//misc。360buyimg。com"</span>/></span>

<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"dns-prefetch"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"//img10.360buyimg。com"</span>/></span>

<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"dns-prefetch"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"//d。3.cn"</span>/></span>

<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"dns-prefetch"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"//d。jd。com"</span>/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理：link会单独开辟一个线程去加载资源，同时html继续向下渲染。所以可以单独开辟一个县城预先解析所有DNS并且缓存，如果下面再遇到这个域名，例如img的src中包含这个域名，那么DNS解析就不用重新再次解析了。</p>
<h3 data-id="heading-18">TCP三次握手</h3>
<p>TCP三次握手的目的：让客户端和服务器端建立稳定可靠的传输通道，确定<strong>双方</strong>都可以<strong>收发</strong>信息。</p>
<p>UDP不需要三次握手，但是快且不稳定。</p>
<h3 data-id="heading-19">数据传输</h3>
<p>HTTP请求与响应。</p>
<p>这部分可以看一下我以前写的这篇文章</p>
<p><a href="https://juejin.cn/post/6985823318070788110" target="_blank" title="https://juejin.cn/post/6985823318070788110">HTTP系列：AJAX基础梳理、axios基本使用梳理 （juejin.cn）</a></p>
<h3 data-id="heading-20">TCP四次挥手</h3>
<p>释放建立的链接通道</p>
<ul>
<li>服务器端收到客户端的SYN连接请求报文后，可以直接发送SYN+ACK报文</li>
<li>但关闭连接时，当服务器端收到FIN报文时，很可能并不会立即关闭链接（正在传输数据），所以只能先回复一个ACK报文，告诉客户端：”你发的FIN报文我收到了”，只有等到服务器端所有的报文都发送完了，我才能发送FIN报文，因此不能一起发送</li>
<li>等所有数据正在传输的数据全部传输完成，服务器才给再次发送一个FIN报文</li>
</ul>
<p>故需要四步握手</p>
<p>TCP连接优化方法：</p>
<p>保持长链接，不关闭http通道，设置Connection： keep-alive请求头
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a70ca8ac451842ab8842a156ce2d6140~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">客户端渲染</h3>
<p>客户端渲染优化可以看我以前的两篇文章</p>
<p><a href="https://juejin.cn/post/6975028927223824391" target="_blank" title="https://juejin.cn/post/6975028927223824391">浏览器渲染过程和CRP优化一：渲染过程 （juejin.cn）</a></p>
<p><a href="https://juejin.cn/post/6975093992232845342" target="_blank" title="https://juejin.cn/post/6975093992232845342">浏览器渲染过程和CRP优化二：CRP优化 （juejin.cn）</a></p>
<h2 data-id="heading-22">网络层性能优化汇总</h2>
<p>网络优化是前端性能优化的中的重点内容，因为大部分的消耗都发生在网络层，尤其是第一次页面加载，如何减少等待时间很重要。http层面的性能优化可以减<strong>少白屏的效果和时间</strong></p>
<p>刚说了http的一次流程，中间顺便穿插一些优化的方法，这里做一个汇总，顺便补充一些内容</p>
<ol>
<li>
<p>利用缓存</p>
<ul>
<li>
<p>对于静态资源文件实现强缓存和协商缓存（扩展：文件有更新，如何保证及时刷新）</p>
</li>
<li>
<p>对于不经常更新的接口数据采用本地存储做数据缓存（扩展：cookie / localStorage / vuex|redux 区别）</p>
</li>
</ul>
</li>
<li>
<p>DNS优化</p>
<ul>
<li>
<p>分服务器部署，增加HTTP并发性（导致DNS解析变慢）</p>
</li>
<li>
<p>DNS Prefetch</p>
</li>
</ul>
</li>
<li>
<p>TCP的三次握手和四次挥手</p>
<ul>
<li>Connection：keep-alive</li>
</ul>
</li>
<li>
<p>数据传输</p>
<ul>
<li>
<p>减少数据传输的大小</p>
<ul>
<li>
<p>内容或者数据压缩（webpack等）</p>
</li>
<li>
<p>服务器端一定要开启GZIP压缩（一般能压缩60%左右）</p>
</li>
<li>
<p>大批量数据分批次请求（例如：下拉刷新或者分页，保证首次加载请求数据少）</p>
</li>
</ul>
</li>
<li>
<p>减少HTTP请求的次数</p>
<ul>
<li>
<p>资源文件合并处理</p>
</li>
<li>
<p>字体图标，一些就不要发请求了，尽量使用字体去做，阿里图标</p>
</li>
<li>
<p>雪碧图 CSS-Sprit</p>
</li>
<li>
<p>图片的BASE64</p>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p>CDN服务器“地域分布式”</p>
<p>在多个地方部署服务器，让各个地域的访问速度保持一致</p>
</li>
<li>
<p>采用HTTP2.0</p>
</li>
</ol>
<p>减少白屏：</p>
<ul>
<li>
<p>loading人性化体验</p>
</li>
<li>
<p>骨架屏：客户端骨屏（其实也是一个loading） + 服务器骨架屏</p>
</li>
<li>
<p>图片延迟加载</p>
</li>
</ul>
<p>减少白屏也是一个值得探索的问题，以后写文章再详细说</p>
<h2 data-id="heading-23">HTTP几个版本的区别</h2>
<h3 data-id="heading-24">HTTP1.0和HTTP1.1的一些区别</h3>
<ul>
<li><strong>缓存处理</strong>，HTTP1.0中主要使用 Last-Modified，Expires 来做为缓存判断的标准，HTTP1.1则引入了更多的缓存控制策略：ETag，Cache-Control</li>
<li><strong>带宽优化及网络连接的使用</strong>，HTTP1.1支持断点续传，即返回码是206（Partial Content）</li>
<li>错误通知的管理，在HTTP1.1中新增了24个错误状态响应码，如409（Conflict）表示请求的资源与资源的当前状态发生冲突；410（Gone）表示服务器上的某个资源被永久性的删除…</li>
<li><strong>Host头处理</strong>，在HTTP1.0中认为每台服务器都绑定一个唯一的IP地址，因此，请求消息中的URL并没有传递主机名（hostname）。但随着虚拟主机技术的发展，在一台物理服务器上可以存在多个虚拟主机（Multi-homed Web Servers），并且它们共享一个IP地址。HTTP1.1的请求消息和响应消息都应支持Host头域，且请求消息中如果没有Host头域会报告一个错误（400 Bad Request）</li>
<li><strong>长连接</strong>，HTTP1.1中默认开启Connection： keep-alive，一定程度上弥补了HTTP1.0每次请求都要创建连接的缺点</li>
</ul>
<h3 data-id="heading-25">HTTP2.0和HTTP1.X相比的新特性</h3>
<ul>
<li>
<p><strong>新的二进制格式（Binary Format）</strong>，HTTP1.x的解析是基于文本，基于文本协议的格式解析存在天然缺陷，文本的表现形式有多样性，要做到健壮性考虑的场景必然很多，二进制则不同，只认0和1的组合，基于这种考虑HTTP2.0的协议解析决定采用二进制格式，实现方便且健壮</p>
</li>
<li>
<p><strong>header压缩</strong>，HTTP1.x的header带有大量信息，而且每次都要重复发送，HTTP2.0使用encoder来减少需要传输的header大小，通讯双方各自cache一份header fields表，既避免了重复header的传输，又减小了需要传输的大小</p>
</li>
<li>
<p><strong>服务端推送（server push）</strong>，例如我的网页有一个sytle.css的请求，在客户端收到sytle.css数据的同时，服务端会将sytle.js的文件推送给客户端，当客户端再次尝试获取sytle.js时就可以直接从缓存中获取到，不用再发请求了</p>
<pre><code class="hljs language-txt copyable" lang="txt">// 通过在应用生成HTTP响应头信息中设置Link命令

Link: </styles.css>; rel=preload; as=style, </example.png>; rel=preload; as=image
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>多路复用（MultiPlexing）</strong></p>
<p>并发请求指的是建立多个链接通道,而不是在一个通道上进行多个HTTP请求</p>
<ul>
<li>
<p>HTTP/1.0  每次请求响应，建立一个TCP连接，用完关闭</p>
</li>
<li>
<p>HTTP/1.1 「长连接」 ,但是,若干个请求排队串行化单线程处理，后面的请求等待前面请求的返回才能获得执行机会，一旦有某请求超时等，后续请求只能被阻塞，毫无办法，也就是人们常说的线头阻塞；</p>
</li>
<li>
<p>HTTP/2.0 「多路复用」多个请求可同时在一个连接上并行执行，某个请求任务耗时严重，不会影响到其它连接的正常执行；</p>
</li>
</ul>
</li>
</ul></div>  
</div>
            