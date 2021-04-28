
---
title: '7 个最能用于构造更整洁的 Flutter 应用的 Dart 小贴士和小技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aad6dba87634c35893f7042caa052ec~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 05:28:48 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aad6dba87634c35893f7042caa052ec~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://betterprogramming.pub/top-7-dart-tips-and-tricks-for-cleaner-flutter-apps-562664a15826" target="_blank" rel="nofollow noopener noreferrer">Top 7 Dart Tips and Tricks for Cleaner Flutter Apps</a></li>
<li>原文作者：<a href="https://medium.com/@educative-inc" target="_blank" rel="nofollow noopener noreferrer">The Educative Team</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/top-7-dart-tips-and-tricks-for-cleaner-flutter-apps.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/PassionPenguin" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：<a href="https://github.com/5Reasons" target="_blank" rel="nofollow noopener noreferrer">5Reasons</a>、<a href="https://github.com/greycodee" target="_blank" rel="nofollow noopener noreferrer">greycodee</a></li>
</ul>
</blockquote>
<p><a href="https://www.educative.io/blog/dart-2-language-features" target="_blank" rel="nofollow noopener noreferrer">Dart</a> 是一门针对客户端进行了优化的编程语言，专门用于快速地构建移动端、桌面端和服务端应用程序。Dart 由 Google 开发，并与 Google 的跨平台框架 Flutter 相互搭配。借助 Flutter 和 Dart，我们可以构建具有流畅 UI 和原生性能的应用程序。</p>
<p>今天，我们总结并分享了七个我们认为最实用的 Dart 技巧，来帮助大家改善应用程序的开发。我们可以使用这些技巧来编写简洁的代码，并充分利用上 Dart 所提供的许多特性。</p>
<p><strong>速览 —— 贴士和技巧：</strong></p>
<ol>
<li>使用匿名函数作为参数</li>
<li>使用 <code>call</code> 方法让类可以像是个函数一样被调用</li>
<li>使用 <code>.entries</code> 来在一个 map 上遍历</li>
<li>如何使用 getter 和 setter</li>
<li>用 <code>Set</code> 存储唯一值</li>
<li>使用 Inspect 功能</li>
<li>使用 sync 和 async 生成器</li>
</ol>
<h2 data-id="heading-0">1. 使用匿名函数作为参数</h2>
<p>在 Dart 语言中，我们可以将函数作为参数传递给其他函数，而 Dart 语言本身还支持无需命名即可调用的匿名函数。</p>
<p>以下是 Dart 中使用匿名函数的示例。在本例中，我们将一个匿名的求立方函数传递给内置方法 <code>forEach</code>，尝试获取 <code>list</code> 数组中每一项的立方。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart">main() &#123;
  <span class="hljs-keyword">var</span> list = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
  list.forEach((item) &#123;
    <span class="hljs-built_in">print</span>(item * item * item);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. 使用 <code>call</code> 方法让类可以像是个函数一样被调用</h2>
<p>使用 Dart 语言我们可以构造一个可调用的类，允许将该类的实例作为函数调用。我们可以用 <code>call()</code> 方法做到这一点,请参见下面的语法：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">class_name</span> </span>&#123;
  ... <span class="hljs-comment">// class </span>

  return_type call ( parameters ) &#123;
  ... <span class="hljs-comment">// 调用这个函数内容</span>
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让我们来看一个例子：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EducativeIntro</span> </span>&#123;

  <span class="hljs-comment">// 定义 call 方法 </span>
  <span class="hljs-built_in">String</span> call(<span class="hljs-built_in">String</span> a, <span class="hljs-built_in">String</span> b, <span class="hljs-built_in">String</span> c) => <span class="hljs-string">'Welcome to <span class="hljs-subst">$a</span><span class="hljs-subst">$b</span><span class="hljs-subst">$c</span>'</span>;
&#125;

<span class="hljs-comment">// 主函数  </span>
<span class="hljs-keyword">void</span> main() &#123;
  <span class="hljs-keyword">var</span> educative_input = EducativeIntro();

  <span class="hljs-comment">// 借助实例调用这个类</span>
  <span class="hljs-keyword">var</span> educative_output = educative_input(<span class="hljs-string">'our '</span>, <span class="hljs-string">'Dart '</span>, <span class="hljs-string">'tutorial'</span>);

  <span class="hljs-built_in">print</span>(educative_output);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意：</strong> Dart 不支持多个可调用方法</p>
</blockquote>
<h2 data-id="heading-2">3. 使用 <code>.entries</code> 来在一个 map 上遍历</h2>
<p>在 Dart 中我们可以使用 <code>entries()</code> 方法以空安全的方式遍历一张 map。假设我们现在有一张 map 用于追踪在不同产品上花费的金额（通常我们会使用 <code>!</code> 运算符在此 map 中进行遍历）：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> moneySpent.keys) &#123;
  <span class="hljs-keyword">final</span> value = moneySpent[key]!;
  <span class="hljs-built_in">print</span>(<span class="hljs-string">'<span class="hljs-subst">$key</span>: <span class="hljs-subst">$value</span>'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以改进此代码，并使用循环使其更安全。当我们使用 <code>entries</code> 变量进行遍历时，我们可以用空安全的方式访问键值对。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> entry <span class="hljs-keyword">in</span> moneySpent.entries) &#123;
  <span class="hljs-comment">// 使用键值对做一些事情</span>
  <span class="hljs-built_in">print</span>(<span class="hljs-string">'<span class="hljs-subst">$&#123;entry.key&#125;</span>: <span class="hljs-subst">$&#123;entry.value&#125;</span>'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. 如何使用 getter 和 setter</h2>
<p>getter 和 setter 是一对特殊的方法，它们能够对一个对象的属性进行读、写操作。我们对 getter 和 setter 的调用类似于实例变量：点运算符（<code>.</code>）后面紧跟函数的名称。</p>
<p>getter 是用于获取对象属性值的函数，使用 <code>get</code> 关键字定义。</p>
<p>在下面的示例中，我们在第 13 行创建了一个 getter 函数，返回当前实例的 <code>name</code> 属性的值。而在第 21 行，我们调用了 getter 函数，这里的输出应是 <code>Sarah</code>。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-built_in">String</span> name;
  <span class="hljs-built_in">String</span> gender;
  <span class="hljs-built_in">int</span> age;

  Person(<span class="hljs-keyword">this</span>.name, <span class="hljs-keyword">this</span>.gender, <span class="hljs-keyword">this</span>.age);

  Person.newBorn()&#123;
    <span class="hljs-keyword">this</span>.age = <span class="hljs-number">0</span>;
  &#125;

<span class="hljs-comment">// getter 函数，获取 name 的值</span>
  <span class="hljs-built_in">String</span> <span class="hljs-keyword">get</span> personName => name;

  walking() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'<span class="hljs-subst">$name</span> is walking'</span>);

  talking() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'<span class="hljs-subst">$name</span> is talking'</span>);
