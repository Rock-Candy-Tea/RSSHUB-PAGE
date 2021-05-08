
---
title: 'Swift必备Tips重点笔记'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=6395'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 21:40:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=6395'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>本章内容来自于喵神的Swift必备Tips，有兴趣的同学可以阅读原书，更加详细！</strong></p>
<p><strong>本章内容来自于喵神的Swift必备Tips，有兴趣的同学可以阅读原书，更加详细！</strong></p>
<p><strong>本章内容来自于喵神的Swift必备Tips，有兴趣的同学可以阅读原书，更加详细！</strong></p>
<h3 data-id="heading-0">@autoclosure 和 ??</h3>
<p><code>@autoclosure</code> 做的事情就是把一句表达式自动地封装成一个闭包 (closure)，这样有时候在语法上看起来就会非常漂亮。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">logIfTrue</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">predicate</span>: () -> <span class="hljs-type">Bool</span>)</span> &#123;
    <span class="hljs-keyword">if</span> predicate() &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"True"</span>)
    &#125;
&#125;

logIfTrue(&#123; <span class="hljs-keyword">return</span> <span class="hljs-number">2</span> <span class="hljs-operator">></span> <span class="hljs-number">1</span> &#125;)
<span class="hljs-comment">// 简化，可以去掉return</span>
logIfTrue(&#123;<span class="hljs-number">2</span> <span class="hljs-operator">></span> <span class="hljs-number">1</span>&#125;)
<span class="hljs-comment">// 简化，尾随闭包，省略括号</span>
logIfTrue&#123;<span class="hljs-number">2</span> <span class="hljs-operator">></span> <span class="hljs-number">1</span>&#125;
<span class="hljs-comment">// 但是不管哪种方式，要么是书写起来十分麻烦，要么是表达上不太清晰</span>

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">logIfTrue2</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">predicate</span>: <span class="hljs-keyword">@autoclosure</span> () -> <span class="hljs-type">Bool</span>)</span> &#123;
    <span class="hljs-keyword">if</span> predicate() &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"True"</span>)
    &#125;
