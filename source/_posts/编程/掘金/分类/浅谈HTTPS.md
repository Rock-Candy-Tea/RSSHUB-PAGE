
---
title: '浅谈HTTPS'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3887'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 01:06:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=3887'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1.为何要使用HTTPS？</h1>
<p>使用HTTPS比起HTTP更加的安全，更加利于SEO，搜索引擎会优先索引HTTPS。</p>
<h1 data-id="heading-1">2.HTTPS和HTTP有什么区别？</h1>
<ul>
<li>HTTPS传输数据是加密传输，HTTP是明文传输。</li>
<li>HTTPS默认使用443端口，HTTP默认使用80接口。</li>
<li>HTTPS需要用到CA证书，HTTP不需要。</li>
<li>访问HTTPS网页会显示绿色的安全锁，HTTP则没有。</li>
</ul>
<h1 data-id="heading-2">3.准备工作</h1>
<h2 data-id="heading-3">准备工作一：HTTPS = HTTP + SSL</h2>
<p>在讨论这个话题之前我们需要了解到HTTPS = HTTP + SSL，HTTP指超文本传输协议，而SSL是一种安全协议，你可以简单地的理解为HTTP开外挂了。</p>
<h2 data-id="heading-4">准备工作二：对称加密</h2>
<p>所谓对称加密指的是双方都拥有相同的钥匙用于解锁。比如钥匙是<code>123</code>，当我们要传输数据为<code>456</code>，我们就使用钥匙加密数据得到<code>579</code>即<code>123+456</code>，接收方接收到数据<code>579</code>之后即可使用钥匙解密数据得到<code>456</code>即<code>579-123</code>。
但是对称加密有一个问题是双方如何安全的得到钥匙，因为如果你发送钥匙的时候被截取，那么接下来的传输就和明文传输无异了。</p>
<h2 data-id="heading-5">准备工作三：非对称加密</h2>
<p>非对称加密表示有两把钥匙，一把用于加密，另一把解密，我们将其称为公钥和私钥，使用公钥加密的数据必须使用私钥解密。所以我们只需要将公钥加密的数据用于传输，即使数据被截取，但是截取的人没有私钥也无法得到真实的数据。听起来好像挺安全的，但是仔细一想如果一开始我们收到公钥就是黑客给的，用黑客的公钥加密数据进行传输，黑客可以轻易的解密我们的信息，我们以为我们是在和服务器对接，其实我们是在和黑客对接。所以我们需要确认我们收到的公钥是不是我们想要对接的服务器发来的，这就需要用到CA证书了。</p>
<h2 data-id="heading-6">准备工作四：CA证书</h2>
<p>CA证书也被称为数字证书，它是由CA机构颁布的，CA机构是一个权威机构，既然是权威机构颁布的证书我们当然可以选择相信它。一般证书中会有以下内容：</p>
<ul>
<li>签发证书的机构;</li>
<li>证书Hash算法;</li>
<li>证书上的Hash值;</li>
<li>服务器的公钥;</li>
<li>证书到期时间;</li>
<li>证书的有效时间；</li>
</ul>
<p>等等。</p>
<h1 data-id="heading-7">HTTPS的工作流程</h1>
<ol>
<li>浏览器(A)初次访问服务器(B)，会传一个<code>随机数1</code>，浏览器会提示安装CA证书拿到证书公钥，但是一般不会提示因为window操作系统会内置CA证书。</li>
<li>B在此时会返回<code>CA证书</code>,<code>B的公钥</code>还有<code>随机数2</code>，其中包含的内容就是我们准备四中的内容。</li>
<li>A拿到证书会确认证书的真实性，这里运用到的就是非对称加密的知识了，我们使用CA证书的公钥去解析CA用私钥加密的Hash-a，然后再利用给到的Hash算法生成Hash-b，如果Hash-a==Hash-b，则表示证书是安全可靠的，即代表里面B的公钥也是安全可靠的。当然除了除了校验了CA证书的安全性还会校验例如发送方是否是B加以确认。在完成这个校验之后，我们就可以正常的使用<code>B的公钥</code>对数据进行加密了，这个时候我们会生成一个<code>随机数3</code>并使用<code>B的公钥</code>加密传给服务器。</li>
<li>由于非对称加密的计算量比较大，而此时你会发现A和B都拥有了<code>随机数1``随机数2``随机数3</code>，所以我们在此时会使用<code>AES算法</code>（面试被问过这个算法）对这三个随机数生成会话密钥，接下来就是切换到对称加密传输的步骤了。至此，SSL的流程就走完了。</li>
</ol>
<p><em>SSL流程图</em></p>
<pre><code class="hljs language-mermaid" lang="mermaid">sequenceDiagram

浏览器->>服务器: 随机数1
服务器-->>浏览器: CA证书+公钥+随机数2
浏览器->>浏览器: 验证CA证书
浏览器->>服务器: 公钥加密的随机数3
浏览器->>浏览器: 根据3个随机数生成会话密钥
服务器->>服务器: 根据3个随机数生成会话密钥
浏览器->>服务器: 会话密钥加密的信息
服务器->>服务器: 会话密钥解密
服务器-->>浏览器: 根据请求信息返回数据

</code></pre>
<h1 data-id="heading-8">尾记</h1>
<p>HTTPS涉及的知识还蛮杂乱的，但是面试的时候经常会问到，所以我们需要牢记过程，特别提一下非对称加密使用的是<code>RSA算法</code>，对称加密一般使用<code>AES算法</code>，如果有兴趣的小伙伴也可以去了解一下相关内容。
以上内容是我对HTTPS的理解，如有错误，希望各位能够留言告知，感谢阅读。</p></div>  
</div>
            