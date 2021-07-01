
---
title: 'Swift与Objective-C API的交互！'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61df9c7d5c8b43c7b1abdbf024e710e9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 22 Jun 2021 23:11:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61df9c7d5c8b43c7b1abdbf024e710e9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>互用性是让 Swift 和 Objective-C 相接合的一种特性，使你能够在一种语言编写的文件中使用另一种语言。当你准备开始把 Swift 融入到你的开发流程中时，你应该懂得如何利用互用性来重新定义并提高你写 Cocoa 应用的方案。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61df9c7d5c8b43c7b1abdbf024e710e9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>互用性很重要的一点就是允许你在写 Swift 代码时使用 Objective-C 的 API 接口。当你导入一个 Objective-C 框架后，你可以使用原生的 Swift 语法实例化它的 Class 并且与之交互。</p>
<h2 data-id="heading-0">初始化</h2>
<p>为了使用 Swift 实例化 Objective-C 的 Class，你应该使用 Swift 语法调用它的一个初始化器。当 Objective-C 的init方法变化到 Swift，他们用 Swift 初始化语法呈现。“init”前缀被截断当作一个关键字，用来表明该方法是初始化方法。那些以“initWith”开头的init方法，“With”也会被去除。从“init”或者“initWith”中分离出来的这部分方法名首字母变成小写，并且被当做是第一个参数的参数名。其余的每一部分方法名依次变味参数名。这些方法名都在圆括号中被调用。</p>
<p>举个例子，你在使用 Objective-C 时会这样做：</p>
<pre><code class="copyable">1.  //Objective-C
2.  UITableView *myTableView = [[UITableView alloc]
3.  initWithFrame:CGRectZero style:UITableViewStyleGrouped];
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>作为一个开发者，有一个学习的氛围跟一个交流圈子特别重要，这是一个我的iOS开发公众号：<strong>编程大鑫</strong>，不管你是小白还是大牛都欢迎入驻 ，让我们一起进步，共同发展！（群内会免费提供一些群主收藏的免费学习书籍资料以及整理好的几百道面试题和答案文档！）</p>
</blockquote>
<p>在 Swift 中，你应该这样做：</p>
<pre><code class="copyable">1.  //Swift
2.  let myTableView: UITableView = UITableView(frame: CGRectZero, style: .Grouped) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你不需要调用 alloc，Swift 能替你处理。注意，当使用 Swift 风格的初始化函数的时候，“init”不会出现。
你可以在初始化时显式的声明对象的类型，也可以忽略它，Swift 能够正确判断对象的类型。</p>
<pre><code class="copyable">1.  //Swift
2.  let myTextField = UITextField(frame: CGRect(0.0, 0.0, 200.0, 40.0)) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的UITableView和UITextField对象和你在 Objective-C 中使用的具有相同的功能。你可以用一样的方式使用他们，包括访问属性或者调用各自的类中的方法。
为了统一和简易，Objective-C 的工厂方法也在 Swift 中映射为方便的初始化方法。这种映射能够让他们使用同样简洁明了的初始化方法。例如，在 Objective-C 中你可能会像下面这样调用一个工厂方法：</p>
<pre><code class="copyable">1.  //Objective-C
2.  UIColor *color = [UIColor colorWithRed:0.5 green:0.0 blue:0.5 alpha:1.0]; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Swift 中，你应该这样做：</p>
<pre><code class="copyable">1.  //Swift
2.  let color = UIColor(red: 0.5, green: 0.0, blue: 0.5, alpha: 1.0) 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">访问属性</h2>
<p>在 Swift 中访问和设置 Objective-C 对象的属性时，使用点语法：</p>
<pre><code class="copyable">1.  // Swift
2.  myTextField.textColor = UIColor.darkGrayColor()
3.  myTextField.text = "Hello world"
4.  if myTextField.editing &#123;
5.  myTextField.editing = false
6.  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 get 或 set 属性时，直接使用属性名称，不需要附加圆括号。注意，darkGrayColor后面附加了一对圆括号，这是因为darkGrayColor是UIColor的一个类方法，不是一个属性。</p>
<p>在 Objective-C 中，一个有返回值的无参数方法可以被作为一个隐式的访问函数，并且可以与访问器使用同样的方法调用。但在 Swift 中不再能够这样做了，只有使用@property关键字声明的属性才会被作为属性引入。</p>
<h2 data-id="heading-2">方法</h2>
<p>在 Swift 中调用 Objective-C 方法时，使用点语法。</p>
<p>当 Objective-C 方法转换到 Swift 时，Objective-C 的selector的第一部分将会成为方法名并出现在圆括号的前面，而第一个参数将直接在括号中出现，并且没有参数名，而剩下的参数名与参数则一一对应的填入圆括号中。</p>
<p>举个例子，你在使用 Objective-C 时会这样做：</p>
<pre><code class="copyable">1.  //Objective-C
2.  [myTableView insertSubview:mySubview atIndex:2]; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Swift 中，你应该这样做：</p>
<pre><code class="copyable">1.  //Swift
2.  myTableView.insertSubview(mySubview, atIndex: 2) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你调用一个无参方法，仍必须在方法名后面加上一对圆括号</p>
<pre><code class="copyable">1.  //Swift
2.  myTableView.layoutIfNeeded() 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">id 兼容性（id Compatibility）</h2>
<p>Swift 包含一个叫做AnyObject的协议类型，表示任意类型的对象，就像 Objective-C 中的id一样。AnyObject协议允许你编写类型安全的 Swift 代码同时维持无类型对象的灵活性。因为AnyObject协议保证了这种安全，Swift 将 id 对象导入为 AnyObject。</p>
<p>举个例子，跟 id 一样，你可以为AnyObject类型的对象分配任何其他类型的对象，你也同样可以为它重新分配其他类型的对象。</p>
<pre><code class="copyable">1.  //Swift
2.  var myObject: AnyObject = UITableViewCell()
3.  myObject = NSDate() 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你也可以在调用 Objective-C 方法或者访问属性时不将它转换为具体类的类型。这包括了 Objcive-C 中标记为 @objc 的方法。</p>
<pre><code class="copyable">1.  //Swift
2.  let futureDate = myObject.dateByAddingTimeInterval(10)
3.  let timeSinceNow = myObject.timeIntervalSinceNow 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而，由于直到运行时才知道AnyObject的对象类型，所以有可能在不经意间写出不安全代码。另外，与 Objective-C 不同的是，如果你调用方法或者访问的属性 AnyObject 对象没有声明，将会报运行时错误。比如下面的代码在运行时将会报出一个 unrecognized selector error 错误：</p>
<pre><code class="copyable">1.  //Swift
2.  myObject.characterAtIndex(5)
3.  // crash, myObject does't respond to that method 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，你可以通过 Swift 的 optinals 特性来排除这个 Objective-C 中常见的错误，当你用AnyObject对象调用一个 Objective-C 方法时，这次调用将会变成一次隐式展开 optional（implicitly unwrapped optional）的行为。你可以通过 optional 特性来决定 AnyObject 类型的对象是否调用该方法，同样的，你可以把这种特性应用在属性上。</p>
<p>举个例子，在下面的代码中，第一和第二行代码将不会被执行因为length属性和characterAtIndex:方法不存在于 NSDate 对象中。myLength常量会被推测成可选的Int类型并且被赋值为nil。同样你可以使用if-let声明来有条件的展开这个方法的返回值，从而判断对象是否能执行这个方法。就像第三行做的一样。</p>
<pre><code class="copyable">1.  //Swift
2.  let myLength = myObject.length?
3.  let myChar = myObject.characterAtIndex?(5)
4.  if let fifthCharacter = myObject.characterAtIndex(5) &#123;
5.  println("Found \(fifthCharacter) at index 5")
6.  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 Swift 中的强制类型转换，从 AnyObject 类型的对象转换成明确的类型并不会保证成功，所以它会返回一个可选的值。而你需通过检查该值的类型来确认转换是否成功。</p>
<pre><code class="copyable">1.  //Swift
2.  let userDefaults = NSUserDefaults.standardUserDefaults()
3.  let lastRefreshDate: AnyObject? = userDefaults.objectForKey("LastRefreshDate")
4.  if let date = lastRefreshDate as? NSDate &#123;
5.  println("\(date.timeIntervalSinceReferenceDate)")
6.  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，如果你能确定这个对象的类型（并且确定不是nil），你可以添加as操作符强制调用。</p>
<pre><code class="copyable">1.  //Swift
2.  let myDate = lastRefreshDate as NSDate
3.  let timeInterval = myDate.timeIntervalSinceReferenceDate 

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">使用nil</h2>
<p>在Objective-C中，对象的引用可以是值为NULL的原始指针（同样也是Objective-C中的nil）。而在Swift中，所有的值–包括结构体与对象的引用–都被保证为非空。作为替代，你将这个可以为空的值包装为optional type。当你需要宣告值为空时，你需要使用nil。你可以在Optionals中了解更多。</p>
<p>因为Objective-C不会保证一个对象的值是否非空，Swift在引入Objective-C的API的时候，确保了所有函数的返回类型与参数类型都是optional，在你使用Objective-C的API之前，你应该检查并保证该值非空。 在某些情况下，你可能绝对确认某些Objective-C方法或者属性永远不应该返回一个nil的对象引用。为了让对象在这种情况下更加易用，Swift使用 implicitly unwrapped optionals 方法引入对象， implicitly unwrapped optionals 包含optional 类型的所有安全特性。此外，你可以直接访问对象的值而无需检查nil。当你访问这种类型的变量时， implicitly unwrapped optional 首先检查这个对象的值是否不存在，如果不存在，将会抛出运行时错误。</p>
<h2 data-id="heading-5">扩展（Extensions）</h2>
<p>Swift 的扩展和 Objective-C 的类别（Category）相似。扩展为原有的类，结构和枚举丰富了功能，包括在 Objective-C 中定义过的。你可以为系统的框架或者你自己的类型增加扩展，只需要导入合适的模块并且保证你在 Objective-C 中使用的类、结构或枚举拥有相同的名字。</p>
<p>举个例子，你可以扩展UIBezierPath类来为它增加一个等边三角形，这个方法只需提供三角形的边长与起点。</p>
<pre><code class="copyable">1.  //Swift
2.  extension UIBezierPath &#123;
3.  convenience init(triangleSideLength: Float, origin: CGPoint) &#123;
4.  self.init()
5.  let squareRoot = Float(sqrt(3))
6.  let altitude = (squareRoot * triangleSideLength) / 2
7.  moveToPoint(origin)
8.  addLineToPoint(CGPoint(triangleSideLength, origin.x))
9.  addLineToPoint(CGPoint(triangleSideLength / 2, altitude))
10.  closePath()
11.  &#125;
12.  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你也可以使用扩展来增加属性（包括类的属性与静态属性）。然而，这些属性必须是通过计算才能获取的，扩展不会为类，结构体，枚举存储属性。下面这个例子为CGRect类增加了一个叫area的属性。</p>
<pre><code class="copyable">1.  //Swift
2.  extension CGRect &#123;
3.  var area: CGFloat &#123;
4.  return width * height
5.  &#125;
6.  &#125;
7.  let rect = CGRect(x: 0.0, y: 0.0, width: 10.0, height: 50.0)
8.  let area = rect.area
9.  // area: CGFloat = 500.0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你同样可以使用扩展来为类添加协议而无需增加它的子类。如果这个协议是在 Swift 中被定义的，你可以添加 comformance 到它的结构或枚举中无论它们在 Objective-C 或在 Swift 中被定义。</p>
<p>你不能使用扩展来覆盖 Objective-C 类型中存在的方法与属性。</p>
<h2 data-id="heading-6">闭包（Closures）</h2>
<p>Objective-C 中的blocks会被自动导入为 Swift 中的闭包。例如，下面是一个 Objective-C 中的 block 变量：</p>
<pre><code class="copyable">1.  //Objective-C
2.  void (^completionBlock)(NSData *, NSError *) = ^(NSData *data, NSError *error) &#123;/* ... */&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而它在 Swift 中的形式为</p>
<pre><code class="copyable">1.  //Swift
2.  let completionBlock: (NSData, NSError) -> Void = &#123;data, error in /* ... */&#125; 

