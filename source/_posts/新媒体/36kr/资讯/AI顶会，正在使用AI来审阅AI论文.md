
---
title: 'AI顶会，正在使用AI来审阅AI论文'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210402/v2_d7547cc9ec9e42dd9a3ae753bbb5e659_img_000'
author: 36kr
comments: false
date: Fri, 02 Apr 2021 06:44:18 GMT
thumbnail: 'https://img.36krcdn.com/20210402/v2_d7547cc9ec9e42dd9a3ae753bbb5e659_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/M1wMu8rq2CDS8Ptbm8037A">“机器之心”（ID:almosthuman2014）</a>，编辑：蛋酱、泽南，36氪经授权发布。</p> 
<p>近年来我们在报道 AI 顶会的文章里不断听到「史上最大」、「论文数量新高」等字眼，论文的审核俨然成了一项挑战。但既然是在研究 AI，为什么不让机器来自动解决问题？</p> 
<p class="image-wrapper"><img data-img-size-val="1080,608" src="https://img.36krcdn.com/20210402/v2_d7547cc9ec9e42dd9a3ae753bbb5e659_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">人工智能顶会 NeurIPS 2019 的现场，曾被人吐槽像跨年夜的百货商场。</p> 
<p>对于大多数科学领域来说，期刊是同行评审和论文发表的主阵地，编辑们会根据专业判断将论文分配给合适的审稿人。但在计算机科学领域，寻找审稿人的过程通常是匆匆忙忙的：大多数论文是一次性提交给年度大会，组织者需要在仅仅一周的时间内将成千上万的论文分配给成千上万的审稿人。</p> 
<p>这样的节奏是非常紧张的，在过去的五年内，大型 AI 会议的投稿量增长了三倍不止，也给大会主办机构带来了不小的压力。举个例子，人工智能领域最大规模的定会 NeurIPS 2020 收到了 9000 多份有效投稿，比上一年增长了 40%。组织者不得不将 3 万多个审稿任务分派给约 7000 位审稿人。NeurIPS 2020 大会主席 Marc’Aurelio Ranzato 表示：「这非常累，压力很大。」</p> 
<p>大概也是「近水楼台先得月」，AI 顶会的审稿工作<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>了 AI 的协助。首先，主办方使用了 Toronto Paper Matching System (TPMS)，在此之前 TPMS 也被应用于其他多个会议的投递论文分配工作，它通过对比投稿论文和审稿人研究工作之间的文本，来计算投稿与审稿人专业知识之间的相关性。这个筛选过程是匹配系统中的一部分，期间审稿人也可以主动争取自己希望审阅的论文。</p> 
<p class="image-wrapper"><img data-img-size-val="430,204" src="https://img.36krcdn.com/20210402/v2_7382caa6ac784ccbb7e45ac1111ec955_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">TPMS 架构，该系统可通过会议管理系统在线使用。</p> 
<p>同时还有方法更加优化的 AI 软件：论文审阅平台 OpenReview 开发了一种「亲和力评测」系统，借助了神经网络「Spectre」来分析论文标题和摘要。OpenReview 和麻省大学阿默斯特分校的计算机科学家 Melisa Bok 和 Haw-Shiuan Chang 表示，包括 NeurIPS 在内的一些计算机科学大会将在今年把亲和力评测系统与 TPMS 结合使用。</p> 
<p>AI 会议的组织者希望通过提高匹配质量来推动同行评审和出版论文的质量。2014 年的一项研究表明这仍有进步空间，作为测试，当年 NeurIPS 中 10% 的投稿论文分别有两组审稿人审阅，在一组中被全部接收，另一组仅接收了 57%。影响到结果的因素可能有很多，但可以确定的是，对于具体某一篇论文来说，至少某一个小组是缺乏评估的专业知识的。</p> 
<p>为了提升匹配质量，CMU 的计算机科学家 Ivan Stelmakh 开发了一种名为「 PeerReview4All」的算法，通常匹配系统会最大程度地提升论文和审稿人之间的平均亲和力，但有可能出现「厚此薄彼」的现象。PeerReview4All 旨在最大程度地提升最差匹配的质量，注重增加该过程的公平性。</p> 
<p>Ivan Stelmakh 在去年的 ICML 大会使用了 PeerReview4All 进行试验，并在今年的 AAAI 大会上介绍了这一结果。他表示，该方法在不损害平均匹配质量的情况下显著提高了公平性。</p> 
<p>具体结论可以参考 Ivan Stelmakh 所写的这篇 2 页论文：https://www.aaai.org/AAAI21Papers/DC-169.StelmakhI.pdf</p> 
<p class="image-wrapper"><img data-img-size-val="774,375" src="https://img.36krcdn.com/20210402/v2_a2f62b4b859140fdbf0644f5ea75b43d_img_000" referrerpolicy="no-referrer"></p> 
<p>OpenReview 也已经开始提供一种旨在提高公平性的系统，称为「FairFlow」。根据 NeurIPS 2021 Call for Papers 页面，今年的 NeurIPS 将使用 OpenReview 进行审稿工作。雅虎计算机科学家、NeurIPS 2021 高级程序主席 Alina Beygelzimer 表示，NeurIPS 今年将至少尝试上述中的一种匹配方法。</p> 
<p>这些系统的作用都是将一组已知的论文与一组已知的审稿人进行匹配，但还有另外一个问题：随着 AI 领域的不断发展，顶会还需要招募、评估、培训新的审稿人。针对此，Ivan Stelmakh 正在进行一项最新实验，探索一种不依赖 AI 来减轻这些任务负担的方法。</p> 
<p>他们在去年的 ICML 上，邀请了一些学生和刚刚毕业的人去审阅从同事那里收集的未发表论文（134 篇）。随后团队邀请了 52 位成员加入审稿人团体，并为他们分配了一位资深研究人员担任导师。最终这些新手审稿人的工作成果还不错，与那些经验丰富的审稿人相差无几。借此 Ivan Stelmakh 证明了：主办方可以在不增加负担的情况下扩招数百名审稿人，「且这些候选审稿人极具热情」。</p> 
<p>使用亲和力来评估审稿人专业知识的匹配系统也可以让身高人们对评审一篇论文进行「招标」，最近的一些工作试图解决这种方法中的潜在偏见。我们有时会听到选论文的审核者只选择朋友的论文，这实际上是在破解算法。</p> 
<p>今年 2 月，康奈尔大学、Facebook 一篇发在 arXiv 上的论文《Making Paper Reviewing Robust to Bid Manipulation Attacks 》描述了使用机器学习来过滤可疑论文审核竞标的过滤方法。在模拟数据集上，即使潜在作弊者知道系统的运行方式，它也可以减少操纵，而不会降低评审质量。去年在 NeurIPS 上的另一种算法《Mitigating Manipulation in Peer Review via Randomized Reviewer Assignments》实质上是对在专业领域以外的论文进行投标的人进行惩罚。</p> 
<p>研究人员通过结合模拟竞价和上次会议的真实数据证明了其方法在减少操纵方面的有效性。</p> 
<p>这些工具面临的问题是——你很难评估它们在实际使用过程中是不是真的优于其他方法。蒙特利尔大学计算机科学家 Laurent Charlin 表示，要想掌握确凿的证据需要进行对照试验，但现在没有任何试验。其中一部分原因是因为其中许多工具都是新的。</p> 
<p>十年前开发 TPMS 工具的亲和性测量工具的 Charlin 表示，随着这些技术的发展，类似的方法可能会在某一天开始帮助计算机科学领域以外的同行审阅者。但是到目前为止，这种方法的应有范围还很有限。</p> 
<p>美国科学促进会 AAAS（《Science》等杂志的主办方）发言人梅根 · 费伦（Meagan Phelan）表示 AAAS 在分配同行审阅者时没有使用 AI。</p> 
<p>「但在人工智能领域里，」Charlin 说道，「作为一个具有一定自动化程度水平的领域。我们没有理由不使用自己的工具。」</p> 
<h3>参考内容：</h3> 
<p>https://www.sciencemag.org/news/2021/04/ai-conferences-use-ai-assign-papers-reviewers</p>  
</div>
            