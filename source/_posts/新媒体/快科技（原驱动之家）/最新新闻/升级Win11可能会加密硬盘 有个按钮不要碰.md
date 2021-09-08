
---
title: '升级Win11可能会加密硬盘 有个按钮不要碰'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210908/S00bd4fc9-3a5e-41ee-b144-d37ed2a461b1.jpg'
author: 快科技（原驱动之家）
comments: false
date: Wed, 08 Sep 2021 20:28:02 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210908/S00bd4fc9-3a5e-41ee-b144-d37ed2a461b1.jpg'
---

<div>   
<p>Windows 11正式版将在10月5日开始推送，这意味着Windows 11操作系统终于正式发布了。</p>
<p>对于之前的Windows 11升级要求当中，大家可能最难以理解的一项就是TPM 2.0，其实简单来说就是一种硬件级别的加密技术，本质上应该由主板上一个专门的芯片来做支持，但大多数是依靠CPU来模拟就可以，之前很多想要尝鲜新系统的同学或多或少都在这一项上卡了一下。</p>
<p>不过随着大家逐渐关注，这个功能也被很多主板厂商默认启用了，比如前段时间刚刚测试的一款新品主板，内部就设置了默认开启TPM技术的选项，在之前这个选项是默认关闭状态。</p>
<p>并且为了防止大家在更换CPU的时候出现加密问题，主板还默认开启了更换CPU将自动重置TPM加密的设置项。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210908/00bd4fc9-3a5e-41ee-b144-d37ed2a461b1.jpg" target="_blank"><img alt="升级Win11可能会加密硬盘 有个按钮不要碰" h="450" src="https://img1.mydrivers.com/img/20210908/S00bd4fc9-3a5e-41ee-b144-d37ed2a461b1.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
主板上的TPM开关</p>
<p>即使是这样，狼叫兽认为还是有一些隐患。<strong>开启TPM功能之后，Windows之中的一个名为Bitlocker的功能就变成了可用状态，这个功能本意是给一些对信息安全有需求的商用客户加密硬盘之中所有文件用的，但对于一些普通用户来说有时会变成噩梦。</strong></p>
<p>有些电脑，尤其是对Windows兼容性非常好的笔记本产品，<strong>会有默认开启Bitlocker或是提醒用户开启Bitlocker的策略</strong>，在不经意的一次系统更新或者手动操作之后，你的硬盘就会被Bitlocker全面加密，如果正常使用其实没啥影响，你的文件依然可以正常读写，并且由于加密，电脑内的文件也变得更加安全，难以被盗取。</p>
<p>但如果某一天电脑系统出现故障，这种故障常常发生在某些系统更新、某些软件的所谓“瘦身”“垃圾清理”“危险隔离”“漏洞修复”等操作之后。</p>
<p>当你无法正常进入系统的时候，如果是往常，我们只需要借助比如PE盘这种临时性的mini系统进入电脑，将硬盘之中的数据拷贝出来，然后重新安装系统即可。</p>
<p>但如果你不小心开启了Bitlocker，这时候就要先对硬盘进行解密，而密码大多数不小心开启Bitlocker加密的用户都不知道在哪里，这个密码通常会在加密的时候让用户选择保存在一个外置U盘当中、你的Microsoft账户当中，或是打印出来一张纸上。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210908/7e290dfa-1aec-454d-9dc6-3a7446d1c84e.jpg" target="_blank"><img alt="升级Win11可能会加密硬盘 有个按钮不要碰" h="468" src="https://img1.mydrivers.com/img/20210908/S7e290dfa-1aec-454d-9dc6-3a7446d1c84e.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
加密开始的时候首先要保存秘钥</p>
<p>对于普通的用户来说，可能根本不知道自己电脑上是否登陆了自己的Microsoft账户，更不用提恢复秘钥保存在哪里了。因为Bitlocker加密级别比较高，普通人基本上无法破解，电脑当中的文件大概率无法找回了。</p>
<p>之前大多数主板都会在BIOS之中默认禁用TPM我想也是因为这种原因吧，毕竟其实普通大众的电脑之中也没有什么特别重要的文件，高安全性反不如高便捷性更重要，TPM这种高大上的玩意还是交给真正有需求的人来用吧。</p>
<p><strong>下面教给大家简单的方法来未雨绸缪，排查一下自己的电脑是否开启了Bitlocker加密。</strong></p>
<p>一、如果你是Windows 10系统，打开路径：开始-设置-更新和安全-设备加密，看一下设备加密是否和下图一样是已关闭状态，记得千万不要点那个打开按钮。</p>
<p>如果是已加密的状态，那就点关闭按钮，进入解密的流程，一般来说，如果你没有特别操作的话，在系统正常运行的时候是可以直接解密的，解密过程之中硬盘会工作在满负荷状态，请大家尽量不要进行其他操作，也千万不要关闭电源，最好将电脑的自动休眠关闭，如果不知道怎么关闭那就隔几分钟动一下鼠标，直到解密完成。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210908/bbabd580-3d90-476a-b891-c01a4b771ab0.jpg" target="_blank"><img alt="升级Win11可能会加密硬盘 有个按钮不要碰" h="465" src="https://img1.mydrivers.com/img/20210908/Sbbabd580-3d90-476a-b891-c01a4b771ab0.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
设备加密</p>
<p>大家可能看到右侧有一个相关设置：Bitlocker设置，这里和设备加密的功能其实是同一个，很多电脑在你点击设备加密当中的选项之后会自动跳转到Bitlocker当中。</p>
<p>二、Windows 11操作系统或者没找到设备加密选项的话，可以直接在设置的搜索栏里输入Bitlocker进行搜索。可以直接进入到管理Bitlocker的页面当中。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210908/cebc78f1-8c01-4654-953a-7e2777b470a1.jpg" target="_blank"><img alt="升级Win11可能会加密硬盘 有个按钮不要碰" h="393" src="https://img1.mydrivers.com/img/20210908/Scebc78f1-8c01-4654-953a-7e2777b470a1.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
直接搜索bitlocker</p>
<p>进入到Bitlocker的管理页面之后就可以清楚地看到你电脑中的每个磁盘的加密状态，比如下图这里都显示的“已关闭”状态，这样就表示磁盘没有被加密。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210908/5dc6de70-6b18-4614-bc8c-8bd40e12f550.jpg" target="_blank"><img alt="升级Win11可能会加密硬盘 有个按钮不要碰" h="358" src="https://img1.mydrivers.com/img/20210908/S5dc6de70-6b18-4614-bc8c-8bd40e12f550.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
Bitlocker设置</p>
<p>如果你的页面和我的有区别，比如显示的是Bitlocker已开启，那么上图“启用Bitlocker”按钮就将会同步变更为“关闭bitlocker”的按钮，点击他等待解密完成即可。</p>
<p>需要注意的是，如果你的电脑已经处在加密或者解密过程中了，这个操作是无法被中止的，只有等加密或者解密完成之后才能进行操作。</p>
<p>如果你的磁盘已经被Bitlocker加密，那么尝试以下操作：</p>
<p>一、尽可能寻找关联的Microsoft账户或者秘钥文件，或尝试曾用过的密码对磁盘进行解密。</p>
<p>二、如果实在找不到密码，那就尝试用U盘等移动存储设备把重要的文件拷贝出来，然后完全清空硬盘重新安装操作系统。如果U盘不能直接拷贝，可以考虑通过QQ等聊天工具传输重要文件。</p>
<p>三、如果不能找到密码也无法拷贝到外部存储设备当中，只能采用最终止损方案了，用被加密的电脑打开重要文档，一笔一划对着抄下来吧。</p>
<p>希望大家在电子设备中进行每一步操作之前都要仔细看一下提示框里的信息，如果不知道或者不清楚这个功能是干什么的，请尽量选择关闭，不要胡乱点击确认或取消。</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windows_10.htm"><i>#</i>Windows 10</a><a href="https://news.mydrivers.com/tag/bitlocker.htm"><i>#</i>BitLocker</a></p>
<p class="url">
     <span>原文链接：<a href="https://diy.zol.com.cn/776/7760055.html">中关村在线</a></span>
<span>责任编辑：万南</span>
</p>
        
</div>
            