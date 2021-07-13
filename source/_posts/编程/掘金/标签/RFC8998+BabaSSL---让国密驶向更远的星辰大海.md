
---
title: 'RFC8998+BabaSSL---让国密驶向更远的星辰大海'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72be135a73974821b65ff78ef4000f97~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 02:26:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72be135a73974821b65ff78ef4000f97~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">01 引言-TLS 1.3 协议及 SM 算法</h2>
<p>说起 TLS，大家一定不会陌生，TLS 可以说是整个互联网安全的基石，保障着我们的通信数据的安全。自从 2014 年 Heartbleed 漏洞被发现以来，网络安全受人关注的程度越来越高，出于更安全更快捷的需求，TLS 1.3 协议也随之被提出，其相应的 RFC 于 2018 年正式发布。随着网络安全越来越受到重视，安全战略也逐步上升到国家战略的高度，国家密码局在 2010 年底公布了我国自主研制的“椭圆曲线公钥密码算法”（SM2 算法），并随后陆续发布了国密算法 SM1-SM9（SM 代表商密的拼音大写）。今天我们要分享的东西，就和 TLS 1.3 及国密有关。</p>
<p>首先先让大家对这两者之间的关系有一个基本的概念，我们以一个典型的 TLS 1.2 中的密钥套件为例：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72be135a73974821b65ff78ef4000f97~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>对应到我们的国密的算法上，则各个算法对应的套件如下：</p>
<p>1、密钥交换算法：ECC-SM2，ECDHE-SM2（这里先不详细展开，只简单介绍一下，国密的密钥交换算法基于当前的椭圆曲线算法设计了两种专门的算法，而对应的曲线则是 SM2 曲线）；</p>
<p>2、数字签名算法：SM2（SM2 既是签名算法的名称，同时在椭圆曲线算法中对应的曲线名也叫 SM2，有的博客文档里也将密钥交换算法称作 SM2，读者请注意不要混淆）；</p>
<p>3、对称加密算法：SM4；</p>
<p>4、hash 算法：SM3。</p>
<p>也就是说，国密局针对安全握手各个阶段所需要的算法都出台了一份自主可控的算法。</p>
<h2 data-id="heading-1">02 why 国密？why not 国密？</h2>
<p>先说说为什么要用国密，国密算法作为国密局的主力产品，肯定是在很多地方有优势的，先来总结下国密的典型优势：</p>
<p>1、更安全：SM2 作为一种 ECC 算法（256 位）的安全性是要高于 2048 位的 RSA 的。同时 SM3 的摘要长度为 256 bit，安全强度也是要高于当时主流的 MD5 算法及 SHA1 算法的。</p>
<p>2、更快速：在通讯过程中，256 位的 SM2 算法相比于 2048 位的 RSA 算法（国密算法在设计时，RSA2048 是主流签名算法，所以这里暂不讨论ECDSA等算法），可以传输更少的数据，也就意味着更少的传输时间，并且在理论上来说，SM2 签名算法的计算速度是要快过 RSA2048 不少的。</p>
<p>3、自主可控：在目前这个国际形势下，这是最最最关键的一点！</p>
<p>国密听起来像是中国密码的一次革新，但这些年却一直没有大面积推行开来，说明其本身肯定有一些问题的，这里抛开一些细节的小问题，谈一谈国密算法在大规模落地过程中遇到的一些比较棘手的问题：</p>
<p>1.速度不够快（麻烦指数★★★）</p>
<p>国密整个 TLS 会话流程中涉及到的几个算法，相对主流国际算法来说，大部分情况下性能均相对弱势，这里针对一些给出一些简单的性能对比表：</p>
<p><strong>对称加密算法性能对比</strong>：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/caaf565163794bcf8014e4f8709b7ecc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p><strong>签名算法性能对比</strong>：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d27d3e36095444dbb4c155e42cc9d2d8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p><strong>hash 算法性能对比</strong>：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c4569a0e2b14fbf81b10609327a7435~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>从对比中我们可以看到，国密的这些算法目前和国际算法性能常常不在一个量级，无论是对称加密还是非对称加密的部分。究极根本原因，还是由于各种通用的国际算法普及程度太大，在工程上有着相应的多层次的优化（硬件计算和各种软加速手段），以对称加密为例：国密对称加密算法 SM4 对标的算法是 aes-128，从本身的加密原理上来看，SM4 在理论上不会和 aes-128 产生如此大的差距，然而 AES 由于普遍性实在太强，典型的 AES 实现都基于 Intel 的 SIMD 指令集对其进行了并行化加速，而 SM4 目前只有纯软的实现，性能上自然有不小的差距。不仅如此，目前的主流对称加密模式为 GCM 及 CCM 模式，其背后的思想为加密即认证技术（AEAD），而国密算法尚不支持这种模式，在安全性上也存在着一些弱点。</p>
<p>2.需要双证书（★★★★）</p>
<p>要把双证书讲清楚首先需要大家理解下 PKI 密钥协商机制，典型的密钥协商算法分为两种：RSA，ECDHE。国密的 ECC-SM2 密钥协商流程和 RSA 比较类似，算法核心的性质在于用公钥加密的数据可以用私钥解密，整个密钥协商流程简化如下图：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/363c366e56a34e2da9da9d9eb7dd3641~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>而 ECDHE-SM2 比较类似 ECDHE 算法，均是基于 DH 和 ECC 的算法，理解起来更加容易，流程简化如下图：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f26ddc3501e4fe08d5bf2f7d2af0b01~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>我们再来谈双证书这个事情，双证书分为签名证书和加密证书，这套体系的目的是满足国家对于敏感数据强管控诉求，即只要能抓到所有数据包，则管控机构则可以在理论上恢复出所有明文数据，由此催生出了加密证书这个东西，加密证书的私钥需要在专门的机构留底。我们来看 RSA 的密钥交换流程，只要拥有了私钥，则中间的密钥生成的材料（随机数）也就可以在理论上进行导出。而对于  ECDHE-SM2 来说，对称密钥的导出流程不仅仅只由随机数 a/c 来决定，同时也需要加密证书对应的私钥参与到计算中（具体流程比较繁琐，这里不展开，读者可参考 GM/T 0024 标准阅读详细的细节），也就意味着当私钥被监管，则对称密钥可以理论上被导出。</p>
<p>这套体系很强悍，但难就难在目前所有主流密码库如 openssl，boringssl 都不支持，那么这也就意味着如果要推进这套体系的普适度，要么基于主流密码库开发，并推进开源社区接受，进而慢慢渗透到国内用户把这套体系用起来，要么在尽可能兼容目前密码体系的情况下开发一套新的密码库并强制国内用户替换，每一种办法都存在不小的难度。</p>
<p>3.需要客户端也持有证书（★★★★★）</p>
<p>国密在 GM/T 0024 标准里面定义了基于 ECDHE-SM2 算法的密钥交换流程，但这个算法的要求十分苛刻，必须要求 Client 也持有证书，的确这对于安全性有一定提升，但麻烦也就随之而来，支付宝的客户端目前没有证书，如果加上证书会让 App 更重，握手交互的数据更多，极大降低用户体验。这些问题还不够致命，如何管理海量的端上证书，才是真正令人头疼的麻烦。</p>
<p>也许你会问：不用 ECDHE 不就好了嘛，但从技术的演进趋势来看，高效/安全是我们孜孜不倦的追求，而类 RSA 的握手流程则从根源上限制了国密 ECC 密钥交换流程无法演进到 1-RTT 握手，0-RTT 信息传输。不仅如此，ECHDE 的安全性及性能，也要好很多。在 TLS 1.3 的 1RTT 标准握手流程中，明确定义了废除 RSA 握手，只支持 ECDHE。目前这个情况就造成了一个死锁，想用 TLS 1.3->需要 ECDHE->需要 Client 有证书->没有证书且不想用证书->问题无解。</p>
<h2 data-id="heading-2">03 重磅推出，TLS 1.3+ 国密算法套件</h2>
<p>针对国密落地过程中的这些痛点问题，2019 年 8 月份，由蚂蚁的同学牵头，撰写了一份 TLS 1.3+ 国密算法 draft，并最终成为了一份 IETF 标准文档：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5167aa9593249848b34b65628dff7a7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>整个标准设计的核心思想是：整合目前国密算法优势，全面贴合国际上的安全技术思路，把不好用的东西先暂时剔除掉，提升国密算法在国内及国际上的影响力，从而让更多组织及个人参与到国密算法的使用和建设中来。基于这个思路，我们联合了 360 等公司，经过和国密局的多次沟通，正式推出了相关标准。在整个流程上，我们在 ECDHE 算法上取消了 Client 证书的要求，并暂时放宽了双证书的需求，由此推出了两个完整的国密算法套件，并确定了签名算法及曲线的标准号。同时我们基于 TLS 1.3 的 AEAD 需求，定义了 SM4 的 GCM 模式和 CCM 模式，并对此做了实现。</p>
<p>整个 draft 定义了以下几个标准（目前这几个标准都已经拿到了对应的标准号）：
国密 SM2 曲线的标准号：curveSM2（41），这个标准号的作用允许 Client 和 server 在进行 TLS 1.3 握手时，使用 curveSM2 作为约定曲线，相当于让 ECDHE_SM2 成为了 TLS 1.3 中的国际标准（当然这里不需要 Client 持有证书）。</p>
<p>基于 SM2 及 SM3 的签名算法标准号：sm2sig_sm3（0x0708），这个标准号的功能在于以后在 TLS 1.3 的流程中，如果 server 持有的是国密证书，则可以默认采用 sm2sig_sm3 作为签名算法，而它的意义在于：国密证书从此也成了标准。</p>
<p>基于 TLS 1.3 及 SM2,SM3,SM4 算法的密钥套件：</p>
<p>TLS_SM4_GCM_SM3（0x00,0xC6）以及 TLS_SM4_CCM_SM3（0x00,0xC7），它意味着从此你可以按照标准使用 TLS 1.3 的 1RTT 握手 + 国密算法，既满足国家标准要求，又能够快速方便。同时 SM4 算法也用上了更安全的 GCM/CCM 模式。</p>
<p>当然，标准也需要工程化的落地实现，而往往工程实现才是真正决定一份算法是否好用的绝对因素。针对 SM2/3/4 性能较差的问题，我们设计并落地了很多方案来进行优化，诸如：异步化的 SM2 硬件加速流程；基于 SIMD 的 SM4 软优化实现等。基于这些技术，真正做到了让国密在生产可用，开销可控。</p>
<h2 data-id="heading-3">04 总结</h2>
<p>当日长缨在手，今朝终缚苍龙。回头看来，协议从一份草案落地成为正式的 IETF 标准文档，差不多经过了两年左右的时间，期间和 IETF 工作组进行多轮，多方的探讨，草案也经过了多轮修订，最终能修成正果，实属不易。随着 TLS 1.3+ 国密正式成为了国家/国际层面均认可的标准（RFC8998），我们也正式在 BabaSSL 中支持了相关能力并将其开源，并建设了 BabaSSL 社区。</p>
<p>所谓鹏北海，凤朝阳，又携书剑路茫茫，BabaSSL 建设的初心是为经济体打造统一/易用的国密密码库，但仅仅一份国密的标准的落地与实现绝不会是 BabaSSL 的终点，BabaSSL 会一直朝着更远的星辰大海奋斗，我们正在积极落地着量子随机数，MPK，Delegated Crendential 等前沿技术，当然，那又是另一些故事了。</p>
<h3 data-id="heading-4">本周推荐阅读</h3>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247488577%26idx%3D1%26sn%3D172642c14cc511e27aa882ca7586a4c4%26chksm%3Dfaa0fb9bcdd7728db0fdceec44b44bb93f36664cbb33e3c50e61fcc05dbc2647ff65dfcda3ee%26scene%3D21" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247488577&idx=1&sn=172642c14cc511e27aa882ca7586a4c4&chksm=faa0fb9bcdd7728db0fdceec44b44bb93f36664cbb33e3c50e61fcc05dbc2647ff65dfcda3ee&scene=21" ref="nofollow noopener noreferrer">揭秘 AnolisOS 国密生态，想要看懂这一篇就够了</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247488835%26idx%3D1%26sn%3Dd645b9abc866048e679b56bfe3b72482%26chksm%3Dfaa0fa99cdd7738ff1749ae75b1670f953c92b70dcf0358337977438fd74b632b21a7b17ece3%26scene%3D21" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247488835&idx=1&sn=d645b9abc866048e679b56bfe3b72482&chksm=faa0fa99cdd7738ff1749ae75b1670f953c92b70dcf0358337977438fd74b632b21a7b17ece3&scene=21" ref="nofollow noopener noreferrer">MOSN 子项目 Layotto：开启服务网格+应用运行时新篇章</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247490185%26idx%3D1%26sn%3Dcfc301e20a1ae5d0754fab3f05ea094a%26chksm%3Dfaa0f553cdd77c450bf3c8e34cf3c27c3bbd89092ff30e6ae6b2631953c4886086172a37cb48%26scene%3D21" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247490185&idx=1&sn=cfc301e20a1ae5d0754fab3f05ea094a&chksm=faa0f553cdd77c450bf3c8e34cf3c27c3bbd89092ff30e6ae6b2631953c4886086172a37cb48&scene=21" ref="nofollow noopener noreferrer">开启云原生 MOSN 新篇章 — 融合 Envoy 和 GoLang 生态</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247488899%26idx%3D1%26sn%3D5558ae0a0c23615b2770a13a39663bb3%26chksm%3Dfaa0fa59cdd7734f35bea5491e364cb1d90a7b9c2c129502da0a765817602d228660b8fbba20%26scene%3D21" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247488899&idx=1&sn=5558ae0a0c23615b2770a13a39663bb3&chksm=faa0fa59cdd7734f35bea5491e364cb1d90a7b9c2c129502da0a765817602d228660b8fbba20&scene=21" ref="nofollow noopener noreferrer">MOSN 多协议扩展开发实践</a></p>
</li>
</ul>
<p>更多文章请扫码关注“金融级分布式架构”公众号</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/407c2c9c35f74d70953135ff210b0940~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote></div>  
</div>
            