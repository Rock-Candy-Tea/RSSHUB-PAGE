
---
title: 'Linux 5.19内核最新改进使其签名验证代码符合FIPS要求'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0622/c0af4f63b208877.png'
author: cnBeta
comments: false
date: Wed, 22 Jun 2022 09:14:12 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0622/c0af4f63b208877.png'
---

<div>   
昨天合并到Linux 5.19中的改进使内核的签名验证代码符合FIPS标准。为了符合FIPS（联邦信息处理标准），操作系统需要进行自我测试工作。FIPS是通过NIST的公共标准，由美国政府机构和承包商在计算机安全和互操作性领域使用。<br>
 <p>用于密码学的FIPS140概述了围绕自我测试的要求，在启动/重启时，实施已知答案的自测试是符合FIPS要求的条件，但Linux内核的签名验证代码一直缺乏这种测试。</p><p><a href="https://static.cnbetacdn.com/article/2022/0622/c0af4f63b208877.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0622/c0af4f63b208877.png" title alt="018618943_1-b45e7f22758d47d035fb08d5a1d087f3.png" referrerpolicy="no-referrer"></a></p><p>签名检查代码被用于模块签名、Kexec和其他功能，随着Linux 5.19的推出，现在在启动时，操作系统会进行一些基本的自我测试。</p><p>红帽公司的David Howells解释说："模块签名、Kexec等使用的签名检查代码是不符合FIPS标准的，因为一直以来都没有部署自我测试流程。为了使内核符合FIPS标准，签名检查必须在使用前进行测试，如果签名检查不可用，在特定情况下可能会造成一些麻烦（例如简单地禁用签名检查将阻止加载任何驱动模块）。内核代码现在通过增加一个最小规模的测试来处理这个问题。"</p><p>这项FIPS密码学支持昨天被合并到Linux主线上，从而让这个FIPS自测试成为Linux 5.19-rc4的一部分。</p><p><a href="https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png" referrerpolicy="no-referrer"></a></p><p><strong>了解更多：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=0273fd423b2fe10af96ff713273137c63a7736c0" _src="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=0273fd423b2fe10af96ff713273137c63a7736c0" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=0273fd423b2fe10af96ff713273137c63a7736c0</a><br></p>   
</div>
            