&#125;

<span class="hljs-built_in">int</span> main() &#123;
  <span class="hljs-keyword">var</span> firstPerson = Person(<span class="hljs-string">"Sarah"</span>, <span class="hljs-string">"Female"</span>, <span class="hljs-number">25</span>);
  <span class="hljs-built_in">print</span>(firstPerson.personName);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>setter 则是用于写入一个对象的属性的函数，使用 <code>set</code> 关键词：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-built_in">String</span> name;
  <span class="hljs-built_in">String</span> gender;
  <span class="hljs-built_in">int</span> age;

  <span class="hljs-built_in">String</span> <span class="hljs-keyword">get</span> personName => name;

<span class="hljs-comment">// setter 函数用于设置 age 的值</span>
  <span class="hljs-keyword">void</span> <span class="hljs-keyword">set</span> personAge(<span class="hljs-built_in">num</span> val) &#123;
    <span class="hljs-keyword">if</span> (val < <span class="hljs-number">0</span>) &#123;
      <span class="hljs-built_in">print</span>(<span class="hljs-string">"Age cannot be negative"</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">this</span>.age = val;
    &#125;
  &#125;

  walking() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'<span class="hljs-subst">$name</span> is walking'</span>);

  talking() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'<span class="hljs-subst">$name</span> is talking'</span>);