&#125;
<span class="hljs-comment">// Swift 将会把 2 > 1 这个表达式自动转换为 () -> Bool。这样我们就得到了一个写法简单，表意清楚的式子。</span>
logIfTrue2(<span class="hljs-number">2</span> <span class="hljs-operator">></span> <span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>空合并运算符 ?? 可以用来快速地对 nil 进行条件判断。这个操作符可以判断输入并在当左侧的值是非 nil 的 Optional 值时返回其 value，当左侧是 nil 时返回右侧的值。</p>
<ul>
<li>a ?? b</li>
<li>a 是可选项</li>
<li>b 可以是可选项，也可以不是可选项</li>
<li>b 跟 a 的存储类型必须相同</li>
<li>如果 b 不是可选项，返回 a 时就会自动解包</li>
</ul>
<p>我们点进去 ?? 的定义可以看到两个版本：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">??<</span></span><span class="hljs-type">T</span><span class="hljs-operator">></span>(optional: <span class="hljs-type">T</span>?, defaultValue: <span class="hljs-keyword">@autoclosure</span> () -> <span class="hljs-type">T</span>?) -> <span class="hljs-type">T</span>?

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">??<</span></span><span class="hljs-type">T</span><span class="hljs-operator">></span>(optional: <span class="hljs-type">T</span>?, defaultValue: <span class="hljs-keyword">@autoclosure</span> () -> <span class="hljs-type">T</span>) -> <span class="hljs-type">T</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由此也能证明，<strong>返回的类型是否是可选类型是由 b 来决定的</strong>。</p>
<p>猜测一下 ?? 的实现：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">??<</span></span><span class="hljs-type">T</span><span class="hljs-operator">></span>(optional: <span class="hljs-type">T</span>?, defaultValue: <span class="hljs-keyword">@autoclosure</span> () -> <span class="hljs-type">T</span>) -> <span class="hljs-type">T</span> &#123;
    <span class="hljs-keyword">switch</span> <span class="hljs-keyword">optional</span> &#123;
        <span class="hljs-keyword">case</span> .<span class="hljs-type">Some</span>(<span class="hljs-keyword">let</span> value):
            <span class="hljs-keyword">return</span> value
        <span class="hljs-keyword">case</span> .<span class="hljs-type">None</span>:
            <span class="hljs-keyword">return</span> defaultValue()
        &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可能你会有疑问，为什么这里要使用 autoclosure，直接接受 T 作为参数并返回不行么，为何要用 <code>() -> T</code> 这样的形式包装一遍，岂不是画蛇添足？其实这正是 autoclosure 的一个最值得称赞的地方。如果我们直接使用 T，那么就意味着在 ?? 操作符真正取值之前，我们就必须准备好一个默认值传入到这个方法中，一般来说这不会有很大问题，<strong>但是如果这个默认值是通过一系列复杂计算得到的话，可能会成为浪费</strong> -- 因为其实如果 optional 不是 nil 的话，我们实际上是完全没有用到这个默认值，而会直接返回 optional 解包后的值的。<strong>这样的开销是完全可以避免的，方法就是将默认值的计算推迟到 optional 判定为 nil 之后。</strong></p>
<p>就这样，我们可以巧妙地绕过条件判断和强制转换，以很优雅的写法处理对 Optional 及默认值的取值了。最后要提一句的是，@autoclosure 并不支持带有输入参数的写法，也就是说只有形如 <code>() -> T</code> 的参数才能使用这个特性进行简化。</p>
<h3 data-id="heading-1">weak 和 unowned</h3>
<p>如果您是一直写 Objective-C 过来的，那么从表面的行为上来说 unowned 更像以前的 unsafe_unretained，而 weak 就是以前的 weak。用通俗的话说，就是 unowned 设置以后即使它原来引用的内容已经被释放了，它仍然会保持对被已经释放了的对象的一个 "无效的" 引用，它不能是 Optional 值，也不会被指向 nil。如果你尝试调用这个引用的方法或者访问成员属性的话，程序就会崩溃。而 weak 则友好一些，在引用的内容被释放后，标记为 weak 的成员将会自动地变成 nil (因此被标记为 @weak 的变量一定需要是 Optional 值)。</p>
<p>关于两者使用的选择，Apple 给我们的建议是<strong>如果能够确定在访问时不会已被释放的话，尽量使用 unowned，如果存在被释放的可能，那就选择用 weak</strong>。</p>
<p>日常工作中一般使用弱引用的最常见的场景有两个：</p>
<ul>
<li>设置 delegate 时</li>
<li>在 self 属性存储为闭包时，其中拥有对 self 引用时</li>
</ul>
<h3 data-id="heading-2">值类型和引用类型</h3>
<p>Swift 的类型分为值类型和引用类型两种，值类型在传递和赋值时将进行复制，而引用类型则只会使用引用对象的一个 "指向"。Swift 中的所有的内建类型都是值类型，不仅包括了传统意义像 Int，Bool 这些，甚至连 String，Array 以及 Dictionary 都是值类型的。这在程序设计上绝对算得上一个震撼的改动，因为据我所知现在流行的编程语言中，像数组和字典这样的类型，几乎清一色都是引用类型。</p>
<p>那么使用值类型有什么好处呢？相较于传统的引用类型来说，一个很显而易见的优势就是<strong>减少了堆上内存分配和回收的次数</strong>。首先我们需要知道，Swift 的值类型，特别是数组和字典这样的容器，在内存管理上经过了精心的设计。值类型的一个特点是在传递和赋值时进行复制，每次复制肯定会产生额外开销，但是在 Swift 中这个消耗被控制在了最小范围内，在没有必要复制的时候，值类型的复制都是不会发生的。也就是说，简单的赋值，参数的传递等等普通操作，虽然我们可能用不同的名字来回设置和传递值类型，但是在内存上它们都是同一块内容。</p>
<p>值类型在复制时，会将存储在其中的值类型一并进行复制，而对于其中的引用类型的话，则只复制一份引用。</p>
<p>虽然将数组和字典设计为值类型最大的考虑是为了线程安全，但是这样的设计在存储的元素或条目数量较少时，给我们带来了另一个优点，那就是非常高效，因为 "一旦赋值就不太会变化" 这种使用情景在 Cocoa 框架中是占有绝大多数的，这有效减少了内存的分配和回收。但是在少数情况下，我们显然也可能会在数组或者字典中存储非常多的东西，并且还要对其中的内容进行添加或者删除。在这时，Swift 内建的值类型的容器类型在每次操作时都需要复制一遍，即使是存储的都是引用类型，在复制时我们还是需要存储大量的引用，这个开销就变得不容忽视了。幸好我们还有 Cocoa 中的引用类型的容器类来对应这种情况，那就是 NSMutableArray 和 NSMutableDictionary。</p>
<p>所以，在使用数组和字典时的最佳实践应该是，<strong>按照具体的数据规模和操作特点来决定到时是使用值类型的容器还是引用类型的容器</strong>：在需要处理大量数据并且频繁操作 (增减) 其中元素时，选择 NSMutableArray 和 NSMutableDictionary 会更好，而对于容器内条目小而容器本身数目多的情况，应该使用 Swift 语言内建的 Array 和 Dictionary。</p>
<h3 data-id="heading-3">重载和自定义操作符</h3>
<p>对于Swift中已经存在的操作符，我们可以通过变换参数进行重载</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Vector2D</span> </span>&#123;
    <span class="hljs-keyword">var</span> x <span class="hljs-operator">=</span> <span class="hljs-number">0.0</span>
    <span class="hljs-keyword">var</span> y <span class="hljs-operator">=</span> <span class="hljs-number">0.0</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">+</span>(<span class="hljs-params">left</span>: <span class="hljs-type">Vector2D</span>, <span class="hljs-params">right</span>: <span class="hljs-type">Vector2D</span>)</span> -> <span class="hljs-type">Vector2D</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-type">Vector2D</span>(x: left.x <span class="hljs-operator">+</span> right.x, y: left.y <span class="hljs-operator">+</span> right.y)
&#125;

<span class="hljs-keyword">let</span> v1 <span class="hljs-operator">=</span> <span class="hljs-type">Vector2D</span>(x: <span class="hljs-number">2.0</span>, y: <span class="hljs-number">3.0</span>)
<span class="hljs-keyword">let</span> v2 <span class="hljs-operator">=</span> <span class="hljs-type">Vector2D</span>(x: <span class="hljs-number">1.0</span>, y: <span class="hljs-number">4.0</span>)
<span class="hljs-keyword">let</span> v3 <span class="hljs-operator">=</span> v1 <span class="hljs-operator">+</span> v2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于我们自定义的操作符，需要先对其进行声明，告诉编译器这个符号其实是一个操作符</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">/// 声明操作符</span>
<span class="hljs-comment">// 定义优先级组</span>
<span class="hljs-keyword">precedencegroup</span> <span class="hljs-title">DotProductPrecedence</span> &#123;
    <span class="hljs-keyword">associativity</span>: <span class="hljs-keyword">none</span>// 结合律方向:<span class="hljs-keyword">left</span>, <span class="hljs-keyword">right</span> or <span class="hljs-keyword">none</span>
    <span class="hljs-keyword">higherThan</span>: <span class="hljs-type">MultiplicationPrecedence</span>// 优先级,比加法运算高
  <span class="hljs-keyword">assignment</span>: <span class="hljs-keyword">false</span>// <span class="hljs-keyword">true</span>=赋值运算符,<span class="hljs-keyword">false</span>=非赋值运算符
&#125;
<span class="hljs-comment">// infix 表示要定义的是一个中位操作符，即前后都是输入；其他的修饰子还包括 prefix 和 postfix</span>
<span class="hljs-keyword">infix</span> <span class="hljs-keyword">operator</span> <span class="hljs-title">+*</span>: <span class="hljs-type">DotProductPrecedence</span>

<span class="hljs-comment">/// 重载操作符</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">+*</span> (<span class="hljs-params">left</span>: <span class="hljs-type">Vector2D</span>, <span class="hljs-params">right</span>: <span class="hljs-type">Vector2D</span>)</span> -> <span class="hljs-type">Double</span> &#123;
    <span class="hljs-keyword">return</span> left.x <span class="hljs-operator">*</span> right.x <span class="hljs-operator">+</span> left.y <span class="hljs-operator">*</span> right.y
&#125;

<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Vector2D</span> </span>&#123;
    <span class="hljs-keyword">var</span> x <span class="hljs-operator">=</span> <span class="hljs-number">0.0</span>
    <span class="hljs-keyword">var</span> y <span class="hljs-operator">=</span> <span class="hljs-number">0.0</span>
&#125;

<span class="hljs-keyword">let</span> v1 <span class="hljs-operator">=</span> <span class="hljs-type">Vector2D</span>(x: <span class="hljs-number">2.0</span>, y: <span class="hljs-number">3.0</span>)
<span class="hljs-keyword">let</span> v2 <span class="hljs-operator">=</span> <span class="hljs-type">Vector2D</span>(x: <span class="hljs-number">1.0</span>, y: <span class="hljs-number">4.0</span>)
<span class="hljs-keyword">let</span> result <span class="hljs-operator">=</span> v1 <span class="hljs-operator">+*</span> v2
<span class="hljs-built_in">print</span>(result) <span class="hljs-comment">// 14.0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Swift 的操作符是<strong>不能定义在局部域</strong>中的，因为至少会希望在能在全局范围使用你的操作符，否则操作符也就失去意义了。</li>
<li>来自不同 module 的操作符是有可能冲突的，这对于库开发者来说是需要特别注意的地方。如果库中的操作符冲突的话，使用者是无法像解决类型名冲突那样通过指定库名字来进行调用的。因此<strong>在重载或者自定义操作符时，应当尽量将其作为其他某个方法的 "简便写法"</strong>，而避免在其中实现大量逻辑或者提供独一无二的功能。这样即使出现了冲突，使用者也还可以通过方法名调用的方式使用你的库。</li>
<li><strong>运算符的命名也应当尽量明了，避免歧义和可能的误解</strong>。因为一个不被公认的操作符是存在冲突风险和理解难度的，所以我们不应该滥用这个特性。</li>
</ul>
<h3 data-id="heading-4">inout 函数参数修饰符</h3>
<ul>
<li>可以用 <code>inout</code> 定义一个输入输出参数：可以在函数内部修改外部实参的值。</li>
<li>可变参数不能标记为inout</li>
<li>inout参数不能有默认值</li>
<li>inout参数只能传入可以被多次赋值的</li>
<li>inout 的本质是地址传递（引用传递）</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">var</span> number <span class="hljs-operator">=</span> <span class="hljs-number">10</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">add</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">num</span>: <span class="hljs-keyword">inout</span> <span class="hljs-type">Int</span>)</span> &#123;
num <span class="hljs-operator">=</span> <span class="hljs-number">20</span>
&#125;
add(<span class="hljs-operator">&</span>number)

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">swapValues</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">v1</span>: <span class="hljs-keyword">inout</span> <span class="hljs-type">Int</span>, <span class="hljs-keyword">_</span> <span class="hljs-params">v2</span>: <span class="hljs-keyword">inout</span> <span class="hljs-type">Int</span>)</span> &#123;
  <span class="hljs-keyword">let</span> tmp <span class="hljs-operator">=</span> v1
  v1 <span class="hljs-operator">=</span> v2
  v2 <span class="hljs-operator">=</span> tmp
