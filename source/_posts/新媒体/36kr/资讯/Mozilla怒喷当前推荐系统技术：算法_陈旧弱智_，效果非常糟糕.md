
---
title: 'Mozilla怒喷当前推荐系统技术：算法_陈旧弱智_，效果非常糟糕'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6483'
author: 36kr
comments: false
date: Fri, 09 Jul 2021 06:43:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=6483'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/zIcq8Ji6UZRv-Mnp-NzOow">“InfoQ”（ID:infoqchina）</a>，作者：核子可乐、Tina，36氪经授权发布。</p> 
<blockquote> 
 <p>Mozilla 喷当前视频平台引领者所使用的推荐系统技术：使用的算法“陈旧弱智”，效果非常“糟糕”，堪称“恐怖秀”。</p> 
</blockquote> 
<p>根据 Mozilla 本周三发布的调查研究结果表明，大部分饱受用户们吐槽的 YouTube 视频推荐内容都出自该网站陈旧的 AI 算法之手。</p> 
<p>该调查研究从去年 9 月开始启动，总共涉及到 37380 名 YouTube 观众。根据 Mozilla 的报告，这是同类研究中规模最大的一次，而且显示出来的结果只是“冰山的一角”，其中每项发现都值得进一步跟踪并做出深刻剖析。</p> 
<p>Mozilla 敦促 YouTub 对内容审核与推荐模型予以透明化公开，并建议给用户提供退出个性化推荐的选项。但 YouTube 每季度从广告中获得的收入高达 60 亿美元，实现提供退出“个性化推荐“选项不太可能。</p> 
<h2>1 这套推荐系统已经用了十几年，但还存在哪些问题？</h2> 
<p>对比成立于 2015 年的<a class="project-link" data-id="30859" data-name="快手" data-logo="https://img.36krcdn.com/20200729/v2_a1a6228d3ad9447592b615f38c6bd7a3_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/30859" target="_blank">快手</a>，2016 年上线的抖音， 创建于 2005 年的 YouTube 算是推荐系统技术的早期引路人。</p> 
<p>YouTube 成立没多久，网站上的视频数量就迅猛增长，成为全球最大的视频网站。截止 2008 年，整个 YouTube 视频量已突破四千五百万，每分钟上传视频量 7 小时。截止 2014 年，每分钟上传视频量超过 100 小时。2019 年，月度活跃用户达 19 亿。如此庞大的视频量，使得用户难以搜索到其感兴趣的视频。YouTube 的成功最终得益于推荐系统，同时它也是实时大规模推荐系统技术的<a class="project-link" data-id="25594" data-name="探路者" data-logo="https://img.36krcdn.com/20201021/v2_1cca3ab3e1f74da3bd7e1436d9234448_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25594" target="_blank">探路者</a>。</p> 
<p>虽然多年来一直被用户吐槽视频推荐效果，但 YouTube 在该研究方向上却处于业界前沿。几篇已经发表的论文显示，2008 年 YouTube 研究并使用了基于用户 - 视频图的随机遍历算法；2010 年，算法升级为基于物品的协同过滤算法；2013 年将推荐问题转换成多分类问题，并解决从神经网络最后的众多输出节点中找出最大概率的输出节点。此举也为 2016 年将推荐核心算法升级为深度学习算法打下了基础。这几篇论文《Video Suggestion and Discovery for YouTube》、《The YouTube Video Recommendation System》、《Label Partitioning For Sublinear Ranking》、《Deep Neural Networks for YouTube Recommendations》和《Recommending what video to watch next: A multitask ranking system》都是推荐系统的典范之作。</p> 
<p>从去年开始，来自 190 个国家的总计 37380 名 YouTube 观众自愿参加了这项由 Mozilla 牵头开展的众包研究；在 2020 年 7 月至 2021 年 5 月期间，Mozzila 共收到 3362 份关于不感兴趣视频的提交报告。</p> 
<p>根据本周三发布的调查结果，“YouTube 推荐算法自身只是问题的缩影，由此可以想见商业算法正在给民众的生活蒙上一层不透明、不确定的阴影。”</p> 
<p>“YouTube 的算法每天向用户提供约 7 亿小时的视频观看时长，但公众对其底层运作方式可谓知之甚少。我们甚至找不到任何官方支持的研究方法。”</p> 
<p>作为火狐浏览器的开发商，Mozilla 公司开发出一款名为 RegretsReporter 的浏览器扩展供 YouTube 用户们下载。在安装之后，该扩展程序会记录网民在 YouTube 上的观看活动、记录所观看视频的详细信息，并允许用户轻松标记出自己觉得根本不感兴趣的内容。通过将数据汇集起来并加以分析，Mozilla 希望深入研究 YouTube 推荐引擎的行为模式与实际效果。</p> 
<p>这项研究的结果有几项亮点：</p> 
<ul> 
 <li>志愿参与调查的用户们也有多种不同的抗拒理由，有些视频与政治阴谋论有关、有些是与 COVID-19 疫苗相关的虚假信息、也有一些是对热门大片《玩具总动员》的拙劣模仿。</li> 
 <li>Mozilla 研究人员发现，在志愿参与调查的用户们提交的全部不感兴趣视频中，有 71% 来自 YouTube 平台的 whiz-bang AI 推荐算法。</li> 
 <li>他们估计，在被举报的视频中，甚至有 12.2% 的内容有违 YouTube 自己提出的视频管理方针及政策——换句话说，这些视频压根不应该出现在 YouTube 网站上，但推荐算法居然还将其广泛传阅。</li> 
 <li>研究还发现，推荐的视频被志愿者举报的可能性比他们自己搜索到的视频高 40%。</li> 
 <li>在 Mozilla 志愿者对视频进行负面反馈后，只有 43.6% 的推荐与志愿者之前观看的视频完全无关。</li> 
 <li>YouTube 推荐算法在非英语国家的表现似乎更差。其中巴西、德国与法国的推荐质量最差，美国和英国则分别排名第八位与第十六位。</li> 
