
---
title: '关于Websocket的两次实践（Vue项目实现在线聊天&Angular项目首页实时推送图表数据）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5395'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 17:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5395'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>摘要：该文章记录了我使用websocket的两次实践经历，在第一次实践过程中，踩了很多坑。第二次实践，可谓得心应手，但是很多理论性还很欠缺。通过该文章，从理论到实践，一举全部拿下。</p>
<p><strong>目录</strong></p>
<p><a href="https://juejin.cn/post/6985328447346180132#%E4%B8%80%E3%80%81Websocket%E7%90%86%E8%AE%BA" target="_blank" title="#%E4%B8%80%E3%80%81Websocket%E7%90%86%E8%AE%BA">一、Websocket理论</a></p>
<p><a href="https://juejin.cn/post/6985328447346180132#%EF%BC%881%EF%BC%89Websocket%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F" target="_blank" title="#%EF%BC%881%EF%BC%89Websocket%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F">（1）Websocket是什么？</a></p>
<p><a href="https://juejin.cn/post/6985328447346180132#%EF%BC%882%EF%BC%89Websocket%E5%87%BA%E7%8E%B0%E7%9A%84%E8%83%8C%E6%99%AF%EF%BC%9F" target="_blank" title="#%EF%BC%882%EF%BC%89Websocket%E5%87%BA%E7%8E%B0%E7%9A%84%E8%83%8C%E6%99%AF%EF%BC%9F">（2）Websocket出现的背景？</a></p>
<p><a href="https://juejin.cn/post/6985328447346180132#%EF%BC%883%EF%BC%89%E9%87%87%E7%94%A8%E8%AF%A5%E5%8D%8F%E8%AE%AE%E7%9A%84%E4%BC%98%E5%8A%BF%EF%BC%9F" target="_blank" title="#%EF%BC%883%EF%BC%89%E9%87%87%E7%94%A8%E8%AF%A5%E5%8D%8F%E8%AE%AE%E7%9A%84%E4%BC%98%E5%8A%BF%EF%BC%9F">（3）采用该协议的优势？</a></p>
<p><a href="https://juejin.cn/post/6985328447346180132#%EF%BC%884%EF%BC%89%E6%8F%A1%E6%89%8B%E5%8D%8F%E8%AE%AE" target="_blank" title="#%EF%BC%884%EF%BC%89%E6%8F%A1%E6%89%8B%E5%8D%8F%E8%AE%AE">（4）握手协议</a></p>
<p><a href="https://juejin.cn/post/6985328447346180132#%EF%BC%885%EF%BC%89Websocket%E5%92%8CSocket%E7%9A%84%E5%8C%BA%E5%88%AB%EF%BC%9F" target="_blank" title="#%EF%BC%885%EF%BC%89Websocket%E5%92%8CSocket%E7%9A%84%E5%8C%BA%E5%88%AB%EF%BC%9F">（5）Websocket和Socket的区别？</a></p>
<p><a href="https://juejin.cn/post/6985328447346180132#%EF%BC%886%EF%BC%89%E5%85%B3%E4%BA%8Esocket.io" target="_blank" title="#%EF%BC%886%EF%BC%89%E5%85%B3%E4%BA%8Esocket.io">（6）关于socket.io</a></p>
<p><a href="https://juejin.cn/post/6985328447346180132#%E4%BA%8C%E3%80%81Vue%E5%AE%9E%E7%8E%B0%E5%9C%A8%E7%BA%BF%E8%81%8A%E5%A4%A9%EF%BC%88%E5%AE%9E%E8%B7%B5%E4%B8%8E%E8%B8%A9%E5%9D%91%EF%BC%89" target="_blank" title="#%E4%BA%8C%E3%80%81Vue%E5%AE%9E%E7%8E%B0%E5%9C%A8%E7%BA%BF%E8%81%8A%E5%A4%A9%EF%BC%88%E5%AE%9E%E8%B7%B5%E4%B8%8E%E8%B8%A9%E5%9D%91%EF%BC%89">二、Vue实现在线聊天（实践与踩坑）</a></p>
<p><a href="https://juejin.cn/post/6985328447346180132#%E4%B8%89%E3%80%81Angular%E9%A1%B9%E7%9B%AE%E9%A6%96%E9%A1%B5%E5%AE%9E%E6%97%B6%E6%8E%A8%E9%80%81%E5%9B%BE%E8%A1%A8%E6%95%B0%E6%8D%AE" target="_blank" title="#%E4%B8%89%E3%80%81Angular%E9%A1%B9%E7%9B%AE%E9%A6%96%E9%A1%B5%E5%AE%9E%E6%97%B6%E6%8E%A8%E9%80%81%E5%9B%BE%E8%A1%A8%E6%95%B0%E6%8D%AE">三、Angular项目首页实时推送图表数据</a></p>
<hr>
<h2 data-id="heading-0">一、Websocket理论</h2>
<h3 data-id="heading-1">（1）Websocket是什么？</h3>
<p>Websocket是一种网络通信协议，是一种在单个TCP连接上的全双工通信协议。</p>
<p>WebSocket使得客户端和服务器之间的数据交换变得更加简单，允许服务端主动向客户端推送数据。在WebSocket API中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，并进行双向数据传输。</p>
<p><strong>全双工通信</strong>：又称为双向同时通信，即通信的双方可以同时发送和接收信息的信息交互方式。</p>
<p>关于通信协议的分类，该文章图文并茂，介绍很详细：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FDingjiawang6%2Farticle%2Fdetails%2F81093518" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/Dingjiawang6/article/details/81093518" ref="nofollow noopener noreferrer">blog.csdn.net/Dingjiawang…</a></p>
<h3 data-id="heading-2">（2）Websocket出现的背景？</h3>
<p>很多网站为了实现<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E6%258E%25A8%25E9%2580%2581%25E6%258A%2580%25E6%259C%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E6%8E%A8%E9%80%81%E6%8A%80%E6%9C%AF" ref="nofollow noopener noreferrer">推送技术</a>，所用的技术都是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E8%25BD%25AE%25E8%25AF%25A2" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E8%BD%AE%E8%AF%A2" ref="nofollow noopener noreferrer">轮询</a>。轮询是在特定的的时间间隔（如每1秒），由浏览器对服务器发出<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2FHTTP%25E8%25AF%25B7%25E6%25B1%2582%2F10882159" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/HTTP%E8%AF%B7%E6%B1%82/10882159" ref="nofollow noopener noreferrer">HTTP请求</a>，然后由服务器返回最新的数据给客户端的浏览器。这种传统的模式带来很明显的缺点，即浏览器需要不断的向服务器发出请求，然而HTTP请求可能包含较长的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%25A4%25B4%25E9%2583%25A8" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%A4%B4%E9%83%A8" ref="nofollow noopener noreferrer">头部</a>，其中真正有效的数据可能只是很小的一部分，显然这样会浪费很多的带宽等资源。</p>
<p>而比较新的技术去做轮询的效果是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2FComet" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/Comet" ref="nofollow noopener noreferrer">Comet</a>。这种技术虽然可以双向通信，但依然需要反复发出请求。而且在Comet中，普遍采用的长链接，也会消耗服务器资源。</p>
<p>在这种情况下，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2FHTML5" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/HTML5" ref="nofollow noopener noreferrer">HTML5</a>定义了WebSocket协议，能更好的节省服务器资源和带宽，并且能够更实时地进行通讯。</p>
<h3 data-id="heading-3">（3）采用该协议的优势？</h3>
<ul>
<li>较少的控制开销。在连接创建后，服务器和客户端之间交换数据时，用于协议控制的数据包头部相对较小。在不包含扩展的情况下，对于服务器到客户端的内容，此头部大小只有2至10<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%25AD%2597%25E8%258A%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%AD%97%E8%8A%82" ref="nofollow noopener noreferrer">字节</a>（和数据包长度有关）；对于客户端到服务器的内容，此头部还需要加上额外的4字节的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E6%258E%25A9%25E7%25A0%2581" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E6%8E%A9%E7%A0%81" ref="nofollow noopener noreferrer">掩码</a>。相对于HTTP请求每次都要携带完整的头部，此项开销显著减少了。</li>
<li>更强的实时性。由于协议是全双工的，所以服务器可以随时主动给客户端下发数据。相对于HTTP请求需要等待客户端发起请求服务端才能响应，延迟明显更少；即使是和Comet等类似的长轮询比较，其也能在短时间内更多次地传递数据。</li>
<li>保持连接状态。与HTTP不同的是，Websocket需要先创建连接，这就使得其成为一种有状态的协议，之后通信时可以省略部分状态信息。而HTTP请求可能需要在每个请求都携带状态信息（如身份认证等）。</li>
<li>更好的二进制支持。Websocket定义了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E4%25BA%258C%25E8%25BF%259B%25E5%2588%25B6" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E4%BA%8C%E8%BF%9B%E5%88%B6" ref="nofollow noopener noreferrer">二进制</a>帧，相对HTTP，可以更轻松地处理二进制内容。</li>
<li>可以支持扩展。Websocket定义了扩展，用户可以扩展协议、实现部分自定义的子协议。如部分浏览器支持<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%258E%258B%25E7%25BC%25A9" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%8E%8B%E7%BC%A9" ref="nofollow noopener noreferrer">压缩</a>等。</li>
<li>更好的压缩效果。相对于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2FHTTP%25E5%258E%258B%25E7%25BC%25A9" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/HTTP%E5%8E%8B%E7%BC%A9" ref="nofollow noopener noreferrer">HTTP压缩</a>，Websocket在适当的扩展支持下，可以沿用之前内容的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E4%25B8%258A%25E4%25B8%258B%25E6%2596%2587" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E4%B8%8A%E4%B8%8B%E6%96%87" ref="nofollow noopener noreferrer">上下文</a>，在传递类似的数据时，可以显著地提高压缩率。</li>
</ul>
<h3 data-id="heading-4">（4）握手协议</h3>
<p><strong>WebSocket同HTTP一样也是应用层的协议，但是它是一种双向通信协议，是建立在TCP之上的。</strong></p>
<p>Websocket 通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2FHTTP" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/HTTP" ref="nofollow noopener noreferrer">HTTP</a>/1.1 协议的101状态码进行握手。</p>
<p>为了创建Websocket连接，需要通过浏览器发出请求，之后服务器进行回应，这个过程通常称为“<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E6%258F%25A1%25E6%2589%258B" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E6%8F%A1%E6%89%8B" ref="nofollow noopener noreferrer">握手</a>”（handshaking）。</p>
<p><strong>握手过程：</strong></p>
<p>1. 浏览器、服务器建立TCP连接，三次握手。这是通信的基础，传输控制层，若失败后续都不执行。<br>
2. TCP连接成功后，浏览器通过HTTP协议向服务器传送WebSocket支持的版本号等信息。（开始前的HTTP握手）<br>
3. 服务器收到客户端的握手请求后，同样采用HTTP协议回馈数据。<br>
4. 当收到了连接成功的消息后，通过TCP通道进行传输通信。</p>
<h3 data-id="heading-5">（5）Websocket和Socket的区别？</h3>
<p>Socket是TCP、IP网络的API，是为了方便使用TCP或UDP而抽象出来的一层，位于应用层和传输层之间的一组接口，而Websocket是一个典型的应用层协议。</p>
<h3 data-id="heading-6">（6）关于socket.io</h3>
<p>Socket.IO是node.js的一个模块，它是通过WebSocket进行通信的一种简单方式。WebSocket协议很复杂，从头开始写一个支持WebSocket的应用程序将需要花费很多时间。Socket.IO提供服务器和客户端双方的组件，所以只需一个模块就可以给应用程序加入对WebSocket的支持。Socket.IO也解决了各浏览器的支持问题（不是所有浏览器都支持WebSocket）并让实时通信可以跨几乎所有常用的浏览器实现。Socket.IO的设计非常好，将实时通信带入应用程序的过程便得非常简单。如果想做任何涉及在web服务器和浏览器之间通信的事情，那么nodejs和Socket.IO是极好的选择哦！</p>
<pre><code class="copyable"># npm安装socket.op
$ npm install --save socket.io
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">二、Vue实现在线聊天（实践与踩坑）</h2>
<p><strong>需求</strong>：在后台管理系统中加入售后服务人员与客户的在线聊天功能。</p>
<p><strong>框架</strong>：Vue</p>
<p><strong>实践第一步</strong>：连接websocket及携带token</p>
<p>连接websocket 的方式我所接触过的包括原生方式，代码如下：</p>
<pre><code class="copyable">`initWebSocket () &#123;
    // 初始化websocket
    const wsuri = 'wss://XXXXXXXXXXXXXX/ws/adminOnlineService'
    this.websock = new WebSocket(wsuri)
&#125;,`
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>踩坑一</strong>：对于我的项目而言，这样连接报错500，原因是没有携带token，该方式携带token的方式我所了解的如下：<br>
（1）send发送参数，这种方式的劣势为每次发送消息，都会重新连接一次websocket；<br>
（2）请求地址中带参数，如：var  wss = new WebSocket("wss://" + url?token + "/webSocketServer");<br>
（3）基于协议头：this.websock = new WebSocket(wsuri, ['Bearer' + store.state.token])；<br>
经历了一番尝试之后，我认为无论采用哪种方式，都需要跟服务端协商，即前端传什么样的类型，后端应采用相应的处理方式，不要轻易否定任何一种方式，这是一个尝试的过程。之所以这样说，是因为前端尝试了很多种方式，最终决定放在请求地址中，此时服务端做相应的处理。<br>
连接websocket的另一种方式是使用socket.io-client</p>
<pre><code class="copyable">`onConnect: () => &#123;
      console.log('connect')
      this.message = 'connect'
    &#125;,
    onDisconnect: () => &#123;
      console.log('disconnect')
      this.message = 'disconnect'
    &#125;,
    connect: () => &#123;
      let socket = io('wss://XXXXXXXXXXX', &#123;
        path: '/welfare/ws/adminOnlineService',
        query: &#123;
          'Authorization': 'Bearer  abdadfssadfasdf'
        &#125;
      &#125;)
      socket.connect()
&#125;`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在请求的时候会带上token，但是同样token会拼在url中，需要服务端进一步做处理。该方式连接成功，但是遇到的问题是在连接成功之后，会断连，之后会立马连接，如此循环，直到刷新页面为止。该问题当时没有解决。但是原生方式没有存在该问题，连接一次即可。</p>
<p><strong>实践第二步</strong>：在点击登录按钮时就进行websocket的连接</p>
<p>点击登录按钮即连接websocket，要求定义全局方法，当时采用的是vuex。虽然时间过去很久了，并且现在看来并不需要采用这种方案，但是再来回顾下当时的实现思路吧。</p>
<p> 在vuex的modules下新建了websocket.js文件，其中的代码如下所示：</p>
<pre><code class="copyable">import store from './user'
const state = &#123;
  websock: null
