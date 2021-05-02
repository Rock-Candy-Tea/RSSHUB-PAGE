
---
title: '最新曝光的iPhone大漏洞：传文件会泄露个人隐私 2年多了苹果知而不改'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210502/s_866543f7bb494a6689781cc420cbc99f.png'
author: 快科技（原驱动之家）
comments: false
date: Sun, 02 May 2021 15:17:58 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210502/s_866543f7bb494a6689781cc420cbc99f.png'
---

<div>   
<p>来自iPhone用户善意的提醒总是让人感到温暖：</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210502/866543f7bb494a6689781cc420cbc99f.png" target="_blank"><img alt="最新曝光的iPhone大漏洞：传文件会泄露个人隐私 2年多了苹果知而不改" h="349" src="https://img1.mydrivers.com/img/20210502/s_866543f7bb494a6689781cc420cbc99f.png" style="border: black 1px solid;" w="221" referrerpolicy="no-referrer"></a></p>
<p>于是我反手就来一个“感谢”：</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210502/d7b8f9a6c75c4f3b8b7dd8d77b83a2ac.png" target="_blank"><img alt="最新曝光的iPhone大漏洞：传文件会泄露个人隐私 2年多了苹果知而不改" h="398" src="https://img1.mydrivers.com/img/20210502/s_d7b8f9a6c75c4f3b8b7dd8d77b83a2ac.png" style="border: black 1px solid;" w="229" referrerpolicy="no-referrer"></a></p>
<p>iPhone的AirDrop用完不关，不止是被骚扰这一点小事，黑客还可以在几毫秒内截获个人信息。</p>
<p>基本相当于你把自己的手机号、邮箱等等联系方式公之于众了。</p>
<p>而且，这个bug苹果早就知道，却一直不修复。</p>
<p><strong>根本来不及闪，信息就泄露了</strong></p>
<p>怎么回事？</p>
<p>达姆施塔特工业大学的研究人员对漏洞进行了深入研究，他们的结论是：</p>
<p>苹果AirDrop存在双向漏洞，无论接受还是发送，只要打开，黑客就能在几毫秒间破解用户的邮箱、电话号码等等信息。</p>
<p>而被黑客截获的个人信息，可能被用作精准网络钓鱼攻击、诈骗等等，最简单的方法，是直接转卖个人信息获利。</p>
<p>AirDrop，国内用户更熟悉的名字是隔空投送，通过蓝牙与wifi来进行传输。其中，蓝牙“握手”，Wi-Fi“传输”。</p>
<p>整个传输过程，并不需要公共网络连接的参与。</p>
<p>但是问题就出在蓝牙“握手阶段”。</p>
<p>传输确认阶段，为了确定可能的发件人的设备是否应该与附近的其他设备连接，AirDrop会广播本机蓝牙信号，其中包含发件人的电话号码和电子邮件地址的部分加密哈希值。</p>
<p>如果有哈希值与接收设备通讯录中的某人信息相匹配，这两台设备将通过Wi-Fi进行相互验证握手。</p>
<p style="text-align: center"><img alt="最新曝光的iPhone大漏洞：传文件会泄露个人隐私 2年多了苹果知而不改" h="372" src="https://img1.mydrivers.com/img/20210502/60f17a4c-edbd-409b-9351-46e9c1700873.jpg" style="border: black 1px solid" w="595" referrerpolicy="no-referrer"></p>
<p>当然，如果接受者设置为从任何设备接收，则可以跳过通讯录验证。</p>
<p>在握手过程中，设备会交换所有者的电话号码和电子邮件地址的完整SHA-256哈希值。</p>
<p>本来，从哈希值中不能直接转录出生成它们的原信息，但根据明文中的熵（entropy）或随机值的数量，是有可能被计算出来的。</p>
<p>所以，黑客理论上可以通过执行 “暴力攻击 “来做到这一点，即抛出大量的测试值，“碰”出正确的信息。</p>
<p>关键点来了，一个电话号码，或是一个电子邮件地址中，信息熵小到微不足道。</p>
<p>即使是包含世界上所有可能的电话号码的数据库。在其中查找一个哈希值也只需要几毫秒的时间。</p>
<p>就是这样，根本来不及闪，信息就泄露出去了。</p>
<p><strong>黑客“守株待兔”</strong></p>
<p>最简单的方法，黑客只需监视附近其他设备发送的发现请求，不需要任何先验信息。</p>
<p>举例来说，在公共场合安一个蓝牙“窃听器”就行了。</p>
<p>第二种方法是反向的。</p>
<p>攻击者打开共享菜单，看看是否有附近的设备回应自己的握手请求信息。</p>
<p>但这种技术没有第一种方法适用面广，因为它只在攻击者的信息已经在接收者的地址簿中时才起作用。</p>
<p>但是，来自“熟人”的攻击同样可怕。</p>
<p>例如，公司老板可以用它来获得任何员工的非工作电话号码或电子邮件地址….</p>
<p><strong>两年了，苹果充耳不闻</strong></p>
<p>苹果知道吗？</p>
<p>当然知道。而且，两年前就知道了。</p>
<p>不光知道，发现漏洞的达姆施塔特工业大学小组，还专门开发出了漏洞补丁PrivateDrop，允许双方在不暴露哈希值的情况下互相握手发现。</p>
<p style="text-align: center"><img alt="最新曝光的iPhone大漏洞：传文件会泄露个人隐私 2年多了苹果知而不改" h="400" src="https://img1.mydrivers.com/img/20210502/31d34644-bcd7-464c-ab36-f9f886e3e3e3.jpg" style="border: black 1px solid" w="400" referrerpolicy="no-referrer"></p>
<p>在2019年报告漏洞时，顺手一并提交了补丁。</p>
<p>但是两年过去了，石沉大海。</p>
<p>苹果官方从没回应过研究人员是否采用他们的方案，而且，漏洞也一直没有修复。</p>
<p>现成答案都懒得抄…</p>
<p>所以直到今天，只要有用户使用隔空投送，就存在泄露个人信息的风险。</p>
<p style="text-align: center"><img alt="最新曝光的iPhone大漏洞：传文件会泄露个人隐私 2年多了苹果知而不改" h="110" src="https://img1.mydrivers.com/img/20210502/25e4aa80-621f-41ed-8f87-7888dbea8025.jpg" style="border: black 1px solid" w="268" referrerpolicy="no-referrer"></p>
<p>目前，防止泄漏的唯一方法是在系统设置菜单中把AirDrop设置为 “no one”。</p>
<p>iOS 14.5推出本来以安全性著称，但如今却被曝严重漏洞持续两年“知而不改”，而且影响全球15亿用户….</p>
<p>对了，还要提醒一下，不光是iPhone上的iOS，macOS、iPadOS，所有有“隔空投送”功能的苹果设备，都面临威胁。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210502/73da5289a8ef494d84c772d547b7c234.jpg" target="_blank"><img alt="最新曝光的iPhone大漏洞：传文件会泄露个人隐私 2年多了苹果知而不改" h="450" src="https://img1.mydrivers.com/img/20210502/s_73da5289a8ef494d84c772d547b7c234.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/pingguo.htm"><i>#</i>苹果</a><a href="https://news.mydrivers.com/tag/iphoneshouji.htm"><i>#</i>iPhone手机</a><a href="https://news.mydrivers.com/tag/loudong.htm"><i>#</i>漏洞</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/CtLaoWdsoTwBwqw9M-_Kag">量子位</a></span>
<span>责任编辑：陈驰</span>
</p>
        
</div>
            