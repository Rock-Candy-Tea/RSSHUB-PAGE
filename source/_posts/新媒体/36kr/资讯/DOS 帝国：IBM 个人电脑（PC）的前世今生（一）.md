
---
title: 'DOS 帝国：IBM 个人电脑（PC）的前世今生（一）'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210714/v2_1be2878fe2374ced9a4ad3afb701526f_img_jpg'
author: 36kr
comments: false
date: Thu, 15 Jul 2021 11:20:30 GMT
thumbnail: 'https://img.36krcdn.com/20210714/v2_1be2878fe2374ced9a4ad3afb701526f_img_jpg'
---

<div>   
<blockquote> 
 <p>神译局是36氪旗下编译团队，关注科技、商业、职场、生活等领域，重点介绍国外的新技术、新观点、新风向。</p> 
</blockquote> 
<p>编者按：《时代》杂志每年年底都会评选出当年度对世界最具有影响力的<a class="project-link" data-id="3969467" data-name="人物" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969467" target="_blank">人物</a>。但，1982年的风云人物很特殊，因为当选的不是人，而是机器。这是第一次非人类当选时代年度风云人物。这个人物就是IBM PC。“有时候，出现在年度新闻中最重要的力量不是一个人，而是一个进程，一个被全体社会广泛认为正在改变所有其他进程的进程。”可以说，IBM PC的出现彻底改变了全世界的工作与生活方式。在IBM PC即将迎来诞生40周年之际，我们不妨回顾一下这台神奇机器的历史。原文发表在arstechnica网站上，标题是：The complete history of the IBM PC, part two: The DOS empire strikes。篇幅关系，我们分三部分刊出，此为第一部分。</p> 
<p><strong>相关阅读：</strong></p> 
<p><a target="_blank" rel="noopener noreferrer" href="https://36kr.com/p/preview/1Y-pmocSMjYNV5C7FHU9HcX19--Oycj6AcCKTPl_sMA9Aoc5wUNs8X0OIOJzHNWl">世纪交易：IBM 个人电脑（PC）的前世今生（一）</a></p> 
<p><a target="_blank" rel="noopener noreferrer" href="https://36kr.com/p/preview/AP_yZ7XaFibu_MNfdITv_vLsuB1wn0icp-cnDnagdAYOBylwdXQopwcxxMnF0qKq">世纪交易：IBM 个人电脑（PC）的前世今生（二）</a></p> 
<p><a target="_blank" rel="noopener noreferrer" href="https://36kr.com/p/preview/kGIVgfuuAQSt5DqgkpEOhN0LDJAYohVRa6qDuzvRnQEqNC2zoSA5iRGceYki7bkl">世纪交易：IBM 个人电脑（PC）的前世今生（三）</a></p> 
<blockquote> 
 <p><strong>划重点：</strong></p> 
 <p>IBM PC选择了8088作为CPU有多种考虑</p> 
 <p>硬件公司SCP 的 Tim Paterson一个人写出了一套操作系统QDOS</p> 
 <p>QDOS有没有抄袭CP/M一直有争议</p> 
 <p>IBM希望把软件方面的问题全推给微软，微软的“问题”将在几年内变成IBM的一个大问题</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="536,551" src="https://img.36krcdn.com/20210714/v2_1be2878fe2374ced9a4ad3afb701526f_img_jpg" referrerpolicy="no-referrer"></p> 
