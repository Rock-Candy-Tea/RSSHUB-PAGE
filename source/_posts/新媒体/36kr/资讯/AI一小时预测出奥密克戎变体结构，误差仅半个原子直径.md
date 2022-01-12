
---
title: 'AI一小时预测出奥密克戎变体结构，误差仅半个原子直径'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220112/v2_6dc7da2b41ed457f9d4a7f6a62babdae_img_000'
author: 36kr
comments: false
date: Wed, 12 Jan 2022 08:07:19 GMT
thumbnail: 'https://img.36krcdn.com/20220112/v2_6dc7da2b41ed457f9d4a7f6a62babdae_img_000'
---

<div>   
<p>就在这两天，“天津迎战新冠变异病毒<strong>奥密克戎</strong>（Omicron）”引发了高度关注。</p> 
<p>奥密克戎最早发现于南非，并且席卷了大半个世界，在被发现时已经传播三代。</p> 
<p>天津作为此次防疫“主战场”，截至昨日12时，已经累计97例阳性。</p> 
<p>抗击疫情，刻不容缓。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220112/v2_6dc7da2b41ed457f9d4a7f6a62babdae_img_000" referrerpolicy="no-referrer"></p> 
<p>而与此同时，全球科学家对奥密克戎的研究也没有停滞。</p> 
<p>来自北卡罗来纳大学夏洛特分校的<strong>Colby Ford</strong>研究团队，便在近日发布了其最新研究成果：</p> 
<blockquote> 
 <p>利用AI技术，<strong>几乎准确地预测了奥米克戎的复杂结构</strong>。</p> 
</blockquote> 
<p>他们的工作可以说是“站在巨人的肩膀上”，具体而言，就是利用<strong> AlphaFold2</strong>和<strong>RoseTTAFold</strong>，由此预测出了3D蛋白质结构。</p> 
<p>在论文中，Ford对研究结果是这样总结的：</p> 
<blockquote> 
 <p>奥密克戎受体结合域（RBD）的一些结构变化，可能会<strong>减少抗体相互作用</strong>，但不会完全避开现有的中和性抗体。</p> 
</blockquote> 
<p>简单来说，就是现有疫苗对奥密克戎病毒有用，但由于其结构的改变，降低了抗体的识别能力。</p> 
<p>这就能解释，为何现有的奥密克戎感染病例中有已经打过疫苗的患者了。</p> 
<p>但这项研究所提供更深远的意义，正如《连线》杂志评价的那样：</p> 
<blockquote> 
 <p>可以为未来的药物指明方向。</p> 
</blockquote> 
<h2><strong>AI一小时预测奥密克戎结构</strong></h2> 
<p>关于这项研究，还得追溯到去年的11月27日。</p> 
<p>当日凌晨，世卫组织将这个新冠“最凶变种”正式命名为<strong>Omicron</strong>。</p> 
<p>而就在第二天，不列颠哥伦比亚大学（UBC）的<strong>Sriram Subramaniam</strong> 便火速下载了发布在网上的基因序列组，还安排把奥密克戎的DNA 样本运送到实验室中。</p> 
<p>他们想采用的方法是通过显微镜来揭示奥密克戎的蛋白质3D结构。</p> 
<p>与此同时，<strong>Colby Ford</strong>也在密切关注着这件事情。</p> 
<p>也是在世卫组织正式命名的前后脚，他尝试用免费的AI软件，从奥密克戎基因组编码的氨基酸序列中预测其结构。</p> 
<p>仅仅<strong>1小时</strong>之后，Ford便<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20210807/v2_966db147ab4646ef82349f069ce61219_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>了他的第一个结果，并且很快将它们发布到了网上。</p> 
<p>Subramaniam则是在12月21日，发表了他们通过显微镜得到的结果。</p> 
<p>最终结果表明，Ford用AI技术预测的2个蛋白质结构中，有一个被证明是与Subramaniam真实观测结果高度接近——</p> 
<blockquote> 
 <p>中心原子的位置误差只有约半埃（大约是氢原子的半径）。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220112/v2_51e1b27602c84eafbaee978566c90ee1_img_000" referrerpolicy="no-referrer"></p> 
