
---
title: '明尼苏达大学有害提交事件后 Linux考虑为补丁提供加密证明'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Sun, 30 May 2021 12:04:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
Linux内核开发者Konstantin Ryabitsev一直在开发Patatt，作为一个基于加密的补丁认证系统。虽然已经开始了一段时间，<strong>但在明尼苏达大学技术人员为了完成课题而向Linux内核灌入缺陷代码的 "伪君子提交"事件之后，人们对这种补丁认证重新产生了兴趣。</strong><br>
 <p>Patatt允许选择性地在补丁中加入端到端的加密证明，其设计是基于DKIM电子邮件签名标准。Patatt可用于在涉及电子邮件补丁提交的工作流程中签署代码补丁，如Linux内核开发中的情况。</p><p>这种选择式的补丁证明旨在尽可能的简单易用，不具侵入性，并能直接采用。最新的b4 0.7版本还增加了对使用Patatt的支持，它本身可以通过Python的pip轻松安装。</p><p>有兴趣了解更多关于Patatt的补丁认证的人可以了解一下Konstantin的博文以及GitHub仓库中的README：</p><p><a href="https://people.kernel.org/monsieuricon/end-to-end-patch-attestation-with-patatt-and-b4" _src="https://people.kernel.org/monsieuricon/end-to-end-patch-attestation-with-patatt-and-b4" target="_blank">https://people.kernel.org/monsieuricon/end-to-end-patch-attestation-with-patatt-and-b4</a></p><p><a href="https://github.com/mricon/patatt" _src="https://github.com/mricon/patatt" target="_blank">https://github.com/mricon/patatt</a><br></p><p>不过，是否/何时会鼓励或推荐更多的内核开发者使用Patatt这样的解决方案来进行基于电子邮件的补丁交换，还有待观察。</p><p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1118079.htm" target="_blank">因故意插入实验性漏洞 明尼苏达大学开发者被禁止向Linux内核供应代码</a></p><p><a href="https://www.cnbeta.com/articles/tech/1118511.htm" target="_blank">明尼苏达大学就Linux内核被注入实验性漏洞一事作出回应</a></p><p><a href="https://www.cnbeta.com/articles/tech/1119547.htm" target="_blank">明尼苏达大学Linux内核“伪装者提交”研究人员发表公开信</a></p><p><a href="https://www.cnbeta.com/articles/tech/1120165.htm" target="_blank">Linux内核维护人员Greg Kroah-Hartman拒绝明尼苏达大学的道歉</a></p><p><a href="https://www.cnbeta.com/articles/tech/1130971.htm" target="_blank">Linux 5.13还原及修复明尼苏达大学的问题补丁</a></p><p><a href="https://www.cnbeta.com/articles/tech/1131581.htm" target="_blank">Linux 5.13-rc3发布 全面回滚来自明尼苏达大学的问题补丁</a></p></div>   
</div>
            