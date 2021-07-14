
---
title: 'Http学习篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f51859cfde59412fb4afc09159de7547~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 01:09:20 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f51859cfde59412fb4afc09159de7547~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">学习资料链接</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffebobo%2Fweb-interview" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/febobo/web-interview" ref="nofollow noopener noreferrer">HTTP面试篇</a></p>
<h1 data-id="heading-1">1.http请求头和响应头里有哪些参数</h1>
<h2 data-id="heading-2">Request Headers</h2>
<ul>
<li>Accept:  客户端能接收的资源类型</li>
<li>Accept-language: 客户端能接收的语言类型</li>
<li>Accept-Encoding: 客户端能接收的压缩数据类型</li>
<li>connection: 客户端和服务端的连接关系</li>
<li>Host： 目标主机和端口号(用于虚拟主机）</li>
<li>User-Agent: 客户端版本号名字</li>
<li>Cookie： 客户端暂存服务端的信息</li>
<li>Date: 客户端请求服务端的时间</li>
</ul>
<h2 data-id="heading-3">Response Headers</h2>
<ul>
<li>Connection: 客户端和服务端保持的连接关系</li>
<li>Content-Encoding: 服务端压缩编码类型</li>
<li>Content-Type: 资源类型 application/json;charset=utf-8 ; text/css; application/javascript;</li>
<li>Content-Length: 压缩数据的长度</li>
<li>Cache-Control</li>
<li>Last-Modified: 上次修改时间</li>
<li>Etag: 上次修改时间</li>
<li>Access-Control-Allow-Credentials</li>
<li>Access-Control-Allow-Origin</li>
<li>Access-Control-Allow-Methids</li>
<li>Date: 服务端响应时间</li>
</ul>
<h1 data-id="heading-4">2. cookie选项</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F52091630" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/52091630" ref="nofollow noopener noreferrer">一文看懂cookie</a></p>
<ul>
<li>Name</li>
<li>Value</li>
<li>Domin</li>
<li>Path</li>
<li>Expires/MaxAge</li>
<li>Size</li>
<li>HttpOnly: 禁止js读取cookie</li>
<li>Secure: 只有https能携带cookie信息</li>
<li>SameSite: 禁止跨域，防止</li>
<li>Priority: 优先级</li>
</ul>
<h1 data-id="heading-5">3.什么是HTTP，HTTPS和HTTP的区别</h1>
<h2 data-id="heading-6">HTTP协议</h2>
<p>超文本传输协议，是实现网络通信的一种规范</p>
<ul>
<li>灵活：支持客户端/服务端模式</li>
<li>简单快速：客户端请求服务器时，只需要传送请求方法和路径</li>
<li>无连接：每次连接只处理一个请求，随后断开</li>
<li>无状态：HTTP请求无法根据以前的状态处理本次请求</li>
</ul>
<h2 data-id="heading-7">HTTPS协议</h2>
<p>由于HTTP是以明文的形式进行数据传输，不安全，HTTPS = HTTP + SSL/TLS，让HTTP协议运行在安全的SSL/TLS协议上，通过SSL证书来验证服务器的身份，并为浏览器和服务器之间的通信进行加密</p>
<p>SSL/TLS协议运行在TCP/IP协议和应用层协议之间，浏览器和服务器建立SSL连接时需要选择一组恰当的加密算法来实现安全通信，为数据通信提供安全支持</p>
<h2 data-id="heading-8">区别</h2>
<ul>
<li>http是明文传输不安全</li>
<li>默认端口不一样，http是80, https是443</li>
<li>https需要SSL证书，证书要钱，费用高</li>
</ul>
<h1 data-id="heading-9">4.HTTPS如何保证安全</h1>
<h2 data-id="heading-10">HTTP协议存在的问题</h2>
<ul>
<li>使用明文通信，内容可能被窃听</li>
<li>不验证身份，因此可能遭到伪装</li>
</ul>
<h2 data-id="heading-11">HTTPS</h2>
<p>使HTTP协议运行在SSL/TSL协议之上，安全性由SST来保证</p>
<p>SSL：Secure Socket Layer 安全套接字协议
TSL： 传输层协议</p>
<h2 data-id="heading-12">优势</h2>
<p>信息加密、完整性校验、身份验证</p>
<h2 data-id="heading-13">实现</h2>
<p>SSL的实现主要依赖于以下几种手段</p>
<ul>
<li>对称加密： 采用协商的密钥对数据加密</li>
<li>非对称加密： 实现身份认证和密钥协商</li>
<li>摘要算法： 验证信息的完整性</li>
<li>数字签名： 身份验证</li>
</ul>
<h2 data-id="heading-14">对称加密</h2>
<p>加密和解密的密钥是同一个。只要保证了对称密钥是安全的，就可以保证通信安全，而如何保证对方拿到安全的对称密钥，使用到了非对称加密技术。</p>
<h2 data-id="heading-15">非对称加密</h2>
<p>公钥加密和私钥解密，公钥可公开给任何人使用，私钥保密</p>
<h2 data-id="heading-16">混合加密</h2>
<p>在HTTPS通信过程中，使用的是对称加密+非对称加密。</p>
<p>发送密文的一方使用对方的公钥进行加密处理“对称的密钥”，这样对方用自己的私钥拿到了对称的密钥，之后就可以通过这个对称的密钥进行加密通信</p>
<h2 data-id="heading-17">摘要算法</h2>
<p>一种特俗的压缩算法，常说的散列函数、哈希函数，给数据生成了一个数字指纹。发送一段数据的时候，附上她的摘要，对方接收到数据之后进行对比，就知道数据有没有被修改。</p>
<h2 data-id="heading-18">数字签名</h2>
<p>数字签名可以确定消息是由发送方签名发出来的，因为别人假冒不了发送方的签名。</p>
<p>原理是利用私钥加密，公钥解密。</p>
<p>签名和公钥一样公开。</p>
<h2 data-id="heading-19">CA验证机构</h2>
<p>引入第三方机构，确保安全性</p>
<h1 data-id="heading-20">5.如何理解UDP和TCP， 区别，应用场景</h1>
<h2 data-id="heading-21">TCP</h2>
<p>传输控制协议。</p>
<h2 data-id="heading-22">UDP</h2>
<p>用户数据包协议，简单的面向数据包的通信协议，即对应用层交下来的报问，不合并，不拆分，只是在上面加了首部之后就交给了下面的网络层。</p>
<h2 data-id="heading-23">区别</h2>
<ul>
<li>可靠性： TCP可靠（面向连接、不丢失）、UDP不可靠（面向无连接、存在丢失的可能）</li>
<li>连接性： TCP面向连接、UDP无连接</li>
<li>报文： TCP面向字节流、UDP面向报文</li>
<li>双共性： TCP全双工、UDP一对一/一对多/多对多</li>
<li>流量控制：TCP滑动窗口、UDP无</li>
<li>拥塞控制： TCP慢开始/拥塞避免/快重传、UDP无</li>
<li>传输效率： TCP慢、UDP快</li>
</ul>
<h2 data-id="heading-24">应用场景</h2>
<p>TCP：邮件、QQ文件传输、浏览器
UDP：QQ语音、QQ视频、直播</p>
<h1 data-id="heading-25">6.OSI七层模型</h1>
<p>从下往上：物理层、数据链路层、网络层、传输层、会话层、表示层、应用层</p>
<p>TCP/UDP位于传输层</p>
<p>IP位于网络层</p>
<h1 data-id="heading-26">7.DNS协议是什么？DNS查询完整过程</h1>
<h2 data-id="heading-27">DNS</h2>
<p>域名系统，是互联网的一项服务, 是进行域名和与之对应的ip地址进行转换的服务器。</p>
<h2 data-id="heading-28">域名</h2>
<p>域名是具有层次的结构，从上到下分为根域名、顶级域名(net、com、org、edu、cn）、二级域名、三级域名、、、、</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.xxx.com%25EF%25BC%259A" target="_blank" rel="nofollow noopener noreferrer" title="http://www.xxx.com%EF%BC%9A" ref="nofollow noopener noreferrer">www.xxx.com：</a> www为三级域名、xxx为二级域名、com为顶级域名</p>
<p>在域名的每一层都有一个域名服务器，除此之外，还有电脑默认的本地域名服务器</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f51859cfde59412fb4afc09159de7547~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-29">DNS查询方式</h2>
<ul>
<li>
<p>递归查询</p>
</li>
<li>
<p>迭代查询</p>
</li>
</ul>
<h2 data-id="heading-30">域名缓存</h2>
<p>两种缓存方式</p>
<ul>
<li>浏览器缓存</li>
<li>操作系统缓存（用户自己配置的host文件）</li>
</ul>
<h2 data-id="heading-31">域名解析过程</h2>
<ul>
<li>搜索DNS缓存，先浏览器缓存，再操作系统缓存</li>
<li>请求本地域名服务器，本地域名符预期递归查询自己的DNS缓存，查找成功则返回结果</li>
<li>向上迭代查询，本地域名服务器向根域名服务器发起请求，根服务器返回顶级域名服务器的地址给本地服务器</li>
<li>本地服务器向顶级域名服务器发送请求，获取权限服务器的地址</li>
<li>本地服务器向权限服务器发送请求，获得最终的IP地址</li>
<li>本地服务器拿到IP地址，返回给操作系统，同时将自己的IP地址缓存</li>
<li>操作系统将IP地址返回给浏览器，同时缓存</li>
<li>浏览器获得IP地址，缓存</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b9fdbab924143d498cca35bdf68a517~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-32">8.CDN</h1>
<p>内容分发网络。构建在现有的网络基础之上的智能虚拟网络，依靠部署在各地的边缘服务器，通过中心平台的负载均衡、内容分发、调度等功能模块，使用户就近获取所需内容，降低网络拥塞，提高用户访问响应速度和命中率。</p>
<h2 data-id="heading-33">关键技术</h2>
<ul>
<li>负载均衡</li>
<li>缓存技术</li>
</ul>
<h2 data-id="heading-34">原理分析</h2>
<p>没有应用CDN之前，DNS查询返回的是目标服务器的IP地址</p>
<p>应用CDN之后，DNS查询返回的是一个CNAME（Cannonical Name）别名记录，指向CDN的全局负载均衡</p>
<p>CNAME在域名解析中承担了中间人的角色，是实现CDN的关键</p>
<h2 data-id="heading-35">负载均衡系统</h2>
<p>由于没有返回IP地址，于是本地DNS会向负载均衡系统发送请求，全局负载均衡系统进行智能调度</p>
<ul>
<li>根据用户的IP地址，查表得知地理位置，找到最近的边缘节点</li>
<li>看用户所在的运营商网络，找到相同网络的边缘节点</li>
<li>检查边缘节点的负载情况，找负载较轻的节点</li>
</ul>
<p>综合找到最合适的边缘节点，把这个节点返回给用户，用户就能就近访问CDN的缓存</p>
<h2 data-id="heading-36">缓存代理</h2>
<p>缓存系统可以划分层次，分为一级缓存节点、二级缓存节点。一级缓存节点配置高一些，直连源站；二级缓存节点配置低一些，直连用户。</p>
<p>回源的时候二级缓存只找一级缓存，一级缓存没有才回源站，可以有效的减少真正的回源。</p>
<h2 data-id="heading-37">CDN服务质量指标</h2>
<ul>
<li>回源率</li>
<li>命中率</li>
</ul>
<h1 data-id="heading-38">9. HTTP1.0/1.1/2.0的区别</h1>
<h2 data-id="heading-39">HTTP1.0</h2>
<ul>
<li>无连接、无状态（每次请求与服务器建立一个TCP连接，请求结束后关闭）</li>
<li>只支持GET、POST请求</li>
</ul>
<h2 data-id="heading-40">HTTP1.1</h2>
<ul>
<li>默认支持长连接（Connection: Keep-Alive)（一个TCP连接上可以传送多个HTTP请求和响应）</li>
<li>允许客户端一个请求未完成就发送下一个请求，但是服务端必须按照客户端请求的顺序先后返回结果</li>
<li>增加了更多的请求头和响应头（Last-Modified、If-Modified-Since、Etag、If-None-Match等缓存头来控制缓存策略）</li>
<li>引入range，允许请求资源的某一部分</li>
<li>引入host，虚拟主机</li>
<li>增加了put、delete、option请求</li>
</ul>
<h2 data-id="heading-41">HTTP2.0</h2>
<ul>
<li>多路复用</li>
</ul>
<p>HTTP1.1，一个TCP链接上发送多个请求，有先后顺序规定。但是HTTP2.0，在一个TCP连接里，客户端和服务器都可以发送请求，而且不要求按照顺序，避免了“对头堵塞”</p>
<ul>
<li>二进制分帧</li>
</ul>
<p>帧是HTTP2.0中最小的通信单位。HTTP2.0才用二进制格式传输数据，非1.x的文本格式，解析起来更高校</p>
<ul>
<li>首部压缩</li>
</ul>
<p>减少冗余数据，传输体积减少，降低开销</p>
<ul>
<li>服务器推送</li>
</ul>
<p>允许服务器向客户端推送消息</p>
<h1 data-id="heading-42">10.HTTP状态码</h1>
<ul>
<li>100: 用于POST大数据传输，在传输之前先征询服务器情况，是否处理POST数据</li>
<li>200: 成功</li>
<li>206: 断点续传，视频大文件的加载</li>
<li>301: 永久重定向 （常用于新旧域名替换）</li>
<li>302: 临时重定向 （常用于未登陆页面重新定向到登陆页面）</li>
<li>304：协商缓存 （告诉客户端直接使用缓存中的数据，只返回头部信息，没有内容）</li>
<li>400: 参数错误，服务端无法识别</li>
<li>401: 未登录</li>
<li>403: 禁止访问 （比如只有内网能访问的一些资源）</li>
<li>404: 资源路径错误</li>
<li>503: 服务器停机维护，使用503响应请求</li>
<li>504: 网关超时</li>
</ul>
<h1 data-id="heading-43">11.GET和POST请求</h1>
<ul>
<li>请求资源的形式： GET获取资源、POST提交资源</li>
<li>携带参数： GET在url上、POST在body中</li>
<li>参数大小限制： GET 2kb 、 POST无限制</li>
<li>安全性： POST比GET更安全，因为数据在地址栏不可见（但是从传输角度来说，明文传输都不安全）</li>
</ul>
<h1 data-id="heading-44">12.TCP为什么需要三次握手和四次挥手</h1>
<h2 data-id="heading-45">三次握手</h2>
<p>建立一个TCP连接，需要客户端和服务器总共发送3个包</p>
<p>作用是确认双方的接收和发送能力是否正常，指定自己的初始化序列号为后面的可靠性传输做准备</p>
<p>第一次握手： 客户端发送一个SYN报文，并指明客户端的初始化序列号ISN</p>
<p>第二次握手： 服务端役自己的SYN报文应答，为了确认客户端的SYN报文，将客户端的ISN + 1 作为ACK的值</p>
<p>第三次握手：客户端发送ACK报文，值为服务器的ISN + 1</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8d0aee289ef42c996022461a99f9209~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-46">四次挥手</h2>
<p>第一次挥手： 客户端发送一个FIN报文，报文中制定一个序列号</p>
<p>第二次挥手： 服务端接收到FIN报文，发送ACK报文，值为客户端序列号+1</p>
<p>第三次挥手：如果服务器也想断开连接，会向客户端发送一个FIN报文，指定一个序列号</p>
<p>第四次挥手： 客户端发送ACK报文应答，值为服务端序列号+1</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51c87aaa7e74438cb16cb6fcfc912a64~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-47">13. WebSocket的理解</h1>
<p>是一种网络协议，应用层协议。可在单个TCP连接上进行全双工通信，能够更好的节省服务器资源和带宽并达到实时通讯</p>
<p>客户端和服务端只需要完成一次握手，就可以建立持久性的通信，并进行双向数据传输</p>
<p>websocket之前实现实时通讯的方式为轮询</p>
<p>引入ws和wss分别代表明文和密文的websocket协议，且默认端口使用80或443，几乎与http一致</p>
<h1 data-id="heading-48">优点</h1>
<p>相较于HTTP： 更强的实时性、保持连接的状态（不用每次带身份信息）、较小的开销（数据包头部协议较小）</p>
<h1 data-id="heading-49">应用场景</h1>
<ul>
<li>弹幕</li>
<li>媒体聊天</li>
<li>体育实况更新</li>
<li>股票基金报价的实时更新</li>
</ul></div>  
</div>
            