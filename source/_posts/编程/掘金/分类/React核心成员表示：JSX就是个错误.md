
---
title: 'React核心成员表示：JSX就是个错误'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cea36a6f4cc4268a47c301ab8e49407~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 22 May 2021 18:17:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cea36a6f4cc4268a47c301ab8e49407~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>近日，在一场关于<code>JSX</code>的讨论中，<code>React</code>核心成员<strong>Sebastian Markbåge</strong>（<code>Hooks</code>作者）表示：</p>
<p>他更推崇<code>SwiftUI</code>语法，并认为<code>JSX</code>就是个错误。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cea36a6f4cc4268a47c301ab8e49407~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>JSX</code>最早由<code>Facebook</code>提出并推广，在<code>React</code>中被广泛用来描述视图状态。</p>
<p>作为一种类<code>XML</code>的<code>JS</code>语法糖，<code>JSX</code>同时兼顾了两个优点：</p>
<h3 data-id="heading-0"><code>XML</code>对树状结构优秀的表现力</h3>
<p>不管是<strong>嵌套</strong>还是<strong>属性</strong>，<code>JSX</code>都能很自然的描述。</p>
<p>我们可以很容易从如下<code>JSX</code>结构推导出实际视图效果：</p>
<pre><code class="hljs language-js copyable" lang="js"><div style=&#123;&#123;<span class="hljs-attr">color</span>: <span class="hljs-string">'#f00'</span>&#125;&#125;>
  i am <span>Ka Song</span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1"><code>JS</code>在运行时的灵活</h3>
