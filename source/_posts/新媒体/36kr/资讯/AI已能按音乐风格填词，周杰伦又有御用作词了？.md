
---
title: 'AI已能按音乐风格填词，周杰伦又有御用作词了？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210630/v2_5becf8cdee88409cb676fd63d0e5e41b_img_000'
author: 36kr
comments: false
date: Wed, 30 Jun 2021 10:37:46 GMT
thumbnail: 'https://img.36krcdn.com/20210630/v2_5becf8cdee88409cb676fd63d0e5e41b_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/9iHUpgwpoWEqBhf4qCXfpA">“量子位”（ID:QbitAI）</a>，作者：关注前沿科技，36氪经授权发布。</p> 
<p>虽然AI在艺术领域一直有不少争议，但它一直也没停下各种尝试的步伐：</p> 
<p>写歌、画画、写诗……这不，刚又学会了填词。</p> 
<p>我们给这个AI放了一首钢琴曲，曲调非常悠扬平和。</p> 
<p>然后，它生成的部分词是这样的：</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_5becf8cdee88409cb676fd63d0e5e41b_img_000" data-img-size-val="628,730" referrerpolicy="no-referrer"></p> 
<p>各位感觉如何？</p> 
<p>其中，生成过程的动态效果看着还不错：</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_71df28316eea495186b585ec152493d3_img_000" data-img-size-val="600,238" referrerpolicy="no-referrer"></p> 
<p>当然，它可以很好地分辨不同风格的音乐：给安静的钢琴乐生成的词与给嘈杂的摇滚乐生成的会完全不一样。</p> 
<p>不过，鉴于目前的填词效果（比如有时无厘头的上下衔接），研究人员也表示：</p> 
<p>这个工具也不是为了取代音<a class="project-link" data-id="84161" data-name="乐家" data-logo="https://img.36krcdn.com/20200729/v2_5f9e7b389cff40159e04bb495c9b6fea_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/84161" target="_blank">乐家</a>，而是成为一个激发音乐家创作灵感的工具，辅助他们创造出满意的作品。</p> 
<p>ps.此处在线cue周杰伦，御用词人试试AI？</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_29c222a2f455436e9a8a759dd6aa523a_img_000" data-img-size-val="306,266" referrerpolicy="no-referrer"></p> 
<h2>如何分辨出不同风格的曲子？</h2> 
<p>这项研究来自滑铁卢大学，研究成果即将发表在ICCC 2021。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_c1f13e2317084279b7cbc18d8aba30e5_img_000" data-img-size-val="996,228" referrerpolicy="no-referrer"></p> 
<p>项目的动机源于其中一位研究员的个人兴趣。</p> 
<p>这名研究员非常喜欢音乐，所以她很好奇机器是否可以生成听起来像她最喜欢的音<a class="project-link" data-id="103261" data-name="乐艺" data-logo="https://img.36krcdn.com/20200729/v2_37708443707342648174f333d2f36ac4_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/103261" target="_blank">乐艺</a>术家风格的歌词。</p> 
<p>最终做出来的系统叫做LyricJam，已有在线网页版供任何感兴趣的音乐人访问使用。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_f02b899bc17d45839337a9b959ad07b3_img_000" data-img-size-val="1000,478" referrerpolicy="no-referrer"></p> 
<p>该系统通过将原始音频文件转换为频谱图，然后使用深度学习模型实时生成与音乐相匹配的歌词。</p> 
<p>模型的架构由两个变分自动编码器（VAE）组成，一个用于学习音乐音频的表示，另一个用于学习生成歌词。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_3c8a9ebd126c42b1b1c59757702a015b_img_000" data-img-size-val="800,530" referrerpolicy="no-referrer"></p> 
<p>训练数据集由18000个原始歌曲的WAV音频片段和7种音乐艺术家的相应歌词组成。</p> 
<p>首先使用CNN来根据频谱图将带歌词的音频，按风格分类成不同“艺术家”。</p> 
<p>然后训练一个条件VAE(conditional VAE，CVAE)“重建”原始歌词，根据不同类型音乐的歌词用词和表达方式的不同，生成一系列连贯的新歌词。</p> 
<p>其中生成条件是前面预先训练的“艺术家”种类。</p> 
<p>推理阶段，流程差不多：系统将实时录制的音频片段转换成频谱图，然后进行风格识别，为了生成最匹配的歌词，需要根据“艺术家”的类别从潜在空间中采样并对其进行解码，然后生成对应的歌词表达。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_dcef1dd9a8144600877bbb56a8e339e8_img_000" data-img-size-val="1000,600" referrerpolicy="no-referrer"></p> 
<p>最后，使用基于GAN的对齐模型来对齐两种编码器生成的歌词和音频表示。</p> 
<p>最终效果如何呢？</p> 
<h2>“非批判性的即兴演奏伙伴”</h2> 
<p>为了评估他们开发的系统，研究人员进行了一项简单的用户研究，请来一批搞音乐创作的人来测试。</p> 
<p>测试要求音乐人现场演奏音乐并分享他们对系统所作歌词的反馈。</p> 
<p>首先确定该系统是否能更准确地生成与音乐所产生的情绪相匹配的歌词。</p> 
<p>研究人员选用了5种不同乐器演奏的不同歌曲的片段，每段约10秒，用该模型的两种变体（下图中每组的第二三行）各生成一行歌词，再用一个基线模型（下图中每组第一行）生成歌词。</p> 
<p>生成示例如下：</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_cc154b6035b149299bdf03e77e6db005_img_000" data-img-size-val="668,790" referrerpolicy="no-referrer"></p> 
<p>测试者需对以上3种词，进行打分，选出最匹配当前音乐的一种。</p> 
<p>总共有15个人参与了这项研究，从下表可以看出，无论播放的歌曲类型如何，用户都更喜欢后两个模型的歌词，而非基线模型的。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_5874d49c1b0a44daababd2385dab1e27_img_000" data-img-size-val="1080,266" referrerpolicy="no-referrer"></p> 
<p>这说明，该系统可以生成匹配音乐风格的歌词。</p> 
<p>最后，通过一系列问卷调查显示，大多数参与实验的音乐人都觉得，LyricJam是一个非批判性的即兴演奏“伙伴”，可以鼓励他们即兴创作并尝试不同寻常的歌词表达方式。</p> 
<p>另外，即使中间改变音乐风格或尝试加入新的和弦，歌词也能实时做出抒情主题的变化。</p> 
<p>最后研究人员表示，如果在更大的数据集上训练，填的词就更具有多样性了。</p> 
<p>感兴趣的朋友可戳在线链接试玩，系统操作非常简单，录入一个音频就可以：https://lyricjam.ai/</p> 
<p>论文地址：https://arxiv.org/abs/2106.01960</p> 
<p>参考链接：</p> 
<p>https://techxplore.com/news/2021-06-lyricjam-lyrics-instrumental-music.html</p>  
</div>
            