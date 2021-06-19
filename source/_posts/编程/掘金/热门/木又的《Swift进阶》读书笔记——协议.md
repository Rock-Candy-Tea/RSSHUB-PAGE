
---
title: '木又的《Swift进阶》读书笔记——协议'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=3182'
author: 掘金
comments: false
date: Tue, 25 May 2021 01:50:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=3182'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">协议</h2>
<p>当我们使用泛型类型的时候，通常都会使用协议约束泛型参数的行为。有很多理由使得你应该如此，下面就是一些最常见的例子：</p>
<ul>
<li>通过协议，你可以构建一个依赖数字 (而不是诸如 Int，Double 等某个具体的数值类型) 或集合类型的算法。这样一来，所有实现了这个协议的类型就都具备了这个心算法提供的能力。</li>
<li>通过协议还可以抽象代码接口背后的实现细节，你可以针对协议进行编程，然后让不同的类型实现这个协议。例如，一个使用了 Drawable 协议的画图程序既可以使用 SVG 来渲染图形，也可以使用 Core Graphics。类似的，跨平台的代码可以使用一个 Platform 协议，然后由类似 Linux，macOS 或 iOS 这样的类型来提供具体的实现。</li>
<li>你还可以使用协议来让代码更具可测试性。更具体地说，当你基于协议而不是一个具体类型来实现某个功能的时候，在测试用例中就很容易把这部分替换成表示各种测试结果的类型。</li>
</ul>
<p>在 Swift 里，一个协议表示一组正式提出的 <strong>要求 (requirements)</strong>。例如，<code>Equatable</code> 协议要求实现的类型提供 <code>==</code> 操作符。这些要求可以是普通方法、初始化方法、关联类型、属性和继承的协议。有些协议还有一些无法用 Swift 类型系统表达的要求，例如，<code>Collection</code> 协议就要求下标操作符访问元素的时间复杂度是 0(1) (但你也可以违背这个要求，如果算法的时间复杂度不是O(1)，在方法的文档中明确说明就行了。)</p>
<p>Swift 协议的主要特性。</p>
<ul>
<li>协议可以自行扩展新的功能。</li>
<li>协议可以通过条件化扩展（conditional extensions）添加需要额外约束的 API。</li>
<li>协议可以继承其他协议。</li>
<li>协议可以被组合起来形成新的协议。</li>
<li>有时，某个协议的实现还依赖于其他协议的实现。</li>
<li>协议还可以声明关联类型，实现了这个协议的类型就需要定义关联类型对应的具体类型。</li>
</ul>
<h3 data-id="heading-1">协议目击者</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Eq</span><<span class="hljs-title">A</span>> </span>&#123;
  <span class="hljs-keyword">let</span> eq:(<span class="hljs-type">A</span>,<span class="hljs-type">A</span>) -> <span class="hljs-type">Bool</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们就可以为比较不同的具体类型 (例如： Int) 创建不同的 Eq 实例了。我们管这些实例，叫做表示相等判断的 <strong>显示目击者 (explicit witnesses)</strong>：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">Array</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">allEqual</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">compare</span>: <span class="hljs-type">Eq</span><<span class="hljs-type">Element</span>>)</span> -> <span class="hljs-type">Bool</span> &#123;
    <span class="hljs-keyword">guard</span> <span class="hljs-keyword">let</span> f <span class="hljs-operator">=</span> first <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span> &#125;
    <span class="hljs-keyword">for</span> el <span class="hljs-keyword">in</span> dropFirst() &#123;
      <span class="hljs-keyword">guard</span> compare.eq(f,el) <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span> &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是通过协议取代了显示目击者 (explicit witnesses) 的 allEqual 实现：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">Array</span> <span class="hljs-title">where</span> <span class="hljs-title">Element</span>: <span class="hljs-title">Equatable</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">allEqual</span>()</span> -> <span class="hljs-type">Bool</span> &#123;
    <span class="hljs-keyword">guard</span> <span class="hljs-keyword">let</span> f <span class="hljs-operator">=</span> first <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span> &#125;
    <span class="hljs-keyword">for</span> el <span class="hljs-keyword">in</span> dropFirst() &#123;
      <span class="hljs-keyword">guard</span> f <span class="hljs-operator">==</span> el <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span> &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相比泛型参数A，我们可以使用隐式泛型参数 Self，用它表示实现了协议的类型：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">Equatable</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">notEqual</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">l</span>:<span class="hljs-keyword">Self</span>, <span class="hljs-keyword">_</span> <span class="hljs-params">r</span>:<span class="hljs-keyword">Self</span>)</span> -> <span class="hljs-type">Bool</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-operator">!</span>(l <span class="hljs-operator">==</span> r)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">条件化协议实现 (Conditional Conformance)</h4>
