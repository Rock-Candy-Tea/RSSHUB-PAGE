
---
title: 'AI越进化越跟人类大脑像，Meta找到了机器的_前额叶皮层_，AI学者和神经科学家都惊了'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220620/v2_63bef79e99f84f9f844577311986a549_img_000'
author: 36kr
comments: false
date: Mon, 20 Jun 2022 07:00:38 GMT
thumbnail: 'https://img.36krcdn.com/20220620/v2_63bef79e99f84f9f844577311986a549_img_000'
---

<div>   
<p>说出来你可能不信，有一只AI刚刚被证明，处理语音的方式跟<strong>大脑</strong>谜之相似。</p> 
<p>甚至在<strong>结构</strong>上都能相互对应——</p> 
<p>科学家们在AI身上直接定位出了“视觉皮层”。</p> 
<p class="image-wrapper"><img data-img-size-val="480,287" src="https://img.36krcdn.com/20220620/v2_63bef79e99f84f9f844577311986a549_img_000" referrerpolicy="no-referrer"></p> 
<p>这项来自<strong>Meta AI</strong>等机构的研究一经po出，立马在社交媒体上炸开了锅。一大波神经科学家和AI研究者前往围观。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,529" src="https://img.36krcdn.com/20220620/v2_100436e4a4a340b98b9a7f503568bf41_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>LeCun</strong>称赞这是“出色的工作”：自监督Transformer分层活动与人类听觉皮层活动之间，确实密切相关。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,678" src="https://img.36krcdn.com/20220620/v2_995fdecbee5a4298bba52dceedbd151d_img_000" referrerpolicy="no-referrer"></p> 
<p>还有网友趁机调侃：Sorry马库斯，但AGI真的快要来了。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,444" src="https://img.36krcdn.com/20220620/v2_938bcbed7df8435ca9765e55fbfc9247_img_000" referrerpolicy="no-referrer"></p> 
<p>不过，研究也引发了一些学者的好奇。</p> 
<p>例如麦吉尔大学神经科学博士Patrick Mineault提出疑问：</p> 
<blockquote> 
 <p>我们发表在NeurIPS的一篇论文中，也尝试过将fMRI数据和模型联系起来，但当时并不觉得这俩有啥关系。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,289" src="https://img.36krcdn.com/20220620/v2_e6770b1d93794a13b7b81dade54689ff_img_000" referrerpolicy="no-referrer"></p> 