<p class="img-desc">英特尔 8086 芯片内核照，价格比最终将成为IBM PC内核的英特尔 8088 贵（但功能相同）。</p> 
<p class="image-wrapper"><img data-img-size-val="940,705" src="https://img.36krcdn.com/20210714/v2_fa73c63f7bdd441a8614cfd7b74da3de_img_jpeg" referrerpolicy="no-referrer"></p> 
<p class="img-desc">不起眼的 Intel 8088 CPU。</p> 
<p class="image-wrapper"><img data-img-size-val="800,424" src="https://img.36krcdn.com/20210714/v2_227065aa63944c5b997621477541f278_img_jpg" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Seattle Computer Products 生产的 Intel 8086 卡。</p> 
<p>1979 年 11 月，跟<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a>合作频繁的Seattle Computer Products 发布了一款独立的 Intel 8086 主板，以供硬核爱好者及计算机制造商尝鲜使用一下这款新型且功能强大的 CPU。8086跟 IBM 为PC 选择的 8088 密切相关；后者是前者的削减成本版，是8位/16位混合的芯片，而不是像8086那样纯16位。</p> 
<p>IBM 选择功能稍弱的 8088 部分是为了控制成本，但也是为了使用需要 8088 的 8 位外部数据总线的某些硬件。但就像经常发生的情况那样，也许最大的考虑因素是来自于营销部门而不是工程部门。8086作为芯片太强大了，以至于配备功能如此强大的 IBM PC 可能会导致部分客户选择它来代替 IBM 自己的大型系统。IBM 想挖走其他 PC 制造商的业务，而不是撬自己其他部门的墙角。</p> 
<p>不过，就我们的目的而言，需要理解的重要一点是，这两款芯片共享着相同的<a class="project-link" data-id="6632" data-name="指令集" data-logo="https://img.36krcdn.com/20210714/v2_949add4087f54678a4a1cb6db9763398_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4854500224" target="_blank">指令集</a>，所以可以跑一样的软件。人人都想在 SCP 板上跑CP/M，但 CP/M 只支持Intel 8080 和Zilog Z80。因此，SCP遇到了Jack Sams和 IBM 几个月后将要面临的同样问题。Digital Research 一再承诺会提供8086/8088 版本的 CP/M，但承诺未能兑现。于是，1980 年 4 月，SCP 的 Tim Paterson 决定自己写一套8086/8088 操作系统。他称之为 QDOS——“Quick and Dirty Operating System”（临时应急操作系统的意思）。</p> 
<p>多年来，大家一直在争论Paterson所做的事情是不是符合道德。Gary Kildall多次强硬表态称Paterson抄了CP/M的源码，但这个说法是很有问题的。甚至都没有证据表明他能不能访问到源码，因为就像当时和现在的大多数公司一样，Digital一直在小心翼翼地保护着自己的源码。</p> 
<p>但另一方面，Paterson也坦承，自己拿出了手头的CP/M 参考手册，并逐一复制了其中的每个 API 调用。从另一面的另一方面来说，虽然这种做法也许体现不出多少的原创性或创造性思维，但他的所作所为，即便按照今天的标准很明确也是合法的。法院已一再裁定 API 不受版权保护，只有具体实现才受保护，所以是允许逆向工程的。（好吧，还有专利法，但那是我们会远离的沼泽……）</p> 
<p>对于开源倡导者和微软憎恨者来说值得深思的是：如果QDOS 在道德上是不对的话，那么 Linux——基本上是对Unix标准的再次实现——肯定一样是不对的。Paterson 声称抄CP/M抄得这么厉害是<a class="project-link" data-id="1205494" data-name="有充" data-logo="https://img.36krcdn.com/20210712/v2_50cb1987094344f588b2da9f5fbd1f36_img_000" data-refer-type="1" href="https://p.36kr.com/space/3436012335" target="_blank">有充</a>分理由的：他想让程序员尽可能轻松地把现有的 CP/M 软件移植到 QDOS上个。他还声称，自己还对原有模型进行了重大改进，尤其是在磁盘以及文件处理方面。</p> 
<p>与此同时，比尔盖茨想知道他到底怎么才能在指定的时间范围内为 IBM 设计出一个操作系统。然后有一天，Paterson打电话给微软联合创始人保罗·艾伦，告诉他 QDOS 的情况，他当时想的是万一微软有兴趣为这个操作系统写一些软件或者在内部来使用。盖茨就是那个看到突然出现的救世主就能一眼认出的人，他马上打电话给Sams，问：“你是想自己弄操作系统，还是想<a class="project-link" data-id="297673" data-name="让我来" data-logo="https://img.36krcdn.com/20201112/v2_9076846c56fc4a999e22cdc3d42bd81a_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/297673" target="_blank">让我来</a>弄？” Sams对这个问题的回答，在未来几十年内将会让 IBM 付出数十亿美元的代价。“你来弄，务必要弄出来，”他说。</p> 
<p>意识到PC 软件远非自己的专长领域，Sams几乎已经把所有的系统软件问题都推给了微软，他认为现在没有理由改变方向。他后来说：“我们希望这变成他们的问题。”不过，微软的“问题”将在几年内变成IBM的一个大问题。</p> 
<h3>要有光！</h3> 
<p class="image-wrapper"><img data-img-size-val="665,1024" src="https://img.36krcdn.com/20210714/v2_3a538a90842140bb8d2b39b5799a5f61_img_jpg" referrerpolicy="no-referrer"></p> 
<p class="img-desc">史蒂夫·鲍尔默与比尔·盖茨，1986 年，PC 论坛。</p> 
<p>9 月 30 日，盖茨、史蒂夫·鲍尔默以及Bob O'Rear（微软的第七名员工）飞往佛罗里达，向 IBM提交他们的最终提案。对于想把软件问题强加给其他人的Sams来说，他们的计划看上去很理想。微软将负责提供操作系统、四种编程语言（BASIC、COBOL、Fortran 、Pascal）和一系列的其他软件（包括我们的老朋友 Microsoft Adventure）。</p> 
<p>盖茨小心地拟定了<a class="project-link" data-id="3969340" data-name="一条" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969340" target="_blank">一条</a>规定：微软会以许可方式提供所有的软件给IBM，而不是直接卖给他们，而且希望按照拷贝数支付版税。因为感觉有足够的机会让每个人都从中受益，而且让微软的命运跟IBM PC 的命运如此紧密地捆绑在<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>并没有什么坏处，IBM就同意了。这家一贯规避风险和保守的大公司，选择把自己有史以来最大的项目之一的命运交到一位 24 岁的年轻人手中。如果微软挺不过来的话，IBM PC就会胎死腹中。</p> 
<p>11 月 6 日，微软与IBM 正式签订合同，后者马上向微软支付了 700000 美元，开始把这些不同的软件全部移植到新架构上。具有讽刺意味的是，尽管IBM的Lowe 和Sams在之前的一切扮演了那么重要的角色，后来却都被调到了其他部门。Project Chess也许是独立的业务部门，但它显然并不能完全不受 IBM那种变幻无常的官僚主义做派的影响。此后，这个项目被Don Estridge接管了。</p> 
<p>在软件交易敲定的同时，Project Chess 并没有闲着。同年 11 月，微软拿到了第一和第二台原型机。IBM 非常担心保密问题，要求他们把机器保存在一个没有窗户的保险库里面，而且用的还是他们自己的锁。微软和 IBM 的 Project Chess，几乎就像这两家组织在地理上的距离但仍然都在美国一样，双方建立了一种跟今天颇为相似的工作关系，也就是地理距离的关系已经很小了。他们通过电话以及所设置的特殊电子邮件系统不断地交流，通过一项通宵服务来回传递软件包，双方还时常互相拜访——有时候甚至都没有提前通知。（微软特别担心这个。IBM有不事先通知突然查岗的习惯，目的是想看看自己拜占庭式的安全程序有没有<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>履行。）</p> 
<p>当然，IBM的团队有一堆事情可以让他们忙，但微软却要面临极大的困难。因为各种谈判，据盖茨说，等到合同敲定时进度已经“比原计划晚了三个月”。每个人都得一周7天地忙，这样连续工作数月。大多数人甚至连圣诞节都没过。</p> 
<p>第一个目标必须是让机器能够在两种操作模式下运行：BASIC 以及基于磁盘的操作系统。微软可以自己处理前者，但后者他们必须依赖eattle Computer Products。即便微软跟IBM 的交易正在敲定并开始工作，Paterson和 SCP仍一直在继续自己的工作，把QDOS 从“临时应急”的拼凑改进成可以出售的操作系统。在此过程中，出于显而易见的原因，他们把操作系统重新命名为 86-DOS。随着 1980 年接近尾声，他们终于有了一个他们认为适合外部世界的版本。</p> 
<p>译者：boxi</p>  
</div>
            