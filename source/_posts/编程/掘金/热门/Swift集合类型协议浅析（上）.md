
---
title: 'Swift集合类型协议浅析（上）'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3a0b39a70c044d2941a1efc2979e888~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 00:21:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3a0b39a70c044d2941a1efc2979e888~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>导 读</strong></p>
<p>狐友技术团队</p>
<p>Swift是一门面向协议的语言，协议可以被扩展，来给遵循该协议的类型提供方法等具体实现，通过扩展协议，我们可以为协议所要求的方法提供默认实现。在Swift出现以前，协议在iOS中就十分重要，想想UITableViewDataSource 和 UITableViewDelegate 等协议的讨论，可以说他们每天出现在我们的脑海里；使用Swift编程中一定会用到标准库中的协议，例如Array就是一个继承了10个协议的Struct，Bool类型是一个继承了7个协议的Struct；</p>
<p>本篇文章为Swift集合类型协议浅析系列文章的上篇，在这篇（上）中，我们尝试去解读一些基础协议的内部关系和逻辑，向你展示Swift如此强大的秘密。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3a0b39a70c044d2941a1efc2979e888~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Sequence</strong></p>
<p>Sequence是一组值的列表，能够提供对元素的顺序、迭代访问。</p>
<pre><code class="copyable">1protocol Sequence &#123;2   associatedtype Iterator3   func makeIterator() -> Iterator4&#125;5protocol IteratorProtocol &#123;6   associatedtype Element7   mutating func next() -> Element?8&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遵循Sequence协议需要有一个名为makeIterator的获取遍历器的方法，返回遍历器Iterator，Iterator遵循IteratorProtocol协议，协议有一个mutating的next方法，这个方法返回Sequence中下一个对象，直到没有返回nil。</p>
<p>举个例子：</p>
<pre><code class="copyable">1struct InfiniteIterator: IteratorProtocol &#123;2  let value: Int3  mutating func next() -> Int? &#123;4    return value5  &#125;6&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>InfiniteIterator遵循IteratorProtocol协议，所以需要有next方法，这里我们简化一下，让next的返回值始终是value：</p>
<pre><code class="copyable">1var iterator = InfiniteIterator(value: 24)2iterator.next()   //243iterator.next()   //24
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你会发现输出始终是24，下面我们继续实现Sequence协议：</p>
<pre><code class="copyable">1struct InfiniteSequence: Sequence &#123;2  let value: Int3  func makeIterator() -> InfiniteIterator &#123;4    return InfiniteIterator(value: value)  //注意此处5  &#125;6&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现makeIterator方法，返回的类型是上一步刚刚实现的遵循IteratorProtocol的协议对象InfiniteIterator，这样一个遵循Sequence协议的对象就构成了；我们可以尝试使用Sequence协议的prefix方法，取前几个对象测试：</p>
<pre><code class="copyable">1let infinite = InfiniteSequence(value: 20)2for value in infinite.prefix(5) &#123;3  print(value)   //204&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遵循Sequence的类型都可以使用for in遍历，如：</p>
<pre><code class="copyable">1let array = [1,2,3]2for item in array &#123;3    print(item)4&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么为什么能够这么使用呢？内部的实现类似下面，由于有了迭代器和获得下一个元素的next方法，我们就可以知道下一个，下一个的下一个，不断重复。</p>
<pre><code class="copyable">1var iterator = someSequence.makeIterator()2while let element = iterator.next() &#123;3   doSomething(with:element)4&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单小结一下：</p>
<p>（1）Sequence可以是有限序列，也可以是无限序列，如同上面InfiniteSequence就是一个无限序列；</p>
<p>（2）Sequence只可以迭代一次，有些时候可以多次进行迭代，但是不能保证每次都可以对其多次迭代。</p>
<p><strong>AnySequence</strong></p>
<p>为了简化创建Sequence需要遵循协议的复杂性，我们发现标准库帮我们提供了一个sequence方法：</p>
<pre><code class="copyable">1func sequence<T>(first: T, next: @escaping (T) -> T?) -> UnfoldFirstSequence<T>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数有两个参数，第一个参数需要Sequence序列返回的第一个值，第二个参数是一个闭包，接受之前的sequence元素并返回下一个：</p>
<pre><code class="copyable">1func infiniteBasic(value: Int) -> UnfoldSequence<Int, (Int?, Bool)> &#123;2 return sequence(first: value) &#123; _ in return value &#125;3&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回类型UnfoldSequence 遵循IteratorProtocol和Sequence，这样会简化上一步，就不需要写两个类分别遵循这两个协议：</p>
<pre><code class="copyable">1for value in infiniteBasic(value: 24).prefix(5) &#123;2  print(value)3&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果仍然是24，与前面的分别实现的效果一致；</p>
<p>然后我们就来看看这小节的AnySequence，它是一个类型擦除器，官方这样定义：</p>
<blockquote>
<p>An instance of AnySequence forwards its operations to an underlying base sequence having the same Element type, hiding the specifics of the underlying sequence.</p>
</blockquote>
<p>它本质上并没有什么作用，只是用来隐藏内部真实的类型，可以类比OC类型中的id，有相似的作用。AnySequence遵循Sequence协议，所以上面的infiniteBasic可以改造为：</p>
<pre><code class="copyable">1func infinite(value: Int) -> AnySequence<Int> &#123;2  return AnySequence &#123;3    sequence(first: value) &#123; _ in return value &#125;4  &#125;5&#125;6for value in infinite(value: 24).prefix(5) &#123;7  print(value)    //24  8&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>AnyIterator</strong></p>
<p>类型擦除序列。AnyIterator是AnySequence的实例，将其操作转发给具有相同元素类型的底层基序列，从而隐藏底层序列的细节。实质是传入一个生成下一个元素的闭包，内部通过next方法往后遍历下一个Element元素类型。</p>
<pre><code class="copyable">1func infinite(value: Int) -> AnySequence<Int> &#123;2  return AnySequence<Int> &#123;3    AnyIterator<Int> &#123; value &#125;4  &#125;5&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>AnyIterator中闭包return下一个元素，其中很适合使用defer做索引的+1获-1操作，这样隐藏了IteratorProtocol的实现，比如下面的例子：</p>
<pre><code class="copyable"> 1var x=0 2func infinite2(value: Int) -> AnySequence<Int> &#123; 3    return AnySequence<Int> &#123; 4        AnyIterator<Int> &#123; 5            defer &#123; 6                x+=1 7            &#125; 8            return x<15 ? x : nil 9        &#125;10    &#125;11&#125;