<p>不过Ford认为，对于新冠这类病毒，研究上的<strong>时效</strong>显得格外重要，毕竟其传播的凶猛程度也是有目共睹的。</p> 
<p>至于Ford所采用的AI方法，也正如刚才提到的，是基AlphaFold2和RoseTTAFold。</p> 
<p>整体而言，他的研究主要包含三大方面。</p> 
<p>第一步，是<strong>监测变种</strong>（VBM）和<strong>关切变种</strong>（VOC）的序列比较。</p> 
<p>Ford团队下载了新冠病毒的参考基因组，以及各种VOC和VBM的前100个全基因组序列。</p> 
<p>对这些基因组再进行一个“对齐”和“修剪”的工作，最终留下了1026条序列。</p> 
<p>基于此，Ford对这1026条序列进行“注释”，再根据序列相似性确定了该序列上的受体结合基序。</p> 
<p>然后，他们用MEGA11.0.10版计算每对序列之间的成对p-距离，再使用标准翻译表将尖峰蛋白的这个变体核苷酸序列翻译成氨基酸。</p> 
<p>最终对该序列进行修剪，使其只包含穗状蛋白的RBD（第319至541位）。</p> 
<p>第二步，是<strong>RBD的结构预测</strong>。</p> 
<p>Ford在这一步中，基于上面得到奥密克戎衍生RBD氨基酸序列，使用AlphaFold2和RoseTTAFold创建了预测的3D蛋白质结构。</p> 
<p>基于AlphaFold2的预测，是在 “单一序列 “模式下使用PTM方法（predicted TM-score）运行。</p> 
<p>而基于RoseTTAFold的预测，则是用 “mmseqs2 “模式运行的。</p> 
<p>这两个系统都产生了奥密克戎的预测RBD结构，以及围绕多序列比对覆盖率、预测比对误差（PAE）和预测置信度（pLDDT）等指标。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220112/v2_05c350f61d4e42679a4ce5d336f0e53f_img_000" referrerpolicy="no-referrer"></p> 
<p>第三步，是<strong> 中和抗体相互作用模拟</strong>。</p> 
<p>在这个步骤中，Ford团队基于上面得到的奥密克戎RBD预测结构，模拟了与四个现有中和抗体结构的相互作用（分别为C105, CC12.1, CC12.3, and CV30）。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220112/v2_248283c840104a85a4262add8da01bbe_img_000" referrerpolicy="no-referrer"></p> 
<p>在这个过程中，他们只使用抗体结构的一个单片段抗原结合（Fab）区域，作为对接的位置。</p> 
<p>接下来，他们用到了生物分子建模软件HADDOCK，来预测RBD表位与中和抗体结构的副体之间的结合亲和力。</p> 
<p>最后，Ford团队将实际复合物（即真正的RBD结构和Fab）与奥密克戎的预测RBD结构（有相同的Fab）的指标进行了比较。</p> 
<p>……</p> 
<p>而从实验结果上来看，现有的中和抗体可能仍然会与奥密克戎变异的突变刺突蛋白结合。</p> 
<p>然而，与参考RBD结构相比，奥密克戎的RBD对中和抗体的亲和力似乎降低了。</p> 
<p>AlphaFold2和RoseTTAFold的结果都表明，以前感染的抗体至少会对奥密克戎提供一些保护。</p> 
<p>而也正因如此，加之此次奥密克戎患者的症状并没有此前德尔塔那般严重，许多人都把它比作“大号感冒”。</p> 
<p>但事实是否真的如此呢？</p> 
<h2><strong>张伯礼：奥密克戎并非“大号感冒”</strong></h2> 
<p>也就在天津这两天天津疫情被高度关注之际，国内专家已经站出来对“大号感冒”的说法做出了解释。</p> 
<p>国家传染病医学中心主任<strong>张文宏</strong>认为：</p> 
<blockquote> 
 <p>对于已经获得免疫力的人来讲，它是个“大号流感”。</p> 
 <p>如果你的免疫力不够强大，奥密克戎不是“大号流感”；如果没有很好的医疗资源，奥密克戎是会“咬人”的。</p> 
</blockquote> 
<p>中国工程院院士<strong>张伯礼</strong>也表示：</p> 
<blockquote> 
 <p>奥密克戎和“大号流感”并不一样，在国外大概有百分之五六十的病人出现了持续症状或后遗症，但一般的流感不会出现这么多。</p> 
</blockquote> 
<p>而就在最近，世卫组织也对奥密克戎发出警告，称“尽管其毒性可能较弱，但不能低估了它”。</p> 
<p>甚至还做出了“或在6到8周内感染半数以上欧洲人”的预测。</p> 
<p>因此，<strong>做好防疫措施</strong>依然是重中之重。</p> 
<p>对此，汕头大学病毒学专家常荣山建议，“没有准备N95或KN95口罩的天津市民，外出时应当戴双层外科口罩，或在布口罩外面套戴一个外科口罩增强密闭性”。</p> 
<p>他表示：</p> 
<blockquote> 
 <p>叠加两个口罩的保护效果为90%，即可以减少90%的传染概率，而单个口罩的效果则为70%。</p> 
</blockquote> 
<p>参考链接：</p> 
<p>[1]<a href="https://www.wired.com/story/ai-software-nearly-predicted-omicrons-tricky-structure/[2]https://www.biorxiv.org/content/10.1101/2021.12.03.471024v4.full" _src="https://www.wired.com/story/ai-software-nearly-predicted-omicrons-tricky-structure/[2]https://www.biorxiv.org/content/10.1101/2021.12.03.471024v4.full">https://www.wired.com/story/ai-software-nearly-predicted-omicrons-tricky-structure/</a></p> 
<p><a href="https://www.wired.com/story/ai-software-nearly-predicted-omicrons-tricky-structure/[2]https://www.biorxiv.org/content/10.1101/2021.12.03.471024v4.full" _src="https://www.wired.com/story/ai-software-nearly-predicted-omicrons-tricky-structure/[2]https://www.biorxiv.org/content/10.1101/2021.12.03.471024v4.full">[2]https://www.biorxiv.org/content/10.1101/2021.12.03.471024v4.full</a></p> 
<p>[3]<a href="https://baijiahao.baidu.com/s?id=1721544674645640819&wfr=spider&for=pc" _src="https://baijiahao.baidu.com/s?id=1721544674645640819&wfr=spider&for=pc">https://baijiahao.baidu.com/s?id=1721544674645640819&wfr=spider&for=pc</a> </p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247608984&idx=4&sn=8414d46a4e3d3f34f2cd545427862d05&chksm=e8d19deadfa614fcb85d82ee6cd4e5945321f541c0f90958fc0acdc1271c52bb32ac479c49ae#rd">“量子位”（ID：QbitAI）</a>，作者：金磊，36氪经授权发布。</p>  
</div>
            