
---
title: '无法运行Win11的原因已找到！一文了解TPM'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210701/S18b66adf-6c61-4252-8821-8c66254fdb96.jpg'
author: 快科技（原驱动之家）
comments: false
date: Thu, 01 Jul 2021 09:07:15 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210701/S18b66adf-6c61-4252-8821-8c66254fdb96.jpg'
---

<div>   
<p>前几天微软针对Windows 11升级发布的检测软件上线，让TPM 2.0走进了大众的视野，很多人表示电脑里还有这样一个玩意呢？它到底是干什么的？</p>
<p>TPM英文全名为Trust Platform Module，中文名叫可信平台模块。TPM一种行业标准，<strong>目前最新标准为TPM 2.0，在2016年制定，上一代标准为TPM 1.2在2011年制定。</strong></p>
<p>相较于TPM 1.2，TPM 2.0的兼容性更好，安全性更高。如果想要使用TPM 2.0，就需要电脑里有符合TPM 2.0标准的安全芯片，因此完整的TPM 2.0模块可以理解为TPM 2.0标准+安全芯片。</p>
<p>TPM模块主要作用是加密，通过芯片内置的加密算法生成秘钥，可以有效地保护电脑，防止非法用户访问。</p>
<p><span style="color:#ff0000;"><strong>同时因为TPM芯片本身具有存储能力，所以有些电脑的指纹识别、磁盘加密功能也会通过TPM模块来实现。</strong></span></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210701/18b66adf-6c61-4252-8821-8c66254fdb96.jpg" target="_blank"><img alt="无法运行Win11的罪魁祸首 TPM是什么？" h="419" src="https://img1.mydrivers.com/img/20210701/S18b66adf-6c61-4252-8821-8c66254fdb96.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>如果想要确认自己电脑有没有TPM 2.0模块，可以在运行命令里输入tpm.msc，以此打开TPM管理器来查看TPM模块的情况。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210701/059aab27-17e6-4b80-8894-22a8e54e12dc.jpg" target="_blank"><img alt="无法运行Win11的罪魁祸首 TPM是什么？" h="195" src="https://img1.mydrivers.com/img/20210701/S059aab27-17e6-4b80-8894-22a8e54e12dc.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>TPM 2.0模块目前比较广泛应用于笔记本电脑上，台式机比较少。</p>
<p><span style="color:#ff0000;"><strong>因为台式机就算支持TPM 2.0模块也会默认关闭，开启的话很简单，在主板BIOS中打开就行了，</strong></span>一般在电脑高级Advance选项中，以华硕主板为例，我们进入到高级选项的PCH FW设置里。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210701/77df623d-48cd-440a-944f-d24aaf85852a.jpg" target="_blank"><img alt="无法运行Win11的罪魁祸首 TPM是什么？" h="450" src="https://img1.mydrivers.com/img/20210701/S77df623d-48cd-440a-944f-d24aaf85852a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>进入后可以看到PTT选项，因为国内消费级主板根据政策原因不提供TPM芯片，所以需要处理器的支持，PTT是英特尔处理器模拟TPM功能。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210701/c6b065db-8bf5-46a2-b33a-cc753d534765.jpg" target="_blank"><img alt="无法运行Win11的罪魁祸首 TPM是什么？" h="450" src="https://img1.mydrivers.com/img/20210701/Sc6b065db-8bf5-46a2-b33a-cc753d534765.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>BIOS里PTT选项默认为“开启独立TPM”，这其实是关闭了PTT选项，下面的“开启”选项才是真正的开启。开启INTEL PTT时会出现注意事项，确认开启PTT后，TPM 2.0也会随之打开。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210701/532ead99-3606-44c1-9cd4-83b6acdafd28.jpg" target="_blank"><img alt="无法运行Win11的罪魁祸首 TPM是什么？" h="381" src="https://img1.mydrivers.com/img/20210701/S532ead99-3606-44c1-9cd4-83b6acdafd28.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>因为不带TPM芯片，所以很多消费级主板上会提供TPM的插槽，可以通过单独购买TPM 2.0模块来解决这个问题，不过也恰好因为Windows 11这次的需求，TPM 2.0模块近日价格疯涨。</p>
<p>TPM 2.0其实并不是高端平台专属的技术，现在很多新电脑都自带TPM 2.0，只是需要手动调校。</p>
<p>不过很多老电脑确实没有TPM 2.0，想要体验需要必须升级，这种捆绑销售的做法会令人反感在正常不过，为了所谓的数据安全给用户增加负担明显并不能让大部分人买账。</p>
<p>目前Windows 11只是刚刚起步，后续会怎么发展还不得而知，现在也有一些第三方安装方法可以跳过TPM 2.0检测，微软也在考虑放宽限制，有兴趣以及有条件的用户的可以尝试一下Windows 11，对比Windows 10、Windows 7会不会更令你满意呢？</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210701/501abd14ec8b47daa423cb55fc233a44.png" target="_blank"><img alt="无法运行Win11的原因已找到！一文了解TPM" h="450" src="https://img1.mydrivers.com/img/20210701/s_501abd14ec8b47daa423cb55fc233a44.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     <span>原文链接：<a href="https://diy.zol.com.cn/771/7715744.html">中关村在线</a></span>
<span>责任编辑：振亭</span>
</p>
        
</div>
            