
---
title: 'iOS开发的几个知识点'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=9570'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 00:28:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=9570'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第10天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h1 data-id="heading-0">如何分析dSYM？</h1>
<h2 data-id="heading-1">dSYM是什么？</h2>
<p><code>Xcode</code>编译项目之后，我们会看到一个同名的<code>dSYM</code>文件，<code>dSYM</code>是保存<code>十六进制函数地址映射信息</code>的中转文件，我们调试的<code>symbols</code>都会包含在这个文件中，并且每次编译项目的时候都会生成一个新的<code>dSYM</code>文件，位于<code>/User/<用户名>/Library/Developer/Xcode/Archives</code>目录下，对于每一个发布版本我们都很有必要保存对应的<code>Archives</code>文件；</p>
<h2 data-id="heading-2">dSYM文件有什么用？</h2>
<p>当我们软件<code>release</code>模式打包或上线后，不会像我们在<code>Xcode</code>中那样直观的看到用崩溃的错误，这个时候我们就需要分析<code>crash report</code>文件了，iOS设备中会有日志文件保存我们每个应用出错的函数内存地址，通过<code>Xcode</code>的<code>Organizer</code>可以将iOS设备中的<code>DeviceLog</code>导出成<code>crash</code>文件，这个时候我们就可以通过<code>出错的函数地址</code>去查询<code>dSYM</code>文件中程序对应的函数名和文件名。大前提是我们需要有软件版本对应的<code>dSYM</code>文件，这也是为什么我们很有必要保存每个发布版本的<code>Archives</code>文件了。</p>
<h2 data-id="heading-3">如何将文件一一对应?</h2>
<p>每一个<code>xx.app</code>和<code>xx.app.dSYM</code>文件都有对应的<code>UUID</code>, <code>crash</code>文件也有自己的<code>UUID</code>，只要这三个文件的<code>UUID</code>-致，我们就可以通过他们解析出正确的错误函数信息了。</p>
<ul>
<li>1.查看<code>xx.app</code>文件的<code>UUID</code>, terminal 中输入命令: <code>dwarfdump --uuid xx.app/xx</code> (xx代表你的项目名)</li>
<li>2.查看<code>xx.app.dSYM</code>文件的<code>UUID</code>，在terminal中输入命令: <code>dwarfdump --uuid xx.app.dSYM</code></li>
<li>3.<code>crash</code>文件内第一行<code>Incident Identifier</code>就是该<code>crash</code>文件的<code>UUID</code>。</li>
</ul>
<h1 data-id="heading-4">关于多线程</h1>
<h2 data-id="heading-5">多线程分类</h2>
<ul>
<li>pthread
<ul>
<li>一套通用的多线程API</li>
<li>适用于Unix\Linux\Windows等系统</li>
<li>跨平台，可移植</li>
<li>使用难度大</li>
<li>使用语言：C语言</li>
<li>使用频率：几乎不使用</li>
<li>线程生命周期：开发者进行管理</li>
</ul>
</li>
<li>NSThread
<ul>
<li>面向对象</li>
<li>简单易用，可直接操作线程</li>
<li>使用语言：OC语言</li>
<li>使用频率：偶尔使用</li>
<li>线程生命周期：开发者进行管理</li>
</ul>
</li>
<li>GCD
<ul>
<li>替换NSThread的技术</li>
<li>充分利用了设备的多核(自动)</li>
<li>使用语言：C语言</li>
<li>使用频率：经常使用</li>
<li>线程生命周期：自动管理</li>
</ul>
</li>
<li>NSOperation
<ul>
<li>基于GCD</li>
<li>比GCD多了一些更简单实用的功能</li>
<li>使用更加面向对象</li>
<li>使用语言：OC语言</li>
<li>使用频率：经常使用</li>
<li>线程生命周期：自动管理</li>
</ul>
</li>
</ul>
<h2 data-id="heading-6">多线程的原理</h2>
<p>同一时间，<code>CPU</code>只能处理<code>1</code>条线程，只有<code>1</code>条线程在工作(执行)多线程并发(同时)执行，其实是<code>CPU</code>快速地在多条线程之间<code>调度</code>(切换)如果CPU调度线程的时间足够快，就造成了多线程<code>并发</code>执行的
假象思考:如果线程非常非常多，会发生什么情况?<code>CPU</code>会在<code>N</code>多线程之间调度，<code>CPU</code>会累死，消耗大量的<code>CPU</code>资源每条线程被调度执行的频次会降低(线程的执行效率降低)</p>
<h2 data-id="heading-7">多线程的优点</h2>
<p>能适当提高程序的执行效率能适当提高资源利用率(CPU、内存利用率)</p>
<h2 data-id="heading-8">多线程的缺点</h2>
<p>线程需要占用一定的内存空间(默认情况下，主线程占用1M，子线程占用512KB)，如果开启大量的线程，会占用大量的内存空间，降低程序的性能线程越多，CPU在调度线程上的开销就越大程序设计更加复杂：比如线程之间的通信、多线程的数据共享；</p>
<h2 data-id="heading-9">GCD与NSOperation的比较</h2>
<ul>
<li>1、<code>GCD</code>是底层的C语言构成的API,而<code>NSOperationQueue</code>及相关对象是<code>Objc</code>的对象。在<code>GCD</code>中，在队列中执行的是由<code>block</code>构成的任务，这是一个轻量级的数据结构;而<code>Operation</code>作为一个对象，为我们提供了更多的选择;</li>
<li>2、在<code>NSOperationQueue</code>中，我们可以随时取消已经设定要准备执行的任务(当然，已经开始的任务就无法阻止了)，而<code>GCD</code>没法停止已经加入<code>queue</code>的<code>block</code>(其实是有的，但需要许多复杂的代码);</li>
<li>3、<code>NSOperatio</code>n能够方便地设置依赖关系，我们可以让一个<code>Operation</code>依赖于另一个<code>Operation</code>,这样的话尽管两个<code>Operation</code>处于同-个并行队列中，但前者会直到后者执行完毕后再执行;</li>
<li>4、我们能将<code>KVO</code>应用在<code>NSOperation</code>中，可以监听一个<code>Operation</code>是否完成或取消，这样子能比<code>GCD</code>更加有效地掌控我们执行的后台任务;</li>
<li>5、在<code>NSOperation</code>中，我们能够设置<code>NSOperation</code>的<code>priority</code>优先级，能够使同一个并行队列中的任务区分先后地执行，而在<code>GCD</code>中，我们只能区分不同任务队列的优先级，如果要区分<code>block</code>任务的优先级,也需要大量的复杂代码;</li>
<li>6、我们能够对<code>NSOperation</code>进行继承，在这之，上添加成员变量与成员方法，提高整个代码的复用度，这比简单地将<code>block</code>任务排入执行队列更有自由度，能够在其之.上添加更多自定制的功能。总的来说，<code>Operation queue</code>提供了更多你在编写多线程程序时需要的功能，并隐藏了许多线程调度,线程取消与线程优先级的复杂代码，为我们提供简单的API入口。从编程原则来说，-般我们需要尽可能的使用高等级、封装完美的API,在必须时才使用底层API。但是我认为当我们的需求能够以更简单的底层代码完成的时候，简洁的<code>GCD</code>或许是个更好的选择，<code>而Operation queue</code>为我们提供能更多的选择。</li>
<li>7、<code>NSOperation</code>拥有更多的函数可用，具体查看api。<code>NSOperationQueue</code>是在<code>GCD</code>基础.上实现的，只不过是<code>GCD</code>更高一层的抽象</li>
<li>8、在<code>NSOperationQueue</code>中，可以建立各个<code>NSOperation</code>之间的依赖关系。</li>
<li>9、<code>NSOperationQueue</code>支持<code>KVO</code>。可以监测<code>operation</code>是否正在执行(<code>isExecuted</code>)、是否结束(<code>isFinished</code>) ， 是否取消(<code>isCanceld</code>)</li>
<li>10、<code>GCD</code>只支持<code>FIFO</code>的队列，而<code>NSOperationQueue</code>可以调整队列的执行顺序(通过调整<code>权重</code>)。<code>NSOperationQueue</code>可以方便的管理并发、<code>NSOperation</code>之间的优先级。</li>
<li>总结
<ul>
<li>使用<code>NSOperation</code>的情况:各个操作之间有依赖关系、操作需要取消暂停、并发管理、控制操作之间优先级，限制同时能执行的线程数量.让线程在某时刻停止/继续等。</li>
<li>使用<code>GCD</code>的情况:一般的需求很简单的多线程操作，用<code>GCD</code>都可以了，简单高效。从编程原则来说，一般我们需要尽可能的使用高等级、封装完美的API，在必须时才使用底层API。当需求简单，简洁的<code>GCD</code>或许是个更好的选择，而<code>Operation queue</code>为我们提供能更多的选择。</li>
</ul>
</li>
</ul>
<h1 data-id="heading-10">单例的弊端</h1>
<ul>
<li>优点：
<ul>
<li>一个类只被实例化一次，提供了对唯一实例的受控访问</li>
<li>节省系统资源</li>
<li>允许可变数目的实例</li>
</ul>
</li>
<li>缺点：
<ul>
<li>一个类只有一个对象，可能造成责任过重，在一定程度上违背了<code>单一职责原则</code></li>
<li>由于单例模式中没有抽象层，因此单例类的扩展有很大困难</li>
<li>滥用单例将带来一些负面问题，如：为了节省资源将数据库连接池对象设计为单例类，可能会导致共享连接池对象的程序过多而出现连接池溢出；如果实例化的对象长时间不被利用，系统会认为是垃圾而被回收，这将导致对象状态的丢失</li>
</ul>
</li>
</ul>
<h1 data-id="heading-11">介绍下App启动的完成过程</h1>
<h2 data-id="heading-12">App启动过程</h2>
<ul>
<li>解析<code>Info.plist</code></li>
<li>加载相关信息，例如闪屏</li>
<li>沙盒建立、权限检查</li>
<li><code>Mach-O</code>加载</li>
<li>如果是二进制文件，寻找合适当前CPU类别的部分</li>
<li>加载所有依赖的<code>Mach-O</code>文件(递归调用<code>Mach-o</code>加载方法)</li>
<li>定位内部、外部指针引用，例如字符串，函数等</li>
<li>执行声明为<code>attribute(constructor)</code>的C函数</li>
<li>加载类的扩展中的方法</li>
<li><code>C++</code>静态对象加载，调用<code>Objc</code>的<code>+load</code>函数</li>
</ul>
<h2 data-id="heading-13">程序执行</h2>
<ul>
<li><code>main</code>函数</li>
<li>执行<code>UlApplicationMain</code>函数</li>
<li>创建<code>UIApplication</code>对象</li>
<li>创建<code>UIApplicationDelegate</code>对象并复制</li>
<li>读取配置文件<code>info.plist</code>,设置程序启动的一些属性</li>
<li>创建应用程序的<code>Main Runloop</code>循环</li>
<li><code>UlApplicationDelegate</code>对象开始处理监听事件</li>
<li>程序启动之后，首先调用<code>application.didFinishLaunchingWithOptions:</code>方法</li>
<li>如<code>果info.plist</code>中配置了启动的<code>storyBoard</code>的文件名，则加载<code>storyboard</code>文件</li>
<li>如果没有配置，则根据代码创建<code>UIWindow</code> -><code>rootViewController</code>->显示</li>
</ul>
<h1 data-id="heading-14">引起App启动过慢的因素</h1>
<ul>
<li>影响启动性能的因素<code>App</code>启动过程中每个步骤都会影响启动性能,但是有些部分所消耗的时间少之又少，另外有些部分根本无法避免，考虑到投入产出比，我们只列出我们可以优化的部分: <code>main</code>(函数之前耗时的影响因素</li>
<li>动态库加载越多，启动越慢。</li>
<li><code>ObjC</code>类越多，启动越慢</li>
<li><code>C</code>的<code>constructor</code>函数越多，启动越慢</li>
<li><code>C++</code>静态对象越多，启动越慢</li>
<li><code>ObjC</code>的<code>+load</code>越多，启动越慢实验证明，在<code>ObjC</code>类的数目 一样多的情况下，需要加载的动态库越多，<code>App</code>启动就越慢。同样的，在动态库一样多的情况下，<code>ObjC</code>的类越多，<code>App</code>的启动也越慢。需要加载的动态库从<code>1</code>个上升到<code>10</code>个的时候，用户几乎感知不到任何分别，但从<code>10</code>个， 上升到<code>100</code>个的时候就会变得十分明显。同理，<code>100</code>个类和<code>1000</code>个类， 可能也很难查察觉得出，但<code>1000</code>个类和<code>10000</code>个类的分别就开始明显起来。同样的，尽量不要写<code>atribute((constrcror))</code>的<code>C函数</code>，也尽量不要用到<code>C++</code>的静态对象;至于<code>ObjC</code>的<code>+load</code>方法，似乎大家已经习惯不用它了。任何情况下，能用<code>dispatch_ _once()</code>来完成的，就尽量不要用到以上的方法。<code>main()</code>函数之后耗时的影响因素</li>
<li>执行<code>main()</code>函数的耗时</li>
<li>执行<code>applicationWillFinishLaunching</code>的耗时</li>
<li>rootViewController及其<code>childViewController</code>的加载、<code>view</code>及其<code>subviews</code>的加载<code>applicationWillFinishLaunching</code>的耗时</li>
</ul>
<h1 data-id="heading-15">0x8badf00d表示什么？</h1>
<ul>
<li><code>0x8badf00d</code>:该编码表示应用是因为发生<code>watchdog</code>超时而被<code>iOS</code>终止的。通常是应用花费太多时间而无法启动、终止或响应用系统事件。</li>
<li><code>0xbad22222</code>:该编码表示<code>VolP</code>应用因为过于频繁重启而被终止</li>
<li><code>Oxdead10cc</code>: 该代码表明应用因为在后台运行时占用系统资源，如通讯录数据库不释放而被终止。</li>
<li><code>Oxdeadfa11</code>:该代码表示应用是被用户强制退出的。根据苹果文档,强制退出发生在用户长按开关按钮直到出现“滑动来关机”，然后长按Home按钮。强制退出将产生包含0xdeadfa11异常编码的崩溃日志,因为大多数是强制退出是因为应用阻塞了界面。</li>
</ul>
<h1 data-id="heading-16">防止反编译</h1>
<ul>
<li>本地数据加密: iOS应用防反编译加密技术之一:对<code>NSUserDefaults</code>,<code>sqlite</code>存储文件数据加密，保护帐号和关键信息</li>
<li>URL编码加密: <code>iOS</code>应用防反编译加密技术之二:对程序中出现的<code>URL</code>进行编码加密，防此<code>URL</code>被静态分析</li>
<li>网络传输数据加密: <code>iOS</code>应用防反编译加密技术之三:对客户端传输数据提供加密方案，有效防止通过网络接口的拦截获取数据</li>
<li>方法体，方法名高级混淆: <code>iOS</code>应用防反编译加密技术之四:对应用程序的<code>方法名</code>和<code>方法</code>体进行混淆，保证源码被逆向后无法解析代码</li>
<li>程序结构混排加密: <code>iOS</code>应用防反编译加密技术之五:对应用程序逻辑结构进行打乱混排，保证源码可读性降到最低</li>
<li>借助第三方APP加固</li>
</ul>
<h1 data-id="heading-17">需要了解的第三方原理或者底层知识</h1>
<p><code>Runtime</code>、<code>Runloop</code>、<code>block</code>、<code>SDWebImage</code>、<code>AFN</code>、<code>YYCache</code>、<code>GCD</code>等等底层实现</p></div>  
</div>
            