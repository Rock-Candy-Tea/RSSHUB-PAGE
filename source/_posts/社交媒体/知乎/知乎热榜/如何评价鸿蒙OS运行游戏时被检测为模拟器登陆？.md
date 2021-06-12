
---
title: '如何评价鸿蒙OS运行游戏时被检测为模拟器登陆？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic3.zhimg.com/v2-5a0d28f539fbc30282ce92446603289a_1440w.jpg'
author: 知乎
comments: false
date: Sat, 12 Jun 2021 07:54:07 GMT
thumbnail: 'https://pic3.zhimg.com/v2-5a0d28f539fbc30282ce92446603289a_1440w.jpg'
---

<div>   
姬昌 君的回答<br><br><p></p><p></p><p>并不能，虚拟机是什么，虚拟机就模拟了一个计算机（现代手机也是计算机），里面再装上操作系统。</p><p>一般pc的虚拟机软件都会明确告诉内部系统这个主机的名字是虚拟机。</p><p>安卓模拟器这种手机模拟器在实际使用中，可能由于手机绑定的性质，会提供虚拟一个手机的型号来欺骗系统和软件，让其误以为是实体手机。所以手机APP检测运行环境会更严格一点，会通过分辨率，系统型号，Mac地址和登录手机号之类的多种数据去推断运行环境，而非简单询问系统。</p><p>应该是通过读取数据，发现运行的环境不符合数据库已有的安卓手机特征给出的提示，过段时间数据库加上了就正常了。明显是没适配的原因。</p><hr><p>有疑问的看看以下连接</p><a href="http://link.zhihu.com/?target=https%3A//m.sohu.com/a/314532590_354899" data-draft-node="block" data-draft-type="link-card" class=" wrap external" target="_blank" rel="nofollow noreferrer">反虚拟机和沙箱检测的一些小技巧_手机搜狐网</a><hr><p>为了防止你们误会“不适配”代表着我认为鸿蒙是完全全新的系统，给你们从代码上介绍一下原理。</p><h2>我就喜欢这种字体编程，看着头疼你们自己克服一下。</h2><p>最近在看RPG Maker MV的代码，用它介绍一下基于JavaScript的浏览器游戏怎么判断自己运行在不同设备上，毕竟web应用天生跨平台，适配鸿蒙分分钟。</p><figure data-size="normal"><img src="https://pic3.zhimg.com/v2-5a0d28f539fbc30282ce92446603289a_1440w.jpg" data-caption data-size="normal" data-rawwidth="663" data-rawheight="430" data-default-watermark-src="https://pic2.zhimg.com/v2-0552bec92a103194d9a78f6ec60c19e5_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic3.zhimg.com/v2-5a0d28f539fbc30282ce92446603289a_r.jpg" referrerpolicy="no-referrer"></figure><p>因为市面上只有这两种系统，肯定直接问一下当前用的是什么系统</p><figure data-size="normal"><img src="https://pic4.zhimg.com/v2-20ab80adbd02b9ce4bae4c1e906e74e8_1440w.jpg" data-caption data-size="normal" data-rawwidth="595" data-rawheight="1045" data-default-watermark-src="https://pic2.zhimg.com/v2-8fc6a182c53f8008525168eb55bfdbd1_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic4.zhimg.com/v2-20ab80adbd02b9ce4bae4c1e906e74e8_r.jpg" referrerpolicy="no-referrer"></figure><p>代码贴在这里了，询问方法是直接查看 navigator.userAgent 里的内容进行比较，除了以上几种固定情况，那就认为不是移动设备了，因为它只考虑游戏运行在移动设备上时需要屏幕虚拟按键，而对这种设备，它只考虑是不是安卓和苹果。</p><p>那么 navigator.userAgent 数据怎么来的呢？</p><figure data-size="normal"><img src="https://pic2.zhimg.com/v2-45b04bb390823cfba90f8e53b2b8b600_720w.jpg" data-caption data-size="normal" data-rawwidth="415" data-rawheight="423" data-default-watermark-src="https://pic3.zhimg.com/v2-4d8b6605411a75e6fd13f0e85ad21294_720w.jpg" class="content_image" referrerpolicy="no-referrer"></figure><figure data-size="normal"><img src="https://pic2.zhimg.com/v2-03791276a173b0110a134204e5ce67eb_1440w.jpg" data-caption data-size="normal" data-rawwidth="877" data-rawheight="318" data-default-watermark-src="https://pic1.zhimg.com/v2-afcf47b21f5a16d726b37eee2a7314c6_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic2.zhimg.com/v2-03791276a173b0110a134204e5ce67eb_r.jpg" referrerpolicy="no-referrer"></figure><p>他是浏览器告诉程序的。</p><p>所以如果不做修改，添加新的判断条件，直接运行在鸿蒙上，鸿蒙告诉你系统名字是HarmonyOS，不满足移动设备条件，那就识别为PC，不给你虚拟按键。这叫什么，这叫不适配。</p><p>我之前说的其他检测机制，就是为了应对最后一张图片最后一句，用户通过修改达成的欺骗，让PC被识别为移动设备，为了识别出真实的设备情况，采取的不完全信任 navigator.userAgent 得到的数据结果。不过想了一下，鸿蒙天生就不满足 navigator.userAgent 对真实手机的判断，既能运行，又不是移动设备，那肯定是模拟器没跑了，网易大概是这样简单粗暴但是没有鸿蒙这种捣乱的套壳系统，那就非常正确的工程做法。适配鸿蒙，只要在安卓那里加个判断条件就好了。</p><p></p>  
</div>
            