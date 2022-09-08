
---
title: '基于WEB的可视化PPT制作扩展篇-动画时间轴实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed00961d3f6a4785bf201a7c744f2f69~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 02:24:55 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed00961d3f6a4785bf201a7c744f2f69~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">基于WEB的可视化PPT制作扩展篇-动画时间轴实现</h1>

















<table><thead><tr><th>文档创建人</th><th>创建日期</th><th>文档内容</th><th>更新时间</th></tr></thead><tbody><tr><td>adsionli</td><td>2022-09-07</td><td>动画时间轴实现</td><td>2022-09-07</td></tr></tbody></table>
<p>躺平之后整个人思路都打开了，花了一晚上就写完了一直拖着的动画时间轴的执行实现，可以支持开始、暂停、点击触发、快进、直接完成、重置这几个功能的动画时间轴控制器，接下来就说是如何设计这块内容的啦。</p>
<ol>
<li><a href="https://juejin.cn/post/7117982197939699726" target="_blank" title="https://juejin.cn/post/7117982197939699726">基于WEB的可视化PPT制作Part1-项目描述及实现内容</a></li>
<li><a href="https://juejin.cn/post/7118264381229498404" target="_blank" title="https://juejin.cn/post/7118264381229498404">基于 WEB 的可视化 PPT 制作 Part2-控件添加及修改，埋点</a></li>
<li><a href="https://juejin.cn/post/7118619234669690888" target="_blank" title="https://juejin.cn/post/7118619234669690888">基于WEB的可视化PPT制作Part3-拖拽、旋转、放缩通用组件实现</a></li>
<li><a href="https://juejin.cn/post/7119067380579303432" target="_blank" title="https://juejin.cn/post/7119067380579303432">基于WEB的可视化PPT制作Part4-实现撤销与恢复</a></li>
<li><a href="https://juejin.cn/post/7119405438294032414" target="_blank" title="https://juejin.cn/post/7119405438294032414">基于WEB的可视化PPT制作Part5-层级设计</a></li>
<li><a href="https://juejin.cn/post/7117534409405759519" target="_blank" title="https://juejin.cn/post/7117534409405759519">基于WEB的可视化PPT制作扩展篇-学习并实现FullScreen</a></li>
<li><a href="https://juejin.cn/post/7111225695262474277" target="_blank" title="https://juejin.cn/post/7111225695262474277">通用型Resize,Drag,Rotate组件内容解析</a></li>
<li><a href="https://juejin.cn/post/7140581044113113118" target="_blank" title="https://juejin.cn/post/7140581044113113118">基于WEB的可视化PPT制作扩展篇-动画时间轴实现</a></li>
</ol>
<h2 data-id="heading-1">内容分析</h2>
<p>通过对PPT的动画播放分析，我们可以发现以下几个点：</p>
<ol>
<li>控件过渡动画出现前，会执行PPT页面进入的过渡效果，当PPT页面进入完成之后，才会执行拥有动画的控件的动画效果。</li>
<li>有的控件是通过点击出来后进行显示的，也就是通过主动触发的方式进入、离开；而有的控件则是通过自动进入、离开来显示过渡效果的。</li>
<li>有的控件还可以新增强调效果(这里不完成该内容)。</li>
<li>自动展示的控件如果是跟在点击触发的控件之后的话，也会因为未点击而不可呈现。</li>
<li>可以支持一下全部显示，跳过控件动画过渡。</li>
<li>支持鼠标滚轮调整控件显示(暂时也不支持)。</li>
<li>可以返回上一次的动画过渡效果执行之前的状态。</li>
</ol>
<p>上面就是对PPT控件动画过渡的内容分析，除了上述分析之外，我还增加了一些小功能</p>
<ol>
<li>可以在自动控件过渡效果连续执行的时候，暂停执行，然后再开始执行的功能。</li>
<li>快进功能，可以按照倍速播放的效果，加快控件展示进度。</li>
<li>在任意阶段都可以重置，然后从头开始执行。</li>
</ol>
<h2 data-id="heading-2">具体实现</h2>
<p>内容分析完成后，我们就可以来进行具体实现了，这里先只是一个测试的类的实现，还未接入具体的数据，我们可以先用模拟数据进行测试。</p>
<p>然后开始来实现这个功能。</p>
<h3 data-id="heading-3">类设置</h3>
<p>我们需要用一个<code>class</code>来控制，我们把这个class叫做<code>ImplementAnimate</code></p>
<h4 data-id="heading-4">参数及类型定义</h4>
<p>然后就来定义一些参数和参数类型来供我们使用。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> <span class="hljs-title class_">Animate</span> = &#123;
    <span class="hljs-attr">time</span>: <span class="hljs-built_in">number</span>,
    <span class="hljs-attr">action</span>: <span class="hljs-built_in">string</span>,
    options?: <span class="hljs-built_in">any</span>
