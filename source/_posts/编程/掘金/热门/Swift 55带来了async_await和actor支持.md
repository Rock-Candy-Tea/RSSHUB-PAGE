
---
title: 'Swift 5.5带来了async_await和actor支持'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=9150'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 23:44:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=9150'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在<a href="https://developer.apple.com/videos/" target="_blank" rel="nofollow noopener noreferrer">WWDC21</a>上，苹果公司推出了Swift 5.5，可用于测试。在其新功能中，最令人期待的是使用<code>aysnc/await</code> 和行动者的<a href="https://developer.apple.com/documentation/swift/swift_standard_library/concurrency" target="_blank" rel="nofollow noopener noreferrer">更好的并发性支持</a>。</p>
<p>苹果表示，<a href="https://developer.apple.com/videos/play/wwdc2021/10132" target="_blank" rel="nofollow noopener noreferrer">异步功能</a>q旨在使并发的Swift代码更容易编写和理解。传统上，Swift使用闭包和完成处理程序来处理异步操作。众所周知，当你的代码有许多异步操作，或者控制流变得复杂时，这种方法很快就会导致 "回调地狱"。</p>
<p>Swift的异步函数则为语言带来了<a href="https://en.wikipedia.org/wiki/Coroutine" target="_blank" rel="nofollow noopener noreferrer">循环线</a>。</p>
<blockquote>
<p>函数可以选择成为异步的，允许程序员使用正常的控制流机制来组成涉及异步操作的复杂逻辑。编译器负责将一个异步函数翻译成适当的闭包和状态机集合。</p>
</blockquote>
<p><a href="https://github.com/apple/swift-evolution/blob/main/proposals/0296-async-await.md" target="_blank" rel="nofollow noopener noreferrer">下面的代码片断</a>显示了如何声明和调用<code>async</code> ，就像它们是同步的一样。</p>
<pre><code class="copyable">func loadWebResource(_ path: String) async throws -> Resource
func decodeImage(_ r1: Resource, _ r2: Resource) async throws -> Image
func dewarpAndCleanupImage(_ i : Image) async throws -> Image

func processImageData() async throws -> Image &#123;
  let dataResource  = try await loadWebResource("dataprofile.txt")
  let imageResource = try await loadWebResource("imagedata.dat")
  let imageTmp      = try await decodeImage(dataResource, imageResource)
  let imageResult   = try await dewarpAndCleanupImage(imageTmp)
  return imageResult
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然异步函数似乎大大简化了并发管理，但它们并没有排除死锁或状态损坏的可能性。特别是，程序员应该注意到 <a href="https://github.com/apple/swift-evolution/blob/main/proposals/0296-async-await.md#suspension-points" target="_blank" rel="nofollow noopener noreferrer"><em>暂停点</em></a>异步函数带来的问题。在一个暂停点，一个函数放弃了它的线程。例如，当你调用一个与不同执行上下文相关的异步函数时，就会发生这种情况。为了避免死锁或数据损坏的风险，异步函数应该避免调用可能阻塞其线程的函数。</p>
<blockquote>
<p>例如，获取一个mutex只能阻塞到当前运行的某个线程放弃mutex；这有时是可以接受的，但必须谨慎使用，以避免引入死锁或人为的可扩展性问题。相反，等待一个条件变量可以阻塞，直到一些任意的其他工作被安排为信号变量；这种模式强烈反对推荐。</p>
</blockquote>
<p>这个功能的一个有趣的演化<a href="https://github.com/apple/swift-evolution/blob/main/proposals/0297-concurrency-objc.md" target="_blank" rel="nofollow noopener noreferrer">，使调用异步的Objective-C API成为可能</a>，这些API使用完成处理程序，使用<code>await</code> 表达式。</p>
<p>另一方面，行动者是建立在<code>async</code> 和<code>await</code> 上的抽象，可以安全地访问可变的状态。简而言之，行为体封装了一些状态，并提供了一组方法来安全地访问它。</p>
<blockquote>
<p>与类不同的是，行为体每次只允许一个任务访问其可变状态，这使得多个任务的代码可以安全地与行为体的同一个实例进行交互。</p>
</blockquote>
<p>这是一个Swift actor的例子。</p>
<pre><code class="copyable">actor TemperatureLogger &#123;
    let label: String
    var measurements: [Int]
    private(set) var max: Int

    init(label: String, measurement: Int) &#123;
        self.label = label
        self.measurements = [measurement]
        self.max = measurement
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>行为体的方法可以从行为体内部同步或异步地使用，但编译器会强迫你使用异步操作从行为体外部读取行为体的状态。</p>
<p>如果你有兴趣学习Swift并发性在幕后的工作原理，了解Swift任务与Grand Central Dispatch的区别，以及如何在编写Swift并发性代码时考虑到性能，请不要错过苹果WWDC会议的<a href="https://developer.apple.com/videos/play/wwdc2021/10254/" target="_blank" rel="nofollow noopener noreferrer">Swift并发性。幕后</a>花絮。</p>
<p>Swift 5.5目前作为<a href="https://developer.apple.com/documentation/xcode-release-notes/xcode-13-beta-release-notes" target="_blank" rel="nofollow noopener noreferrer">Xcode 13测试版</a>的一部分，可以从<a href="https://developer.apple.com/download/" target="_blank" rel="nofollow noopener noreferrer">苹果开发者网站</a>下载。</p></div>  
</div>
            