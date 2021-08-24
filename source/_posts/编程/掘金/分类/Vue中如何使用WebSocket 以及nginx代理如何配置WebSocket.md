
---
title: 'Vue中如何使用WebSocket 以及nginx代理如何配置WebSocket'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3582'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 20:21:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=3582'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">简述websocket特性:</h2>
<p>1.主要有ws(不加密)和wss(加密)；ws是基于http请求建立握手，wss是基于https请求建立握手。<br>
2.ws的握手基于http的get方式，协议应不小于1.1。<br>
3.ws和wss的请求头会比单纯的http的请求头多很多特殊的header。<br>
4.ws请求在建立连接后，通信双方都可以在任何时刻向另一方发送数据。(http只能客户端发送请求给服务端)<br>
websocket的基本用法这里就不介绍了，网上相关的文章有很多，在此贴出不错的链接地址。<br>
w3c对websocket的介绍：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fhtml%2Fhtml5-websocket.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/html/html5-websocket.html" ref="nofollow noopener noreferrer">www.runoob.com/html/html5-…</a></p>
<h2 data-id="heading-1">项目配置:</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改vue.config.js文件</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 启动后在浏览器打开</span>
    <span class="hljs-attr">proxy</span>: &#123; 
      <span class="hljs-string">'/api'</span>: &#123; <span class="hljs-comment">// 设置普通的http代理</span>
        <span class="hljs-attr">target</span>: <span class="hljs-string">'http://x.x.x.x:8080'</span>,
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">pathRewrite</span>: &#123;
          <span class="hljs-string">'^/api'</span>: <span class="hljs-string">''</span>
        &#125;
      &#125;,
      <span class="hljs-string">'/socket'</span>: &#123; <span class="hljs-comment">// 设置websocket代理</span>
        <span class="hljs-attr">target</span>: <span class="hljs-string">'http://x.x.x.x:8080'</span>,
        <span class="hljs-attr">ws</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 开启websocket代理  注意</span>
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">pathRewrite</span>: &#123;
          <span class="hljs-string">'^/socket'</span>: <span class="hljs-string">''</span>
        &#125;
    &#125;&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">Vue单页面</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">socket</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">connectCount</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 连接次数</span>
      <span class="hljs-attr">heartInterval</span>: <span class="hljs-literal">null</span>
    &#125;
  &#125;,
  created () &#123;
    <span class="hljs-built_in">this</span>.initSocket()
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">/**
     * 建立连接是http
     * 消息推送都是tcp连接，没有同源限制
     * 服务端人员try catch 消息推送不成功，则关闭连接
     */</span>
    initSocket () &#123;
      <span class="hljs-keyword">const</span> &#123; protocol, host &#125; = location
      <span class="hljs-keyword">const</span> url = <span class="hljs-string">`<span class="hljs-subst">$&#123;protocol === <span class="hljs-string">'https'</span> ? <span class="hljs-string">'wss'</span> : <span class="hljs-string">'ws'</span>&#125;</span>://<span class="hljs-subst">$&#123;host&#125;</span>/socket/websocket/mineStatus/<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.$store.getters.userId&#125;</span>`</span>
      <span class="hljs-comment">// 判断当前浏览器是否支持WebSocket</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> WebSocket === <span class="hljs-string">'undefined'</span>) &#123;
        <span class="hljs-built_in">this</span>.$notification.warning(&#123;
          <span class="hljs-attr">message</span>: <span class="hljs-string">'系统提示'</span>,
          <span class="hljs-attr">description</span>: <span class="hljs-string">'您的浏览器不支持socket'</span>,
          <span class="hljs-attr">duration</span>: <span class="hljs-number">4</span>
        &#125;)
        <span class="hljs-keyword">return</span>
      &#125;
      
      <span class="hljs-built_in">this</span>.socket = <span class="hljs-keyword">new</span> WebSocket(url)
      <span class="hljs-built_in">this</span>.socket.onmessage = <span class="hljs-function">(<span class="hljs-params">evt</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (evt.data === <span class="hljs-string">'连接成功'</span> || evt.data.includes(<span class="hljs-string">'refresh'</span>)) &#123;
          <span class="hljs-built_in">this</span>.heartCheck() <span class="hljs-comment">// 重置心跳检测</span>
          <span class="hljs-comment">// this.onRefresh() 接收到推送消息，刷新列表</span>
        &#125;
      &#125;
      
      <span class="hljs-comment">// 监听窗口事件，当窗口关闭时，主动断开websocket连接</span>
      <span class="hljs-built_in">window</span>.onbeforeunload = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.closeSocket()
      &#125;
    &#125;,
    <span class="hljs-comment">/**
     * 定时发送心跳包
     * 59s发送一次心跳，比nginx设置的最大连接时间短一点，以达到在临界点重置连接时间
     */</span>
    heartCheck () &#123;
      <span class="hljs-keyword">const</span> _this = <span class="hljs-built_in">this</span>
      <span class="hljs-built_in">this</span>.heartInterval && <span class="hljs-built_in">clearTimeout</span>(<span class="hljs-built_in">this</span>.heartInterval)
      <span class="hljs-built_in">this</span>.heartInterval = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.socket.readyState === <span class="hljs-number">1</span>) &#123; <span class="hljs-comment">// 连接状态</span>
          <span class="hljs-built_in">this</span>.socket.send(<span class="hljs-string">'ping'</span>)
        &#125; <span class="hljs-keyword">else</span> &#123;
          _this.connectCount += <span class="hljs-number">1</span>
          <span class="hljs-keyword">if</span> (_this.connectCount <= <span class="hljs-number">5</span>) &#123;
            <span class="hljs-built_in">this</span>.initSocket() <span class="hljs-comment">// 断点重连5次</span>
          &#125;
        &#125;
      &#125;, <span class="hljs-number">59</span> * <span class="hljs-number">1000</span>)
    &#125;,
    <span class="hljs-comment">/** 断开websocket连接 */</span>
    <span class="hljs-function"><span class="hljs-title">closeSocket</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.socket.close()
      <span class="hljs-built_in">this</span>.heartInterval && <span class="hljs-built_in">clearTimeout</span>(<span class="hljs-built_in">this</span>.heartInterval)
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.closeSocket()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ps：当客户端网络不好，或者断网，服务器并不知情，还是会给客户端推送消息，造成资源浪费，故后端服务器要做异常处理，在消息推送不成功，主动关闭websocket连接。</code></p>
<h2 data-id="heading-3">Nginx配置</h2>
<pre><code class="hljs language-js copyable" lang="js">http &#123;
    map $http_upgrade $connection_upgrade &#123;
        <span class="hljs-keyword">default</span> upgrade;
        <span class="hljs-string">''</span>      close;
    &#125;

    server &#123;
        listen       <span class="hljs-number">8084</span>;
        server_name  _;
        root         /usr/share/nginx/html/pcNet;
        include /etc/nginx/<span class="hljs-keyword">default</span>.d<span class="hljs-comment">/*.conf;
        
        location ^~/socket/ &#123;
           proxy_pass http://x.x.x.x:8080/;
           proxy_http_version 1.1; 
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header Upgrade websocket;
           proxy_set_header Connection Upgrade;
        &#125;        

        location ^~/api/ &#123;
           proxy_pass http://x.x.x.x:8080/;
        &#125;
        ...
    &#125;&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>配置的属性参数：<br>
proxy_pass: 要代理到的url<br>
roxy_http_version: 代理时使用的 http版本<br>
proxy_set_header Host: http请求的主机域名<br>
proxy_set_header X-Real-IP: 给代理设置原http请求的ip,填写$remote_addr 即可<br>
proxy_set_header X-Forwarded-For: 反向代理之后转发之前的IP地址<br>
proxy_set_header Upgrade: 把代理时http请求头的Upgrade 设置为原来http请求的请求头,wss协议的请求头为websocket<br>
proxy_set_header Connection: 因为代理的wss协议,所以http请求头的Connection设置为Upgrade<br>
<code>在此特别注意: https是加密请求，需要SSL加密，所以nginx支持https，需要配置SSL</code><br>
<code>在此贴出解决方案的链接</code><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fzhoudawei%2Fp%2F9257276.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/zhoudawei/p/9257276.html" ref="nofollow noopener noreferrer">www.cnblogs.com/zhoudawei/p…</a></p></div>  
</div>
            