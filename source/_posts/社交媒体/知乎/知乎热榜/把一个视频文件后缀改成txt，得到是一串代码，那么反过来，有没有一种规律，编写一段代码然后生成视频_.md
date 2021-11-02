
---
title: '把一个视频文件后缀改成txt，得到是一串代码，那么反过来，有没有一种规律，编写一段代码然后生成视频_'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic1.zhimg.com/v2-bd3cfe5905a8cb6ab81c110ae2a2fa75_720w.jpg'
author: 知乎
comments: false
date: Mon, 01 Nov 2021 23:43:16 GMT
thumbnail: 'https://pic1.zhimg.com/v2-bd3cfe5905a8cb6ab81c110ae2a2fa75_720w.jpg'
---

<div>   
萝魏紫的回答<br><br><p>这是属于定性正确，定量物理上做不得的情况。计算机工程作为一种工科工程学，和其他工程学一样，有很多这种定性正确但是实际上做不到的，比如计算机密码学里面的强密码也可以通过反复尝试而算出来，只不过要几百亿年罢了。</p><p>多说无益，给你看实际的。</p><p>打开一个视频。这个视频多长。当然，我擦掉点网站链接什么。</p><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-bd3cfe5905a8cb6ab81c110ae2a2fa75_720w.jpg" data-caption data-size="normal" data-rawwidth="232" data-rawheight="41" class="content_image" referrerpolicy="no-referrer"></figure><figure data-size="normal"><img src="https://pic3.zhimg.com/v2-fc4efadc4b8708a2ec58c7a948ac04ad_1440w.jpg" data-caption data-size="normal" data-rawwidth="1759" data-rawheight="701" class="origin_image zh-lightbox-thumb" data-original="https://pic3.zhimg.com/v2-fc4efadc4b8708a2ec58c7a948ac04ad_r.jpg" referrerpolicy="no-referrer"></figure><p>视频都是声音和图像组成的，我这个是mp4封装，当然封装和压制还能讲一整天，这里忽略，总之你下载下来的视频，最后到手就是这么个mp4的玩意，里面你要看的都有了。</p><p>你看红色箭头。位率，也有人叫码率的，也就是说，这个通道上，一秒钟有多少数据。当然，现在的视频都是可变比特率的，根据画面动的快慢自动变化。好在我这个视频，都是室内镜头，没什么高速公路追车的，变化不大，就近似看成一样好了。</p><p>6899kbps，就是我这个视频，一秒钟快7000，000 b,你注意，计算机里面B是byte，b是bits，差八倍。bit就是0或1，当然bit到Byte还有什么校验位啊，字长啊，放到计算机里面还有块长啊之类的，我们这不是考组成，都忽略了，理解个原理就成。</p><p>一秒钟就是七百万个0或1. 我这个电影，两个多小时。504亿个0和1.正常语速大概200到300音节一分钟，你要讲一分钟不停全速念，得五年半才能念完。</p><p>这0和1可不能随便，是有要求的。</p><p>比如上面这一帧，截图下来看是这样的，这就是最常见的我们IT讲的“二进制”，普通人讲的0和1，其实是十六进制啦，省的太长显示不下来，毕竟二进制和十六进制天生fit</p><figure data-size="normal"><img src="https://pic4.zhimg.com/v2-9c0b8d8dca93e2dacd712be461006d24_1440w.jpg" data-caption data-size="normal" data-rawwidth="1906" data-rawheight="832" class="origin_image zh-lightbox-thumb" data-original="https://pic4.zhimg.com/v2-9c0b8d8dca93e2dacd712be461006d24_r.jpg" referrerpolicy="no-referrer"></figure><p>比如我在中间插入了一大段其他的0，1，红色部分</p><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-5cb0c28f14e04350c331bd37aa97dd0c_1440w.jpg" data-caption data-size="normal" data-rawwidth="759" data-rawheight="654" class="origin_image zh-lightbox-thumb" data-original="https://pic1.zhimg.com/v2-5cb0c28f14e04350c331bd37aa97dd0c_r.jpg" referrerpolicy="no-referrer"></figure><p>再打开，就变成这样了，因为每个字节都是有自己的要求的，不能随便上。</p><p><br></p><figure data-size="normal"><img src="https://pic2.zhimg.com/v2-897b71446f675343f2ae6eefc7b352e2_1440w.jpg" data-caption data-size="normal" data-rawwidth="1168" data-rawheight="678" class="origin_image zh-lightbox-thumb" data-original="https://pic2.zhimg.com/v2-897b71446f675343f2ae6eefc7b352e2_r.jpg" referrerpolicy="no-referrer"></figure><p>所以要直接写出500亿个有格式规定的01来生成视频，几乎是不可能的啦，起码现在科技不行。</p><p>这个问题和下面问题一样的核心原理。</p><p><a href="https://www.zhihu.com/question/399474422/answer/1278732101" class="internal">文件是不是都由0和1组成的，一个视频文件包含多少0和1呢？通过这些0和1可以得到视频吗？</a></p>  
</div>
            