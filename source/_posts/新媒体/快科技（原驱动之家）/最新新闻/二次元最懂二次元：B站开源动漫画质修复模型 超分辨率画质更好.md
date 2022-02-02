
---
title: '二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220202/S7c7c6cff-4f9b-4e5f-9221-334dd1cbad46.png'
author: 快科技（原驱动之家）
comments: false
date: Wed, 02 Feb 2022 19:30:03 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220202/S7c7c6cff-4f9b-4e5f-9221-334dd1cbad46.png'
---

<div>   
<p>为了让你能高清重温童年的XXX，AI近来没少努力。</p>
<p>最近我们就发现了一个专为动漫图像而生的画质修复模型：</p>
<p>Real-CUGAN。</p>
<p>这个开源模型在今天登上了GitHub热榜，还来自b站官方。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/7c7c6cff-4f9b-4e5f-9221-334dd1cbad46.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="160" src="https://img1.mydrivers.com/img/20220202/S7c7c6cff-4f9b-4e5f-9221-334dd1cbad46.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/cee310c5-b329-484a-bd17-1956ced18d4e.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="179" src="https://img1.mydrivers.com/img/20220202/Scee310c5-b329-484a-bd17-1956ced18d4e.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>它的效果也比此前俩个挺火的超分模型要更进一步，推理速度、兼容性什么的也都更快、更好。</strong></p>
<p>“老二刺猿”了就是说[狗头]。</p>
<p style="text-align: center"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="587" src="https://img1.mydrivers.com/img/20220202/10c0b8bc-61ce-480d-bb5e-ca1d696fb832.png" style="border: black 1px solid" w="587" referrerpolicy="no-referrer"></p>
<p>结构魔改自Waiuf2x</p>
<p>Real-CUGAN，全名Real Cascade U-Nets for Anime Image Super Resolution。</p>
<p>其结构魔改自此前大火的图片无损放大/降噪神器——Waiuf2x （GitHub标星23k），并可以与之无缝兼容；训练代码基本来自腾讯去年刚出品的RealESRGAN （GitHub标星9.1k）。</p>
<p><span style="color:#ff0000;"><strong>Waiuf2x出自日本的一位“技术宅”，原理大概就是把一堆二次元图片缩小再和原图放一起，通过算法让模型自己学会了如何放大拉伸图片。</strong></span></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/de03787f-c78f-490b-ae31-eb128f766e28.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="802" src="https://img1.mydrivers.com/img/20220202/Sde03787f-c78f-490b-ae31-eb128f766e28.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>Waiuf2x有免费的网页版供大家使用。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/e2cd0011-ae09-4f0f-a755-bbb1e11854a7.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="348" src="https://img1.mydrivers.com/img/20220202/Se2cd0011-ae09-4f0f-a755-bbb1e11854a7.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>RealESRGAN，主要通过模拟高分辨率图像变低分辩率过程中的各种“退化”过程，然后让模型看到一张糊图后倒推出来它的高清图。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/a1f2eda8-a6ec-4612-82b0-078f715018f3.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="542" src="https://img1.mydrivers.com/img/20220202/Sa1f2eda8-a6ec-4612-82b0-078f715018f3.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>它是对超分“前辈”ESRGAN的进一步改进，后者曾赢得ECCV2018 PIRM-SR挑战赛中的第一名。</p>
<p>相比这两位，Real-CUGAN都有什么独到之处呢？</p>
<p>首先在训练集方面，前两者都是采用私有二次元训练集，量级与质量未知，Real-CUGAN则用了百万级高清的二次元数据集。</p>
<p>在推理耗时方面（目标为1080P），如果以Waiuf2x为基线，RealESRGAN要耗费2.2x的时间，Real-CUGAN则只需1x。</p>
<p>在强度调整方面，Waiuf2x可以支持多种降噪强度，RealESRGAN没法调整，Real-CUGAN则支持4种降噪强度与保守修复，未来还会提供不同程序的去模糊、去JPEG伪影、锐化等功能。</p>
<p>此外，Waiuf2x只能实现1倍和2倍分辨率修复，RealESRGAN只支持4倍，Real-CUGAN则2～4倍都可以（1倍还在训练中）。</p>
<p>当然，最最最重要的还是效果。</p>
<p>来看一些最直观的对比图：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/4374b43a-b516-4226-9550-65342c881ea4.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="183" src="https://img1.mydrivers.com/img/20220202/S4374b43a-b516-4226-9550-65342c881ea4.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/19482992-2029-4a92-a998-04344d68f994.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="184" src="https://img1.mydrivers.com/img/20220202/S19482992-2029-4a92-a998-04344d68f994.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>可以看到，Real-CUGAN和Waiuf2x的结果都差不多，但是RealESRGAN却没有处理好地板纹理。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/0086e514-2cd4-405f-8c81-83ff0ff5642d.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="221" src="https://img1.mydrivers.com/img/20220202/S0086e514-2cd4-405f-8c81-83ff0ff5642d.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/d8db1f39-f59a-417f-9f5c-3760d6fdb174.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="224" src="https://img1.mydrivers.com/img/20220202/Sd8db1f39-f59a-417f-9f5c-3760d6fdb174.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>在这组对比图中，Waiuf2x明显不如后两者线条清晰，而相比Real-CUGAN，RealESRGAN中人物嘴巴和下颚处的线条是虚的，有杂线。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/3eb80784-8105-40b6-99c5-1dad8cdd6971.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="296" src="https://img1.mydrivers.com/img/20220202/S3eb80784-8105-40b6-99c5-1dad8cdd6971.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/05147b3b-6074-4042-9b7a-c7265317f3c8.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="296" src="https://img1.mydrivers.com/img/20220202/S05147b3b-6074-4042-9b7a-c7265317f3c8.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>而在这组“极致渣清型”图片的超分效果中，Waiuf2x仍然明显不够清晰。</p>
<p>而RealESRGAN整体清晰是清晰，却仍然出现了杂线，以及和明显的伪影——只有Real-CUGAN画面干干净净，表现最好。</p>
<p><strong>面向4类玩家提供不同参数配置</strong></p>
<p>为了方便更多的创造者，Real-CUGAN面向4类群体开源了不同的推理参数设置。</p>
<p><strong>-Windows 玩家</strong></p>
<p>Real-CUGAN为Windows用户打包了一个可执行环境（下载链接可在文末的仓库里自取）。</p>
<p>通过congfig文件可进行通用参数设置：在mode中填写video或者image决定超视频还是超图像。</p>
<p>模型分三类，具体选哪种也给了参考：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/7a02afc7-2efe-4896-8a5c-3c984a824876.png" target="_blank"><img alt="二次元最懂二次元：B站开源动漫画质修复模型 超分辨率画质更好" h="55" src="https://img1.mydrivers.com/img/20220202/S7a02afc7-2efe-4896-8a5c-3c984a824876.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>-Waifu2x-caffe玩家</strong></p>
<p>提供了两套参数：Real-CUGAN2x标准版(denoise-level3) 和Real-CUGAN2x无切割线版。</p>
<p><strong>-Python玩家</strong></p>
<p>需torch>=1.0.0，配备numpy、opencv-python、moviepy模块。</p>
<p><strong>-VapourSynth玩家（专业视频压制）</strong></p>
<p>这个就不细说了，相应的读者可以参见仓库的Readme说明～</p>
<p>最后，Real-CUGAN也正在计划更新更多：包括快速模型、简单的GUI、一步超到任意指定分辨率功能以及对本身效果的改进（优化纹理保留，削减模型处理痕迹）。</p>
<p>心动的朋友可以戳下方链接试试手：<a class="f14_link" href="https://github.com/bilibili/ailab/tree/main/Real-CUGAN" target="_blank">点此跳转</a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/github.htm"><i>#</i>GitHub</a><a href="https://news.mydrivers.com/tag/bilibili.htm"><i>#</i>哔哩哔哩</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/tGl6hjm6fTU6uyX0dgz-ZA">量子位</a></span>
<span>责任编辑：祥云</span>
</p>
        
</div>
            