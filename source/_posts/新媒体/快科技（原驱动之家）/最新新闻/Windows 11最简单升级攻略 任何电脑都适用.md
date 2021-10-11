
---
title: 'Windows 11最简单升级攻略 任何电脑都适用'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211011/Sbdc118ff-d3f7-4d87-a7ad-9a421959324c.jpg'
author: 快科技（原驱动之家）
comments: false
date: Mon, 11 Oct 2021 06:29:07 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211011/Sbdc118ff-d3f7-4d87-a7ad-9a421959324c.jpg'
---

<div>   
<p>最近，很多朋友在升级Windows 11系统时都遇到了下面这样的问题。</p>
<p>不瞒大家说，笔者的电脑也是因为没有开启安全启动和TPM 2.0而遭到了限制。虽然开启这两项功能的操作并不复杂，但是因为涉及到要进入BIOS进行设置，所以对于一些不太懂电脑的朋友来说还是有一些上手难度的。</p>
<p>那么能不能绕过这两项限制直接升级Windows 11系统呢？当然能。不过网上很多方法甚至比去BIOS开启这两项功能还难，有些甚至还要去Github下载第三方软件，操作起来着实繁琐了一些。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211011/bdc118ff-d3f7-4d87-a7ad-9a421959324c.jpg" style="text-align: center;" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="600" src="https://img1.mydrivers.com/img/20211011/Sbdc118ff-d3f7-4d87-a7ad-9a421959324c.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>今天给大家带来的这个升级Windows 11系统的方法，适用于任何未通过微软官方检测的电脑，而且操作简单，男女老少都可以操作。</p>
<p>下面我们就来看看如何用最简单的方法绕过检测直接安装Windows 11。</p>
<p>首先还是进入Windows 11系统下载页面：<strong>【</strong><a class="f14_link" href="https://www.microsoft.com/zh-cn/software-download/windows11" target="_blank"><strong>点此进入</strong></a><strong>】</strong>，进入之后会看到下面这张图，点选红框里的下载Windows 11磁盘映像，将Windows 11系统的镜像文件下载下来。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/07aa2607-1fd5-4536-bd97-0b0f59600574.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="583" src="https://img1.mydrivers.com/img/20211011/S07aa2607-1fd5-4536-bd97-0b0f59600574.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>下载完Windows 11的ISO镜像文件之后，鼠标右键点击，并将其解压缩到任意位置。笔者为了方便操作，直接将它解压缩到了桌面上。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/98ff32a4-9c48-4d79-b8c2-1f75d96a6e51.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="426" src="https://img1.mydrivers.com/img/20211011/S98ff32a4-9c48-4d79-b8c2-1f75d96a6e51.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>之后三步是最关键的地方，大家拿出小本本记好了：</strong></p>
<p>首先在Windows 11安装文件夹下的<strong>sources文件夹</strong>里找到“<strong>appraiserres.dll</strong>”这个文件，注意这里有很多相似的文件名，一定别找错了。</p>
<p>其次，<strong>将其文件名复制下来</strong>，<strong>之后将这个文件彻底删除。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/1cddddec-1a30-4e7b-bc46-973b6c5fd82b.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="392" src="https://img1.mydrivers.com/img/20211011/S1cddddec-1a30-4e7b-bc46-973b6c5fd82b.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>删除之后新建一个文件夹，</strong>注意是文件夹，不是别的类型的文件，然后<strong>将删除掉的那个文件的名称连带.dll后缀一起复制成新文件夹的名称</strong>，如下：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/83c0fbcc-5768-46fb-bac6-1b41a74a9368.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="383" src="https://img1.mydrivers.com/img/20211011/S83c0fbcc-5768-46fb-bac6-1b41a74a9368.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>做完上面三步之后，退回到Windows 11安装文件夹的根目录，找到最下面的setup.exe，并使用鼠标左键双击。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/6c5cf9f5-082f-4261-9816-2377e81a6db5.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="335" src="https://img1.mydrivers.com/img/20211011/S6c5cf9f5-082f-4261-9816-2377e81a6db5.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>为了避免安装过程中出现问题，笔者建议大家把无线和有线网都断掉。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/519d9b80-0035-4f82-b968-c44c75554c64.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="257" src="https://img1.mydrivers.com/img/20211011/S519d9b80-0035-4f82-b968-c44c75554c64.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>双击setup.exe之后，就可以看到下面这个界面了，直接点选右下角的“下一页”按钮。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/73cd40d7-52f0-46d1-9ef2-38764bd284d4.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="521" src="https://img1.mydrivers.com/img/20211011/S73cd40d7-52f0-46d1-9ef2-38764bd284d4.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>之后的步骤不再赘述，都点右下角的下一页按钮即可：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/e1ae1c34-873e-45aa-bde3-bb2b9cd46dfe.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="519" src="https://img1.mydrivers.com/img/20211011/Se1ae1c34-873e-45aa-bde3-bb2b9cd46dfe.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>接下来这一点比较重要，大家要注意：</strong></p>
<p>如果遇到下图所示让你输入产品密钥，不用着急。打开任意搜索引擎，如百度、bing等，搜索关键词“Windows 10密钥”，之后随便找一个靠谱的网页打开，将其他网友分享的密钥复制过来输入到这一栏中。当下方状态显示为“你的产品密钥有效……”即可继续进行下一步。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/7a2cc9cb-f9b7-4cdf-9b84-1ec0fc14ce10.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="518" src="https://img1.mydrivers.com/img/20211011/S7a2cc9cb-f9b7-4cdf-9b84-1ec0fc14ce10.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>后面步骤同样不再赘述，各种下一步就好了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/41f20c5a-8ffc-4590-ae0d-b1a46d1c93b8.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="518" src="https://img1.mydrivers.com/img/20211011/S41f20c5a-8ffc-4590-ae0d-b1a46d1c93b8.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>看到下面这个页面的时候就已经大功告成了，最后直接点击“安装”按钮。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/4317f0be-fe50-4778-8e13-35b34a6329c3.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="514" src="https://img1.mydrivers.com/img/20211011/S4317f0be-fe50-4778-8e13-35b34a6329c3.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>接下来系统就会进入自动安装过程，耐心等待系统安装完成。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/8ec812ee-685c-4bad-b488-77fb1c5e87fa.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="338" src="https://img1.mydrivers.com/img/20211011/S8ec812ee-685c-4bad-b488-77fb1c5e87fa.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>笔者成功将不符合条件的电脑升级到了Windows 11系统，不过桌面原本规则摆放的图标都被打乱了，其它一切正常。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211011/bfe324c7-ba97-43c7-b3bb-85b24142d06c.jpg" target="_blank"><img alt="Windows 11最简单升级攻略 任何电脑都适用" h="338" src="https://img1.mydrivers.com/img/20211011/Sbfe324c7-ba97-43c7-b3bb-85b24142d06c.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>如果你的电脑符合升级条件，就不需要用这个方法，可以参考笔者之前写的《<a class="f14_link" href="https://news.mydrivers.com/1/787/787435.htm" target="_blank">保姆级Windows 11升级教程三分钟包学会</a>》一文进行系统升级。</p>
<p>总体来说，Windows 11系统与Windows 10系统相比除了桌面UI，Icon图标有所变化之外，底层操作逻辑、交互体验没有太大变化。不过Windows 11系统在安装速度方面确实比以往的系统快了很多，笔者整个升级过程不到20分钟，所以有兴趣的朋友都可以直接升级Windows 11系统，目前来看绝大多数日常应用都没有兼容性问题。</p>
<p>此外在升级Windows 11系统之后，第一件要做的事笔者写在这篇文章里了：《<a class="f14_link" href="https://news.mydrivers.com/1/787/787511.htm" target="_blank">性能最高可提升28%！Windows 11电脑必做这件事</a>》，大家可以参考。</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     <span>原文链接：<a href="https://nb.zol.com.cn/778/7781122.html">中关村在线</a></span>
<span>责任编辑：万南</span>
</p>
        
</div>
            