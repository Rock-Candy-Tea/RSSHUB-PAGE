
---
title: 'Web前端工程师Flutter快速入门，大佬勿入！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80329c33a7f6495d9dcc236ed18339c0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 23:12:17 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80329c33a7f6495d9dcc236ed18339c0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p><img alt="Snipaste_2021-03-28_14-10-42.jpg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80329c33a7f6495d9dcc236ed18339c0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>2021年3月4日，Flutter重磅发布了其2.0版。将Flutter一套代码横跨6端的体验全部带到了stable。大帅从去年年底开始接触并学习Flutter，刚开始还不是特别喜欢Flutter的开发体验。这次2.0发布后，我决心要成为Flutter的布道者。那么同样身为前端工程师的我，带大家一起来感受一下Flutter的魅力。</p>
<blockquote>
<p>本篇文章中将结合一些我曾经文章里的内容，整合为一篇面向Web前端工程师的Flutter入门教程。</p>
</blockquote>
<p>本篇内容的视频版：<a href="https://www.bilibili.com/video/bv1ev41187gs" target="_blank" rel="nofollow noopener noreferrer">www.bilibili.com/video/bv1ev…</a></p>
<h1 data-id="heading-1">跨端开发的前世今生</h1>
<p>大帅曾经是一名<code>闪客</code>。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4250737d8244e6c917a374c445e7ad7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>之所以提到这个，是因为我说Flash是曾经的Web1.0时代的跨端之王，应该没有人反对吧（我个人拿Flash做过网页，在当时还没有Adobe AIR的时候，我就拿.net + ActiveObjectX实现过桌面端），后来的ActionScript3.0更是<code>ES4</code>的唯一实现。不过那个时候还没有诞生移动互联网，直到乔帮主给Flash下了驱逐令。</p>
<blockquote>
<p>跨端真正变成一种开发方式，要从移动互联时代开始说起</p>
</blockquote>
<h2 data-id="heading-2">1.基于Webview的跨端模式</h2>
<p>就是使用网页浏览容器（Webview）来呈现html页面，配合Webview和原生系统的通讯api，可以调用原生方法。优点是开发效率高，成本最低，缺点是Webview的内存开销较高，启动白屏问题以及没有原生的页面跳转体验等（这个问题后来的引擎通过webview多开都解决了）。</p>
<h2 data-id="heading-3">2.使用JS+受限的HTML和CSS的Native渲染模式</h2>
<p>为了解决Webview跨端的问题，另一种新的方案被提出来。代码仍然使用Javascript编写，运行在独立的JS内核（如JSCore，V8）中，使用受限的HTML，受限的CSS来编写界面，但最终会使用原生的UI框架来渲染（如UIKit）。Facebook旗下的RN，Apache基金会的Weex都属于这种方式。</p>
<h2 data-id="heading-4">3.Hybrid渲染模式</h2>
<p>注意，不是混合开发，而是指混合渲染。是在一个页面里既使用Webview来渲染又使用原生的UI来渲染。比如微信小程序</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bb5650a79f041fa835922fb84ec4b20~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>第2,3种方式都有一个问题，就是JS代码是运行在独立的JS内核中，和视图层的渲染不在一个线程里，那逻辑层和视图层里的数据要互通，会有通讯折损，这个时间差大部分时候我们感受不到。但我们去尝试做一个跟手的交互效果，就能明显感受到。</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17e97b90298c465da19c0bea3a13fd7d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>为了解决这个问题，在RN/Weex里我们有了BindingX方案，微信小程序里有了WXS方案。</p>
<h1 data-id="heading-5">自渲染的Flutter</h1>
<p>Flutter是自己“<code>独创</code>”的一套渲染模式，即不使用webview来渲染，也不使用原生UI来渲染，而是自己实现了一套声明式的UI体系，然后在画布里画出来。</p>
<p><code>这套东西并不新鲜</code></p>
<p>十几年前的Flash也是“自渲染”呀，当年就很多“<code>传统工程师</code>”反映在Flash里做UI太麻烦了，后来有了第三方的UI框架Aswing等，再后来有了Flex。各种知名的游戏引擎也是如此，比如Unity3D，Unreal。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84d6d0e2ba2b4a1384325179cf416ed2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>游戏里不也有各种UI吗？它们的跨端表现不也是一致的吗？游戏里要绘制那么多图形，浮点运算，3D渲染....效率不也挺高的吗？</p>
<p>所以，别被这些新词搞蒙了，“自渲染”就是自己有一套规范约束声明UI，然后自己在一个独立的“画布”里把它们绘制出来。这个画布在游戏引擎里叫<code>OpenGL</code>,<code>WebGL</code>....在Flutter里，它叫<code>SGL</code>（SkiaGraphicsLibrary）。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99a226153b2a40a09229f9bc3de701d5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>而<code>Skia</code>本身就很强大，Chrome浏览器，Android系统的底层绘制库都是它。</p>
<h1 data-id="heading-6">Dart语言</h1>
<p>对于Web前端开发者而言，Dart绝对不是把你拦在门外的因素，毕竟Dart语言也是ECMA的标准。但Dart在提供一些新特性的同时，也有其特立独行的一面，这些差异会增加Web前端开发者的学习和记忆成本。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5310efb365b14878835b6677d760d9b9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>举个简单的例子，获取一个0.0到1.0之间的随机浮点值</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">//JS的随机浮点值</span>
Math.random();