<p>曾有人说：</p>
<blockquote>
<p><code>JSX</code>就是拥有超能力的<code>HTML</code></p>
</blockquote>
<p>这里的超能力指：<code>JSX</code>作为<code>JS</code>语法糖，可以用<code>JS</code>语法灵活的描述视图状态。</p>
<pre><code class="copyable">function App(&#123;children&#125;) &#123;
  return (
    <div>
      &#123;children || 'i am empty'&#125;
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>作为对比，<code>Vue</code>模版语法的表现力就差很多。</p>
<p>然而，吾之蜜糖彼之砒霜：</p>
<h3 data-id="heading-2">受<code>JS</code>语法限制的<code>XML</code></h3>
<p>比如<code>class</code>属于<code>JS</code>语法<code>keyword</code>，而<code>class</code>在<code>HTML</code>中代表<strong>类名</strong>。</p>
<p>所以当<code>JSX</code>使用<code>className</code>作为<strong>类名</strong>的<code>props</code>时难免让人困惑。</p>
<pre><code class="hljs language-js copyable" lang="js"><div className=<span class="hljs-string">"container"</span>></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">依赖编译</h3>
<p><code>JSX</code>需要先编译为<code>JS</code>才能在宿主环境执行，所以使用<code>JSX</code>描述视图的框架（比如<code>React</code>）都需要依赖编译工具。</p>
<p>这增加了项目环境配置的复杂度。</p>
<h2 data-id="heading-4">DSL哪家强？</h2>
<p>到这里我们可以发现，衡量一门<code>DSL</code>（领域相关语言）优劣的标准有三点：</p>
<ul>
<li>
<p>是否能直观描述视图状态</p>
</li>
<li>
<p>是否有灵活的编程能力</p>
</li>
<li>
<p>原生支持还是需要编译</p>
</li>
</ul>
<p>让我们按这三个维度权衡几种不同平台的<code>DSL</code>：</p>
<h3 data-id="heading-5">HTML</h3>
<p>视图描述能力：🌟🌟🌟</p>
<p>编程能力：🌟</p>
<p>不需要编译：🌟</p>
<p><code>HTML</code>描述视图能力最强（因为与<code>DOM</code>节点一一对应），但是缺乏编程能力。</p>
<h3 data-id="heading-6">Pug、Vue、JSX</h3>
<p>视图描述能力：🌟🌟🌟</p>
<p>编程能力：🌟🌟~🌟🌟🌟</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff8b2052456846b282611a0ede50c820~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>都是在<code>XML</code>基础上演进的语法糖，拥有强大的描述视图能力。</p>
<p>他们的区别在于<strong>编程能力</strong>与<strong>模版语法</strong>的束缚之间取舍。</p>
<h3 data-id="heading-7">Flutter</h3>
<p>视图描述能力：🌟</p>
<p>编程能力：🌟🌟🌟🌟</p>
<p>使用函数调用的方式描述视图，编程能力很强。</p>
<p>但是在描述嵌套的组件树结构时，函数调用不如<code>XML</code>描述能力强。</p>
<p>比如如下<code>HTML</code>结构：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>I am<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Ka Song<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用<code>Flutter</code>语法描述：</p>
<pre><code class="hljs language-js copyable" lang="js">Stack(
  children: <Widget>[
     Text(<span class="hljs-string">"Hello"</span>),
     Text(<span class="hljs-string">"I am"</span>),
     Text(<span class="hljs-string">"Ka Song"</span>)
   ],
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">SwiftUI与React</h2>
<p><code>SwiftUI</code>作为被苹果寄予厚望、意图统领<code>IOS</code>全平台的<code>DSL</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06c3e922c9dd4e75ab8b80088dfc2593~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在保证强大的编程能力同时，也希望在视图表现力方面做的更好。</p>
<p>接下来我们通过一个简单的<strong>点击加一</strong>的计数器来对比<code>React</code>与<code>SwiftUI</code>语法：</p>
<p><code>React</code>使用<code>class</code>语法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Counter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
  &#125;
  <span class="hljs-attr">increment</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> &#123;counter&#125; = <span class="hljs-built_in">this</span>.state;
    <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">counter</span>: counter + <span class="hljs-number">1</span>&#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;counter&#125; = <span class="hljs-built_in">this</span>.state;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>数字：&#123;counter&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.increment&#125;</span>></span>点我加一<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>SwiftUI</code>：</p>
<pre><code class="hljs language-js copyable" lang="js">struct Counter : View &#123;
    @State <span class="hljs-keyword">var</span> counter = <span class="hljs-number">0</span>

    func increment () &#123;
        counter += <span class="hljs-number">1</span>
    &#125;

    <span class="hljs-keyword">var</span> body: some View &#123;
        VStack &#123;
            Text(<span class="hljs-string">"数字: \(counter)"</span>)
            <span class="hljs-function"><span class="hljs-title">Button</span>(<span class="hljs-params">action: increment</span>)</span> &#123;
                Text(<span class="hljs-string">"点我加一"</span>)
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，抛开语法差异，两个框架的写法是很类似的。</p>
<p>同时，<code>SwiftUI</code>凭借强大的编程能力，原生实现<code>React</code>当前并不支持的功能：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a782258c8b841ccbef66a0cb2aef987~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如，在<code>React</code>中，子组件要改变父组件的状态，需要父组件将<strong>状态</strong>与<strong>改变状态的方法</strong>传递给子组件。</p>
<p>子组件调用<strong>改变状态的方法</strong>通知父组件状态变化，父组件再传递变化后的<strong>状态</strong>给子组件。</p>
<p>这种方式在<code>React</code>中被称为<strong>受控组件</strong>。</p>
<p>在<code>SwiftUI</code>中，子组件只需要将父组件传递的状态申明为<code>@Binding</code>，就能达到与父组件该状态<strong>双向绑定</strong>的效果。</p>
<p>比如上例的<code>counter</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 从</span>
@State <span class="hljs-keyword">var</span> counter = <span class="hljs-number">0</span>
<span class="hljs-comment">// 变为</span>
@Binding <span class="hljs-keyword">var</span> counter
<span class="copy-code-btn">复制代码</span></code></pre>
<p>则计数器接受父组件传递的<code>counter</code>状态，子组件<code>counter</code>状态改变后会作用于父组件<code>counter</code>状态。</p>
<h2 data-id="heading-9">你更喜欢哪种DSL</h2>
<p>从2013年5月29日<code>React</code>诞生到现在。</p>
<p>经过8年的教育，大部分<code>React</code>开发者已经接受<code>JSX</code>。</p>
<p>但是，这期间也不断有人提出<code>JSX</code>的替代方案。</p>
<p>比如<a href="https://github.com/mlmorg/react-hyperscript" target="_blank" rel="nofollow noopener noreferrer">react-hyperscript</a>。</p>
<p>随着<code>SwiftUI</code>热度提升，更是有人提出用其替代<code>React</code>中的<code>JSX</code>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adbe74c73c024df59eeb123b8b19f6b5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>也有人做出模型<a href="https://github.com/tvler/experimental-react-like-framework#what-ive-built-so-far" target="_blank" rel="nofollow noopener noreferrer">experimental-react-like-framework</a></p>
<p>你喜欢<code>JSX</code>么？你觉得未来他会被谁取代？或者他会取代谁？</p></div>  
</div>
            