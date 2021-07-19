
---
title: '微软Windows Hello曝漏洞：外接一个USB摄像头，分分钟破解你的电脑'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210719/v2_016403bfe6f0469fa55a876519d594d5_img_000'
author: 36kr
comments: false
date: Mon, 19 Jul 2021 06:31:25 GMT
thumbnail: 'https://img.36krcdn.com/20210719/v2_016403bfe6f0469fa55a876519d594d5_img_000'
---

<div>   
<p>Windows Hello，相信大家都不陌生了。</p> 
<p>毕竟一度被称为“最简单的登录方式”——刷个脸，电脑就可以立马解锁。</p> 
<p><img src="https://img.36krcdn.com/20210719/v2_016403bfe6f0469fa55a876519d594d5_img_000" data-img-size-val="1080,542" referrerpolicy="no-referrer"></p> 
<p>但就在最近，它却被曝出了一个大bug：</p> 
<p>只需外接一个USB摄像头，2帧图像。</p> 
<p>然后“啪的一下”，就进来了……</p> 
<h2>Windows Hello最近不太好</h2> 
<p>人脸解锁，近几年可以说是越发的普及。</p> 
<p>像苹果的iPhone和iPad，就可以利用自带的前置摄像头来解锁。</p> 
<p><img src="https://img.36krcdn.com/20210719/v2_8f42352925e84a8fac8689f1c6a1af42_img_000" data-img-size-val="1080,709" referrerpolicy="no-referrer"></p> 
<p>但Windows电脑的人脸识别解锁，不仅可以用自带摄像头，也可以与第三方网络摄像头<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>工作。</p> 
<p>于是，这一点就成功引起了安全公司CyberArk一名研究员的注意。</p> 
<p>他认为：</p> 
<blockquote> 
 <p>老式的网络摄像头，在收集和传输数据过程中，安全性是比较差的。</p> 
</blockquote> 
<p>目前市场上很多刷脸解锁，利用的都是RGB人脸解锁方法。</p> 
<p>但网络摄像头除了有RGB传感器之外，还拥有红外传感器。</p> 
<p>于是这名研究员便对Windows Hello做了一番研究。</p> 
<p>真是“不看不知道，一看吓一跳”。</p> 
<p>他惊奇地发现：</p> 
<blockquote> 
 <p>Windows Hello甚至不看RGB数据。</p> 
</blockquote> 
<p><img src="https://img.36krcdn.com/20210719/v2_70d6c921b1694201a1dcd45f0fc191aa_img_000" data-img-size-val="1080,594" referrerpolicy="no-referrer"></p> 
<p>什么意思？</p> 
<p>黑客只需向PC发送两帧，就可以直接骗过你的Windows Hello。</p> 
<p>其中<a class="project-link" data-id="397963" data-name="一帧" data-logo="https://img.36krcdn.com/20200729/v2_d4652a1312b14f6696e9a17200dba1c1_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/397963" target="_blank">一帧</a>是目标的真实红外捕捉数据，而另一帧是空白黑帧。</p> 
<p>第二帧是用来欺骗WindowsHello的有效性验证的。</p> 
<p>操作也可以说是相当简单了。</p> 
<p>外接一个USB网络摄像头，传送一个图像，Windows Hello就会误以为“哦！主人出现了”……</p> 
<p>对此，这名研究员做出了如下解释：</p> 
<blockquote> 
 <p>我们试图去找人脸识别中最脆弱的环节，以及看看什么方法是最有意思、最容易的。</p> 
 <p>我们创建了一个完整的 Windows Hello 面部识别流图，发现“黑掉”它最简单的方法，就是假装一个摄像头。</p> 
 <p>这是因为整个系统都依赖于它的输入。</p> 
</blockquote> 
<h2>微软回应：已出补丁</h2> 
<p>这种破解方式，听上去确实有些简单可行了。</p> 
<p>于是，<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a>这边也立即作出了回应：</p> 
<blockquote> 
 <p>这是Windows Hello安全功能的绕过漏洞（bypass vulnerability）。</p> 
</blockquote> 
<p>并且在本月的13日，已经发布了补丁来解决这一问题。</p> 
<p><img src="https://img.36krcdn.com/20210719/v2_570e7dfe33f24a43b12532011c896a90_img_000" data-img-size-val="1080,407" referrerpolicy="no-referrer"></p> 
<p>但是CyberArk公司对用户还是做出了这样的建议：</p> 
<blockquote> 
 <p>建议采用增强后的Windows Hello登录方式。</p> 
</blockquote> 
<p>这种方式是采用了微软“基于虚拟化的安全”，来对Windows Hello 的面部数据进行加密。</p> 
<p>而且这些数据是在内存保护区被处理的，这样一来，数据就不会被篡改了。</p> 
<p>那么接下来的一个问题是，CyberArk为什么要选择攻击Windows Hello？</p> 
<p>对此，公司的解释如下：</p> 
<blockquote> 
 <p>从行业角度来看，研究人员对PIN破解和欺骗指纹传感器等方式，已经做过大量的研究工作了。</p> 
</blockquote> 
<p><img src="https://img.36krcdn.com/20210719/v2_c69b7741caf94167a5cdd5294f342d0a_img_000" data-img-size-val="1080,459" referrerpolicy="no-referrer"></p> 
<p>其次，Windows Hello所涵盖的用户数量可以说是相当庞大了。</p> 
<p>据微软去年5月的数据，这个服务拥有超过1.5亿用户；而去年12月，微软更是表示：</p> 
<blockquote> 
 <p>84.7%的 Windows 10用户，使用 Windows Hello 登录。</p> 
</blockquote> 
<p>但或许你更关心的一点是，自己是否会受到影响。</p> 
<p>就目前来看，这方面的担忧也是大可不必了。</p> 
<p>因为这种攻击方法只是听起来简单，但对于不是黑客出身的人来说，实现起来还是有困难的。</p> 
<p>包括网友们也留言道：</p> 
<blockquote> 
 <p>是很酷的一种方法，但普通用户无需担心。</p> 
</blockquote> 
<p><img src="https://img.36krcdn.com/20210719/v2_051d06f5845248b7ba1b08051718fbcc_img_000" data-img-size-val="1080,187" referrerpolicy="no-referrer"></p> 
<p>最后，这位研究员表态道：</p> 
<blockquote> 
 <p>这种攻击方式我们早就知道了，对于微软还是挺失望的。</p> 
 <p>他们对摄像头的安全性、可信度，没有做更严格的要求。</p> 
</blockquote> 
<h3 label="二级标题" style>参考链接</h3> 
<p>[1]https://www.wired.com/story/windows-hello-facial-recognition-bypass/</p> 
<p>[2]https://www.reddit.com/r/windows/comments/omwsm0/hackers_got_past_windows_hello_by_tricking_a/</p> 
<p>[3]https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-34466</p> 
<p>[4]https://www.cyberark.com/resources/threat-research-blog/bypassing-windows-hello-without-masks-or-plastic-surgery</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/uKJqnmeD6VPk7Kqf89tm2Q">“量子位”（ID:QbitAI）</a>，作者：金磊，36氪经授权发布。</p>  
</div>
            