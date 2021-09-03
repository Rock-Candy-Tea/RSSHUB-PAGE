
---
title: '特斯拉 D1 芯片遭实名 diss：内存到封装都成问题'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/9/b902ad39-8750-45b6-a015-2fb3fde3d02a.png'
author: IT 之家
comments: false
date: Fri, 03 Sep 2021 11:15:10 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/9/b902ad39-8750-45b6-a015-2fb3fde3d02a.png'
---

<div>   
<p>在今年特斯拉 AI 开放日上，D1 芯片风光无限。</p><p>独特的晶圆封装系统 + 芯片设计，让 D1 在训练万亿参数级神经网络时，可以拥有数量级优势。特斯拉更在发布会上表示，它在性能上已经完全碾压英伟达 GPU 和谷歌 TPU。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/9/b902ad39-8750-45b6-a015-2fb3fde3d02a.png" w="1080" h="589" title="特斯拉 D1 芯片遭实名 diss：内存到封装都成问题" width="1080" height="447" referrerpolicy="no-referrer"></p><p>不过，颠覆性的设计能够带来关注，也会遭到质疑。</p><p>最近，半导体分析网站 SemiAnalysis 就表示：</p><p>D1 芯片存在一些重大技术问题。</p><p>内存、成本上都有疑问</p><p>作为特斯拉首款 AI 训练芯片，D1 芯片采用分布式结构和 7nm 工艺，搭载 500 亿个晶体管、354 个训练节点，实现了超高算力和超高带宽。</p><p>根据特斯拉已经透露的信息，SemiAnalysis 从以下几个方面提出了质疑：</p><p>首先是内存问题。</p><p>SemiAnalysis 认为，D1 芯片无论在功能单元层面还是系统层面，想要达到他们所说的算力，内存可能都不够。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/9/d2a2a5e1-7282-4ab0-994c-5891a0f3abb1.png" w="1080" h="537" title="特斯拉 D1 芯片遭实名 diss：内存到封装都成问题" width="1080" height="408" referrerpolicy="no-referrer"></p><p>功能单元层面，D1 芯片的单个功能单元具有 1.25MB SRAM 缓存、1TFlop 的 FP16/CFP8 精度计算能力。</p><p>在芯片层面，裸片上没有其他 SRAM 结构，只有 354 个单元的 1.25MB SRAM 来支撑。</p><p>基于设计相似的 IPU，SemiAnalysis 推测这种设计会导致严重的内存缺陷，从而影响芯片的算力。</p><p>事实上，每个 IPU 芯片上 SRAM 的数量还是 D1 的两倍，但它在性能上和英伟达 A100 比起来，劣势依旧非常明显。</p><p>在 BERT 和 ResNet50 训练中，英伟达 A100 的速度分别是 IPU 的 1.54 倍和 1.43 倍。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/9/ad7b435c-8219-4144-903a-42b471e72f63.png" w="1080" h="168" title="特斯拉 D1 芯片遭实名 diss：内存到封装都成问题" width="1080" height="128" referrerpolicy="no-referrer"></p><p>其次，就是在成本问题上。</p><p>特斯拉 D1 芯片之间可以实现无缝融合，这使它能够达到 8 TB/s 的 IO，比 ASIC 和英伟达高出一个数量级。</p><p>为了满足这样大的 IO，特斯拉采用了独特的封装方式，即 InFO_SoW。</p><p>这种封装方式的特点就是可以够大。</p><p>在发布会上，它们也展示了由 25 个 D1 芯片组成的训练模块。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/9/ceb64f9a-b2f6-44f7-af3a-3d7082309f94.gif" w="640" h="360" title="特斯拉 D1 芯片遭实名 diss：内存到封装都成问题" width="640" height="360" referrerpolicy="no-referrer"></p><p>但这种封装方式在实际生产中的难度很高，出现报废的情况会更多，由此也会导致成本突增。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/9/b220c4f5-785c-4ec2-a55a-18355772c15f.png" w="1080" h="580" title="特斯拉 D1 芯片遭实名 diss：内存到封装都成问题" width="1080" height="440" referrerpolicy="no-referrer"></p><p>除了这两方面，SemiAnalysis 认为 D1 还有很多未解决的问题。</p><p>比如，在发布会现场被问到软件方面的问题时，特斯拉工程师甚至回答他们完全没有准备。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/9/c671878d-6cb0-43a0-a422-88cfe71b934d.png" w="1080" h="850" title="特斯拉 D1 芯片遭实名 diss：内存到封装都成问题" width="1080" height="645" referrerpolicy="no-referrer"></p><p>SRAM 方面的问题也亟需解决，否则将会面临运行速度过快的风险。</p><p>以上种种，都导致特斯拉的开发人员需要对系统进行大量的优化。</p><p>此外特斯拉透露，目前他们已经部署的 D1 芯片只有 3000 个。</p><p>如此看来，D1 芯片的摊销成本也是非常高了。</p><p>D1 真的在神坛之上吗？</p><p>事实上，在特斯拉 AI 开放日的第二天，它的股价上涨甚至还不如英伟达。</p><p>可见投资界对于马斯克带来的新技术，也都非常冷静。</p><p>有人表示，特斯拉把技术封锁在自己的堡垒内，外界无法测评，也就无从得知它真正的优势和局限性。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/9/8baf473c-1bca-46b1-93fc-83148fae387d.png" w="1080" h="139" title="特斯拉 D1 芯片遭实名 diss：内存到封装都成问题" width="1080" height="106" referrerpolicy="no-referrer"></p><p>这一次向特斯拉开怼的是 SemiAnalysis，它是一家半导体分析评论网站，首席分析师为 Dylan Patel，毕业于佐治亚大学特里商学院。</p><blockquote><p>参考链接：</p><p>[1]https://semianalysis.com/the-tesla-dojo-chip-is-impressive-but-there-are-some-major-technical-issues/</p><p>[2]https://news.ycombinator.com/item?id=28361807</p><p>[3]https://www.linkedin.com/in/dylanpatelsa/</p></blockquote>
          
</div>
            