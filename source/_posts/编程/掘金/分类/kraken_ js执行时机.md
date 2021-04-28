
---
title: 'kraken_ js执行时机'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65212839066b4f089c57d2dcd7b78bb4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 00:45:25 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65212839066b4f089c57d2dcd7b78bb4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="copyable">flutter: 2.0.1
kraken: main@b5574e6
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看源码一定要带着问题，有针对性的了解不然会陷入代码的汪洋大海中，对于整个仓库有个通观概览的认识，先看效果。运行仓库中的示例代码(kraken/example/assets/bundle.js)可以看到生成了flutter节点控件：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65212839066b4f089c57d2dcd7b78bb4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
源码片断如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> text1 = <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-string">'Hello World!'</span>);
<span class="hljs-keyword">var</span> br = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'br'</span>);
<span class="hljs-keyword">var</span> text2 = <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-string">'你好，世界！'</span>);
p.style.textAlign = <span class="hljs-string">'center'</span>;
...
p.appendChild(text1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>于是很自然的，我们想知道js生成节点如何与dart控件对应的；要运行js文本那js引擎必须准备好，它是如何初始化的；同时外部传入的<code>assets/bundle.js</code>是什么时机读取并传给引擎执行的：</p>
<ol>
<li>
<p>js生成节点如何与dart控件对应</p>
</li>
<li>
<p>js引擎初始化的时机</p>
</li>
<li>
<p>运行指定js文件的时机</p>
</li>
</ol>
<h2 data-id="heading-0">概览</h2>
<p>从示例应用(kraken/example/lib/main.dart)的来看，入口还是相对清晰的,直接将<code>Kraken</code>对象作为<code>Scaffold</code>的body主体，接收了参数<code>assets/bundle.js</code>作为<code>bundlePath</code>的值，跟踪它就解决问题3。</p>
<p><code>Kraken</code>是一个无状态的Widget, 创建的子控件为<code>_KrakenRenderObjectWidget</code>, 它又是一个<code>SingleChildRenderObjectWidget</code>，这种控件是为了专门绘制单个节点的控件，最重要的2个方法:<code>RenderObject createRenderObject(BuildContext context)</code>创建一个绘制对象；<code>_KrakenRenderObjectElement createElement()</code>创建控件对应的节点(Element)。</p>
<p>先明析一个概念，前端经常说到<strong>渲染</strong>，但这里的渲染不是指具体的绘制操作，一般是输出一段html文本或者几个vnode节点交由浏览器作解析，离绘制还有很长一段距离。flutter里的<code>RenderObject</code>(渲染对象)是真正的绘制，在这里需要有尺寸，内容，色值，画刷等相关的对象去进行绘制操作(离屏幕上出现绘制内容其实也有不小的距离)，所以为了防止一些名词上的混乱，一概以绘制代替渲染。</p>
<p>另一个概念是节点Element，flutter里的Element不区分TextNode也没有显式的<code>appendChild</code>操作，也不是html/xml文本里说的元素，它由Widget创建(<code>Element createElement()</code>是Widget的抽象方法)并且与Widget一一对应。</p>
<p>再一个需要回顾的是flutter框架如何建立控件节点树相关的一些机制。简而言之，我们是先得有Widget对象，它来创建一个节点(Element),节点具体做父子关系建立的工作，这样节点树通过各种类型的Widget及其build方法建立起来，这一步由flutter框架完成的，外部不能自己持有节点自行建立层级关系，这一过程叫做挂载(mount)。</p>
<p>所以就可以明白<code>_KrakenRenderObjectElement</code>的唯一方法<code>void mount(Element parent, dynamic newSlot) async &#123;</code>的作用了。</p>
<p>从<code>Widget Kraken.build(BuildContext)</code>到<code>void _KrakenRenderObjectElement.mount(Element parent, dynamic newSlot)</code>是异步的，中间显然创建了非常多的东西，一步一步来看。</p>
<p>于是按上面的概览总体的分了4步:</p>
<pre><code class="copyable">1 Kraken.build()
  _KrakenRenderObjectWidget()

2 _KrakenRenderObjectWidget.createRenderObject

3 _KrakenRenderObjectWidget.createElement

4 _KrakenRenderObjectElement.mount

<span class="copy-code-btn">复制代码</span></code></pre>
<p>步骤1几乎没什么操作，只是生成对象持有外部传入数据</p>
<p>步骤4的代码也不多，其实已经知道问题3的答案了，不确定的话查找一下传入的<code>_bundlePath</code>的最终引用，其实就是在<code>KrakenController.loadBundle</code>这个方法里。深入代码再看一下方法调用:</p>
<pre><code class="copyable">4 _KrakenRenderObjectElement.mount
  4.1 KrakenController.loadBundle
    KrakenBundle.getBundle
      AssetsBundle()
      *AssetsBundle.resolve
  4.2 _evalBundle
    controller.evalBundle()
      KrakenBundle.eval
        evaluateScripts
          _evaluateScripts
            'evaluateScripts'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就2步 4.1载入资源js文本，具体解析资源的是<code>AssetsBundle</code>, 基类是<code>KrakenBundle</code></p>
<p>4.2调用js引擎求值(evaluate)，这里用了个全局方法<code>_evalBundle</code>，真是匪夷所思的操作，所有对象都在<code>KrakenController</code>里还搞个全局方法； 最终通过dart的ffi调用了js引擎库的方法 <code>'evaluateScripts'</code>。</p>
<p>于是问题3答案近在咫尺：
Kraken是在挂载节点的时候读取内容，再由js引擎执行</p>
<p>问题接踵而至js引擎又是何时完成初始化的?</p></div>  
</div>
            