
---
title: 'Gwenview 名字背后的故事'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/e8a0563355b36a31cc690a3f54a808be.jpg!custom'
author: 煎蛋
comments: false
date: Sat, 26 Mar 2022 03:15:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/e8a0563355b36a31cc690a3f54a808be.jpg!custom'
---

<div>   
<blockquote><p>Gwenview 一开始是作为 GTK+ 应用程序诞生的</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/e8a0563355b36a31cc690a3f54a808be.jpg!custom" referrerpolicy="no-referrer"><p>投稿：<strong>笑眯眯的狗</strong><br>
<em>原文：https://agateau.com/2021/the-story-behind-gwenview-name/</em></p>
<p><strong>引子</strong><br>
前两天我<em>(原作者)</em>在回想我是如何创建了 Gwenview， 然后我意识到它的诞生以及其不同寻常(作为一个 KDE 应用)的名字背后的原因并非众所周知。是时候写一篇文章了。这篇文章中至少会揭开一个隐藏了很久的秘密……让我们开始吧！</p>
<p><img src="https://cors.zfour.workers.dev/?http://tva1.sinaimg.cn/mw690/00745YaMgy1h0n41qo1ktj3074074gle.jpg" alt="Gwenview 名字背后的故事" referrerpolicy="no-referrer"><br>
<em>这个古怪的人物曾是 Gwenview 0.1.0 的图标</em></p>
<p><strong>起源</strong><br>
90年代末期，我开始使用 Linux，跑的是带 GNOME 的 Mandrake 发行版。当时我很可能尝试过 KDE，要么是它无法正常运行，要么就是我不喜欢它。我用 GQview 来浏览图片，但并不是很满意，所以我决定自己写一个图像查看器。当时我只有在 Windows 上的 UI 开发经验，用的是 Borland C++ Builder 和它自带的 VCL toolkit。我看了一圈 Linux 上可用来创建图形应用的 C++ 框架。我发现了 Qt，但是很快就把它排除了，主要是因为那个声名狼藉的 MOC(元对象编译器)。这个异端根本就不是纯正的 C++！我已经被C++ Builder添加到语言中的众多扩展功能搞得焦头烂额，我不打算再接受不纯的东西了！当时我既年轻又傻(现在我没那么年轻了，希望也傻的轻点了)。</p>
<p>候选对象是 GTK+。我对 GTK+ 有特殊的好感，因为我是通过 GIMP 来到 Linux 的(一开始是在 Windows 上跑它，很喜欢它，但它在 Linux 上更稳定，所以我开始经常使用双系统启动)。</p>
<p>是的，你没看错！ Gwenview 一开始是作为 GTK+ 应用程序诞生的！</p>
<p>此时我需要一个以字母“G”开头的名字。因为这在当时是一项传统：GNOME 和 GTK+ 程序要以“G”命名开头，KDE 程序要以“K”开头。我记得和当时的女友(现在是我妻子)Gwenaëlle 讨论过。我们一个名字也想不出。某天我开玩笑地说：“你看，我可以把它叫做 Gwenview”。然后我也想不出更好的名字了，就这么一直叫到现在。</p>
<p><strong>成为 KDE 应用程序</strong><br>
我一边写 Gwenview 一边学习 gtkmm，我发现其维护者之一 Guillaume Laurent 最近离开了项目并切换到了 Qt。我思考了片刻。这家伙精通 gtkmm，并且在其中投入了大量时间，依然决定切换到 Qt。就算 Qt不是“纯正的 C++”，我至少也该给它个机会。说干就干。第一件让我惊讶的事就是它的文档。当时 GTK+ 的文档大多数只有一个教程(现在已经好多了)。与之相反的是 Qt 有完整的相互参照的 API 文档和众多的示例。我惊了。读了更多之后，很明显，这就是我想用的 toolkit。Qt 感觉要更高效，更易用。它并不完美，但让我的启程之路变得更容易了。</p>
<p>所以我用 Qt 重写了 Gwenview。当时我已经切换到了 KDE 2，所以切换到 Qt 后不久我就开始使用 KDELibs，然后 Gwenview 就成了 KDE 应用程序。Gwenview 最早是在 SourceForge 上开发的，你依然可以在那里找到 gwenview-0.1.0.tar.gz。到 KDE 3 时，它和 KDE 的关系更近了：成为了 KDE Extra Gear 的一部分：这是一套有自己发布计划，但使用 KDE 基础架构(CVS → SVN，Bugzilla，最重要的是，translators)的应用程序的合集。在 KDE 4.0 (当时管它叫“KDE 4”还不是什么弥天大罪)开发期间，它转移到了 kdegraphics 并且成为了默认的图像查看器。</p>
<p><img src="https://cors.zfour.workers.dev/?http://tva1.sinaimg.cn/mw690/00745YaMgy1h0n41qu8n1j30lf0flaxi.jpg" alt="Gwenview 名字背后的故事" referrerpolicy="no-referrer"><br>
<em>运行在 KDE 3 上的 Gwenview 0.x</em></p>
<p>为什么不重新起个名字？</p>
<p>其实是如果我给它改个名字，感觉就像是背叛了我女友一样。用她名字的一部分成为了某种感情纽带。我维护 Gwenview 14年了。最后我累了，但这种感情纽带让我很难轻易放手。我最终克服了它，并让其他人接手开发，但如果当初它是其他名字的话，这事就容易多了。如今我很高兴看到 Gwenview 有了自己的生命，很多人在照料它。</p>
<p>回顾这事，我不推荐用所爱之人或周围人的名字命名项目。我觉得这会影响你的判断并且很难继续前行。毕竟，这只是代码，你并不是你的代码。而且，如果我和 Gwenaëlle 最终没有一起的话，继续用 Gwenview 这名字会有点怪异。这种情况确实至少发生过一次，而且是发生在一个大项目身上：Debian。Ian Murdock 创建了 Debian，他的名字是“Debian”中的“Ian”。“Deb”则来自 Debra Lynn 的名。Debra 当时是 Ian 的女朋友。他们结婚了，但最终分开(参见 Wikipedia 上 Debian 文章的“创建”部分)。</p>
<p>好了，你现在已经知道了 Gwenview 从未被讲述过的早期历史，以及我在起了这么个名字后获得的一点小小的智慧。</p>  
</div>
            