&#125;
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@type</span> AnimateType 控件动画内容
 * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">Animate</span>&#125; enter 控件标识
 * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">Animate</span>&#125; leave 执行类型
 */</span>
<span class="hljs-keyword">type</span> <span class="hljs-title class_">AnimateType</span> = &#123;
    enter?: <span class="hljs-title class_">Animate</span>,
    leave?: <span class="hljs-title class_">Animate</span>
&#125;
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@type</span> AnimateList 动画可视化列表显示
 * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">string</span>&#125; itemIndex 控件标识
 * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">string</span>&#125; type 执行类型
 * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">string</span>&#125; icon 执行内容图标
 * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">string</span>&#125; mode 触发方式
 */</span>
<span class="hljs-keyword">type</span> <span class="hljs-title class_">AnimateList</span> = &#123;
    <span class="hljs-attr">itemIndex</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">icon</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'in'</span> | <span class="hljs-string">'out'</span>,
    <span class="hljs-attr">trigger</span>: <span class="hljs-string">'click'</span> | <span class="hljs-string">'auto'</span>
&#125;
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@type</span> AnimateOrder 动画执行属性
 * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">AnimateList</span>&#125;
 * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">Animate</span>&#125; action 动画属性
 */</span>
<span class="hljs-keyword">type</span> <span class="hljs-title class_">AnimateOrder</span> = <span class="hljs-title class_">AnimateList</span> & &#123; <span class="hljs-attr">action</span>: <span class="hljs-title class_">Animate</span> &#125;
<span class="hljs-keyword">type</span> <span class="hljs-title class_">PageAnimateAction</span> = &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">time</span>: <span class="hljs-built_in">number</span>,
    <span class="hljs-attr">status</span>: <span class="hljs-built_in">any</span>,
&#125;
<span class="hljs-keyword">type</span> <span class="hljs-title class_">AnimatePage</span> = &#123;
    <span class="hljs-attr">in</span>: <span class="hljs-title class_">PageAnimateAction</span>,
    <span class="hljs-attr">out</span>: <span class="hljs-title class_">PageAnimateAction</span>
&#125;

<span class="hljs-keyword">class</span> <span class="hljs-title class_">ImplementAnimate</span> &#123;
    <span class="hljs-comment">/**
     * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">Map<string, AnimateOrder></span>&#125; autoImplementStack 自动播放任务栈
     * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">Map<string, AnimateOrder></span>&#125; activeTrigger 主动触发任务栈
     * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">Map<number, AnimateOrder></span>&#125; execuationOrder 顺序执行等待栈
     * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">Map<string, AnimateOrder></span>&#125; execuatedStack 已执行任务栈
     * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">AnimateList[]</span>&#125; showList 动画展示列表数据
     * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">string</span>&#125; status 当前动画进行状态
     * <span class="hljs-doctag">@property</span> &#123;<span class="hljs-type">number</span>&#125; actionSpeed 播放速度
     */</span>
    <span class="hljs-attr">autoImplementStack</span>: <span class="hljs-title class_">Map</span><<span class="hljs-built_in">string</span>, <span class="hljs-title class_">AnimateOrder</span>>
    <span class="hljs-attr">activeTrigger</span>: <span class="hljs-title class_">Map</span><<span class="hljs-built_in">string</span>, <span class="hljs-title class_">AnimateOrder</span>>
    <span class="hljs-attr">execuationOrder</span>: <span class="hljs-title class_">Map</span><<span class="hljs-built_in">number</span>, <span class="hljs-title class_">AnimateOrder</span>>
    <span class="hljs-attr">showList</span>: <span class="hljs-title class_">AnimateList</span>[]
    <span class="hljs-attr">execuatedStack</span>: <span class="hljs-title class_">Map</span><<span class="hljs-built_in">number</span>, <span class="hljs-title class_">AnimateOrder</span>>
    <span class="hljs-attr">pageAnimate</span>: <span class="hljs-title class_">AnimatePage</span>
    <span class="hljs-attr">status</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">actionSpeed</span>: <span class="hljs-built_in">number</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里我定义了两个栈，专门用来分别存储自动执行的动画效果与点击触发的动画执行效果，分别是<code>autoImplementStack</code>与<code>activeTrigger</code>。</p>
