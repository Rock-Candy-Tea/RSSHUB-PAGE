
---
title: '看个 B 站搞得电脑风扇狂转？ 网友们这次炸了……'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/03/yhjI1VXGzQ2ENjpGDf59.png'
author: 人人都是产品经理
comments: false
date: Thu, 14 Apr 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/03/yhjI1VXGzQ2ENjpGDf59.png'
---

<div>   
<blockquote><p>编辑导语：前段时间，B站又陷入舆论的风口浪尖。有人爆料B站为了省带宽，强行在Web端开启了HEVC编码视频播放，这导致电脑端看B站视频时，容易出现高负载运行状态。本文作者就此事展开了分析，希望能够给大家带来帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-775240 aligncenter" src="https://image.yunyingpai.com/wp/2022/03/yhjI1VXGzQ2ENjpGDf59.png" alt referrerpolicy="no-referrer"></p>
<p>最近托尼刷到一条微博，内容大致说的是 B 站为了省带宽，强行在 Web 端开启了 HEVC 编码视频播放，导致我们在用浏览器看 B 站视频的时候，电脑很容易就会处在一种高负载的运行状态。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/o1rLXtWLdZ5KIILF9AAX.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="677" height="323" referrerpolicy="no-referrer"></p>
<p>很多网友看到这条微博之后，也是纷纷在评论区留言说“怪不得我一看 B 站电脑风扇就狂转掉电还贼快 ”、“我说呢，看B 站视频时不时会卡原来是这么回事 ”、“ 看 B 站能耗掉油管两倍的电 ”。</p>
<p>尽管B 站官方后来发文表示HEVC 编码方式并不是强制使用，只有设备满足一定性能才会开启：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/DUqiiZ7VXqeXx4IVO8vQ.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="668" height="208" referrerpolicy="no-referrer"></p>
<p>但依然还是有很多网友不买账。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/81qHJlck12Dn34ZLmoqN.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" referrerpolicy="no-referrer"></p>
<p>讲真，在没看到那条微博前，托尼之前还真没怎么注意到这个事情，不过在了解清楚 HEVC 究竟是什么后，我觉得这次很多人可能错怪 B 站了。</p>
<p><strong>至少在使用 HEVC 编码视频播放这件事上，B 站这么做并没有错，反而是浏览器拖了 B 站的后腿。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/rdMU9cmbEeLhK1Sl4EWM.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" referrerpolicy="no-referrer"></p>
<p>为什么这么说呢？这就要从视频压缩的必要性开始说起了。</p>
<p>很多人可能不知道，无论是我们用手机拍出来的视频，还是别人发在网上的视频，其实都经过了压缩，<strong>如果视频没压缩，原始文件就会变得非常大。</strong></p>
<p>就拿一段 1080P 60 帧的视频来说吧。</p>
<p>视频每一帧有 200 万像素（ 1920*1080 ），每个像素算占3 个字节（ R、G、B 各一个），这意味着一帧画面就要消耗 5.7MB，60 帧就是 342 MB：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/B3pVXOTuvtUUQ4TrSsZ7.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="624" height="298" referrerpolicy="no-referrer"></p>
<p>如果不压缩，<strong>一台 256G的手机，满打满算也只能拍766.5 秒1080P 60 帧视频</strong>，换你你能接受？</p>
<p>另外要是你想在线观看完全没压缩过的1080P 60 帧视频，没 3000 兆以上的宽带提供网速支持，视频来不及加载也就根本没法流畅播放好吧。</p>
<p>所以为了方便视频的保存和传播，我们肯定有必要对它进行压缩。</p>
<p>压缩视频的原理讲起来有点儿复杂，但要是往简单的说主要就是干了三件事 —— <strong>跳帧、划块、抽色。</strong></p>
<p>比如说在前期把相似的画面只保留一帧，后期再通过预测还原；</p>
<p>又或者把一块颜色相同的区域当做一个大色块处理；</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/zL7o2rkoLbZ63fW31W8N.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" referrerpolicy="no-referrer"></p>
<p>再或者偷偷砍掉人眼不容易察觉的颜色，毕竟现在的视频甚至能装十亿种色彩，人眼基本分辨不出那么多。</p>
<p>总之效率越高压缩编码技术，往往可以在保证不损失画质的前提下，尽可能地把视频体积压缩到更小。</p>
<p><strong>而 HEVC 就是一种高效的视频压缩编码技术，它通常也被叫作 H.265。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/Mk4o9BhWoiZqbA6IzEiF.jpeg" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" referrerpolicy="no-referrer"></p>
<p>根据官方给出的说法，HEVC相比传统的AVC 也就是H.264 压缩编码技术，可以在保证相同视频画质的前提下，减少约 50% 左右的数据量。</p>
<p>简单来说就是同等规格的视频，<strong>采用 HEVC 编码所需要的空间大概是 AVC 的一半甚至更少，</strong><strong>而且 HEVC 最高甚至支持对 8K 超高清视频进行编码。</strong></p>
<p>这样一来经过 HEVC 编码压缩之后的视频，体积还可以进一步减小，我们也只需更低的带宽就能实现高清视频在线播放或者直播推流。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/XVJjpGHYJlph1ijUD880.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" referrerpolicy="no-referrer"></p>
<p>也正是基于HEVC 这种更高效的编码，早在 2017 年，苹果就开始让自家 iOS 11 支持 HEVC，并且首个支持 HEVC 的应用就是它自带的相机App。</p>
<p>而安卓后来也是很快就跟上了，<strong>到如今基本上每台手机都能拍摄并且播放 HEVC 编码格式的视频：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/kP4iKCtpu6CVRNK029xI.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="727" height="403" referrerpolicy="no-referrer"></p>
<p>另外像是 AMD、NVIDIA、英特尔等厂商，也早就在硬件上开放了对HEVC 编解码的支持。</p>
<p>别的不说，英伟达 2014 年发布的 GTX 750，就支持一部分 HEVC 视频的编解码：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/LUU3lhPBz38r99L8GPs9.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="684" height="318" referrerpolicy="no-referrer"></p>
<p>而对画质有追求的B 站呢，也是从 2019 年就上线了 HEVC 编码，算是国内一众视频网站中最早支持 HEVC 的那一批，它这么做也算是在紧跟潮流。</p>
<p>之所以我们看 B 站视频会导致电脑卡顿或者发热严重，<strong>要怪就怪 Chrome 和那些使用 Chromium 内核的浏览器到现在都不支持 GPU 硬解 HEVC。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/0JC4lprnoEGVphdqWgDH.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="591" height="319" referrerpolicy="no-referrer"></p>
<p>浏览器不支持 GPU 硬解 HEVC 会导致一个问题，<strong>那就是它在播放视频时只能通过 CPU 来实现软解码，这对 CPU 的运算性能要求非常高。</strong></p>
<p>托尼实测，用 Chrome 看 B 站高画质的视频。</p>
<p>如果你在设置里选了“优先使用 HEVC 编码视频播放”，你会发现它对 CPU 的占用率非常高，都快飙到 100 了，而对 GPU 的占用率却一直都很低：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/v3vG3VvGWZoPXX5oZCiU.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="615" height="386" referrerpolicy="no-referrer"></p>
<p>而一旦你把视频切换成Chrome 支持硬解的 AVC 编码播放，浏览器对 CPU 的占用率立马就会降下去，GPU 的占用率虽然有所上升，但并不算高：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/8hfv6SBe4mZ82RlGtzUd.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="596" height="379" referrerpolicy="no-referrer"></p>
<p>这是因为 GPU 拥有专门的解码模块，<strong>在硬解对应编码视频时候的解码效率非常高，不但能减轻 CPU 的负担，还有着功耗低、发热少的特点。</strong></p>
<p>遗憾的是，托尼特意去搜了下，目前除了苹果端的 Safari 浏览器，包括 Chrome、Edge 在内的其它几个主流浏览器均不支持硬解 HEVC。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/VaShgfpq2NxETKEGSa2V.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="567" height="258" referrerpolicy="no-referrer"></p>
<p>这些浏览器不支持硬件 HEVC 的原因倒不是因为技术受限，而是因为想要获得 HEVC 相关组织的授权，所需要支付的授权费一点都不低。</p>
<p>目前负责 HEVC 授权的组织一共有三家，就拿其中相对比较厚道的 MPEG LA 来说。</p>
<p>想要获得它家的 HEVC 授权，<strong>厂商每年头十万台终端免费，之后每台终端就要花费 0.20 美元，不过每年封顶 2500 万美元</strong>，但也是笔不小的数目。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/iZldVUnc7dzXEvnc1olQ.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="589" height="272" referrerpolicy="no-referrer"></p>
<p>这个费用在手机厂商看来可能没啥，毕竟成本分摊到每台手机上也就是两块不到的事情，但对于可以免费下载到多台设备的浏览器来说就很恐怖了。</p>
<p>所以之前谷歌也搞了一套叫做 VP9 的编码方式，性能和 H.265 差不多，但其他厂商不乐意啊！</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/5uQJWZd2JIYXhg72GDIU.jpeg" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="600" height="350" referrerpolicy="no-referrer"></p>
<p>一方面是因为 Chrome 的市占率太大，要是大家选了这套方案，谷歌肯定一家独大，甚至可能垄断视频编码市场。</p>
<p>另一方面，则是因为 VP 系列编码是参考 H.26x 开发，对于这编码是否侵犯专利还真说不清楚，万一真出事了，那些用了 VP9 的厂商，可能也会有麻烦。</p>
<p>到时候出事了谷歌可不会对此负责~</p>
<p>所以现在谷歌、微软、亚马逊、Facebook、Netflix 等几大互联网公司联合推出了开源免费的 AV1 压缩编码技术。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/huFEqCJ0umpyzUl74xfD.jpeg" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="638" height="336" referrerpolicy="no-referrer"></p>
<p>它的视频压缩效率不比 HEVC 低，既然有免费的这些浏览器当然会优先考虑支持它。</p>
<p>之所以要这么干，也是因为天天给别人交专利费，心里不爽，有这个技术条件，搞个更好用的出来，岂不美哉？</p>
<p>只不过由于在视频编解码方面，为这个编码格式提供硬件解码的厂商目前比较少，现在只有各大芯片厂商以及最新的显卡比如 RTX 系列才能支持。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/hy8eVqGzvHqDX3iFi3Nm.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="622" height="352" referrerpolicy="no-referrer"></p>
<p>所以日后 AV1 能不能成为一种主流视频编码格式还是个问题。</p>
<p>‍‍‍‍‍‍回到 B 站推 HEVC 这件事上。</p>
<p>B 站作为国内少有能提供 8K 以及 HDR 10 内容的视频网站，它在借助 HEVC 给我们提供更高规格视频的同时还能节省带宽，这事本身就值得肯定。</p>
<p>之前甚至还有不少人通过 B 站 UWP 应用提供的 HEVC 视频扩展，在 Windows 上白嫖到了本来要花钱才能买到的 HEVC 解码器。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/dQNf3FwHffwYnAAwkaFq.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" width="625" height="416" referrerpolicy="no-referrer"></p>
<p>不过话说回来，B 站支持 HEVC 编码是一回事，它在这个编码下能给视频提供多少码率就是另外一回事了。</p>
<p>有网友表示，最近 B 站给 HEVC 的码率变低了，结果导致选择 HEVC 播放的视频画质还不如 AVC，尤其是在 1080P 分辨率下会特别明显。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/GH8EUaKwk5NEDiUH0MvW.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" referrerpolicy="no-referrer"></p>
<p>然而也有人实际测试了下，在 1080P 分辨率下，HEVC 的视频码率确实比 AVC 高：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" src="https://image.yunyingpai.com/wp/2022/04/2lYbAzsQHjcZ3t0TIuzH.png" alt="看个 B 站搞得电脑风扇狂转？ 网友们这次炸了。" referrerpolicy="no-referrer"></p>
<p>由于这点还存在争议，所以托尼对这事也不好评价。</p>
<p>但不管怎么说，HEVC 必然是一个大趋势，在流媒体平台和硬件产品的通力支持下，我们离顺畅体验它的未来，应该也不远了。</p>
<p> </p>
<p>作者：托尼；公众号：差评</p>
<p>原文链接：https://mp.weixin.qq.com/s/XU_Qwcp9Tp_wHTrAr6l6GQ</p>
<p>本文由 @差评 授权发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
                      
</div>
            