&#125;
<span class="hljs-keyword">var</span> num1 <span class="hljs-operator">=</span> <span class="hljs-number">10</span>; <span class="hljs-keyword">var</span> num2 <span class="hljs-operator">=</span> <span class="hljs-number">20</span>
swapValues(<span class="hljs-operator">&</span>num1, <span class="hljs-operator">&</span>num2)

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">swapValues</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">v1</span>: <span class="hljs-keyword">inout</span> <span class="hljs-type">Int</span>, <span class="hljs-keyword">_</span> <span class="hljs-params">v2</span>: <span class="hljs-keyword">inout</span> <span class="hljs-type">Int</span>)</span> &#123;
  (v1, v2) <span class="hljs-operator">=</span> (v2, v1)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">typealias 类型别名</h3>
<p>typealias 是用来为已经存在的类型重新定义名字的，通过命名，可以使代码变得更加清晰。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">distance</span>(<span class="hljs-params">from</span> <span class="hljs-params">point</span>: <span class="hljs-type">CGPoint</span>, <span class="hljs-params">to</span> <span class="hljs-params">anotherPoint</span>: <span class="hljs-type">CGPoint</span>)</span> -> <span class="hljs-type">Double</span> &#123;
    <span class="hljs-keyword">let</span> dx <span class="hljs-operator">=</span> <span class="hljs-type">Double</span>(anotherPoint.x <span class="hljs-operator">-</span> point.x)
    <span class="hljs-keyword">let</span> dy <span class="hljs-operator">=</span> <span class="hljs-type">Double</span>(anotherPoint.y <span class="hljs-operator">-</span> point.y)
    <span class="hljs-keyword">return</span> sqrt(dx <span class="hljs-operator">*</span> dx <span class="hljs-operator">+</span> dy <span class="hljs-operator">*</span> dy)
&#125;

<span class="hljs-keyword">let</span> origin: <span class="hljs-type">CGPoint</span> <span class="hljs-operator">=</span> <span class="hljs-type">CGPoint</span>(x: <span class="hljs-number">0</span>, y: <span class="hljs-number">0</span>)
<span class="hljs-keyword">let</span> point: <span class="hljs-type">CGPoint</span> <span class="hljs-operator">=</span> <span class="hljs-type">CGPoint</span>(x: <span class="hljs-number">1</span>, y: <span class="hljs-number">1</span>)

<span class="hljs-keyword">let</span> d: <span class="hljs-type">Double</span> <span class="hljs-operator">=</span>  distance(from: origin, to: point)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然在数学上和最后的程序运行上都没什么问题，但是阅读和维护的时候总是觉得有哪里不对。因为我们没有将数学抽象和实际问题结合起来，使得在阅读代码时我们还需要在大脑中进行一次额外的转换：CGPoint 代表一个点，而这个点就是我们在定义的坐标系里的位置；Double 是一个数字，它代表两个点之间的距离。</p>
<p>如果我们使用 typealias，就可以将这种转换直接写在代码里，从而减轻阅读和维护的负担：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">import</span> UIKit

<span class="hljs-keyword">typealias</span> <span class="hljs-type">Location</span> <span class="hljs-operator">=</span> <span class="hljs-type">CGPoint</span>
<span class="hljs-keyword">typealias</span> <span class="hljs-type">Distance</span> <span class="hljs-operator">=</span> <span class="hljs-type">Double</span>

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">distance</span>(<span class="hljs-params">from</span> <span class="hljs-params">location</span>: <span class="hljs-type">Location</span>,
    <span class="hljs-params">to</span> <span class="hljs-params">anotherLocation</span>: <span class="hljs-type">Location</span>)</span> -> <span class="hljs-type">Distance</span> &#123;
        <span class="hljs-keyword">let</span> dx <span class="hljs-operator">=</span> <span class="hljs-type">Distance</span>(location.x <span class="hljs-operator">-</span> anotherLocation.x)
        <span class="hljs-keyword">let</span> dy <span class="hljs-operator">=</span> <span class="hljs-type">Distance</span>(location.y <span class="hljs-operator">-</span> anotherLocation.y)
        <span class="hljs-keyword">return</span> sqrt(dx <span class="hljs-operator">*</span> dx <span class="hljs-operator">+</span> dy <span class="hljs-operator">*</span> dy)
&#125;

<span class="hljs-keyword">let</span> origin: <span class="hljs-type">Location</span> <span class="hljs-operator">=</span> <span class="hljs-type">Location</span>(x: <span class="hljs-number">0</span>, y: <span class="hljs-number">0</span>)
<span class="hljs-keyword">let</span> point: <span class="hljs-type">Location</span> <span class="hljs-operator">=</span> <span class="hljs-type">Location</span>(x: <span class="hljs-number">1</span>, y: <span class="hljs-number">1</span>)

<span class="hljs-keyword">let</span> d: <span class="hljs-type">Distance</span> <span class="hljs-operator">=</span> distance(from: origin, to: point)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在别名中引入泛型</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">typealias</span> <span class="hljs-type">Worker</span><<span class="hljs-type">T</span>> <span class="hljs-operator">=</span> <span class="hljs-type">Person</span><<span class="hljs-type">T</span>>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span><<span class="hljs-title">T</span>> </span>&#123;&#125;
<span class="hljs-keyword">typealias</span> <span class="hljs-type">WorkId</span> <span class="hljs-operator">=</span> <span class="hljs-type">String</span>
<span class="hljs-keyword">typealias</span> <span class="hljs-type">Worker</span> <span class="hljs-operator">=</span> <span class="hljs-type">Person</span><<span class="hljs-type">WorkId</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">associatedtype 关联类型</h3>
<p>关联类型为协议中的某个类型提供了一个占位符名称，其代表的实际类型在协议被遵循时才会被指定。关联类型通过 <code>associatedtype</code> 关键字来指定。</p>
<p>定义一个协议时，声明一个或多个关联类型作为协议定义的一部分将会非常有用。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">Food</span> </span>&#123; &#125;
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Meat</span>: <span class="hljs-title">Food</span> </span>&#123; &#125;
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Grass</span>: <span class="hljs-title">Food</span> </span>&#123; &#125;

<span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-keyword">associatedtype</span> <span class="hljs-type">F</span>: <span class="hljs-type">Food</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">eat</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">food</span>: <span class="hljs-type">F</span>)</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Tiger</span>: <span class="hljs-title">Animal</span> </span>&#123;
<span class="hljs-comment">// 只要实现了正确类型的eat，F的类型就可以被推断出来，所以我们也不需要显式地写明F</span>
<span class="hljs-comment">// typealias F = Meat</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">eat</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">food</span>: <span class="hljs-type">Meat</span>)</span> &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"eat <span class="hljs-subst">\(meat)</span>"</span>)
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Sheep</span>: <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">eat</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">food</span>: <span class="hljs-type">Grass</span>)</span> &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"eat <span class="hljs-subst">\(food)</span>"</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过在添加 associatedtype 后，Animal 协议就不能被当作独立的类型使用了。</p>
<p>这是因为 Swift 需要在编译时确定所有类型，这里因为 Animal 包含了一个不确定的类型，所以随着 Animal 本身类型的变化，其中的 F 将无法确定 (试想一下如果在这个函数内部调用 eat 的情形，你将无法指定 eat 参数的类型)。在一个协议加入了像是 associatedtype 或者 Self 的约束后，它将<strong>只能被用为泛型约束，而不能作为独立类型的占位使用，也失去了动态派发的特性</strong>。也就是说，这种情况下，我们需要将函数改写为泛型：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">isDangerous</span><<span class="hljs-type">T</span>: <span class="hljs-type">Animal</span>>(<span class="hljs-params">animal</span>: <span class="hljs-type">T</span>)</span> -> <span class="hljs-type">Bool</span> &#123;
    <span class="hljs-keyword">if</span> animal <span class="hljs-keyword">is</span> <span class="hljs-type">Tiger</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;
