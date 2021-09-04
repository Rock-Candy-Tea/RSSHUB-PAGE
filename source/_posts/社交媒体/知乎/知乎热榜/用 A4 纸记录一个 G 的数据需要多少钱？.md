
---
title: '用 A4 纸记录一个 G 的数据需要多少钱？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic4.zhimg.com/v2-fa042e26b5a2874bdb12ac11d3397af1_1440w.jpg'
author: 知乎
comments: false
date: Sat, 04 Sep 2021 08:03:43 GMT
thumbnail: 'https://pic4.zhimg.com/v2-fa042e26b5a2874bdb12ac11d3397af1_1440w.jpg'
---

<div>   
木头龙的回答<br><br><h2>激光打印机30来张纸吧，多少钱看你用什么纸什么打印机</h2><p><br></p><p>记录数据为什么要用10pt等线字体呢？</p><p><br></p><p>既然电脑的数据是二进制的0和1，那么我们用纸来记录的时候，用一个点是否有颜色来表示就可以了。</p><p><br></p><p>所以一张纸能记录多少数据，取决于打印机可以打印出多精细的点。以京东自营超过30万好评的HP 1136激光打印机为例，分辨率1200dpi，也就是每英寸打印1200个点。</p><p><br></p><p>A4纸大小是8.3"×11.7"，很容易计算打满的话是139,838,400个点。不过为了避免边缘的数据难以分辨，我们在四周留出100个点的空白（2毫米多一点），那就是135,078,400个点，每个点代表1bit，每字节8bit，那就是16,884,800字节。</p><p><br></p><p>然后我们可以双面打印，所以要打印1000进制的1GB数据，需要：</p><p>1,000,000,000÷16,884,800÷2=30张纸。</p><p>如果是1024进制的1GiB数据，需要：</p><p>1,073,741,824÷16,884,800÷2=32张纸。</p><p><br></p><p>不过这样直接打印，万一碰到一长串的0/1，就很难辨认，可以参考多种串行技术采用的8b/10b编码，每8个bit用10个bit表示，平衡白点和黑点数量，使得每20bit中0、1数量相差不超过2个，而且不会出现连续5个及以上的0和1。这样需要多消耗25%的纸张，如果觉得太浪费而且分辨设备的分辨率足够高的话，可以用PCIe 3.0采用的128b/130b编码，这样只需要多消耗1.56%纸张，可以忽略不计了。</p><p><br></p><p>当然，如果你用喷墨打印机，或者用600dpi分辨率打印，或者你用照片纸打印，价格自然会不一样。</p><hr><p>补充：针对评论区的一些意见统一回答一下：</p><p><b>激光打印机真的能打印1200dpi的点么？</b></p><p>这个其实我自己是存疑的。不过激光打印机打印的字体边缘非常清晰的。借用 <a class="member_mention" href="http://www.zhihu.com/people/23dacaee24800ca8af1407c5d53f2763" data-hash="23dacaee24800ca8af1407c5d53f2763" data-hovercard="p$b$23dacaee24800ca8af1407c5d53f2763">@Xin Sui</a> 这篇文章</p><a href="https://zhuanlan.zhihu.com/p/136509245" data-draft-node="block" data-draft-type="link-card" class="internal">Xin Sui：针式、激光、喷墨文字打印品质对比</a><p>里面的一张图片（大家可以放大来观察字体边缘）：</p><figure data-size="normal"><img src="https://pic4.zhimg.com/v2-fa042e26b5a2874bdb12ac11d3397af1_1440w.jpg" data-caption data-size="normal" data-rawwidth="2380" data-rawheight="2944" data-default-watermark-src="https://pic3.zhimg.com/v2-f634eb9fa38d72bf81db7f7dcd8d9609_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic4.zhimg.com/v2-fa042e26b5a2874bdb12ac11d3397af1_r.jpg" referrerpolicy="no-referrer"></figure><p>如果实际测试无法准确还原的话，打印时设置到600DPI应该是可以接受的。</p><p><br></p><p><b>如何读取这些数据？</b></p><p>扫描仪就可以，4800dpi的扫描仪也就几百块钱的事情，不过我不确认这个4800dpi是否是物理分辨率。</p><p>实在不行，胶片扫描仪的精度高很多，价格也不至于不可接受。</p><p><br></p><p><b>彩色、灰度更省钱</b></p><p>打印不同于显示器，通过亮度的不同来显示不同深度的颜色，墨水、碳粉只有一种颜色而且不会发光，只能通过打印点的不同密度来显示不同深度的颜色。这也是为什么我们的屏幕通常使用96DPI，打印文字一般需要300DPI，照片需要600甚至更高DPI的原因。所以使用最高DPI的话，密度失效，理论上一个点只能有一种颜色，没有灰度这么一说。</p><p><br></p><p>即使DPI减半，不考虑墨点/碳粉重叠带来的识别问题，也只能容纳4种颜色，代表2bit。相比耗材成本的提高，还不如多用一张纸。</p>  
</div>
            