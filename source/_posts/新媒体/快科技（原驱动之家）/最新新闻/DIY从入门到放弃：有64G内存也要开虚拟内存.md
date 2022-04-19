
---
title: 'DIY从入门到放弃：有64G内存也要开虚拟内存'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220419/Sc324ec5c-40d4-4066-a0e8-c9f5531d55e3.jpg'
author: 快科技（原驱动之家）
comments: false
date: Tue, 19 Apr 2022 06:35:47 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220419/Sc324ec5c-40d4-4066-a0e8-c9f5531d55e3.jpg'
---

<div>   
<p>提到虚拟内存，玩家会有2种心态，一是觉得虚拟内存高大上，担心设置错误出现故障而不敢操作；另一种则是觉得虚拟内存太简单，有钱就加内存条，没必要在低速硬盘中划分虚拟内存空间。<strong>其实这两种说法都是错误的，本期DIY从入门到放弃就来聊一聊虚拟内存。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220419/c324ec5c-40d4-4066-a0e8-c9f5531d55e3.jpg" target="_blank"><img alt="DIY从入门到放弃：有64G内存也要开虚拟内存" h="400" src="https://img1.mydrivers.com/img/20220419/Sc324ec5c-40d4-4066-a0e8-c9f5531d55e3.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>首先要了解的是，我们通常所说的虚拟内存和微软也就是windows官方的虚拟内存指的不是一个概念，在实际的应用中会存在一些疑惑，也需要玩家先了解清楚。</p>
<p><span style="color:#ff0000;"><strong>我们一般说的虚拟内存，指的是在硬盘上划分出来的一个独立空间，和主板上的物理内存（RAM）做区分，是作为物理内存的辅助。</strong></span></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220419/70e60f56-7b57-463c-b447-a3c9fdc44a7e.jpg" target="_blank"><img alt="DIY从入门到放弃：有64G内存也要开虚拟内存" h="396" src="https://img1.mydrivers.com/img/20220419/S70e60f56-7b57-463c-b447-a3c9fdc44a7e.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>而在Windows里，硬盘上划分出来的这块空间被称为为“page file”，直译为页面文件，而虚拟内存（virtual memory）指的则是物理内存和page file的和，为了方便理解和描述，下文中统一将page file称为虚拟内存，主板上的内存称为物理内存。</p>
<p>虚拟内存是在硬盘上划分出一块专属空间，当做内存使用，但和大多数玩家的理解不同，虚拟内存和物理内存并不承担完全一样的作用，<strong>除了可以作为内存使用之外，还会让系统能够从物理内存中转移不常使用的数据，从而让系统更高效地使用物理内存来处理更频繁访问的数据。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220419/3fb6313b-3342-445b-91aa-7f9f04b84edf.jpg" target="_blank"><img alt="DIY从入门到放弃：有64G内存也要开虚拟内存" h="499" src="https://img1.mydrivers.com/img/20220419/S3fb6313b-3342-445b-91aa-7f9f04b84edf.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>换句话说，虚拟内存可以看做是物理内存的“仓库”，因为其本质还是硬盘，所以读写速度要比物理内存慢得多，不经常使用的数据放在这里，受速度的影响不大，而物理内存则存放经常使用的数据，可以让系统运行更高效。</p>
<p><strong>如果用户的物理内存空间很大，是不是就不用开启虚拟内存了呢？</strong>其实并不是，而且我还建议用户开启大容量的虚拟内存。</p>
<p>一方面，很多大型3D建模软件需要大容量的内存保障高效的运行，有时候浏览器也会占用非常多的内存，有充裕的虚拟内存可以让系统更加流畅；另一方面，即使不使用大型软件也不会多开应用，开启虚拟内存可以获得高宽容度的地址混淆，更强大的进程分叉缓存，优化内存纠错等等加成，而硬盘容量本身不会占据很多成本，所以还是划算的。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220419/6a6a3418-5cb6-4d37-be46-ee045ff1d643.jpg" target="_blank"><img alt="DIY从入门到放弃：有64G内存也要开虚拟内存" h="328" src="https://img1.mydrivers.com/img/20220419/S6a6a3418-5cb6-4d37-be46-ee045ff1d643.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>开启虚拟内存的方法其实也很简单，以Windows 10系统为例，在桌面右键单击“此电脑”打开属性页面，在底部的“高级系统设置”中打开“高级”选项卡，单击性能区域的“设置……”按钮，找到“高级”选项卡，在虚拟内存区域单击“更改……”按钮，就可以打开虚拟内存的设置页面了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220419/7e203e93-3bdd-4d7a-af54-9bf3c94d5d42.jpg" target="_blank"><img alt="DIY从入门到放弃：有64G内存也要开虚拟内存" h="493" src="https://img1.mydrivers.com/img/20220419/S7e203e93-3bdd-4d7a-af54-9bf3c94d5d42.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>如果对电脑的参数不了解，建议勾选“自动管理所有驱动器的分页文件大小(A)”前面的复选框，系统会自动设置虚拟内存的空间。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220419/c9e3dbd9-7882-42f3-8d6c-61d6b5a15f15.jpg" target="_blank"><img alt="DIY从入门到放弃：有64G内存也要开虚拟内存" h="803" src="https://img1.mydrivers.com/img/20220419/Sc9e3dbd9-7882-42f3-8d6c-61d6b5a15f15.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>如果物理内存足够大，且不经常使用大型3D制图软件，不经常玩3A大作，虚拟内存可以设置512-1024MB。</p>
<p>如果物理内存只有8G甚至4G，且有运行大型软件玩大型游戏的需求，虚拟内存建议设置为物理内存的1.5倍。</p>
<p>在设置完成之后点击确认，注意需要重启电脑才会生效。如果C盘空间有限，也可以将虚拟内存设置在其他盘符下。<strong>最后要提醒大家的是，虚拟内存并不是设置得越大就越好，而是要根据自己的实际使用环境和硬盘容量进行设置，来让电脑有更好的运行环境。</strong></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：建嘉</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/diannao.htm">电脑</a><a href="https://news.mydrivers.com/tag/pcdiannao.htm">PC电脑</a><a href="https://news.mydrivers.com/tag/neicun.htm">内存</a><a href="https://news.mydrivers.com/tag/diy.htm">DIY</a>  </p>
        
</div>
            