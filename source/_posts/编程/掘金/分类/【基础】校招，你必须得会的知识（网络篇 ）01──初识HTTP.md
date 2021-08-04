
---
title: '【基础】校招，你必须得会的知识（网络篇 ）01──初识HTTP'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa074ad4fcd4d6c97ae4a318ad3be48~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 06:31:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa074ad4fcd4d6c97ae4a318ad3be48~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">写在前面</h2>
<p>秋招已经开始，校招笔试面试环节经常考察《计算机网络》、《操作系统》、《数据库原理》等计算机基础知识，对于应届生而言这是必须掌握的技能。已经工作的伙伴在技术发展遇到瓶颈，不妨将基础再进行巩固，才能让自己走得更远。</p>
<h2 data-id="heading-1">初识HTTP</h2>
<h3 data-id="heading-2">HTTP协议</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa074ad4fcd4d6c97ae4a318ad3be48~tplv-k3u1fbpfcp-zoom-1.image" alt="浏览器的简易原理图" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>HTTP</strong>：超文本传输协议（HTTP）是一种通信协议，它允许将超文本标记语言文档从web服务器传送到客户端的浏览器。HTTP协议是构建在TCP/IP协议之上的，是TCP/IP协议的一个子集。</p>
<p><strong>TCP/IP族</strong>：TCP/IP协议是一系列与互联网相关联的协议集合的总成，分层管理是TCP/IP协议的重要特征。TCP/IP族通常由应用层、传输层、网络层以及数据链路层构成的系统。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29c2b99a035344e8b443749f7744f7ac~tplv-k3u1fbpfcp-zoom-1.image" alt="计算机网络的分层" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>应用层</strong>：应用层一般是编写的应用程序，决定向用户提供什么应用服务。可以通过系统调用与传输层进行通信，比如：FTP、DNS、HTTP等。</p>
<p><strong>传输层</strong>：传输层是通过系统调用向应用层提供处于网络连接中的两台计算机之间的数据传输功能。传输层具有两个不同性质的协议：TCP和UDP。<strong>TCP</strong>是面向连接的，可靠的，效率低。<strong>UDP</strong>是无连接的，可靠性低，效率高</p>
<p><strong>网络层</strong>：网络层是用于处理在网络上流动的数据包，而数据包是网络传输的最小数据单位。此层规定了通过什么路径（传输路线）到达对方对方计算机，并把数据包传输给对方。</p>
<p><strong>链路层</strong>：链路层用于处理连接网络的硬件部分，包括控制操作系统、硬件设备驱动、NIC网络适配器以及光纤等物理可见部分。硬件上的范畴均在链路层的作用范围内。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d564a0cac9e648c18b3365f3dd814819~tplv-k3u1fbpfcp-zoom-1.image" alt="数据包的封装过程" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">HTTP的传输过程</h3>
<p>在发送端发送数据时，数据会从上层传输到下层，且每经过一层都会被打上该层的头部信息。而接收端接收数据时，数据会从下层传输到上层，传输前会把下层的头部信息删除。</p>
<p>在下图中，当你想在浏览器查看某个页面时，会在应用层发起一个HTTP请求，通过传输层的TCP协议进行分割HTTP报文，并为每个报文打上标记序号、端口号等信息后发送到网络层。在网络层通过IP协议为每个报文增加作为通讯目的地的MAC地址，然后转发给链路层，接收端的服务器在链路层接收请求的HTTP数据。在服务器返回到浏览器的流程则是相反的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac533963d6a74864995c3f23ece2b429~tplv-k3u1fbpfcp-zoom-1.image" alt="HTTP数据传输过程" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">TCP的三次握手</h3>
<p>使用TCP协议进行通信的双方必须先建立连接，然后才能开始传输数据。为了确保连接双方的可靠性，在双方建立连接时，TCP协议会采用三次握手策略。</p>
<p><strong>第一次握手</strong>：客户端发送带有SYN标志的连接请求报文段，然后进入SYN_SEND状态，等待服务端的确认。</p>
<p><strong>第二次握手</strong>：服务端接受到客户端的SYN报文段后，需要发送ACK信息对这个SYN报文段进行确认，同时还要发送自己的SYN请求信息。服务端会将上述的信息放到一个报文段（SYN+ACK报文段）中，一并发送给客户端，此时服务端将会进入SYN_SEND状态。</p>
<p><strong>第三次握手</strong>：客户端接收到服务端的SYN+ACK报文段后，会向服务端发送ACK确认报文段，这个报文段发送完毕后，客户端和服务端都进入ESTABLISHED状态，完成TCP三次握手。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e255d8ca067e46c38ccbda0dd6dd92f0~tplv-k3u1fbpfcp-zoom-1.image" alt="客户端与服务端之间的三次握手" loading="lazy" referrerpolicy="no-referrer"></p>
<p>讲到这里，通常会有疑问：为什么TCP协议要进行三次握手而不是两次呢？</p>
<p>这是因为要建立可靠的通信，首先客户端和服务端都得确保对方具有完整的收发能力。<strong>第一次握手</strong>客户端发送请求报文给服务端，服务端可以确认客户端的发送能力是正常的以及服务端的接收能力是正常的；<strong>第二次握手</strong>客户端接收到服务端返回的报文信息，可以确认服务端的收发能力是正常的，同时客户端的收发能力是正常的；<strong>第三次握手</strong>客户端再次向服务端发送确认信息，此时服务端可以确认客户端的接收报文的能力和服务端的发送能力是正常。最后能够确认双方的收发能力是正常的，因此需要进行三次握手，而两次握手是不能彼此确认双方的收发能力是否正常。</p>
<h3 data-id="heading-5">DNS域名解析</h3>
<p>在上面的知识点中，我们知道与HTTP有着密切联系的TCP/IP协议，而DNS服务与HTTP协议也有着密不可分的关系。</p>
<p>比如说你要访问百度www.baidu.com，可以使用主机名100.100.10.10或者域名www.baidu.com进行访问，但是相比于一串纯数字的IP地址而言，使用域名更容易让人记住和访问。要知道在计算机网络中TCP/IP协议使用的就是IP地址进行访问，因此需要通过一种机制将域名转换为IP地址。而 DNS服务正是用于解决这个问题的，可以提供域名到IP地址之间的解析服务，其实就像我们打电话时查阅通讯录一样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5974ea09f5c4843a1414aa922508fd4~tplv-k3u1fbpfcp-zoom-1.image" alt="DNS域名解析过程" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图所示，当我们在浏览器输入www.baidu.com时，具体细节如下：</p>
<ul>
<li>① TCP/IP协议会先去访问本地域名解析器，当搜索到对应的IP地址则直接返回到客户端，客户端则直接向服务端发起HTTP请求；而当没有搜索到www.baidu.com对应的IP地址时，则向上溯源，查找上一级域名解析器</li>
<li>② TCP/IP协议访问根域名服务器搜索对应的IP地址，若同样的搜索通过则沿原路返回到客户端；若没有搜索到则继续溯源搜寻</li>
<li>③ TCP/IP协议一直溯源搜寻直至顶级域名服务器，搜寻沿原路返回，否则则告知客户端没有此域名</li>
</ul>
<h3 data-id="heading-6">HTTP事务处理过程</h3>
<p>当客户端访问WEB站点时，首先会用过DNS服务查询到域名对应的IP地址，返回到客户端生成HTTP请求，通过TCP/IP协议发送给WEB服务器。WEB服务器接收到请求后，会根据请求生成相应内容，并通过TCP/IP协议返回到客户端。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3016e643fc3d4e6eb00de291834f126b~tplv-k3u1fbpfcp-zoom-1.image" alt="HTTP事务处理过程" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">参考资料</h2>
<ul>
<li><a href="https://juejin.cn/post/6919755385330991112" target="_blank" title="https://juejin.cn/post/6919755385330991112">《超详细 DNS 协议解析》</a></li>
<li>《图解HTTP》</li>
<li>《计算机网络》</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoding.imooc.com%2Fclass%2F395.html%23Anchor" target="_blank" rel="nofollow noopener noreferrer" title="https://coding.imooc.com/class/395.html#Anchor" ref="nofollow noopener noreferrer">慕课网《编程必备基础－大话HTTP协议》</a></li>
</ul>
<h2 data-id="heading-8">写在最后</h2>
<p>我是前端小菜鸡，感谢大家的阅读，我将继续和大家分享更多优秀的文章，此文参考了大量书籍和文章，如果有错误和纰漏，希望能给予指正。校招需要内推的可以私信我。</p>
<p>更多最新文章敬请关注笔者掘金账号<a href="https://juejin.cn/user/2972687627730765" target="_blank" title="https://juejin.cn/user/2972687627730765"><strong>一川萤火</strong></a>和公众号<strong>前端万有引力</strong>。</p></div>  
</div>
            