&#125;

isDangerous(animal: <span class="hljs-type">Tiger</span>()) <span class="hljs-comment">// true</span>
isDangerous(animal: <span class="hljs-type">Sheep</span>()) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">Associated Object 关联对象</h3>
<p>得益于 Objective-C 的运行时和 Key-Value Coding 的特性，我们可以在运行时向一个对象添加值存储。而在使用 Category 扩展现有的类的功能的时候，直接添加实例变量这种行为是不被允许的，这时候一般就使用 property 配合 Associated Object 的方式，将一个对象 “关联” 到已有的要扩展的对象上。进行关联后，在对这个目标对象访问的时候，从外界看来，就似乎是直接在通过属性访问对象的实例变量一样，可以非常方便。</p>
<p>在 Swift 中这样的方法依旧有效，只不过在写法上可能有些不同。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// MyClass.swift</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;
&#125;

<span class="hljs-comment">// MyClassExtension.swift</span>
<span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> key: <span class="hljs-type">Void</span>?

<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">MyClass</span> </span>&#123;
    <span class="hljs-keyword">var</span> title: <span class="hljs-type">String</span>? &#123;
        <span class="hljs-keyword">get</span> &#123;
            <span class="hljs-keyword">return</span> objc_getAssociatedObject(<span class="hljs-keyword">self</span>, <span class="hljs-operator">&</span>key) <span class="hljs-keyword">as?</span> <span class="hljs-type">String</span>
        &#125;

        <span class="hljs-keyword">set</span> &#123;
            objc_setAssociatedObject(<span class="hljs-keyword">self</span>,
                <span class="hljs-operator">&</span>key, newValue,
                .<span class="hljs-type">OBJC_ASSOCIATION_RETAIN_NONATOMIC</span>)
        &#125;
    &#125;
&#125;


<span class="hljs-comment">// 测试</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">printTitle</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">input</span>: <span class="hljs-type">MyClass</span>)</span> &#123;
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> title <span class="hljs-operator">=</span> input.title &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"Title: <span class="hljs-subst">\(title)</span>"</span>)
    &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"没有设置"</span>)
    &#125;
&#125;

