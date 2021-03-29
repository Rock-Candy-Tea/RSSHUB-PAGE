
---
title: '漫谈LLDB：最优雅的方式打印UIViewController生命周期'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2a78a8026b6414e838fc77a0cf20401~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 16 Mar 2021 22:46:59 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2a78a8026b6414e838fc77a0cf20401~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">漫谈LLDB：最优雅的方式打印UIViewController生命周期</h1>
<h2 data-id="heading-1">前言</h2>
<p>打印UIViewController的生命周期有显而易见的好处，可以很方便看到当前页进入哪个UIViewController，也可以检查退出当前UIViewController后有没有销毁（dealloc）它。<br>
通常实现的方式有两种，一种是父类中重写（override）生命周期方法，并用<code>NSLog</code>或<code>print</code>方法输出相应的方法名，这样所有继承于它的业务子类都能自动打印指定的生命周期方法。另一种是使用Method Swizzling，无侵入的方式打印<strong>所有</strong>UIViewController指定的生命周期，我早期开发常在Category中完成方法交换，以下是一个简易打印dealloc的例子：</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">UIViewController</span> (<span class="hljs-title">HMExtension</span>)</span>

+ (<span class="hljs-keyword">void</span>)load &#123;
    SEL s1 = <span class="hljs-built_in">NSSelectorFromString</span>(<span class="hljs-string">@"dealloc"</span>);
    Method m1 = class_getInstanceMethod(<span class="hljs-keyword">self</span>, s1);

    SEL s2 = <span class="hljs-built_in">NSSelectorFromString</span>(<span class="hljs-string">@"hm_dealloc"</span>);
    Method m2 = class_getInstanceMethod(<span class="hljs-keyword">self</span>, s2);
    <span class="hljs-keyword">if</span> (class_addMethod(<span class="hljs-keyword">self</span>, s1, method_getImplementation(m2), method_getTypeEncoding(m2))) &#123;
        class_replaceMethod(<span class="hljs-keyword">self</span>, s2, method_getImplementation(m1), method_getTypeEncoding(m1));
    &#125; <span class="hljs-keyword">else</span> &#123;
        method_exchangeImplementations(m1, m2);
    &#125;
&#125;

- (<span class="hljs-keyword">void</span>)hm_dealloc &#123;
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@ dealloc"</span>, [<span class="hljs-keyword">self</span> <span class="hljs-keyword">class</span>]);
    [<span class="hljs-keyword">self</span> hm_dealloc];