<p>所以，这到底是一项怎样的研究，它又是如何得出“这只AI干起活来像大脑”的结论的？</p> 
<h2><strong>AI学会像人脑一样工作</strong></h2> 
<p>简单来说，在这项研究中，研究人员聚焦语音处理问题，将自监督模型<strong>Wav2Vec 2.0</strong>同<strong>412名</strong>志愿者的大脑活动进行了比较。</p> 
<p>这412名志愿者中，有351人说英语，28人说法语，33人说中文。研究人员给他们听了大约1个小时的有声书，并在此过程中用fMRI对他们的大脑活动进行了记录。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,675" src="https://img.36krcdn.com/20220620/v2_c333b95658ce48f18ff5b1f8877cad20_img_000" referrerpolicy="no-referrer"></p> 
<p>模型这边，研究人员则用超过600小时的无标签语音来训练Wav2Vec 2.0。</p> 
<p>对应志愿者的母语，模型也分为英语、法语、中文三款，另外还有一款是用非语音声学场景数据集训练的。</p> 
<p>而后这些模型也听了听志愿者同款有声书。研究人员从中提取出了模型的激活。</p> 
<p>相关性的评价标准，遵照这个公式：</p> 
<p class="image-wrapper"><img data-img-size-val="976,90" src="https://img.36krcdn.com/20220620/v2_89ecec79b72d42de8144ee4f33e76fa4_img_000" referrerpolicy="no-referrer"></p> 
<p>其中，X为模型激活，Y为人类大脑活动，W为标准编码模型。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,358" src="https://img.36krcdn.com/20220620/v2_d5bea2dfd3f9443eb62bef6efb7d27c9_img_000" referrerpolicy="no-referrer"></p> 
<p>从结果来看，<strong>自监督学习确实让Wav2Vec 2.0产生了类似大脑的语音表征</strong>。</p> 
<p>从上图中可以看到，在初级和次级听觉皮层，AI明显预测到了几乎所有皮层区域的大脑活动。</p> 
<p>研究人员还进一步发现了AI的“听觉皮层”、“前额叶皮层”到底长在哪一层。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,777" src="https://img.36krcdn.com/20220620/v2_31bbd392211543718dffddabf9837492_img_000" referrerpolicy="no-referrer"></p> 
<p>图中显示，听觉皮层与Transformer的第一层（蓝色）最吻合，而前额叶皮层则与Transformer的最深一层（红色）最吻合。</p> 
<p>此外，研究人员量化分析了人类感知母语和非母语音素的能力差异，并与Wav2Vec 2.0模型进行对比。</p> 
<p>他们发现，AI也像人类一样，对“<strong>母语</strong>”有更强的辨别能力，比如，法语模型就比英语模型更容易感知来自法语的刺激。</p> 
<p>上述结果证明了，<strong>600小时</strong>的自监督学习，就足以让Wav2Vec 2.0学习到语言的特定表征——这与婴儿在学说话的过程中接触到的“数据量”相当。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,577" src="https://img.36krcdn.com/20220620/v2_f547aa694bb0452abe58a2977113a9f5_img_000" referrerpolicy="no-referrer"></p> 
<p>要知道，之前DeepSpeech2论文认为，至少需要<strong>10000小时</strong>的语音数据（还得是标记的那种），才能构建一套不错的语音转文字（STT）系统。</p> 
<p class="image-wrapper"><img data-img-size-val="372,328" src="https://img.36krcdn.com/20220620/v2_fc2d86779fce42b78dc8980df67ee700_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>再次引发神经科学和AI界讨论</strong></h2> 
<p>对于这项研究，有学者认为，它确实做出了一些新突破。</p> 
<p>例如，来自谷歌大脑的Jesse Engel称，这项研究将可视化滤波器提升到了一个新的层次。</p> 
<p>现在，不仅能看到它们在“像素空间”里长啥样，连它们在“类脑空间”中的模样也能模拟出来了：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,247" src="https://img.36krcdn.com/20220620/v2_1c0c0f31eaa94b5a875a3183f33c380e_img_000" referrerpolicy="no-referrer"></p> 
<p>又例如，前MILA和谷歌研究员Joseph Viviano认为，这个研究还证明了fMRI中的静息态（resting-state）成像数据是有意义的。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,960" src="https://img.36krcdn.com/20220620/v2_43632aafe71143be8120e0ea2814c3b5_img_000" referrerpolicy="no-referrer"></p> 
<p>但在一片讨论中，也出现了一些质疑的声音。</p> 
<p>例如，神经科学博士Patrick Mineault除了指出自己做过相似研究但没得出结论外，也给出了自己的一些质疑。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,625" src="https://img.36krcdn.com/20220620/v2_dc08e3c97e554a659c44fa0b027c561f_img_000" referrerpolicy="no-referrer"></p> 
<p>他认为，这篇研究并没有真正证明它测量的是“语音处理”的过程。</p> 
<p>相比于人说话的速度，fMRI测量信号的速度其实非常慢，因此贸然得出“Wav2vec 2.0学习到了大脑的行为”的结论是不科学的。</p> 
<p>当然，Patrick Mineault表示自己并非否认研究的观点，他自己也是“作者的粉丝之一”，但这项研究应该给出一些更有说服力的数据。</p> 
<p>此外也有网友认为，Wav2vec和人类大脑的输入也不尽相同，一个是经过处理后的波形，但另一个则是原始波形。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,261" src="https://img.36krcdn.com/20220620/v2_0432c05c5d6b466a9df92f21f58da64f_img_000" referrerpolicy="no-referrer"></p> 
<p>对此，作者之一、Meta AI研究员Jean-Rémi King总结：</p> 
<blockquote> 
 <p>模拟人类水平的智能，确实还有很长的路要走。但至少现在来看，我们或许走在了一条正确的道路上。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,306" src="https://img.36krcdn.com/20220620/v2_8bebdce6183942cab83a8ef02fc27768_img_000" referrerpolicy="no-referrer"></p> 
<p>你认为呢？</p> 
<p>论文地址：https://arxiv.org/abs/2206.01685</p> 
<p>参考链接：[1]https://twitter.com/patrickmineault/status/1533888345683767297[2]https://twitter.com/Jean<a class="project-link" data-id="1678221047624706" data-name="Remi" data-logo="https://img.36krcdn.com/20220331/v2_0f16e9ff3aed41228c9d9da43c9e8b33_img_000" data-refer-type="1" href="https://36kr.com/project/1678221047624706" target="_blank">Remi</a>King/status/1533720262344073218[3]https://www.reddit.com/r/singularity/comments/v6bqx8/toward_a_realistic_model_of_speech_processing_in/[4]https://twitter.com/ylecun/status/1533792866232934400</p> 
<p class="editor-note">本文来自微信公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/YMRhoohkuO8vt4Qh2heF5g">“量子位”（ID:QbitAI）</a>，作者：鱼羊 萧箫，36氪经授权发布。</p>  
</div>
            