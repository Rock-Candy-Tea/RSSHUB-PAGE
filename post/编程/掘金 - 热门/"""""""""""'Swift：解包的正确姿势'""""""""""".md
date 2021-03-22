
---
title: """""""""""'Swift：解包的正确姿势'"""""""""""
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Fri, 19 Feb 2021 17:39:16 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><h2 data-id="heading-0">嗯，先来一段感慨</h2>
<p>在掘金里面看见iOS各路大神各种底层与runtime，看得就算工作了好几年的我也一脸蒙圈，于是只好从简单的入手。</p>
<p>文章最初发布在简书上面，有段时间了，考虑以后大部分时间都会在掘金学习，于是把文章搬过来了。稍微做了点润色与排版。</p>
<p><em><strong>对于Swift学习而言，可选类型Optional是永远绕不过的坎，特别是从OC刚刚转Swift的时候，可能就会被代码行间的?与!，有的时候甚至是??搞得稀里糊涂的。</strong></em></p>
<p>这篇文章会给各位带来我对于可选类型的一些认识以及如何进行解包，其中会涉及到Swift中<em><strong>if let</strong></em>以及<em><strong>guard let</strong></em>的使用以及思考，还有涉及OC部分的<em><strong>nullable</strong></em>和<em><strong>nonnull</strong></em>两个关键字，以及一点点对两种语言的思考。</p>
<h2 data-id="heading-1">var num: Int? 它是什么类型?</h2>
<p>在进行解包前，我们先来理解一个概念，这样可能更有利于对于解包。</p>
<p>首先我们来看看这样一段代码:</p>
<pre><code class="copyable">
  var num: Int?

  num = 10

  if num is Optional<Int> &#123;

  print("它是Optional类型")

  &#125;else &#123;

   print("它是Int类型")

  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>请先暂时不要把这段代码复制到Xcode中，先自问自答，num是什么类型，是Int类型吗?</p>
<p>好了，你可以将这段代码复制到Xcode里去了，然后在Xcode中的if上一定会出现这样一段话：</p>
<pre><code class="copyable">
'is' test is always true

<span class="copy-code-btn">复制代码</span></code></pre>
<p>num不是<em><strong>Int类</strong></em>，它是<em><strong>Optional类型</strong></em>。</p>
<p>那么Optional类型是啥呢--可选类型，具体Optional是啥，Optional类型的本质实际上就是一个带有泛型参数的enum类型，各位去源码中仔细看看就能了解到，这个类型和Swift中的Result类有异曲同工之妙。</p>
<p>var num: Int?这是一个人Optional的声明，意思不是“我声明了一个Optional的Int值”，而是“我声明了一个Optional类型，它可能包含一个Int值，也可能什么都不包含”，也就是说实际上我们声明的是Optional类型，而不是声明了一个Int类型！</p>
<p><em><strong>至于像Int!或者Int?这种写法，只是一种Optional类型的糖语法写法。</strong></em></p>
<p>以此类推String?是什么类型，泛型T?是什么类型，答案各位心中已经明了吧。</p>
<p>正是因为num是一个可选类型。所以它才能赋值为nil， <code>var num: Int = nil。</code>这样是不可能赋值成功的。因为Int类型中没有nil这个概念！</p>
<p>这就是Swift与OC一个很大区别，<em><strong>在OC中我们的对象都可以赋值为nil，而在Swift中，能赋值为nil只有Optional类型！</strong></em></p>
<h2 data-id="heading-2">解包的基本思路，使用if let或者guard let，而非强制解包</h2>
<p>我们先来看一个简单的需求，虽然这个需求在实际开发中意义不太大：</p>
<p>我们需要从网络请求获取到的一个人的身高(cm为单位)以除以100倍，以获取m为单位的结果然后将其结果进行返回。</p>
<p>设计思路：</p>
<p>由于实际网络请求中，后台可能会返回我们的身高为空(即nil)，所以在转模型的时候我们不能定义Float类型，而是定义Float?便于接受数据。</p>
<p>如果身高为nil，那么nil除以100是没有意义的，在编译器中Float?除以100会直接报错，那么其返回值也应该为nil，所以函数的返回值也是Float?类型</p>
<p>那么函数应该设计成为这个样子是这样的:</p>
<pre><code class="copyable">
  func getHeight(_ height: Float?) -> Float?

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果一般解包的话，我们的函数实现大概会写成这样:</p>
<pre><code class="language- copyable">
  func getHeight(_ height: Float?) -> Float? &#123;

     if height != nil &#123;

     return height! / 100

     &#125;

     return nil

  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用!进行强制解包，然后进行运算。</p>
