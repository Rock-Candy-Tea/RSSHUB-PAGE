
---
title: '多年考量后NIST公布后量子加密和签名算法的首推名单'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0729/798db925cf088af.webp'
author: cnBeta
comments: false
date: Fri, 29 Jul 2022 09:20:10 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0729/798db925cf088af.webp'
---

<div>   
<strong>美国国家标准技术研究所（NIST）近日宣布已持续数年的后量子加密和签名算法竞赛已落下阶段性帷幕，首批获胜者名单已经出炉。</strong>在后量子加密上，NIST 首推 CRYSTALS-Kyber 算法，但后期可能会根据表现有所调整。在签名算法上，NIST 首推 CRYSTALS-Dilithium，以及两款同样优秀的备选算法：Falcon 和 SPHINCS+。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0729/798db925cf088af.webp" alt="vx4w3hgb.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">NIST 耗费了很长时间才选定这些获胜者，期间更是经历了多次延期。其中一个重要原因是，未来的量子计算机可能会破坏当前所使用的几乎所有公钥加密。像 RSA 等其他基于椭圆曲线的算法在未来都可以使用强大的量子计算机进行破解。尽管当前这样的量子计算机还未诞生，但是科学家在这方面的研究已经有了进展。</p><p style="text-align: left;">因此，研究人员开始探索即便是量子计算机也无法破解的算法，也就是我们上文所说的是后量子加密学（post-quantum cryptography）。在 2016 年，NIST 宣布希望标准化后量子加密学并寻求建议。</p><p style="text-align: left;">这项竞赛已阶段性结束，不过 NIST 也表示计划未来对其他算法进行调查，再从中确认可以成为标准的算法。而且对于签名算法，NIST 希望能够推动多种加密方式，从而实现算法的多样性。</p><p style="text-align: left;">自然，这也会给获胜者带来巨大的好处。在 NIST 公开的细节中，NIST 提到，它正在与几个潜在相关专利持有人签订专利协议：“如果协议在 2022 年年底前无法执行，那么 NIST 可能考虑使用 NTRU 来替代 Kyber”。NTRU 也是一种比较热门的算法，其专利影响目前已经过期。Kyber 和 NTRU 都是基于 Lattice 的加密算法。</p><p style="text-align: left;">在签名算法方面，该机构选择了 3 款算法，表明了该机构对该领域的犹豫。选中的这 3 款算法都能对像 TLS 这样每天都在使用的协议进行安全替代。其中 Falcon 和 Dilithium 是基于 Lattice 的，而 SPHINCS+ 是基于 hash 的。</p><p style="text-align: left;">Falcon 是三款中体积最小的签名算法，但这在其他方面做出了牺牲：Falcon 需要恒定的浮点算术。如果无法正确计算，那么可能会导致 side-channel 攻击，从而曝光私钥。</p><p style="text-align: left;">SPHINCS+ 是三款中安全性最高的。这项基于 hash 的算法主要依赖基础哈希函数。哈希函数是一个非常知名的加密结构，不过在签名尺寸上存在挑战：基于版本和安全等级，可以达到 8-50 kilobytes。</p>   
</div>
            