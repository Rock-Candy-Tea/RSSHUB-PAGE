
---
title: 'Google开源Carbon语言，旨在成为C++的继任者'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=1770'
author: Dockone
comments: false
date: 2022-08-11 09:10:41
thumbnail: 'https://picsum.photos/400/300?random=1770'
---

<div>   
<br>作为谷歌内部开发的最新编程语言，Carbon日前已经以C++候选继任者的身份正式亮相。<br>
<br>多年以来，谷歌先后创造出多种编程语言，但有些大受欢迎、有些则寂寂无名。例如，Golang（简称Go）就是专为改进服务器和分布式系统开发而创造的语言，现已得到广泛应用。而当初为了替代JavaScript而设计的Dart语言，则一直到Flutter的出现才逐渐成为主流。<br>
<br>日前，于多伦多召开的Cpp North大会上，谷歌员工Chandler Carruth公布了全新编程语言Carbon的发展愿景。为了结合应用场景，Carruth还专门展示了目前最流行的编程语言中有多少是原有语言的继任者，又是如何利用现代语言成果帮助开发者快速提高生产力。<br>
<br>Android开发者很清楚，Kotlin就是Java的继任者；iOS开发者也很清楚，Swift就是Objective-C的继任者。微软打造的TypeScript彻底增强了JavaScript，能够在保证开发者友好的同时将代码“转译”回JS。在谷歌内部得到广泛使用的C++，也在一定程度上被看作是C语言的继任者。<br>
<br>还有很多朋友眼中的纯Mozilla项目，目前拥有众多铁杆粉丝的Rust，它实际上当初也是作为C++继任者登场的。但Carruth对它的继任者身份提出了一点质疑，毕竟Rust确实很适合用于新项目开发，但却不像Java和Kotlin间那样具有“双向互操作性”，因此难以稳定迁移。<br>
<br>换句话说，如果Rust能让大家用得开心，不妨继续使用。但想要把C++生态系统迁移到Rust，则是相当困难。<br>
<br>为此，虽然Carbon与Rust有着许多相同目标，例如帮助开发者创建“以性能为先的软件”，但Carbon的独特优势在于能跟现有C++代码全面互操作。此外，如果必要，谷歌甚至希望能轻松把C++代码转译为Carbon。<br>
<br>至于C++开发者接纳Carbon的理由，Carruth在舞台上分享了这种新语言的诸多亮点。<br>
<br>Introducer关键字和简单语法<br>
函数输入参数为只读值<br>
指针提供间接访问和变体<br>
使用表达式来命名类型<br>
软件包为root命名空间<br>
通过包名导入API<br>
用显式对象参数进行方法声明<br>
单继承；默认使用最终类<br>
强大且经过定义检查的泛型<br>
类型可显式实现接口<br>
<br>除了语言本身的特性之外，Carbon团队还着力面向未来需求进行语言设计。项目代码被公开托管在<a href="https://github.com/carbon-language/carbon-lang">GitHub上</a>，且对PR请求开放。Carbon还采取非常包容的项目文化，对企业员工和个人自由开放。<br>
<br>换言之，Carbon编程语言并不强调自己的谷歌出身。虽然此次演讲来自谷歌员工，而且Carbon目前的项目负责人主要（但并非全部）来自谷歌，但其并不属于纯谷歌自有项目。<br>
<br>其中的用意当然非常明显，虽然Carbon孕育自谷歌内部，但项目团队知道只有将其广泛分享给社区，这款年轻的语言才有望最终成功。Carbon必须成为“一个由独立社区驱动的项目”。在评论中，Carruth还进一步强调，Carbon目前还只是实验性项目，但已经有一些公司表现出早期关注。<br>
<br>如果大家也对Carbon语言感兴趣，不妨下载<a href="https://github.com/carbon-language/carbon-lang#getting-started">源代码</a>并在自己的设备上一探究竟。另外，它还跟<a href="https://carbon.compiler-explorer.com/">Compiler Explorer</a> Web应用相集成，所以大家可以直接在浏览器中体验Carbon语言。<br>
<br><strong>原文链接：<a href="https://9to5google.com/2022/07/19/carbon-programming-language-google-cpp/">Carbon, a new programming language from Google, aims to be C++ successor</a></strong>
                                
                                                              
</div>
            