<p>我想说的是使用强制解包固然没有错，不过如果在实际开发中这个height参数可能还要其他用途，那么是不是每使用一次都要进行强制解包？</p>
<p>强制解包是一种很危险的行为，一旦解包失败,就有崩溃的可能，也许你会说这不是有if判断,然而实际开发中，情况往往比想的复杂的多。<em><strong>所以安全的解包行为应该是通过if let 或者guard let来进行。</strong></em></p>
<pre><code class="copyable">
  func getHeight(_ height: Float?) -> Float? &#123;

     if let unwrapedHeight = height &#123;

     return unwrapedHeight / 100

     &#125;

     return nil

  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者：</p>
<pre><code class="copyable">
  func getHeight(_ height: Float?) -> Float? &#123;

     guard let unwrapedHeight = height else &#123;

     return nil

     &#125;

     return unwrapedHeight / 100

  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么if let和guard let 你更倾向使用哪个呢？</p>
<p>在本例子中，其实感觉二者的差别不大，不过我个人更倾向于使用guard let。</p>
<hr>
<p>原因如下：</p>
<p>在使用if let的时候其大括号类中的情况才是正常情况，而外部主体是非正常情况的返回的nil；</p>
<p>而在使用guard let的时候，guard let else中的大括号是异常情况，而外部主体返回的是正常情况。</p>
<p><em><strong>对于一个以返回结果为目的的函数，函数主体展示正常返回值，而将异常抛出在判断中，这样不仅逻辑更清晰，而且更加易于代码阅读。</strong></em></p>
<hr>
<h2 data-id="heading-3">解包深入</h2>
<p>有这么一个需求，从本地路径获取一个json文件，最终将其转为字典，准备进行转模型操作。</p>
<p>在这个过程中我们大概有这么几个步骤：</p>
<h4 data-id="heading-4">1. 获取本地路径 </h4>
<pre><code class="copyable">func path(forResource name: String?, ofType ext: String?) -> String?
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">2. 将本地路径读取转为Data </h4>
<pre><code class="copyable">init(contentsOf url: URL, options: Data.ReadingOptions = default) throws
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">3. JSON序列化</h4>
<pre><code class="copyable">class func jsonObject(with data: Data, options opt: JSONSerialization.ReadingOptions = []) throws -> Any
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">4. 是否可以转为字典类型</h4>
<p>我们可以看到以上几个函数中，获取路径获取返回的路径结果是一个可选类型而转Data的方法是抛出异常，JSON序列化也是抛出异常，至于最后一步的类型转换是使用as？ [Sting: Any]这样的操作</p>
<h4 data-id="heading-8">这个函数我是这来进行设计与步骤分解的：</h4>
<p>函数的返回类型为可选类型，因为下面的4步中都有可能失败进而返回nil。</p>
<p>虽然有人会说第一步获取本地路径，一定是本地有的才会进行读取操作，但是作为一个严谨操作，凡事和字符串打交道的书写都是有隐患的，所以我这里还是用了guard let进行守护。</p>
<p>这个函数看起来很不简洁，每一个guard let 后面都跟着一个异常返回，甚至不如使用if let看着简洁</p>
<p>但是这么写的好处是：<em><strong>在调试过程中你可以明确的知道自己哪一步出错</strong></em></p>
<pre><code class="copyable">
  func getDictFromLocal() -> [String: Any]? &#123;

     /// 1 获取路径

     guard let path = Bundle.main.path(forResource: "test", ofType:"json") else &#123;

       return nil

     &#125;

     /// 2 获取json文件里面的内容

     guard let jsonData = try? Data.init(contentsOf: URL.init(fileURLWithPath: path)) else &#123;

       return nil

     &#125;

     /// 3 解析json内容

     guard let json = try? JSONSerialization.jsonObject(with: jsonData, options:[]) else &#123;

       return nil

     &#125;

     /// 4 将Any转为Dict

     guard let dict = json as? [String: Any] else &#123;

       return nil

     &#125;

     return dict

  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然,如果你要追求简洁,这么写也未尝不可,一波流带走</p>
<pre><code class="copyable">
  func getDictFromLocal() -> [String: Any]? &#123;

     guard let path = Bundle.main.path(forResource: "test", ofType:"json"),

     let jsonData = try? Data.init(contentsOf: URL.init(fileURLWithPath: path)),

     let json = try? JSONSerialization.jsonObject(with: jsonData, options:[]),

     let dict = json as? [String: Any] else &#123;

       return nil

     &#125;

     return dict

  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>guard let与if let不仅可以判断一个值的解包,而且可以进行连续操作</strong></em></p>
