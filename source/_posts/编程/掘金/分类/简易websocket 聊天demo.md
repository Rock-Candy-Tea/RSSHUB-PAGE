
---
title: '简易websocket 聊天demo'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5890'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 01:39:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=5890'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这两天在看websocket 的东西，于是跟着视频写了个简单的双向通信的聊天小案例,服务气端口用的是 nodemon 工具来来监听端口将js文件作为服务来启动，前端可以使用各种构建工具，例如webpack,rollup,vite 来启动服务，但由于这些工具都是用来打包项目的，我这边只是一个小案例用他们显得有些大材小用了，也可以使用nodemon 来启动文件作为静态服务器，但是为了多学多用，就用了 live-server.
node的这两个库使用方法大同小异，就是使用该命令来监听制定目录下文件的变动。</p>
<pre><code class="copyable">    live-server ./ --port=8888
    nodemon ./index.js --port = 9999
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-0">基本概念</h5>
<pre><code class="copyable">先总结下websocket 基本概念
服务器端: 服务器端主要是各个客户端传输过来的消息的分发，即(收集各个客户端发的消息，再广播给各个客户端);
客户端：客户端连接服务端的websocket服务器，然后发送消息给服务器
主要api有:
1.open
2.message
3.error
4.message
服务气短相比客户端api
1.open
2.close
3.error
4.connection  -> message
5.connection 调用message 方法，调用 websocket 的clients 方法获取所有链接到该服务器的客户端，然后将接收到的消息通过，客户端.send()，广发给所有客户端
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体代码如下：
index.js:</p>
<pre><code class="copyable">/*
 * @Author: wwt
 * @Date: 2021-07-12 11:08:27
 * @LastEditors: wwt
 * @LastEditTime: 2021-07-12 13:35:33
 * @Description: file content
 */

(function(storage,doc)&#123;
    const userName = doc.querySelector('#username');
    const btn = document.querySelector('#enter');
    
    const init = ()=>&#123;
  bindEvent();
    &#125;

    const bindEvent = ()=>&#123;
  btn.addEventListener('click',handleEnter,false);
    &#125;

    const handleEnter = ()=>&#123;
  const userNameVal = userName.value.trim();

  if(!userNameVal)&#123;
window.alert('请输入用户名！')
  &#125;

  storage.setItem('userName',userNameVal);
  location.href = '../chat.html';
    &#125;

    init();
&#125;)(localStorage,document)
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>server.js</p>
<pre><code class="copyable">/*
 * @Author: wwt
 * @Date: 2021-07-12 13:50:45
 * @LastEditors: wwt
 * @LastEditTime: 2021-07-12 16:22:11
 * @Description: file content
 */

const ws = require('ws');

(function () &#123;
    const server = new ws.Server(&#123; port: 8000 &#125;); //可抽离成配置文件

    const init = ()=> &#123;
  bindEvent();
    &#125;

    const bindEvent = () =>&#123;
  server.on('open',handleOpen);
  server.on('close',handleClose);
  server.on('error',handleError);
  server.on('connection',handleConnection);
    &#125;

    const handleOpen = ()=>&#123;
  console.log('server --- ws open');
    &#125;

    const handleClose = ()=>&#123;
  console.log('server --- ws close');
    &#125;

    const handleError = ()=>&#123;
  console.log('server --- ws error');
    &#125;

    const handleConnection = (ws)=>&#123;
  ws.on('message',handleMsg);
    &#125;

    const handleMsg = (msg)=>&#123;
  console.log(msg,'server ==== msg');
  server.clients.forEach(c=>&#123;
c.send(msg); // 发给所有客户端
  &#125;)
    &#125;

    init();

&#125;)(ws)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>chat.js</p>
<pre><code class="copyable">/*
 * @Author: wwt
 * @Date: 2021-07-12 13:36:50
 * @LastEditors: wwt
 * @LastEditTime: 2021-07-13 08:56:42
 * @Description: file content
 */

 (function(doc,storage)&#123;

    const sendBtn = doc.querySelector('#sendBtn');
    const inputMsg = doc.querySelector('#inputMsg');
    const msgList = doc.querySelector('#msgList');
    const ws = new WebSocket("ws:10.28.56.81:8000");
    let userName = '';


   

    const init = () =>&#123;
  bindEvent();
    &#125;

    const bindEvent = ()=>&#123;
  sendBtn.addEventListener('click',sendMsg,false);
  ws.addEventListener('open',handleOpen,false);
  ws.addEventListener('close',handleClose,false);
  ws.addEventListener('error',handleError,false);
  ws.addEventListener('message',handleMessage,false);
    &#125;

    const sendMsg = ()=>&#123;
  const msg = inputMsg.value.trim();
  if(!msg)&#123;return&#125;
  //TODO
  let data = &#123;
user:userName,
time:new Date(),
message:msg,
  &#125;
  ws.send(JSON.stringify(data));

  inputMsg.value = '';
  

    &#125;

    const handleOpen = ()=>&#123;
  userName = storage.getItem('userName');
  //用户名不存在直接去入口页面
  if(!userName)&#123;
location.href = '../index.html';
return;
  &#125;
  console.log('ws open11---');
    &#125;

    const handleClose = ()=>&#123;
  console.log('ws closed---');
    &#125;
    const handleError = ()=>&#123;
  console.log('ws error--');
    &#125;
    const handleMessage = (e)=>&#123;
  console.log(e.data,'server 发回来的message');
  const msgData = JSON.parse(e.data);
  msgList.appendChild(createMsg(msgData));
    &#125;

    const createMsg = (data)=>&#123;
  const &#123;user,time,message&#125; = data;
  const item = doc.createElement('div');
  item.innerHTML = `
<p>
    <span>$&#123;user&#125;</span>
    <i>$&#123;time&#125;</i>
</p>
<p>消息: $&#123;message&#125;</p>
  `
  return item;
    &#125;

    init();

&#125;)(document,localStorage)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后续继续完善，看是否能够发送二进制图片，语音等信息！</p></div>  
</div>
            