<span class="hljs-comment">//Dart的随机浮点值</span>
Random().nextDouble();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">//JS的数组</span>
<span class="hljs-keyword">var</span> list = [];
list.push(<span class="hljs-number">1</span>);
list.push(<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>);

<span class="hljs-comment">//Dart的数组</span>
<span class="hljs-keyword">var</span> list = [];
list.add(<span class="hljs-number">1</span>);
list.addAll([<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>像这样的差异还有挺多，如果你的工作需要在两种语言间反复切换，那就换个工作吧~~ 哈哈：p！开个玩笑，但你应该感受到了什么叫做记忆成本的增加。</p>
<h1 data-id="heading-7">安装Flutter开发环境</h1>
<p>这里就不废话了，请查看 <a href="https://juejin.cn/post/6887967800799789064" target="_blank">安装教程</a> 。开发环境支持Win/Mac/Linux。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dded3e7ff201401b9c7cf6e73dc83563~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>不安装开发环境，我们也能在网页里 <a href="https://juejin.cn/post/dartpad.cn">dartpad.cn</a> 来编写调试感受一下Dart和Flutter的魅力</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a9383180b3c4b588ab260a94c89563c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">IDE选择</h1>
<ul>
<li>VSCode</li>
</ul>
<blockquote>
<p>安装插件：Flutter，Dart，Bracket Pair Colorizer，Awesome Flutter Snippets</p>
</blockquote>
<ul>
<li>Android Studio</li>
</ul>
<blockquote>
<p>无论是是否使用Android Studio来编写Dart代码，Android Studio都是Flutter开发环境安装的必选项。</p>
</blockquote>
<p>我平时属于经常在多个前端语言里切换的，主要使用的IDE就是VSCode，所以我基本不使用Android Studio。但我在看了很多其他大佬的视频后发现，Android Studio更配Flutter，有一些特性VSCode里暂时还没有插件可以实现。</p>
<h1 data-id="heading-9">嵌套地狱？</h1>
<p><em>Flutter是一种声明式UI框架，每个组件，会有个build函数，这里会返回一个能够完整描述UI的对象结构。</em></p>
<p>而Flutter的嵌套地狱问题，主要就来自这个声明式UI的特性。我们可以用<code>拆解嵌套</code>来解决嵌套过深的问题，但嵌套的究竟是什么？</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/832912520dad4bd88ecb31bade478016~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a5a1d3187c94086a16203558c137307~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>来，让我<code>换一个说法</code>给你介绍</p>
<p><code>声明式UI</code> 就是 <code>虚拟Dom</code></p>
<h1 data-id="heading-10">万物皆Widgets！</h1>
<p>像 <em><code>万物皆Widgets ，一切皆组件</code></em> 这样的话很多文章都说过了。</p>
<p>我提一<del>杯</del>，不是，提一句</p>
<p><code>子不教，父之过</code></p>
<ul>
<li>当儿子没有这个能力的时候，找他爹！</li>
<li>他爹没有这个能力的时候，找他爷爷！</li>
<li>他爹没有这个能力的时候，是不是可以换个爹！</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69eb08f6beff46059ef0bcde060e40cf~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我把官方文档中列举的所有Widgets做成一个脑图</p>
<p>微信搜索 <code>大帅老猿</code> 关注后回复 <code>flutter</code> 即可下载</p>
<h1 data-id="heading-11">Flutter项目基本结构</h1>
<h2 data-id="heading-12">创建项目</h2>
<pre><code class="copyable">flutter create projectname
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">配置文件</h2>
<pre><code class="copyable">pubspec.yaml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个文件就等于我们熟悉的packages.json</p>
<ul>
<li>配置依赖</li>
</ul>
<pre><code class="copyable">dependencies:
  flutter:
    sdk: flutter
  flame: ^1.0.0-rc5

dev_dependencies:
  flutter_test:
    sdk: flutter
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>配置图片和字体</li>
</ul>
<pre><code class="copyable">assets:
    - assets/images/
    - assets/images/xxx.jpg
    
fonts:
    - family: MyFont
      fonts:
        - asset: assets/fonts/myfont.ttf
<span class="copy-code-btn">复制代码</span></code></pre>
<p>pubspec.yaml的配置采用缩进式结构体，在配置时要注意缩进的规则。</p>
<h2 data-id="heading-14">入口代码</h2>
<pre><code class="copyable">lib/main.dart
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你所有的代码都应该在lib这个文件夹下，你可以根据自己的习惯来组织你的代码。</p>
<h2 data-id="heading-15">项目内常用命令</h2>
<p>查看当前可run的设备列表</p>
<pre><code class="copyable">flutter devices
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将Flutter项目运行到设备列表中的默认项</p>
<pre><code class="copyable">flutter run
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将Flutter项目运行到设备列中的指定设备</p>
<pre><code class="copyable">flutter run -d macos
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">入门demo之点不到的按钮</h1>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bf5344e3e4d450a9f65f90f47d52e62~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>界面里有一个按钮，点击后就随机改变坐标</p>
</blockquote>
<pre><code class="hljs language-dart copyable" lang="dart">
<span class="hljs-built_in">double</span> left = <span class="hljs-number">100</span>;<span class="hljs-comment">//x坐标</span>
<span class="hljs-built_in">double</span> top = <span class="hljs-number">100</span>;<span class="hljs-comment">//y坐标</span>


<span class="hljs-comment">//爷爷是Stack，爸爸是Positioned，儿子是ElevatedButton</span>
Stack(
    children:[
        Positioned(
            left:left,  <span class="hljs-comment">//x坐标</span>
            top:top,   <span class="hljs-comment">//y坐标</span>
            child:ElevatedButton(
                child:Text(<span class="hljs-string">"点我呀"</span>),
                onPressed:()&#123;
                    setState(()&#123;
                        left = Random().nextDouble()*<span class="hljs-number">300</span>;
                        top = Random().nextDouble()*<span class="hljs-number">300</span>;
                    &#125;)
                &#125;
            )
        )
    ]
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">加入动画</h2>
<p>位置改变的时候加入动画效果？So easy~</p>
<p>Flutter的Widget封装得太好了，记得我们前面说的。</p>
<p><code>儿子不行找爸爸</code></p>
<p><code>爸爸不行，换一个爸爸</code></p>
<p>我们只需要把Positioned换成AnimatedPositioned，然后设置一下动画持续时长</p>
<pre><code class="hljs language-dart copyable" lang="dart">Stack(
    children:[
        AnimatedPositioned(
            duration:<span class="hljs-built_in">Duration</span>(millsecond:<span class="hljs-number">500</span>),<span class="hljs-comment">//动画持续500毫秒</span>
            left:left,  <span class="hljs-comment">//x坐标</span>
            top:top,   <span class="hljs-comment">//y坐标</span>
            child:ElevatedButton(
                child:Text(<span class="hljs-string">"点我呀"</span>),
                onPressed:()&#123;
                    setState(()&#123;
                        left = Random().nextDouble()*<span class="hljs-number">300</span>;
                        top = Random().nextDouble()*<span class="hljs-number">300</span>;
                    &#125;)
                &#125;
            )
        )
    ]
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="2021-03-29 13_22_01.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/311461cc68d748cd96d3356c02c0eba7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-18">Flutter里的路由</h1>
<p>使用Navigator</p>
<p>推入新页面</p>
<pre><code class="hljs language-dart copyable" lang="dart">Navigator.push(context, MaterialPageRoute(builder: (BuildContext context)&#123;
    <span class="hljs-keyword">return</span> PageDetail();
&#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>退出当前页</p>
<pre><code class="hljs language-dart copyable" lang="dart">Navigator.pop(context);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">动画之神奇移动？</h1>
<p>两个路由页之间相同元素的动画怎么做？比如A页面是个通讯录列表页，B页面是点击之后的联系人详情页。A页面的头像和昵称要以动画的方式移动到B页面里的状态。</p>
<p>好好感受一下这个动画，它在两个页面之间</p>
<p><img alt="2021-03-29 15_00_32.gif" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8eb19335b52d471ba3c5c37e5ee937eb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在其它框架里，要实现这个动画效果，要么你创建一个独立于两个页面的顶级元素，在A页面的动画开始时隐藏元素，B页面先隐藏元素推入，在动画结束后再将其显示出来。要么把两个页面整合到一个页面里。</p>
<p>而在Flutter里，我们只需要用<strong>Hero动画</strong>将目标动画元素包裹起来，即可直接实现。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">//A页面</span>
Hero(
  tag: <span class="hljs-string">"logo"</span>, 
  child: FlutterLogo(
  size: <span class="hljs-number">64</span>,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">//B页面</span>
Hero(
  tag: <span class="hljs-string">"logo"</span>, 
  child: FlutterLogo(
  size: <span class="hljs-number">128</span>,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是这么简单！</p>
<h1 data-id="heading-20">结束语</h1>
<p>简简单单的一个入门导读，并没有特别系统的介绍到Flutter的方方面面，但希望能让更多的Web前端工程师们对Flutter产生兴趣，加入进来吧！</p>
<hr>
<p>微信搜索 <code>大帅老猿</code> 关注后回复 <code>flutter</code> 加入Flutter交流群</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            