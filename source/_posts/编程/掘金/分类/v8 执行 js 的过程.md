
---
title: 'v8 执行 js 的过程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ebc5da8de5b4e6891eea39752db23db~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 16:36:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ebc5da8de5b4e6891eea39752db23db~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ebc5da8de5b4e6891eea39752db23db~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 102 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://zoo.team/article/the-process-of-executing-js-in-v8" target="_blank" rel="nofollow noopener noreferrer">v8 执行 js 的过程</a></p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cd1a5e813ea4227b8fd21be41a71938~tplv-k3u1fbpfcp-watermark.image" alt="九渊.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">前言</h2>
<p>本文意在简单的介绍一下 V8 执行 JS 的过程，通过了解 V8 执行 JS 的过程，知道 JS 代码呈现在浏览器上到底做了什么。当然本人也是在陆续探索 V8 ，文章中如有不当之处，还望不吝指正，理性交流。</p>
<p>众所周知，机器（CPU）只能识别机器码（二进制码），对于 JS 代码，它是识别不了的，所以当代码成为页面出现在屏幕上的时候，必然是做了很多的转译工作。</p>
<h2 data-id="heading-1">V8 执行 Javascript 过程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c22fdb3bf7c6441091d97e4808918ef3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，我们将一步步进行拆分分析：</p>
<h3 data-id="heading-2">JS TO AST</h3>
<p>在 V8 引擎拿到 JS 代码之后，<strong>解析器</strong>（Parser）会对其进行词法分析和语法分析。</p>
<h4 data-id="heading-3">词法分析</h4>
<p>将 JS 代码拆分成对应的 Token，Token 是能拆分的最小单位，固定 type 表述类型/属性，value 表示对应的值，如下图 Token。</p>
<h4 data-id="heading-4">语法分析</h4>
<p>在进行词法分析转为 Token 之后，解析器继续根据生成的 Token 生成对应的 AST，AST 相信前端同学并不陌生，也是热词之一，无论是在 Vue、React 中虚拟 DOM 的表示，或者 Babel 对 JS 转译的表示都是先将其转化为对应的 AST，解析器解析之后的 AST 结构如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43af5a528db34860901cbb5c03d1fc10~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，一段极小的代码片段，被解析成 AST 之后复杂了很多，在图中的 AST 还仅仅是简化后的数据，全部的 AST 其实还有很多参数，将会更复杂。</p>
<h3 data-id="heading-5">字节码</h3>
<p>在解析器（Parser）将 JS 代码解析成 AST 之后，<strong>解释器</strong>（Ignition）根据 AST 来生成字节码（也称中间码）。前文提到 CPU 只能识别机器码，对字节码是识别不了的，这里就衍生出一个问题，如果 CPU 识别不了字节码，那为什么还要在中间插一步来耗费资源转字节码呢？效率不是很更低吗？</p>
<p>在计算机学科里聊效率，都逃避不了时间和空间这两个概念，绝大部分的优化都是空间换时间和时间换空间，两者的平衡，效率如何达到最高，是一个很值得深入研究的问题。</p>
<p>拿之前版本的 V8 引擎执行 JS 来说，是没有转字节码这一步骤的，直接从 AST 转成机器码，这个过程称为编译过程，所以每次拿到 JS 文件的时候，首先都会编译，而这个过程还是比较浪费时间的，这是一件比较头疼的事情，需要一个解决办法。</p>
<p>一个网页第一次打开，关闭再次去打开，大部分情况下，还是和原来 JS 文件一致的，除非开发者修改了代码，但这个可以暂时不考虑，毕竟哪个网站也不会一天闲的无聊，不停的修改，上传替换。</p>
<h4 data-id="heading-6">缓存机器码</h4>
<p>按照这个思路，既然绝大多数情况下，文件不会修改，那编译后的机器码可以考虑缓存下来，这样一来，下次再打开或者刷新页面的时候就省去编译的过程了，可以直接执行了，存储机器码被分成了两种情况，一个是浏览器未关闭时候，直接存储到浏览器本地的内存中，一个是浏览器关闭了，直接存储在磁盘上，而早期的 V8 也确实是这么做的，典型的牺牲空间换时间。</p>
<h4 data-id="heading-7">缓存带来的问题</h4>
<p>思考一个问题，从上面的图中可以看到，一个很小的代码片段，转换成 AST 之后，变大了很多，文件大了导致一个问题就是需要更大的内存来存储，而 JS 文件转成机器码（即二进制文件），会比原来的 JS 文件大几百甚至几千倍，这就意味这一个几十 KB 的 JS 文件将会达到几十 MB，这就很可怕，本来 Chrome 多进程架构就已经很占用内存了，再来这一出，配置再好的电脑，也怕是无福消受 Chrome 了，毕竟使用者体验的好坏，直接决定了一个产品在市场上是否能生存下去，尽管 V8 缓存了编译后的代码，减少了编译的时间，提高了时间上的效率，但代价是内存占用太大了，所以 Chrome 团队是有必要优化这个问题的。</p>
<h4 data-id="heading-8">惰性编译</h4>
<p>当然，引进其他技术是需要时间去开发和优化的，在一个技术架构产生的同时，必然会有劣势方面的弥补，而早期版本的 V8 为了解决占用内存和启动速度，引进了<strong>惰性编译</strong>，那么问题来了，<strong>惰性编译</strong>做了什么去提高效率的呢？</p>
<p><strong>惰性编译</strong>还是比较容易理解的，从作用域的角度思考，ES6 之前之只有全局作用域和函数作用域，而<strong>惰性编译</strong>的思路就是 V8 启动的时候只编译和缓存全局作用域的代码，而函数作用域中的代码，会在调用的时候去编译，同样函数内部编译后的代码一样不会被缓存下来。</p>
<h4 data-id="heading-9">惰性编译存在的问题</h4>
<p>引入<strong>惰性编译</strong>之后，在编译速度和缓存上看来，都得到了提升，一切看起来似乎很完美了，对，是看起来，但是设计出来的东西，你永远不知道使用者会怎么使用，在 ES6 和 Vue、React 等这些没有普及之前，绝大部分开发者都使用的是 jQuery，以及 RequireJS 等类似产品，JQ 插件各种引用，各种插件或者开发者自己封装的方法，为了不污染其他使用者的变量，一般都封装成一个函数，这样问题就来了，<strong>惰性编译</strong>不会保存函数编译后的机器码和理解编译函数，如果一个插件太大那等到使用函数再去编译，编译的时间上就会变得很慢，这相当于是开发者将<strong>惰性编译</strong>给玩完了，路给封死了。</p>
<h4 data-id="heading-10">引入字节码</h4>
<p>好吧，玩不过开发者了，那 V8 团队只好换个思路，就引入字节码吧。首先要理解什么是字节码，字节码其实是机器码的抽象，各种字节码的相互构成，可以实现 JS 所需的所有功能，当然首先一点，字节码比机器码占用的内存要小很多很多，基本是机器码所在内存的几十甚至几百分之一，这样一来字节码缓存下来所消耗的内存还是可以接受的。</p>
<p>这里会有一个疑问，既然 CPU 不能识别字节码，那是不是还需要将字节码转成机器码呢？不然怎么执行，答案是肯定。解释在将 AST 转为字节码之后，会在执行的时候将字节码转成机器码，这个执行过程肯定是比直接执行机器码要慢的，所以在执行方面，速度上会比较慢，但是 JS 源码通过解析器转 AST，然后再通过解释器转字节码，这个过程是比编译器直接将 JS 源码转机器码要快很多的，全流程看来，整个时间上是差不了多少的，但是却减小了大量的内存占用，何乐而不为。</p>
<h3 data-id="heading-11">编译器</h3>
<h4 data-id="heading-12">热代码</h4>
<p>在代码中，常常会有同一部分代码，被多次调用，同一部分代码如果每次都需要解释器转二进制代码再去执行，效率上来说，会有些浪费，所以在 V8 模块中会有专门的监控模块，来监控同一代码是否多次被调用，如果被多次调用，那么就会被标记为<strong>热代码</strong>，这有什么作用呢？</p>
<h4 data-id="heading-13">优化编译器</h4>
<p><strong>TurboFan</strong> (优化编译器) 这个词相信关注手机界的同学并不陌生，华为、小米等这些品牌，在近几年产品发布会上都会出现这个词，主要的能力是通过软件计算能力来优化一系列的功能，使得效率更优。</p>
<p>接着热代码继续说，当存在热代码的时候，V8 会借着 TurboFan 将为热代码的字节码转为机器码并缓存下来，这样一来，当再次调用热代码时，就不在需要将字节码转机器码，当然热代码相对来说还是少部分的，所以缓存也并不会占用太大内存，并且提升了执行效率，同样此处也是牺牲空间换时间。</p>
<h4 data-id="heading-14">反优化</h4>
<p>JS 语言是动态语言，非常之灵活，对象的结构和属性在运行时是可以发生改变的，设想一个问题，如果热代码在某次执行的时候，突然其中的某个属性被修改了，那么编译成机器码的热代码还能继续执行吗？答案是肯定不能。这个时候就要使用到优化编译器的<strong>反优化</strong>了，他会将热代码退回到 AST 这一步，这个时候解释器会重新解释执行被修改的代码，如果代码再次被标记为热代码，那么会重复执行优化编译器的这个步骤。</p>
<h2 data-id="heading-15">总结</h2>
<p>从分析的过程来看，V8 对 JS 执行的过程，不仅使用到了解释器，还用到了优化编译器。这种两者结合去处理的方式，业界称为 JIT (Just-In-Time)。使用这种结合的方式来处理 JS，主要是利用了 AST 形成的文件较小，而通过优化编译器编译后的热代码执行效率高，两者结合，各自发挥各自的优势，将效率尽量提升到最大。</p>
<p>V8 所做的事情，远远不止这些，这里也仅仅是简单概况和分析一下主流程上所做的一些事情，如果细化到每个点，还有很多概念，比如内联缓存、隐藏类、快属性、慢属性、创建对象，以及笔者之前写的<a href="https://juejin.cn/post/6909239354418266119" target="_blank">垃圾回收</a>等等，所做的事情实在太多，就不一一例举了。</p>
<h2 data-id="heading-16">推荐阅读</h2>
<p><a href="https://juejin.cn/post/6945624014643855367" target="_blank">通过自定义Vue指令实现前端曝光埋点</a></p>
<p><a href="https://juejin.cn/post/6968988552075952141" target="_blank">手把手带你入门Webpack Plugin</a></p>
<h2 data-id="heading-17">开源作品</h2>
<ul>
<li>政采云前端小报</li>
</ul>
<p><strong>开源地址 <a href="https://www.zoo.team/openweekly/" target="_blank" rel="nofollow noopener noreferrer">www.zoo.team/openweekly/</a></strong> (小报官网首页有微信交流群)</p>
<h2 data-id="heading-18">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 40 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b28026eff3a4b2f8d8bb03d1989dd5b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            