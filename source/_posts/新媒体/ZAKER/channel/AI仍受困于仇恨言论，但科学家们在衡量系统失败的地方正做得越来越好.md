
---
title: 'AI仍受困于仇恨言论，但科学家们在衡量系统失败的地方正做得越来越好'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202107/60dd42cc8e9f095ae47bdcdf_1024.jpg'
author: ZAKER
comments: false
date: Thu, 01 Jul 2021 03:14:44 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202107/60dd42cc8e9f095ae47bdcdf_1024.jpg'
---

<div>   
<p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202107/60dd42cc8e9f095ae47bdcdf_1024.jpg" data-height="850" data-width="1280" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202107/60dd42cc8e9f095ae47bdcdf_1024.jpg" referrerpolicy="no-referrer"></div></div><strong>作者：Karen Hao</strong><p></p><p><strong>翻译：朱启轩</strong></p><p><strong>校对：詹好</strong></p><p>尽管自然语言处理最近取得了诸多进展，但它仍在最基本的应用上受阻。在一项新的研究中，科学家们测试了四种最佳的检测仇恨言论的人工智能系统，他们发现这些系统或多或少在区分带有仇恨情绪和没有仇恨情绪的句子时存在一些问题。</p><p>然而这个结果并不令人惊讶——因为创造能够理解语言细微差别的人工智能是很困难的。这使得研究人员诊断和分析这些问题的方法显得尤为重要。他们针对仇恨言论开发了 29 个不同的测试方法，以便更准确地找出每个系统的疏漏，从而让人们更容易去克服这一问题。实际上，上述的这个测试已经在帮助一家商业公司改善其人工智能系统。</p><p>The study authors 是由牛津大学 ( University of Oxford ) 和艾伦 · 图灵研究所 ( Alan Turing Institute ) 的科学家们所领导的团队。该团队采访了来自 16 家研究网络仇恨的非营利机构的员工，以求了解 AI 检测仇恨言论的进一步信息。</p><p>该团队利用这些采访结果把仇恨言论分成了 18 大类，他们致力于关注基于英文文本的仇恨言论，包括贬损言论，侮辱性语言和威胁性语言。他们还识别了 11 种通常会让 AI 陷入困境的非仇恨场景，包括在无害声明中使用脏话，被目标社区收回的诋毁，以及引用或引用原始仇恨言论 ( 即反言论 ) 的仇恨谴责。</p><p>对于 29 个不同的仇恨类别 , 他们创造了大量的例子并且使用 " 模板 " 句式，比如 " 我讨厌 ( 身份 ) " 或 " 你只是在（诽谤）我 "，从而为 7 个受保护的群体生成相同的例子集合。根据美国法律，这些 " 受保护群体 " 受到法律保护，不应当遭到歧视。他们还有一个开源的数据集叫 HateCheck，其中总共包含了近 4000 个案例。</p><p>研究人员随后检查了两个流行的商业公司的服务条款 : 谷歌 Jigsaw 的 Perspective API 和 Two Hat 的 SiftNinja。两者都允许客户在帖子或评论中举报违规内容。Perspective API，它被 Reddit 等平台以及《纽约时报》和《华尔街日报》等新闻机构所使用。它基于有害性的衡量对帖子和评论进行标记和排序，以供人们审查。</p><p>而 SiftNinja 对仇恨言论则过于宽容，没有能检测到所有的变化。相反，Perspective 则过于严格。它擅长于检测 18 个仇恨类别，但也同时标记了大多数非仇恨类别，比如被撤回的侮辱性言语和反击言论。研究人员在测试谷歌的两种学术模型时发现了同样的特征，这两种模型代表了现有的一些最好的自然语言处理技术，且有望成为其他商业内容审核系统的基础。学术模型也显示出在受保护群体上不均衡的表现——对某些群体的仇恨进行错误分类的频率高于其他群体。</p><p>这些结果指明了当前基于 AI 的仇恨言语检测系统中最具挑战性的一个方面：若不注重消除仇恨言论，就无法解决该问题 ; 若过于注重消除仇恨言论就会误伤。牛津互联网研究所的博士生 Paul Rottge 指出：" 突然间你会首先惩罚那些被仇恨锁定的群体。"</p><p>Jigsaw 的首席软件工程师露西 · 瓦瑟曼提出，一个更好的被叫做 Perspective 的模型，可以通过依靠人类调解员做出最终决定，来克服了这些限制。但是这个过程不适用于更大的平台和更多的数据。Jigsaw 现在正致力于开发一项功能，可以根据 Perspective 的不确定性重新调整帖子和评论的优先级——自动删除那些它认为令人讨厌的内容，并向人们标记出可疑内容。</p><p>Jigsaw 指出，这项新研究令人兴奋的地方在于，它是否提供了一种精细的方法来评估技术水平。Jigsaw 现在正在使用 HateCheck 来更好地理解其模型之间的差异以及它们需要改进的地方。</p><p>其他学者也对这项研究感到兴奋。华盛顿大学的语言人工智能研究员马尔滕 • 萨普表示 :" 这篇论文为我们评估行业系统提供了一个很好的资源，它允许企业和用户提出改进的需求。"</p><p>罗格斯大学的社会学助理教授 Thomas Davidson 对此表示赞同。他说，语言模型的局限性和语言的混乱意味着，仇恨言论的识别总是会在识别力欠缺和识别过度之间进行权衡。他补充说："HateCheck 数据集有助于让这些权衡变得可见。"</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            