
---
title: '去年合并的"新"NTFS Linux驱动因缺乏维护再度引起关注'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0426/836a4e0244c8ae1.jpg'
author: cnBeta
comments: false
date: Tue, 26 Apr 2022 10:46:18 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0426/836a4e0244c8ae1.jpg'
---

<div>   
早在2020年，文件系统驱动供应商Paragon软件公司宣布，他们想把他们的NTFS驱动上传到Linux内核。该驱动之前是该公司的商业产品，但考虑到NTFS如今的状况，他们希望将这个驱动上游化，提供完整的读写支持和其他现有NTFS驱动中没有的功能。<br>
 <p>去年，在经历了多轮审查之后，新驱动程序终于被并入了Linux 5.15。可悲的是，在不到一年的时间里，人们担心这个驱动程序已经成为了孤儿，并且没有得到维护。</p><p>虽然Paragon软件公司在向上游提交驱动时承诺维护该驱动，但自从去年它进入Linux 5.15后，就没有任何重大的更新，甚至从那时起，各种修复请求都在排队。在审查过程中为NTFS3代码贡献了许多补丁的开发者之一Kari Argillander今天对这个驱动的状态提出了担忧。Kari还指出，他一直无法从Paragon的维护者那里得到任何回应，甚至连邮件都不回一个。</p><p>Kari在帖文中总结了这一现状，在NTFS3驱动宣布开放并快速推进合并到内核时曾引起了很多人的兴奋，但现在，人们担心该驱动接下来无人维护。由于它依然是一个相当有用的功能，Kari把这个驱动归类为“孤儿”类型，并向社区提出了共同维护这个驱动的提议，但是迄今为止还是没有收到源头维护者的回应。因此，现在Linux内核社区已经有人讨论这个驱动是否应该从主线上删除，或者采取什么行动让这个驱动进入一个维护状态。</p><p><img src="https://static.cnbetacdn.com/article/2022/0426/836a4e0244c8ae1.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>从Git提交记录中不难看出，自从去年为Linux 5.15合并后，NTFS3文件系统驱动确实没有重大的代码变化。Paragon的开发分支最后一次提交还是在去年10月和11月，甚至这些修复还没有合并上行。因此，现在情况对这个曾经很有前途的Linux的NTFS驱动来说并不乐观，我们将继续观察开发和维护的情况是否有变化或内核团队会对此采取任何即时行动。</p>   
</div>
            