<blockquote>
<p>不过后来发现确实没啥必要分出两个，因为我们最后可以通过mode来区分触发方式。</p>
</blockquote>
<p>一个等待执行的顺序栈<code>execuationOrder</code>与一个记录已经执行的任务栈<code>execuatedStack</code>。</p>
<p>还定义了一个<code>pageAnimate</code>用来记录页面过渡效果，而且这个页面过渡效果的执行是独立于控件动画执行的。</p>
<p>最后就是两个比较重要的参数，一个是记录状态的<code>status</code>，以及一个用来记录播放速度的<code>actionSpeed</code>了。</p>
<h4 data-id="heading-5">函数定义</h4>
<p>有了参数和类型后，我们需要定义一些函数，来完成我们的需求。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">class</span> <span class="hljs-title class_">ImplementAnimate</span> &#123;
    setPageAnimate!: <span class="hljs-function">(<span class="hljs-params">pageAnimate: PageAnimate</span>) =></span> <span class="hljs-built_in">void</span>
    setItemAnimate!: <span class="hljs-function">(<span class="hljs-params">itemAnimate: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">void</span>
    playAnimate!: <span class="hljs-function">(<span class="hljs-params">animateList: &#123; order: <span class="hljs-built_in">number</span>[], animate: AnimateOrder[] &#125;, isClick?: <span class="hljs-built_in">boolean</span></span>) =></span> <span class="hljs-built_in">void</span>
    playPage!: <span class="hljs-function">() =></span> <span class="hljs-title class_">Promise</span><<span class="hljs-built_in">boolean</span>>
    <span class="hljs-attr">setTask</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>
    <span class="hljs-attr">runTask</span>: <span class="hljs-keyword">async</span> () => <span class="hljs-built_in">void</span>
    <span class="hljs-attr">parseTask</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>
    <span class="hljs-attr">quickRunning</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>
    <span class="hljs-attr">triggerClick</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>
    <span class="hljs-attr">executeNow</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>
    <span class="hljs-attr">restartStack</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>
    <span class="hljs-attr">getAnimateList</span>: <span class="hljs-function">() =></span> &#123; <span class="hljs-attr">order</span>: <span class="hljs-built_in">number</span>[], <span class="hljs-attr">animate</span>: <span class="hljs-title class_">AnimateOrder</span>[] &#125;
    <span class="hljs-attr">clearStack</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p><code>setPageAnimate</code>:  设置页面动画(这里大家用不到的这块内容，可以改成设置自己需要的内容)</p>
</li>
<li>
<p><code>setItemAnimate</code>: 设置控件动画效果(这里大家用不到的这块内容，可以改成设置自己需要的内容)</p>
</li>
<li>
<p><code>playAnimate</code>: 运行动画(也就是一个启动时间控制器任务的函数，需要配合下面的<code>runTask</code>,<code>parseTask</code>,<code>triggerClick</code>这三个函数使用)</p>
</li>
<li>
<p><code>playPage</code>: 运行页面动画(这里是因为页面动画的执行是独立于控件动画执行的，会位于开始和结束的位置执行，这里大家可以设置成自己需要特殊执行的任务)</p>
</li>
<li>
<p><code>setTask</code>:设置任务数据，主要是对外暴露的接口函数，用于设置需要执行内容的数据</p>
</li>
<li>
<p><code>runTask</code>: 启动动画展示任务(<strong>重要</strong>)</p>
</li>
<li>
<p><code>parseTask</code>: 暂停动画任务执行(<strong>重要</strong>)</p>
<blockquote>
<p>这里有一点要说明一下，在按下暂停动画执行的时候，如果有正在执行的动画的话，是会先执行完之后在停止执行的。</p>
</blockquote>
</li>
<li>
<p><code>quickRunning</code>: 加快执行速度</p>
</li>
<li>
<p><code>triggerClick</code>: 触发点击执行任务(<strong>重要</strong>)</p>
</li>
<li>
<p><code>executeNow</code>: 立即完成全部剩余任务</p>
</li>
<li>
<p><code>restartStack</code>: 重置动画执行任务，进入初始状态</p>
</li>
<li>
<p><code>getAnimateList</code>: 获取等待执行动画内容列表</p>
</li>
<li>
<p><code>clearStack</code>: 清空任务栈</p>
</li>
</ol>
<p>上面这些大概就是我们需要实现的函数啦，下面是一张动画执行流程图，借助着流程图，我们就可以去实现我们函数的代码。</p>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed00961d3f6a4785bf201a7c744f2f69~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="animate_process" loading="lazy" referrerpolicy="no-referrer">
<p>画的也不是特别好，大家凑合看着😂。但是也基本知道了整个流程啦，通过控制status的改变，来推进整个任务进程的进行。</p>
<p>接下来就是来实现几个比较关键的函数。</p>
<h5 data-id="heading-6">playPage</h5>
<p><code>playPage</code>函数主要是用来进行页面切换时的等待进程，我们需要等待页面过渡效果完成之后，再让控件进入，所以我们需要等待其完成后在进行流程执行，所以这里的<code>playPage</code>函数我们可以让它返回一个<code>Promise</code>对象，这样就可以让外部调用函数使用<code>await</code>进行等待了。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> playPage = <span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-variable language_">this</span>: <span class="hljs-built_in">any</span></span>): <span class="hljs-title class_">Promise</span><<span class="hljs-built_in">boolean</span>> &#123;
    <span class="hljs-keyword">let</span> <span class="hljs-attr">animate</span>: <span class="hljs-title class_">PageAnimateAction</span>;
    <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> === <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">PageIn</span>) &#123;
        animate = <span class="hljs-variable language_">this</span>.<span class="hljs-property">pageAnimate</span>.<span class="hljs-property">in</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
        animate = <span class="hljs-variable language_">this</span>.<span class="hljs-property">pageAnimate</span>.<span class="hljs-property">out</span>;
    &#125;
    <span class="hljs-comment">//<span class="hljs-doctag">NOTE:</span> 具体实现后再打开，用来控制显隐的</span>
    <span class="hljs-comment">// animate.status.value = !animate.status.value;</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-title function_">resolve</span>(<span class="hljs-literal">true</span>);
        &#125;, animate.<span class="hljs-property">time</span>)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">playAnimate</h5>
<p><code>playAnimate</code>函数就是uml图中框起来的部分的执行函数啦，也是整个动画运转中最关键的地方，虽然看起来好像很复杂，实际实现起来却非常非常的简单😂，这可能也是我这里的需求比较简单，而且有很多情况没有考虑到的原因，我们其实只需要设置一个setTimeout函数中，进行一个回溯的写法即可完成每一次任务的执行，然后在每一次进入<code>playAnimate</code>函数时，取出当前第一个待执行动画任务，并进行判断即可，然后在进入到setTimeout执行函数中后，对状态进行判断，如果不符合就直接跳出即可。接下来就是代码实现啦：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span> 本文件主要处理动画的定时播放的进行
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">&#123; order: number[], animate: AnimateOrder[] </span>&#125;&#125; info 等待执行任务栈内容
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">boolean</span>&#125; isClick 是否已经由用户主动触发判断, true即为用户主动触发
 */</span>
<span class="hljs-keyword">const</span> playAnimate = <span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-variable language_">this</span>: <span class="hljs-built_in">any</span>, info: &#123; order: <span class="hljs-built_in">number</span>[], animate: AnimateOrder[] &#125;, isClick: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span></span>) &#123;
    <span class="hljs-keyword">let</span> that = <span class="hljs-variable language_">this</span>;
    <span class="hljs-keyword">let</span> animateList = info.<span class="hljs-property">animate</span>;
    <span class="hljs-keyword">let</span> orderList = info.<span class="hljs-property">order</span>;
    <span class="hljs-comment">//<span class="hljs-doctag">NOTE:</span> 判断当前执行动画任务栈是否已经执行完成，如果完成了就直接取消执行即可</span>
    <span class="hljs-keyword">if</span> (animateList.<span class="hljs-property">length</span> === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">PageOut</span>;
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">let</span> <span class="hljs-attr">animateTask</span>: <span class="hljs-built_in">any</span> = animateList.<span class="hljs-title function_">shift</span>();
    <span class="hljs-keyword">let</span> <span class="hljs-attr">order</span>: <span class="hljs-built_in">any</span> = orderList.<span class="hljs-title function_">shift</span>();
    <span class="hljs-comment">//<span class="hljs-doctag">NOTE:</span> 如果当前动画任务为自动触发的或者是点击触发且已经由用户主动点击的话，那么就改变控件显示状态，触发过渡效果，并且维护可执行动画栈</span>
    <span class="hljs-keyword">if</span> (animateTask.<span class="hljs-property">trigger</span> === <span class="hljs-string">'auto'</span> || (animateTask.<span class="hljs-property">trigger</span> === <span class="hljs-string">'click'</span> && isClick)) &#123;
        animateTask.<span class="hljs-property">action</span>.<span class="hljs-property">options</span>.<span class="hljs-property">show</span> = <span class="hljs-literal">true</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuationOrder</span>.<span class="hljs-title function_">delete</span>(order);
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuatedStack</span>.<span class="hljs-title function_">set</span>(order, animateTask);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (animateTask.<span class="hljs-property">trigger</span> === <span class="hljs-string">'click'</span> && !isClick) &#123;
        <span class="hljs-comment">//<span class="hljs-doctag">NOTE:</span> 如果是一个点击触发的动画，且用户未进行点击触发时，终止动画执行，修改动画执行状态</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">WaitTrigger</span>;
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-comment">//README: 这里就需要进行下次任务的等待了，同时这里的时间回去进行计算，因为用户可能会进行加速播放，所以实际持续时间为time / actionSpeed</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">//<span class="hljs-doctag">NOTE:</span> 对状态进行判断，如果状态不可执行，直接返回，如果可以继续执行，就直接进行执行。</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> === <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">PageOut</span>) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-keyword">if</span> (that.<span class="hljs-property">status</span> == <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">Pause</span>) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-keyword">if</span> (that.<span class="hljs-property">status</span> == <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">Running</span>) &#123;
            <span class="hljs-keyword">if</span> (animateList.<span class="hljs-property">length</span> === <span class="hljs-number">0</span>) &#123;
                that.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">PageOut</span>;
                <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'end'</span>, that.<span class="hljs-property">status</span>)
                <span class="hljs-keyword">return</span>;
            &#125;

            <span class="hljs-keyword">return</span> playAnimate.<span class="hljs-title function_">call</span>(that, &#123; <span class="hljs-attr">order</span>: orderList, <span class="hljs-attr">animate</span>: animateList &#125;);
        &#125;
    &#125;, animateTask.<span class="hljs-property">action</span>.<span class="hljs-property">time</span> / <span class="hljs-variable language_">this</span>.<span class="hljs-property">actionSpeed</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们最关键的<code>playAnimate</code>函数就设计好了，接着就是用<code>playAnimate</code>时的几个场景了。</p>
<h5 data-id="heading-8">runTask</h5>
<p><code>runTask</code>函数即执行动画运行函数，它是在两个场景进行使用：1. 起始阶段进行触发 2. 暂停后进行触发。</p>
<p>那么针对这两个阶段，我们就可以来设计<code>runTask</code>函数了。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
* <span class="hljs-doctag">@method</span> runTask 运行动画执行任务
*/</span>
<span class="hljs-keyword">async</span> <span class="hljs-title function_">runTask</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-comment">//<span class="hljs-doctag">NOTE:</span> 首先需要获取动画执行任务栈内容</span>
    <span class="hljs-keyword">let</span> playAnimate = <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">getAnimateList</span>();
    <span class="hljs-comment">//README: 根据当前进行状态判断，如果是ready状态，就还需要去执行pageIn，如果是pause状态，只需要从中断位置继续执行即可</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> === <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">Pause</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">Running</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">playAnimate</span>(playAnimate);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">PageIn</span>;
        <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">pageAnimate</span>.<span class="hljs-property">in</span>.<span class="hljs-property">type</span> != <span class="hljs-string">''</span>) &#123;
            <span class="hljs-keyword">await</span> <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">playPage</span>();
        &#125;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">Running</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">playAnimate</span>(playAnimate);
    &#125;
&#125;

<span class="hljs-comment">/**
* <span class="hljs-doctag">@method</span> getAnimateList 获取播放动画列表
* <span class="hljs-doctag">@return</span> &#123;<span class="hljs-type">&#123; order: number[], animate: AnimateOrder[] </span>&#125;&#125;
*/</span>
<span class="hljs-title function_">getAnimateList</span>(): &#123; <span class="hljs-attr">order</span>: <span class="hljs-built_in">number</span>[], <span class="hljs-attr">animate</span>: <span class="hljs-title class_">AnimateOrder</span>[] &#125; &#123;
    <span class="hljs-keyword">let</span> <span class="hljs-attr">res</span>: &#123; <span class="hljs-attr">order</span>: <span class="hljs-built_in">number</span>[], <span class="hljs-attr">animate</span>: <span class="hljs-title class_">AnimateOrder</span>[] &#125; = &#123; <span class="hljs-attr">order</span>: [], <span class="hljs-attr">animate</span>: [] &#125;;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuationOrder</span>) &#123;
        res.<span class="hljs-property">order</span>.<span class="hljs-title function_">push</span>(key);
    &#125;
    res.<span class="hljs-property">order</span>.<span class="hljs-title function_">sort</span>(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b);
    res.<span class="hljs-property">order</span>.<span class="hljs-property">length</span> != <span class="hljs-number">0</span> && res.<span class="hljs-property">order</span>.<span class="hljs-title function_">forEach</span>(<span class="hljs-function">(<span class="hljs-params">v: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        <span class="hljs-keyword">let</span> <span class="hljs-attr">itemInfo</span>: <span class="hljs-built_in">any</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuationOrder</span>.<span class="hljs-title function_">get</span>(v);
        <span class="hljs-keyword">let</span> <span class="hljs-attr">key</span>: <span class="hljs-built_in">string</span> = itemInfo.<span class="hljs-property">itemIndex</span> + <span class="hljs-string">'-'</span> + itemInfo.<span class="hljs-property">mode</span>;
        <span class="hljs-keyword">let</span> <span class="hljs-attr">task</span>: <span class="hljs-built_in">any</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">activeTrigger</span>.<span class="hljs-title function_">has</span>(key) ? <span class="hljs-variable language_">this</span>.<span class="hljs-property">activeTrigger</span>.<span class="hljs-title function_">get</span>(key) : <span class="hljs-variable language_">this</span>.<span class="hljs-property">autoImplementStack</span>.<span class="hljs-title function_">get</span>(key);
        res.<span class="hljs-property">animate</span>.<span class="hljs-title function_">push</span>(task)
    &#125;)
    <span class="hljs-keyword">return</span> res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">pauseTask</h5>
<p><code>pauseTask</code>暂停动画任务执行函数，这里其实就很简单了，我们只需要将状态进行改变就可以了，但是有一个前提，只有当当前执行状态为<code>running</code>时才可以暂停。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
* <span class="hljs-doctag">@method</span> parseTask 暂停动画执行
*/</span>
<span class="hljs-title function_">pauseTask</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> != <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">Running</span>) &#123;
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">Pause</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">triggerClick</h5>
<p><code>triggerClick</code>函数是用来让用户在主动触发时执行的函数，我们需要在这里告诉<code>playAnimate</code>函数，现在是用户主动触发之后的状态，可以继续执行<code>mode = click</code>的动画任务了。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
* <span class="hljs-doctag">@method</span> triggerClick 触发点击执行
*/</span>
<span class="hljs-title function_">triggerClick</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> !== <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">WaitTrigger</span>) &#123;
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">Running</span>;
    <span class="hljs-comment">//<span class="hljs-doctag">NOTE:</span> 继续执行动画任务栈，同时告诉其是由用户主动触发的</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">playAnimate</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-title function_">getAnimateList</span>(), <span class="hljs-literal">true</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">其余函数书写</h5>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
* <span class="hljs-doctag">@method</span> setTask 设置动画执行任务
* <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">Page | null</span>&#125; pageInfo 页面信息
*/</span>
<span class="hljs-title function_">setTask</span>(<span class="hljs-params">pageInfo: Page | <span class="hljs-literal">null</span></span>) &#123;
    <span class="hljs-keyword">if</span> (!pageInfo) <span class="hljs-keyword">return</span>;
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">setPageAnimate</span>(pageInfo!.<span class="hljs-property">animate</span>);
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">setItemAnimate</span>(pageInfo.<span class="hljs-property">item</span>);
&#125;

<span class="hljs-comment">/**
* <span class="hljs-doctag">@method</span> quickRunning 加速动画执行
*/</span>
<span class="hljs-title function_">quickRunning</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">actionSpeed</span> += <span class="hljs-number">0.5</span>;
&#125;

<span class="hljs-comment">/**
* <span class="hljs-doctag">@method</span> executeNow 立即执行完成
*/</span>
<span class="hljs-title function_">executeNow</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-comment">//<span class="hljs-doctag">NOTE:</span> 这里代码写的很冗余，后期会修改掉</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuationOrder</span>) &#123;
        <span class="hljs-keyword">let</span> <span class="hljs-attr">index</span>: <span class="hljs-built_in">string</span> = value.<span class="hljs-property">itemIndex</span> + <span class="hljs-string">'-'</span> + value.<span class="hljs-property">mode</span>;
        <span class="hljs-keyword">let</span> <span class="hljs-attr">task</span>: <span class="hljs-built_in">any</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">activeTrigger</span>.<span class="hljs-title function_">has</span>(index) ? <span class="hljs-variable language_">this</span>.<span class="hljs-property">activeTrigger</span>.<span class="hljs-title function_">get</span>(index) : <span class="hljs-variable language_">this</span>.<span class="hljs-property">autoImplementStack</span>.<span class="hljs-title function_">get</span>(index);
        task.<span class="hljs-property">action</span>.<span class="hljs-property">options</span>.<span class="hljs-property">show</span> = <span class="hljs-literal">true</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuatedStack</span>.<span class="hljs-title function_">set</span>(key, value)
    &#125;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuationOrder</span>.<span class="hljs-title function_">clear</span>();
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">PageOut</span>;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuatedStack</span>);
&#125;
<span class="hljs-comment">/**
* <span class="hljs-doctag">@method</span> restartTask 重置动画执行
*/</span>
<span class="hljs-title function_">restartTask</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuatedStack</span>) &#123;
        <span class="hljs-comment">//<span class="hljs-doctag">NOTE:</span> 这里代码写的很冗余，后期会修改掉</span>
        <span class="hljs-keyword">let</span> <span class="hljs-attr">index</span>: <span class="hljs-built_in">string</span> = value.<span class="hljs-property">itemIndex</span> + <span class="hljs-string">'-'</span> + value.<span class="hljs-property">mode</span>;
        <span class="hljs-keyword">let</span> <span class="hljs-attr">task</span>: <span class="hljs-built_in">any</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">activeTrigger</span>.<span class="hljs-title function_">has</span>(index) ? <span class="hljs-variable language_">this</span>.<span class="hljs-property">activeTrigger</span>.<span class="hljs-title function_">get</span>(index) : <span class="hljs-variable language_">this</span>.<span class="hljs-property">autoImplementStack</span>.<span class="hljs-title function_">get</span>(index);
        task.<span class="hljs-property">action</span>.<span class="hljs-property">options</span>.<span class="hljs-property">show</span> = <span class="hljs-literal">false</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuationOrder</span>.<span class="hljs-title function_">set</span>(key, value)
    &#125;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuatedStack</span>.<span class="hljs-title function_">clear</span>();
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">Ready</span>;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">pageAnimate</span>.<span class="hljs-property">in</span>.<span class="hljs-property">status</span> = <span class="hljs-literal">false</span>;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">pageAnimate</span>.<span class="hljs-property">out</span>.<span class="hljs-property">status</span> = <span class="hljs-literal">true</span>;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuationOrder</span>)
&#125;

<span class="hljs-comment">/**
* <span class="hljs-doctag">@method</span> getAnimateList 获取播放动画列表
* <span class="hljs-doctag">@return</span> &#123;<span class="hljs-type">AnimateList[]</span>&#125;
*/</span>
<span class="hljs-title function_">getAnimateList</span>(): &#123; <span class="hljs-attr">order</span>: <span class="hljs-built_in">number</span>[], <span class="hljs-attr">animate</span>: <span class="hljs-title class_">AnimateOrder</span>[] &#125; &#123;
    <span class="hljs-keyword">let</span> <span class="hljs-attr">res</span>: &#123; <span class="hljs-attr">order</span>: <span class="hljs-built_in">number</span>[], <span class="hljs-attr">animate</span>: <span class="hljs-title class_">AnimateOrder</span>[] &#125; = &#123; <span class="hljs-attr">order</span>: [], <span class="hljs-attr">animate</span>: [] &#125;;
    <span class="hljs-comment">//<span class="hljs-doctag">NOTE:</span> 这里是我自己的问题，书写错误了，导致这里要多处理一些，大家可以根据自己的需要进行修改</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuationOrder</span>) &#123;
        res.<span class="hljs-property">order</span>.<span class="hljs-title function_">push</span>(key);
    &#125;
    res.<span class="hljs-property">order</span>.<span class="hljs-title function_">sort</span>(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b);
    res.<span class="hljs-property">order</span>.<span class="hljs-property">length</span> != <span class="hljs-number">0</span> && res.<span class="hljs-property">order</span>.<span class="hljs-title function_">forEach</span>(<span class="hljs-function">(<span class="hljs-params">v: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        <span class="hljs-keyword">let</span> <span class="hljs-attr">itemInfo</span>: <span class="hljs-built_in">any</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuationOrder</span>.<span class="hljs-title function_">get</span>(v);
        <span class="hljs-keyword">let</span> <span class="hljs-attr">key</span>: <span class="hljs-built_in">string</span> = itemInfo.<span class="hljs-property">itemIndex</span> + <span class="hljs-string">'-'</span> + itemInfo.<span class="hljs-property">mode</span>;
        <span class="hljs-keyword">let</span> <span class="hljs-attr">task</span>: <span class="hljs-built_in">any</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">activeTrigger</span>.<span class="hljs-title function_">has</span>(key) ? <span class="hljs-variable language_">this</span>.<span class="hljs-property">activeTrigger</span>.<span class="hljs-title function_">get</span>(key) : <span class="hljs-variable language_">this</span>.<span class="hljs-property">autoImplementStack</span>.<span class="hljs-title function_">get</span>(key);
        res.<span class="hljs-property">animate</span>.<span class="hljs-title function_">push</span>(task)
    &#125;)
    <span class="hljs-keyword">return</span> res;
&#125;
<span class="hljs-comment">/**
* <span class="hljs-doctag">@method</span> cleatStack 清空动画栈全部内容
*/</span>
<span class="hljs-title function_">clearStack</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">autoImplementStack</span>.<span class="hljs-title function_">clear</span>();
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">activeTrigger</span>.<span class="hljs-title function_">clear</span>();
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuationOrder</span>.<span class="hljs-title function_">clear</span>();
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">showList</span> = [];
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">execuatedStack</span>.<span class="hljs-title function_">clear</span>();
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">status</span> = <span class="hljs-title class_">AnimateStatus</span>.<span class="hljs-property">Ready</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好啦，到这里我们其实就已经把所有内容处理完了，具体代码整体的实现，可以看以下几个地址，然后大家可以复制到自己的项目里面进行实验。</p>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFlyBirdHeight%2Fadsionliblog_manager%2Fblob%2Fmain%2Fsrc%2Fmodules%2Fperson%2Fpresentation%2Fanimation%2Fimplement.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FlyBirdHeight/adsionliblog_manager/blob/main/src/modules/person/presentation/animation/implement.ts" ref="nofollow noopener noreferrer">implement.ts</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFlyBirdHeight%2Fadsionliblog_manager%2Fblob%2Fmain%2Fsrc%2Fmodules%2Fperson%2Fpresentation%2Fanimation%2Futils%2Ftimeline.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FlyBirdHeight/adsionliblog_manager/blob/main/src/modules/person/presentation/animation/utils/timeline.ts" ref="nofollow noopener noreferrer">timeline.ts</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFlyBirdHeight%2Fadsionliblog_manager%2Fblob%2Fmain%2Fsrc%2Fviews%2Fsite%2Ftest%2Fanimate.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FlyBirdHeight/adsionliblog_manager/blob/main/src/views/site/test/animate.vue" ref="nofollow noopener noreferrer">animate.vue</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFlyBirdHeight%2Fadsionliblog_manager%2Fblob%2Fmain%2Fsrc%2Fviews%2Fsite%2Ftest%2Fdata%2Fanimate_test.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FlyBirdHeight/adsionliblog_manager/blob/main/src/views/site/test/data/animate_test.ts" ref="nofollow noopener noreferrer">animate_test.ts 这个是测试数据</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFlyBirdHeight%2Fadsionliblog_manager%2Fblob%2Fmain%2Fsrc%2Fmodules%2Fperson%2Fpresentation%2Fanimation%2Fenum%2Fanimate_enum.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FlyBirdHeight/adsionliblog_manager/blob/main/src/modules/person/presentation/animation/enum/animate_enum.ts" ref="nofollow noopener noreferrer">animate_enum.ts</a></li>
</ol>
<blockquote>
<p>里面有些数据类型大家可以自己进行修改，不需要使用我这边的数据类型</p>
</blockquote>
<h2 data-id="heading-12">效果展示</h2>
<p>这里由于还没有一个具体的实现，所以我们可以通过控制台的输出来看一下整个工作流程</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9d4246dc4254c02b4d9ab8e18e07bb1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="working.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这里是因为我再转成gif时加了3倍速，所以会导致快进之后会有点鬼畜</p>
</blockquote>
<h2 data-id="heading-13">总结</h2>
<p>这是躺平之后的第一个完成的内容了，虽然之前也有些了不少东西，但是也还没梳理过，比如说在改用tsx之后遇到的很多问题及踩的坑，下一篇也会整理出来给大家，避免重复踩坑😂。</p>
<p>果然还是学习和写代码是真的快乐，当然啦，如果工作了，肯定干不了这么多自己想干的事情了（虽然真的想去大厂学习更多的知识，但是没有机会嘞），所以还是润回家了，然后继续写好玩的代码分享给大家，冲呀。</p></div>  
</div>
            