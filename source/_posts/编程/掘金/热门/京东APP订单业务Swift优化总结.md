
---
title: '京东APP订单业务Swift优化总结'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=8121'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 22:19:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=8121'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原创：京东零售技术平台</p>
<p>技术分类：优化、APP、分析</p>
<p>收录于：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" target="_blank">Github</a></p>
<blockquote>
<p>随着Swift ABI稳定，开发者对Swift的关注也持续升温，一些开源框架甚至已经不再提供ObjC版本了，部分苹果新出的系统库也是Swift Only。</p>
</blockquote>
<p>在这样的背景下，京东商城订单业务在不同场景下尝试更多的使用Swift开发，比如:</p>
<ul>
<li>
<p>京东App部分订单业务页面</p>
</li>
<li>
<p>京东App物流小组件</p>
</li>
<li>
<p>“京东工作站”，为公司内部提供的集成部分工作环境与开发环境，以及部分工作流的macOS应用</p>
</li>
</ul>
<blockquote>
<p>在改造过程中，Swift的高效安全与便捷和一些优秀特性给团队留下了深刻的印象。有很多特性是开发者在写ObjC时不会太多考虑的。比如，Swift的静态派发方式、值类型的使用、静态多态、Errors+Throws、柯里化与函数合成以及丰富高阶函数等等，而且相对于OOP，Swift也能更好的支持面向协议编程、泛型编程以及更抽象函数式编程，解决了很多ObjC时代开发者面临的痛点问题。</p>
</blockquote>
<p>结合Swift和ObjC的异同点，我们从Swift优势出发，重新审视和优化了项目的功能代码，优化点包括但不限于如下几个方面。</p>
<p><strong>将部分方法动态派发替换为静态派发</strong></p>
<blockquote>
<p>Swift运行速度比ObjC快的原因之一就是其派发方式：静态派发(值类型)和函数表派发(引用类型)。使用静态派发ARM架构可直接用bl指令跳转到对应函数地址，调用效率最高并且有利于编译器的内联优化。值类型无法继承父类，编译时期能确定类型，满足静态派发的条件。对于引用类型，不同编译器的设置也会对派发方式有影响。比如WMO全模块编译下，系统会自动填用隐式final等关键字来修饰没有被子类继承的类，从而尽可能多的使用静态派发。</p>
</blockquote>
<p>在我们的项目中，针对所有使用Class的类做了整体检查。除非必要应完全避免继承NSObject，少用NSObject的子类。对于不需要考虑继承或者多态的场景，尽可能的使用final 或者 private等关键字修饰。</p>
<p>另外需要关注的是，ObjC也引入了方法的静态派发。在Xcode12中集成的最新LLVM已经支持 ObjC 通过对方法指定__attribute__((objc_direct)) 的方式，来将原本的动态消息派发改为静态派发。</p>
<p><strong>检查所有Class 尽可能替换为结构体或者枚举</strong></p>
<p>Swift中的结构体和枚举是值类型，Class是引用类型。在Swift中使用值类型还是引用类型是开发者需要思考和评估的。</p>
<p>在我们开发的京东物流小组件和基于SwiftUI开发的macOS应用中，我们目前更多的使用了结构体和枚举。先对比下值类型与引用类型的区别，值类型(Struct Enum等等):</p>
<ul>
<li>
<p>在栈上创建，创建速度快</p>
</li>
<li>
<p>内存占用小。整体占用的内存就是内部属性内存对齐后的大小</p>
</li>
<li>
<p>内存回收快，用栈帧控制入栈出栈即可，没有处理堆内存的开销</p>
</li>
<li>
<p>不需要引用计数 (结构体中使用引用类型作为属性除外)</p>
</li>
<li>
<p>一般是静态派发，运行速度快，也方便编译器优化，如内联等</p>
</li>
<li>
<p>赋值时深拷贝。系统通过Copy-On-Write，避免不必要的copy，减少拷贝开销</p>
</li>
<li>
<p>没有隐式数据共享，具有独立性不可变性</p>
</li>
<li>
<p>可通过mutating去修改结构体中的属性。这样在保证值类型的独立性的同时，也能支持对部分属性的修改。</p>
</li>
<li>
<p>线程安全，一般来说没有竞态条件和死锁(要注意确定值在各个子线程中是被copy过的)</p>
</li>
<li>
<p>不支持继承，避免OOP子类过于耦合父类的问题。</p>
</li>
<li>
<p>可通过协议和泛型实现抽象。但实现协议的结构体内存大小不同，因此无法直接放入数组中，为了存储的一致性，传参赋值时系统会引入中间层Existential Container。此处如果结构体属性较多会复杂一点，但苹果也会有优化(Indirect Storage With Copy-On-Write)，较少开销。总体来说，值类型的多态是有成本的，系统会尽量优化。开发者要考虑的是：减少动态多态把协议直接当做类来使用，需要更多考虑静态多态，多结合泛型约束来使用。</p>
</li>
</ul>
<p>引用类型(Class Function Closure等等):</p>
<ul>
<li>
<p>引用类型在内存使用上没有值类型高效，在堆上创建并需要有栈指针指向该区域，增加了堆内存分配和回收的开销</p>
</li>
<li>
<p>赋值消耗小，一般是浅拷贝复制指针。但有引用计数成本</p>
</li>
<li>
<p>多个指针可指向同一内存，独立性差，容易误操作</p>
</li>
<li>
<p>非线程安全，要考虑原子性，多线程需要线程锁配合</p>
</li>
<li>
<p>需要引用计数来控制内存释放，使用不当会有野指针、内存泄漏和循环引用的风险</p>
</li>
<li>
<p>允许继承，但继承的Side effect就是子类与父类的紧耦合。比如系统的 UIStackView主要目的只是用来布局使用，但却不得不继承UIView的所有属性和方法。</p>
</li>
</ul>
<p>由此可见，Swift提供了更强大的值类型试图来解决ObjC时代OOP的子类与父类的紧耦合、对象隐式数据共享、非线程安全、引用计数等典型痛点。翻看Swift 标准库会发现其主要由值类型组成，基本类型集合如 Int，Double，Float，String，Array，Dictionary，Set，Tuple也都是结构体。当然，虽然值类型有众多优点，但也不是说要完全抛弃Class，还是要根据实际情况分析，实际的Swift开发中更多的是一个种结合的方式，完全不使用OOP也是不现实的。</p>
<p><strong>优化结构体内存</strong></p>
<p>和使用C语言结构体一样，Swift结构体的大小就是内部属性内存对齐后的大小。结构体中属性放置在不同的顺序会影响最后的内存大小。可使用系统提供的 MemoryLayout查看相应结构体占用内存大小。</p>
<p>我们从一些细节层面做了review，比如对于Int32完全满足的场景没有必要使用Int，不要使用String或者Int代替应该使用Bool的场景，内存小的属性尽量放在后面等等。</p>
<pre><code class="copyable">struct GameBoard &#123;  var p1Score: Int32  var p2Score: Int32  var gameOver: Bool &#125;struct GameBoard2 &#123;  var p1Score: Int32  var gameOver: Bool   var p2Score: Int32&#125;//基于CPU寻址效率考虑，GameBoard2字节对齐后占用空间更多MemoryLayout<GameBoard>.self.size  //4 + 4 + 1 = 9(bytes)MemoryLayout<GameBoard2>.self.size //4 + 4 + 4 = 12(bytes)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用静态多态替换动态多态</strong></p>
<p>上面提到值类型的时候，我们有提到静态多态，静态多态是指编译器能在编译时期确定类型的多态。这样编译器可以类型降级，在编译时可产生特定类型的方法。</p>
<p>将泛型定义为遵守某个协议的约束可以避免直接把协议直接当做类来传参使用，否则编译器会报错，相当于接口支持多态，但调用时要用特定的类型调用，从而达到了静态多态的目的。对于静态多态，编译器会充分利用其静态特性做优化，同时在设置了WMO全模块优化(Whole Module Optimization)的情况下会尽量控制由此可能产生的代码增长。</p>
<p>简而言之，开发者要尽可能多考虑静态多态。比如在使用协议作为函数的参数时，可以引入泛型。WWDC中有很经典的讨论:</p>
<pre><code class="copyable">protocol Drawable &#123;    func draw()&#125;struct Line: Drawable &#123;    var x: Double = 0    func draw() &#123;    &#125;&#125;func drawACopy<T: Drawable>(local: T) &#123;//指定T必须遵守Drawable    local.draw()&#125;let line = Line()drawACopy(local: line)//Success (传入具体的实现了Drawable的结构体，编译器可推断其类型)let line2: Drawable = Line()drawACopy(local: line2)//Error，编译器不允许直接使用Drawable协议作为入参
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>面向协议为协议提供扩展默认实现</strong></p>
<p>对于类的继承父类和遵守协议，Swift更愿意选择后者。ObjC中OOP的形式，在Swift里基本都可以使用 Structs/Enums + Protocols + Protocol extensions + Generics 来实现逻辑抽象。</p>
<p>我们尽量减少了项目中使用OOP的场景，尽可能的只用值类型面向协议和利用泛型，这样编译器能做更多的静态优化，更能降低OOP超类带来的紧耦合。</p>
<p>同时，Protocol extension能够为protocol提供一个默认实现，这也是区别于ObjC协议的很重要的优化。</p>
<p>使用时要注意，应该用具体的类型去调用Protocol extension中的方法，而不是用通过类型推断得到的Protocol来调用。使用Protocol调用时，如果该方法没有在Protocol中定义，Protocol extension中的默认实现将被调用，即使具体的类型中有实现对应方法。因为此时编译器此时只能找到默认实现。</p>
<p><strong>优化错误处理</strong></p>
<p>相对于ObjC, Swift 中对 Error 和 Throw 的处理更加完善，这样显而易见的好处是API更友好，提高可读性，利用编辑器检测降低出错概率。ObjC时代大家往往不会考虑抛出异常的操作，这个也是习惯ObjC编码的程序员在封装底层API时需要注意的。常见的是使用继承Error协议的Enum。</p>
<pre><code class="copyable">enum CustomError: Error &#123;   case error1   case error2&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>产生Error后也可以抛出让外部处理，支持throw的方法后编译器会做强检测是否有处理throw。要注意 () throws -> Void 和 () -> Void 是不同的 Function Type。</p>
<pre><code class="copyable">//(Int)->Void可以赋值给(Int)throws->Voidlet a: (Int) throws -> Void = &#123; n in&#125;//反之类型不匹配 编译报错let b: (Int) -> Void = &#123; n throws in&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rethrows:如果一个函数入参是一个支持throw的函数，那么通过rethrows可以标识该函数同样可以抛出Error。这样在使用该函数时，编译器会检测是否需要try-catch。</p>
<p>这是我们在封装基础功能时需要考虑的，系统中友好的示例很多，比如map函数在系统中的定义：</p>
<pre><code class="copyable">public func map<T>(_ transform: (Element) throws -> T) rethrows -> [T]let a = [1, 2, 3]enum CustomError: Error &#123;  case error1  case error2&#125;do &#123;  let _ = try a.map &#123; n -> Int in    guard n >= 0 else &#123;      //如果map接受的closure内部有抛出throw，编译器会强制检测外部是否有try-catch      throw CustomError.error1    &#125;    return n * n  &#125;&#125; catch CustomError.error1 &#123;&#125; catch &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>用Guard减少if嵌套</strong></p>
<p>关键性检测可以使用 Guard，其优势是可以增强可读性，较少过多的if嵌套。使用Guard时，一般else里面会是 return、 throw、continue、 break等。</p>
<pre><code class="copyable">//if嵌套过多，难以阅读，增加后期维护成本if (xxx)&#123;  if (xxx) &#123;    if (xxx) &#123;    &#125;  &#125;&#125;//使用Guard，整体更清晰，便于后期维护let dict : Dictionary = ["key": "0"]guard let value1 = dict["key"], value == "0" else &#123;  return&#125;guard let value2 = dict["key2"], value == "0" else &#123;  return&#125;print("\(value1) \(value2)")
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>利用Defer</strong></p>
<p>被defer修饰的closure会在当前作用域退出的时候调用，主要用来避免重复添加返回前需要执行的代码，提高可读性。</p>
<p>比如在我们macOS应用中有对文件读写的操作，这时候使用defer可以确保不会忘记关闭文件。</p>
<pre><code class="copyable">func write() throws &#123;  //...  guard let file = FileHandle(forUpdatingAtPath: filepath) else &#123;    throw WriteError.notFound  &#125;  defer &#123;    try? file.close()  &#125;  //...&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外比较常用的场景是释放锁的时候，以及非逃逸闭包回调等。</p>
<p>但是defer不要过度使用，使用时要注意closure捕获变量和作用域的问题。</p>
<p>比如如果在if语句中使用defer，则跳出if时，该defer就会被执行。</p>
<p><strong>用可选绑定替换所有的强制拆包</strong></p>
<p>对于可选值，要尽最大可能甚至完全避免强制拆包。大部分情况下如果遇到了需要使用 ! 的情况，很可能说明最初的设计是不合理的。包括downCasting时，由于类型转换本身就有可能失败，要避免使用 as! ，尽量使用as?，当然try!也要避免。</p>
<p>对于可选值，永远要使用<strong>可选绑定</strong>检测，确保可选变量具有真正的值存在，然后再进行操作:</p>
<pre><code class="copyable">var optString: String?if let _ = optString &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>多考虑懒加载</strong></p>
<p>将项目中不需要必须创建的属性，改为懒加载。Swift的懒加载相对于ObjC来说可读性更好，也更容易实现，使用Lazy修饰就好。</p>
<pre><code class="copyable">lazy var aLabel: UILabel = &#123;    let label = UILabel()    return label&#125;()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用函数式编程 减少状态变量声明与维护</strong></p>
<p>在类里面声明过多的状态变量是不利于后期维护的。Swift里函数可以作为函数参数、返回值以及变量，可以很好的支持函数式编程。利用函数式能有效减少全局变量或者状态变量。</p>
<p>命令式编程更关注解决问题的步骤。直接反应机器指令序列。有变量（对应存储单元），赋值语句（对应获取与存储指令），表达式（对应 指令算数计算），控制语句（对应跳转指令）。</p>
<p>函数式编程更关注数据的映射关系和数据的流向，即输入和输出。函数被当做变量，既可以作为其它函数的参数（输入值），也可以从函数中返回（输出值）。将计算描述为表达式求值，自变量的映射f(x)->y，给定x，会稳定映射为y。函数内尽量不访问函数作用域之外的变量，只依赖入参，减少状态变量的声明与维护。同时少用可变变量(对象)，多用不可变变量(结构体)。这样就不会有其他side effects干扰。</p>
<p>利用柯里化把接受多个参数的函数变换成接受一个单一参数的函数，将<strong>部分参数缓存到函数内部</strong>。同时利用函数合成增加可读性。比如做加法乘法计算，我们可以封装加法和乘法函数然后逐一调用:</p>
<pre><code class="copyable">func add(_ a: Int, _ b: Int) -> Int &#123; a + b &#125;func multiple(_ a: Int, _ b: Int) -> Int &#123; a * b &#125;let n = 3multiple(add(n, 7), 6) //(n + 7) * 6 = 60
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以使用函数式：</p>
<pre><code class="copyable">//柯里化add和multiple函数: 由两个入参改为一个并返回一个(Int)->Int类型函数func add(_ a: Int) -> (Int) -> Int &#123; &#123; $0 + a&#125; &#125; func multiple(_ a: Int) -> (Int) -> Int &#123; &#123; $0 * a&#125; &#125; //函数合成 自定义中置运算符 > 增加可读性infix operator > : AdditionPrecedencefunc >(_ f1: @escaping (Int)->Int,       _ f2: @escaping (Int)->Int) -> (Int) -> Int &#123;  &#123;f2(f1($0))&#125; &#125;//生成新的函数 newFnlet n = 3let newFn = add(7) > multiple(6) // (Int)->Intprint( newFn(n) ) //(n + 7) * 6 = 60
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，从使用multiple(add(n, 7), 6) 到 let newFn = add(7) > multiple(6), newFn(n)，整体更清晰了，尤其是在更复杂的场景下，其优势会更明显。</p>
<p><strong>总结</strong></p>
<blockquote>
<p>Swift提供了丰富简便的语法糖以及强大的类型推断，这些都让Swift变得很容易上手入门。但是要从性能考虑或者是设计出更完美API的角度出发，还是需要投入更多的实践才行。订单团队正在iOS小组件、AppClips、京东工作站(macOS桌面应用)等场景下尝试尽可能多的使用Swift与SwiftUI开发，开发效率与项目稳定性都有不错的表现。目前京东集团内部对Swift的基础设施正在逐步完善中，我们相信也希望未来集团内有更多的同学参与到Swift的开发中进来。</p>
</blockquote>
<p>推荐收藏：干货：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" target="_blank">Github</a></p></div>  
</div>
            