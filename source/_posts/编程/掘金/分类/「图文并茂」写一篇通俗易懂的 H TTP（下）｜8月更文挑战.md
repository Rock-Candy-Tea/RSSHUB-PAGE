
---
title: '「图文并茂」写一篇通俗易懂的 H TTP（下）｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43e35895aeeb4247bf8ba82c4a27838a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 01:58:59 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43e35895aeeb4247bf8ba82c4a27838a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>借 8 月更文挑战督促自己，感谢掘金！</p>
<p><a href="https://juejin.cn/post/6992363499720540196" target="_blank" title="https://juejin.cn/post/6992363499720540196">前面写过了一篇 HTTP 的基础知识的文章，有 Header、响应码以及 Cookie 等介绍。</a>现在，我们得思考一下，数据在网络中传输安全性能否得到保障。<strong>先说结论，HTTP是不安全的传输协议，通常我们会使用HTTPS。</strong> 接下来看这篇文章的大致结构：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43e35895aeeb4247bf8ba82c4a27838a~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 10.22.26.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">HTTP和HTTPS的区别</h2>
<h3 data-id="heading-1">一、HTTP 存在的问题</h3>
<p>其实，在网络上数据的传输并不是由发送方直接就到达了接收方，数据在传输的过程中，是由一个一个的节点进行传输的进行转发，最后才到达了接收方的。那么，数据在传输的
是否会存在不安全的情况。例如，数据被第三个窃听、甚至是有篡改的风险。这就是HTTP之所以会被取代的重要原因，因为HTTP对传输的数据没有加密，数据是以明文进行传输的，很容易被监听、窃取和篡改。而HTTPS 的出现正是为了解决HTTP在传输过程中的不安全而产生的，那么HTTPS是什么呢？</p>
<h3 data-id="heading-2">二、HTTPS又是什么</h3>
<p>HTTPS是什么呢？首先需要说明的是 HTTPS 并不是一种的新的协议，它是在HTTP的基础上套了一层 TLS 和 SSL，从而变成了HTTPS。HTTPS 能够保证数据传输的安全性，除了对数据进行加密之外，还需要验证 CA 机构签发的证书。</p>
<h3 data-id="heading-3">三、STL 和 SSL</h3>
<p>前面讲到了HTTPS使用 SSL 和 TLS 来保证数据传输的安全性，那么是什么 TLS SSL 呢？TLS(Transport Layer Security，传输层安全协议) 和 SSL 的（Secure Socket Layer，安全套接字层），位于可靠的面向连接的网络层协议和应用层协议之间的协议层。通过 SSL 认证，使用数字签名确保数据的完整性、使用加密来确保数据的私密性，以实现客户端和服务端的安全通信。</p>
<p>在 TCP/IP 网络分层理论中，网络可以分成四层：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4304b03e41741c3a8714c6cc998e005~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 15.08.51.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么 TLS 和 SSL 又处于一个什么样的位置呢？来看下面的的这张图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fc232ea03054286b83f6c282396c012~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 15.10.41.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为什么有 TLS 和 SSL 就能够实现数据传输安全呢，HTTPS 又是如何保证的呢？</p>
<h2 data-id="heading-4">HTTPS是如何保证数据安全的</h2>
<h3 data-id="heading-5">一、数据加密</h3>
<p>前面我们知道了 HTTP 数据传输是以明文进行传输的，HTTPS 对数据进行了加密，那么 HTTPS 是怎么对数据进行加密的呢？</p>
<p>既然需要对数据进行加密，就必须的采用一定的加密算法。实际上，加密算法可以分为对称加密和非对称加密，那么什么是对称加密什么是非对称加密呢？截取了维基百科的定义：</p>
<blockquote>
<p><strong>公开密钥密码学</strong>（英语：<strong>Public-key cryptography</strong>）也称<strong>非对称式密码学</strong>（英语：<strong>Asymmetric cryptography</strong>）是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%25AF%2586%25E7%25A2%25BC%25E5%25AD%25B8" title="https://zh.wikipedia.org/wiki/%E5%AF%86%E7%A2%BC%E5%AD%B8" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">密码学</a>的一种<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E6%25BC%2594%25E7%25AE%2597%25E6%25B3%2595" title="https://zh.wikipedia.org/wiki/%E6%BC%94%E7%AE%97%E6%B3%95" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">算法</a>，它需要两个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%25AF%2586%25E9%2592%25A5" title="https://zh.wikipedia.org/wiki/%E5%AF%86%E9%92%A5" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">密钥</a>，一个是公开密钥，另一个是私有密钥；公钥用作加密，私钥则用作解密。使用公钥把<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E6%2598%258E%25E6%2596%2587" title="https://zh.wikipedia.org/wiki/%E6%98%8E%E6%96%87" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">明文</a>加密后所得的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%25AF%2586%25E6%2596%2587" title="https://zh.wikipedia.org/wiki/%E5%AF%86%E6%96%87" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">密文</a>，只能用相对应的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E7%25A7%2581%25E9%2592%25A5" title="https://zh.wikipedia.org/wiki/%E7%A7%81%E9%92%A5" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">私钥</a>才能解密并得到原本的明文，最初用来加密的公钥不能用作解密。由于加密和解密需要两个不同的密钥，故被称为非对称加密；不同于加密和解密都使用同一个密钥的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%25AF%25B9%25E7%25A7%25B0%25E5%258A%25A0%25E5%25AF%2586" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E5%AF%B9%E7%A7%B0%E5%8A%A0%E5%AF%86" ref="nofollow noopener noreferrer">对称加密</a>。公钥可以公开，可任意向外发布；私钥不可以公开，必须由用户自行严格秘密保管，绝不透过任何途径向任何人提供，也不会透露给被信任的要通信的另一方。</p>
</blockquote>
<p>可以看到，对称加密算法加密和解密都使用一个密钥，因此对称加密使用的效率高，非对称加密的效率比较低。很明显，网络中数据的传输是追求效率的，这里数据传输应该使用对称加密，就像下面这样：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bdf319c1a704709833c84a1429ef579~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 16.16.23.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，对数据进行加密之后，监听者拿到的是密文，由于它没有密钥，所以无法对密文进行解密，数据看起来是安全的。但是这里存在一个问题，客户端和服务器使用的密钥A是如何得到的呢？无论怎样，客户端和服务器在首次通信都是明文的，需要把这个密钥A进行传输对方。</p>
<p>为了解决这个问题，我们引入了非对称加密。那么，非对称加密是如何保证数据传输安全的呢？</p>
<p>非对称加密分为公钥和私钥，公钥用来加密数据，私钥用来解密数据，公钥允许在网络中传输，私钥不允许泄露。客户端想要向服务器请求数据，首先它会生成一个密钥，并且使用服务器的公钥对这个随机值进行加密，服务器收到这条消息之后，会使用自己的私钥对其进行解密，从而获得密钥，接下来就可以使用对称加密进行数据传输了，画了一个示意图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61f3ff313e13403e92979067ea1f9df2~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 16.46.47.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">二、证书校验</h3>
<p>上面讲了数据的加密，实际上还忽略一个重要的点，客户端使用服务器的公钥进行加密，如果有第三者把这个公钥替换成自己的公钥，并且成功用自己的私钥进行了解密，那么传输的数据岂不是泄露了，又画了一个示意图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a37cf0bdf6b44c809dd9a89d7f230be0~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 17.10.49.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了解决这个问题，引入证书这样的一种机制。下面是掘金平台证书：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6d5115824244634ba72b2165c7d4731~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 17.16.13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个证书是有 CA 机构进行签发认证的，那这个证书都包含了哪些信息呢？很明显，这个证书至少应该包含公钥，还有网站域名、有效时长以及签发机构。另外，我们如何验证 这个 CA 机构是合法的呢？这就需要使用根证书了，在我们的操作系统内部。在掘金平台的证书中，我们可以看到对它进行签发的机构是<code>Encryption Everywhere DV TLS CA - G1</code>，我们系统的根证书<code>DigiCert Global Root CA</code>又对这个签发机构的证书进行验证，在哪里找到这个系统的更证书呢？在 MacOS 中，可以在钥匙串中找到：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54978fc4c1c84ec4a477a3e3a0f6e7da~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 17.31.29.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果有人会问，系统的这个证书怎么进行校验呢？这样下去岂不是无限递归了呢？很遗憾告诉大家，到这一步证书校验就停止了，你必须无条件信任这个系统的根证书，所以不会发生无限递归的情况。</p>
<p>是不是神奇？奇奇怪怪的知识又增加了。以上就是 HTTPS 原理了，虽然不够深入，但是在面试被问到的时候，也不至于说一句：<code>Https 是安全的 Http</code>。</p>
<h2 data-id="heading-7">总结</h2>
<p>下面来做一个总结：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d317604c822146cd826d135ea611c477~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 17.55.42.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一切的总结都在图中，就不必多说了。另外，总算圆了标题的「图文并茂」。</p>
<p>另外，由于水平有限，有错误的地方在所难免，未免误导他人，欢迎大佬指正！码字不易，感谢大家的点赞关注！🙏</p></div>  
</div>
            