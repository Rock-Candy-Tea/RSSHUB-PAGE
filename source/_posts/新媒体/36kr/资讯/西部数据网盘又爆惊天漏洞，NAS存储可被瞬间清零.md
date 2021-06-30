
---
title: '西部数据网盘又爆惊天漏洞，NAS存储可被瞬间清零'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210630/v2_ab15e8450bb34aa2957b04bbf79b61af_img_000'
author: 36kr
comments: false
date: Wed, 30 Jun 2021 10:29:22 GMT
thumbnail: 'https://img.36krcdn.com/20210630/v2_ab15e8450bb34aa2957b04bbf79b61af_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/amIfVQR9VK2hR4jqr7fNBA">“新智元”（ID:AI_era）</a>，编辑：Emil、小匀，36氪经授权发布。</p> 
<blockquote> 
 <p>【导读】一项调查显示，上周发生在西部数据 My Book Live 上的「大规模数据删除」事件不仅涉及一个漏洞，还涉及第二个！该漏洞甚至允许黑客在没有密码的情况下远程执行恢复出厂设置。</p> 
</blockquote> 
<p>如今影像功能成了新款智能手机宣传的主要噱头。</p> 
<p>1亿像素、4k甚至是8k视频拍摄屡见不鲜。但是在这背后就是数据的爆炸：一张一亿像素的照片最高可能达到20MB，一分钟的8k视频需要吞掉2GB的存储空间。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_ab15e8450bb34aa2957b04bbf79b61af_img_000" data-img-size-val="548,308" referrerpolicy="no-referrer"></p> 
<p>看来想要把手机当生产力工具来使用，512GB的存储空间都有点捉襟见肘了。</p> 
<p>想要使用不限速的大容量网盘服务？先把年费付一下。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_76c7d77d0c3c4598925a984da35c9118_img_000" data-img-size-val="548,123" referrerpolicy="no-referrer"></p> 
<p>如果不甘心被绑架，那自己组建一个不限速的简易的大容量网络存储设备（NAS），绝对是个好主意。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_a7f33a0b0b2d40af95a78de4271f5aa5_img_000" data-img-size-val="447,631" referrerpolicy="no-referrer"></p> 
<p>如今越来越多的硬盘厂商提供了类似的产品，只要把这套设备连接自家的网络，就可以随时随地访问以及备份数据，且速度上限就是家里的网络带宽。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_cd85ed9937ab49c6a2f11649a652838b_img_000" data-img-size-val="548,308" referrerpolicy="no-referrer"></p> 
<p>但是把重要文件备份在自己的NAS上靠谱吗？</p> 
<h2 label="一级标题" style>我的NAS突然空空如也？</h2> 
<p>上周，国外网友发帖：我在西部数据My Book Live NAS里的数据，一夜之间都没了！</p> 
<p>并且通过客户端登陆管理页面，还会提示你密码无效。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_6842afdc98d6473cbe34a47de43f3bc2_img_000" data-img-size-val="548,256" referrerpolicy="no-referrer"></p> 
<p>硬盘就这样罢工了！随之消失的，还有你手机拍摄的珍贵照片和视频，还有珍藏的电影。</p> 
<p>如果你恰巧在手机上删除了这些文件来清理空间，并且没有第二个备份的话，这就意味着这些珍贵数据你永远找不回来了。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_f649b8ed3b9342a99bac0917daf0d0ac_img_000" data-img-size-val="548,548" referrerpolicy="no-referrer"></p> 
<p>有用户调取了设备日志，发现设备在无人监管的情况下自动运行了一个脚本，从而擦除了所有存储内容，恢复成了出厂设置：</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_53ee157b5cc24395b550e7ed710d745f_img_000" data-img-size-val="548,185" referrerpolicy="no-referrer"></p> 
<p>西部数据当时也是一头雾水，于是给出了一个最简单的解决方案：拔网线。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_e668ffe9ae6547f3a071802b4e967b9f_img_000" data-img-size-val="548,202" referrerpolicy="no-referrer"></p> 
<p>网盘立刻变移动硬盘。</p> 
<p>根据官方声明，涉及的NAS设备已经停产，并且在2015年停止了固件更新。所以大概率是由于某个漏洞所致。而新的My Cloud 5以及My Cloud Home系列设备由于采用了新的安全架构，则不会受此影响。</p> 
<p>西部数据这样抛弃老用户的行为着实有点上不了台面。</p> 
<p>如今，这次事件破案了。</p> 
<h2 label="一级标题" style>居然还有另一个Bug</h2> 
<p>最近的调查找到了此次事件的原因：My Book Live系列固件的漏洞不仅可以让黑客获得root访问权限，而且另外一个漏洞居然允许黑客在远程可以直接绕过密码，直接让NAS设备恢复出厂设置！</p> 
<p>这个漏洞存在于一个名为 system_factory_restore 的文件中。它包含一个执行重置的 PHP 脚本，允许用户恢复所有默认配置并擦除存储在设备上的所有数据。</p> 
<p>通常，恢复出厂设置要求提出请求的人提供用户密码。</p> 
<p>但是，如下面的脚本所示，西部数据开发人员创建了五行代码来对重置命令进行密码保护。由于未知原因，身份验证检查被取消，或者用开发人员的话来说，它被注释掉了，如每行开头的双 / 字符所示。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_69daae106ff84f778c6591bcc9c598b4_img_000" data-img-size-val="548,120" referrerpolicy="no-referrer"></p> 
<p>「这就像他们故意启用了绕过的方法。」一位网络安全专家说。</p> 
<p>要利用这个漏洞，攻击者必须知道触发系统重置的XML请求格式。这不像用GET请求打击一个随机的URL那么容易，但也相差不远。</p> 
<h2 label="一级标题" style>这个漏洞目前无解</h2> 
<p>这一发现提出了一个令人困惑的问题：如果黑客已经通过利用CVE-2018-18472获得了完全的root权限，那么他们有什么必要利用这第二个安全漏洞？</p> 
<p>一切都很未知。</p> 
<p>Abdine提出了一个合理的理论——一个黑客首先利用了CVE-2018-18472，一个竞争对手的黑客后来利用了另一个漏洞，试图夺取对那些已经被入侵的设备的控制权。</p> 
<p>利用CVE-2018-18472的攻击者利用其提供的代码执行能力，修改了My Book Live堆栈中一个名为language_configuration.php的文件，这就是该漏洞所在。根据一个恢复的文件，该修改添加了以下几行。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_07691e2f202c41a4aa0fb8b79fc9aafc_img_000" data-img-size-val="606,248" referrerpolicy="no-referrer"></p> 
<p>到目前为止，还除了拔网线以外，还没有有效的破解方法。</p> 
<p>此次事件严重打击了用户对于西部数据设备的信心，相信那些数据被清零的用户以后再也不会购买任何一款西部数据的产品了。</p> 
<p>不过专家建议可以用新的 My Cloud Live 设备取代西部数据的 My Book Live 产品，就像之前说的，它具备了新的安全架构，不包含这次事件中的任何一个漏洞。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_d80a23f65dce459393d1cc41485a0d88_img_000" data-img-size-val="548,544" referrerpolicy="no-referrer"></p> 
<p>所以，你还会买吗？</p> 
<p>参考资料：</p> 
<p>https://arstechnica.com/gadgets/2021/06/hackers-exploited-0-day-not-2018-bug-to-mass-wipe-my-book-live-devices/</p>  
</div>
            