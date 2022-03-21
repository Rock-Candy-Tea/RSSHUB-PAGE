
---
title: '在Android上跑Windows 11，只是一场美丽的误会'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220321/v2_f3b05d352c654c0791b1e80e2ba42f29_img_000'
author: 36kr
comments: false
date: Mon, 21 Mar 2022 12:06:32 GMT
thumbnail: 'https://img.36krcdn.com/20220321/v2_f3b05d352c654c0791b1e80e2ba42f29_img_000'
---

<div>   
<p>最近这段时间，谷歌刚刚发布的Android 13开发者预览版系统在各大手机论坛可谓是很火了一把。原因倒不是因为它是迄今最新的Android版本，而是由于在这一系统中进行一些“操作”后，我们将手机变成下图的这个样子。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_f3b05d352c654c0791b1e80e2ba42f29_img_000" referrerpolicy="no-referrer"></p> 
<p>没错，熟悉PC的朋友想必已经看出来，这是微软Windows 11的界面。事实上，这个截图也确实来自一台Pixel 6，更准确地说，是来自一台运行在Android 13系统内部的Windows 11虚拟机。 </p> 
<p>根据最早如此操作的海外网友描述，Windows 11“在Android 13里”的运行状况相当良好，虽然目前还没有办法解决GPU加速问题（也就是基本没法运行3D程序），但CPU、内存和内置存储设备都能发挥出接近原生的性能。如果不嫌弃的话，甚至已经可以在手机上玩一些早期的像素风或3D游戏了——虽然只靠CPU进行运算，但也并不会卡顿。 </p> 
<p>看到这你是不是已经心动了？别急，让我们先来给你解释一下，为什么Android 13“能够”运行Windows 11，以及其背后的用意。 </p> 
<p>首先用最通俗的话来说，之所以此前的Android版本都没有类似功能，唯有Android 13可以做到这一点，是因为谷歌在这个最新版的系统中首次集成了一个名为“受保护的内核虚拟机（pKVM）”的功能。与其他大家熟悉的虚拟机类似，pKVM可以模拟出一个硬件环境，从而运行各种各样的操作系统，不仅是Windows 11，实际上还包括桌面版Linux或其他更冷门的系统。 </p> 
<p>那么它在实际的使用当中，到底又能起什么作用呢？有些朋友可能会想到微软此次在Windows 11上新增的WSA（Windows Android子系统）功能，认为谷歌是想“反其道而行之”，让消费者能够在手机上运行Windows软件。 </p> 
<p>然而大家要明白，Android、或者至少AOSP（可以理解为Android的开源版本）是一个免费、开源的软件。微软在Windows里要加入一个Android模块，用于运行Android APP，在法律上是不会有任何风险的。但Windows可不是开源系统，就算谷歌有这个想法和技术，要在手机上跑Windows本身其实是一件风险很大的事情。 </p> 
<p>其次，微软之所以要将Android应用引入Windows 11，还有一个原因是因为现在很多Windows PC都有触控屏，再加上Windows自带的窗口化机制，运行Tik Tok之类的Android APP无论体验还是实用性都是已经不错了。但反过来说，在一台6.x英寸的手机屏幕上，运行很可能没有针对触控设计过的Windows软件，这么搞真的有实用价值吗？ </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_5e61492c518a461c92ff64340944cc25_img_000" referrerpolicy="no-referrer"></p> 
<p>没错，虽然我们从前文中就已提及，现在Android 13的确具备了能在虚拟机里运行Windows 11、甚至其他更多PC操作系统的“能力”。但这种能力本身，其实并不在谷歌的意料之内，本质上只不过是极客玩家对Android 13所集成pKVM功能的一种变通，以及破解式的用法而已。 </p> 
<p>按照我们三易生活目前所得到的消息显示，谷歌之所以要在Android 13里引入一个新的虚拟机模块，本来的用意其实是为了让市场中大量的“魔改”第三方系统变得更加安全。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_f23b403ac8fd4d228b52794fe497eaec_img_000" referrerpolicy="no-referrer"></p> 
<p>而这个说法的证据，则来自Android系统团队的开发者Will Deacon。据他所言，由于过去的Android版本一直缺乏一个虚拟机，就导致许多手机厂商喜欢把版权保护、安全加密，以及其他一些自研的第三方二进制代码，“扔”到处理器的Hypervisor层运行。而Hypervisor则是ARM处理器内置的一个虚拟化相关模块，但问题就在于它的权限太高，甚至比操作系统本身还高，万一手机厂商自己编写的代码出了点问题，就可能会损害到系统本身。 </p> 
<p>相比之下，Android 13引入的pKVM虚拟机，在权限上与主操作系统是平行、且隔离的。所以哪怕你在其中运行恶意软件，理论上也无法感染到手机自身的主系统。再加上pKVM可以提供近似原生的性能，这就使得新版系统在提高安全性的同时，也不会损害到这些手机厂商自研代码的执行效率。 </p> 
<p>说实在的，虽然这个功能听起来有点深奥，但它对于普通用户的意义，其实要比单纯在手机上运行Windows软件要重大得多。 </p> 
<p>【本文图片来自网络】 </p> 
<p>本文来自微信公众号 <a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MzA4MTk2NTk5Nw==&mid=2649808563&idx=2&sn=c76ac7fbcac740260719c095a41b248d&chksm=87889871b0ff11679efeabae072dc9330b44dc196453b83e93aae770366183e3484c60cc9ac7#rd">“三易生活”（ID：IT-3eLife）</a>，作者：三易菌，36氪经授权发布。</p>  
</div>
            