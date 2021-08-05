
---
title: 'HTTPS原理与运行机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08736efcc1fb47c3b1fba809578e20ff~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 23:05:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08736efcc1fb47c3b1fba809578e20ff~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文主要想说明以下几个问题：</p>
<p>1.https解决了什么问题？</p>
<p>2.https是如何解决数据在网络传输中的安全问题的？</p>
<p>3.https的运行过程是怎样的？</p>
<p>4.如何使用https?</p>
<h3 data-id="heading-0">一、https解决了什么问题</h3>
<p>http在网络传输过程中都是明文传输，在传输过程中存在以下风险（下文称风险1、风险2、 风险3）：</p>
<ol>
<li>内容被窃听：传输过程中数据被第三方看到</li>
<li>内容被篡改：数据传输过程中，被第三方修改</li>
<li>被第三方冒充：通信过程中，被第三方冒充身份，进行通信，比如被冒充身份与银行通信，将钱转出。</li>
</ol>
<p>https的出现主要就是为了解决以上三个问题。</p>
<h3 data-id="heading-1">二、https是如何解决数据在网络传输中的安全问题的</h3>
<p>为了解决内容被窃听，最简单的方法就是加密。客户端发送请求给服务端，服务端返回加密后的数据给客户端，客户端通过密钥解密，获取内容。这个过程中，只有看客户端和与之通信的服务端才有密钥，所以，如果加密算法的安全性足够强，是能够保证数据不被第三方看到的。并且由于加密方式未知，通信的内容也无法被篡改，也不太容易被冒充身份。</p>
<p>当然，这只是理想状态下的情形。在互联网环境中，每个服务端和客户端通信时都要使用不同的密钥，而且在不同的会话过程中也要使用不同的密钥。而双方通信前，必须要商定使用哪一种密钥，或者存储密钥，这在实际情况中几乎是不可能的。</p>
<p>为了解决密钥的分发问题，https采用了非对称加密算法。既然有非对称加密，就一定有对称加密，下面解释一下二者的区别。</p>
<p>**对称加密：**如下图，加密和解密使用相同的密钥，解密为加密的逆运算。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08736efcc1fb47c3b1fba809578e20ff~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>**非对称加密：**与对称加密对应的，非对称加密则有两个密钥，一个公钥，一个私钥。公钥和私钥是一对，二者只能配合使用，虽然二者是相关的，但是无法通过公钥推断出私钥，反之也不可以。可以用公钥加密用私钥解密，也可以用私钥加密，用公钥解密。非对称加密有极强的保密性，安全性非常高，但是由于算法复杂，导致运算速度相对较慢。</p>
<p>有了非对称加密，似乎密钥分发的问题迎刃而解了。假设A,B 都有自己的公钥和私钥。则A和B通信的过程可以是：</p>
<p>（1）A和B交换彼此的公钥。</p>
<p>（2）A使用B的公钥，加密请求，发送给B。</p>
<p>（3）B使用私钥获取请求内容，并用A的公钥将应答数据加密后发送给A</p>
<p>（4）A通过自己的私钥解密数据，获得明文。</p>
<p>我们分析一下以上过程，首先这个过程是可以防止风险1的。对于风险2，即使被篡改了，无法被A正确解密，其破坏性也有限。对于风险3，如果中间人C可以获取A，B的通信内容，则完全可以在步骤(1) 获得A, B的公钥，再将自己的公钥分别分发给A, B，则A，B发送过程中的信息都是用C的公钥加密，C可以使用自己的私钥解密，并且A、B对此毫不知情。</p>
<p>造成这个问题的原因是通信双方无法得知，自己所获取到的对方的公钥的真实性。为了解决公钥真实性问题，https使用数字证书来保证公钥的真实性。</p>
<p><strong>数字证书：</strong></p>
<p>服务端会向权威机构申请数字证书。</p>
<p>数字证书中包含用于给浏览器加密的公钥，申请人的基本信息，但是会使用机构的私钥进行加密。</p>
<p>通信过程中，浏览器拿到了从服务端返回的证书，首先由于浏览器在安装的时候已经内置了信任的机构的证书，如果互相信任，则浏览器中保存了该机构用于对明文进行加密的私钥的公钥。浏览器使用公钥解密得到服务端的基本信息，如果和自己需要请求的服务端信息相同则表示信息是正确的，则可以获得服务端的公钥。在这个过程中，如果有第三方想要冒充服务端和浏览器通信，由于没有被信任的证书，所以是做不到的，或者即使有被信任的证书，但是整数中的身份信息是无法修改的，同样在身份验证过程中也是不会被浏览器接受的。</p>
<p>但是非对称加密算法有一个问题：由于算法复杂，导致运算时间长，如果每次通信都使用公钥加密数据，则会非常耗时。上文中我们说到，如果可以解决通信双方密钥分发的问题，则使用运算时间短的对称加密，在安全上也足够了。因此，https采用了对称加密 + 非对称加密的策略。非对称加密算法只用来交换对称加密的密钥和加密算法，在后面的通信中使用对称加密算法来加密数据，兼顾了安全性和效率。</p>
<h3 data-id="heading-2">三、https的运行过程</h3>
<p>（1） 客户端向服务器端索要并验证公钥。</p>
<p>（2） 双方协商生成"对话密钥"(对称加密算法密钥)。</p>
<p>（3） 双方采用"对话密钥"进行加密通信。</p>
<p><strong>其中前两步是握手阶段。详细如下：</strong></p>
<p><strong>1.浏览器向服务器发送请求加密通信的请求。请求内容如下：</strong></p>
<p>（1） 支持的协议版本，比如TLS 1.0版。</p>
<p>（2） 一个客户端生成的随机数，稍后用于生成"对话密钥"。</p>
<p>（3） 支持的加密方法，比如RSA公钥加密。</p>
<p>（4） 支持的压缩方法。</p>
<p><strong>2.服务器收到请求后，向浏览器回应。内容如下：</strong></p>
<p>（1） 确认使用的加密通信协议版本，比如TLS 1.0版本。如果浏览器与服务器支持的版本不一致，服务器关闭加密通信。</p>
<p>（2） 一个服务器生成的随机数，稍后用于生成"对话密钥"。</p>
<p>（3） 确认使用的加密方法，比如RSA公钥加密。</p>
<p>（4） 服务器证书。</p>
<p><strong>3.浏览器收到服务器的回应后，首先校验证书是否是受信任的机构颁发的，是否过期，如果都正常，使用内置的证书中的私钥解密服务器返回证书，得到服务器的域名等信息。如果和自己请求的服务器域名信息一致则校验通过。取出服务器证书中的公钥。并发消息给服务器，内容如下：</strong></p>
<p>（1） 一个随机数。该随机数用服务器公钥加密，防止被窃听。</p>
<p>（2） 编码改变通知，表示随后的信息都将用双方商定的加密方法和密钥发送。</p>
<p>（3） 浏览器握手结束通知，表示浏览器的握手阶段已经结束。这一项同时也是前面发送的所有内容的hash值，用来供服务器校验。</p>
<p><strong>4.服务器收到信息后，根据前三次通信的三个随机数，以及双方商定的加密算法，生成密钥。然后向浏览器发送如下信息：</strong></p>
<p>（1）编码改变通知，表示随后的信息都将用双方商定的加密方法和密钥发送。</p>
<p>（2）服务器握手结束通知，表示服务器的握手阶段已经结束。这一项同时也是前面发送的所有内容的hash值，用来供客户端校验。</p>
<p>使用三个随机数是为了增加随机度，增加算法的随机性，因为计算机生成的随机数一般都是伪随机数，使用三个伪随机数，可以近似看作随机数了。</p>
<p>经过以上四个步骤，浏览器和服务器商定了通信的密钥，则每次通信和http通信，除了信息会使用密钥加密，其他没什么区别了。</p>
<p><strong>经常会出现因为某些原因导致https会话中断，如果重新进行握手比较耗时，常见的作法是使用session id，或者session ticket 来恢复https会话。</strong></p>
<h3 data-id="heading-3">四、如何使用https</h3>
<p>1.获取证书</p>
<p>2.服务器上安装证书</p>
<p>3.将网页加载的 HTTP 资源，要全部改成 HTTPS 链接。因为加密网页内如果有非加密的资源，浏览器是不会加载那些资源的。</p>
<p>4.修改服务器配置，将http导向https</p>
<p>参考文献：</p>
<p>1.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F43789231" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/43789231" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/43789231</a></p>
<p>2.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F36981565" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/36981565" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/36981565</a></p>
<p>3.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2014%2F09%2Fillustration-ssl.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2014/09/illustration-ssl.html" ref="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2014/0…</a></p>
<p>4.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2016%2F08%2Fmigrate-from-http-to-https.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2016/08/migrate-from-http-to-https.html" ref="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2016/0…</a></p></div>  
</div>
            