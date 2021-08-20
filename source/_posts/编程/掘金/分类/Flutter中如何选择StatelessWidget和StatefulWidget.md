
---
title: 'Flutter中如何选择StatelessWidget和StatefulWidget'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bba65de67ff84aefba21e0bd711260c3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 20:29:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bba65de67ff84aefba21e0bd711260c3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Flutter作为“新”的跨平台UI开发框架，延续了React组件化的开发思路，开发者可以通过一个个组件来构建完整的App的界面。由于React中只提供了一个基础组件类React.Component，因此开发者在在写组件代码之前不需要进行选择，直接继承React.Component类进行开发即可。然而在Flutter中，它提供给了开发者两个重要的基础组件，分别是StatelessWidget和StatefulWidget。虽然从名字来看很好理解，一个是无状态的组件，另一个是有状态的组件。但是对于一个刚接触Flutter的初学者来说，可能会产生一系列疑问：</p>
<p>1.它们的区别是什么？</p>
<p>2.如何进行选择？</p>
<p>3.使用不当会不会影响性能？</p>
<p>下面的内容将围绕这三个问题展开。</p>
<h1 data-id="heading-0">StatelessWidget和StatefulWidget的区别</h1>
<p>在讲解它们之间的区别前，我们先来熟悉一下StatelessWidget和StatefulWidget的基本概念和用法。</p>
<h2 data-id="heading-1">StatelessWidget</h2>
<p>无状态组件的概念与React中的“展示型组件”非常相似。无状态意味着该组件内部不维护任何可变的状态，组件渲染所依赖的数据都是通过组件的构造函数传入的，并且这些数据是不可变的。我们先来看看StatelessWidget的使用示例，代码如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> content;
  <span class="hljs-keyword">const</span> MyWidget(<span class="hljs-keyword">this</span>.content);
  
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Container(
      child: Text(content)
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码中，我们定义了一个名为MyWidget的无状态组件，该组件通过外部传入的content来展示一段文本。那么这里为什么说数据是不可变的呢？</p>
<p>可以注意到，组件内定义content变量的时候，使用了final进行修饰，因此该值在构造函数中第一次被赋值后就无法被改变了，也因此该组件在渲染一次后，其内容将无法被再次改变。如果我们在定义变量时不使用final，编辑器会给予对应的警告，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bba65de67ff84aefba21e0bd711260c3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果想展示其它的文本内容，只能在父组件通过变量进行改变。例如，我们可以用一个有状态组件包裹它，并通过改变状态值来改变无状态子组件展示的内容（这部分会在下面的内容中进行讲解）。该组件将在Flutter进行下一帧渲染前销毁并创建一个全新的组件用于渲染。</p>
<h2 data-id="heading-2">StatefulWidget</h2>
<p>有状态组件的概念与React中的“容器型组件”非常类似。有状态组件除了可以从外部传入不可变的数据，还可以在组件自身内部定义可变的状态。通过StatefulWidget提供的setState方法改变这些状态的值来触发组件重新构建，从而在界面中显示新的内容。我们使用一个StatefulWidget来包裹上面的MyWidget，通过状态来改变MyWidget渲染的文本内容，代码如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> content;
  <span class="hljs-keyword">const</span> MyWidget(<span class="hljs-keyword">this</span>.content);
  
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">'MyWidget build'</span>);
    <span class="hljs-keyword">return</span> Container(
      key: key,
      child: Text(content)
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyStateFulWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;

  <span class="hljs-meta">@override</span>
  State<StatefulWidget> createState() &#123;
    <span class="hljs-keyword">return</span> _FulWidgetStateWidgetState();
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_FulWidgetStateWidgetState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">MyStateFulWidget</span>> </span>&#123;
  
  <span class="hljs-built_in">String</span> content = <span class="hljs-string">'default'</span>;
  
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">'FulWidget build'</span>);
    <span class="hljs-keyword">return</span> GestureDetector(
      onTap: ()&#123;
        setState(()&#123;
          content = <span class="hljs-string">'text'</span>;
        &#125;);
      &#125;,
      child: MyWidget(content),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码中，我们创建了一个有状态的MyStateFulWidget来管理content内容。当我们通过setState改变content值时，将会触发MyStateFulWidget子组件的更新，Flutter将会使用新的content值创建一个MyWidget对象进行渲染，然后在界面中展示出新的content内容。</p>
<h2 data-id="heading-3">区别</h2>
<p>从上面对两类组件的介绍中不难看出，除了实现方法之外，它们最大的区别在于组件内部是否维护有可以改变的状态。对于无状态组件而言，其内部不维护可改变状态，渲染所依赖的数据全部来自于组件创建时的构造函数。无状态组件只有在父组件中调用构造函数之后才能触发构建，因此无状态组件需要依赖父组件来触发构建。而有状态组件在其内部维护了可变的状态，可以在内部通过setState来改变状态以触发自身包括子组件的重新构建。</p>
<p>那么有状态组件是如何做到通过改变状态来触发子组件更新的呢？我们来看一下setState的源码：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// framework.dart Line:1048</span>
<span class="hljs-meta">@protected</span>
<span class="hljs-keyword">void</span> setState(VoidCallback fn) &#123;
    ……
    <span class="hljs-keyword">if</span> (_debugLifecycleState == _StateLifecycle.created && !mounted) &#123;
      <span class="hljs-keyword">throw</span> FlutterError.fromParts(<DiagnosticsNode>[
        ……
      ]);
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
  &#125;());
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">Object?</span> result = fn() <span class="hljs-keyword">as</span> <span class="hljs-built_in">dynamic</span>;

<span class="hljs-comment">// 重点</span>
  _element!.markNeedsBuild();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>setState方法的最后一行调用了Element的markNeedsBuild方法，该方法将标记当前元素为脏元素，告诉Flutter在下一帧渲染前需要对该组件进行重新构建。要理解这个过程，我们需要先了解Flutter将Widget转换为UI的过程。</p>
<p>在Flutter中，Widget的作用是存储它所代表的UI块的配置信息。也就是说，Flutter并不直接使用Widget来渲染UI，而是把它当做UI的配置项，真正代表UI的是Element类。从Widget的创建到渲染UI，大致的流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfa2cc9f14ae4b82bbb5d55345938b17~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Flutter在这个过程中会生成3颗树：Widget树、Element树和RenderObject树。Flutter根据Widght树生成Element树，然后根据Element树生成RenderObject树。Flutter的UI系统会最终根据RenderObject树提供的布局信息，将组件绘制在屏幕上。</p>
<p>当这三颗树初次构建完毕后，UI呈现在了屏幕上。Flutter在后续每一帧渲染前，都需要对树进行逐层diff判断，看它们是否有变化（是否被标记为脏组件）。如果树的某个节点被标记为脏组件，则会把该节点及其子节点重新创建新的组件引用替换原来的节点。这样在下一帧渲染后，我们在界面上就能看到新的内容了。</p>
<p>Flutter如何判断组件节点有没有更新呢？前面提到的markNeedsBuild方法就起到这个作用。被markNeedsBuild标记组件，会被Flutter认为是有更新且需要重新被构建的。因此当我们在调用setState方法后，该组件就在diff阶段被重新构建。</p>
<blockquote>
<p>从setState源码中我们还能看到一个有趣的事：对于改变组件状态的代码 content = 'text'，无论是写在setState回调函数内部还是外部，作用是一样的。因为组件只要被标记为需要更新，都会在重新构建时获取最新的状态进行构建。</p>
</blockquote>
<p>当我们了解setState的原理后，可能会产生一个疑问：既然setState是调用markNeedsBuild方法让有状态组件进行更新的，那么无状态组件有没有办法也通过调用markNeedsBuild方法来让自己更新呢？其实也是有的，我们来看下面的代码：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> MaterialApp(
      theme: ThemeData.dark().copyWith(scaffoldBackgroundColor: darkBlue),
      debugShowCheckedModeBanner: <span class="hljs-keyword">false</span>,
      home: Scaffold(
        body: Center(
          child: MyWidget(<span class="hljs-string">'wwww'</span>),
        ),
      ),
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> content;
  <span class="hljs-keyword">const</span> MyWidget(<span class="hljs-keyword">this</span>.content);
  
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">'MyWidget build'</span>);
    <span class="hljs-keyword">return</span> GestureDetector(
      onTap: ()&#123;
        <span class="hljs-comment">// 重点</span>
        (context <span class="hljs-keyword">as</span> <span class="hljs-built_in">Element</span>).markNeedsBuild();
      &#125;,
      child: Container(
        width: <span class="hljs-number">300</span>,
        height: <span class="hljs-number">300</span>,
        decoration: BoxDecoration(
          color: Color.fromRGBO(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>)
        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码中，MyWidget是一个宽和高都为300的白色方形区域，通过GestureDetector在这个区域上监听了Tap事件。在Tap事件中，我们将context强制转换为Element类型（Element实现了BuildContext接口：framework.dart Line: 3004 : abstract class Element extends DiagnosticableTree implements BuildContext），当我们每次点击白色区域时，都会将MyWidget标记为脏组件，让Flutter对其进行重新构建。在DartPad中运行上面的demo，点击白色的区域，可以在控制台中看到输出的MyWidget build日志，这说明MyWidget被重新构建了，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f55adaee353a46a891ff6a596f0beb91~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在看来无状态组件也可以通过某些方法自己触发自己重新构建嘛，好像与开头说的“无状态组件只有在调用构造函数之后才能触发构建”有点相悖？</p>
<p>我个人认为不用过于纠结这个点，StatelessWidget的设计意图就是让开发者可以更方便的去实现一个无自管理状态的组件。StatelessWidget隐藏很多StatefulWidget中的方法，在使用StatelessWidget时无需override各种不需要的方法，也不需要关心内部状态的变化，只需要关心外部传入什么数据并展示即可。</p>
<p>在使用React的时候，我们需要通过代码规范来约定哪些是容器型组件，哪些是展示型组件。并且需要看完组件的实现代码才能知道它是哪种类型的。Flutter在设计中直接将这两个概念分开，使其更为显性，阅读代码时只需要看组件开头的定义就能知道是哪种组件。</p>
<h1 data-id="heading-4">什么情况下应该用StatelessWidget？什么情况下应该用StatefulWidget？</h1>
<p>从整体上来看，Flutter期望开发人员在实现组件之前，就考虑并决定需要使用的是无状态还是有状态组件，这可以使得应用的组件设计更为合理。</p>
<p>我们抽象一些场景来谈谈如何进行选择，以一个按钮为例。</p>
<h2 data-id="heading-5">通用按钮</h2>
<p>需求是要实现一个非常普通的通用按钮，这个按钮会在多处用到，除了按钮文字不同之外，其它的样式完全相同。因此，我们需要实现一个可以根据外部传入的内容来展示按钮中的文字通用按钮组件。从需求分析来看，按钮自身不会改变自身要显示的内容，而是由外部控制的，所以这种情况显然应该用StatelessWidget。代码如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

<span class="hljs-keyword">final</span> Color darkBlue = Color.fromARGB(<span class="hljs-number">255</span>, <span class="hljs-number">18</span>, <span class="hljs-number">32</span>, <span class="hljs-number">47</span>);

<span class="hljs-keyword">void</span> main() &#123;
  runApp(MyApp());
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> MaterialApp(
      theme: ThemeData.dark().copyWith(scaffoldBackgroundColor: darkBlue),
      debugShowCheckedModeBanner: <span class="hljs-keyword">false</span>,
      home: Scaffold(
        body: Center(
          child: CommonButtonWidget(<span class="hljs-string">'确定'</span>),
        ),
      ),
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommonButtonWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> buttonText;
  <span class="hljs-keyword">const</span> CommonButtonWidget(<span class="hljs-keyword">this</span>.buttonText);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> GestureDetector(
      child: Container(
        width: <span class="hljs-number">120</span>,
        height: <span class="hljs-number">60</span>,
        decoration: BoxDecoration(color: Color.fromRGBO(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>)),
        child: Text(
          buttonText,
          textAlign: TextAlign.center,
          style: TextStyle(
            color: Colors.blue,
            fontSize: <span class="hljs-number">18.0</span>,
            height: <span class="hljs-number">2.5</span>,
            fontFamily: <span class="hljs-string">"Courier"</span>,
          ),
        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码运行结果如下图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19ba11a27abd499ebf17628d836a2c26~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">自带倒计时的按钮</h2>
<p>想必大家都使用过各网站的短信验证码发送功能，当验证码成功发出后，发送按钮会增加一个倒计时的功能并修改按钮的文案。在倒计时开始后，按钮将不可点击。从需求分析来看，按钮的呈现形式在用户使用的过程中会有三个变化：</p>
<p>1.按钮文案更改</p>
<p>2.显示倒计时</p>
<p>3.可点击状态的变更</p>
<p>根据这些点，我们在实现之前就需要判断这些变化是由外部控制还是内部控制的，进而选择用哪种组件形式实现更为合理。很显然，这些变更点都属于这个按钮本身的职责范围内。根据低耦合高内聚的设计原则，这部分的代码逻辑应该实现在组件代码内部。因此，这里需要使用有状态组件来实现，代码如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'dart:async'</span>;

<span class="hljs-keyword">final</span> Color darkBlue = Color.fromARGB(<span class="hljs-number">255</span>, <span class="hljs-number">18</span>, <span class="hljs-number">32</span>, <span class="hljs-number">47</span>);

<span class="hljs-keyword">void</span> main() &#123;
  runApp(MyApp());
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> MaterialApp(
      theme: ThemeData.dark().copyWith(scaffoldBackgroundColor: darkBlue),
      debugShowCheckedModeBanner: <span class="hljs-keyword">false</span>,
      home: Scaffold(
        body: Center(
          child: ButtonWidget(),
        ),
      ),
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ButtonWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  State<StatefulWidget> createState() &#123;
    <span class="hljs-keyword">return</span> _ButtonWidgetState();
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_ButtonWidgetState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">ButtonWidget</span>> </span>&#123;
  <span class="hljs-built_in">int</span> count = <span class="hljs-number">10</span>;
  <span class="hljs-built_in">int</span> status = <span class="hljs-number">0</span>;
  <span class="hljs-built_in">Map</span><<span class="hljs-built_in">int</span>, <span class="hljs-built_in">String</span>> textMap = &#123;<span class="hljs-number">0</span>: <span class="hljs-string">'发送'</span>, <span class="hljs-number">1</span>: <span class="hljs-string">'已发送'</span>&#125;;
  Timer timer = Timer(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">0</span>), () &#123;&#125;);
  
  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">'FulWidget build'</span>);
    <span class="hljs-keyword">return</span> GestureDetector(
      onTap: () &#123;
        <span class="hljs-keyword">if</span> (status == <span class="hljs-number">0</span>) &#123;
          setState(() &#123;
            status = <span class="hljs-number">1</span>;
          &#125;);
          timer.cancel();
          timer = Timer.periodic(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">1</span>), (timer) &#123;
            count = count - <span class="hljs-number">1</span>;
            <span class="hljs-keyword">if</span>(count == <span class="hljs-number">0</span>)&#123;
              timer.cancel();
              setState(() &#123;
                status = <span class="hljs-number">0</span>;
                count = <span class="hljs-number">10</span>;
              &#125;);
            &#125;<span class="hljs-keyword">else</span>&#123;
              setState(() &#123;
                count = count;
              &#125;);
            &#125;
          &#125;);
        &#125;
      &#125;,
      child: Container(
        width: <span class="hljs-number">120</span>,
        height: <span class="hljs-number">60</span>,
        decoration: BoxDecoration(color: Color.fromRGBO(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>)),
        child: Row(
            mainAxisSize: MainAxisSize.min,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                textMap[status] ?? <span class="hljs-string">'发送'</span>,
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: Colors.blue,
                  fontSize: <span class="hljs-number">18.0</span>,
                  height: <span class="hljs-number">1.5</span>,
                  fontFamily: <span class="hljs-string">"Courier"</span>,
                ),
              ),
              status == <span class="hljs-number">1</span> ?SizedBox(
                width: <span class="hljs-number">5</span>
              ): Container(),
              status == <span class="hljs-number">1</span> ? Text(
                count.toString(),
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: Colors.blue,
                  fontSize: <span class="hljs-number">18.0</span>,
                  height: <span class="hljs-number">1.5</span>,
                  fontFamily: <span class="hljs-string">"Courier"</span>,
                ),
              ): Container(),
            ]),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码运行结果如下图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a403f76ad4f41e3ad30e9cd161b554a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>回到最初的问题，开发者怎么选择？</p>
<p>这里的建议是，如果将要实现的组件需要内部管理渲染依赖的数据，并且会在首次渲染后通过改变状态来重新渲染，那么就需要使用有状态组件StatefulWidget，如果不是则使用StatelessWidget。当我们不知道如何进行选择时，先尝试使用StatelessWidget实现，遇到问题再切换到StatefulWidget。</p>
<h1 data-id="heading-7">使用不当会不会影响性能？</h1>
<p>这个问题的核心点在于StatelessWidget和StatefulWidget在什么情况下会重新构建。</p>
<p>对于StatelessWidget来说，只要其父组件的状态发生改变，或祖先组件改变状态导致其父组件重新构建，StatelessWidget本身都会重新构建。受React PureCompoment概念的影响，从React转到Flutter时总是会惯性的认为如果传入StatelessWidget的参数不变，那么它将不会重新构建。由于Flutter中在diff时没有比较参数的机制（官方认为这个过程已经足够快了），因此StatelessWidget在上述情况中总是会重新构建。StatefulWidget基本与StatelessWidget相同，除了受到父元素影响而导致重新构建之外，它还能自己触发重新构建。因此，无论使用哪个都不会有性能上的差异。</p>
<p>我们不妨写的demo来验证一下：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

final Color darkBlue = Color.fromARGB(<span class="hljs-number">255</span>, <span class="hljs-number">18</span>, <span class="hljs-number">32</span>, <span class="hljs-number">47</span>);

<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  runApp(MyApp());
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  @override
  Wid<span class="hljs-keyword">get</span> <span class="hljs-title">build</span>(<span class="hljs-params">BuildContext context</span>) &#123;
    <span class="hljs-keyword">return</span> MaterialApp(
      theme: ThemeData.dark().copyWith(scaffoldBackgroundColor: darkBlue),
      <span class="hljs-attr">debugShowCheckedModeBanner</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">home</span>: Scaffold(
        body: Center(
          child: FulWidget(),
        ),
      ),
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  
  final <span class="hljs-built_in">String</span> content;

  MyWidget(<span class="hljs-built_in">this</span>.content);
  
  @override
  Wid<span class="hljs-keyword">get</span> <span class="hljs-title">build</span>(<span class="hljs-params">BuildContext context</span>) &#123;
    print(<span class="hljs-string">'MyWidget build'</span>);
    <span class="hljs-keyword">return</span> Container(
      key: key,
      <span class="hljs-attr">child</span>: Text(content, <span class="hljs-attr">style</span>: Theme.of(context).textTheme.headline4)
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FulWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  @override
  State<StatefulWidget> <span class="hljs-function"><span class="hljs-title">createState</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> _FulWidgetStateWidgetState();
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_FulWidgetStateWidgetState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">FulWidget</span>> </span>&#123;
  int a = <span class="hljs-number">0</span>;
  
  @override
  Wid<span class="hljs-keyword">get</span> <span class="hljs-title">build</span>(<span class="hljs-params">BuildContext context</span>) &#123;
    print(<span class="hljs-string">'FulWidget build'</span>);
    <span class="hljs-keyword">return</span> GestureDetector(
      onTap: ()&#123;
        setState(()&#123;
          a = a + <span class="hljs-number">1</span>;
        &#125;);
      &#125;,
      <span class="hljs-attr">child</span>: Row(
        children: [
          Container(
            width: <span class="hljs-number">300</span>,
            <span class="hljs-attr">height</span>: <span class="hljs-number">300</span>,
            <span class="hljs-attr">decoration</span>: BoxDecoration(
              color: Color.fromRGBO(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>)
            ),
          ),
          MyWidget(<span class="hljs-string">'Test'</span>)
        ]
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码中，MyWidget是一个无状态组件，它的父组件为FulWidget为有状态组件。我们通过响应点击事件来改变FulWidget的内部状态a来触发FulWidget的重新构建。从点击后输出的结果来看，在我们并没有改变传入MyWidget组件的值的情况下，MyWidget组件还是重新构建了。于此同时，FulWidget自身也进行了重新构建，如下图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba9bfd3c67204f27bcde1509fba90ebb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果在应用场景中某个无状态组件在任何情况下都不需要重新构建，那么可以在声明和调用的时候给无状态组件加上const，如下代码所示：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> content;

  <span class="hljs-comment">// 给构造函数加const</span>
  <span class="hljs-keyword">const</span> MyWidget(<span class="hljs-keyword">this</span>.content);
  
  ……
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FulWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  ……
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_FulWidgetStateWidgetState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">FulWidget</span>> </span>&#123;
  <span class="hljs-built_in">int</span> a = <span class="hljs-number">0</span>;
  
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">'FulWidget build'</span>);
    <span class="hljs-keyword">return</span> GestureDetector(
      onTap: ()&#123;
        ……
      &#125;,
      child: Row(
        children: [
          ……
<span class="hljs-comment">// 在调用时使用const</span>
          <span class="hljs-keyword">const</span> MyWidget(<span class="hljs-string">'Test'</span>)
        ]
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们按照同样的方法点击白色方块，可以在console中看到MyWidget并没有重新构建，只有FulWidget进行重新构建了，如下图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0db94c8bc3a946388b329715ee9f9266~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然官方说这个过程很快，但是没有必要的重新构建还是让人膈应。有没有办法像React那样有个shouComponentUpdate方法来让开发者对这一行为进行控制从而进行极致的优化呢？Flutter本身是没有提供的，但可以通过其它方法来实现。如果想了解更多关于这个方面的内容，可以阅读下面文章中的内容。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloppaper.com%2Fthe-ultimate-solution-to-prevent-widget-rebuild-by-flutter%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developpaper.com/the-ultimate-solution-to-prevent-widget-rebuild-by-flutter/" ref="nofollow noopener noreferrer">developpaper.com/the-ultimat…</a></p></div>  
</div>
            