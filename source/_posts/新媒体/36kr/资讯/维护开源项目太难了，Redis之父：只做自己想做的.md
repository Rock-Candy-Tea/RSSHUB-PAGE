
---
title: '维护开源项目太难了，Redis之父：只做自己想做的'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210611/v2_b27aa28905ed4ef6857cfc126aeb5b67_img_000'
author: 36kr
comments: false
date: Fri, 11 Jun 2021 07:32:46 GMT
thumbnail: 'https://img.36krcdn.com/20210611/v2_b27aa28905ed4ef6857cfc126aeb5b67_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/Di-yGgjFxed5Prt3h8h_FA">“InfoQ”（ID:infoqchina）</a>，作者：<a class="project-link" data-id="659552" data-name="万佳" data-logo="https://img.36krcdn.com/20201113/v2_093ffc0f84be4065b709ccb4815f2e4e_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/659552" target="_blank">万佳</a>、Tina，36氪经授权发布。</p> 
<blockquote> 
 <p>开源正在吞噬世界，但开源维护者却都身处水深火热之中。</p> 
</blockquote> 
<p>最近，开源项目 Docz 作者 Pedro 发表短文称繁重的开源维护工作不可持续，自己曾处于“崩溃”状态。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_b27aa28905ed4ef6857cfc126aeb5b67_img_000" data-img-size-val="1080,289" referrerpolicy="no-referrer"></p> 
<p>Pedro 表示最初为了开发 Docz，他可以提前 3 小时起床，推迟 3 小时睡觉，全力以赴地创建这个项目的经历让他“感觉很棒”。但随着项目的发展，使用的人越来越多，需求也日渐增多，维护开源变成了一件非常困难的事情。很多人只想索取，而不是提供帮助，这让他感到“崩溃”。</p> 
<p>而且 Pedro 除了自己的本职工作外，还得抽时间维护自己的开源项目，最后却损害了自己的身体健康。他不得已在“保持开源项目活跃度”和“保持健康”之间选择了后者。这给项目带来了一种非常糟糕的状态，导致很长一段时间里没有人来维护它。</p> 
<p>对此，众多开源维护者纷纷表示有同感，包括 Redis 之父 antirez 也发表了自己的看法。</p> 
<p>Redis 之父 Salvatore Sanfilippo（又名 antirez），是资深的开源维护者，开发了很多不同规模的 OSS 项目，如 Redis、Hping、Jim Tcl、Visitors web analyzer 等等。antirez 以他丰富的维护经验说道，开源维护并不是要满足所有人的要求，也不是什么都不做，而是需要挑选你想要解决的问题，“只做自己想做的 (just do what you want)”，并且“花固定时间，甚至每天几分钟都行，在这段时间只做你喜欢做的事情”。</p> 
<p>antirez 表示自己正是通过这样的方式写出了 Redis ，这个由他一个人写出的产品在市场上击败了许多数百名开发者<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210601/v2_2bbe1c6ad79748b3be29e04d8999edac_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>打造的同类项目。同时，他还提出了几个要点：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>不要以为别人在没有付出的条件下向你索取是在犯错或是在滥用“权力”。事实上，人们可以提出任何要求，但你也可以忽略这些要求。</p></li> 
 <li><p>不要因为软件是免费的而陷入对软件质量不负责任的陷阱：只做自己想做的事，认真完成工作，并形成良好的文档。不要因为因为“它是免费的”就发布一些糟糕的东西，另外就是按照你想要的方式做事，但要带着爱。</p></li> 
 <li><p>当被人攻击时，平静地回答自己的想法，不要陷入争论。</p></li> 
 <li><p>在参与开源过程中结交好朋友。因为当遇到困难的时候，他们会给你极大的帮助。请记住：聪明人往往都是友好的。</p></li> 
