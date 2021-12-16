
---
title: '这么多年都被Windows骗了 硬盘容量为啥总不够'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211216/S9365ec65-69ad-49bf-8874-bcee1947f17c.jpg'
author: 快科技（原驱动之家）
comments: false
date: Thu, 16 Dec 2021 10:13:29 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211216/S9365ec65-69ad-49bf-8874-bcee1947f17c.jpg'
---

<div>   
<p><span style="color:#ff0000;"><strong>你买的1TB硬盘为啥到手只有931GB，那100GB上哪去了？是不是硬盘厂骗我呢？</strong></span></p>
<p>为啥买了iPhone就发现iPhone 13 Pro Max 远峰蓝1TB版里面确实写的就是1TB甚至还多出来零点几TB，看到这是不是想马上振臂一喊：苹果牛哔！</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211216/9365ec65-69ad-49bf-8874-bcee1947f17c.jpg" target="_blank"><img alt="这么多年都被Windows骗了 硬盘容量为啥总不够" h="376" src="https://img1.mydrivers.com/img/20211216/S9365ec65-69ad-49bf-8874-bcee1947f17c.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
苹果的1TB就是1TB</p>
<p><strong>别着急，其实只不过是微软这么多年以来一直有一个小的错误而已，这个问题出在单位上，</strong>我们平常说的KB、MB、GB、TB，其实全称应该是Kilobyte、Megabyte、Gigabyte、Terabyte，中文名字分别叫千字节，兆字节，吉字节，太字节，之后其实还有其他的更大的单位，但咱们这里先不考虑了，都一样。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211216/a77edf72-fb95-4f55-86e2-9c62d9668137.jpg" target="_blank"><img alt="这么多年都被Windows骗了 硬盘容量为啥总不够" h="450" src="https://img1.mydrivers.com/img/20211216/Sa77edf72-fb95-4f55-86e2-9c62d9668137.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
出来挨打</p>
<p>问题出现在这里了，按照国际单位制 (SI)的标准，Kilo前缀代表1000倍的Byte，Mega前缀代表（1000*1000），也就是1000的二次方，以此类推，Giga代表（1000*1000*1000），1000的三次方。这样算下来的话，确实这个单位换算就是1000进制的。也就是我们常见的硬盘存储空间的算法，也是苹果使用的标准，这种算法的国际单位制（SI）标准写法就是KB、MB、GB、TB（B一定大写，代表byte字节，如果是小写b就代表bit位，1Byte=8bit）。</p>
<p>因此我们看到苹果设备的存储空间就是“足容”的，1TB版的手机，就是显示1TB空间。</p>
<p>在微软这边就不一样了，微软在Windows当中使用的单位也写成了KB、MB、GB、TB，但他的计算方式是按照二进制的方法，这种方式的准确写法应该是KiB、MiB、GiB、TiB，全称是Kilo binary byte可以缩写成Kibibyte（千位二进制字节）、Mega binary byte 缩写成Mebibyte、Giga binary byte 缩写成Gibibyte、Tera binary byte 缩写成Tebibyte。</p>
<p><strong>这个二进制换算的方式就变成了，1KiB=1024Byte，1MiB=1024KiB，2的十次方。</strong>问题就出在这个地方，相当于准确写，你买的1TB的硬盘在Windows系统中显示成了931.51 GiB，但由于Windows的显示小问题，系统中显示的是“931.51 GB”。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211216/7e703a10-90a7-407f-9238-2a0e4a6ff4ec.jpg" target="_blank"><img alt="这么多年都被Windows骗了 硬盘容量为啥总不够" h="244" src="https://img1.mydrivers.com/img/20211216/S7e703a10-90a7-407f-9238-2a0e4a6ff4ec.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
磁盘0就是一个1TB的机械硬盘</p>
<p>虽然这中间有点换算的小问题，但由于Windows有全世界超过九成以上的装机量，大家都这么用之后，也就逐渐成了习惯，如果突然再改回去，又可能导致一些奇怪的问题，所以干脆就这样吧，大家都这么认为，不就成了行业标准么？</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211216/d7613c4c-be6a-473d-8c43-1c27bc683ed6.jpg" target="_blank"><img alt="这么多年都被Windows骗了 硬盘容量为啥总不够" h="787" src="https://img1.mydrivers.com/img/20211216/Sd7613c4c-be6a-473d-8c43-1c27bc683ed6.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
Windows其实已经严谨的显示了字节数量</p>
<p>Windows其实也十分严谨的在属性当中准确的显示了文件的提及大小，后面的换算只是为了显示直观一些。</p>
<p>其实这个单位上的差异，早在很多年前大家就已经发现了，<strong>很多用苹果电脑的朋友应该也发现了同样的文件从网上下载下来或者从Windows电脑拷贝过来就会莫名其妙的变大一些，这其实就是单位显示的问题。</strong></p>
<p><span style="color:#ff0000;"><strong>之前大家还以为是硬盘厂商偷工减料，但现在看起来似乎也不完全是这样，只不过是单位换算的问题。</strong></span></p>
<p>现状就是，苹果设备因为使用了国际单位制 (SI)的标准，不会出现对不上号的问题，所以没有在参数页面进行特别注释。而一些经常用在Windows生态下面的硬件设备几乎都对这些容量单位换算方式进行了备注。</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/yingpan.htm"><i>#</i>硬盘</a></p>
<p class="url">
     <span>原文链接：<a href="https://diy.zol.com.cn/783/7831967.html">中关村在线</a></span>
<span>责任编辑：建嘉</span>
</p>
        
</div>
            