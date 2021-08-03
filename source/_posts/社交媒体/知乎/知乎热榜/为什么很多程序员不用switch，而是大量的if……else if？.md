
---
title: '为什么很多程序员不用switch，而是大量的if……else if？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic3.zhimg.com/v2-21b5720ca7b4d41b87d7e903a16db2c8_1440w.jpg'
author: 知乎
comments: false
date: Tue, 03 Aug 2021 12:47:19 GMT
thumbnail: 'https://pic3.zhimg.com/v2-21b5720ca7b4d41b87d7e903a16db2c8_1440w.jpg'
---

<div>   
编程指北的回答<br><br><p>曾经接手过一份代码，遇到过一个三十几个if else套if else的模块。</p><figure data-size="normal"><img src="https://pic3.zhimg.com/v2-21b5720ca7b4d41b87d7e903a16db2c8_1440w.jpg" data-caption data-size="normal" data-rawwidth="1302" data-rawheight="938" data-default-watermark-src="https://pic3.zhimg.com/v2-f6564eda3f0569c9cfc3dca8e4248c36_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic3.zhimg.com/v2-21b5720ca7b4d41b87d7e903a16db2c8_r.jpg" referrerpolicy="no-referrer"></figure><p><br>心理骂骂咧咧谁他喵写的这玩意，然后开始review历史。<br></p><p>大致情况是这样的：第一个程序员写下这段代码时，只有两个if else；后来开始逐渐加需求，先是一个、两个，随后量变引起质变，于是逻辑分支快速扩张。<br>这个时候已经没有人愿意去重构成switch或是其他什么设计模式了，毕竟复杂度摆在那里，万一崩了还得背锅。<br>三四个程序员接手这段代码之后，就变成我现在这种局面了。<br><br></p><p>第一个程序员绝对没有料到这么简单的逻辑在之后会变成这么复杂的模块，甚至在增添第一第二条else时，也只是很随意的加上。</p><p>所以我觉得，这个锅绝对是是甲方的，让***的随便改需求。<br>这么一想心里就好受多了，编程嘛，最重要的是要看的开。<br>于是我又增加了两条else，测试，提交，下班。<br>有时候真的不是我们不想写好代码，是不能写好代码。写着写着需求砍了、需求变了，什么设计模式都不顶用，最终还是怎样快怎样方便怎样来，因为根本没人知道这段代码还能不能活的过下一段需求变动。<br>有的人肯定要说怎么不订合同。合同肯定是有的，但是明明白纸黑字写的合同，该改还是得改，毕竟你要是不同意甲方那些“微小的变动”，以后还做不做了？！金主真能去得罪？<br><br><br><br></p><p>还是要学会得过且过，跟什么过不去也不能跟自己过不去，糟糕的代码忍一忍就完了:代码能跑、头发不少，对我们这些打工的人而言比什么都重要。<br>现实工作绝不是课本中的理想状态，会有无数的突发情况在等着你。你定义了半天观察者、备忘录，第二天这部分需求被砍了；写了半天接口，抽象类，忽然下午告诉你要加个十万八千里打不着边的啥东西，于是又开始加适配器，等你加完了告诉你又砍了。甚至有次半夜被喊起来改代码，等改完了发现需求被撤回了，气的我直接请了两天假调整心情。<br>设计模式和大的框架绝对是一个项目中非常重要的东西，但不是绝对重要的；一个好的PM团队，在某种意义上，才真正决定了这个项目的代码质量。<br><br></p><blockquote>作者：程序员新社区 来源：牛客博客，原文：<a href="http://link.zhihu.com/?target=https%3A//blog.nowcoder.net/n/e46f2ac3e37f490a97f91669a46269e6%3Ffrom%3Dnowcoder_improve" class=" wrap external" target="_blank" rel="nofollow noreferrer">为什么很多程序员不用 switch，而是大量的 if...else if ...？</a></blockquote><p>那么怎么优化这种逻辑呢？</p><p><b>记住下面的口诀：</b><br></p><figure data-size="normal"><img src="https://pic3.zhimg.com/v2-6143fe745082e4947d0836143c6af0cd_1440w.jpg" data-caption data-size="normal" data-rawwidth="500" data-rawheight="384" data-default-watermark-src="https://pic4.zhimg.com/v2-8eebd5045b70a21ca6273ab71d081d81_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic3.zhimg.com/v2-6143fe745082e4947d0836143c6af0cd_r.jpg" referrerpolicy="no-referrer"></figure><p><br></p><p>最后，分享一份大学期间自己整理的电子书库，绝不是在网上那种打包下载的，而是自己需要学到某个方向知识的时候，去网上挨个找的，最后汇总而成。</p><p>包括设计模式、代码优化、计算机基础等书籍，对编程提升帮助非常大：</p><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-d7a9537446e8aafeb0c5feb8cce72fc5_720w.jpg" data-caption data-size="normal" class="content_image" referrerpolicy="no-referrer"></figure><p><br></p><p><b>我整理的这些书大家可以在这里获取，对于学习计算机的同学帮助非常大，且十分系统</b>：</p><p>书单：<a href="http://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzg4NjUxMzg5MA%3D%3D%26mid%3D100000686%26idx%3D1%26sn%3Daaf4a33db6e08f9be085c0c57f14fb3a%26chksm%3D4f99ca2378ee43350e13cba18595a432a0e87ddc2a8aa8457eed8d1712fb45deb1295546d834%23rd" class=" wrap external" target="_blank" rel="nofollow noreferrer">书单推荐，少即是多（含下载方式）</a></p>  
</div>
            