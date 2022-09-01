
---
title: '你的SSD还能用几年？教你查看硬盘健康状态'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220901/Sdcf4b45e-7008-4031-ae19-f340f349ea3e.png'
author: 快科技（原驱动之家）
comments: false
date: Thu, 01 Sep 2022 12:25:26 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220901/Sdcf4b45e-7008-4031-ae19-f340f349ea3e.png'
---

<div>   
<p>最近在贴吧和一些相关论坛中，有关固态硬盘“0E”的讨论成为热门话题，讨论指向某些型号的NVMe固态硬盘正频繁出现S.M.A.R.T.信息中“0E”与“03”两项的异常值，而这两个现象意味着这类NVM存储介质正在出现非正常寿命损耗范畴内的“坏块”，继续使用将对用户存储数据的安全和完整带来很大影响。</p>
<p>要想知道如何查看0E与03，我们先要对S.M.A.R.T.这项固态硬盘的“自我检测分析与报告技术”有所了解。</p>
<p><strong>简单来说，这项技术可使硬盘测量自身的健康指标，</strong>并将数值向操作系统与用户的监控软件开放，不过每个硬盘生产商也有权决定哪些指标需要测量，以及为其设定各不相同的安全阈值。</p>
<p>作为一项行业标准，S.M.A.R.T.已经成为多种硬盘产品的标配，其各项健康指标所使用的ID代码，也随硬盘种类的不同而存在各自的定义。</p>
<p>我们要讨论的0E与03就是NVMe固态硬盘S.M.A.R.T.信息中的“媒体与数据完整性错误计数”与“可用备用空间”，可以使用我们熟悉的CrystalDiskMark来查看它们，正如下图所示，这是笔者将一块替换下来的OEM固态通过硬盘盒连接至电脑后，软件显示的结果。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220901/dcf4b45e-7008-4031-ae19-f340f349ea3e.png" target="_blank"><img alt="你的SSD还能用几年？教你查看硬盘健康状态" h="616" src="https://img1.mydrivers.com/img/20220901/Sdcf4b45e-7008-4031-ae19-f340f349ea3e.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>可以看到底下的信息栏中第三行与倒数第二行分别是我们要查看的0E与03，但它们显示的值包含一长串0、其他数字和字母，这是因为S.M.A.R.T.信息目前以十六进制显示，我们可以在软件中设置以十进制显示，此外也可以设置属性名称以英文显示，方便我们查找相关资料。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220901/aa00977d-544d-4d16-9ce7-bd5ca55b30cf.png" target="_blank"><img alt="你的SSD还能用几年？教你查看硬盘健康状态" h="547" src="https://img1.mydrivers.com/img/20220901/Saa00977d-544d-4d16-9ce7-bd5ca55b30cf.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>十进制显示方式的设置在顶部菜单栏中的功能-高级设置-原始值-10[DEC]，随后我们看到的就是如下图更易读的十进制信息。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220901/180f51b2-49db-4a28-bc23-36c5f98b52aa.png" target="_blank"><img alt="你的SSD还能用几年？教你查看硬盘健康状态" h="616" src="https://img1.mydrivers.com/img/20220901/S180f51b2-49db-4a28-bc23-36c5f98b52aa.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>可以看到，这块固态硬盘的03与0E值分别为100(百分比)和0(次数)，处在正常状态，长期读写使用并未使其产生坏块等现象，我们也可以查看其他信息，包括严重警告标志的计数、已用寿命百分比(也会在左上角的健康状态中显示)、不安全关机计数等等。</p>
<p>更值得担忧的是当前网友和用户曝光出的众多0E开始计数的情况，固态硬盘的坏块是不可逆的，并且从存储原理上来说，坏块必然会影响存储数据的完整性，导致文件损坏或丢失，正如0E这个ID的具体意义：主控检测到未恢复的数据完整性错误的次数。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220901/dd9e33dd-8cb8-4e68-9c29-26525357f652.png" target="_blank"><img alt="你的SSD还能用几年？教你查看硬盘健康状态" h="444" src="https://img1.mydrivers.com/img/20220901/Sdd9e33dd-8cb8-4e68-9c29-26525357f652.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>当有纠错引擎无法校正的ECC、CRC校验失败或者LBA标签不匹配错误发生时，0E数值会增加，只要它不为0，就代表固态硬盘已经不再处于稳定的工作状态。</p>
<p>同时，<span style="color:#ff0000;"><strong>0E的增加也伴随着03可用备用空间的减少，如果这个百分比数值降低到0，就意味着可用于替换坏块的闪存备用块已经用尽。</strong></span></p>
<p>因此难怪有人认为0E是NVMe固态硬盘的“绝症”，因为它既代表了非正常使用寿命的损耗，也具有不可逆转性，0E的数值大小没有程度上的区别，因为数据损坏对用户而言即使是仅有一次也可能带来不可预料的后果。</p>
<p>读者们可以根据上文提供的步骤来了解自己的NVMe固态硬盘健康状况，如果真的出现了0E计数，笔者的建议是不再将其作为系统盘等主盘使用，尽快备份、转移数据，并尽快寻求产品售后。</p>
<p>对用户而言固态硬盘的坏块不是一个能通过维修解决的问题，保证数据的完整，同时获得相应退换货服务就是最好的结果。</p>
<p>0E计数以及其代表的坏块现象，成因目前还存在多种推测，但贴吧等论坛网友归纳出的初步规律，包含某些型号存储颗粒以及部分版本的硬盘固件有更高产生此类现象的概率，想要深入了解的朋友可以自行查找。</p>

            
 <div style="overflow: hidden;font-size:14px;padding-top:30px;border-bottom:1px solid #eee;">
             
          <p class="url"><span style="color:#666">责任编辑：宪瑞</span></p>
        </div>
     
        
</div>
            