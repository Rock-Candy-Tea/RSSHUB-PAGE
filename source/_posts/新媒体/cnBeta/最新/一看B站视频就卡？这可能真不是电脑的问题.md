
---
title: '一看B站视频就卡？这可能真不是电脑的问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0414/b2a13290c7fcda9.jpg'
author: cnBeta
comments: false
date: Thu, 14 Apr 2022 10:14:52 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0414/b2a13290c7fcda9.jpg'
---

<div>   
不知道最近屏幕前的小伙伴有没有这样的经历：一用浏览器打开B站视频，就会偶尔出现卡顿的情况，部分场景下还会出现电脑风扇狂转的情况，十分的诡异。这时有用户指出B站处于节省带宽的目的在Web端开启了HEVC编码播放，导致电脑播放时造成较高的负载，对此B站也是予以了回应。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0414/b2a13290c7fcda9.jpg" referrerpolicy="no-referrer"></p><p>看到这里，相信不少围观群众就要纳闷了：这个HEVC编码到底是个什么东西？怎么开了以后电脑就卡？</p><p>这就要从视频的编码技术开始说起了，而且笔者可以肯定地说，电脑卡顿的锅，源头既不在B站身上，也不是电脑配置低，至于为什么，还请接着往下看：</p><p><strong>所谓视频编码方式就是指通过压缩技术，将原始视频格式的文件转换成另一种视频格式文件的方式。</strong></p><p>这里有个重点是对视频进行压缩，那为什么要压缩视频呢？其实很简单，因为原始视频实在是太大了。</p><p>拿一个1080P（1020x1080）分辨率，60帧的视频举例，未经压缩的情况下，光是一帧就有1920x1080x3/1024/1024≈6MB的内容，每秒就占据了大约360MB的内容，这样的大小连本地存储都费劲，更何况用于网络传输，现如今千兆带宽才刚刚开始普及，承载不了这么庞大的数据量，因此显然需要对原始视频进行一定的处理。</p><p>这也是视频编码技术出现的缘由，通过去除视频数据中冗余信息，实现视频数据在互联网中快速传输和离线的存储。使得视频数据量得以极大的压缩，有利于传输和存储。</p><p>在过去的几十年中，一系列的视频编码标准被广泛的应用。<strong>目前已有的视频压缩标准有很多种，包括国际标准化组织（ISO）和国际电工技术委员会（IEC）制定的MPEG-1、MPEG-2、MPEG-4标准；国际电信联盟电信标准化部门（ITU-T）制定的H.261、H.263等等。</strong></p><p>直到2003年，ITU-T和ISO/IEC正式公布了H.264/MPEG-4 AVC视频压缩标准，由于在编码效率和灵活性方面有着相当大的优势，H.264也成为了目前应用最为广泛的视频编码标准。</p><p><img src="https://static.cnbetacdn.com/article/2022/0414/6d3e7750a770bd1.jpg" referrerpolicy="no-referrer"></p><p>而HEVC则是H.264之后又一革命性的视频编码技术，相比传统的H.264编码技术，HEVC可以在保证相同视频画质的前提下，减少约50%左右的数据量，同时支持8K视频的编码。</p><p>如此先进的编码技术自然也是得到了众多厂商的支持，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>、安卓、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>、NVIDIA、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>等厂商都先后对HEVC编码技术进行了支持。</p><p>那看起来很美好的一个事情，为什么到浏览器这里就不行了呢？</p><p>问题主要出在HEVC复杂的专利授权模式上，光是HEVC技术相关的专利池就有MPEG LA、HEVC Advance和Velos Media三家，而高额的授权费用往往使得很多厂商望而却步，以MPEG LA为例，厂商每年前十万台终端免费，之后每台终端花费0.20美元，2500万美元封顶，这对于可以免费下载到多台设备的浏览器厂商来说，无疑是十分巨大的开销。</p><p>也因此，<strong>很多浏览器都放弃了GPU对HEVC硬解的支持，因此在观看HEVC编码的视频时，CPU负载经常过高</strong>，也就出现了文章最开始所说的卡顿或者<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C738%2C751" target="_blank">风扇</a>狂转的情况，只有Safari幸免于难。</p><p><img src="https://static.cnbetacdn.com/article/2022/0414/8b11e7b8ef63f1c.jpg" referrerpolicy="no-referrer"></p><p>当然，众多厂商也并没有完全摆烂，谷歌曾经开发了一套叫做VP9的编码技术，但由于种种原因并未普及开来，后来谷歌、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>、亚马逊、Facebook、Netflix等几大互联网公司联合推出了开源免费的AV1编码技术，但由于在视频编解码方面，为这个编码格式提供硬件解码的厂商目前比较少，导致AV1编码技术在普及之路上也充满了艰难险阻。</p><p>所以短期来看，浏览器不支持HEVC编码还没有什么好的解决方法，不过2020年，Fraunhofer宣布最新的视频编解码标准 H.266/VVC制定完成。同等画质下将节省近50%传输流量，清晰度越高，码率节省越多。这项耗时3年的标准，主要面向未来的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_110018%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">4K</a>和8K，希望H.266的出现能改善这个局面吧。</p>   
</div>
            