<p>标准库中 Array 对 Equatable 的实现:</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">Array</span>: <span class="hljs-title">Equable</span> <span class="hljs-title">where</span> <span class="hljs-title">Element</span>: <span class="hljs-title">Equatable</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">==</span> (<span class="hljs-params">lhs</span>:[<span class="hljs-type">Element</span>], <span class="hljs-params">rhs</span>:[<span class="hljs-type">Element</span>])</span> -> <span class="hljs-type">Bool</span> &#123;
    <span class="hljs-built_in">fatalError</span>(<span class="hljs-string">"Implementation left out"</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">协议继承</h4>
<p>Swift 还支持协议的继承。例如，实现 Comparable 的类型也一定实现了 Equatable。这叫做 <strong>细化 (refinging)</strong>。换句话说，Comparable 改进了 Equatable：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">Comparable</span>: <span class="hljs-title">Equatable</span> </span>&#123;  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title"><</span> (<span class="hljs-params">lhs</span>: <span class="hljs-keyword">Self</span>, <span class="hljs-params">rhs</span>: <span class="hljs-keyword">Self</span>)</span> -> <span class="hljs-type">Bool</span>  <span class="hljs-comment">// ...&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">使用协议进行设计</h3>
<p>举个绘图协议的例子，首先，定义一个要求实现绘制椭圆和矩形接口的协议：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">DrawingContext</span> </span>&#123;
  <span class="hljs-keyword">mutating</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">addEllipse</span>(<span class="hljs-params">rect</span>: <span class="hljs-type">CGRect</span>, <span class="hljs-params">fill</span>: <span class="hljs-type">UIColor</span>)</span>
  <span class="hljs-keyword">mutating</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">addRectangle</span>(<span class="hljs-params">rect</span>: <span class="hljs-type">CGRect，fill：UIColor</span>)</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">CGContext</span>: <span class="hljs-title">DrawingContext</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">addEllipse</span>(<span class="hljs-params">rect</span>: <span class="hljs-type">CGRect</span>, <span class="hljs-params">fill</span> <span class="hljs-params">fillColor</span>: <span class="hljs-type">UIColor</span>)</span> &#123;
    setFillColor(fillColor.cgColor)
    fillEllipse(in: rect)
  &#125;
  
  <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">addRectangle</span>(<span class="hljs-params">rect</span>: <span class="hljs-type">CGRect</span>, <span class="hljs-params">fill</span> <span class="hljs-params">fillColor</span>: <span class="hljs-type">UIColor</span>)</span> &#123;
    setFillColor(fillColor.cgColor)
    fill(rect)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">SVG</span>: <span class="hljs-title">DrawingContext</span> </span>&#123;  <span class="hljs-keyword">mutating</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">addEllipse</span>(<span class="hljs-params">rect</span>: <span class="hljs-type">CGRect</span>, <span class="hljs-params">fill</span>: <span class="hljs-type">UIColor</span>)</span> &#123;    <span class="hljs-keyword">var</span> attributes: [<span class="hljs-type">String</span>: <span class="hljs-type">String</span>] <span class="hljs-operator">=</span> rect.svgEllipseAttributes    attributes[<span class="hljs-string">"fill"</span>] <span class="hljs-operator">=</span> <span class="hljs-type">String</span>(hexColor: fill)    append(<span class="hljs-type">Node</span>(tag: <span class="hljs-string">"ellipse"</span>, attributes: attributes))  &#125;    <span class="hljs-keyword">mutating</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">addRectangle</span>(<span class="hljs-params">rect</span>: <span class="hljs-type">CGRect</span>, <span class="hljs-params">fill</span>: <span class="hljs-type">UIColor</span>)</span> &#123;    <span class="hljs-keyword">var</span> attributes: [<span class="hljs-type">String</span>: <span class="hljs-type">String</span>] <span class="hljs-operator">=</span> rect.svgAttributes    attributes[<span class="hljs-string">"fill"</span>] <span class="hljs-operator">=</span> <span class="hljs-type">String</span>(hexColor: fill)    append(<span class="hljs-type">Node</span>(tag: <span class="hljs-string">"rect"</span>, attributes: attributes))  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">协议扩展</h4>
<p>Swift 协议中的一个关键特性就是 <strong>协议扩展 (protocol extension)</strong>。只要知道了如何绘制椭圆，就可以添加一个扩展来以某点为圆心绘制圆形。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">DrawingContexnt</span> </span>&#123;  <span class="hljs-keyword">mutating</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">addCircle</span>(<span class="hljs-params">center</span>: <span class="hljs-type">CGPoint</span>,<span class="hljs-params">radius</span>: <span class="hljs-type">CGFloat</span>, <span class="hljs-params">fill</span>: <span class="hljs-type">UIColor</span>)</span> &#123;    <span class="hljs-keyword">let</span> diameter <span class="hljs-operator">=</span> radius <span class="hljs-operator">*</span> <span class="hljs-number">2</span>    <span class="hljs-keyword">let</span> origin <span class="hljs-operator">=</span> <span class="hljs-type">CGPoint</span>(x: center.x <span class="hljs-operator">-</span> radius, y: center.y <span class="hljs-operator">-</span> radius)    <span class="hljs-keyword">let</span> size <span class="hljs-operator">=</span> <span class="hljs-type">CGSize</span>(width: diameter, height: diameter)    <span class="hljs-keyword">let</span> rect <span class="hljs-operator">=</span> <span class="hljs-type">CGRect</span>(origin: origin, size: size)    addEllipse(rect: rect.integral, fill: fill)  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给 DrawingContext 再创建一个扩展，给它添加一个在黄色方块中绘制蓝色圆形的方法：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">DrawingContext</span> </span>&#123;  <span class="hljs-keyword">mutating</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">drawingSomething</span>()</span> &#123;    <span class="hljs-keyword">let</span> rect <span class="hljs-operator">=</span> <span class="hljs-type">CGRect</span>(x: <span class="hljs-number">0</span>, y: <span class="hljs-number">0</span>, width: <span class="hljs-number">100</span>, height: <span class="hljs-number">100</span>)    addRectangle(rect: rect, fill: .yellow)    <span class="hljs-keyword">let</span> center <span class="hljs-operator">=</span> <span class="hljs-type">CGPoint</span>(x: rect.midX, y: rect.midY)    addCircle(center: center, radius: <span class="hljs-number">25</span>, fill: .blue)  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把这个方法定义在 DrawingContext 的扩展里，我们就能通过 SVG 或 CGContext 实例调用它。这是一种贯穿 Swift 标准库的做法： 只要你实现了协议要求的几个少数方法，就可以“免费”收获这个协议通过扩展得到所有功能。</p>
<h4 data-id="heading-6">定制协议扩展</h4>
<p>通过扩展给协议添加的方法，并不作为协议约束的一部分。在某些情况下，这会导致出乎意料的结果。</p>
<p>只有协议目击者中的方法才能被动态派发到一个具体类型对应的实现，因为只有目击者中的信息在运行时是可用的。在泛型上下文环境中，调用协议中的非约束方法总是会被静态派发到协议扩展中的实现。</p>
<p>为了获得动态派发的行为，我们应该让 addCircle 成为协议约束的一部分。这样，在协议扩展中 addCircle 的实现就变成了协议约束的 <strong>默认实现</strong>。带有默认实现的协议方法在 Swift 社区中有时也叫做 <strong>定制点 (customization point)</strong>。实现协议的类型会收到一份方法的默认实现，并有权决定是否要对其进行覆盖。</p>
<h4 data-id="heading-7">协议组合</h4>
<p>协议可以被组合在一起。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">typealias</span> <span class="hljs-type">Codable</span> <span class="hljs-operator">=</span> <span class="hljs-type">Decodable</span> & <span class="hljs-type">Encodable</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">协议继承</h4>
<p>协议之间还可以是继承关系。实际上，<code>typealias Codable = Encodable & Decodable</code> 这种写法在语法上，和 <code>protocol Codable: Encodable & Decodable</code> 是完全一样的。只是别名的写法看上去稍微简洁了一点，它更明确地告诉我们：Codable <strong>仅仅</strong> 是这两个协议的组合，并没有在组合的结果里添加任何新的方法。</p>
<h3 data-id="heading-9">协议和关联类型</h3>
<p>有些协议需要约束的不仅仅是方法、属性和初始化方法，它们还希望和它相关的一些类型满足特定的条件。这就可以通过关联类型 (associated type) 来实现。</p>
<p>举个栗子，通过协议关联类型，重新实现一个小型的 UIKit 状态恢复机制。</p>
<p>在 UIKit 里，状态恢复需要读取视图控制器以及视图的架构，并在 app 挂起的时候将它们的状态序列化。当 App 下一次加载的时候，UIKit 会尝试恢复应用程序的状态。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">ViewController</span> </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">Restorable</span> </span>&#123;
  <span class="hljs-keyword">associatedtype</span> <span class="hljs-type">State</span>: <span class="hljs-type">Codable</span>
  <span class="hljs-keyword">var</span> state: <span class="hljs-type">State</span> &#123; <span class="hljs-keyword">get</span> <span class="hljs-keyword">set</span> &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建一个显示消息的视图控制器。这个视图控制器的状态由一个消息数组以及当前的滚定位置构成，我们把它定义成一个实现了 Codable 的内嵌类型：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MessagesVC</span>: <span class="hljs-title">ViewController</span>, <span class="hljs-title">Restorable</span> </span>&#123;  <span class="hljs-keyword">typealias</span> <span class="hljs-type">State</span> <span class="hljs-operator">=</span> <span class="hljs-type">MessagesState</span>  <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">MessagesState</span>: <span class="hljs-title">Codable</span> </span>&#123;    <span class="hljs-keyword">var</span> messgaes: [<span class="hljs-type">String</span>] <span class="hljs-operator">=</span> []    <span class="hljs-keyword">var</span> scrollPosition: <span class="hljs-type">CGFloat</span> <span class="hljs-operator">=</span> <span class="hljs-number">0</span>  &#125;  <span class="hljs-keyword">var</span> state: <span class="hljs-type">MessagesState</span> <span class="hljs-operator">=</span> <span class="hljs-type">MessgaesState</span>()&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">基于关联类型的条件化协议实现</h4>
<p>有些类型只有在特定条件下才会实现一个协议。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">Range</span>: <span class="hljs-title">Sequence</span>
<span class="hljs-title">where</span> <span class="hljs-title">Bound</span>: <span class="hljs-title">Strideable</span>, <span class="hljs-title">Bound</span>.<span class="hljs-title">Stride</span>: <span class="hljs-title">SignedInteger</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">存在体</h3>
<p>严格来说，在 Swift 中是不能把协议当作一个具体类型来使用的，它们只能用来约束泛型参数。但让人诧异的是，下面的代码却可以通过编译：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> <span class="hljs-type">Context：DrawingContext</span> <span class="hljs-operator">=</span> <span class="hljs-type">SVG</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们把协议当作具体类型使用的时候，编译器会为协议创建一个包装类型，叫做 <strong>存在体 (existential)</strong>。<code>let context:DrawingCon</code> 这种写法本质上就是类似 <code>let context: Any<DrawingContext></code> 这种写法的语法糖。尽管这种语法并不存在，编译器会创建一个 (32字节的) Any 盒子，并在其中为类型实现的每个协议添加一个 8 字节的协议目击者。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-type">MemoryLayout</span><<span class="hljs-keyword">Any</span>>.size <span class="hljs-comment">// 32</span>
<span class="hljs-type">MemoryLayout</span><<span class="hljs-type">DrawingContext</span>>.size <span class="hljs-comment">// 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为协议创建的这个盒子也叫做 <strong>存在体容器 (existential container)</strong>。这是编译器必须要做的事情，因为它需要在编译期确认类型的大小。不同的类型自身大小有差异 (例如：所有的类都是一个指针的大小，而结构体和枚举的大小则依赖他们的实际内容)，这些类型实现了一个协议的时候，把协议包装在存在体容器中可以让类型的尺寸保持固定，编译器也就能确定对象的内存布局了。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-type">MemoryLayout</span><<span class="hljs-type">Codable</span>>.size <span class="hljs-comment">// 48</span>
<span class="hljs-keyword">let</span> codables: [<span class="hljs-type">Codable</span>] <span class="hljs-operator">=</span> [<span class="hljs-type">Int</span>(<span class="hljs-number">42</span>), <span class="hljs-type">Double</span>(<span class="hljs-number">42</span>), <span class="hljs-string">"fourtytwo"</span>] <span class="hljs-comment">// 占用144(48 * 3)字节空间</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">存在体和关联类型</h4>
<p>在 Swift 5 里，存在体只针对那些没有关联类型和 Self 约束的协议。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> collections: [<span class="hljs-type">Collection</span>] <span class="hljs-operator">=</span> [<span class="hljs-string">"foo"</span>, [<span class="hljs-number">1</span>]]
<span class="hljs-comment">// 错误： 'Collection' 只能用作泛型参数约束</span>
<span class="hljs-comment">// 因为它包含了 Self 或关联类型约定。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们不能在不指定关联类型 <code>Element</code> 的情况下使用 Collection。</p>
<h3 data-id="heading-13">类型消除器</h3>
<p>尽管我们无法为带有 Self 或关联类型约束的协议创建存在体，但我们可以编写一个执行类似功能的函数，叫做：<strong>类型消除器 (type erasers)</strong>。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> seq <span class="hljs-operator">=</span> [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>].lazy.filter &#123; <span class="hljs-variable">$0</span> <span class="hljs-operator">></span> <span class="hljs-number">1</span> &#125;.map &#123; <span class="hljs-variable">$0</span> <span class="hljs-operator">*</span> <span class="hljs-number">2</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>seq</code> 的类型是 <code>LazyMapSequence<LazyFilterSequence<[Int]>, Int></code>。</p>
<p>我们会想要<strong>消除</strong>掉结果中类型的细节，只得到一个包含 Int 元素的序列就好了。可以用 <code>AnySequence</code> 隐藏掉原始的类型：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> anySeq <span class="hljs-operator">=</span> <span class="hljs-type">AnySequence</span>(seq)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>anySeq</code>  的类型就是 <code>AnySequence<Int></code>。尽管这看上去简单多了，并且用起来也和一个序列一样，但这样做也是有代价的：AnySequence 引入了额外的一层间接性，它比直接使用被隐藏的原始类型慢一些。</p>
<p>标准库为很多协议都提供了类型消除器，例如：<code>AnyCollection</code> 和 <code>AnyHashable</code>。</p>
<p>下面我们给之前定义的 <code>Restorable</code> 协议实现一个简单的类型消除器。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AnyRestorableBoxBase</span><<span class="hljs-title">State</span>: <span class="hljs-title">Codable</span>>: <span class="hljs-title">Restorable</span> </span>&#123;
  <span class="hljs-keyword">internal</span> <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;&#125;
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">var</span> state: <span class="hljs-type">State</span> &#123;
    <span class="hljs-keyword">get</span> &#123; <span class="hljs-built_in">fatalError</span>() &#125;
    <span class="hljs-keyword">set</span> &#123; <span class="hljs-built_in">fatalError</span>() &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AnyRestorableBox</span><<span class="hljs-title">R</span>: <span class="hljs-title">Restorable</span>>: <span class="hljs-title">AnyRestorableBoxBase</span><<span class="hljs-title">R</span>.<span class="hljs-title">State</span>> </span>&#123;
  <span class="hljs-keyword">var</span> r: <span class="hljs-type">R</span>
  int(<span class="hljs-keyword">_</span> r: <span class="hljs-type">R</span>) &#123;
    <span class="hljs-keyword">self</span>.r <span class="hljs-operator">=</span> r
  &#125;
  
  <span class="hljs-keyword">override</span> <span class="hljs-keyword">var</span> state: <span class="hljs-type">R</span>.<span class="hljs-type">State</span> &#123;
    <span class="hljs-keyword">get</span> &#123; <span class="hljs-keyword">return</span> r.state &#125;
    <span class="hljs-keyword">set</span> &#123; r.state <span class="hljs-operator">=</span> newValue &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AnyRestorable</span><<span class="hljs-title">State</span>: <span class="hljs-title">Codable</span>>: <span class="hljs-title">Restorable</span> </span>&#123;
  <span class="hljs-keyword">let</span> box: <span class="hljs-type">AnyRestorableBoxBase</span><<span class="hljs-type">State</span>>
<span class="hljs-function"><span class="hljs-keyword">init</span><<span class="hljs-type">R</span>>(<span class="hljs-keyword">_</span> <span class="hljs-params">r</span>: <span class="hljs-type">R</span>)</span> <span class="hljs-keyword">where</span> <span class="hljs-type">R</span>: <span class="hljs-type">Restorable</span>, <span class="hljs-type">R</span>.<span class="hljs-type">State</span> <span class="hljs-operator">==</span> <span class="hljs-type">State</span> &#123;
    <span class="hljs-keyword">self</span>.box <span class="hljs-operator">=</span> <span class="hljs-type">AnyRestorableBox</span>(r)
  &#125;
  
  <span class="hljs-keyword">var</span> state: <span class="hljs-type">State</span> &#123;
    <span class="hljs-keyword">get</span> &#123; <span class="hljs-keyword">return</span> box.state &#125;
    <span class="hljs-keyword">set</span> &#123; box.state <span class="hljs-operator">=</span> newValue &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">滞后于类型定义的协议实现</h3>
<p>Swift 中协议的一个主要特性就是一个类型对协议的实现可以之后滞后于类型定义本身。</p></div>  
</div>
            