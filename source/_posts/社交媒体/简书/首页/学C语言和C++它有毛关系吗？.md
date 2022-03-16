
---
title: '学C语言和C++它有毛关系吗？'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/9824247-627c951140495574.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/9824247-627c951140495574.png'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="3600" data-height="1532"><img data-original-src="//upload-images.jianshu.io/upload_images/9824247-627c951140495574.png" data-original-width="3600" data-original-height="1532" data-original-format="image/png" data-original-filesize="1034342" src="https://upload-images.jianshu.io/upload_images/9824247-627c951140495574.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">20200810234426.png</div>
</div>
<hr>
<p>这是最近一周时间几个读者小伙伴所提的问题，我顺手截了两个图。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1198" data-height="382"><img data-original-src="//upload-images.jianshu.io/upload_images/9824247-7c4de4f3bbeb576f.png" data-original-width="1198" data-original-height="382" data-original-format="image/jpeg" data-original-filesize="37402" src="https://upload-images.jianshu.io/upload_images/9824247-7c4de4f3bbeb576f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1242" data-height="334"><img data-original-src="//upload-images.jianshu.io/upload_images/9824247-403c169e1d5966a8.png" data-original-width="1242" data-original-height="334" data-original-format="image/jpeg" data-original-filesize="43978" src="https://upload-images.jianshu.io/upload_images/9824247-403c169e1d5966a8.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>实不相瞒，这类问题之前也经常看到，但是我忘了截图了。</p>
<p>每次遇到这种问题，看起来很简单，但是打字一时半会还真说不清，想想今天周末了，写一篇文章来统一聊聊吧，如果小伙伴们有不同看法，也欢迎批评指正，评论区见。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="160" data-height="158"><img data-original-src="//upload-images.jianshu.io/upload_images/9824247-c658e8de02010214.png" data-original-width="160" data-original-height="158" data-original-format="image/png" data-original-filesize="34136" src="https://upload-images.jianshu.io/upload_images/9824247-c658e8de02010214.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<blockquote>
<p>本文在开源项目：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fhansonwang99%2FJavaCollection" target="_blank">https://github.com/hansonwang99/JavaCollection</a> 中已收录，里面包含不同方向的自学编程路线、面试题集合/面经、及系列技术文章等，资源持续更新中...</p>
</blockquote>
<hr>
<h2><strong><code>C</code>语言和<code>C++</code>到底是什么关系？</strong></h2>
<p>首先<code>C++</code>和<code>C</code>语言本来就是两种<strong>不同的</strong>编程语言，但<code>C++</code>确实是对<code>C</code>语言的扩充和延伸，并且对<code>C</code>语言提供后向兼容的能力。对于有些人说的<code>C++</code>完全就包含了<code>C</code>语言的说法还是有点别扭的。</p>
<p><code>C++</code>一开始被本贾尼·斯特劳斯特卢普（Bjarne Stroustrup）发明时，起初被称为<code>“C with Classes”</code>，即「带类的<code>C</code>」。很明显它是在<code>C</code>语言的基础上扩充了类class等面向对象的特性和机制。但是后来经过一步步修订和很多次演变（如下图所示），最终才形成了现如今这个支持一系列重大特性的庞大编程语言。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2000" data-height="351"><img data-original-src="//upload-images.jianshu.io/upload_images/9824247-49f641ff54f45e51.png" data-original-width="2000" data-original-height="351" data-original-format="image/png" data-original-filesize="31225" src="https://upload-images.jianshu.io/upload_images/9824247-49f641ff54f45e51.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>就像经典书籍《Effective C++》一开头就说的，现如今我们提到<code>C++</code>，都应该视其为一个庞大的「<strong>语言联邦</strong>」，最起码包含如下几个重要的组成部分：</p>
<ul>
<li><strong>面向过程编程</strong></li>
<li><strong>面向对象编程</strong></li>
<li><strong>泛型编程</strong></li>
<li><strong>元编程</strong></li>
<li><strong>函数式编程</strong></li>
<li><strong>STL标准库</strong></li>
</ul>
<p>这其中的第一部分「面向过程编程」，正是<code>C++</code>提供的向后兼容<code>C</code>语言的部分，所以你能看到市面上在售的大部分讲<code>C++</code>编程的书，一开始前几个章节基本都是在讲「面向过程编程」的内容，包括但不限于：数据类型、变量、运算符、表达式、语句、判断、循环、函数、指针等等这些内容。</p>
<hr>
<h2><strong>不学<code>C</code>语言能直接学<code>C++</code>吗？</strong></h2>
<p>还是像前面所说，<code>C++</code>编程语言的第一大重要组成部分就是「面向过程编程」，而这正是<code>C</code>语言老大哥的领域。即使没有学过C语言，一上来就直接学习<code>C++</code>的小伙伴，应该也难逃『面向过程』这一部分的内容。因为市面上在售的大部分讲<code>C++</code>编程的书，开始的章节都在讲「面向过程编程」的内容。</p>
<p>从理论上来说，学<code>C++</code>前<strong>并不一定</strong>非得学<code>C</code>语言，但是有<code>C</code>语言底子再去学<code>C++</code>往往更具优势，最起码「面向过程编程」这一部分内容能够轻车熟路。</p>
<p>但是遗憾的是，即使是《C++ Primer》这种<code>700</code>多页厚的权威<code>C++</code>书籍，开头也只有很少一部分在讲「面向过程编程」，所以对于面向过程这一部分的讲述是肯定没有专门讲<code>C</code>语言的书籍剖析得细致和全面的，不然也不会有这种重点侧重于指针相关的《C和指针》等这类书籍的出现了。</p>
<p>所以个人建议是在学<code>C++</code>之前，<code>C</code>语言的基础还是尽量要夯实，肯定是有帮助的。</p>
<hr>
<h2><strong><code>C</code>学得好的，学习<code>C++</code>是否更具优势？</strong></h2>
<p>是的。</p>
<p>最起码学<code>C++</code>时，里面的「面向过程」这一部分内容可以说轻车熟路了。</p>
<hr>
<h2><strong><code>C++</code>能替代<code>C</code>语言吗？</strong></h2>
<p>既然<code>C++</code>这么强大，包含这么多模块和范式，而且也几乎包含了<code>C</code>语言面向过程这一部分的内容，那为啥还要学<code>C</code>语言呢？都直接学习<code>C++</code>它不香嘛？</p>
<p>是的，<code>C++</code>很强大没错，但那些强大的范式和机制本身带来的<strong>包袱</strong>就不轻，也确实给学习者造成了不小的负担，甚至劝退了很多人。</p>
<p>而反观<code>C</code>语言，<code>C</code>语言本身就是一个把<strong>能力</strong>、<strong>性能</strong>、<strong>效率</strong>和<strong>学习成本</strong>权衡得非常极致的一种编程语言，以至于大学阶段必开的程序设计课程里基本都有<code>C</code>语言的身影。</p>
<p>而且<code>C</code>语言的应用领域极度广泛，上到操作系统底层的原生接口，下到普通的应用层开发，<code>C</code>语言都有着不小的功劳。以至于这么多年来，在<code>Tiobe</code>编程语言排行榜里，<code>C</code>语言都是居高位不下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1240" data-height="549"><img data-original-src="//upload-images.jianshu.io/upload_images/9824247-867f5cd19d67d68c.png" data-original-width="1240" data-original-height="549" data-original-format="image/png" data-original-filesize="248192" src="https://upload-images.jianshu.io/upload_images/9824247-867f5cd19d67d68c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>而且<code>2020</code>开年<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fhansonwang99%2FJavaCollection" target="_blank">C语言重回巅峰王座</a>，一举夺得「<code>2019</code>年度编程语言」。虽然这只是一个看起来很无聊的排名，但多多少少能说明一些事情。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1219" data-height="1036"><img data-original-src="//upload-images.jianshu.io/upload_images/9824247-c13c6e056d1e944f.png" data-original-width="1219" data-original-height="1036" data-original-format="image/png" data-original-filesize="245345" src="https://upload-images.jianshu.io/upload_images/9824247-c13c6e056d1e944f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>所以无论是过去，现在，甚至是未来，近<code>50</code>岁的<code>C</code>语言老将军依然永不为奴。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1319" data-height="862"><img data-original-src="//upload-images.jianshu.io/upload_images/9824247-471237dc59bfebec.png" data-original-width="1319" data-original-height="862" data-original-format="image/png" data-original-filesize="1839709" src="https://upload-images.jianshu.io/upload_images/9824247-471237dc59bfebec.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<hr>
<h2><strong>只有<code>C++</code>这种面向对象的语言才适合大型项目吗？</strong></h2>
<p><code>C++</code>的出现的确是为了更方便地开发大型应用程序，毕竟面向对象编程里的很多重要思想和机制都对大型项目和复杂系统所要求的项目工程化、代码复用性/扩展性/可维护性等提供了强大的支撑。</p>
<p>但是<strong>摆在眼前的事实</strong>告诉我们，即便是<code>C</code>语言，也照样可以构建出极其复杂的系统和软件。上到<code>Linux</code>这种旷世伟大的操作系统内核，小到被各个公司重度依赖的<code>Redis</code>、<code>Nginx</code>等开源软件或框架，都是<code>C</code>语言的代表作品。</p>
<p>所以有时候我们<strong>不得不承认的是</strong>，大家所说的抽象能力更多的是看写这个程序的人，而并非编程语言本身。</p>
<hr>
<h2><strong>小 结</strong></h2>
<p>好啦，扯得有点多了，总结一下就是：</p>
<ul>
<li>
<code>C</code>语言和<code>C++</code>是两个不同的编程语言，只不过内容上有一定的重叠；</li>
<li>
<code>C</code>语言是一门很强大的编程语言，我觉得有机会还是要学一下；</li>
<li>一般来说，有了<code>C</code>语言的基础，上手<code>C++</code>也会更快；</li>
<li>
<code>C++</code>和<code>C</code>各有各的选用考虑和应用场景，并没有谁更好一说，学不学看自己的兴趣和自身技术发展的考量</li>
</ul>
<hr>
<h2><strong>书籍推荐</strong></h2>
<p>最后聊一聊学习<code>C</code>语言和<code>C++</code>的书籍吧。</p>
<p>个人觉得如果想系统学习这两门语言，最好还是得看一下经典的书籍。</p>
<p>关于<code>C</code>语言学习书籍，最最权威的当然是<code>C</code>语言的发明者<code>Dennis M. Ritchie</code>所著的《The C Programming Language》（它也有中文版的），除此之外《C Primer Plus》也很系统全面。</p>
<p>关于<code>C++</code>的学习书籍，最权威的当属<code>C++</code>的发明者<code>Bjarne Stroustrup</code>大佬所著的《The C++ Programming Language》，但是很明显这本书不适合初学者，更加适合的还得是《C++ Primer》，也很系统全面。至于再深入可以继续阅读诸如《Effective C++》、《STL源码剖析》、《深度探索C++对象模型》等书籍。</p>
<p>这些书读完，成神之路便可由此开启。</p>
<blockquote>
<p>本文在开源项目：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fhansonwang99%2FJavaCollection" target="_blank">https://github.com/hansonwang99/JavaCollection</a> 中已收录，里面包含不同方向的自学编程路线、面试题集合/面经、及系列技术文章等，资源持续更新中...</p>
</blockquote>
<hr>
<p>每天进步一点点</p>
<p>慢一点才能更快</p>
  
</div>
            