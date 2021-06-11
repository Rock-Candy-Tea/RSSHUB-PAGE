
---
title: 'socket 通信'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5019'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 17:32:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=5019'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">socket 通信</h2>
<p><strong>net模块</strong></p>
<p>serverCode</p>
<pre><code class="copyable">const net = require('net')

const server = new net.createServer()

let clients = &#123;&#125;
let clientName = 0

server.on('connection', (client) => &#123;
  client.name = ++clientName
  clients[client.name] = client

  client.on('data', (msg) => &#123;
    // console.log('客户端传来：' + msg);
    broadcast(client, msg.toString())
  &#125;)

  client.on('error', (e) => &#123;
    console.log('client error' + e);
    client.end()
  &#125;)

  client.on('close', (data) => &#123;
    delete clients[client.name]
    console.log(client.name + ' 下线了');
  &#125;)
&#125;)

function broadcast(client, msg) &#123;
  for (var key in clients) &#123;
    clients[key].write(client.name + ' 说：' + msg)
  &#125;
&#125;

server.listen(9000)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>clientCode</p>
<pre><code class="copyable">
var net = require('net')
const readline = require('readline')

var port = 9000
var host = '127.0.0.1'

var socket = new net.Socket()

socket.setEncoding = 'UTF-8'

socket.connect(port, host, () => &#123;
  socket.write('hello.')
&#125;)

socket.on('data', (msg) => &#123;
  console.log(msg.toString())
  say()
&#125;)

socket.on('error', function (err) &#123;
  console.log('error' + err);
&#125;)

socket.on('close', function () &#123;
  console.log('connection closeed');
&#125;)

const r1 = readline.createInterface(&#123;
  input: process.stdin,
  output: process.stdout
&#125;)

function say() &#123;
  r1.question('请输入：', (inputMsg) => &#123;
    if (inputMsg != 'bye') &#123;
      socket.write(inputMsg + '\n')
    &#125; else &#123;
      socket.destroy()
      r1.close()
    &#125;
  &#125;)
&#125;



<span class="copy-code-btn">复制代码</span></code></pre>
<p>websocket</p>
<pre><code class="copyable">
const ws = new WebSocket('ws://localhost:8080/')

ws.onopen = () => &#123;
  ws.send('大家好')
&#125;

ws.onmessage = (msg) => &#123;
  const content = document.getElementById('content')
  content.innerHTML += msg.data + '<br/>'
&#125;

ws.onerror = (err) => &#123;
  console.log(err);
&#125;

ws.onclose = () => &#123;
  console.log('closed~');
&#125;
ws.send(msg2)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>server.js</p>
<pre><code class="copyable">const WebSocket = require('ws')
const ws = new WebSocket.Server(&#123; port: 8080 &#125;)

let clients = &#123;&#125;
let clientName = 0

ws.on('connection', (client) => &#123;
  client.name = ++clientName
  clients[client.name] = client

  client.on('message', (msg) => &#123;
    broadcast(client, msg)
  &#125;)

  client.on('close', () => &#123;
    delete clients[client.name]
    console.log(client.name + ' 离开了~')
  &#125;)
&#125;)

function broadcast(client, msg) &#123;
  for (var key in clients) &#123;
    clients[key].send(client.name + ' 说：' + msg)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>socket.io</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>socket.io</title>
  <script src="socket.io.js" charset="utf-8"></script>
</head>
<body>
  <h1>gp6 交流区</h1>
  <div id="content" name="name" style="overflow-y: scroll; width: 400px; height: 300px; border: solid 1px #000"></div>
  <br />
  <div>
    <input type="text" id="msg" style="width: 200px;">
  </div>
  <button id="submit">提交</button>
  <script>
    var socket = io.connect('http://10.9.164.98:8081');
    const content = document.getElementById('content')
    document.querySelector('#submit')
      .addEventListener('click', function () &#123;
        var msg2 = msg.value
        socket.emit('receive', msg2)
        msg.value = ''
        content.innerHTML += msg2 + '<br/>'
      &#125;, false)

      socket.on('message', function(msg)&#123;
        content.innerHTML += msg + '<br/>'
      &#125;)
  </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>server.js</em></p>
<pre><code class="copyable">var express = require('express');
var app = express();
var server = require('http').Server(app);
var io = require('socket.io')(server);

app.use(express.static(__dirname + '/client'))

io.on('connection', function (socket) &#123;
  setInterval(function () &#123;
    socket.emit('list', 'abc')
  &#125;, 1000)
  socket.broadcast.emit('list', 'test');
  socket.on('backend', (msg) => &#123;
    console.log(msg);
  &#125;)

  socket.on('receive', (msg) => &#123;
    socket.broadcast.emit('message', msg);
  &#125;)
&#125;);

server.listen(8081, '10.9.164.98');
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            