&#125;

<span class="hljs-built_in">int</span> main() &#123;
  <span class="hljs-keyword">var</span> firstPerson = Person();
  firstPerson.personAge = <span class="hljs-number">-5</span>;
  <span class="hljs-built_in">print</span>(firstPerson.age);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第 9 行到第 15 行代码中我们创建了一个 setter 函数用于设置 <code>age</code> 的值。该函数还被添加了一个条件判断，让我们不能输入负的年龄。在第 23 行，我们使用 <code>personAge</code> setter 函数为 <code>firstPerson</code> 设置了年龄值。</p>
<h2 data-id="heading-4">用 <code>Set</code> 存储唯一值</h2>
<p>列表是 Dart 中最常见的集合类型之一，但是列表可以容纳重复项。有时我们只想要唯一值的集合，这就是 <code>Set</code> 用武之处。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart">
<span class="hljs-keyword">final</span> countriesSet = &#123;
  <span class="hljs-string">'USA'</span>,
  <span class="hljs-string">'India'</span>,
  <span class="hljs-string">'Iceland'</span>,
  <span class="hljs-string">'USA'</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在一个 <code>Set</code> 中两个元素不能相同，因此上面的代码会有一个 warning 并且无法被编译。同理使用 <code>const set</code> 也无法被编译。</p>
<h2 data-id="heading-5">6. 使用 Inspect 功能</h2>
<p>在网络开发中我们经常会需要用到 Inspect 功能，因为它能够告诉我们应用于 HTML 标记的所有属性。Dart 也提供了类似的功能，我们称之为 Flutter Inspect。这个功能可以有效简化 Flutter 应用程序的开发，用于找到屏幕上的任何控件并查看应用于它的属性。</p>
<p>Inspect 还可以帮助我们可视化 Flutter 控件树以了解布局或确定布局问题。</p>
<p>要使用它，请按照下列步骤操作：</p>
<ul>
<li>单击 <code>Flutter Inspector</code>。</li>
<li>单击 <code>启用选择 Widget 模式</code>。</li>
<li>选择屏幕上的控件以获取更多信息</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aad6dba87634c35893f7042caa052ec~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">7. 使用 Sync 和 Async 生成器</h2>
<p>在 Dart 中，生成器可以生成一系列值。而 Dart 一共有两个生成器函数：</p>
<ul>
<li><strong>同步生成器：</strong> 返回一个可迭代的对象</li>
<li><strong>异步生成器：</strong> 返回 <code>Stream</code> 对象</li>
</ul>
<p>换句话说，同步生成器返回可以顺序访问的值的集合。为此，我们将函数体标记为 <code>sync*</code>。我们会以 <code>yield</code> 语句用作值。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-built_in">Iterable</span><<span class="hljs-built_in">int</span>> count(<span class="hljs-built_in">int</span> n) <span class="hljs-keyword">sync</span>* &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= n; i++) &#123;
    <span class="hljs-keyword">yield</span> i;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>异步生成器则会返回一个 <code>Stream</code> 对象，让接收一系列事件成为可能。我们可以通过将函数体标记为 <code>async*</code> 来做到这一点。我们会以 <code>yield</code> 语句用作值。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart">Stream<<span class="hljs-built_in">int</span>> countStream(<span class="hljs-built_in">int</span> n) <span class="hljs-keyword">async</span>* &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= n; i++) &#123;
    <span class="hljs-keyword">yield</span> i;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">你下一步将学习什么？</h2>
<p>我们希望这些技巧能帮助您充分利用 Dart 及其提供的所有特性。Flutter 和 Dart 是一套强大的工具，用于构建具有原生感和流畅感的应用程序。接下来要研究的其他高级的 Dart 特性应该是：</p>
<ul>
<li>嵌套 <code>if</code> 语句的传播运算符</li>
<li>命名构造函数和初始化列表</li>
<li>Dart 库</li>
<li>枚举类型</li>
</ul>
<p>学习愉快！</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            