1for value in infinite2(value: 24) &#123;2    print(value)3&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码会每次不断迭代+1返回，直到15为止。</p>
<p>小结一下目前用到的这几个类型的关系，Sequence协议有Iterator属性，这个属性遵循IteratorProtocol协议，UnfoldSequence协议同时遵循Sequence协议和IteratorProtocol协议，AnySequence遵循Sequence协议，AnySequence也有相同Iterator属性，这个属性遵循AnyIterator协议，而AnyIterator协议又同时遵循IteratorProtocol和Sequence，构成了一个关联关系，所以我们可以通过AnySequence和AnyIterator的组合构成Sequence。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf8fa975ceef43979914aed7a19d3670~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Collection</strong></p>
<p>collection 是一个有索引的sequence，可以从任何index反复寻址很多次（单向）。</p>
<p>实现一个collection：</p>
<ul>
<li>
<p>定义Comaprable index type；</p>
</li>
<li>
<p>定义 startIndex；</p>
</li>
<li>
<p>定义 endIndex，是最后一个元素的下一个；</p>
</li>
<li>
<p>定义方法 index(after:) 增加index；</p>
</li>
<li>
<p>定义O(1) subscript operator get only 通关给定index，返回元素element。</p>
</li>
</ul>
<p>我们来举一个具体的例子，称为Fizz Buzz Collection；我们要创建一个范围从1到100的集合，打印范围1-100，被3整除时，print Fizz；被5整除时，print Buzz；如果同时能够被3和5整除，print FizzBuzz。</p>
<pre><code class="copyable"> 1struct FizzBuzz: Collection &#123; 2 3    typealias Index = Int 4 5    var startIndex: Index &#123; 6        return 1 7    &#125; 8 9    var endIndex: Index &#123;10        return 10111    &#125;1213    func index(after i: Index) -> Index &#123;14        return i + 115    &#125;1617    func index(_ i: Int, offsetBy distance: Int) -> Int &#123;18        return i + distance19    &#125;2021    subscript (index: Index) -> String &#123;22        precondition(indices.contains(index), "out of 1-100")23        switch (index.isMultiple(of: 3), index.isMultiple(of: 5)) &#123;24        case (false, false):25            return String(index)26        case (true, false):27            return "Fizz"28        case (false, true):29            return "Buzz"30        case (true, true):31            return "FizzBuzz"32        &#125;33    &#125;34&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Collection继承Sequence，与Sequence不同的是，Collection不再可能是无限的，你总能知道集合当中有多少个元素，因此我们可以对集合进行多次迭代；而对序列而言，一般只能迭代一次；另外，协议中新增的主要元素就是名为Index的新关联类型，Collection的范围通过属性从startIndex到endIndex标记，需要注意的是，endIndex指向最后一个元素的下一个位置，所以是101；另外，Index这个关联类型必须是Comparable，要获得下一个元素会增加index，直到抵达endIndex，这时候迭代会终止。</p>
<pre><code class="copyable">1for value in FizzBuzz() &#123;2    print(value)3&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>BidirectionalCollection</strong></p>
<p>双向集合与集合非常类似，只是它多了一个功能。与 Collection 继承自 Sequence 相同，BidirectionalCollection 继承自 Collection，但是双向集合可以向两个方向任意移动。在集合当中，前进我们已经有了 indexAfter 这个函数，所以为了增加后退的功能，需要再增加一个名为 indexBefore 的新函数，它将可以让我们以相反的顺序来遍历集合。</p>
<pre><code class="copyable">1protocol Collection &#123;2  //...3  func index(after index: Index) -> Index4&#125;56protocol BidirectionalCollection: Collection &#123;7  func index(before index: Index) -> Index8&#125;9
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以试想一下如果是一个Collection普通集合，如果想要得到最后一个元素该如何处理？</p>
<p>显然你需要一个一个的遍历，直到最后一个元素，这样显然太慢了，我们更希望一步跳到最后，并立即将末尾的值返回，现在有了BidirectionalCollection，就很不一样了，先检查集合是否为空，如果为空，那么直接返回nil即可；如果不是，我们就需要取endIndex，然后通过indexBefore得到endIndex的前一个索引，这样就得到了last元素。</p>
<pre><code class="copyable">1var last: Iterator.Element? &#123;2    guard !self.isEmpty else &#123; return nil &#125;3    let indexOfLastItem = self.index(before: self.endIndex)4    return self[indexOfLastItem]5&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>RandomAccessCollection</strong></p>
<p>遵循此协议可以更快地访问值。你可以直接跳转到想要获取的那个元素，而不必去逐步遍历；RandomAccessCollection继承BidirectionalCollection，可以在常量时间访问任何元素的集合，我们常用的Array就是一个例子。</p>
<p>遵循RandomAccessCollection需要实现index(_:offsetBy:)和distance(from:to:)方法或者Index遵循Strideable协议。</p>
<p><strong>MutableCollection</strong></p>
<p>支持集合通过下标的方式改变自身的元素，即 array[index] = newValue。该协议在 Collection 的基础上新增的 API 是下标subscript[5]必须提供的一个setter方法。</p>
<p><strong>RangeReplaceableCollection</strong></p>
<p>支持插入和删除任意区间的元素集合；遵循RangeReplaceableCollection协议需要实现：</p>
<p>（1）空的初始化集合；</p>
<p>（2）实现replaceSubrange(_:with:)，RangeReplaceableCollection协议提供了这个方法的默认实现，它用来替换当前集合中指定范围中的元素。目标范围和用来替换集合的长度可以不同。</p>
<p>我们再回头看看文章开始处这张集合类型关系的图谱，你会发现RangeReplaceableCollection和MutableCollection位于同一个层级，并没有继承关系，一些类型只符合MutableCollection（例如UnsafeMutableBufferPointer[6]），一些只适用于RangeReplaceableCollection（例如String.CharacterView），只有一部分同时遵守，如图中所示的Array：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84b94c3b15b04123b1f6467099e73bc9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>结语</strong></p>
<p>Sequence 和 Collection 组成了 Swift 中集合类型的根基。而专门性的集合类型 BidirectionalCollection、RandomAccessCollection、MutableCollection 和 RandomAccessCollection 对你自定义的类型和算法的功能和性能特性提供了非常细粒度的控制，构成了强大的功能组合。</p>
<p>参考：/ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" target="_blank">Github</a> /</p></div>  
</div>
            