<span class="hljs-keyword">let</span> a <span class="hljs-operator">=</span> <span class="hljs-type">MyClass</span>()
printTitle(a)
a.title <span class="hljs-operator">=</span> <span class="hljs-string">"Swifter.tips"</span>
printTitle(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">初始化方法顺序</h3>
<p>与 Objective-C 不同，Swift 的初始化方法需要保证类型的所有属性都被初始化。所以初始化方法的调用顺序就很有讲究。在某个类的子类中，初始化方法里语句的顺序并不是随意的，我们需要保证在当前子类实例的成员初始化完成后才能调用父类的初始化方法。</p>
<h3 data-id="heading-9">协议和类方法中的 Self</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">IntervalType</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">clamp</span>(<span class="hljs-params">intervalToClamp</span>: <span class="hljs-keyword">Self</span>)</span> -> <span class="hljs-keyword">Self</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个 IntervalType 的协议定义了一个方法，接受实现该协议的自身的类型，并返回一个同样的类型。</p>
<p>这么定义是因为协议其实本身是没有自己的上下文类型信息的，在声明协议的时候，我们并不知道最后究竟会是什么样的类型来实现这个协议，Swift 中也不能在协议中定义泛型进行限制。而在声明协议时，我们希望在协议中使用的类型就是实现这个协议本身的类型的话，就需要使用 Self 进行指代。</p>
<p>在这种情况下，Self 不仅指代的是实现该协议的类型本身，也包括了这个类型的子类。</p>
<p>实际实现的时候需要稍微转一个弯，我们需要通过一个和当前上下文无关的，又能够指代当前类型的方式进行初始化。我们可以使用 <code>type(of:)</code> 来获取对象类型，通过它也可以进一步进行初始化，以保证方法与当前类型上下文无关</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">Copyable</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">copy</span>()</span> -> <span class="hljs-keyword">Self</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">copy</span>()</span> -> <span class="hljs-keyword">Self</span> &#123;
    <span class="hljs-keyword">let</span> result <span class="hljs-operator">=</span> <span class="hljs-built_in">type</span>(of: <span class="hljs-keyword">self</span>).<span class="hljs-keyword">init</span>()
    result.num <span class="hljs-operator">=</span> num
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>单单是这样还是无法通过编译，编译器提示我们如果想要构建一个 Self 类型的对象的话，<strong>需要有 required 关键字修饰的初始化方法</strong>，这是因为 Swift 必须保证当前类和其子类都能响应这个 init 方法。另一个解决的方案是<strong>在当前类类的声明前添加 final 关键字，告诉编译器我们不再会有子类来继承这个类型</strong>。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span>: <span class="hljs-title">Copyable</span> </span>&#123;

    <span class="hljs-keyword">var</span> num <span class="hljs-operator">=</span> <span class="hljs-number">1</span>

    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">copy</span>()</span> -> <span class="hljs-keyword">Self</span> &#123;
        <span class="hljs-keyword">let</span> result <span class="hljs-operator">=</span> <span class="hljs-built_in">type</span>(of: <span class="hljs-keyword">self</span>).<span class="hljs-keyword">init</span>()
        result.num <span class="hljs-operator">=</span> num
        <span class="hljs-keyword">return</span> result
    &#125;

    <span class="hljs-keyword">required</span> <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">单例</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyManager</span>  </span>&#123;
    <span class="hljs-keyword">static</span> <span class="hljs-keyword">let</span> shared <span class="hljs-operator">=</span> <span class="hljs-type">MyManager</span>()
    <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种写法不仅简洁，而且保证了单例的独一无二。在初始化类变量的时候，Apple 将会把这个初始化包装在一次 swift_once_block_invoke 中，以保证它的唯一性。不仅如此，对于所有的全局变量，Apple 都会在底层使用这个类似 dispatch_once 的方式来确保只以 lazy 的方式初始化一次。</p>
<blockquote>
<p>dispatch_once 在 swift3 被移除了</p>
</blockquote>
<p>另外，我们在这个类型中加入了一个私有的初始化方法，来覆盖默认的公开初始化方法，这让项目中的其他地方不能够通过 init 来生成自己的 MyManager 实例，也保证了类型单例的唯一性。如果你需要的是类似 default 的形式的单例 (也就是说这个类的使用者可以创建自己的实例) 的话，可以去掉这个私有的 init 方法。</p>
<p><strong>swift 单例的实现，是如何保证线程安全的？</strong></p>
<p>let 定义的属性本身就是线程安全的，同时 static 定义的是一个 class constant，拥有全局作用域和懒加载特性。</p>
<h3 data-id="heading-11">String 和 NSString 的区别和联系</h3>
<p>String 和 NSString 在使用的时候是可以无缝转换的，但是也是有一定区别的，本质上，String 是值类型，NSString 是引用类型。</p>
<p>在 Swift 中尽可能的话还是使用原生的 String 类型。</p>
<ul>
<li>因为现在所有的 Cocoa 框架都能接收和也能返回 String 类型，所以没有必要特地转换</li>
<li>“因为在 Swift 中 String 是 struct，相比起 NSObject 的 NSString 类来说，更切合字符串的 "不变" 这一特性。通过配合常量赋值 (let) ，这种不变性在多线程编程时就非常重要了，它从原理上将程序员从内存访问和操作顺序的担忧中解放出来。另外，在不触及 NSString 特有操作和动态特性的时候，使用 String 的方法，在性能上也会有所提升。</li>
<li>因为 String 实现了 Collection 这样的协议，因此有些 Swift 的语法特性只有 String 才能使用，而 NSString 是没有的。</li>
<li>String 字符串之间的拼接比 NSString 方便</li>
<li>String 独有的字符串插值功能</li>
</ul>
<p>使用 NSString 的情况：</p>
<ul>
<li>通过 Range 截取字符串的时候，使用 NSString 更加方便一点</li>
</ul>
<h3 data-id="heading-12">条件编译</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">#if</span> <span class="hljs-operator"><</span>condition<span class="hljs-operator">></span>

<span class="hljs-keyword">#elseif</span> <span class="hljs-operator"><</span>condition<span class="hljs-operator">></span>

<span class="hljs-keyword">#else</span>

<span class="hljs-keyword">#endif</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这几个表达式里的 condition 并不是任意的。Swift 内建了几种平台和架构的组合，来帮助我们为不同的平台编译不同的代码</p>





















<table><thead><tr><th>方法</th><th>可选参数</th></tr></thead><tbody><tr><td>os()</td><td>macOS, iOS, tvOS, watchOS, Linux</td></tr><tr><td>arch()</td><td>x84_64, arm, arm64, i386</td></tr><tr><td>swift()</td><td>>= 某个版本</td></tr></tbody></table>
<p>另外对于 arch() 的参数需要说明的是 arm 和 arm64 两项分别对应 32 位 CPU 和 64 位 CPU 的真机情况，而对于模拟器，相应地 32 位设备的模拟器和 64 位设备的模拟器所对应的分别是 i386 和 x86_64，它们也是需要分开对待的。</p>
<p>另一种方式是对自定义的符号进行条件编译，比如我们需要使用同一个 target 完成同一个 app 的收费版和免费版两个版本，并且希望在点击某个按钮时收费版本执行功能，而免费版本弹出提示的话，可以使用类似下面的方法：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@IBAction</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">someButtonPressed</span>(<span class="hljs-params">sender</span>: <span class="hljs-type">AnyObject</span>!)</span> &#123;
    <span class="hljs-keyword">#if</span> <span class="hljs-type">FREE_VERSION</span>
        <span class="hljs-comment">// 弹出购买提示，导航至商店等</span>
    <span class="hljs-keyword">#else</span>
        <span class="hljs-comment">// 实际功能</span>
    <span class="hljs-keyword">#endif</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里我们用 FREE_VERSION 这个编译符号来代表免费版本。为了使之有效，我们需要在项目的编译选项中进行设置，在项目的 Build Settings 中，找到 Swift Compiler - Custom Flags，并在其中的 Other Swift Flags 加上 -D FREE_VERSION 就可以了。</p>
<h3 data-id="heading-13">GCD延时调用</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">import</span> Foundation

<span class="hljs-keyword">typealias</span> <span class="hljs-type">Task</span> <span class="hljs-operator">=</span> (<span class="hljs-keyword">_</span> cancel : <span class="hljs-type">Bool</span>) -> <span class="hljs-type">Void</span>

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">delay</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">time</span>: <span class="hljs-type">TimeInterval</span>, <span class="hljs-params">task</span>: <span class="hljs-keyword">@escaping</span> ()->())</span> ->  <span class="hljs-type">Task</span>? &#123;

    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">dispatch_later</span>(<span class="hljs-params">block</span>: <span class="hljs-keyword">@escaping</span> ()->())</span> &#123;
        <span class="hljs-keyword">let</span> t <span class="hljs-operator">=</span> <span class="hljs-type">DispatchTime</span>.now() <span class="hljs-operator">+</span> time
        <span class="hljs-type">DispatchQueue</span>.main.asyncAfter(deadline: t, execute: block)
    &#125;

    <span class="hljs-keyword">var</span> closure: (()-><span class="hljs-type">Void</span>)<span class="hljs-operator">?</span> <span class="hljs-operator">=</span> task
    <span class="hljs-keyword">var</span> result: <span class="hljs-type">Task</span>?

    <span class="hljs-keyword">let</span> delayedClosure: <span class="hljs-type">Task</span> <span class="hljs-operator">=</span> &#123;
        cancel <span class="hljs-keyword">in</span>
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> internalClosure <span class="hljs-operator">=</span> closure &#123;
            <span class="hljs-keyword">if</span> (cancel <span class="hljs-operator">==</span> <span class="hljs-literal">false</span>) &#123;
                <span class="hljs-type">DispatchQueue</span>.main.async(execute: internalClosure)
            &#125;
        &#125;
        closure <span class="hljs-operator">=</span> <span class="hljs-literal">nil</span>
        result <span class="hljs-operator">=</span> <span class="hljs-literal">nil</span>
    &#125;

    result <span class="hljs-operator">=</span> delayedClosure

    dispatch_later &#123;
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> delayedClosure <span class="hljs-operator">=</span> result &#123;
            delayedClosure(<span class="hljs-literal">false</span>)
        &#125;
    &#125;

    <span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">cancel</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">task</span>: <span class="hljs-type">Task</span>?)</span> &#123;
    task<span class="hljs-operator">?</span>(<span class="hljs-literal">true</span>)
&#125;

<span class="hljs-keyword">let</span> task <span class="hljs-operator">=</span> delay(<span class="hljs-number">5</span>) &#123; <span class="hljs-built_in">print</span>(<span class="hljs-string">"拨打 110"</span>) &#125;

<span class="hljs-comment">// 仔细想一想..</span>
<span class="hljs-comment">// 还是取消为妙..</span>
cancel(task)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">KeyPath 和 KVO</h3>
<p>在 Swift 中我们也是可以使用 KVO 的，而且在 Swift 4 中，结合 KeyPath，Apple 为我们提供了非常漂亮的一套新的 API。不过 KVO 仅限于在 NSObject 的子类中，这是可以理解的，因为 KVO 是基于 KVC (Key-Value Coding) 以及动态派发技术实现的，而这些东西都是 Objective-C 运行时的概念。另外由于 Swift 为了效率，默认禁用了动态派发，因此想用 Swift 来实现 KVO，我们还需要做额外的工作，那就是将想要观测的对象标记为 <code>dynamic</code> 和 <code>@objc</code>。</p>
<p>Swift4之前：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span>: <span class="hljs-title">NSObject</span> </span>&#123;
    <span class="hljs-keyword">@objc</span> <span class="hljs-keyword">dynamic</span> <span class="hljs-keyword">var</span> date <span class="hljs-operator">=</span> <span class="hljs-type">Date</span>()
&#125;

<span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> myContext <span class="hljs-operator">=</span> <span class="hljs-number">0</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class</span>: <span class="hljs-title">NSObject</span> </span>&#123;

    <span class="hljs-keyword">var</span> myObject: <span class="hljs-type">MyClass</span>!

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.<span class="hljs-keyword">init</span>()
        myObject <span class="hljs-operator">=</span> <span class="hljs-type">MyClass</span>()
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"初始化 MyClass，当前日期: <span class="hljs-subst">\(myObject.date)</span>"</span>)
        myObject.addObserver(<span class="hljs-keyword">self</span>,
            forKeyPath: <span class="hljs-string">"date"</span>,
            options: .new,
            context: <span class="hljs-operator">&</span>myContext)

        delay(<span class="hljs-number">3</span>) &#123;
