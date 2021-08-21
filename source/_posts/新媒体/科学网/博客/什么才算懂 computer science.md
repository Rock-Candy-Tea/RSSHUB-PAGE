
---
title: '什么才算懂 computer science'
categories: 
 - 新媒体
 - 科学网
 - 博客
headimg: 'https://picsum.photos/400/300?random=9815'
author: 科学网
comments: false
date: Fri, 20 Aug 2021 07:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9815'
---

<div>   
<p><span style="font-family: Tahoma, "Microsoft Yahei", Simsun; font-size: 14px; background-color: #FFFFFF;">中学的时候在收音机里听了一部凡尔纳的小说，讲一群人在海上航行，船在一个无人孤岛触礁了，幸存者于是在岛上开始一步一步自力更生重建文明。故事详细讲述从生火开始、做陶器、炼铁、合成硝酸甘油等过程，从原理到工艺，听完小说，落难荒岛的人们完成了从石器时代到电力时代的进化，听者初高中物理化学也学得差不多了。有天他们做出了一个照相机与胶卷，对着远方的水平线拍了一张照片，冲印出来之后，发现有个黑点，再用放大镜仔细一看，那是一艘海盗船，于是准备战斗。。。这个故事给我留下了很深的印象。真正掌握了相关的知识，你就能重建科技文明。这是个人能力的标杆与境界。否则把你扔到荒岛上，你跟原始人也没啥差别。</span></p><p><span style="font-family: Tahoma, "Microsoft Yahei", Simsun; font-size: 14px; background-color: #FFFFFF;"><br></span></p><p>学计算机科学（ computer science) 的要达到这个类似的境界需要什么呢？得会两件东西，会写 compiler，会写操作系统。会不会这两招，是是否掌握CS文明的标准。按这个标准，比尔盖茨可能还行，会写点 BASIC的，更复杂的可能就玩不动了。漂流到荒岛上，他的美元成了废纸，雇佣不了人，在现代CS方面也只能靠边站了。当然了，在CS之前还有其他的，得有懂物理的先造出计算机硬件，但我们这里只讲CS。</p><p><br></p><p>Compiler 是一门理论与艺术结合的技能。昨天，有人问我你怎么写的 C++ compiler，不是有 gcc 吗？这么说的显然没读过 gcc 代码。我是若干年前打开看过，不能不拍案惊叹。其 c++ parser 一个文件数万行代码，完全是手写的 似乎 top-down parsing。你不能不敬佩开发者艰苦卓绝的毅力与勇气（当然这也可能是因为最初C的编译器也是手写的，g++ 继承了这个传统）。要知道，LL parsing 在很多语法上是麻烦的。模仿 gcc 手工攻克 C++，我看很少有人会有这个勇气。</p><p><br></p><p>我查看了我当年写的C++ 编译器代码，它是用 LEX，YACC 与 C++ 写的。C++这部分很容易可以改用C，所以说得过去。里面的关键是语法定义，如何消除大量的 shift-reduce 冲突与解决C++中的各种歧义。parser 不是 context free 的，而是根据语义进行变化。Lexical 分析部分会参考当前的符号表区分类名与其他的 identifier，这就把语法变得好设计多了。这个C++ compiler 支持当时C++的大部分功能，包括多继承等，但不支持 templates。那是 1990年代中期，微软的 VC++ 都不支持 templates 。Parsing 完成之后，我的 compiler 直接生成一种RISC汇编代码（类似MIPS），所以运行还需要一个 assembler。如果要写 assembler，那是个相对简单的事情。这个Compiler 也没有做什么复杂的优化，虽然优化手段我也是学了的。从我的角度，主要目的是完成一个相对功能完整的C++编译器，能够正确编译、运行相当复杂的C++程序。这应该算是足够了。</p><p><br></p><p>写完 compiler 之后，你会立刻会感觉功力提高了一个级别。如同少年侠客将九阳真经练到了1/4，再看巨鲸帮混混们那点招数，可以随时一掌击倒。</p><p><br></p><p>当然，你也知道，山外有山、人外有人。</p><p><br></p><p>当年计算机系过道里、公司办公室到处听到 PLUS-PLUS 那特有的双重爆破音。今天的C++越来越复杂，用的人也越来越少。但那段时光依旧令人怀念。</p><p><br></p>                    <br><br>
                                        <label style="font-size:13px; color:#850f0f">转载本文请联系原作者获取授权，同时请注明本文来自岳东晓科学网博客。<br>链接地址：</label><a href="http://blog.sciencenet.cn/blog-684007-1300534.html" target="_blank" style="font-size:13px; color:#850f0f">http://blog.sciencenet.cn/blog-684007-1300534.html </a>
  <br><br>上一篇：<a href="http://blog.sciencenet.cn/blog-684007-1296415.html" target="_black">风动力车跑得比风快：物理教授与网红科普人对赌1万美金的问题</a><br>                    <!--大赛结束-->
                                        
  
</div>
            