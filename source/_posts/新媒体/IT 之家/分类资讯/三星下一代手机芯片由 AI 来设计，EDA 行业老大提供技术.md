
---
title: '三星下一代手机芯片由 AI 来设计，EDA 行业老大提供技术'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/8/0e1ee82f-eea5-42b3-936e-e19afea21d81.png'
author: IT 之家
comments: false
date: Mon, 16 Aug 2021 04:47:23 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/8/0e1ee82f-eea5-42b3-936e-e19afea21d81.png'
---

<div>   
<p>刚刚发布新款折叠屏手机的三星，又搞了个大新闻：</p><p>下一代手机芯片将使用 AI 来设计。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/0e1ee82f-eea5-42b3-936e-e19afea21d81.png" w="1080" h="648" title="三星下一代手机芯片由 AI 来设计，EDA 行业老大提供技术" width="1080" height="492" referrerpolicy="no-referrer"></p><p>据外媒《连线》的报道，<span class="accentTextColor">三星将使用新思科技（Synopsys）提供的 AI 功能 ——DSO.ai—— 来设计下一代 Exynos 处理器。</span></p><p>Exynos 芯片在三星的智能手机、平板电脑中都有使用（主要是韩国与欧洲市场），并且还有少量提供给国产手机厂商使用。</p><p>新思科技是全球最大的芯片设计软件（EDA）供应商之一，这家公司的董事长表示，DSO.ai 是第一个用于处理器设计的商业 AI 软件。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/89246f43-df60-4f6d-98db-4c27c389d85c.png" w="750" h="421" title="三星下一代手机芯片由 AI 来设计，EDA 行业老大提供技术" width="750" height="421" referrerpolicy="no-referrer"></p><h2>受 AlphaZero 启发的 AI 设计师</h2><p>AI 设计芯片并非将工作全部交给 AI，而是使用强化学习自动搜索设计空间，寻求最佳解决方案。</p><p>这就要简单说一说芯片的设计流程。</p><p>首先，一款芯片要先完成其逻辑设计部分，这部分由人类工程师完成。之后开始进行布局走线设计，也就是确定每个晶体管的放置位置以及它们如何连接。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/0c84ad2f-dde5-42b2-bb63-5ebd5f0c645e.png" w="1080" h="698" title="三星下一代手机芯片由 AI 来设计，EDA 行业老大提供技术" width="1080" height="530" referrerpolicy="no-referrer"></p><p>而现代芯片一般有数十亿乃至上百亿个晶体管，设计布局和测试通常需要几个工程师花费 20~30 周才能完成。</p><p>面对“无数种”选择，最终的布局设计需要达到性能、功耗和面积（即 PPA）三个目标之前的权衡。</p><p>这个“无数种”到底有多大呢？反正比 AlphaGo 下围棋还要复杂得多。围棋的搜索空间大约有 10³⁶⁰个状态，而芯片设计可能包含 10⁹⁰⁰⁰⁰种可能性。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/297eb5c2-61e0-41b5-9ccd-1426818fd227.png" w="850" h="478" title="三星下一代手机芯片由 AI 来设计，EDA 行业老大提供技术" width="850" height="461" referrerpolicy="no-referrer"></p><p>工程师对不同的设计将如何芯片具有一种本能的理解，但是这种理解很难写成计算机代码，但却和强化学习有着异曲同工之妙。</p><p>强化学习通过奖励或惩罚来训练算法，DSO.ai 则受到 AlphaZero 的启发。</p><p>AlphaZero 通过 AI 自我博弈来学会下围棋、国际象棋，DSO.ai 通过电脑生成的大型数据流学习如何做出优化决策，在学习的过程中以更短时间找到更可靠的设计方案。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/18726943-e1e1-4ac9-ac2f-905ba3318be1.png" w="751" h="388" title="三星下一代手机芯片由 AI 来设计，EDA 行业老大提供技术" width="751" height="388" referrerpolicy="no-referrer"></p><p>△ 谷歌用 AI 找到了人类工程师（a）更好的芯片布局（b）</p><p>DSO.ai 对设计速度的提升效果明显，新思科技说，<span class="accentTextColor">这项工具在一些情况下将芯片频率提高了 18%，功耗降低了 21%，同时将工程时间从六个月缩短到了一个月。</span></p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/5770af25-0733-4359-b3aa-7e579c66b3c6.png" w="960" h="415" title="三星下一代手机芯片由 AI 来设计，EDA 行业老大提供技术" width="960" height="354" referrerpolicy="no-referrer"></p><p>△ DSO.ai 在不同芯片设计中对效率的提升</p><p>而且 AI 还会不断自学提高能力，从一个项目中获得的经验会被保留下来，用于未来的芯片设计工作。</p><h2>国外遍地开花，国内尴尬</h2><p>除了新思科技外，一些公司也在研究自己的芯片设计 AI 工具，其中最知名的就是谷歌和英伟达。</p><p>去年 4 月，谷歌团队 arXiv 发布了一篇论文，表示在 6 小时内，AI 可以生成与人类相当或者更强的芯片设计结果，最终这篇论文于两个月前正式发表在 Nature 上。</p><p>谷歌现在正将 AI 用于设计下一代 TPU。英伟达也将使用 GPU 来优化下一代 GPU 设计。</p><p>据传闻，谷歌的下一款智能手机 Pixel 6 的自研芯片也可能是使用 AI 来完成辅助设计，不过谷歌发言人拒绝对此发表评论。</p><p>另外，另一家 EDA 厂商 Cadence 也与近期推出了 AI 设计工具。</p><p>国外芯片软件技术遍地开花，而中国芯片厂商则面临着尴尬的局面。由于市场上三大 EDA 软件公司 Synopsys、Cadence、Mentor 均来自美国，且占据着中国 95% 的市场份额。</p><p>美国一些政界人士呼吁将软件加入出口管制清单，中国芯片企业可能面临着软件断供的风险。</p><p>面对国产 EDA 软件研发以及 AI 设计技术落地的不足，国内半导体行业仍然任重道远。</p>
          
</div>
            