
---
title: 'Git 2.33 发布，新增_merge-ort_合并实现 500-9000 倍加速'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0818/060654_kQl7_2744687.png'
author: 开源中国
comments: false
date: Wed, 18 Aug 2021 06:07:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0818/060654_kQl7_2744687.png'
---

<div>   
<div class="content">
                                                                                            <p>Git 2.33 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.blog%2F2021-08-16-highlights-from-git-2-33%2F" target="_blank">发布</a>，本次更新由 74个人贡献的 449 个非合并提交组成，其中 19 位是新面孔。此版本并没有很多面向终端用户的变化和新功能，但在这个周期内包含了很多修复和内部改进。</p> 
<p>另外，新的合并策略后端（可以用 "git merge -sort"）的准备工作已经进入最后阶段。官方表示，其有希望在下一个版本中成为默认设置。 </p> 
<p><img alt height="507" src="https://static.oschina.net/uploads/space/2021/0818/060654_kQl7_2744687.png" width="721" referrerpolicy="no-referrer"></p> 
<p>具体<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phoronix.com%2Fscan.php%3Fpage%3Dnews_item%26px%3DGit-2.33-Released" target="_blank">来说</a>，Git 2.33 带来了有关 geometric repacking 的最新补丁、“merge-ort”作为处理跨分支 Git 合并的新合并策略，以及许多与位图相关的优化。还有一些常见的各种修复和小项目。</p> 
<p>Git 的新 merge-ort 策略是对其递归策略的一次从头重写，但解决了正确性和性能问题。GitHub 报告称，对于具有许多重命名的大型合并来说，merge-ort 可以达到 “500 倍”的加速。在 re-base 操作中的合并，merge-ort 的速度则可以提高到 9000 倍以上。新的 merge-ort 应该比现有的合并代码执行的更快。</p> 
<p>更多亮点内容可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.blog%2F2021-08-16-highlights-from-git-2-33%2F" target="_blank">官方博客</a>，完整更改可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flore.kernel.org%2Flkml%2Fxmqq1r6touqi.fsf%40gitster.g%2F" target="_blank">查看邮件列表</a>。</p>
                                        </div>
                                      
</div>
            