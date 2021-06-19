
---
title: 'OpenSSL 3.0 Beta1 发布，变更开源许可证为 Apache 2.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6642'
author: 开源中国
comments: false
date: Sat, 19 Jun 2021 07:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6642'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OpenSSL 3.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fblog%2Fblog%2F2021%2F06%2F17%2FOpenSSL3.0ReleaseCandidate%2F" target="_blank">发布</a>了首个 Beta 版本，开发团队表示他们将其视作 RC 版本，因此鼓励所有 OpenSSL 用户针对这个测试版进行构建和测试，并提供反馈。</p> 
<p>据介绍，在过去的几个月里，开发团队为 OpenSSL 3.0 的最终发布做了许多工作。他们表示整个 OpenSSL 3.0 的开发工作量是巨大的，自从开始 3.0 以来，已经有 300 多个不同的贡献者提交了 7000 多个 commit。</p> 
<p>下面介绍一下 OpenSSL 3.0 的主要新功能和变化。</p> 
<ul> 
 <li>采用新的开源许可证。OpenSSL 3.0 将在标准和广泛使用的 Apache License 2.0 下发布，而不是在 1.1.1 及之前版本使用的自定义“双重”许可证：OpenSSL 和 SSLeay License（两者均被使用）</li> 
 <li>采用新的版本控制方案，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fblog%2Fblog%2F2018%2F11%2F28%2Fversion%2F" target="_blank">详情点此查看</a></li> 
 <li>采用基于"Provider"的架构，它取代了旧的"engine"接口，可提供更大的灵活性，以及方便第三方作者将新加密算法添加到 OpenSSL</li> 
 <li>增加一个新的 Provider，将按照 FIPS 140-2 标准进行验证</li> 
 <li>完全“可插拔”的 TLSv1.3 组，使第三方作者能够通过 Provider 添加新的 TLS 密钥交换/封装组</li> 
 <li>增加新的编码器和解码器支持</li> 
 <li>完整的证书管理协议 (CMP) 实现</li> 
 <li>新增用于处理 MAC（消息身份验证代码）、KDF（密钥派生函数）和随机数 (EVP_RAND) 的新 API</li> 
 <li> <p>对内核 TLS 的集成支持</p> </li> 
</ul> 
<p>OpenSSL 3.0 是一个重要的大版本更新，且该工具库的 ABI 发生了变化，使用者需要重新编译所有依赖的应用程序，此外还有一些细小的 API 破坏性变化。</p> 
<p>关于如何将应用程序迁移到 OpenSSL 3.0 的详细指导，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fdocs%2Fmanmaster%2Fman7%2Fmigration_guide.html" target="_blank">查看迁移指南</a>。</p> 
<p>OpenSSL 3.0 Beta1 下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fsource%2F" target="_blank">https://www.openssl.org/source/</a></p>
                                        </div>
                                      
</div>
            