<span class="hljs-keyword">self</span>.myObject.date <span class="hljs-operator">=</span> <span class="hljs-type">Date</span>()
        &#125;
    &#125;

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">observeValue</span>(<span class="hljs-params">forKeyPath</span> <span class="hljs-params">keyPath</span>: <span class="hljs-type">String</span>?,
                            <span class="hljs-params">of</span> <span class="hljs-params">object</span>: <span class="hljs-keyword">Any</span><span class="hljs-operator">?</span>,
                               <span class="hljs-params">change</span>: [<span class="hljs-params">NSKeyValueChangeKey</span> : <span class="hljs-keyword">Any</span>]<span class="hljs-operator">?</span>,
                              <span class="hljs-params">context</span>: <span class="hljs-type">UnsafeMutableRawPointer</span>?)</span>
    &#123;
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> change <span class="hljs-operator">=</span> change, context <span class="hljs-operator">==</span> <span class="hljs-operator">&</span>myContext &#123;
            <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> newDate <span class="hljs-operator">=</span> change[.newKey] <span class="hljs-keyword">as?</span> <span class="hljs-type">Date</span> &#123;
                <span class="hljs-built_in">print</span>(<span class="hljs-string">"MyClass 日期发生变化 <span class="hljs-subst">\(newDate)</span>"</span>)
            &#125;
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">let</span> obj <span class="hljs-operator">=</span> <span class="hljs-type">Class</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Swift4中引入了新的 KeyPath 的表达方式，现在，对于类型 Foo 中的变量 <code>bar: Bar</code>，对应的 KeyPath 可以写为 <code>\Foo.bar</code>。在这种表达方式下，KeyPath 将通过泛型的方式带有类型信息，比如上的 KeyPath 的类型为 <code>KeyPath<Foo, Bar></code>。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span>: <span class="hljs-title">NSObject</span> </span>&#123;
    <span class="hljs-keyword">@objc</span> <span class="hljs-keyword">dynamic</span> <span class="hljs-keyword">var</span> date <span class="hljs-operator">=</span> <span class="hljs-type">Date</span>()
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AnotherClass</span>: <span class="hljs-title">NSObject</span> </span>&#123;
    <span class="hljs-keyword">var</span> myObject: <span class="hljs-type">MyClass</span>!
    <span class="hljs-keyword">var</span> observation: <span class="hljs-type">NSKeyValueObservation</span>?
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.<span class="hljs-keyword">init</span>()
        myObject <span class="hljs-operator">=</span> <span class="hljs-type">MyClass</span>()
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"初始化 AnotherClass，当前日期: <span class="hljs-subst">\(myObject.date)</span>"</span>)

        observation <span class="hljs-operator">=</span> myObject.observe(\<span class="hljs-type">MyClass</span>.date, options: [.new]) &#123; (<span class="hljs-keyword">_</span>, change) <span class="hljs-keyword">in</span>
            <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> newDate <span class="hljs-operator">=</span> change.newValue &#123;
                <span class="hljs-built_in">print</span>(<span class="hljs-string">"AnotherClass 日期发生变化 <span class="hljs-subst">\(newDate)</span>"</span>)
            &#125;
        &#125;

        delay(<span class="hljs-number">1</span>) &#123; <span class="hljs-keyword">self</span>.myObject.date <span class="hljs-operator">=</span> <span class="hljs-type">Date</span>() &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相较于原来 Objective-C 方式的处理，<strong>使用 Swift 4 KeyPath 的好处显而易见</strong>：</p>
<ol>
<li>首先，设定观察和处理观察的代码被放在了一起，让代码维护难度降低很多；</li>
<li>其次在处理时我们得到的是类型安全的结果，而不是从字典中取值；</li>
<li>最后，我们不再需要使用 context 来区分是哪一个观察量发生了变化，而且使用 observation 来持有观察者，这可以让我们从麻烦的内存管理中解放出来，观察者的生命周期将随着 AnotherClass 的释放而结束。对比一下在 Class 中，我们还需要在实例完成任务时找好时机停止观察，否则将造成内存泄漏。</li>
</ol>
<p>不过在 Swift 中使用 KVO 还是有有<strong>两个显而易见的问题</strong>：</p>
<ol>
<li>
<p>显然 Swift 的 KVO 需要依赖的东西比原来多。在 Objective-C 中我们几乎可以没有限制地对所有满足 KVC 的属性进行监听，而现在我们需要属性有 dynamic 和 @objc 进行修饰。大多数情况下，我们想要观察的类不包含这两个修饰，并且有时候我们很可能也无法修改想要观察的类的源码。遇到这样的情况的话，一个可能可行的方案是继承这个类并且将需要观察的属性使用 dynamic 和 @objc 进行重写。</p>
</li>
<li>
<p>对于那些非 NSObject 的 Swift 类型怎么办。因为 Swift 类型并没有通过 KVC 进行实现，所以更不用谈什么对属性进行 KVO 了。对于 Swift 类型，语言中现在暂时还没有原生的类似 KVO 的观察机制。我们可能只能通过<strong>属性观察</strong>来实现一套自己的类似替代了。</p>
</li>
</ol>
<h3 data-id="heading-15">尾递归</h3>
<p>一般对于递归，解决栈溢出的一个好方法是采用尾递归的写法。顾名思义，尾递归就是让函数里的最后一个动作是一个函数调用的形式，这个调用的返回值将直接被当前函数返回，从而避免在栈上保存状态。这样一来程序就可以更新最后的栈帧，而不是新建一个，来避免栈溢出的发生。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">tailSum</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">n</span>: <span class="hljs-type">UInt</span>)</span> -> <span class="hljs-type">UInt</span> &#123;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">sumInternal</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">n</span>: <span class="hljs-type">UInt</span>, <span class="hljs-params">current</span>: <span class="hljs-type">UInt</span>)</span> -> <span class="hljs-type">UInt</span> &#123;
        <span class="hljs-keyword">if</span> n <span class="hljs-operator">==</span> <span class="hljs-number">0</span> &#123;
            <span class="hljs-keyword">return</span> current
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> sumInternal(n <span class="hljs-operator">-</span> <span class="hljs-number">1</span>, current: current <span class="hljs-operator">+</span> n)
        &#125;
    &#125;

    <span class="hljs-keyword">return</span> sumInternal(n, current: <span class="hljs-number">0</span>)
&#125;

