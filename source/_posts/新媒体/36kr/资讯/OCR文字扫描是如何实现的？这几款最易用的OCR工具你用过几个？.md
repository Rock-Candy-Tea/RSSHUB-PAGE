
---
title: 'OCR文字扫描是如何实现的？这几款最易用的OCR工具你用过几个？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20211022/v2_0a664bf9c25240c48a45c650fe40d738_img_000'
author: 36kr
comments: false
date: Fri, 22 Oct 2021 08:30:29 GMT
thumbnail: 'https://img.36krcdn.com/20211022/v2_0a664bf9c25240c48a45c650fe40d738_img_000'
---

<div>   
<p>随着图片时代的深度发展，大量的文字内容为了优化排版和表现效果，都采用了图片的形式发布和存储，这为内容的传播和安全性带来了很大的便利，但对于内容编辑者来说，却造成了一些不便——需要重复性劳动。</p> 
<p class="image-wrapper"><img data-img-size-val="640,427" src="https://img.36krcdn.com/20211022/v2_0a664bf9c25240c48a45c650fe40d738_img_000" referrerpolicy="no-referrer"></p> 
<p>OCR文字扫描工具逐渐走进广大内容制作者的视野，帮助用户解决了内容编辑的难题。</p> 
<p>OCR全称是Optical Character Recognition，意思是“光学字符识别技术”，是最为常见的、也是目前最高效的文字扫描技术，它可以从图片或者PDF中识别和提取其中的文字内容，输出文本文档，方便验证用户信息，或者直接进行内容编辑。</p> 
<p>那么OCR技术是如何实现文字识别的呢？从图片到文字的过程发生了什么？</p> 
<p class="image-wrapper"><img data-img-size-val="640,92" src="https://img.36krcdn.com/20211022/v2_06b10463d8ec48e3bf0a5fd5e08aace5_img_000" referrerpolicy="no-referrer"></p> 
<p>典型的OCR技术路线分为5个大的步骤，分别是输入、图像与处理、文字检测、文本识别，及输出。每个过程都需要算法的深度配合，因此从技术底层来讲，从图片到文字输出，要经历以下的过程：</p> 
<ol style="list-style-type: decimal;" class=" list-paddingleft-2"> 
 <li><p>图像输入：读取不同图像格式文件；</p></li> 
 <li><p>图像预处理：主要包括图像二值化，噪声去除，倾斜校正等；</p></li> 
 <li><p>版面分析：将文档图片分段落，分行；</p></li> 
 <li><p>字符切割：处理因字符粘连、断笔造成字符难以简单切割的问题；</p></li> 
 <li><p>字符特征提取：对字符图像提取多维特征；</p></li> 
 <li><p>字符识别：将当前字符提取的特征向量与特征模板库进行模板粗分类和模板细匹配，识别出字符；</p></li> 
 <li><p>版面恢复：识别原文档的排版，按原排版格式将识别结果输出到文本文档；</p></li> 
 <li><p>后处理校正: 根据特定的语言上下文的关系，对识别结果进行校正。</p></li> 