<p>像下面这种写法，更加追求的是结果，对于一般的调试与学习，多几个guard let进行拆分，未尝不是好事。</p>
<p>至于哪种用法更适合，因人而异。</p>
<h2 data-id="heading-9">可选链的解包</h2>
<p>至于可选链的解包是完全可以一步到位，假设我们有以下这个模型。</p>
<pre><code class="copyable">
  class Person &#123;

     var phone: Phone?

  &#125;

  class Phone &#123;

     var number: String?

  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>Person类中有一个手机对象属性，手机类中有个手机号属性，现在我们有位小明同学，我们想知道他的手机号。</p>
<p>小明他不一定有手机，可能有手机而手机并没有上手机号码。</p>
<pre><code class="copyable">
  let xiaoming = Person()

  guard let number = xiaoming.phone?.number else &#123;

     return

  &#125;
  
  print(number)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只是抛砖引玉，更长的可选链也可以一步到位，而不必一层层进行判断，因为可选链中一旦有某个链为nil，那么就会返回nil。</p>
<h2 data-id="heading-10">nullable和nonnull</h2>
<p>我们先来看这两个函数,PHImageManager在OC与Swift中通过PHAsset实例获取图片的例子</p>
<pre><code class="copyable">
  [[PHImageManager defaultManager] requestImageForAsset:asset targetSize:size contentMode:PHImageContentModeDefault options:options resultHandler:^(UIImage * _Nullable result, NSDictionary * _Nullable info) &#123;

     //、 非空才进行操作 注意_Nullable,Swift中即为nil,注意判断

     if (result) &#123;

     &#125;

  &#125;];

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">
PHImageManager.default().requestImage(for: asset, targetSize: size, contentMode: .default, options: options, resultHandler: &#123; (result: UIImage?, info: [AnyHashable : Any]?) in

   guard let image = result else &#123; return &#125;

&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Swift中闭包返回的是两个可选类型，result: UIImage?与info: [AnyHashable : Any]? </p>
<p>而在OC中返回的类型是 UIImage * _Nullable result, NSDictionary * _Nullable info</p>
<p>注意观察OC中返回的类型UIImage * 后面使用了_Nullable来修饰,至于Nullable这个单词是什么意思，我想稍微有点英文基础的应该一看就懂--"可以为空"，<em><strong>这不恰恰和Swift的可选类型呼应吗？</strong></em></p>
<p>另外还有PHFetchResult遍历这个函数,我们再来看看在OC与Swift中的表达</p>
<pre><code class="copyable">
  PHFetchResult *fetchResult;

  [fetchResult enumerateObjectsUsingBlock:^(id _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) &#123;

  &#125;];

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">
  let fetchResult: PHFetchResult

  fetchResult.enumerateObjects(&#123; (obj, index, stop) in

  &#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看见OC中Block中的回调使用了Nonnull来修饰，即不可能为空，不可能为nil，一定有值，对于使用这样的字符修饰的对象，我们就不必为其做健壮性判断了。</p>
<p>这也就是nullable与nonnull两个关键字出现的原因吧--与Swift做桥接使用以及显式的提醒对象的状态</p>
<h2 data-id="heading-11">一点点Swift与OC的语言思考</h2>
<p>我之前写过一篇文章,是说有关于一个字符串拼接函数的</p>
<p><a href="https://www.jianshu.com/p/b1ff3ab6c80f" target="_blank" rel="nofollow noopener noreferrer">从Swift来反思OC的语法</a></p>
<p>OC函数是这样的：</p>
<pre><code class="copyable">
- (NSString *)stringByAppendingString:(NSString *)aString;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>Swift中函数是这样的：</p>
<pre><code class="copyable">
public mutating func append(_ other: String)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>仅从API来看，OC的入参是很危险的,因为类型是NSString *</p>
<p>那么nil也可以传入其中，而传入nil的后果就是崩掉，我觉得对于这种传入参数为nil会崩掉的函数需要特别提醒一下，应该写成这样:</p>
<pre><code class="copyable">
- (NSString *)stringByAppendingString:(NSString * _Nonnull)aString;

/// 或者下面这样

- (NSString *)stringByAppendingString:(nonnull NSString *)aString;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>以便告诉程序员，入参不能为空，不能为空，不能为空，重要的事情说三遍！！！</p>
<p>反观Swift就不会出现这种情况，other后面的类型为String，而不是String?，说明入参是一个非可选类型。</p>
<p>基于以上对于代码的严谨性，所以我才更喜欢使用Swift进行编程。</p>
<p>当然，Swift的严谨使得它失去部分的灵活性，OC在灵活性上比Swift卓越。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            