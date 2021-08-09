
---
title: 'iOS摸鱼周报 第十八期'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af45bf3ff8334de397a03cc93d9fd4ac~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 16:20:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af45bf3ff8334de397a03cc93d9fd4ac~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af45bf3ff8334de397a03cc93d9fd4ac~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">本期概要</h3>
<blockquote>
<ul>
<li>本期话题：什么是暗时间。</li>
<li>Tips 带来了多个内容：Fastlane 用法总结、minimumLineSpacing 与 minimumInteritemSpacing 的区别以及一个定位 RN 发热问题的过程。</li>
<li>面试解析：本期围绕 block 的变量捕获机制展开说明。</li>
<li>优秀博客带来了几篇编译优化的文章。</li>
<li>学习资料带来了一个从 0 设计计算机的视频教程，还有 Git 和正则表达式的文字教程。</li>
<li>开发工具介绍了两个代码片段整理的相关工具。</li>
</ul>
</blockquote>
<h2 data-id="heading-1">本期话题</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhangferry.com" target="_blank" rel="nofollow noopener noreferrer" title="https://zhangferry.com" ref="nofollow noopener noreferrer">@zhangferry</a>：最近在看一本书：《暗时间》，初听书名可能有些不知所云，因为这个词是作者发明的，我们来看<a href="https://link.juejin.cn/?target=http%3A%2F%2Fmindhacks.cn%2F2009%2F12%2F20%2Fdark-time%2F" title="http://mindhacks.cn/2009/12/20/dark-time/" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">文中</a>对“暗时间”的解释：</p>
<blockquote>
<p>看书并记住书中的东西只是记忆，并没有涉及推理，只有靠推理才能深入理解一个事物，看到别人看不到的地方，这部分推理的过程就是你的思维时间，也是人一生中占据一个显著比例的“暗时间”。你走路、买菜、洗脸洗手、坐公交、逛街、出游、吃饭、睡觉，所有这些时间都可以成为暗时间，你可以充分利用这些时间进行思考，反刍和消化平时看和读的东西，这些时间看起来微不足道，但日积月累会产生巨大的效应。</p>
</blockquote>
<p>这里对于暗时间的解释是思维时间，因为思维是人的”后台线程“，我们通常注意不到它，可它却实际存在且非常重要。但按思维时间来说其适用的范围就有点窄了，大多数情况我们并不会一直保持思考。我尝试把刘未鹏关于暗时间的概念进行扩展，除思维时间外，还包括那些零碎的，可以被利用但未被利用起来的时间。“明时间”，暗时间倘若都能利用起来，那定是极佳的。</p>
<p>目前我有两个关于暗时间应用的实践：</p>
<p>1、在上下班走路过程中是思考时间。我现在换了一条上下班路线，使得步行时间更长，一趟在 15 分钟左右。这段时间，我会尝试想下今天的工作内容，规划日常任务；或者回忆最近在看的某篇文章，脑海里进行推演然后尝试复述其过程；或者仅仅观察路过的行人，想象下如果我是他们，我在另一个视角观察到的自己是什么样子。总之，让大脑活跃起来。</p>
<p>2、等待的过程是运动时间。等人或者等红绿灯的时候，我会尝试让自己运动起来，比如小动作像垫垫脚，大一点的动作像跳一跳、跑一跑。运动是一项反人性的事情，所以它不能规划，一规划就要跟懒惰做斗争，所以干脆就随时有空就动两下。通常这种小型的运动体验，如果突然因为要开始干正事被打断了，还会有种意犹未尽的感觉。</p>
<p>当然还可以有别的尝试，重要的是我们要明白和感受到暗时间这个东西，然后再想办法怎么利用它。至少在我的一些尝试中会让一些本该枯燥的时间变得更有趣了些。</p>
<h2 data-id="heading-2">开发Tips</h2>
<p>整理编辑：<a href="https://juejin.cn/user/3298190611456638" target="_blank" title="https://juejin.cn/user/3298190611456638">zhangferry</a></p>
<h3 data-id="heading-3">Fastlane 用法总结</h3>
<p>图片来源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fawesome-tips%2FiOS-Tips%2Fblob%2Fmaster%2Fresources%2Ffastlane.png" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/awesome-tips/iOS-Tips/blob/master/resources/fastlane.png" ref="nofollow noopener noreferrer">iOS-Tips</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9aa52a0108949bcb09720e07d5d33e7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">React Native 0.59.9 引发手机发烫问题解决思路</h3>
<p>内容贡献：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyyhinbeijing" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yyhinbeijing" ref="nofollow noopener noreferrer">yyhinbeijing</a></p>
<p>问题出现的现象是：RN 页面放置久了，或者反复操作不同的 RN 页面，手机会变得很烫，并且不会自动降温，要杀掉进程才会降温，版本是 0.59.9，几乎不同手机不同手机系统版本均遇到了这个问题，可以确定是 RN 导致的，但具体哪里导致的呢，以下是通过代码注释定位问题的步骤，后面数值为 CPU 占用率：</p>
<p>1、原生：7.2%</p>
<p>2、无网络无 Flatlist：7.2%</p>
<p>3、网络 + FlatList ：100%+</p>
<p>4、网络 + 无 FlatList：100%+</p>
<p>5、去掉 loading：2.6% — 30%，会降低</p>
<p>6、网络和 FlatList 全部放开，只关闭 loading 最低 7.2%，能降低，最高 63%</p>
<p>首先是发现网络导致 CPU 占用率很高，然后网络注释掉 RNLoading （我们自写的 loading 动画），发现内存占用不高了。就断定是 RNLoading 问题，查询发现：我们每次点击 tab 都会加载 loading，而 loading 又是动画，这样大量的动画引发内存问题。虽不是特例问题，但发现、定位、解决问题的过程仍然是有借鉴意义的，即确定范围，然后不断缩小范围。</p>
<h2 data-id="heading-5">面试解析</h2>
<p>整理编辑：<a href="https://link.juejin.cn/?target=opooc.com" target="_blank" title="opooc.com" ref="nofollow noopener noreferrer">反向抽烟</a>、<a href="https://juejin.cn/user/782508012091645" target="_blank" title="https://juejin.cn/user/782508012091645">师大小海腾</a></p>
<p>面试解析会按照主题讲解一些高频面试题，本期面试题是 <strong>block 的变量捕获机制</strong>。</p>
<h3 data-id="heading-6">block 的变量捕获机制</h3>
<p>block 的变量捕获机制，是为了保证 block 内部能够正常访问外部的变量。</p>
<p>1、对于全局变量，不会捕获到 block 内部，访问方式为<code>直接访问</code>；作用域的原因，全局变量哪里都可以直接访问，所以不用捕获。</p>
<p>2、对于局部变量，外部不能直接访问，所以需要捕获。</p>
<ul>
<li>auto 类型的局部变量（我们定义出来的变量，默认都是 auto 类型，只是省略了），block 内部会自动生成一个同类型成员变量，用来存储这个变量的值，访问方式为<code>值传递</code>。<strong>auto 类型的局部变量可能会销毁，其内存会消失，block 将来执行代码的时候不可能再去访问那块内存，所以捕获其值</strong>。由于是值传递，我们修改 block 外部被捕获变量的值，不会影响到 block 内部捕获的变量值。</li>
<li>static 类型的局部变量，block 内部会自动生成一个同类型成员变量，用来存储这个变量的地址，访问方式为<code>指针传递</code>。static 变量会一直保存在内存中， 所以捕获其地址即可。相反，由于是指针传递，我们修改 block 外部被捕获变量的值，会影响到 block 内部捕获的变量值。</li>
<li>对于对象类型的局部变量，block 会连同它的所有权修饰符一起捕获。
<ul>
<li>如果 block 是在栈上，将不会对对象产生强引用</li>
<li>如果 block 被拷贝到堆上，将会调用 block 内部的 <code>copy(__funcName_block_copy_num)</code>函数，copy 函数内部又会调用 <code>assign(_Block_object_assign)</code>函数，assign 函数将会根据变量的所有权修饰符做出相应的操作，形成强引用（retain）或者弱引用。</li>
<li>如果 block 从堆上移除，也就是被释放的时候，会调用 block 内部的 <code>dispose(_Block_object_dispose)</code>函数，dispose 函数会自动释放引用的变量（release）。</li>
</ul>
</li>
<li>对于 <code>__block</code>（可用于解决 block 内部无法修改 auto 变量值的问题） 修饰的变量，编译器会将 <code>__block</code> 变量包装成一个 <code>__Block_byref_varName_num</code> 对象。它的内存管理几乎等同于访问对象类型的 auto 变量，但还是有差异。
<ul>
<li>如果 block 是在栈上，将不会对 <code>__block</code> 变量产生强引用</li>
<li>如果 block 被拷贝到堆上，将会调用 block 内部的 copy</li>
</ul>
函数，copy 函数内部又会调用 assign 函数，assign 函数将会直接对 <code>__block</code> 变量形成强引用（retain）。
<ul>
<li>如果 block 从堆上移除，也就是被释放的时候，会调用 block 内部的 dispose 函数，dispose 函数会自动释放引用的 <code>__block</code> 变量（release）。</li>
</ul>
<img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/2/23/170724cf4ff4b2bd~tplv-t2oaga2asx-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></li>
<li>被 <code>__block </code>修饰的对象类型的内存管理：
<ul>
<li>
<p>如果 <code>__block</code> 变量是在栈上，将不会对指向的对象产生强引用</p>
</li>
<li>
<p>如果 <code>__block</code> 变量被拷贝到堆上，将会调用 <code>__block</code> 变量内部的 <code>copy(__Block_byref_id_object_copy)</code>函数，copy 函数内部会调用 assign 函数，assign 函数又会根据变量的所有权修饰符做出相应的操作，形成强引用（retain）或者弱引用。（注意：这里仅限于 ARC 下会 retain，MRC 下不会 retain，所以在 MRC 下还可以通过 <code>__block</code> 解决循环引用的问题）</p>
</li>
<li>
<p>如果 <code>__block</code> 变量从堆上移除，会调用 <code>__block</code> 变量内部的 dispose 函数，dispose 函数会自动释放指向的对象（release）。</p>
</li>
</ul>
</li>
</ul>
<p>掌握了 block 的变量捕获机制，我们就能更好的应对内存管理，避免因使用不当造成内存泄漏。</p>
<p>常见的 block 循环引用为：<code>self(obj) -> block -> self(obj)</code>。这里 block 强引用了 self 是因为对于对象类型的局部变量，block 会连同它的所有权修饰符一起捕获，而对象的默认所有权修饰符为 __strong。</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-keyword">self</span>.block = ^&#123;
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@"</span>, <span class="hljs-keyword">self</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>为什么这里说 self 是局部变量？因为 self 是 OC 方法的一个隐式参数。</p>
</blockquote>
<p>为了避免循环引用，我们可以使用 <code>__weak</code> 解决，这里 block 将不再持有 self。</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">__<span class="hljs-keyword">weak</span> <span class="hljs-keyword">typeof</span>(<span class="hljs-keyword">self</span>) weakSelf = <span class="hljs-keyword">self</span>;
<span class="hljs-keyword">self</span>.block = ^&#123;
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@"</span>, weakSelf);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了避免在 block 调用过程中 self 提前释放，我们可以使用 <code>__strong</code> 在 block 执行过程中持有 self，这就是所谓的 Weak-Strong-Dance。</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">__<span class="hljs-keyword">weak</span> <span class="hljs-keyword">typeof</span>(<span class="hljs-keyword">self</span>) weakSelf = <span class="hljs-keyword">self</span>;
<span class="hljs-keyword">self</span>.block = ^&#123;
    __<span class="hljs-keyword">strong</span> <span class="hljs-keyword">typeof</span>(<span class="hljs-keyword">self</span>) strongSelf = weakSelf;
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@"</span>, strongSelf);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，我们平常用的比较多的还是 <code>@weakify(self)</code> 和 <code>@strongify(self)</code> 啦。</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">@weakify(<span class="hljs-keyword">self</span>);
<span class="hljs-keyword">self</span>.block = ^&#123;
    @strongify(<span class="hljs-keyword">self</span>);
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@"</span>, <span class="hljs-keyword">self</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你使用的是 RAC 的 Weak-Strong-Dance，你还可以这样：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">@weakify(<span class="hljs-keyword">self</span>, obj1, obj2);
<span class="hljs-keyword">self</span>.block = ^&#123;
    @strongify(<span class="hljs-keyword">self</span>, obj1, obj2);
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@"</span>, <span class="hljs-keyword">self</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是嵌套的 block：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">@weakify(<span class="hljs-keyword">self</span>);
<span class="hljs-keyword">self</span>.block = ^&#123;
    @strongify(<span class="hljs-keyword">self</span>);
    <span class="hljs-keyword">self</span>.block2 = ^&#123;
        @strongify(<span class="hljs-keyword">self</span>);
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@"</span>, <span class="hljs-keyword">self</span>);
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你是否会疑问，为什么内部不需要再写 @weakify(self) ？这个问题就留给你自己去思考和解决吧！</p>
<p>相比于简单的相互循环引用，block 造成的大环引用更需要你足够细心以及敏锐的洞察力，比如：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">TYAlertView *alertView = [TYAlertView alertViewWithTitle:<span class="hljs-string">@"TYAlertView"</span> message:<span class="hljs-string">@"This is a message, the alert view containt text and textfiled. "</span>];
[alertView addAction:[TYAlertAction actionWithTitle:<span class="hljs-string">@"取消"</span> style:TYAlertActionStyleCancle handler:^(TYAlertAction *action) &#123;
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@-%@"</span>, <span class="hljs-keyword">self</span>, alertView);
&#125;]];
<span class="hljs-keyword">self</span>.alertController = [TYAlertController alertControllerWithAlertView:alertView preferredStyle:TYAlertControllerStyleAlert];
[<span class="hljs-keyword">self</span> presentViewController:alertController animated:<span class="hljs-literal">YES</span> completion:<span class="hljs-literal">nil</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里循环引用有两处：</p>
<ol>
<li><code>self -> alertController -> alertView -> handlerBlock -> self</code></li>
<li><code>alertView -> handlerBlock -> alertView</code></li>
</ol>
<p>避免循环引用：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">TYAlertView *alertView = [TYAlertView alertViewWithTitle:<span class="hljs-string">@"TYAlertView"</span> message:<span class="hljs-string">@"This is a message, the alert view containt text and textfiled. "</span>];
@weakify(<span class="hljs-keyword">self</span>, alertView);
[alertView addAction:[TYAlertAction actionWithTitle:<span class="hljs-string">@"取消"</span> style:TYAlertActionStyleCancle handler:^(TYAlertAction *action) &#123;
    @strongify(<span class="hljs-keyword">self</span>, alertView);
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@-%@"</span>, <span class="hljs-keyword">self</span>, alertView);
&#125;]];
<span class="hljs-keyword">self</span>.alertController = [TYAlertController alertControllerWithAlertView:alertView preferredStyle:TYAlertControllerStyleAlert];
[<span class="hljs-keyword">self</span> presentViewController:alertController animated:<span class="hljs-literal">YES</span> completion:<span class="hljs-literal">nil</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>另外再和你提一个小知识点，当我们在 block 内部直接使用 _variable 时，编译器会给我们警告：<code>Block implicitly retains self; explicitly mention 'self' to indicate this is intended behavior</code>。</p>
<p>原因是 block 中直接使用 <code>_variable</code> 会导致 block 隐式的强引用 self。Xcode 认为这可能会隐式的导致循环引用，从而给开发者带来困扰，而且如果不仔细看的话真的不太好排查，笔者之前就因为这个循环引用找了半天，还拉上了我导师一起查找原因。所以警告我们要显式的在 block 中使用 self，以达到 block 显式 retain 住 self 的目的。改用 <code>self->_variable</code> 或者 <code>self.variable</code>。</p>
<p>你可能会觉得这种困扰没什么，如果你使用 <code>@weakify</code> 和 <code>@strongify</code> 那确实不会造成循环引用，因为 <code>@strongify</code> 声明的变量名就是 self。那如果你使用 <code>weak typeof(self) weak_self = self;</code> 和 <code>strong typeof(weak_self) strong_self = weak_self</code> 呢？</p>
</blockquote>
<h2 data-id="heading-7">优秀博客</h2>
<p>整理编辑：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fu%2F739b677928f7" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/u/739b677928f7" ref="nofollow noopener noreferrer">皮拉夫大王在此</a>、<a href="https://juejin.cn/user/1151943916921885" target="_blank" title="https://juejin.cn/user/1151943916921885">我是熊大</a></p>
<p>本期主题：<code>编译优化</code></p>
<p>1、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FHello_Hwc%2Farticle%2Fdetails%2F53557308" title="https://blog.csdn.net/Hello_Hwc/article/details/53557308" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">iOS编译过程的原理和应用</a> -- 来自 CSDN：黄文臣</p>
<p>做编译优化前，先了解下编译原理吧！该作者通过 iOS 的视角，白话了编译原理，通俗易懂。</p>
<p>2、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1817236" title="https://cloud.tencent.com/developer/article/1817236" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">Xcode编译疾如风系列 - 分析编译耗时</a> -- 来自腾讯社区：小菜与老鸟</p>
<p>在进行编译速度优化前，一个合适的分析工具是必要的，它能告诉你哪部分编译时间较长，让你发现问题，从而解决问题，本文介绍了几种分析编译耗时的方式，助你分析构建时间。该作者还有其他相关姊妹篇，建议前往阅读。</p>
<p>3、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1564372" title="https://cloud.tencent.com/developer/article/1564372" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">iOS 微信编译速度优化分享</a> -- 来自云+社区：微信终端开发团队</p>
<p>文章对编译优化由浅入深做了介绍。作者首先介绍了常见的现有方案，利用现有方案以及精简代码、将模板基类改为虚基类、使用 PCH 等方案做了部分优化。文章精彩的部分在于作者并没有止步于此，而是从编译原理入手，结合量化手段，分析出编译耗时的瓶颈。在找到问题的瓶颈后，作者尝试人工进行优化，但是效率较低。最终在 IWYU 基础上，增加了 ObjC 语言的支持，高效地处理了一部分多余的头文件。</p>
<p>4、<a href="https://juejin.cn/post/6903407900006449160" title="https://juejin.cn/post/6903407900006449160" target="_blank">iOS编译速度如何稳定提高10倍以上之一</a> -- 来自掘金：Mr_Coder</p>
<p>美柚 iOS 的编译提效历程。作者对常见的优化做了分析，列举了各自的优缺点。有想做编译优化的可以参考这篇文章了解一下。对于业界的主流技术方案，别的技术文章往往只介绍优点，对方案的缺点谈的不够彻底。这篇文章从实践者的角度阐述了常见方案的优缺点，很有参考价值。文章介绍了双私有源二进制组件并与 ccache 做了对比，最后列出了方案支持的功能点。</p>
<p>5、<a href="https://juejin.cn/post/6903408514778497031" title="https://juejin.cn/post/6903408514778497031" target="_blank">iOS编译速度如何稳定提高10倍以上之二</a> -- 来自掘金：Mr_Coder</p>
<p>作为上文的姊妹篇，本文详细介绍了双私有源二进制组件的方案细节以及使用方法。对该方案感兴趣的可以关注下。</p>
<p>6、<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftech.meituan.com%2F2021%2F02%2F25%2Fcocoapods-hmap-prebuilt.html" title="https://tech.meituan.com/2021/02/25/cocoapods-hmap-prebuilt.html" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">一款可以让大型iOS工程编译速度提升50%的工具</a> -- 来自美团技术团队：思琦 旭陶 霜叶</p>
<p>本文主要介绍了如何通过优化头文件搜索机制来实现编译提速，全源码编译效率提升 45%。文中涉及很多知识点，比如 hmap 文件的作用、Build Phases - Headers 中的 Public，Private，Project 各自是什么作用。文中详细分析了 podspec 创建头文件产物的逻辑以及 Use Header Map 失效的原因。干货比较多，可能得多读几遍。</p>
<h2 data-id="heading-8">学习资料</h2>
<p>整理编辑：<a href="https://juejin.cn/user/1433418892590136" target="_blank" title="https://juejin.cn/user/1433418892590136">Mimosa</a></p>
<h3 data-id="heading-9">从 0 到 1 设计一台计算机</h3>
<p>地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1wi4y157D3" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1wi4y157D3" ref="nofollow noopener noreferrer">www.bilibili.com/video/BV1wi…</a></p>
<p>来自 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fspace.bilibili.com%2F481434238" target="_blank" rel="nofollow noopener noreferrer" title="https://space.bilibili.com/481434238" ref="nofollow noopener noreferrer">Ele实验室</a> 的计算机组成原理课程，该系列视频主要目的是让大家对「计算机是如何工作的」有个较直观的认识，做为深入学习计算机科学的一个启蒙。观看该系列视频最好有一些数字电路和模拟电路的基础知识，Ele 实验室同时也有关于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Hi4y1t7zY" title="https://www.bilibili.com/video/BV1Hi4y1t7zY" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">数电</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1774114798" title="https://www.bilibili.com/video/BV1774114798" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">模电</a> 的基础知识介绍供大家参考。</p>
<h3 data-id="heading-10">Git Cheat Sheet 中文版</h3>
<p>地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflyhigher139%2FGit-Cheat-Sheet" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flyhigher139/Git-Cheat-Sheet" ref="nofollow noopener noreferrer">github.com/flyhigher13…</a></p>
<p>Git Cheat Sheet 让你不用再去记所有的 git 命令！对新手友好，可以用于查阅简单的 git 命令。</p>
<h3 data-id="heading-11">正则表达式 30 分钟入门教程</h3>
<p>地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeerchao.cn%2Ftutorials%2Fregex%2Fregex.htm" target="_blank" rel="nofollow noopener noreferrer" title="https://deerchao.cn/tutorials/regex/regex.htm" ref="nofollow noopener noreferrer">deerchao.cn/tutorials/r…</a></p>
<p>30 分钟内让你明白正则表达式是什么，并对它有一些基本的了解。别被那些复杂的表达式吓倒，只要跟着我一步一步来，你会发现正则表达式其实并没有想象中的那么困难。除了作为入门教程之外，本文还试图成为可以在日常工作中使用的正则表达式语法参考手册。</p>
<h2 data-id="heading-12">工具推荐</h2>
<p>整理编辑：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhangferry.com" target="_blank" rel="nofollow noopener noreferrer" title="https://zhangferry.com" ref="nofollow noopener noreferrer">zhangferry</a></p>
<h3 data-id="heading-13">SnippetsLab</h3>
<p><strong>地址</strong>：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.renfei.org%2Fsnippets-lab%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.renfei.org/snippets-lab/" ref="nofollow noopener noreferrer">www.renfei.org/snippets-la…</a></p>
<p><strong>软件状态</strong>：$9.99</p>
<p><strong>软件介绍</strong>：</p>
<p>一款强大的代码片段管理工具，从此告别手动复制粘贴，SnippetsLab 的设计更符合 Apple 的交互习惯，支持导航栏快速操作。另外还可以同步 Github Gist 内容，使用 iCloud 备份。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71f496e74b9c4089b7addd8742e8473c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">CodeExpander</h3>
<p><strong>地址</strong>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodeexpander.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://codeexpander.com/" ref="nofollow noopener noreferrer">codeexpander.com/</a></p>
<p><strong>软件状态</strong>：普通版免费，高级版付费</p>
<p><strong>软件介绍</strong>：</p>
<p>专为开发者开发的一个集输入增强、代码片段管理工具，支持跨平台，支持云同步（Github/码云）。免费版包含 90% 左右功能，相对 SnippetsLab 来说其适用范围更广泛，甚至包括一些日常文本的片段处理。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba4ae50f1fc44cb1a0f207ca0559750a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">关于我们</h2>
<p>iOS 摸鱼周报，主要分享开发过程中遇到的经验教训、优质的博客、高质量的学习资料、实用的开发工具等。周报仓库在这里：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzhangferry%2FiOSWeeklyLearning" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zhangferry/iOSWeeklyLearning" ref="nofollow noopener noreferrer">github.com/zhangferry/…</a> ，如果你有好的的内容推荐可以通过 issue 的方式进行提交。另外也可以申请成为我们的常驻编辑，一起维护这份周报。另可关注公众号：iOS成长之路，后台点击进群交流，联系我们，获取更多内容。</p>
<h3 data-id="heading-16">往期内容</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F3vukUOskJzoPyES2R7rJNg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/3vukUOskJzoPyES2R7rJNg" ref="nofollow noopener noreferrer">iOS摸鱼周报 第十七期</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fnuij8iKsARAF2rLwkVtA8w" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/nuij8iKsARAF2rLwkVtA8w" ref="nofollow noopener noreferrer">iOS摸鱼周报 第十六期</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F6thW_YKforUy_EMkX0OVxA" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/6thW_YKforUy_EMkX0OVxA" ref="nofollow noopener noreferrer">iOS摸鱼周报 第十五期</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fbr4DUrrtj9-VF-VXnTIcZw" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/br4DUrrtj9-VF-VXnTIcZw" ref="nofollow noopener noreferrer">iOS摸鱼周报 第十四期</a></p></div>  
</div>
            