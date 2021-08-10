
---
title: '如何看待苹果 iOS 15 扫描用户相册行为，是否侵犯隐私？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=6960'
author: 知乎
comments: false
date: Tue, 10 Aug 2021 09:13:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=6960'
---

<div>   
Thym0s的回答<br><br><p>先说结论，<b>会侵犯隐私，而且具体会侵犯哪些隐私是由 NCMEC 拍板决定的，连苹果都不一定能控制，用户就更无力把握了。</b></p><p>说这个功能不会侵犯隐私的人，我就不说苹果的 CSAM Detection 白皮书了，苹果官网的 Child Safety 宣传页完整读过了吗？</p><a data-draft-node="block" data-draft-type="link-card" href="http://link.zhihu.com/?target=https%3A//www.apple.com/child-safety/" data-image="https://pic4.zhimg.com/v2-f5562edaf787849bebffee610e80f713.jpg" data-image-width="1200" data-image-height="630" class=" wrap external" target="_blank" rel="nofollow noreferrer">Child Safety</a><p><br></p><p>整个技术的大致原理，通俗来说是这样的：</p><p>美国国家儿童失踪与受虐儿童援助中心（NCMEC）会给苹果提供一份“儿童色情图片”特征库，苹果手机拿到这份特征库后，会在你的设备上直接比对哪些图片符合这些特征。</p><blockquote>[...], an on-device matching process is performed for that image against the known CSAM hashes.</blockquote><p>如果吻合的图片超过一定数量，苹果就能通过一项名为“threshold secret sharing”的技术解密你的图片数据，人工检查相册里的照片到底是不是儿童色情，要不要上报给执法部门等等。</p><blockquote>Apple then manually reviews each report to confirm there is a match, disables the user’s account, and sends a report to NCMEC.</blockquote><p>换句话说，<b>只要你的相册里有足够的照片命中了特征库，苹果（或者说执法部门）就可以解密并翻阅你的相册数据。</b></p><p>有的朋友可能不理解，特征都已经匹配上了，为什么还需要人工审查？</p><p>这是因为苹果使用的 NeuralHash 技术属于模糊哈希（Fuzzy Hash / Local Sensitivity Hash）的一种，它的结果不是100%确定的。有可能你只是在相册里存了几十张不太健康的图片，但却被神经网络识别成了几十张儿童色情图片。如果你不允许苹果工作人员亲自翻检你的相册的话，就可能会平白蒙受牢狱之灾……至少苹果的故事版本是这样的。</p><p>为了让用户安心，苹果声称自己使用的 NeuralHash 技术误报率只有“每年不超过万亿分之一“（less than a one in one trillion chance per year），所以用户不用太担心自己的照片因为误报而被解密。</p><p><b>但问题是，如果这些匹配结果不是误报呢？</b></p><p>如果 NCMEC 的特征库从一开始就加了一堆私货，会大量匹配到执法部门感兴趣的图片，那不就意味着云端可以绕过现行的所有加密体系，不断通过 threshold secret sharing 解密这些用户的照片？</p><p>而且苹果在白皮书里也说了，NCMEC 下发的特征库是通过层层加密精心保护的，不会开放给用户检查，这样就能“避免恶意用户绕过特征库的检查”。也就是说，用户是基本没有机会检查这个特征库的内容的，整个体系就是刻意设计成了这样。</p><p><b>整份白皮书看下来，让我感觉苹果根本就是在自身已有的安全体系上开了一个大口子。</b></p><p>苹果原本是全世界最安全的手机/云备份厂商之一，这也是很多用户选择购买苹果产品的核心要素。用户的照片上传到 iCloud 前，会先经过高强度的加密。而且加密密钥只会保存在本地，不会上传到苹果服务器上，有全世界人数众多的逆向工程师和安全工程师在监督这个安全流程。即使你把整个苹果的数据中心打穿了，也拿不到一条明文数据。</p><p>虽然有人常常提起苹果收到法院传票后会帮美国政府解锁数据，但是目前为止苹果官方的 Law Enforcement Guideline 都声称苹果手里的技术仅能解锁 iOS 8 以下的系统，iOS 8 及以上的系统只能求助于黑市上那些苹果都不知道的非公开 0-Day 漏洞。</p><p>但是有了这个 CSAM Detection 之后，苹果相当于绕过了自己之前大力宣传的安全体系。匹配哪些图片、解密哪些图片，完全是由一份不透明的特征库来决定的。而且有大量关键环节发生在云端，只有苹果的服务器知道发生了什么，凭借逆向工程无法完全监督这个流程，也无怪乎引来大众的质疑了。</p><hr><p>顺便一提，有的朋友可能会好奇，美国执法机构和苹果合作搞这种东西会不会有什么法律风险之类的。这方面推荐阅读一下斯诺登写的《永久记录》，美国执法机构玩了一个非常巧妙的文字游戏——它们声称自己从来没有“大规模收集民众隐私”，而是“用一套自动化的系统收集了大量数据，存放到了一个数据库里”。只有当执法机构从这个数据库里查询某个人的记录的时候，才算是“访问了这个人的隐私”，而这个规模是很小的，所以一切都非常合法。</p><p>好了，话题跑远了，正好我们就用斯诺登对此次事件的评价作为结尾吧。</p><blockquote>No matter how well-intentioned, @Apple is rolling out mass surveillance to the entire world with this. Make no mistake: if they can scan for kiddie porn today, they can scan for anything tomorrow. They turned a trillion dollars of devices into iNarcs—*without asking.*<br><br>不管初衷有多好，苹果这次都相当于在推行一套世界规模的监控体系。不要被话术蒙蔽了：他们今天能扫描儿童色情内容，明天他们就能扫描任何信息。他们正在将上万亿美元的电子设备变成“i卧底” —— 却没有征求我们任何用户的意见。<br><br></blockquote><p>在这个电子设备掌握你一切秘密的时代，不要依赖“他人的道德”这种模糊的东西来保护自己，“商业公司的道德”听起来更是一种荒诞的讽刺。</p><p>不会背叛你的只有你自己。</p>  
</div>
            