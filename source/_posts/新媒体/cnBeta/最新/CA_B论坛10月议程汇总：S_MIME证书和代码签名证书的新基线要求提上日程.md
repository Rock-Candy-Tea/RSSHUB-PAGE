
---
title: 'CA_B论坛10月议程汇总：S_MIME证书和代码签名证书的新基线要求提上日程'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://picsum.photos/400/300?random=7152'
author: cnBeta
comments: false
date: Fri, 29 Oct 2021 06:36:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=7152'
---

<div>   
<strong>感谢<a href="https://www.racent.com/email-sign-ssl" target="_blank">锐成信息</a>的投递</strong><br><br>
 <p><strong>Apple新root程序</strong></p><p>Apple 宣布了新的<a href="https://www.racent.com/email-sign-ssl">S/MIME邮件证书</a>文件要求，预计在明年4月开始实施。Apple称自2022 年4月1日起，将缩短S/MIME证书的有效期为两年，并要求所有证书颁发机构（即CA）公开所有与<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>根证书列表相关链的CA证书。</p><p>此外，Apple还要求S/MIME证书：</p><p>ü  包括 emailProtection EKU；</p><p>ü  包括至少一个包含电子邮件地址的使用者可选名称 rFC822Name 值；</p><p>ü  有效期不超过 825 天；</p><p>ü  使用加密强度≥SHA-256签名算法；</p><p>ü  满足以下密钥大小要求：</p><p>• 如使用RSA加密算法，密钥大小必须至少为 2048 位，且必须能被 8 整除。</p><p>        • 如使用 ECDSA算法，密钥必须代表 NIST P-256、NIST P-384 或 NIST P-521 命名椭圆曲线上的有效点。</p><p><strong>更改SSL/TLS证书文件</strong></p><p>在过去两年左右的时间里，验证小组委员会一直致力于更清楚、更明确地说明哪些内容可以展示在公众信任的SSL/TLS证书中，哪些内容可能不出现在证书中。虽然我们强烈支持明确的要求，但更严格的信息要求可能会给部分客户造成困扰。此次会议中提出了很多更新建议，其中大部分可能会在2022年通过，并在2023年被要求执行。</p><p><strong>eIDAS 2.0 预告</strong></p><p>Enrico Entschew 在会议上围绕在欧洲正实施 eIDAS（欧盟电子签名及信任体系条例）更新做了总结。根据当前的提案，浏览器将被要求遵守欧盟信任列表，并为欧洲证书（称为 QWAC）提供可视化指标。此外，在eIDAS 2.0中他强调了数字身份重要性，并表示在数字钱包和下一代数字身份方面还有很多工作要做。</p><p><strong>S/MIME证书基线要求</strong></p><p>S/MIME工作组正在制定一套新的S/MIME基线要求。虽然这些要求要到2022年才能最终确定，可能要到2023年或更晚才会生效，但该组织已经完成了对S/MIME文件草案的讨论，并初步达成共识。在策略要求中有部分亮点值得关注：首先，它有一个传统概要文件，里面基本包括了对行业中现有的实践的系统介绍，也允许现有的CA快速采用和推进新的S/MIME基线要求。此外，它还包括升级到更有价值的证书类型的路径，包括那些包含经过验证的身份信息的证书。最后，最苛刻的条款将被降级为严格规定，这样那些认为此条款有用的人可以继续采用，如果认为无用则可以选择忽略。</p><p><strong>改善代码签名服务要求</strong></p><p>最后，代码签名工作组正在改善<a href="https://www.racent.com/code-sign-ssl">代码签名</a>服务，这可能会大大提高个人持有的数字令牌的安全性和可用性。该工作组的工作仍处于早期阶段，目前的要求尚不明确，但我们希望代码签名服务能够快速提高数字签名资产的安全性和可用性。</p><p>正如今年早些时候，CA/B论坛宣布<a href="https://www.racent.com/blog/code-signing-changes-in-2021">代码签名证书更改最小密钥长度为3072位</a>一样，其目的也是为了提高数字签名的安全性。</p><p>根据以上会议摘要可看出，不论是CA/B论坛还是Apple公司都在开始研究S/MIME证书和代码签名证书的新要求。随着公共PKI的广泛应用，锐成信息相信在不久的将来，将会有越来越多的用户注重身份认证和数字签名，这也就意味着互联网安全行业需要基于安全性和可用性原则提高数字证书合规标准，让广大用户群体使用上方便快捷的证书，保障其数据安全。</p>   
</div>
            