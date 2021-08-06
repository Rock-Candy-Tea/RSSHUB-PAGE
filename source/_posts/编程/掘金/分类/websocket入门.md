
---
title: 'websocket入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=900'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 00:31:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=900'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">websocket是什么</h2>
<p>答: 它是一种网络通信协议，是HTML5开始提供的一种在单个 TCP 连接上进行全双工通讯的协议。</p>
<h3 data-id="heading-1">为什么需要websocket? 疑问? 我们已经有了 HTTP 协议，为什么还需要另一个协议？它能带来什么好处？</h3>
<ul>
<li>因为 HTTP 协议有一个缺陷：通信只能由客户端发起</li>
<li>我们都知道轮询的效率低，非常浪费资源（因为必须不停连接，或者 HTTP 连接始终打开）, 因此websocket应运而生。</li>
</ul>
<p>WebSocket目前支持两种统一资源标志符ws和wss，类似于HTTP和HTTPS。</p>
<p>通过get可以表明此次连接的建立是以HTTP协议为基础的，返回101状态码。</p>
<p>如果不是101状态码，表示握手升级的过程失败了</p>
<p>101是Switching Protocols,表示服务器已经理解了客户端的请求，并将通过Upgrade 消息头通知客户端采用不同的协议来完成这个请求。在发送这个响应后的空档，将http升级到webSocket。</p>
<p>其中Upgrade和Connection字段告诉服务端，发起的是webSocket协议</p>
<p>Sec-WebSocket-Key是浏览器经过Base64加密后的密钥，用来和response里面的Sec-WebSocket-Accept进行比对验证</p>
<p>Sec-WebSocket-Version是当前的协议版本</p>
<p>Sec-WebSocket-Extensions是对WebSocket的协议扩展</p>
<h2 data-id="heading-2">客户端的简单示例</h2>
<pre><code class="copyable">//以下 API 用于创建 WebSocket 对象
var ws = new WebSocket("wss://echo.websocket.org");

ws.onopen = function(evt) &#123; 
  console.log("Connection open ..."); 
  ws.send("Hello WebSockets!");
&#125;;

ws.onmessage = function(evt) &#123;
  console.log( "Received Message: " + evt.data);
  ws.close();
&#125;;

ws.onclose = function(evt) &#123;
  console.log("Connection closed.");
&#125;; 

ws.onerror = function(evt) &#123;
  console.log("error!!!"); 
&#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">websocket 属性</h2>
<p>ws.readyState</p>
<p>CONNECTING：值为0，表示正在连接。</p>
<p>OPEN：值为1，表示连接成功，可以通信了。</p>
<p>CLOSING：值为2，表示连接正在关闭。</p>
<p>CLOSED：值为3，表示连接已经关闭，或者打开连接失败。</p>
<p>ws.bufferedAmount</p>
<p>只读属性 bufferedAmount 已被 send() 放入正在队列中等待传输，但是还没有发出的 UTF-8 文本字节数。</p>
<h2 data-id="heading-4">WebSocket 事件</h2>
<pre><code class="copyable">事件       事件处理程      描述
open     ws.onopen      连接建立时触发
message  ws.onmessage   客户端接收服务端数据时触发
error    ws.onerror     通信发生错误时触发
close    ws.onclose     连接关闭时触发
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">websocket 方法</h2>
<p>方法 描述</p>
<p>ws.send() 使用连接发送数据</p>
<p>ws.close() 关闭链接</p></div>  
</div>
            