</ul> 
<h2 label="一级标题" style>1 开源项目维护者的窘境：工作忙，薪水低</h2> 
<p>2011 年，Mosaic 的创始人‍‍马克·安德森说过这么一句话：软件正在吞食整个世界；2013 年，‍‍麦克·斯考克对这句话进行了扩展：开源软件正在吞食整个世界。但这些开源软件背后的维护者却都身处水深火热之中。</p> 
<p><strong>活儿多，工作强度大</strong></p> 
<p>此前，坐拥百万用户的开源项目 Babel 引起开发者关注。Babel 宣布，尽管有 Airbnb、Facebook、Salesforce、Gitpod、GatsbyJS、Discord 和 Elastic 等企业的赞助，但由于花钱速度继续高于获取捐赠的速度，项目储备资<a class="project-link" data-id="3968359" data-name="金目" data-logo="https://img.36krcdn.com/20210601/v2_e07117195f374cf384a4035b92e5f658_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4460100123" target="_blank">金目</a>前只够维持到 2021 年底。</p> 
<p>去年，Redis 之父宣布退出开源项目维护，他说：“最近几年来，我每天的工作内容发生了很大变化。我把大部分精力花在检查其他开发者提交的 Redis 代码、改进代码质量以及提升软件正确性、速度与安全性方面。但我真的不喜欢这类维护工作。”</p> 
<p>更重要的是，这种全年无休的上班生活让他无法放松，从而无法做一些创造性的工作。</p> 
<p>开源项目维护工作是一项艰巨的任务。如果说开发者的职责在于修复 bug、新建功能，而审查者的职责在于把控代码质量，那么维护者就是要让开源项目长久稳定地持续下去。</p> 
<p>可以想见，正常的开源项目中必然是开发者多于审查者、审查者又多于维护者。维护者相当于一支管弦乐团中的指挥角色。如果开发者没能修复 bug，维护者需要及时救场；如果代码未经审查，维护者也得尽快介入。</p> 
<p>另外，对于像 Linux 这样的大型项目，每周维护者大约需要面对数百项代码补丁，工作强度可想而知。</p> 
<p><strong>大多数开源项目维护者“穷的可伶”</strong></p> 
<p>近日，零日漏洞代理公司 Zerodium 宣布，正在寻找影响 Windows 和 Linux 上 Pidgin 的零日漏洞。为获得其零日漏洞，该公司出价 10 万美元。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_afe051e938f74a839590831d9b29e9cf_img_000" data-img-size-val="823,459" referrerpolicy="no-referrer"></p> 
<p>对此，网名叫 Gary Kramlich 的网友发推文回应，“这真实表明了开源软件悲惨的资金状况。去年，我全职为维护 Pidgin 项目工作，薪水只有 2.5 万美元，但是如果你能在我的工作和其他人的无偿工作中挖到安全漏洞，你赚取的收入将是我的 4 倍。”</p> 
<p>据悉，Pidgin 是一款免费和开源的多平台即时通讯客户端。早在 2007 年，Pidgin 已经有 300 万名用户。</p> 
<p>根据 Tidelift 发布的调查报告显示，近 50% 开源项目维护者拿不到任何报酬。</p> 
<p>大多数开源项目维护者“穷的可伶”。虽然 Linus Torvalds 和 Kroah-Hartman 等 Linux 顶尖维护者的收入确实可观，但是 Tidelift 的一项最新调查发现，46% 的开源项目维护者根本拿不到任何报酬。即使在拥有报酬的维护者中，也只有 26% 的比例年均工作收入超过 1000 美元。</p> 
<p>根据 Linux 基金会开源安全基金会（OSSF）与哈佛创新科学实验室（LISH）最近发布的 2020 年 FOSS 贡献者调查报告显示，开发者参与开源项目的首要原因，在于添加自己需要的功能或者是改进正在使用的功能；第二大原因就是享受学习感、满足感、创造性以及令人愉悦的工作内容。最后<a class="project-link" data-id="3969340" data-name="一条" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969340" target="_blank">一条</a>，才是获取报酬。</p> 
<p>但是，不管你是开发者，还是审查者或维护者，这并不代表获取报酬不重要。ZDNet 对此评论，“志愿服务的目标在于自我实现，而非无家可归。”</p> 
<p>根据 Tidelift 的调查表明，大多数人只是还没开始留意贡献工作的无偿属性。在年收益不足 1000 美元的受访者中，只有 18% 表示自己对报酬较为看重；但每年能拿到 10000 美元以上的维护者中，高达 61% 的受访者开始正视薪酬的重要意义。</p> 
<p>Tidelift 公司 CEO 兼联合创始人 Donald Fischer 表示，“整个世界都依赖于开源组件为应用程序提供动力，但我们的调查数据显示，负责建立并维持开源体系良好运行的维护者们并没能拿到适当的收益。必须开辟出一条更安全、更健康的开源软件供应链发展道路，也必须保证能有更多的志愿维护者能因自己做出的卓越贡献拿到充足的报酬。”</p> 
<p>在调查当中，近半数受访者（49%）将“我的工作完全没有或者没有<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>相应的经济报偿”作为不想担任维护者的首要原因，其次则是“会增加我的个人压力”（45%）以及“感觉不受重视、或者会吃力不讨好”（40%）。</p> 
<p>事实上，超过半数（59%）的受访维护者已经或者正在考虑退出项目维护工作。</p> 
<p>而维护者同时管理的项目越多，决定中途放弃的可能性就越大——在同时管理 10 个甚至更多项目的维护者中，有超过三分之二（68%）已经退出或者正考虑退出。</p> 
<h2 label="一级标题" style>2 写在最后</h2> 
<p>当今，开源已经成为一股潮流，开源文化流行，开源项目层出不穷。但是，我们也看到无数的开源项目逐渐衰落，被人遗弃，被人淡忘。想让一个开源项目具有长久的生命力，开源项目维护无疑是亟待解决的首要问题。</p> 
<p>参考链接：</p> 
<p>https://news.ycombinator.com/item?id=27420554</p> 
<p>https://www.infoq.cn/article/xuuw7UCl5ReSwo7zr6oP</p>  
</div>
            