</ol> 
<p>走完了全部的8个流程，输出后的文档才能尽可能地避免错别字和语义上的错误，方便用户直接使用。</p> 
<p class="image-wrapper"><img data-img-size-val="640,420" src="https://img.36krcdn.com/20211022/v2_0e37d9f9fe8d4880a303ea2e35e4c25e_img_000" referrerpolicy="no-referrer"></p> 
<p>由于汉字的构型中有很多重复的偏旁部首，以及很多字形相似的字体，比如“已”和“己”这样的汉字，所以识别汉字的难度比识别英文字母高出很多。为了提高这个过程的识别准确率，我们熟知的大公司如<a class="project-link" data-id="28215" data-name="百度" data-logo="https://img.36krcdn.com/20210806/v2_f96267de58b643faae02c0cb24debbed_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/28215" target="_blank">百度</a>和<a class="project-link" data-id="24961" data-name="腾讯" data-logo="https://img.36krcdn.com/20201201/v2_016524a9a477434cb3584e1558f3257a_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/24961" target="_blank">腾讯</a>，还专门为此进行过AI训练，以优化特征库的丰富度、准确度以及算法的匹配效率，借助机器学习和AI，OCR工具的识别准确率直线上升，极少出现错误。</p> 
<p class="image-wrapper"><img data-img-size-val="640,399" src="https://img.36krcdn.com/20211022/v2_a3a7ffde4e074a09b6e2b2e2aeda7c29_img_000" referrerpolicy="no-referrer"></p> 
<p>不过借助AI，就意味着过程中需要<a class="project-link" data-id="207497" data-name="连接网" data-logo="https://img.36krcdn.com/20210809/v2_b7ddae3cbe4647dcad5304a917c7dd30_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/207497" target="_blank">连接网</a>络与云特征库进行匹配，因此会有一定的隐私和数据风险，这也是基于AI的OCR识别工具的唯一劣势。</p> 
<p>OCR技术的成熟，使得图文时代的内容编辑更加轻松，对于经常和文字图片打交道的职场人士来说，基于OCR技术的文字识别和提取工具是必不可少的办公神器，除了专门的文档管理工具如Document和CS全能扫王，不少我们熟悉的APP都内置了文字识别工具，比如<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>和为微云。</p> 
<p>那么在我们日常的办公场景中，哪些OCR识别工具离我们最近，使用最方便呢？</p> 
<h3 label="二级标题" style>微信</h3> 
<p>微信7.0版本之后便内置了文字提取工具，点击聊天中的图片，再长按呼出菜单，选择下方的“文字提取”，经过云处理后，就可以提取出其中的文字内容，使用方法还是非常简单的。</p> 
<p class="image-wrapper"><img data-img-size-val="640,1138" src="https://img.36krcdn.com/20211022/v2_46e4a9354dbe43e3b4819abe67339f4c_img_000" referrerpolicy="no-referrer"></p> 
<p>遗憾的是，微信电脑版并不具备这一功能，无法和Word直接打通，不然的话，效率超级加倍！</p> 
<h3 label="二级标题" style>QQ截图</h3> 
<p>电脑版QQ自带的截图工具功能非常丰富，是很多人都习惯使用的截图方式，默认呼出快捷键为“Ctr+Alt+A”，和微信的“Alt+A”截图工具，在用户习惯程度上不相上下。</p> 
<p class="image-wrapper"><img data-img-size-val="640,370" src="https://img.36krcdn.com/20211022/v2_9d15e2cb5cf94d3d8dd31d4338f12bd0_img_000" referrerpolicy="no-referrer"></p> 
<p>QQ截图识别出来的文字，在回车符上可能会有部分不准确的情况，直接粘贴会丢失格式，以及使用过程中必须登陆QQ，因此不是<a class="project-link" data-id="149284" data-name="非常完美" data-logo="https://img.36krcdn.com/20210808/v2_bf6495ae826142ee9e4d47b1c4febc8a_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/149284" target="_blank">非常完美</a>。</p> 
<p>不过考虑到PC端的文字编辑流程，使用鼠标点击就能完成文字识别，仍然是非常高效的。</p> 
<h3 label="二级标题" style>印象笔记</h3> 
<p><a class="project-link" data-id="26151" data-name="印象笔记" data-logo="https://img.36krcdn.com/20211019/v2_62848122054547c6b25081b985f38b66_img_000" data-refer-type="1" href="https://www.36dianping.com/space/3011001034" target="_blank">印象笔记</a>是大家熟悉的老牌笔记软件了，印象笔记从很早就开始支持OCR文稿扫描功能，并且功能较为完善，可以一次扫描多张稿件，适合用来做大批量文字资料的录入。</p> 
<p class="image-wrapper"><img data-img-size-val="640,959" src="https://img.36krcdn.com/20211022/v2_7a970ebf888446e5b2405342a018d5ee_img_000" referrerpolicy="no-referrer"></p> 
<p>这些方便又好用的文字识别工具你掌握了吗？据传即将到来的新版Edge浏览器，也将内置OCR识别工具，支持从网页中的图片上提取文字，大家可以期待一下！</p> 
<p>本文来自<a href="https://36kr.com/projectDetails/3968527">微信</a>公众号“ZEALER”（ID:zealertech），作者：ZEALER，36氪经授权发布。</p>  
</div>
            