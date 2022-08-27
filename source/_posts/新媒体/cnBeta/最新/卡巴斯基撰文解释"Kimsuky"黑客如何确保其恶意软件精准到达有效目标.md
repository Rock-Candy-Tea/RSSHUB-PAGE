
---
title: '卡巴斯基撰文解释"Kimsuky"黑客如何确保其恶意软件精准到达有效目标'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0827/948438b2f379294.webp'
author: cnBeta
comments: false
date: Sat, 27 Aug 2022 07:07:17 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0827/948438b2f379294.webp'
---

<div>   
朝鲜'Kimsuky'威胁行为者正在不遗余力地确保他们的恶意有效载荷只被有效目标下载，而不是在安全研究人员的系统上。<strong>根据卡巴斯基今天发布的一份报告，自2022年开始，该威胁组织一直在采用新技术来过滤无效的下载请求，当时该组织针对朝鲜半岛的各种目标发起了新的活动。</strong><br>
 <p>Kimsuky实施的新保障措施非常有效，卡巴斯基报告说，即使在成功连接到威胁者的指挥和控制服务器之后，也无法获得最终的恶意软件载荷。</p><p>卡巴斯基发现的攻击始于向朝鲜和韩国的政治家、外交官、大学教授和记者发送的钓鱼邮件。由于检索到含有部分目标电子邮件地址的C2脚本，卡巴斯基能够编制一份潜在目标的清单。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0827/948438b2f379294.webp" title alt="targets-list.webp" referrerpolicy="no-referrer"></p><p>这些电子邮件包含一个链接，将受害者带到一个第一阶段的C2服务器，该服务器在提供恶意文件之前检查和验证一些参数。如果访问者不符合目标列表，他们会得到一个无害的文件。</p><p>这些参数包括访问者的电子邮件地址、操作系统（<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>是有效的），以及由第二级服务器投放的文件"[who].txt"。</p><p>同时，访问者的IP地址被转发给第二阶段的C2服务器，作为后续检查参数。</p><p>第一阶段C2投放的文件包含一个恶意的宏，将受害者连接到第二阶段C2，获取下一阶段的有效载荷，并通过mshta.exe进程运行。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0827/32b9b13e4497fa8.webp" title alt="documents.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">发送给目标的一些文件</p><p>该有效载荷是一个.HTA文件，它也创建了一个自动执行的计划任务。它的功能是通过检查ProgramFiles文件夹路径、反病毒软件名称、用户名、操作系统版本、MS <a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a>版本、.NET框架版本等，对受害者进行特征分析。</p><p>指纹结果被存储在一个字符串（"chnome"）中，一个副本被发送到C2，一个新的有效载荷被获取并在一个持久性机制中注册。</p><p>下一个有效载荷是一个VBS文件，可以把受害者带到一个完全正常的博客，或者，如果识别出他们是有效的目标，就把他们带到有效载荷下载阶段。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0827/32b9b13e4497fa8.webp" title alt="documents.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">感染的每一步都会进行C2检查</p><p>"有趣的是，这个C2脚本根据受害者的IP地址生成了一个博客地址。在计算了受害者IP地址的MD5哈希值后，它切断了最后的20个字符，并把它变成了一个博客地址，"卡巴斯基详细说明。</p><p>"作者在这里的意图是为每个受害者操作一个专门的假博客，从而减少他们的恶意软件和基础设施的暴露。"</p><p>这时，受害者的系统会被检查是否存在不寻常的"chnome"字符串，该字符串是故意拼错的，作为一个独特的验证器，仍然不会引起怀疑。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0827/24a9ac4629e5dc7.webp" title alt="attack-diagram(4).webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">Kimsuky的感染过程</p><p>不幸的是，卡巴斯基无法从这里继续下去，获取下一阶段的有效载荷，所以这是否会是最后一个，或者是否有大多数验证步骤，仍然是未知数。</p><p>Kimsuky是一个非常复杂的威胁行为者，最近被看到部署定制的恶意软件和使用Google浏览器扩展来窃取受害者的电子邮件。</p><p>卡巴斯基强调的活动展示出朝鲜黑客为对抗安全研究机构的分析并使他们的追踪变得更加困难而采用的精心设计的技术。</p>   
</div>
            