<span class="copy-code-btn">复制代码</span></code></pre>
<p>Swift 的闭包与 Objective-C 中的 blocks 能够和睦相处，所以你可以把一个 Swift 闭包传递给一个把 block 作为参数的 Objective-C 函数。Swift 闭包与函数具有互通的类型，所以你甚至可以传递 Swift 函数的名字。
闭包与 blocks 语义上想通但是在一个地方不同：变量是可以直接改变的，而不是像 block 那样会拷贝变量。换句话说，Swift 中变量的默认行为与 Objective-C 中 __block 变量一致。</p>
<h2 data-id="heading-7">比较对象</h2>
<p>当比较两个 Swift 中的对象时，可以使用两种方式。第一种，使用（==），判断两个对象内容是否相同。第二种，使用(===)，判断常量或者变量是否为同一个对象的实例。</p>
<p>Swift 与 Objective-C 一般使用 == 与 === 操作符来做比较。Swift 的 == 操作符为源自 NSObject 的对象提供了默认的实现。在实现 == 操作符时，Swift 调用 NSObject 定义的 isEqual: 方法。</p>
<p>NSObject 类仅仅做了身份的比较，所以你需要在你自己的类中重新实现 isEqual: 方法。因为你可以直接传递 Swift 对象给 Objective-C 的 API，你也应该为这些对象实现自定义的 isEqual: 方法，如果你希望比较两个对象的内容是否相同而不是仅仅比较他们是不是由相同的对象派生。</p>
<p>作为实现比较函数的一部分，确保根据Object comparison实现对象的hash属性。更进一步的说，如果你希望你的类能够作为字典中的键，也需要遵从Hashable协议以及实现hashValues属性。</p>
<h2 data-id="heading-8">Swift 类型兼容性</h2>
<p>当你定义了一个继承自NSObject或者其他 Objective-C 类的 Swift 类，这些类都能与 Objective-C 无缝连接。所有的步骤都有 Swift 编译器自动完成，如果你从未在 Objective-C 代码中导入 Swift 类，你也不需要担心类型适配问题。另外一种情况，如果你的 Swift 类并不来源自 Objectve-C 类而且你希望能在 Objecive-C 的代码中使用它，你可以使用下面描述的 @objc 属性。</p>
<p>@objc可以让你的 Swift API 在 Objective-C 中使用。换句话说，你可以通过在任何 Swift 方法、类、属性前添加@objc，来使得他们可以在 Objective-C 代码中使用。如果你的类继承自 Objective-C,编译器会自动帮助你完成这一步。编译器还会在所有的变量、方法、属性前加 @objc，如果这个类自己前面加上了@objc关键字。当你使用@IBOutlet，@IBAction，或者是@NSManaged属性时，@objc也会自动加在前面。这个关键字也可以用在 Objetive-C 中的 target-action 设计模式中，例如，NSTimer或者UIButton。</p>
<p>当你在 Objective-C 中使用 Swift API，编译器基本对语句做直接的翻译。例如，Swift API func playSong(name: String)会被解释为- (void)playSong:(NSString *)name。然而，有一个例外：当在 Objective-C 中使用 Swift 的初始化函数，编译器会在方法前添加“initWith”并且将原初始化函数的第一个参数首字母大写。例如，这个 Swift 初始化函数init (songName: String, artist: String将被翻译为- (instancetype)initWithSongName:(NSString *)songName artist:(NSString *)artist 。</p>
<p>Swift 同时也提供了一个@objc关键字的变体，通过它你可以自定义在 Objectiv-C 中转换的函数名。例如，如果你的 Swift 类的名字包含 Objecytive-C 中不支持的字符，你就可以为 Objective-C 提供一个可供替代的名字。如果你给 Swift 函数提供一个 Objecytive-C 名字，要记得为带参数的函数添加（:）</p>
<pre><code class="copyable">1.  //Swift
2.  @objc(Squirrel)
3.  class Белка &#123;
4.  @objc(initWithName:)
5.  init (имя: String) &#123; /*...*/ &#125;
6.  @objc(hideNuts:inTree:)
7.  func прячьОрехи(Int, вДереве: Дерево) &#123; /*...*/ &#125;
8.  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当你在 Swift 类中使用@objc(<#name#>)关键字，这个类可以不需要命名空间即可在 Objective-C 中使用。这个关键字在你迁徙 Objecive-C 代码到 Swift 时同样也非常有用。由于归档过的对象存贮了类的名字，你应该使用@objc(<#name#>)来声明与旧的归档过的类相同的名字，这样旧的类才能被新的 Swift 类解档。</p>
<h2 data-id="heading-9">Objective-C 选择器（Selectors）</h2>
<p>一个 Objective-C 选择器类型指向一个 Objective-C 的方法名。在 Swift 时代，Objective-C 的选择器被Selector结构体替代。你可以通过字符串创建一个选择器，比如let mySelector: Selector = "tappedButton:"。因为字符串能够自动转换为选择器，所以你可以把字符串直接传递给接受选择器的方法。</p>
<pre><code class="copyable">1.  //Swift
2.  import UIKit
3.  class MyViewController: UIViewController &#123;
4.  let myButton = UIButton(frame: CGRect(x: 0, y: 0, width: 100, height: 50))

6.  init(nibName nibNameOrNil: String!, bundle nibBundleOrNil: NSBundle!) &#123;
7.  super.init(nibName: nibName, bundle: nibBundle)
8.  myButton.targetForAction("tappedButton:", withSender: self)
9.  &#125;

11.  func tappedButton(sender: UIButton!) &#123;
12.  println("tapped button")
13.  &#125;
14.  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意： performSelector:方法和相关的调用选择器的方法没有导入到 Swift 中因为它们是不安全的。</p>
</blockquote>
<blockquote>
<p>作为一个开发者，有一个学习的氛围跟一个交流圈子特别重要，这是一个我的iOS开发公众号：<strong>编程大鑫</strong>，不管你是小白还是大牛都欢迎入驻 ，让我们一起进步，共同发展！（群内会免费提供一些群主收藏的免费学习书籍资料以及整理好的几百道面试题和答案文档！）</p>
</blockquote>
<p>如果你的 Swift 类继承自 Objective-C 的类，你的所有方法都可以用作 Objective-C 的选择器。另外，如果你的 Swift 类不是继承自 Objective-C，如果你想要当选择器来使用你就需要在前面添加@objc关键字，详情请看Swift 类型兼容性。</p></div>  
</div>
            