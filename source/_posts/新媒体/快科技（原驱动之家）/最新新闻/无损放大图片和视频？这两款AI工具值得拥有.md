
---
title: '无损放大图片和视频？这两款AI工具值得拥有'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220120/Sc22a3999-d9c2-4042-a038-cdfd0076e616.jpg'
author: 快科技（原驱动之家）
comments: false
date: Thu, 20 Jan 2022 08:57:37 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220120/Sc22a3999-d9c2-4042-a038-cdfd0076e616.jpg'
---

<div>   
<p>身为一个编辑，除了文字工作这个主要的工作内容之外，经常还需要考虑一个很重要的问题：插图。</p>
<p>全是文字的文章肯定没有图文形式的文章抓人眼球，更别提这个视频当道的年代了，因此每次撰写文章的时候，笔者都要在无版权图片网站精挑细选，让图片和文章主旨契合，并且最好是高分辨率的图像。</p>
<p>但意外也总是有的，有的时候遇到了分辨率不足但偏偏最适合的图像，就很让人苦恼了，直接将低分辨率图像插入文章中，会很明显地感觉到视觉上的不舒适，虽然现在PS甚至是Windows自带的画图工具都能修改图片分辨率，但强行拉伸的结果只会是：图片非常糊。</p>
<p>可以看到，在进行图片拉伸后，图片边缘已经出现了明显的毛刺感。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220120/c22a3999-d9c2-4042-a038-cdfd0076e616.jpg" target="_blank"><img alt="无损放大图片和视频？这两款AI工具值得拥有" h="537" src="https://img1.mydrivers.com/img/20220120/Sc22a3999-d9c2-4042-a038-cdfd0076e616.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>那有没有什么方法能够让图片无损放大呢？</p>
<p><strong>别说，还真有，这个来自GitHub的项目“waifu2x”就能做到。</strong></p>
<p>项目地址为https://github.com/nagadomi/waifu2x，有兴趣的朋友可以研究一下，网页版地址为<a class="f14_link" href="http://waifu2x.udp.jp/" target="_blank">http://waifu2x.udp.jp/</a>。</p>
<p>闲话少说，这里直接放使用waifu2x和普通拉伸图片后的对比（左侧为拉伸，右侧为使用waifu2x的效果）。</p>
<p style="text-align: center"><img alt="无损放大图片和视频？这两款AI工具值得拥有" h="207" src="https://img1.mydrivers.com/img/20220120/858c1ab2-cf03-4bcc-91d5-a4f06cac2cec.jpg" style="border: black 1px solid" w="552" referrerpolicy="no-referrer"></p>
<p><span style="color:#ff0000;"><strong>可以看到，使用waifu2x放大图片后，“5G”边缘的毛刺感不再明显，虽然部分区域还存在噪点问题，但整体上来说，比直接拉伸的效果要好太多。</strong></span></p>
<p>那为什么waifu2x可以做到无损放大图片呢？这是因为waifu2x使用了名为SR-CNN的卷积算法，传统意义上来说，图像超分辨率问题研究的是在输入一张低分辨率图像时（LR），如何得到一张高分辨率图像（HR）。</p>
<p>传统的图像插值算法可以在某种程度上获得这种效果，比如最近邻插值、双线性插值和双三次插值等，但是这些算法获得的高分辨率图像效果并不理想。</p>
<p>SR-CNN是首个使用CNN结构（即基于深度学习）的端到端的超分辨率算法，它将整个算法流程用深度学习的方法实现了，并且效果比传统多模块集成的方法好。</p>
<p>SR-CNN流程如下:首先输入预处理。对输入的低分辨率LR图像使用bicubic算法进行放大，放大为目标尺寸。</p>
<p>那么接下来算法的目标就是将输入的比较模糊的LR图像，经过卷积网络的处理，得到超分辨率SR的图像，使它尽可能与原图的高分辨率HR图像相似。</p>
<p>与Bicubic、SC、NE+LLE、KK、ANR、A+这些超分算法相比，SR-CNN在大部分指标上都表现最好，且复原速度也在前列，且RGB通道联合训练效果最好，这就意味着相比照片，waifu2x在放大插画（你们最喜欢的二次元图片）时会更有优势。</p>
<p>关于SR-CNN卷积算法，可以到https://arxiv.org/abs/1501.00092了解更多详情。</p>
<p>那既然图片可以无损放大，视频呢？</p>
<p>结果当然也是可行的，不过这次用到的工具，<strong>叫做Topaz Gigapixel AI for Video，这个软件通过数千个视频进行培训，</strong>并结合来自多个输入视频帧的信息，通过真实的细节和运动一致性将视频放大至8K分辨率。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220120/f421b9ca-b2d5-4ba0-a653-9974c42c65e3.jpg" target="_blank"><img alt="无损放大图片和视频？这两款AI工具值得拥有" h="462" src="https://img1.mydrivers.com/img/20220120/Sf421b9ca-b2d5-4ba0-a653-9974c42c65e3.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>作为一个AI软件，它需要一台快速的计算机。推荐的系统配置是32 GB RAM加上具有6GB或更大显存的NVIDIA显卡。虽然也勉强能在旧电脑上跑，但速度会非常慢。</p>
<p>那Topaz Gigapixel AI for Video是如何做到放大视频的呢？其实在安装的时候，会发现这个软件会安装TensorFlow库和cuDNN库，所以很明显，该软件就是运用基于深度学习的卷积神经网络对每一帧进行处理,全程跑CUDA单元（要不然也不会这么慢了）。</p>
<p>熟悉显卡的老哥们都知道，显卡作为电脑主机里的一个重要组成部分，是电脑进行数模信号转换的设备，承担输出显示图形的任务。</p>
<p>显卡接在电脑主板上，它将电脑的数字信号转换成模拟信号让显示器显示出来，同时显卡还是有图像处理能力，可协助CPU工作，提高整体的运行速度。对于从事专业图形设计的人来说显卡非常重要。</p>
<p>民用和军用显卡图形芯片供应商主要包括AMD和NVIDIA两家（今年Intel也会加入乱战）。</p>
<p>GPU的构成相对简单，有数量众多的计算单元和超长的流水线，特别适合处理大量的类型统一的数据，例如矩阵乘法和加法，因此显卡在AI领域的应用也就变得十分广泛，CUDA是NVIDIA推出的只能用于自家GPU的并行计算框架。</p>
<p>只有安装这个框架才能够进行复杂的并行计算，主流的深度学习框架也都是基于CUDA进行GPU并行加速的，Tensorflow也不例外。</p>
<p>不过比较遗憾的是，Topaz Gigapixel AI for Video的售价还是比较贵的，接近200美元的价格可以劝退很多人了，但用来还原或者修复某些古老的影视作品还是相当有用的，现在能在B站搜索到的相当一部分【4K修复】视频，都是基于这个软件制作的。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220120/114bc57d-8e24-4359-8a2d-b096943a5832.jpg" target="_blank"><img alt="无损放大图片和视频？这两款AI工具值得拥有" h="318" src="https://img1.mydrivers.com/img/20220120/S114bc57d-8e24-4359-8a2d-b096943a5832.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>现在想想，AI的出现确实解决了生活中的很多实际问题，如果没有卷积神经网络的高速发展，看到高清重制版的古老影视作品，可能只会存在于想象中。</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/ruanjian.htm"><i>#</i>软件</a><a href="https://news.mydrivers.com/tag/tuxiangchuli.htm"><i>#</i>图像处理</a></p>
<p class="url">
     <span>原文链接：<a href="https://smartcity.zol.com.cn/785/7855060.html">中关村在线</a></span>
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            