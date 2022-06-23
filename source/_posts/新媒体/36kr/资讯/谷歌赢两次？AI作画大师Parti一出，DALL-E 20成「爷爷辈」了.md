
---
title: '谷歌赢两次？AI作画大师Parti一出，DALL-E 2.0成「爷爷辈」了'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220623/v2_61b53378c90a497b8165eea1dd1d0d93_img_000'
author: 36kr
comments: false
date: Thu, 23 Jun 2022 05:18:40 GMT
thumbnail: 'https://img.36krcdn.com/20220623/v2_61b53378c90a497b8165eea1dd1d0d93_img_000'
---

<div>   
<p>最近，在「AI画画」这一块，大厂们又卷上了新高度！</p> 
<p>4月，在GPT-3大模型的加持下，Open AI对画图界的扛把子DALL-E进行了2.0版的全面升级。</p> 
<p>让自然语言生成图像达到了全新的高度。比如下面这幅「孙子玩儿电脑」（非骂街）。</p> 
<p class="image-wrapper"><img data-img-size-val="1024,1024" src="https://img.36krcdn.com/20220623/v2_61b53378c90a497b8165eea1dd1d0d93_img_000" referrerpolicy="no-referrer"></p> 
<p>5月，谷歌不甘落后推出AI创作神器Imagen，效果奇佳。</p> 
<p>号称重夺AI画画老大哥地位的Imagen，迅速被国外网友玩出了新高度，一波「虎戴VR」热度直接起飞。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1080" src="https://img.36krcdn.com/20220623/v2_751d9865ea824f2e8145efee4b422a4b_img_000" referrerpolicy="no-referrer"></p> 
<p>有人惊呼，现在的新模型的保质期只有一个月了么？</p> 
<p>谷歌一看，这是要开卷的节奏，不如我再进一步，再搞个新的AI大画家吧。</p> 
<p>于是，只过了一个月，新一代AI绘画大师Parti就来了！</p> 
<p class="image-wrapper"><img data-img-size-val="1080,465" src="https://img.36krcdn.com/20220623/v2_c2a5b401a5d24c65a4e416b871167a51_img_000" referrerpolicy="no-referrer"></p> 
<p>Parti，全名叫「Pathways Autoregressive Text-to-Image」，是谷歌大脑老大Jeff Dean提出的多任务AI大模型蓝图Pathway的一部分。</p> 
<p>Jeff Dean在社交媒体上第一时间推广了一波。</p> 
<p class="image-wrapper"><img data-img-size-val="1019,802" src="https://img.36krcdn.com/20220623/v2_5a8ea6d4c3b3496885b4031d0983a106_img_000" referrerpolicy="no-referrer"></p> 
<p>同时他也表示，和一个月之前的「老前辈」Imagen相比，这次的Parti使用的是不同的技术路线。</p> 
<p>为此，谷歌AI专门写了一篇博客文章，对比了两个「AI大画家」在技术层面上的区别。</p> 
<p>虽然Imagen和Parti使用类似技术，不过但具体的策略是不同的——自回归和扩散。这样互补的方式使得两个强大模型的有了更加令人期待的组合！</p> 
<h2> </h2> 
<h2>从Imagen到Parti，谷歌又整了啥新活？</h2> 
<p>先来回顾一下「老前辈」Imagen，它是一个Diffusion模型，学习将随机点的图案转换为图像。</p> 
<p>这些图像首先以低分辨率开始，然后通过超分辨率技术，不断的丰富图像的信息，进而达到提高图像分辨率的目的。</p> 
<p class="image-wrapper"><img data-img-size-val="655,601" src="https://img.36krcdn.com/20220623/v2_aa71e5f4b3f54f63ad4619c54e7393ec_img_000" referrerpolicy="no-referrer"></p> 
<p>具体点讲，就是：</p> 
<p>在用户输入文本后，如「一只戴着蓝色格子贝雷帽、穿着红色波点高领毛衣的金毛犬」，Imagen先使用一个冻结（frozen）T5-XXL 编码器将输入文本映射到嵌入序列和64×64图像扩散模型，再将生成的64×64图像上采样为256 × 256图像，最后上采样为1024 × 1024图像。</p> 
<p>而这次新推出Parti是一个自回归模型，它的方法首先将一组图像转换为一系列代码条目，类似于拼图。然后将给定的文本提示转换为这些代码条目并「拼成」一个新图像。</p> 
<p>换言之，Parti将「文本到图像的生成」转换成一个「序列到序列」的建模问题，类似于机器翻译——这使得它能够受益于大型语言模型（如PaLM），这对于处理长而复杂的文本提示和生成高质量的图像至关重要。</p> 
<p>在这种情况下，目标输出是图像token的序列，而不是另一种语言的文本token。</p> 
<p>Parti通过使用功能强大的图像标记器「ViT-VQGAN」将图像编码为离散token序列，并利用其重建图像token序列的能力，使其成为高质量、视觉多样化的图像。</p> 
<p class="image-wrapper"><img data-img-size-val="1065,624" src="https://img.36krcdn.com/20220623/v2_a683298703084b138c4832a0dd26e048_img_000" referrerpolicy="no-referrer"></p> 
<h2> </h2> 
<h2> </h2> 
<h2>参数从3.5亿到200亿：有啥区别？</h2> 
<p>Parti的模型规模支持扩展，最高可扩展至200亿参数。</p> 
<p>参数越多，模型规模越大，生成图像的细节越丰富，错误信息也明显降低。</p> 
<p>比如面对同样的文本输入：</p> 
<p>身穿橙色连帽衫和蓝色太阳镜的袋鼠站在悉尼歌剧院前的草地上，胸前举着写着「欢迎朋友」的标语</p> 
<p class="image-wrapper"><img data-img-size-val="1080,321" src="https://img.36krcdn.com/20220623/v2_3c77dc54c759437b875f8b715be4f4af_img_000" referrerpolicy="no-referrer"></p> 
<p>在3.5亿参数下，袋鼠的眼镜不是蓝色，而且PS痕迹明显，背景只体现出「草地」，悉尼歌剧院基本看不出来。举的牌子上更不知道是哪国文字。</p> 
<p>到了7.5亿参数下，眼镜颜色和背景都和文字准确对上了，但却多了另一只带着蓝眼镜的袋鼠。</p> 
<p>扩展到30亿参数，之前的袋鼠不见了，但举的牌子多了一块，上面的字仍有拼写错误，但大概能看出是「欢迎朋友」了。但背景中的悉尼歌剧院似乎开了「影分身」。</p> 
<p>最终在200亿参数下，文字中的内容得到准确再现。</p> 
<p>换一张图，也是如此。文本信息细节越少，体现的越明显。</p> 
<p>比如文本是「小提琴的背面」这几个字：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,292" src="https://img.36krcdn.com/20220623/v2_6261a2fb16824a368cbdd9cb9d73b320_img_000" referrerpolicy="no-referrer"></p> 
<p>直到30亿参数下，生成的图像仍然是「小提琴的正面」，直到200亿参数下，才生成了正确的图像。</p> 
<p>多面手「艺术家」，风格百搭</p> 
<p>除了由模型参数量扩大带来的细节提升外，画画最要紧的是能画出不同风格，要都是千篇一律，那还叫艺术家吗？</p> 
<p>Parti表示，这挺简单的。</p> 
<p>比如命题作画：</p> 
<p>一只浣熊穿正装，头戴礼帽，拄着拐杖，拿着个垃圾袋。</p> 
<p>就能画出梵高风格的：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1084" src="https://img.36krcdn.com/20220623/v2_f806fbd0b2dd43d99085d13e67938051_img_000" referrerpolicy="no-referrer"></p> 
<p>埃及法老风格的：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1081" src="https://img.36krcdn.com/20220623/v2_96a013ca6d2c409abfbf887f65c547f4_img_000" referrerpolicy="no-referrer"></p> 
<p>甚至是像素艺术风的：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1089" src="https://img.36krcdn.com/20220623/v2_57ce05db660c49cdaae098f4cded3c90_img_000" referrerpolicy="no-referrer"></p> 
<p>再比如下面的文字：</p> 
<p>「一只老虎戴着列车长的帽子，手里拿着一块滑板，上面有一个阴阳符号。」</p> 
<p>也可以画成油画风，真真的那种 。</p> 
<p class="image-wrapper"><img data-img-size-val="1024,1024" src="https://img.36krcdn.com/20220623/v2_de3f975c470244c29f073deca817ddbf_img_000" referrerpolicy="no-referrer"></p> 
<p>或者版画风，酷酷的那种。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1079" src="https://img.36krcdn.com/20220623/v2_3172f062e64f49bda4f010faa4fb64e7_img_000" referrerpolicy="no-referrer"></p> 
<p>甚至国画风，萌萌的那种。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1078" src="https://img.36krcdn.com/20220623/v2_8498576d9cbc4c6d91e009bb442bd6bd_img_000" referrerpolicy="no-referrer"></p> 
<p>当然，也有翻车的时候。</p> 
<p>比如下面这个作品，文字是「一个没有香蕉的盘子,旁边有一个没有橙汁的玻璃杯。」</p> 
<p class="image-wrapper"><img data-img-size-val="1024,1024" src="https://img.36krcdn.com/20220623/v2_36a2ea0ee00c499b9a8bf041962145be_img_000" referrerpolicy="no-referrer"></p> 
<p>然而，生成的图片中盘子里全是香蕉，玻璃杯里也几乎盛满了橙汁！</p> 
<p>就当是艺术家偶尔打了个盹吧！</p> 
<p>看起来，以后「斗图界」说不定可以告别表情包了，想要什么图，打字就行了！</p> 
<p>早些年要是能有这样的神器，「美术课恐惧症」的小编可能也会免去不少不堪回首的回忆吧。</p> 
<p>参考资料：</p> 
<p>https://parti.research.google/</p> 
<p>https://blog.google/technology/research/how-ai-creates-photorealistic-images-from-text/</p> 
<p>本文来自微信公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/YfCqssecNBIJ4kzjc0vPcw">“新智元”（ID:AI_era）</a>，编辑：David 如願 好困，36氪经授权发布。</p>  
</div>
            