
---
title: '在图灵机模型里发现了一个0day漏洞'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom'
author: 煎蛋
comments: false
date: Sun, 23 May 2021 15:29:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom'
---

<div>   
<blockquote><p>图灵机是所有计算机的原型，但这个漏洞并无现实影响</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom" referrerpolicy="no-referrer"><p>一位来自瑞典的计算机科学教授在最古老的通用图灵机中发现了一个 0day任意代码执行 漏洞——尽管教授承认 它"对现实世界毫无影响"。</p>
<p>瑞典斯德哥尔摩KTH皇家理工学院的教授Pontus Johnson在学术资料库ArXiv上发表的论文中，愉快地解释说，他的发现在现实世界中毫无价值，因为它专门针对 已故马文·明斯基设计的模拟通用图灵机(UTM)。明斯基是人工智能学科的共同创始人。</p>
<p>然而，漏洞真正的价值在于哲学上的启发：如果计算机的最基本原型，都存在漏洞，那么在设计过程中我们应该从哪里开始，实现安全功能？</p>
<p>"通用图灵机通常被认为是最简单、最抽象的计算机模型。"Johnson在论文中写道。通过利用明斯基规范UTM缺乏输入验证的特点，他能够欺骗它来运行他编写的程序。</p>
<p>明斯基规范描述了一种基于磁带的机器，它从模拟磁带上读取并执行非常简单的程序。磁带上的指令使模拟磁带读头在 "磁带" 上向左或向右移动，"磁带" 本身被理解成单行字母数字字符串。虽然用户可以在磁带的开始处进行输入，但在UTM模型中，他们不应该修改后面的程序。</p>
<p>UTM的安全性(如果可以这么说的话)来自一个单一数字——它告诉机器 "用户输入到此为止，此后的一切都可以用你刚刚读取的参数执行"。</p>
<p>Johnson的方法很简单，就是在用户输入栏中<strong>提前</strong>写下那个 "输入到此结束" 的字符，然后在它之后写下他自己的程序。UTM执行该程序并跳过预定程序。</p>
<p>与现代漏洞的相似之处是显而易见的：将复杂程度提高一些，这就具备了SQL注入漏洞的所有特征。</p>
<p>教授继续说："显然，马文·明斯基并不打算[创造]一个安全或脆弱的系统。然而，所发生的事情是[它就是]脆弱的。"</p>
<p>从哲学上讲，Johnson的漏洞(已被分配为CVE-2021-32471)为硬件和固件设计者提出了更深层次的问题。"有些人说，安全需要从一开始就建立起来；你不能以后再添加它。但在这种情况下，我所能想到的所有安全措施，都需要后来附加，你无法把安全性建在这台机器里。</p>
<p>"图灵机是所有计算机之母，所以你无法从一开始就建立安全。"</p>
<p>https://www.theregister.com/2021/05/11/turing_machine_0day_no_patch_available/</p>  
</div>
            