
---
title: 'iOS新BUG被发现：路由器使用特定SSID会让Wi-Fi秒挂'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210620/s_6ac3980352ac41f893fe591fa4c2c08a.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sun, 20 Jun 2021 08:26:56 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210620/s_6ac3980352ac41f893fe591fa4c2c08a.jpg'
---

<div>   
<p>相比多数人都有过类似经历，打开Wi-Fi，搜索出的SSID或者说路由器的名字千奇百怪。</p>
<p>对于iOS用户来说，安全研究人员发现一个新的BUG，仅仅通过一个奇葩的SSID，就能让iPhone的Wi-Fi连接异常。</p>
<p><strong>示例SSID为“%p%s%s%s%s%n”，iPhone或者iPad要么无法连接，要么无网络，使用不了隔空投递等功能。</strong></p>
<p>对上述BUG一个可能的解释是，%语法在编程中常用，即将变量格式化为输出字符串，C语言中，%n即不打印任何内容并将到目前为止已打印的字符数写入int变量。所以猜测Wi-Fi子系统可能将未分析的SSID传递给执行字符串格式设置的内部库，从而导致任意内存写入和缓冲区溢出。</p>
<p>当然，简单的处理办法就是重置网络设置即可。</p>
<p>显然，这和此前iOS上的“短信炸弹”，都是特定字符串引起的系统混乱，没办法，原谅二进制的世界……</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210620/6ac3980352ac41f893fe591fa4c2c08a.jpg" target="_blank"><img alt="iOS新BUG被发现：路由器使用特定SSID会让Wi-Fi秒挂" h="334" src="https://img1.mydrivers.com/img/20210620/s_6ac3980352ac41f893fe591fa4c2c08a.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/ios.htm"><i>#</i>iOS</a><a href="https://news.mydrivers.com/tag/wi-fi.htm"><i>#</i>Wi-Fi</a></p>
<p class="url">
     
<span>责任编辑：万南</span>
</p>
        
</div>
            