&#125;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两种方法各有优劣，这里就不分析了，因为接下来介绍的才是本文重点，一种比Method Swizzling更加无侵入的方式，0行代码即可实现打印生命周期。</p>
<h2 data-id="heading-2">使用LLDB符号断点打印生命周期</h2>
<p>Xcode允许我们添加<strong>Symbolic Breakpoint</strong>符号断点，通过设置符号让LLDB触发断点。</p>
<p><img alt="img1.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2a78a8026b6414e838fc77a0cf20401~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="img2.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b144492a9084287ac4bad2115836bf2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
我们可以通过配置UIViewController生命周期的符号，让LLDB触发断点，输出上下文信息。接下来以<code>viewDidAppear:</code>方法为例，讲讲思路。</p>
<ol>
<li>首先根据上图的提示，symbol这一行这样配置<code>-[UIViewController viewDidAppear:]</code>。运行项目，程序很快就会触发了这个断点而停止，并进入LLDB调试模式。</li>
<li>如何输出需要的信息呢？可以在Action这一行新增一个<strong>Debugger Command</strong>，可以用来执行LLDB自带的命令。众所周知，OC消息发送机制的前两个参数是<code>self</code>和<code>_cmd</code>，在LLDB环境中无法直接用这两个关键字，得用别的办法获取<code>self</code>和<code>_cmd</code>。最可靠的是通过寄存器来取值，在方法内部断点，64位模拟器(x86_64)的前两个参数的寄存器是rdi和rsi，64位真机(arm64)的前两个参数的寄存器是x0和x1，前面加上<code>$</code>符号即可在LLDB中取值，假设是在模拟器，那这一行输入这条命令<code>expression -l objc -O -- @import UIKit; [[NSString alloc] initWithFormat:@"%@  %s", (id)$rdi, (char *)$rsi]</code>。还有另一种方法，那就是LLDB提供了<code>$arg1</code>，<code>$arg2</code>，<code>$arg3</code>...等一系列变量，指向当前方法调用的第几个参数，为了同时兼容模拟器和真机，所以这一行应改为<code>expression -l objc -O -- @import UIKit; [[NSString alloc] initWithFormat:@"%@  %s", (id)$arg1, (char *)$arg2]</code>。</li>
<li>命中断点，执行命令，最后还有一个步骤，那就是让程序恢复运行状态，勾选上<strong>Automatically continue after evaluating actions</strong>这个选项。最后的成果如下图：</li>
</ol>
<p><img alt="img3.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/137f1714e72546e5916b91507b87afed~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>把<code>dealloc</code>方法也配置好符号断点，运行Swift开源项目<a href="https://github.com/onevcat/Kingfisher" target="_blank" rel="nofollow noopener noreferrer">Kingfisher</a>里的demo，Xcode的Console输出如下gif:</p>
<p><img alt="img4.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/494e2bd851b14c878887e8edc29efb16~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我在Xcode设置里把Debugger的输出换了颜色（橙色），方便和APP执行程序的输出（黑色）做区分。</p>
<h2 data-id="heading-3">优化：减少@import UIKit语句</h2>
<p>不难看出上面的<code>expression</code>命令执行了两条语句，首先是<code>@import UIKit</code>，然后是<code>[[NSString alloc] initWithFormat:@"%@  %s", (id)$arg1, (char *)$arg2]</code>。可能一些APP并不需要导入UIKit框架，但为了提高稳定性我还是保留了。<br>
LLDB只需要导入一次UIKit，而上面每次触发断点都执行了一次<code>@import UIKit;</code>。为了减少不必要的import，可以在触发UIViewController生命周期断点前，先导入一次UIKit。设置一个符号断点<code>UIApplicationMain</code>，并添加<strong>Debugger Command</strong>的Action，输入<code>expression -l objc -O -- @import UIKit</code>，然后勾选<strong>Automatically continue after evaluating actions</strong>，这样APP启动后就导入了UIKit。如下图所示：</p>
<p><img alt="img5.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/506a5635a72e4d23b617ea31a0159e30~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>接下来的工作和上一节介绍一样，为UIViewController生命周期方法添加符号断点，但是<strong>Debugger Command</strong>的命令缩减为<code>expression -l objc -O -- [[NSString alloc] initWithFormat:@"%@  %s", (id)$arg1, (char *)$arg2]</code>就可以了。</p>
<h2 data-id="heading-4">优化：忽略系统生成的UIViewController</h2>
<p>如果读者有仔细看一下前面那张gif效果图，会发现有一个<strong>UIInputWindowController</strong>出现了，这属于系统生成的UIViewController。iOS系统会在一些情况下生成某些UIViewController，而大部分情况下我们并不需要关注这些系统生成的UIViewController，为了减少干扰，就需要忽略这些类。<br>
再仔细看一眼上面断点编辑窗口，在<strong>Condition</strong>这一行是可以进行类过滤的。但如果这样做的话，每次新增一个需要忽略的类，要调整的地方就太多了：每个项目，项目中每个生命周期符号断点都要修改。<br>
为了简化后续维护工作，我写了一个LLDB脚本命令<code>plifecycle</code>，这个脚本被收集在我的开源命令库<a href="https://github.com/chenhuimao/HMLLDB" target="_blank" rel="nofollow noopener noreferrer">HMLLDB</a>中，读者可以参照文档，安装这个开源库。成功安装之后，<strong>Debugger Command</strong>这行就可以用<code>plifecycle -i</code>就能打印生命周期并忽略系统某些UIViewController，而且也不需要先<code>@import UIKit</code>。配置如下图：</p>
<p><img alt="img6.jpg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d2eb70b431a4292b75c1595b5cfc796~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">LLDB打印生命周期的优点</h2>
<p>我之所以认为使用LLDB打印UIViewController生命周期是最优雅的方式，是因为和传统的方法相比，前者具有以下的优势：</p>
<ul>
<li>0行代码，无侵入，项目无需修改，git看不到任何相关记录。</li>
<li>Xcode可以为<strong>Debugger Output</strong>设置独特颜色，Console窗口也可以设置只显示Debugger Output，非常方便定位。</li>
<li>在程序运行时，在<strong>Breakpoing navigator</strong>可以按需要开启或关闭符号断点，随时控制是否打印。</li>
</ul>
<h2 data-id="heading-6">存在的问题</h2>
<ul>
<li>刚启动APP时有可能会触发下面的警告而暂停程序，需要点击Xcode里的<strong>Continue program execution</strong>让程序继续跑。偶现的问题，可能下次重启电脑就不会出现了。</li>
</ul>
<pre><code class="copyable"># 遇上这个警告，要点击Xcode里的Continue program execution让程序继续跑
Warning: hit breakpoint while running function, skipping commands and conditions to prevent recursion.
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>切换页面卡顿。命中断点进入调试模式本身就会有所消耗，加上执行的命令需要经过即时编译JIT，所以页面切换会有点卡顿。一般情况下并不建议打印所有生命周期方法，<strong>推荐日常开发只启用<code>viewDidAppear:</code>和<code>dealloc</code>打印</strong>。</li>
</ul>
<h2 data-id="heading-7">后记</h2>
<p>也许有读者已经注意到了，上面介绍的那条<code>expression</code>和<code>plifecycle</code>的命令都支持打印任意的OC方法，只不过在本篇文章中只用来打印生命周期而已。但是我不排除后期会变更<code>plifecycle</code>的实现方式，毕竟上面存在的问题会影响使用体验。</p>
<h2 data-id="heading-8">相关资料</h2>
<p>HMLLDB：<a href="https://github.com/chenhuimao/HMLLDB" target="_blank" rel="nofollow noopener noreferrer">github.com/chenhuimao/…</a><br>
plifecycle源码：<a href="https://github.com/chenhuimao/HMLLDB/blob/master/commands/HMLifeCycle.py" target="_blank" rel="nofollow noopener noreferrer">github.com/chenhuimao/…</a><br>
Kingfisher：<a href="https://github.com/onevcat/Kingfisher" target="_blank" rel="nofollow noopener noreferrer">github.com/onevcat/Kin…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            