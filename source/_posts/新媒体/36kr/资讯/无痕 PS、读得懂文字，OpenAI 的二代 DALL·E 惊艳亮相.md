
---
title: '无痕 PS、读得懂文字，OpenAI 的二代 DALL·E 惊艳亮相'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220414/v2_c38309b8ee1041f68deb4bf00d9142a0_img_000'
author: 36kr
comments: false
date: Thu, 14 Apr 2022 10:47:33 GMT
thumbnail: 'https://img.36krcdn.com/20220414/v2_c38309b8ee1041f68deb4bf00d9142a0_img_000'
---

<div>   
<p>能无痕 ps，能将文字转为图像，新一代的 DALL·E 2 有着什么样的魔力？</p> 
<p>去年 1 月，OpenAI 推出了一个名为 DALL·E 的 GPT-3 最强应用。一年后，二代的 DALL·E 2 也惊艳亮相。DALL·E 2 可以将文字转换生成更真实、更准确的图像，相比上一代产品，其分辨率提高了 4 倍，最为关键的是 DALL·E-2 还进化出了一项新技能——可以根据文字描述将图像自动 PS，而这种 PS 修改目前还很难被察觉，足够“以假乱真”。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_c38309b8ee1041f68deb4bf00d9142a0_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">原图</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_dd02d0cf69c646779ecd718d79a20027_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">PS 后</p> 
<p>比如上图中的「狗狗」就是由 DALL·E 2 后加上去的，两幅图对比下，几乎看不出什么破绽。</p> 
<p>可以说 DALL·E 2 带给业界的震撼在于这是一款有着独立创造力的跨模态生成模型。之前不管是可以一键切换为卡通风格的 CycleGAN，还是以自动修复图像的 Partialconv，其中运用的 AI 技术只能在图像或者文字的单一模式下进行生成和模仿，而时下将文字转换成图像、甚至根据文字对于图像进行修改，这种“脑补”的能力也是一次创新性突破。</p> 
<p>从 DALL·E-2 展示出的效果来看，其联想能力已经接近人类六岁的儿童，其艺术加工尤其是 PS 能力也已经达到了人类设计师的巅峰水平，按照 OpenAI 以往的调性，他们往往是三代产品最强，在未来继续扩大参数规模的情况下，DALL·E 2 还预示着DALL·E 3 将会有无限可能，这也不禁让我们想进一步了解人工智能的边界到底在哪。</p> 
<h2><strong>DALL·E 2 的前世今生</strong></h2> 
<p>DALL-E 是艺术家“Dalí”和机器人“WALL-E”的结合词。虽然在 DALL·E 2 的论文中，OpenAI 的科学家们并没有给出这个模型的具体规模与训练所需要的算力，不过考虑到第一代 DALL·E 就已经是基于 GPT-3 这种超大规模模型的项目了，那么我们有理由相信 DALL·E 2 的参数模型应该是 3000 亿起步。</p> 
<p>截至目前，OpenAI 团队也尚未在公共 API 列表中提供 DALL·E 2 的相关功能或者预览。据悉，OpenAI 的人员可能担心 DALL·E 2 的超强功能被用到一些如换脸、图像伪造等会对社会造成负面影响的方面，因此也正在设计限制 DALL·E 被用于负面图像生成的方案，预计完成之后就会对外公开了。</p> 
<p>与此同时，从另一个角度来看，这也推进了 AI 与云计算的结合，因为只有将 AI 云化才能让普通玩家用得到 DALL·E 2，否则中小型公司凭借自己的力量，很难训练出这种超大规模的模型。</p> 
<p>DALL·E 2继承了第一代产品将文本转化为图像的能力，并且提供了更高的分辨率和更低的延迟，还可以根据用户的描述对于现有的图像进行 PS，用户可以从现有的图片开始，选择一个区域，并告诉模型编辑它。例如，你可以在客厅的墙上画<a class="project-link" data-id="1678228599714821" data-name="一幅画" data-logo="https://img.36krcdn.com/20220331/v2_4a0e679338cf4245a8001171fd56c876_img_000" data-refer-type="1" href="https://36kr.com/project/1678228599714821" target="_blank">一幅画</a>，然后用另一幅画代替它，或者在咖啡桌上放一瓶花。该模型可以填充（或删除）对象，同时在 PS 过程中，DALL·E 2 还会考虑房间中阴影的方向等细节。</p> 
<p>正如上文所说第一代的 DALL-E 是基于 GPT-3 模型的，它可以将图像压缩成文字，但图像与文字的匹配往往会限制图像的真实度。DALL·E 2 则引入了 CLIP/unCLIP 的机制，CLIP 类似于编码器，它的工作原理是像人类一样，查看图像并总结图像的内容，而 unCLIP 则是 CLIP 的反向操作，是从文字描述生成图像的过程。CLIP/unCLIP 的机制在一定程度上解决了 CLIP 一个非常有趣的弱点：人们可以通过给一个物体贴上一个标签（比如 iPod)，这种方式往往会达到欺骗模型的目的。DALL·E 2 对于这种贴着标签的苹果有着比较好的识别能力，比如下列图片基本都能被 DALL·E 2 正确处理。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_d5d4037a767e4847933cfa77460e3035_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>DALL·E 2 的基本原理与背后趋势</strong></h2> 
<p>正如前文所说，DALL·E 2 是基于 CLIP/unCLIP 机制的，首先为了获得完整的图像生成模型，将 CLIP 图像嵌入解码器与一个先验模型，它从给定的文本标题生成可能的 CLIP 图像嵌入。而将完整文本条件图像生成堆栈则称为 unCLIP，因为它通过颠倒 CLIP 图像编码器生成图像。训练数据集由成对（x, y）的图像 x 和它们对应的标题 y 组成。设 zi 和 zt 分别为其 CLIP 图像和文本嵌入，其基本的架构如下：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_e177d16e63e3490483fb290ce89059fd_img_000" referrerpolicy="no-referrer"></p> 
<p>笔者认为 DALL·E 2 快速发展的背后，其实是<strong>人工智能由感知智能到认知智能的全面升级</strong>，而这其中的创造性是 AI 今后发展的最大助力，比如金融行业的呼叫中心需要分析客户的语气，以快速处理投诉类案例；出行类 APP 遇到客户说出某些关键词时，则需要立刻与 110 联动报警。这些应用场景其实都需要 AI 模型放弃原先死板僵硬的计算，而发展出某种活性。而一旦 AI 拥有创意，那么就可以和二次元特性进行结合，尤其是 90、00 后的年轻人们，在对话当中经常使用表情图、动态图等方式来表达情感，而将这些非语言信息的语义提取并翻译出来，就需要一定的创意了。</p> 
<p>而再进一步，AI 未来很可能会达到比你自己更懂你的程度。比如前段时间笔者经常熬夜加班，结果打开淘宝会发现总给我推荐防脱洗发水，当然目前已经推荐枸杞了。</p> 
<p>不过这其实也说明<strong>认知智能的终极发展就是让用户在使用过程中对于“人工智能”不断淡化，甚至无感化</strong>。现在用户使用人工智能时还会明显感受到它的存在，比如你打开电视还需要说“我要看XXX的电视剧”，还要对手机说“给XXX打电话”而真正实现认知智能之后，将会让你觉得你的这些交互行为变为多余，比如你回到家，人工智能系统会根据你的步态，推荐一个适合你当下身体状况的食谱，等你吃完饭下楼去超市的时候，你的手机会建议补充一些牛奶，因为你刚刚已经把家里最一袋牛奶喝掉了。相信读到这里读者也就会明白，化有形于无形，就是用户交互的最终奥义。</p> 
<p>虽然短期来看，创造性 AI 还略显遥不可及，但是 DALL·E 2 的出现，让我们看到了希望，让我们做好准备迎接新一代认知 AI 产品的到来。</p> 
<p>本文来自微信公众号<a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MjM5MjAwODM4MA==&mid=2650915725&idx=2&sn=0dd806babf14e3d0f096127f4648cb37&chksm=bd59b25e8a2e3b48cc7c24af78930deb045cf86af0929b1904f3a7f78f2ccc533c9fa4b3d064#rd">“CSDN”（ID：CSDNnews）</a>，作者：马超，36氪经授权发布。</p>  
</div>
            