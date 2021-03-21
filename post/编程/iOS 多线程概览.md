
---
title: iOS 多线程概览
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Fri, 19 Feb 2021 00:55:47 GMT
thumbnail: https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/351466fe66794aff8ca268aae1cc9fdc~tplv-k3u1fbpfcp-watermark.image
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><h6 align="right" data-id="heading-0">小时光</h6>
<h6 align="right" data-id="heading-1"><a href="https://dengfeng520.github.io/" target="_blank" rel="nofollow noopener noreferrer">我的博客</a></h6>
<blockquote>
<h3 data-id="heading-2">1、为什么所有的UI操作都在主线程中</h3>
</blockquote>
<p>不仅是iOS系统，包括Android等，所有的UI渲染、操作都在主线程中来完成。那为什么不采用多线程的方式呢？
使用多线程渲染UI更快，操作更流畅。但是系统设计者和开发者来说，需要解决线程问题的成本就更高了，也就是说成本远大于收益了。所以工程师们把所有的UI渲染和操作全都放在了主线程中。参考<a href="https://juejin.cn/post/6844903763011076110" target="_blank">为什么必须在主线程操作UI</a>。</p>
<blockquote>
<h3 data-id="heading-3">2、为什么要使用多线程</h3>
</blockquote>
<p>即然所有的UI操作都是单线程的，那么为何还需要多线程呢？在App开发中，所遇到不仅有UI操作，还有一些其他的费时操作，如网络请求、文件读取操作、AR模型下载等。此时就需要开发者把费时的操作放到子线程中去，完成后再返回住线程执行一些UI操作。
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/351466fe66794aff8ca268aae1cc9fdc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
如上图所示，当进入这个Controller时开始下载图片，由于下载的图片较多需要几秒甚至十几秒，在下载时我同步滑动底部的<code>UISlider</code>,此时<code>UISlider</code>并没有滑动，直到所有的图片全部下载完成后才滑动。</p>
<p>试想如果我们的使用的每个App在费时操作时都需要等待很长时间用户才能操作，这样势必会给用户很不好的体验。此时的解决方案是创建一个新的线程来下载图片，这样既不影响用户的UI操作也不影响图片下载。</p>
<blockquote>
<h3 data-id="heading-4">3、多线程的实现方式</h3>
</blockquote>
<p>Apple为开发者提供的三种多线程实现方式:</p>
<p>(1)、 Thread</p>
<ul>
<li>轻量级</li>
<li>需要开发者手动管理线程生命周期和线程同步</li>
</ul>
<p>(2)、 GCD（Grand Central Dispatch）</p>
<ul>
<li>相对<code>Thread</code>而言，不需要管理线程生命周期，操作更简单</li>
<li>本身维护了一个线程池，会自动根据当前手机系统的情况来动态管理线程，不需要开发者来管理线程池和线程并发情况</li>
<li>底层源码是开源的，点击<a href="https://opensource.apple.com/tarballs/libdispatch/" target="_blank" rel="nofollow noopener noreferrer">Apple Open Spurce</a>查看源码</li>
</ul>
<p>(3)、 Cocoa Operation</p>
<ul>
<li>面向对象的API</li>
<li>可以取消、依赖、任务优先级、可以子类化</li>
</ul>
<blockquote>
<h3 data-id="heading-5">4、多线程常用队列</h3>
</blockquote>
<p>多线程可以根据任务执行的队列方式分为三种队列：</p>
<ul>
<li>主队列: 在主线程中执行的任务</li>
<li>串行队列（Serial Queue）: 任务按照先后顺序执行，同一时刻只会执行一个任务</li>
<li>并行队列（Concurrent Queue）: 多个任务同时执行，完成的顺序不一定</li>
</ul>
<p>参考 <a href="https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/OperationQueues/OperationQueues.html#//apple_ref/doc/uid/TP40008091-CH102-SW2" target="_blank" rel="nofollow noopener noreferrer">Apple Developer About Dispatch Queues</a></p>
<blockquote>
<h3 data-id="heading-6">5、Serial Queue</h3>
</blockquote>
<ul>
<li>（1）、串行队列处理并发任务</li>
</ul>
<p>前面说过，对于一些耗时操作，一般将其放到一个子线程中执行，待完成后再返回主线程中刷新UI。核心代码如下：</p>
<pre><code class="copyable">// 图片下载管理类`DownloaderManager`
public class DownloaderManager: NSObject {
    public class func downloadImageWithURL(_ url: String) -> UIImage? {
        guard let data = try? Data(contentsOf: URL(string: url)!) else { return nil }
        return UIImage(data: data)
    }
}