</ul> 
<h2>2 必须承认的是，当前软件并不够完美</h2> 
<p>多年来，YouTube 的视频推荐算法一直被指责通过向公众投放经过放大的仇恨言论、政治极端主义、虚假垃圾信息，助长了社会弊病，以此谋取数十亿人的眼球，从而增加广告收入。</p> 
<p>虽然 YouTube 的母公司<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>偶尔会对围绕算法爆发出来的反对意见做出回应：宣布一些政策调整，以及限制或清除奇怪的仇恨账户，但不确定 YouTube 什么时候会重启这些诱导用户点击不健康视频的规则。根据 Mozilla 的研究，YouTube 的人工智能仍然表现得如此糟糕，这也表明谷歌在用肤浅的改革主张模糊这方面的批评。</p> 
<p>谷歌公司一位发言人在声明中表示，“我们这套推荐系统的目标，是帮助观众快速找到自己喜爱的内容。这套系统光是在主页上的单日推荐量就超过 2 亿条视频。”</p> 
<p>“我们使用超过 800 亿条信息为推荐系统提供指引，包括观众对感兴趣内容的调查回复。我们一直致力于改善 YouTube 平台的观看体验；单在过去一年，我们就推出了 30 多项不同调整，希望减少有害内容的推荐比例。伴随这项举措，用户以推荐方式接触到极端视频内容的几率已经远低于 1%。”</p> 
<p>据报道，YouTube 最终删除了近 200 个志愿者在这次调查中反馈过的视频。这些视频在被删除之前总共有 1.6 亿次观看。</p> 
<p>YouTube 多年来一直在努力改善推荐系统，并不断调整以提高效果表现。但必须承认，这款自动化软件仍然不够完美——特别是还在将有违内容管理政策的视频推荐给用户。Mozilla 认为，造成这种结果的核心原因，在于 YouTube 一直对所使用的自家的推荐算法底层逻辑三缄其口。</p> 
<p>报告指出，“我们认为，此次研究揭露出的总是还只是冰山一角；其中每项发现都值得进一步跟踪并做出深刻剖析。”</p> 
<p>“我们还意识到，如果不加以干预并对 YouTube 算法开展更严格的审查，那么相关问题将继续失控蔓延，最终给整个互联网社区产生愈发恶劣的影响。尽管 YouTube 方面宣称已经在一部分问题上取得了进展，但研究人员几乎无法验证这些说法，也极难对 YouTube 推荐算法进行真正有意义的研究。”</p> 
<p>Mozilla 公司认为，YouTube 应该发布关于其推荐系统工作原理的数据，并对内容审核与推荐模型予以透明化公开。只有这样，研究人员才能真正以独立方式对这款 AI 软件开展审计。</p> 
<p>参考链接：</p> 
<p>https://www.theregister.com/2021/07/08/youtubes_mozilla_algorithm/</p>  
</div>
            