tailSum(<span class="hljs-number">1000000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是如果你在项目中直接尝试运行这段代码的话还是会报错，因为在 Debug 模式下 Swift 编译器并不会对尾递归进行优化。我们可以在 scheme 设置中将 Run 的配置从 Debug 改为 Release，这段代码就能正确运行了。</p>
<h3 data-id="heading-16">JSON 和 Codable</h3>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// jsonString</span>
&#123;<span class="hljs-attr">"menu"</span>: &#123;
    <span class="hljs-attr">"id"</span>: <span class="hljs-string">"file"</span>,
    <span class="hljs-attr">"value"</span>: <span class="hljs-string">"File"</span>,
    <span class="hljs-attr">"popup"</span>: &#123;
        <span class="hljs-attr">"menuitem"</span>: [
            &#123;<span class="hljs-attr">"value"</span>: <span class="hljs-string">"New"</span>, <span class="hljs-attr">"onclick"</span>: <span class="hljs-string">"CreateNewDoc()"</span>&#125;,
            &#123;<span class="hljs-attr">"value"</span>: <span class="hljs-string">"Open"</span>, <span class="hljs-attr">"onclick"</span>: <span class="hljs-string">"OpenDoc()"</span>&#125;,
            &#123;<span class="hljs-attr">"value"</span>: <span class="hljs-string">"Close"</span>, <span class="hljs-attr">"onclick"</span>: <span class="hljs-string">"CloseDoc()"</span>&#125;
        ]
    &#125;
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Swift 4 中新加入了 Codable 协议，用来处理数据的序列化和反序列化。利用内置的 JSONEncoder 和 JSONDecoder，在对象实例和 JSON 表现之间进行转换变得非常简单。要处理上面的 JSON，我们可以创建一系列对应的类型，并声明它们实现 Codable：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Obj</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-keyword">let</span> menu: <span class="hljs-type">Menu</span>
    <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Menu</span>: <span class="hljs-title">Codable</span> </span>&#123;
        <span class="hljs-keyword">let</span> id: <span class="hljs-type">String</span>
        <span class="hljs-keyword">let</span> value: <span class="hljs-type">String</span>
        <span class="hljs-keyword">let</span> popup: <span class="hljs-type">Popup</span>
    &#125;

    <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Popup</span>: <span class="hljs-title">Codable</span> </span>&#123;
        <span class="hljs-keyword">let</span> menuItem: [<span class="hljs-type">MenuItem</span>]
        <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">CodingKeys</span>: <span class="hljs-title">String</span>, <span class="hljs-title">CodingKey</span> </span>&#123;
            <span class="hljs-keyword">case</span> menuItem <span class="hljs-operator">=</span> <span class="hljs-string">"menuitem"</span>
        &#125;
    &#125;

    <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">MenuItem</span>: <span class="hljs-title">Codable</span> </span>&#123;
        <span class="hljs-keyword">let</span> value: <span class="hljs-type">String</span>
        <span class="hljs-keyword">let</span> onClick: <span class="hljs-type">String</span>

        <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">CodingKeys</span>: <span class="hljs-title">String</span>, <span class="hljs-title">CodingKey</span> </span>&#123;
            <span class="hljs-keyword">case</span> value
            <span class="hljs-keyword">case</span> onClick <span class="hljs-operator">=</span> <span class="hljs-string">"onclick"</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只要一个类型中所有的成员都实现了 Codable，那么这个类型也就可以自动满足 Codable 的要求。</p>
<p>如果 JSON 中的 key 和类型中的变量名不一致的话 (这很常见，因为 JSON 中往往使用下划线命名 key 值，而 Swift 中的命名规则一般是驼峰式)，我们还需要在对应类中声明 CodingKeys 枚举，并用合适的键值覆盖对应的默认值，上例中 Popup 和 MenuItem 都属于这种情况。</p>
<h3 data-id="heading-17">属性访问控制</h3>
<p>Swift 中由低至高提供了 private，fileprivate，internal，public 和 open 五种访问控制的权限。默认的 internal 在绝大部分时候是适用的，另外由于它是 Swift 中的默认的控制级，因此它也是最为方便的。</p>
<ul>
<li>private：让代码只能在当前作用域或者同一文件中同一类型的作用域中被使用</li>
<li>fileprivate：表示代码可以在当前文件中被访问，而不做类型限定</li>
<li>public：让代码在 target 外部也可以被调用</li>
<li>open：让代码可以被继承或者重写</li>
</ul>
<p>如果我们希望在别的 module 中能访问一个属性，同时又保持只在当前作用域可以设置的话，我们需要将 get 的访问权限提高为 public。属性的访问控制可以通过两次的访问权限指定来实现，具体来说：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">private(set)</span> <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">错误和异常处理</h3>
<p>在 Objective-C 开发中，<strong>异常往往是由程序员的错误导致的 app 无法继续运行</strong>，比如我们向一个无法响应某个消息的 NSObject 对象发送了这个消息，会得到 NSInvalidArgumentException 的异常，并告诉我们 "unrecognized selector sent to instance"；比如我们使用一个超过数组元素数量的下标来试图访问 NSArray 的元素时，会得到 NSRangeException。类似由于这样所导致的程序无法运行的问题应该在开发阶段就被全部解决，而不应当出现在实际的产品中。相对来说，<strong>由 NSError 代表的错误更多地是指那些“合理的”，在用户使用 app 中可能遇到的情况</strong>：比如登陆时用户名密码验证不匹配，或者试图从某个文件中读取数据生成 NSData 对象时发生了问题 (比如文件被意外修改了) 等等。</p>
<p>但是 NSError 的使用方式其实变相在鼓励开发者忽略错误，所以很多工程师在开发时为了省事和简单，就会将输入的 error 设为 nil，也就是不关心错误，导致当错误真正发生时，你几乎无从下手调试。</p>
<p>在 Swift 2.0 中，Apple 为这门语言引入了异常机制。现在，这类带有 NSError 指针作为参数的 API 都被改为了可以抛出异常的形式。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">open</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">write</span>(<span class="hljs-params">toFile</span> <span class="hljs-params">path</span>: <span class="hljs-type">String</span>, 
    <span class="hljs-params">options</span> <span class="hljs-params">writeOptionsMask</span>: <span class="hljs-type">NSData</span>.<span class="hljs-type">WritingOptions</span>)</span> <span class="hljs-keyword">throws</span>

<span class="hljs-keyword">do</span> &#123;
    <span class="hljs-keyword">try</span> d.write(toFile: <span class="hljs-string">"Hello"</span>, options: [])
&#125; <span class="hljs-keyword">catch</span> <span class="hljs-keyword">let</span> error <span class="hljs-keyword">as</span> <span class="hljs-type">NSError</span> &#123;
    print (<span class="hljs-string">"Error: <span class="hljs-subst">\(error.domain)</span>"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你不使用 try 的话，是无法调用 write(toFile:options:) 方法的，它会产生一个编译错误，这让我们无法有意无意地忽视掉这些错误。</p>
<p>在上面的示例中 catch 将抛出的异常 (这里就是个 NSError) 用 let 进行了类型转换，这其实主要是针对 Cocoa 现有的 API 的，是对历史的一种妥协。</p>
<p>对于我们用 Swift 新写的可抛出异常的 API，我们应当抛出一个实现了 Error 协议的类型，比如 enum：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">LoginError</span>: <span class="hljs-title">Error</span> </span>&#123;
    <span class="hljs-keyword">case</span> <span class="hljs-type">UserNotFound</span>, <span class="hljs-type">UserPasswordNotMatch</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">login</span>(<span class="hljs-params">user</span>: <span class="hljs-type">String</span>, <span class="hljs-params">password</span>: <span class="hljs-type">String</span>)</span> <span class="hljs-keyword">throws</span> &#123;
    <span class="hljs-comment">//users 是 [String: String]，存储[用户名:密码]</span>

    <span class="hljs-keyword">if</span> <span class="hljs-operator">!</span>users.keys.contains(user) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-type">LoginError</span>.<span class="hljs-type">UserNotFound</span>
    &#125;

    <span class="hljs-keyword">if</span> users[user] <span class="hljs-operator">!=</span> password &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-type">LoginError</span>.<span class="hljs-type">UserPasswordNotMatch</span>
    &#125;

    <span class="hljs-built_in">print</span>(<span class="hljs-string">"Login successfully."</span>)
&#125;

<span class="hljs-keyword">do</span> &#123;
    <span class="hljs-keyword">try</span> login(user: <span class="hljs-string">"onevcat"</span>, password: <span class="hljs-string">"123"</span>)
&#125; <span class="hljs-keyword">catch</span> <span class="hljs-type">LoginError</span>.<span class="hljs-type">UserNotFound</span> &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"UserNotFound"</span>)
&#125; <span class="hljs-keyword">catch</span> <span class="hljs-type">LoginError</span>.<span class="hljs-type">UserPasswordNotMatch</span> &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"UserPasswordNotMatch"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的 ErrorType 可以非常明确地指出问题所在。在调用时，catch 语句实质上是在进行模式匹配。</p>
<p>可以看出，在 Swift 中，我们虽然把这块内容叫做“异常”，但是实质上它更多的还是“错误”而非真正意义上的异常。</p>
<p>当然，Swift 现在的异常机制也并不是十全十美的。最大的问题是类型安全，不借助于文档的话，<strong>我们现在是无法从代码中直接得知所抛出的异常的类型的</strong>。比如上面的 login 方法，光看方法定义我们并不知道 LoginError 会被抛出。一个理想中的异常 API 可能应该是这样的：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">login</span>(<span class="hljs-params">user</span>: <span class="hljs-type">String</span>, <span class="hljs-params">password</span>: <span class="hljs-type">String</span>)</span> <span class="hljs-keyword">throws</span> <span class="hljs-type">LoginError</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个限制是对于非同步的 API 来说，抛出异常是不可用的 -- <strong>异常只是一个同步方法专用的处理机制</strong>。</p>
<p>Cocoa 框架里对于异步 API 出错时，保留了原来的 Error 机制，比如很常用的 URLSession 中的 dataTask API：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">dataTask</span>(<span class="hljs-params">with</span>: <span class="hljs-type">URLRequest</span>, 
    <span class="hljs-params">completionHandler</span>: (<span class="hljs-type">Data</span>?, <span class="hljs-type">URLResponse</span>?, <span class="hljs-type">Error</span>?) -> <span class="hljs-type">Void</span>)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于异步API，一种现在比较常用的方式就是借助于 enum。枚举 (enum) 类型可以与其他的实例进行绑定，我们可以让方法返回枚举类型，然后在枚举中定义成功和错误的状态，并分别将合适的对象与枚举值进行关联：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">Result</span> </span>&#123;
    <span class="hljs-keyword">case</span> <span class="hljs-type">Success</span>(<span class="hljs-type">String</span>)
    <span class="hljs-keyword">case</span> <span class="hljs-type">Error</span>(<span class="hljs-type">NSError</span>)
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">doSomethingParam</span>(<span class="hljs-params">param</span>:<span class="hljs-type">AnyObject</span>)</span> -> <span class="hljs-type">Result</span> &#123;
    <span class="hljs-comment">//...做某些操作，成功结果放在 success 中</span>
    <span class="hljs-keyword">if</span> success &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-type">Result</span>.<span class="hljs-type">Success</span>(<span class="hljs-string">"成功完成"</span>)
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">let</span> error <span class="hljs-operator">=</span> <span class="hljs-type">NSError</span>(domain: <span class="hljs-string">"errorDomain"</span>, code: <span class="hljs-number">1</span>, userInfo: <span class="hljs-literal">nil</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-type">Result</span>.<span class="hljs-type">Error</span>(error)
    &#125;
&#125;

<span class="hljs-keyword">let</span> result <span class="hljs-operator">=</span> doSomethingParam(path)

<span class="hljs-keyword">switch</span> result &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-keyword">let</span> .<span class="hljs-type">Success</span>(ok):
    <span class="hljs-keyword">let</span> serverResponse <span class="hljs-operator">=</span> ok
<span class="hljs-keyword">case</span> <span class="hljs-keyword">let</span> .<span class="hljs-type">Error</span>(error):
    <span class="hljs-keyword">let</span> serverResponse <span class="hljs-operator">=</span> error.description
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Swift 2.0 中，我们甚至可以在 enum 中指定泛型，这样就使结果统一化了。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">Result</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-keyword">case</span> <span class="hljs-type">Success</span>(<span class="hljs-type">T</span>)
    <span class="hljs-keyword">case</span> <span class="hljs-type">Failure</span>(<span class="hljs-type">NSError</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们只需要在返回结果时指明 T 的类型，就可以使用同样的 Result 枚举来代表不同的返回结果了。这么做可以减少代码复杂度和可能的状态，同时不是优雅地解决了类型安全的问题，可谓一举两得。</p>
<p>因此，在 Swift 中的错误处理，现在一般的最佳实践是<strong>对于同步 API 使用异常机制，对于异步 API 使用泛型枚举</strong>。</p>
<p><strong>关于 try 和 throws：</strong></p>
<ul>
<li>
<p><code>try!</code>，强制执行</p>
</li>
<li>
<p><code>try?</code>，尝试执行，常与 <code>if let</code> 搭配使用，如果你用了 try? 的话，就意味着你无视了错误的具体类型</p>
</li>
<li>
<p>在一个可以 throw 的方法里，我们永远不应该返回一个 Optional 的值。因为结合 try? 使用的话，这个 Optional 的返回值将被再次包装一层 Optional，使用这种双重 Optional 的值非常容易产生错误，也十分让人迷惑</p>
</li>
<li>
<p>rethrows 和 throws 做的事情并没有太多不同，它们都是标记了一个方法应该抛出错误。但是 rethrows 一般用在参数中含有可以 throws 的方法的高阶函数中，来表示它既可以接受普通函数，也可以接受一个能 throw 的函数作为参数。也就是像是下面这样的方法，我们可以在外层用 rethrows 进行标注：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">methodThrows</span>(<span class="hljs-params">num</span>: <span class="hljs-type">Int</span>)</span> <span class="hljs-keyword">throws</span> &#123;
    <span class="hljs-keyword">if</span> num <span class="hljs-operator"><</span> <span class="hljs-number">0</span> &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"Throwing!"</span>)
        <span class="hljs-keyword">throw</span> <span class="hljs-type">E</span>.<span class="hljs-type">Negative</span>
    &#125;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"Executed!"</span>)
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">methodRethrows</span>(<span class="hljs-params">num</span>: <span class="hljs-type">Int</span>, <span class="hljs-params">f</span>: <span class="hljs-type">Int</span> <span class="hljs-keyword">throws</span> -> ())</span> <span class="hljs-keyword">rethrows</span> &#123;
    <span class="hljs-keyword">try</span> f(num)
&#125;

<span class="hljs-keyword">do</span> &#123;
    <span class="hljs-keyword">try</span> methodRethrows(num: <span class="hljs-number">1</span>, f: methodThrows)
&#125; <span class="hljs-keyword">catch</span> <span class="hljs-keyword">_</span> &#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>你在要 throws 另一个 throws 时，应该将前者改为 rethrows。</p>
</li>
</ul>
<h3 data-id="heading-19">Log输出</h3>
<p>在 Swift 中，编译器为我们准备了几个很有用的编译符号</p>






























<table><thead><tr><th>符号</th><th>类型</th><th>描述</th></tr></thead><tbody><tr><td><code>#file</code></td><td>String</td><td>包含这个符号的文件的路径</td></tr><tr><td><code>#line</code></td><td>Int</td><td>符号出现的行号</td></tr><tr><td><code>#column</code></td><td>Int</td><td>符号出现的列</td></tr><tr><td><code>#function</code></td><td>String</td><td>包含这个符号的方法名字</td></tr></tbody></table>
<p>我们可以通过使用这些符号来写一个好一些的 Log 输出方法：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">printLog</span><<span class="hljs-type">T</span>>(<span class="hljs-keyword">_</span> <span class="hljs-params">message</span>: <span class="hljs-type">T</span>,
                    <span class="hljs-params">file</span>: <span class="hljs-type">String</span> <span class="hljs-operator">=</span> #file,
                  <span class="hljs-params">method</span>: <span class="hljs-type">String</span> <span class="hljs-operator">=</span> #function,
                    <span class="hljs-params">line</span>: <span class="hljs-type">Int</span> <span class="hljs-operator">=</span> #line)</span>
&#123;
    <span class="hljs-keyword">#if</span> <span class="hljs-type">DEBUG</span>
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"<span class="hljs-subst">\((file as NSString).lastPathComponent)</span>[<span class="hljs-subst">\(line)</span>], <span class="hljs-subst">\(method)</span>: <span class="hljs-subst">\(message)</span>"</span>)
    <span class="hljs-keyword">#endif</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            