// 创建一个队列
let serialQueue = DispatchQueue(label: "TSN.RPChat.io")
for (index, imgurl) in DownloaderManager.imageArray.enumerated() {
   // 把下载任务加载到队列中
   serialQueue.async { 
      let image = DownloaderManager.downloadImageWithURL(imgurl)
      DispatchQueue.main.async {
         girlsImg.image = image
      }
   }
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时再次运行代码，发现在下载图片的同时也能滑动<code>UISlider</code>，同时发现图片的加载顺序是按照从上到下的顺序加载的。默认情况下，系统会创建一个串行队列，也就是下载完成第一张图片之后再去下载第二张。此时对我来说，我的目的是下载并把图片全部显示出来，我并不关心图片的下载和加载顺序。这样我就需要在创建队列时设置这个队列为一个并行队列。</p>
<p><img alt="串行队列" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ff481b519e44cf1ab3c1442c628bbbd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<h3 data-id="heading-7">6、Concurrent Queue</h3>
</blockquote>
<p>作为队列，<code>concurrent queue</code>中的任务虽然是按照进入队列的顺序启动，但不用等待之前的任务完成，iOS会根据当前系统情况启动多个线程并行执行队列中的任务。</p>
<p>在创建队列时设置<code>attributes</code>属性为<code>concurrent</code>就创建了一个并行队列。</p>
<pre><code class="copyable">let concurrentQueue = DispatchQueue(label: "TSN.RPChat.io", attributes: .concurrent)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时运行工程，可以看到图片并不是按照先后顺序加载的，说明同一个<code>concurrent queue</code>中的所有任务在并行执行。
<img alt="Concurrent Queue" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12d73fba49ea4e6992822fc67e3279a1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<h3 data-id="heading-8">7、面向对象的Cocoa Operation</h3>
</blockquote>
<p>上面创建的队列我使用的是GCD（Grand Central Dispatch）方式，尽管GCD对线程管理进行了封装并加入了面向对象管理模式。但是如果我要对一个队列中的任务做更多的操作，如（查看状态、取消任务，控制任务的执行顺序等）仍然不太方便。考虑到这些问题，苹果为开发这提供了一个面向对象方式的多任务执行机制<a href="https://developer.apple.com/documentation/foundation/operation" target="_blank" rel="nofollow noopener noreferrer">Operation</a>。<code>Operation</code>是基于<code>GCD</code>的对象封装。</p>
<p>(1)、<strong><a href="https://developer.apple.com/documentation/foundation/operation" target="_blank" rel="nofollow noopener noreferrer">Operation概览</a></strong></p>
<p>Operation的一些使用状态：</p>
<ul>
<li>**<a href="https://developer.apple.com/documentation/foundation/operation/1412992-isready" target="_blank" rel="nofollow noopener noreferrer">isReady</a>**是否可执行，一般用于异步的情况下</li>
<li>**<a href="https://developer.apple.com/documentation/foundation/operation/1415621-isexecuting" target="_blank" rel="nofollow noopener noreferrer">isExexuting</a>**标记<code>Operation</code>是否正在执行中</li>
<li>**<a href="https://developer.apple.com/documentation/foundation/operation/1413540-isfinished" target="_blank" rel="nofollow noopener noreferrer">isFinished</a>**标记<code>Operation</code>是否已经执行完成了，一般用于异步</li>
<li>**<a href="https://developer.apple.com/documentation/foundation/operation#1661262" target="_blank" rel="nofollow noopener noreferrer">isCancelled</a>**标记<code>Operation</code>是否已经<code>cancel</code>了</li>
</ul>
<p>更多状态请参考<a href="https://developer.apple.com/documentation/foundation/operation#1661262" target="_blank" rel="nofollow noopener noreferrer">Apple Developer: Maintaining Operation Object States</a></p>
<p>(2)、<strong><a href="https://developer.apple.com/documentation/foundation/operationqueue" target="_blank" rel="nofollow noopener noreferrer">OperationQueue</a></strong></p>
<ul>
<li><strong>OperationQueue</strong>可以加入多个<code>Operation</code></li>
</ul>
<pre><code class="copyable">let ope1 = Operation()
let ope2 = Operation()
       
let que = OperationQueue()
que.addOperation(ope1)
que.addOperation(ope2)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>maxConcurrentOperationCount</code>可设置最大并发数当前,默认情况下，系统会根据当前情况动态确定最大并发数</li>
</ul>
<pre><code class="copyable">que.maxConcurrentOperationCount = 5
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此处需要注意的是最大并发数并不是线程数，最大并发数表示的是当前队列最多可同时执行的的任务（或线程）数量。</p>
<ul>
<li>可取消所有<code>Operation</code>，但当前正在执行的<code>Operation</code>不会取消</li>
<li>所有的<code>Operation</code>执行完毕后退出销毁</li>
</ul>
<p>(3)、<strong><a href="https://developer.apple.com/documentation/foundation/blockoperation" target="_blank" rel="nofollow noopener noreferrer">BlockOperation</a></strong></p>
<pre><code class="copyable">let queblock = BlockOperation.init(block: { [weak self] in
            
})
let que = OperationQueue.init()
que.maxConcurrentOperationCount = 3
que.addOperation(queblock)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(4)、<strong><a href="https://developer.apple.com/documentation/foundation/operation/1408085-completionblock" target="_blank" rel="nofollow noopener noreferrer">completionBlock</a></strong></p>
<p>当执行完一个任务时的回调.
我们可以通过创建Operation的方法，首先创建一个<code>Operation</code>对象，然后将其添加到队列中，这样做就可以通过设置<code>completionBlock</code>，在任务完成时得到通知。</p>
<p>(5)、默认优先级</p>
<p>苹果为<strong>Operation</strong>提供了优先级，<strong>Operation</strong>通过**<a href="https://developer.apple.com/documentation/foundation/operation/1413553-qualityofservice" target="_blank" rel="nofollow noopener noreferrer">qualityOfService</a>**属性来控制其优先级,来看源码：</p>
<pre><code class="copyable">public enum QualityOfService : Int {
    
    case userInteractive = 33

    case userInitiated = 25

    case utility = 17

    case background = 9

    case `default` = -1
}
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>userInteractive</strong>: 最高优先级，用于用户交互事件</li>
<li><strong>userInitiated</strong>:次高优先级，用于用户需要马上执行的事件</li>
<li><strong>utility</strong>:普通优先级，用于普通任务</li>
<li><strong>background</strong>:最低优先级，用于不重要的任务</li>
<li><strong>default</strong>:默认优先级，主线程和没有设置优先级的线程都默认为这个优先级</li>
</ul>
<pre><code class="copyable">operation.qualityOfService = .default
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过**<a href="https://developer.apple.com/documentation/foundation/operation/1411204-queuepriority" target="_blank" rel="nofollow noopener noreferrer">queuePriority</a>**属性来控制在<code>OperationQueue</code>中的优先级：</p>
<pre><code class="copyable">public enum QueuePriority : Int {

        case veryLow = -8

        case low = -4

        case normal = 0

        case high = 4

        case veryHigh = 8
    }
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">operation.queuePriority = .high
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(6)、使用<strong>OperationQueue</strong>下载图片</p>
<pre><code class="copyable">// 创建一个队列
let queue = OperationQueue()

// 创建一个Operation
queue.addOperation {
et image = DownloaderManager.downloadImageWithURL(imgurl)
OperationQueue.main.addOperation {
     girlsImg.image = image 
   }
}

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意的是：更新UI的代码要放到主线程中完成。使用<code>OperationQueue.main</code>获取主线程队列，然后添加<code>addOperation</code>把更新UI的任务放到主线程。
如果需要在下载完成时做一些相关操作，可以使用<code>completionBlock</code>,</p>
<pre><code class="copyable">let operation = BlockOperation(block: {
     // 要执行的任务，如下载图片等
     let image = DownloaderManager.downloadImageWithURL(imgurl)
     // 下载完成后，返回主线程渲染图片
     OperationQueue.main.addOperation {
         girlsImg.image = image
     }
})
operation.completionBlock = {
     // 执行完成后
}
// 设置最大并发数 不设置时系统回根据当前情况动态设置最大并发数 设置为1时为串行队列
queue.maxConcurrentOperationCount = 5
// 将Operation添加到queue队列中
queue.addOperation(operation)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(7)、设置任务之间的关联性</p>
<p><img alt="设置任务之间的关联性" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdaa9343667a42e4bf9562740fe05738~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
如图所示,当点击download按钮的时候开始下载图片，但是客户要求按照432的顺序加载，但是图片1不影响，此处需要用到<code>addDependency</code>方法，让图片按照432的顺序下载，图片1并行下载，核心代码如下：</p>
<pre><code class="copyable">let queue = OperationQueue()

let operation1 = BlockOperation(block: {
       let image = DownloaderManager.downloadImageWithURL(imgArray[0])
       OperationQueue.main.addOperation {
           self.girlsImg1.image = image
    }
})
operation1.completionBlock = {
    print("-------operation1")
 }
        
let operation2 = BlockOperation(block: {
        let image = DownloaderManager.downloadImageWithURL(imgArray[1])
        OperationQueue.main.addOperation {
           self.girlsImg2.image = image
     }
})
operation2.completionBlock = {
     print("-------operation2")
}
        
let operation3 = BlockOperation(block: {
    let image = DownloaderManager.downloadImageWithURL(imgArray[2])
        OperationQueue.main.addOperation {
          self.girlsImg3.image = image
    }
})
operation3.completionBlock = {
   print("-------operation3")
}
        
let operation4 = BlockOperation(block: {
    let image = DownloaderManager.downloadImageWithURL(imgArray[7])
    OperationQueue.main.addOperation {
         self.girlsImg4.image = image
    }
})
operation4.completionBlock = {
    print("-------operation4")
}

operation3.addDependency(operation4)
operation2.addDependency(operation3)
        
queue.addOperation(operation1)
queue.addOperation(operation4)
queue.addOperation(operation3)
queue.addOperation(operation2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此处把添加<code>Operation</code>到<code>Queue</code>的操作，放到了<code>addDependency</code>之后，确保执行前有正确的依赖关系。多次运行代码可以看到，图片的下载顺序依然是4->3->2的顺序。</p>
<pre><code class="copyable">-------operation1
-------operation4
-------operation3
-------operation2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(8)、取消执行的任务</p>
<p>除了设置一个队列中任务关联性之外，还可以控制取消队列中的任务，但是取消的结果会根据任务的状态而不同：</p>
<ul>
<li>已经完成的任务，取消不影响其结果</li>
<li>当一个任务被取消时所有与其关联的任务也会被取消</li>
<li>任务被取消后，<code>completionBlock</code>依旧会执行</li>
</ul>
<p><img alt="取消图片下载" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7b15b84bc8a490396eefb6115858fdc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如图所示，当我点击<code>download</code>按钮后快速点击<code>cancel</code>按钮，可以看到图片一的下载任务被<code>cancel</code>了。</p>
<pre><code class="copyable">let cancelItem = UIBarButtonItem()
cancelItem.title = "cancel"
cancelItem.rx.tap.subscribe(onNext: {
   self.queue.cancelAllOperations()
}).disposed(by: disposeBag)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此处可以通过<code>Operation</code>的<code>isCancelled</code>属性来判断任务是否被<code>cancel</code>。当<code>isCancelled</code>返回<code>true</code>表示该任务被<code>cancel</code>了。</p>
<pre><code class="copyable">-------operation4,false
-------operation3,false
-------operation2,false
-------operation1,true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本文主要简单介绍了Operation的一些简单应用，正确的理解和应用这些多线程技术是构建复杂App的基础，关于更多多线程的应用可参考官方多线程的文档：</p>
<p><strong><a href="https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/OperationQueues/OperationQueues.html#//apple_ref/doc/uid/TP40008091-CH102-SW2" target="_blank" rel="nofollow noopener noreferrer">Apple Developer About Dispatch Queues</a></strong></p>
<p><strong><a href="https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html" target="_blank" rel="nofollow noopener noreferrer">Apple Developer Threading Programming Guide</a></strong></p>
<p><strong><a href="https://github.com/dengfeng520/RPDemo/tree/main/OperationDemo" target="_blank" rel="nofollow noopener noreferrer">本文demo</a></strong></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            