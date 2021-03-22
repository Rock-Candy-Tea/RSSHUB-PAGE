
---
title: 'iOS14开发-UIViewController'
categories: 
    - 编程
    - 掘金
    - 热门

author: 掘金
comments: false
date: Sun, 21 Feb 2021 22:07:34 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">介绍</h2>
<p>UIViewController 可以理解为 App 的界面，负责管理 UIView 中显示的内容和用户的交互，主要有以下作用：</p>
<ul>
<li>负责创建和管理 UIView。</li>
<li>响应用户与视图的交互。</li>
<li>负责界面的切换与传值。</li>
<li>响应设备的方向变化。</li>
<li>有一些特殊的视图控制器（导航控制器、标签栏控制器）可以更加方便和规范地管理 UIView。</li>
</ul>
<h2 data-id="heading-1">创建</h2>
<h3 data-id="heading-2">storyboard</h3>
<ul>
<li>初始化箭头指向的 UIViewController。</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> vc <span class="hljs-operator">=</span> <span class="hljs-type">UIStoryboard</span>(name: <span class="hljs-string">"storyboard名"</span>, bundle: <span class="hljs-literal">nil</span>).instantiateInitialViewController()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>初始化其他的 UIViewController。</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> vc <span class="hljs-operator">=</span> <span class="hljs-type">UIStoryboard</span>(name: <span class="hljs-string">"storyboard名"</span>, bundle: <span class="hljs-literal">nil</span>).instantiateViewController(withIdentifier: <span class="hljs-string">"Storyboard ID"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">纯代码</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> vc <span class="hljs-operator">=</span> <span class="hljs-type">UIViewController</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">xib</h3>
<p>这种方式本质是 xib 创建 UIView，然后让这个 UIView 成为 UIViewController 的默认 View。</p>
<ul>
<li>创建 UIViewController 的时候勾选了<code>Also create XIB file</code>，可以直接通过下面两种方式初始化：</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 方式一</span>
<span class="hljs-keyword">let</span> vc <span class="hljs-operator">=</span> <span class="hljs-type">UIViewController</span>()

<span class="hljs-comment">// 方式二</span>
<span class="hljs-keyword">let</span> vc <span class="hljs-operator">=</span> <span class="hljs-type">UIViewController</span>(nibName: <span class="hljs-string">"xib的名字"</span>, bundle: <span class="hljs-literal">nil</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果 UIViewController 与 xib 分别创建，直接使用上面的两种方式会报错，因为这种方式还需要自己处理 2 件事：</li>
</ul>
<p>（1）将 xib 文件 的<code>File’s Owner</code>的类绑定为 UIViewController。
（2）将<code>File’s Owner</code>的<code>view</code>属性设置为<code>xib</code>文件（拽线设置即可）。</p>
<h2 data-id="heading-5">view属性</h2>
<p>在<strong>入门知识</strong>里初步介绍了 UIViewController 与其属性<code>view</code>的关系，其实它们之间的关系没有那么简单，需要进一步分析。</p>
<h3 data-id="heading-6">生命周期顺序</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">init</span><span class="hljs-operator">、</span><span class="hljs-function"><span class="hljs-keyword">init</span>(nibName<span class="hljs-operator">...</span>)</span>（初始化<span class="hljs-operator">、</span>分配内存）—<span class="hljs-operator">></span> loadView（加载view）—<span class="hljs-operator">></span> viewDidLoad（view已经加载）—<span class="hljs-operator">></span> viewWillAppear（view即将显示）—<span class="hljs-operator">></span> viewWillLayoutSubviews（将要布局子view）—<span class="hljs-operator">></span> viewDidLayoutSubviews（已经布局子view）—<span class="hljs-operator">></span> viewDidAppear（view已经显示）—<span class="hljs-operator">></span> viewWillDisappear（view即将消失）—<span class="hljs-operator">></span> viewDidDisappear（view已经消失）—<span class="hljs-operator">></span> dealloc（释放内存）
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">延迟加载</h3>
<p>UIViewController 的 view 的延迟加载：第一次使用的时候才会去加载，并不是创建 UIViewController 时加载。</p>
<ul>
<li>验证：通过纯代码跳转时发现屏幕黑色且卡顿，设置颜色后正常。</li>
</ul>
<h3 data-id="heading-8">loadView方法</h3>
<ul>
<li>用于创建 UIViewController 的 view。</li>
<li>当 UIViewController 访问 view 时如果发现为 nil，就会调用 loadView 方法。</li>
<li>loadView 方法执行完会自动执行 viewDidLoad。</li>
<li>loadView 方法大概的实现思路如下：</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">loadView</span>()</span> &#123;   
    <span class="hljs-comment">// 如果UIViewController是通过storyboard创建的，从storyboard中加载视图来创建view</span>
    <span class="hljs-keyword">if</span> storyboard创建 &#123;
        <span class="hljs-comment">// ...</span>
        <span class="hljs-keyword">return</span>
    &#125;
    
     <span class="hljs-comment">// 如果UIViewController是通过xib创建的，从xib中加载视图来创建view</span>
    <span class="hljs-keyword">if</span> xib创建 &#123;
        <span class="hljs-comment">// ...</span>
        <span class="hljs-keyword">return</span>
    &#125;
    
    <span class="hljs-comment">// 如果上面都不是，则会创建一个普通的view视图</span>
    <span class="hljs-keyword">let</span> view <span class="hljs-operator">=</span> <span class="hljs-type">UIView</span>(frame: <span class="hljs-type">UIScreen</span>.main.bounds)    
    <span class="hljs-keyword">self</span>.view <span class="hljs-operator">=</span> view
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">重写loadView方法</h4>
<ul>
<li>该方法要么不重写，如果重写一定要注意：
<ul>
<li><strong>必须</strong>在方法里给 UIViewController 的 view 赋值。</li>
<li><strong>不要</strong>调用<code>super.loadView()</code>。</li>
<li><strong>不要</strong>手动调用该方法。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">loadView</span>()</span> &#123;
    <span class="hljs-keyword">let</span> myView <span class="hljs-operator">=</span> <span class="hljs-type">UIView</span>(frame: <span class="hljs-type">UIScreen</span>.main.bounds)
    view <span class="hljs-operator">=</span> myView
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>一旦重写，其他创建 view 的方式都会失效，因为决定 UIViewController 的 view 优先级为：loadView > storyboard > nibName > xib。</li>
</ul>
<h2 data-id="heading-10">跳转</h2>
<p>从一个 UIViewController 跳转到另一个 UIViewController 有两种方式，分别为<strong>模态跳转</strong>和<strong>导航跳转</strong>。</p>
<h3 data-id="heading-11">模态跳转</h3>
<h4 data-id="heading-12">storyboard</h4>
<ul>
<li>直接拽线，选择<code>Present Modally</code>，这根线是一个 UIStoryboardSegue 对象（简称 Segue），可以设置相关的属性。</li>
<li>自动型 Segue
<ul>
<li>直接跳转，无需条件。</li>
<li>通过当前 UIViewController 某个具体的控件（如按钮）拽线到另一个 UIViewController。</li>
</ul>
</li>
<li>手动型 Segue
<ul>
<li>从当前 UIViewController 拽线到另一个 UIViewController，需要给这根线设置<code>identifier</code>。</li>
<li>在程序中需要跳转的地方调用<code>performSegue(withIdentifier: , sender:)</code>方法完成跳转。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-13">纯代码</h4>
<ul>
<li>跳转界面：<code>present</code>。</li>
<li>返回界面：<code>dismiss</code>。</li>
<li>iOS 13 之后，模态跳转并非全屏显示，如果需要全屏显示，需要手动设置。</li>
</ul>
<h4 data-id="heading-14">两个概念</h4>
<ul>
<li><code>presentedViewController</code>: 被 present 的控制器。</li>
<li><code>presentingViewController</code>：正在 presenting 的控制器。</li>
</ul>
<h3 data-id="heading-15">导航跳转</h3>
<p>这种操作的前提是 UIViewController 包含在 UINavigationController 中。</p>
<h4 data-id="heading-16">storyboard</h4>
<ul>
<li>直接拽线，选择<code>Show</code>。</li>
<li>自动型 Segue 和 手动型 Segue 跟模态跳转一样。</li>
</ul>
<h4 data-id="heading-17">纯代码</h4>
<ul>
<li>跳转界面
<ul>
<li><code>navigationController?.pushViewController</code>。</li>
</ul>
</li>
<li>返回界面
<ul>
<li>左上角的返回按钮。</li>
<li>屏幕边缘滑动。</li>
<li><code>navigationController?.popViewController</code>。</li>
</ul>
</li>
</ul>
<h2 data-id="heading-18">传值</h2>
<h3 data-id="heading-19">顺向传值</h3>
<p>顺向传值即按照 UIViewController 跳转的顺序进行传值，比如控制器A跳转到控制器B，A向B的传值就是顺向传值。顺向传值只需要在目标控制器中声明需要接收的参数，然后在源控制器中进行传值即可。</p>
<ul>
<li>storyboard 方式。</li>
<li>代码方式。</li>
</ul>
<h3 data-id="heading-20">逆向传值</h3>
<p>逆向传值即按照 UIViewController 跳转的顺序反向进行传值，比如控制器A跳转到控制器B，控制器B在返回控制器A时进行传值，这种方式就是逆向传值。逆向传值不能像顺向传值那样简单进行，需要借助于下面三种方式。</p>
<h4 data-id="heading-21">代理</h4>
<p>代理模式需要弄清楚被代理对象和代理对象，然后按照下面的规范进行。</p>
<ul>
<li>被代理对象（需要传值的 UIViewController）
<ul>
<li>声明协议，在协议中定义传值方法，方法的参数个数与类型取决于需要传值的个数和类型。</li>
<li>UIViewController 中声明一个代理属性。</li>
<li>在需要传值的地方调用代理属性的方法完成传值。</li>
</ul>
</li>
<li>代理对象（接收值的 UIViewController）
<ul>
<li>实现被代理对象声明的协议，实现协议中的方法，拿到传过来的值进行使用。</li>
<li>需要设置当前的 UIViewController 为被代理 UIViewController 中的代理属性。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-22">闭包</h4>
<p>可以理解为代理模式中<strong>协议的闭包替代</strong>，比代理模式更简单。</p>
<ul>
<li>需要传值的 UIViewController
<ul>
<li>声明一个闭包属性，闭包的参数个数与类型取决于需要传值的个数和类型，闭包的返回值一般为 Void。</li>
<li>在需要传值的地方调用闭包完成传值。</li>
</ul>
</li>
<li>接收值的 UIViewController
<ul>
<li>实现需要传值的 UIViewController 中的闭包属性，在闭包的实现中拿到传过来的值进行使用。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-23">通知</h4>
<ul>
<li>接收值的 UIViewController 通过监听通知捕获传过来的值。</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"> <span class="hljs-type">NotificationCenter</span>.default.addObserver(<span class="hljs-keyword">self</span>, selector: #selector(handlerNoti), name: <span class="hljs-type">NSNotification</span>.<span class="hljs-type">Name</span>(<span class="hljs-string">"abc"</span>), object: <span class="hljs-literal">nil</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>需要传值的 UIViewController 将值通过通知的方式发送出去。</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-type">NotificationCenter</span>.default.post(name: <span class="hljs-type">NSNotification</span>.<span class="hljs-type">Name</span>(<span class="hljs-string">"abc"</span>), object: <span class="hljs-literal">nil</span>, userInfo: [<span class="hljs-string">"info"</span> : inputTf.text<span class="hljs-operator">!</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>需要<strong>先监听，后发送</strong>。</li>
<li>iOS 9 之后 NSNotificationCenter 无需手动移除观察者。</li>
</ul>
<h2 data-id="heading-24">常见ViewController</h2>
<h3 data-id="heading-25">UIAlertController</h3>
<ul>
<li>警告（对话框）控制器。</li>
<li>用一个对话框进行信息的提示，通过模态形式弹出。</li>
<li>有两种样式：<code>alert</code>和<code>actionSheet</code>。</li>
<li>按钮通过 UIAlertAction 添加，有 3 种样式：<code>default</code>、<code>cancel</code>和<code>destructive</code>，一个 UIAlertController 中只能有一个<code>cancel</code>样式的 UIAlertAction。</li>
<li>基本使用</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ViewController</span>: <span class="hljs-title">UIViewController</span> </span>&#123;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">viewDidLoad</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.viewDidLoad()
    &#125;

    <span class="hljs-keyword">@IBAction</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">showAlert</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">sender</span>: <span class="hljs-keyword">Any</span>)</span> &#123;
        <span class="hljs-keyword">let</span> alertVC <span class="hljs-operator">=</span> <span class="hljs-type">UIAlertController</span>(title: <span class="hljs-string">"温馨提示"</span>, message: <span class="hljs-string">"天气转凉，大家注意保暖，小心感冒"</span>, preferredStyle: .alert)

        <span class="hljs-keyword">let</span> ok <span class="hljs-operator">=</span> <span class="hljs-type">UIAlertAction</span>(title: <span class="hljs-string">"OK"</span>, style: .default) &#123; <span class="hljs-keyword">_</span> <span class="hljs-keyword">in</span>
            <span class="hljs-built_in">print</span>(<span class="hljs-string">"点击了ok"</span>)
        &#125;

        <span class="hljs-keyword">let</span> cancel <span class="hljs-operator">=</span> <span class="hljs-type">UIAlertAction</span>(title: <span class="hljs-string">"Cancel"</span>, style: .cancel) &#123; <span class="hljs-keyword">_</span> <span class="hljs-keyword">in</span>
            <span class="hljs-built_in">print</span>(<span class="hljs-string">"点击了cancel"</span>)
        &#125;

        alertVC.addAction(ok)
        alertVC.addAction(cancel)

        present(alertVC, animated: <span class="hljs-literal">true</span>, completion: <span class="hljs-literal">nil</span>)
    &#125;

    <span class="hljs-keyword">@IBAction</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">showSheet</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">sender</span>: <span class="hljs-keyword">Any</span>)</span> &#123;
        <span class="hljs-keyword">let</span> alertVC <span class="hljs-operator">=</span> <span class="hljs-type">UIAlertController</span>(title: <span class="hljs-string">"选择头像"</span>, message: <span class="hljs-string">"请选择合适的方式来处理"</span>, preferredStyle: .actionSheet)

        <span class="hljs-keyword">let</span> ok <span class="hljs-operator">=</span> <span class="hljs-type">UIAlertAction</span>(title: <span class="hljs-string">"相册"</span>, style: .default) &#123; <span class="hljs-keyword">_</span> <span class="hljs-keyword">in</span>
            <span class="hljs-built_in">print</span>(<span class="hljs-string">"用户选择了相册"</span>)
        &#125;

        <span class="hljs-keyword">let</span> des <span class="hljs-operator">=</span> <span class="hljs-type">UIAlertAction</span>(title: <span class="hljs-string">"拍照"</span>, style: .destructive) &#123; <span class="hljs-keyword">_</span> <span class="hljs-keyword">in</span>
            <span class="hljs-built_in">print</span>(<span class="hljs-string">"用户选择了拍照"</span>)
        &#125;

        <span class="hljs-keyword">let</span> cancel <span class="hljs-operator">=</span> <span class="hljs-type">UIAlertAction</span>(title: <span class="hljs-string">"取消"</span>, style: .cancel) &#123; <span class="hljs-keyword">_</span> <span class="hljs-keyword">in</span>
            <span class="hljs-built_in">print</span>(<span class="hljs-string">"点击了取消"</span>)
        &#125;

        alertVC.addAction(ok)
        alertVC.addAction(des)
        alertVC.addAction(cancel)

        present(alertVC, animated: <span class="hljs-literal">true</span>, completion: <span class="hljs-literal">nil</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>登录案例：用 UIAlertController 代替 print 打印。</li>
</ul>
<h3 data-id="heading-26">UINavigationController</h3>
<ul>
<li>导航控制器。</li>
<li>可以展示多个 UIViewController，这些 UIViewController 是层级关系。</li>
<li>它的 View 由三部分组成，最上面的<code>UINavigationBar</code>，最下面默认隐藏的<code>UIToolBar</code>，中间是 UIViewController 的<code>view</code>。</li>
<li>通过栈管理 UIViewController：先进后出。
<ul>
<li><code>pushViewController</code>：压栈。</li>
<li><code>popViewController</code>：出栈。</li>
</ul>
</li>
<li>通过 UINavigationItem 设置 title、leftBarButtonItem、rightBarButtonItem等。</li>
</ul>
<h4 data-id="heading-27">UINavigationBar和UINavigationItem的关系</h4>
<ul>
<li><code>UINavigationBar</code>是 UINavigationController 的属性，其属性设置会影响内部所有的 UIViewController。</li>
<li><code>UINavigationItem</code>是 UIViewController 的属性，用于配置当前 UIViewController 显示时<code>UINavigationBar</code>上显示的内容。</li>
<li><code>UINavigationBar</code>内部也维持一个栈，栈中存放的是一个个 <code>UINavigationItem</code>。当一个 UIViewController push 到  UINavigationController 时，它的<code>UINavigationItem</code>也会被 push 进 <code>UINavigationBar</code>的栈。因此<code>UINavigationBar</code>的栈和  UINavigationController 的栈一一对应。</li>
</ul>
<h4 data-id="heading-28">UINavigationBar 的内容显示</h4>
<h5 data-id="heading-29">标题</h5>
<ul>
<li>如果当前 UIViewController 设置了<code>titleView</code>属性，则展示标题视图。</li>
<li>如果当前 UIViewController 设置了<code>title</code>属性，则显示标题文字。</li>
<li>如果都没设置，则显示空白。</li>
<li>iOS11 之后可以设置大标题。可以通过 storyboard 直接设置，也可以通过如下的代码设置：</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 所有界面显示大标题</span>
navigationController<span class="hljs-operator">?</span>.navigationBar.prefersLargeTitles <span class="hljs-operator">=</span> <span class="hljs-literal">true</span>
<span class="hljs-comment">// 当前界面是否显示大标题，never表示不显示大标题即显示小标题        </span>
navigationItem.largeTitleDisplayMode <span class="hljs-operator">=</span> .never
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-30">右侧按钮</h5>
<ul>
<li>如果当前 UIViewController 设置了<code>rightBarButtonItem</code>属性，则显示右侧按钮，否则显示空白。</li>
</ul>
<h5 data-id="heading-31">左侧按钮</h5>
<ul>
<li>如果当前 UIViewController 设置了<code>leftBarButtonItem</code>属性，则显示左侧按钮。</li>
<li>如果前一个 UIViewController 设置了<code>backButtonItem</code>属性，则显示返回按钮。</li>
<li>如果前一个 UIViewController 设置了<code>title</code>属性，则显示标题文字封装的返回按钮。</li>
<li>如果以上都未设置，则展示文字<code>Back</code>封装的返回按钮。</li>
</ul>
<blockquote>
<p><strong>注意：默认情况下返回按钮和左侧按钮是不同时显示的，只显示返回按钮而不显示左侧按钮。</strong></p>
</blockquote>
<h5 data-id="heading-32">返回按钮</h5>
<ul>
<li>如果当前 UIViewController 设置了<code>leftBarButtonItem</code>属性，则默认的返回按钮会被替代，自带的返回和从屏幕边缘滑动返回的效果失效，此时只能通过<code>popViewController</code>返回。</li>
<li>如果前一个 UIViewController 设置了<code>backButtonItem</code>属性或设置了<code>backButtonTitle</code>，可以起到更改返回按钮文字和图片的目的，但是返回按钮的<code><</code>图标会一直存在，这种方式自带的返回和从屏幕边缘滑动返回的效果依然有效。</li>
</ul>
<h5 data-id="heading-33">颜色问题</h5>
<ul>
<li>UINavigationBar 的颜色：可以通过 UINavigationBar 的<code>barTintColor</code>设置。</li>
<li>UINavigationBar 上面内容的渲染颜色：默认情况下，按钮或系统图片按钮都会渲染成蓝色，可以通过 UINavigationBar 的<code>tintColor</code>设置。</li>
</ul>
<h4 data-id="heading-34">案例</h4>
<ul>
<li>storyboard 使用。</li>
<li>纯代码使用。</li>
<li>自定义使用。</li>
</ul>
<h3 data-id="heading-35">UITabBarController</h3>
<ul>
<li>标签栏控制器。</li>
<li>可以展示多个 UIViewController，这些 UIViewController 是平级关系。但展示的 UIViewController 最多不超过5个，否则会折叠。</li>
<li>它的 View 由两部分组成，上面是 UIViewController 的<code>view</code>，下面是<code>UITabBar</code>。</li>
<li>通过<code>addChildViewController</code>添加 UIViewController，通过UIViewController 的<code>UITabBarItem</code>属性设置展示的文字、默认图片、选中图片和角标。</li>
<li>默认已经实现了<code>UITabBarDelegate</code>。</li>
</ul>
<h4 data-id="heading-36">UITabBarControllerDelegate</h4>
<ul>
<li>UITabBarController 还提供一个代理属性，通过它可以设置一个代理 UITabBarControllerDelegate。</li>
<li>监听切换 UIViewController
<ul>
<li>通过 UITabBarDelegate 的<code>tabBar(_ tabBar: UITabBar, didSelect item: UITabBarItem)</code>方法。</li>
<li>通过 UITabBarControllerDelegate 的<code>tabBarController(_ tabBarController: UITabBarController, didSelect viewController: UIViewController)</code>方法。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-37">颜色问题</h4>
<h5 data-id="heading-38">UITabBar的颜色</h5>
<p>可以通过 UITabBar 的<code>barTintColor</code>设置。</p>
<h5 data-id="heading-39">渲染颜色</h5>
<ul>
<li>图片一般由设计师统一设计，需要设置标题文字颜色以适应图片。</li>
<li>方式一：每个 UIViewController 单独设置。</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 默认文字颜色</span>
vc.tabBarItem.setTitleTextAttributes([<span class="hljs-type">NSAttributedString</span>.<span class="hljs-type">Key</span>.foregroundColor : <span class="hljs-type">UIColor</span>.white], for: .normal)
<span class="hljs-comment">// 选中文字颜色</span>
vc.tabBarItem.setTitleTextAttributes([<span class="hljs-type">NSAttributedString</span>.<span class="hljs-type">Key</span>.foregroundColor : <span class="hljs-type">UIColor</span>.orange], for: .highlighted)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>方式二：Appearance统一设置。</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> item <span class="hljs-operator">=</span> <span class="hljs-type">UITabBarItem</span>.appearance()
<span class="hljs-comment">// 默认文字颜色</span>
item.setTitleTextAttributes([<span class="hljs-type">NSAttributedString</span>.<span class="hljs-type">Key</span>.foregroundColor : <span class="hljs-type">UIColor</span>.white], for: .normal)
<span class="hljs-comment">// 选中文字颜色</span>
item.setTitleTextAttributes([<span class="hljs-type">NSAttributedString</span>.<span class="hljs-type">Key</span>.foregroundColor : <span class="hljs-type">UIColor</span>.orange], for: .highlighted)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>方式三：iOS 10 之后可以统一设置选中和未选中颜色。（<strong>推荐使用</strong>）</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 选中的图片文字颜色</span>
vc.tabBarController<span class="hljs-operator">?</span>.tabBar.tintColor <span class="hljs-operator">=</span> <span class="hljs-type">UIColor</span>.orange
<span class="hljs-comment">// 未选中的文字颜色</span>
vc.tabBarController<span class="hljs-operator">?</span>.tabBar.unselectedItemTintColor <span class="hljs-operator">=</span> <span class="hljs-type">UIColor</span>.white

<span class="hljs-comment">// 角标的背景色</span>
vc.tabBarItem.badgeColor <span class="hljs-operator">=</span> <span class="hljs-type">UIColor</span>.orange
<span class="hljs-comment">// 角标的颜色</span>
vc.tabBarItem.badgeTextAttributes(for: .normal) <span class="hljs-operator">=</span> <span class="hljs-type">UIColor</span>.white
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-40">案例</h4>
<ul>
<li>storyboard 使用。</li>
<li>纯代码使用。</li>
<li>自定义使用。</li>
</ul>
<h3 data-id="heading-41">其他</h3>
<ul>
<li>UITableViewController：表视图控制器，集成了 UITableView 的视图控制器。</li>
<li>UICollectionViewController：集合视图控制器，集成了 UICollectionView 的视图控制器。</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            