&#125;

const mutations = &#123;
  STAFF_UPDATEWEBSOCKET (state, websock) &#123;
    state.websock = websock
  &#125;
  // STAFF_SEND (state, text) &#123;
  //   state.websock.send(text)
  // &#125;
&#125;

// 实现websocket的连接，需要携带参数token
const actions = &#123;
  // 用到 ES2015 的参数解构来简化代码（特别是我们需要调用 commit 很多次的时候）
  STAFF_WEBSOCKET (&#123; commit &#125;) &#123;
    let token = encodeURI('Bearer ' + store.state.token)
    const wsuri = 'wss://XXXXXXXXX/?Authorization=' + token + '&EIO=3&transport=websocket'
    commit('STAFF_UPDATEWEBSOCKET', new WebSocket(wsuri))
    // 只有定义了onopen方法，才能继续实现接收消息，即在使用的地方调用onmessage方法。
    state.websock.onopen = function () &#123;
    &#125;
    // 心跳包，30s左右无数据浏览器会断开连接Heartbeat
    setInterval(function () &#123;
      state.websock.send(JSON.stringify(&#123;
        'heart': true
      &#125;))
    &#125;, 30000)
  &#125;
&#125;

// 该部分为了获取websocket的相关方法。会发现此处跟mutations 里的写法是类似的，但是，想使用return，需要将相关数据写在getters里面。
const getters = &#123;
  STAFF_UPDATE (state) &#123;
    return state.websock
  &#125;
&#125;
export default &#123;
  state,
  mutations,
  actions,
  getters
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 相关代码注释在上述代码中已经有了体现，使用方法在下面的代码中：</p>
<p>1.调用websocket的send方法，即点击发送的时候，会调用send方法，将消息发送给服务端，下述代码是针对不同的定义方式，所采取的不同方法，比如，第三个方法是取得getters中的；第二个方法是取得mutations中的注释的STAFF_SEND中的方法；第一个是取得actions中定义的方法。</p>
<p>乍一眼看上去感觉多此一举，我们直接分发 mutation 岂不更方便？实际上并非如此，还记得 mutation 必须同步执行这个限制么？Action 就不受约束！我们可以在 action 内部执行异步操作</p>
<pre><code class="copyable">// Action 通过 store.dispatch 方法触发
this.$store.dispatch('STAFF_WEBSOCKET')
// this.$store.commit('STAFF_SEND').send('这是来自客户端的消息')
this.$store.getters.STAFF_UPDATE.send('sdfsfs')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Actions 支持同样的载荷方式和对象方式进行分发：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 以载荷形式分发</span>
store.dispatch(<span class="hljs-string">'incrementAsync'</span>, &#123;
  <span class="hljs-attr">amount</span>: <span class="hljs-number">10</span>
&#125;)

<span class="hljs-comment">// 以对象形式分发</span>
store.dispatch(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'incrementAsync'</span>,
  <span class="hljs-attr">amount</span>: <span class="hljs-number">10</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 2.通过websocket实现接收来自服务端的消息，实现方式如下代码：</p>
<pre><code class="copyable">onmessage () &#123;
  let that = this
  this.$store.getters.STAFF_UPDATE.onmessage = function (evt) &#123;
  let message = JSON.parse(evt.data)
  that.messages.push(&#123;
     content: message.content,
     self: false
  &#125;)
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关键是从getters中获取onmessage方法，上面强调过了，在调用该方法之前需要实现onopen方法。</p>
<p>如上，就可以实现聊天了。</p>
<p><strong>实践第三步</strong>：websocket的事件和方法</p>
<pre><code class="copyable">//实例化一个WebSocket对象，并传入要连接的决定URL
var socket = new WebSocket("url");//    url中要使用ws://来代替http:// ;使用wss来代替https://
//当成功建立连接时会触发open事件
socket.onopen = function()&#123;
    alert("established");
&#125;
//当发生错误时会触发error事件
socket.onerror = function()&#123;
    alert("error!");
&#125;
//当连接关闭时会触发close事件
socket.onclose = function()&#123;
    alert("closed!");
&#125;
//使用send() 方法发送数据 只能接受字符串 json对象要先序列化成json字符串
socket.send(str);
//当服务端像客户端发来消息，WebSocket对象就会触发message事件
socket.onmessage = function(event)&#123;
    console.log(event.data);//返回的数据 也为字符串形式
&#125;
//调用close()方法 会关闭Web Sockets连接，可在任何时候调用close（）方法
 socket.close();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">三、Angular项目首页实时推送图表数据</h2>
<p>在上述Websocket出现背景的地方，介绍了Websocket出现的原因。其实想来，这也是在该项目中，该需求使用该方案的原因。接触的其他项目中，页面中也会有实时刷新，会在每隔一段时间后，请求近10个接口。 在本次需求中，数据量更大，请求接口量更多，采用了该方式。</p>
<p>下面是实现代码，其实使用过程都是一样的，主要看业务逻辑。</p>
<pre><code class="copyable">initWebSocket() &#123;
    const url = '*******';
    const ws = new WebSocket(url);

    ws.onopen = () => &#123;
      this.clearWS();
      this.ws = ws;
      ws.onmessage = evt => &#123;
        // 下述是业务逻辑
        const data = JSON.parse(evt.data);
        if (this.simpleMode) &#123;
          this.reciveFromWs4Simple(data);
        &#125; else &#123;
          this.reciveFromWs(data);
        &#125;
      &#125;;
      ws.onclose = () => &#123;
        this.clearWS();
      &#125;;
      ws.onerror = () => &#123;
        this.clearWS();
      &#125;;
    &#125;;
  &#125;
   /**
   * 清除引用, 事件
   */
  private clearWS() &#123;
    const ws: WebSocket = this.ws;
    if (ws) &#123;
      ws.onclose = null;
      ws.onopen = null;
      ws.onmessage = null;
    &#125;
    this.ws = null;
  &#125;
  /**
   * 改成心跳监测连接是否断开的逻辑. 每隔10秒检查一次
   */
  private heartbeat() &#123;
    this.reConnectTimer = window.setInterval(() => &#123;
      const ws: WebSocket | null = this.ws;
      if (!this.isWSAvailable(ws)) &#123;
        this.reConnect();
      &#125;
    &#125;, 10000);
  &#125;
   /**
   * 做个重连， 用close和error做个伪重连
   */
  private reConnect() &#123;
    console.warn('reconnect');
    this.clearWS();
    this.initWebSocket();
  &#125;
sendByWs(data) &#123;
    const ws = this.ws;
    if (!ws) &#123;
      console.warn('[ws-发送数据失败]: Websocket 还没准备好或已断开');
      return;
    &#125;

    switch (ws.readyState) &#123;
      case WebSocket.CONNECTING:
        console.warn('[ws-发送数据失败]: Websocket 正在连接中...');
        break;
      case WebSocket.OPEN:
        ws.send(JSON.stringify(data));
        break;
      default:
        console.warn('[ws-发送数据失败]: Websocket 即将断开或已经断开');
    &#125;
  &#125;

  switchLive(live) &#123;
    this.live = live;
    const name = 'live';
    this.sendByWs(&#123; name, live &#125;);
  &#125;
ngOnDestroy() &#123;
    this.ws && this.ws.close(1000, '用户已经离开当前页面或页面发生刷新');
    this.reConnectTimer && clearInterval(this.reConnectTimer);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            