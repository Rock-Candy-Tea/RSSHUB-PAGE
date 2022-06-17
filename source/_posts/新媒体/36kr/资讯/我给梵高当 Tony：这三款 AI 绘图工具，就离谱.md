
---
title: '我给梵高当 Tony：这三款 AI 绘图工具，就离谱'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220617/v2_a8e363e765c94650b4497b24f58ab17d_img_000'
author: 36kr
comments: false
date: Fri, 17 Jun 2022 12:20:01 GMT
thumbnail: 'https://img.36krcdn.com/20220617/v2_a8e363e765c94650b4497b24f58ab17d_img_000'
---

<div>   
<p>很多人说今年是“AI 绘画元年”。先是 Disco Diffusion 火出了圈，从 Text-to-Image（用文字生成图像）开发社区和创意设计行业，火到了普通人的视野中。</p> 
<p>人们热衷将两种完全不搭界的对象，比如“达芬奇”和“iPhone”字样，输入 AI 程序，然后等着画面层层渲染完成。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_a8e363e765c94650b4497b24f58ab17d_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">又比如，我就把荷包蛋揉进了云朵里丨作者用 Disco Diffusion 生成</p> 
<p>那是一种“拆盲盒”般的体验。对于没有任何美术基础和绘画能力的人来说，AI 的“融梗”图大多足够惊艳，即便效果“翻车”，也能通过调整描述词继续优化。</p> 
<p>紧接着，AI 绘画工具 Midjourney 也火了。和 Disco Diffusion 满屏英文和代码的简陋界面不同，Midjourney 直接搭载在 Discord 频道上，输入指令的过程和给人发微信没什么不同，更让人吃惊的是，它生成画作的时间一般在 60 秒左右。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_5d9321a6ede94c099743ea2d30c40044_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">神说：“要有 Wi-Fi”丨作者用 DALL·E 2 生成</p> 
<p>然后，OpenAI 的 DALL·E 2 半途杀出，和前两者擅长“概念画风”不同，DALL·E 2 更“写实”，60 秒不到可以生成 10 张图，不满意还可以擦去局部重新生成……短短几个月，“最强 AI 画师”的称号几次易主。</p> 
<p>谷歌也坐不住，五月底发论文介绍自家选手——Imagen，直接叫板 DALL·E 2，号称 Imagen 有“前所未有的写实感和深度的语言理解”，目前暂未开放。</p> 
<p>这两个月来，我和前面三位“AI 画师”频繁打交道，几乎每天都在测试描述词、调教机器人，踩了很多坑，翻了不少车。但与此同时，我收获了不少杰作。</p> 
<p><strong>这次，我将对比它们的画作生成特点、用户友好度等方面，同时整理好了它们的网址，以及一些简单的操作方法。</strong></p> 
<p>在普通用户那里，它们是具像化想象的得力工具；<strong>在专业人群那里，如果将它们和其他工具联动起来，能有无穷尽的想象空间。</strong></p> 
<h2>Disco Diffusion，生成图的艺术性最高</h2> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_751ed2d05f014315bc7624f39d1431ed_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>使用入口：https://colab.research.google.com/github/alembics/disco-diffusion/blob/main/Disco_Diffusion.ipynb</strong></p> 
<p>Disco Diffusion 生成画作的流程大概分为这几步：打开程序；设置图片尺寸、过程图张数、生成图张数等参数；用英文写好描述词（Prompts），格式大致为“画作类型 + 对象（可以有多个）+ 画风设定 + 一些起限定作用的修辞词”；然后开始运行，等待 AI 渲染画作。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_1d24d9ab1b204909b773fdca3b3ed33c_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">我给 AI 写的描述词：“A beautiful painting of a starry night, shining its light across a sunflower sea by James Gurney, Trending on artstation.”</p> 
<p>一般来说，你需要等半个小时，如果盯着屏幕看，你会看到图像从满是噪点，逐渐变得清晰、有细节起来。</p> 
<p>使用期间，Disco Diffusion 可能会提示你在电脑上空出足够的运行内存，但因为它运行在谷歌免费提供的 GPU 等计算资源上，对用户的电脑硬件要求并不高，打开浏览器运行就可以。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_328fb099fb8749ebb2ee33b794a928c7_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">用 AI 画一个莫比斯风格的场景：“a beautiful painting of a spaceship flying over a desert by Moebius, trending on artstation.”</p> 
<p>Disco Diffusion 本身是个免费的开源软件，但如果你想要更快的出图速度，可以买谷歌 Colab 会员，以分配到更快的云端计算资源。</p> 
<p>除了只输入文字让 AI 自由发挥，你还可以事先垫进一张初始化图片（Initial Image）去约束 AI 的创作。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_8cda211c376447e7807583a1150d5a15_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">比如，我先做了一张有树木轮廓和绿色色块的底图（左），然后再操作，Disco Diffusion 就会在这个大框架下去发挥，成品为右图</p> 
<p><strong>Disco Diffusion 生成图理论上可以商用，其程序基于 MIT 开源协议，所有互联网用户可以免费使用、复制、修改甚至出售生成图。</strong>但我觉得还是存有风险。风险主要来源于你的描述词会引来画风抄袭的争议。</p> 
<p>当你使用了风格鲜明的艺术家（尤其是在世的艺术家），以及某部商业作品作为关键词时，都请不要直接拿来商用。</p> 
<h2>Midjourney ，不怎么“超纲”，更“听话”</h2> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_f38548668c7d4319a38b63d80ff583c1_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>Midjourney 目前还是邀请制，内测地址：https://o9q981dirmk.typeform.com/to/zZtF1mVc?typeform-source=midjourney-gallery</strong></p> 
<p>为了测试 Midjourney 的生成效果，我复制了之前“投喂”给 Disco Diffusion 的关键词——“星空”、“向日葵”、“梵高”——粘贴进去。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_8fbc9a91754e4f168335d52f06f2d70a_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">我用 Midjourney 生成的画</p> 
<p>看到成品，我有一个直观的感受：<strong>Midjourney 的想象力没有 Disco Diffusion 那么会“超纲”。但如果从辅助创作的角度考虑，我会更倾向于用 Midjourney 这个更“听话的工具”</strong>，毕竟，没有一个创作者愿意把创作主导权让给 AI。</p> 
<p>Midjourney 的优点就是：快。软件生成图非常快，一张算下来大概 60 秒。你要是对成品不满意，还可以几乎实时地提升细节，或延伸变化。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_eb8de3a019944ab8b1190a849d75b598_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">一分钟生成 4 个小狗警察丨用 Midjourney 生成</p> 
<p>Midjourney 搭在了通讯软件 Discord 上，在对话框输入“/image”后，用英文输入描述词，然后按下回车键。这个过程就像在和 AI 聊天一下。</p> 
<p>60 秒后，你就可以在对话框里收到 4 张渲染好的图片。如果对“图 1”不满意，可以点击“U1”按钮增加细节，按“V1”按钮延伸变化，直到满意为止。</p> 
<p>于是，我拿 Midjourney 生成了“十九世纪的麦当劳”和“十八世纪的打工人”：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_83de4ad43be849369b7ddc4534625e5e_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_0891c2a0fb8745abab85ec99adf057e3_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>之所以说 Midjourney 是“产品化”了的 Disco Diffusion，一个是它的界面更友好，另一个是它还内建了一个创作社区，你可以看到玩家们用哪些描述词生成了什么样的画作。</strong>这就是一个极具参考价值的“画风”数据库，太适合拿来“抄作业”了。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_95a191c67e7b428a937c0a0dbae67e51_img_000" referrerpolicy="no-referrer"></p> 
<p>比如，我尝试生成《爱，死亡和机器人》里那集《糟糕之旅》的场景，参考了上图两位艺术家的描述词，之后就生成了满意的画作：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_5055592c60ef4364acb2e5e4891e8abc_img_000" referrerpolicy="no-referrer"></p> 
<p>“抄作业”让生成像样作品的门槛进一步降低了，但另一方面，也会失去了很多探索的乐趣。<strong>不要让游戏秘籍毁掉了一个好游戏。</strong></p> 
<p><strong>版权方面，如果你是免费用户，图像的版权归属于 AI，每月支付 30 美元后，就能将图片拿去商用了。</strong>但同时，如果你因此获利达两万美元以上，则需要给 Midjourney 20% 的分成。</p> 
<h2>DALL·E 2 ，我给梵高理发，我让大象转身</h2> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_610aa6dcea5f44609d1b1bcde08886d7_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>我当了回“托尼”，用 DALL·E 2 给梵高理发，申请地址：labs.openai.com/waitlist</strong></p> 
<p>我等了一个多月，才拿到了 DALL·E 2 的内测资格。如果说 Disco Diffusion 更擅长描绘氛围、风景或概念艺术，那么 DALL· E 2 则擅长写实。</p> 
<p>“大象能转身吗？”我以这个“经典甲方需求”为例，试试 DALL· E 2 的写实能力。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_7dac03076e3e445c8c6639695e61ef49_img_000" referrerpolicy="no-referrer"></p> 
<p>它转过来了。</p> 
<p>我让网友扮演甲方，让大象去做些别的事情。比如，让大象在海洋馆里游：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_2aa403d66006435f8e8d8c66c7985bed_img_000" referrerpolicy="no-referrer"></p> 
<p>让大象和鲨鱼共舞：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_261a48a5c39e497991566d2abd56c10e_img_000" referrerpolicy="no-referrer"></p> 
<p>让大象开哈雷摩托车在路上狂飙：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_f3d746cff5934a3996b4664084b6b0fa_img_000" referrerpolicy="no-referrer"></p> 
<p>让大象被曹冲称：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_013ee3ce043a4dfca73951c4c941b4b7_img_000" referrerpolicy="no-referrer"></p> 
<p>“甲方”们无话可说。</p> 
<p>毫不夸张地说，这是我目前用过体验最好的 AI 绘图工具，<strong>操作足够简单，完成度高，速度快到可以当搜索引擎：不到一分钟生成 10 张图片（1024 × 1024），可无限延伸变化，甚至可以擦除局部重新生成。</strong>你可以不停地给梵高“理发”。</p> 
<p>在版权方面，DALL·E 2 背后的组织 OpenAI 列了几条严格的限制：<strong>图片生成版权最终归属 OpenAI；仅供个人学习探索使用，不能商用，不能用于制作 NFT；不能在社交媒体上发布过于写实的人脸生成结果，会有肖像侵权风险。</strong></p> 
<p>OpenAI 也声称已经禁止 AI 记住名人的脸，也规避了种族和性别的刻板印象等。</p> 
<p>在苦苦等到 DALL·E 2 内测资格之前，我找了一个“平替”——DALL·E mini，是用第一代 DALL·E 做的 demo，生成速度快，但画面完成度不及 DALL·E 2。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_6230c37bb4234cbba3b6c5676f654bbb_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>榴莲沙发｜用 DALL·E mini 生成，软件地址：https://huggingface.co/spaces/dalle-mini/dalle-mini</strong></p> 
<h2>生成图像，只是第一步</h2> 
<p>“能不能让它们动起来？”我看着 AI 返回来的画作，开始想办法：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_2ba9e92cbc6145e7b754437cee4494cf_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_b648afc5124c42d8baf55c3567ece8e4_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_0c38214b590f41618c85036d1133ec47_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_f81ca489ecd64b8790778ff8756290e5_img_000" referrerpolicy="no-referrer"></p> 
<p>AI 生成图像完成，并不代表创意就结束了。如果你把它当成其中一个环节，再连接其他创意流程，想象空间是巨大的。</p> 
<p>我再展示一下插画师 Nerko 的创意：他先用 Midjourney 生成自己想要的素材，然后再将这些局部组装起来。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_0ab832d016da4775b2cf282662103fe8_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220617/v2_d862fa1dcac9429797e159bf5c4589fb_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">@NekroXIII</p> 
<p>在他手里，AI 是种“生产力”。挑选和合成，仍是他全权主导。在用上 Midjourney 之前，他已经画了 15 年插画。</p> 
<p>本文来自微信公众号<a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MTg1MjI3MzY2MQ==&mid=2651995795&idx=1&sn=6b3b4794c37b476b77dda341eb78ee5e&chksm=5dbe1a016ac993176b33a3d193b1914e34b7ea8e9e1efeca08b7ae6181f625f8aa829893bd5f#rd">“果壳”（ID：Guokr42）</a>，作者：Simon_阿文，36氪经授权发布。</p>  
</div>
            