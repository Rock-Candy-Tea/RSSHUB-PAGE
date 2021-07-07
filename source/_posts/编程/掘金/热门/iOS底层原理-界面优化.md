
---
title: 'iOS底层原理-界面优化'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42ee7010c48a49f58f6cb133df8092d8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 25 Jun 2021 01:51:29 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42ee7010c48a49f58f6cb133df8092d8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>界面优化无非就是解决卡顿问，优化界面流畅度，以下就通过先分析卡顿的原因，然后再介绍具体的优化方案，来分析如何做界面优化</p>
<ul>
<li>
<h4 data-id="heading-0">界面渲染流程</h4>
具体流程可以参考<a href="https://juejin.cn/post/6847902220403343374" target="_blank" title="https://juejin.cn/post/6847902220403343374">图片渲染初探</a>这里就大概讲一下图片渲染的流程，大体上可以分为三个阶段就是 <code>CPU</code>处理阶段 <code>GPU</code>处理阶段和视频控制器显示阶段。
<ol>
<li><code>CPU</code>主要是计算出需要渲染的模型数据</li>
<li><code>GPU</code>主要是根据 <code>CPU</code>提供的渲染模型数据渲染图片然后存到帧缓冲区</li>
<li>视频控制器冲帧缓冲区中读取数据最后成像</li>
</ol>
<strong>大致流程图解如下：</strong><br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42ee7010c48a49f58f6cb133df8092d8~tplv-k3u1fbpfcp-watermark.image" alt="16d81697920a87d3.png" loading="lazy" referrerpolicy="no-referrer"><br>
苹果为了解决图片撕裂的问题使用了 <code>VSync</code> + 双缓冲区的形式，就是显示器显示完成一帧的渲染的时候会向 发送一个垂直信号 <code>VSync</code>，收到这个这个垂直信号之后显示器开始读取另外一个帧缓冲区中的数据而 <code>App</code>接到垂直信号之后开始新一帧的渲染。</li>
<li>
<h4 data-id="heading-1">卡顿原理</h4>
通过上文张的界面渲染流程知道，在图一帧渲染完成之后会发送一个垂直信号此时开始读取另外一个帧缓冲区中的数据，加入此时 <code>CPU</code>和 <code>GPU</code>的工作还没有完成，也就是另外一个帧缓冲区还是加锁状态没有数据的时候，此时显示器显示的还是上一帧的图像那么这种情况就会一直等待下一帧绘制完成然后视频控制器再读取另外一个帧缓冲区中的数据然后成像，中间这个等待的过程就造成了掉帧，也就是会卡顿。<br>
<strong>卡顿图解如下：</strong><br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b39110780ca4436a53c26c87a87a079~tplv-k3u1fbpfcp-watermark.image" alt="16d8169791d4b86e.png" loading="lazy" referrerpolicy="no-referrer">
这种情况随会造成卡顿</li>
<li>
<h4 data-id="heading-2">卡顿检测</h4>
<ol>
<li>
<h5 data-id="heading-3">FPS监控</h5>
苹果的iPhone推荐的刷新率是<code>60Hz</code>,也就是每秒中刷新屏幕60次，也就是每秒中有60帧渲染完成，差不多每帧渲染的时间是<code>1000/60 = 16.67</code>毫秒整个界面会比较流畅，一般刷新率低于<code>45Hz</code>的就会出现明显的卡顿现象。这里可以通过<code>YYFPSLabel</code>来实现<code>FPS</code>的监控，该原理主要是依靠 <code>CADisplayLink</code>来实现的，通过<code>CADisplayLink</code>来监听每次屏幕刷新并获取屏幕刷新的时间，然后使用次数（也就是1）除以每次刷新的时间间隔得到<code>FPS</code>,具体源码如下：
<pre><code class="copyable">  #import "YYFPSLabel.h"
  #import "YYKit.h"

  #define kSize CGSizeMake(55, 20)

  @implementation YYFPSLabel &#123;
      CADisplayLink *_link;
      NSUInteger _count;
      NSTimeInterval _lastTime;
      UIFont *_font;
      UIFont *_subFont;

      NSTimeInterval _llll;
  &#125;

  - (instancetype)initWithFrame:(CGRect)frame &#123;
      if (frame.size.width == 0 && frame.size.height == 0) &#123;
          frame.size = kSize;
      &#125;
      self = [super initWithFrame:frame];

      self.layer.cornerRadius = 5;
      self.clipsToBounds = YES;
      self.textAlignment = NSTextAlignmentCenter;
      self.userInteractionEnabled = NO;
      self.backgroundColor = [UIColor colorWithWhite:0.000 alpha:0.700];

      _font = [UIFont fontWithName:@"Menlo" size:14];
      if (_font) &#123;
          _subFont = [UIFont fontWithName:@"Menlo" size:4];
      &#125; else &#123;
          _font = [UIFont fontWithName:@"Courier" size:14];
          _subFont = [UIFont fontWithName:@"Courier" size:4];
      &#125;

      //YYWeakProxy 这里使用了虚拟类来解决强引用问题
      _link = [CADisplayLink displayLinkWithTarget:[YYWeakProxy proxyWithTarget:self] selector:@selector(tick:)];
      [_link addToRunLoop:[NSRunLoop mainRunLoop] forMode:NSRunLoopCommonModes];
      return self;
  &#125;

  - (void)dealloc &#123;
      [_link invalidate];
  &#125;

  - (CGSize)sizeThatFits:(CGSize)size &#123;
      return kSize;
  &#125;

  - (void)tick:(CADisplayLink *)link &#123;
      if (_lastTime == 0) &#123;
          _lastTime = link.timestamp;
          NSLog(@"sdf");
          return;
      &#125;

      //次数
      _count++;
      //时间
      NSTimeInterval delta = link.timestamp - _lastTime;
      if (delta < 1) return;
      _lastTime = link.timestamp;
      float fps = _count / delta;
      _count = 0;

      CGFloat progress = fps / 60.0;
      UIColor *color = [UIColor colorWithHue:0.27 * (progress - 0.2) saturation:1 brightness:0.9 alpha:1];

      NSMutableAttributedString *text = [[NSMutableAttributedString alloc] initWithString:[NSString stringWithFormat:@"%d FPS",(int)round(fps)]];
      [text setColor:color range:NSMakeRange(0, text.length - 3)];
      [text setColor:[UIColor whiteColor] range:NSMakeRange(text.length - 3, 3)];
      text.font = _font;
      [text setFont:_subFont range:NSMakeRange(text.length - 4, 1)];

      self.attributedText = text;
  &#125;

  @end
<span class="copy-code-btn">复制代码</span></code></pre>
<code>FPS</code>只用在开发阶段的辅助性的数值，因为他会频繁唤醒 <code>runloop</code>如果 <code>runloop</code>在闲置的状态被 <code>CADisplayLink</code>唤醒则会消耗性能。</li>
<li>
<h5 data-id="heading-4">通过RunLoop检测卡顿</h5>
通过监听主线程 <code>Runloop</code>一次循环的时间来判断是否卡顿，这里需要配合使用 <code>GCD</code>的信号量来实现，设置初始化信号量为0，然后开一个子线程等待信号量的触发，也是就是在子线程的方法里面调用 <code>dispatch_semaphore_wait</code>方法设置等待时间是1秒，然后主线程的 <code>Runloop</code>的 <code>Observer</code>回调方法中发送信号也就是调用 <code>dispatch_semaphore_signal</code>方法，此时时间可以置为0了，如果是等待时间超时则看此时的 <code>Runloop</code>的状态是否是 <code>kCFRunLoopBeforeSources</code>或者是 <code>kCFRunLoopAfterWaiting</code>，如果在这两个状态下两秒则说明有卡顿，详细代码如下：（代码中也有相关的注释）
<pre><code class="copyable">#import "LGBlockMonitor.h"

  @interface LGBlockMonitor ()&#123;
      CFRunLoopActivity activity;
  &#125;

  @property (nonatomic, strong) dispatch_semaphore_t semaphore;
  @property (nonatomic, assign) NSUInteger timeoutCount;

  @end

  @implementation LGBlockMonitor

  + (instancetype)sharedInstance &#123;
      static id instance = nil;
      static dispatch_once_t onceToken;

      dispatch_once(&onceToken, ^&#123;
          instance = [[self alloc] init];
      &#125;);
      return instance;
  &#125;

  - (void)start&#123;
      [self registerObserver];
      [self startMonitor];
  &#125;

  static void CallBack(CFRunLoopObserverRef observer, CFRunLoopActivity activity, void *info)
  &#123;
      LGBlockMonitor *monitor = (__bridge LGBlockMonitor *)info;
      monitor->activity = activity;
      // 发送信号
      dispatch_semaphore_t semaphore = monitor->_semaphore;
      dispatch_semaphore_signal(semaphore);
  &#125;

  - (void)registerObserver&#123;
      CFRunLoopObserverContext context = &#123;0,(__bridge void*)self,NULL,NULL&#125;;
      //NSIntegerMax : 优先级最小
      CFRunLoopObserverRef observer = CFRunLoopObserverCreate(kCFAllocatorDefault,
                                                              kCFRunLoopAllActivities,
                                                              YES,
                                                              NSIntegerMax,
                                                              &CallBack,
                                                              &context);
      CFRunLoopAddObserver(CFRunLoopGetMain(), observer, kCFRunLoopCommonModes);
  &#125;

  - (void)startMonitor&#123;
      // 创建信号c
      _semaphore = dispatch_semaphore_create(0);
      // 在子线程监控时长
      dispatch_async(dispatch_get_global_queue(0, 0), ^&#123;
          while (YES)
          &#123;
              // 超时时间是 1 秒，没有等到信号量，st 就不等于 0， RunLoop 所有的任务
              // 没有接收到信号底层会先对信号量进行减减操作，此时信号量就变成负数
              // 所以开始进入等到，等达到了等待时间还没有收到信号则进行加加操作复原信号量
              // 执行进入等待的方法dispatch_semaphore_wait会返回非0的数
              // 收到信号的时候此时信号量是1  底层是减减操作，此时刚好等于0 所以直接返回0
              long st = dispatch_semaphore_wait(self->_semaphore, dispatch_time(DISPATCH_TIME_NOW, 1 * NSEC_PER_SEC));
              if (st != 0)
              &#123;
                  if (self->activity == kCFRunLoopBeforeSources || self->activity == kCFRunLoopAfterWaiting)
                  &#123;
                      //如果一直处于处理source0或者接受mach_port的状态则说明runloop的这次循环还没有完成
                      if (++self->_timeoutCount < 2)&#123;
                          NSLog(@"timeoutCount==%lu",(unsigned long)self->_timeoutCount);
                          continue;
                      &#125;
                      // 如果超过两秒则说明卡顿了
                      // 一秒左右的衡量尺度 很大可能性连续来 避免大规模打印!
                      NSLog(@"检测到超过两次连续卡顿");
                  &#125;
              &#125;
              self->_timeoutCount = 0;
          &#125;
      &#125;);
  &#125;



  @end
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h5 data-id="heading-5">微信matrix</h5>
此方案也是借助 <code>runloop</code>实现的大体流程和方案三相同，不过微信加入了堆栈分析，能够定位到耗时的方法调用堆栈，所以需要准确的分析卡顿原因可以借助微信matrix来分析卡顿。当然也可以在方案2中使用 <code>PLCrashReporter</code>这个开源的第三方库来获取堆栈信息</li>
<li>
<h5 data-id="heading-6">滴滴DoraemonKit</h5>
实现方案大概就是在子线程中一直 <code>ping</code>主线程，在主线程卡顿的情况下，会出现断在的无响应的表现，进而检测卡顿</li>
</ol>
</li>
<li>
<h4 data-id="heading-7">优化方案</h4>
上文中分析卡顿的原因我们知道主要就是在 <code>CPU</code>和 <code>GPU</code>阶段占用时间太长导致了掉帧卡顿，所以界面优化主要工作就是给 <code>CPU</code>和 <code>GPU</code>减负
<ul>
<li>
<h5 data-id="heading-8">预排版</h5>
预排版主要是对 <code>CPU</code>进行减负。<br>
假设现在又个 <code>TableView</code>其中需要根据每个 <code>cell</code>的内容来定 <code>cell</code>的高度。我们知道 <code>TableView</code>有重用机制，如果复用池中有数据，即将滑入屏内的 <code>cell</code>就会使用复用池内的 <code>cell</code>,做到节省资源，但是还是要根据新数据的内容来计算 <code>cell</code>的高度,重新布局新 <code>cell</code>中内容的布局 ，这样反复滑动 <code>TableView</code>相同的 <code>cell</code>就会反复计算其 <code>frame</code>，这样也给 <code>CPU</code>带来了负担。如果在得到数据创建模型的时候就把 <code>cell</code> <code>frame</code>算出，<code>TableView</code>返回模型中的 <code>frame</code>这样的话同样的一条 <code>cell</code>就算来回反复滑动 <code>TableView</code>,计算 <code>frame</code>这个操作也就仅仅只会执行一次，所以也就做到了减负的功能,如下图：一个 <code>cell</code>的组成需要 <code>modal</code>找到数据，也需要 <code>layout</code>找到这个 <code>cell</code>如何布局：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6760ebc1ceb477ba7ed85fcd5be62c3~tplv-k3u1fbpfcp-watermark.image" alt="未命名文件(41).png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>
<h5 data-id="heading-9">预解码 & 预渲染</h5>
图片的渲染流程，在 <code>CPU</code>阶段拿到图片的顶点数据和纹理之后会进行解码生产位图，然后传递到 <code>GPU</code>进行渲染主要流程图如下
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa30d5f4478b4a41a23be58265de9a02~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如果图片很多很大的情况下解码工作就会占用主线程 <code>RunLoop</code>导致其他工作无法执行比如滑动，这样就会造成卡顿现象，所以这里就可以将解码的工作放到异步线程中不占用主线程，可能有人会想只要将图片加载放到异步线程中在异步线程中生成一个 <code>UIImage</code>或者是 <code>CGImage</code>然后再主线程中设置给 <code>UIImageView</code>,此时可以写段代码使用 <code>instruments</code>的 <code>Time Profiler</code>查看一下堆栈信息
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4feda961c714e58a0d25aed49237d07~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
发现图片的编解码还是在主线程。
针对这种问题常见的做法是在子线程中先将图片绘制到<code>CGBitmapContext</code>，然后从<code>Bitmap</code> 直接创建图片，例如<code>SDWebImage</code>三方框架中对图片编解码的处理。这就是<code>Image</code>的预解码，代码如下：
<pre><code class="copyable">    dispatch_async(queue, ^&#123;
     CGImageRef cgImage = [UIImage imageWithData:[NSData dataWithContentsOfURL:[NSURL URLWithString:self]]].CGImage;
     CGImageAlphaInfo alphaInfo = CGImageGetAlphaInfo(cgImage) & kCGBitmapAlphaInfoMask;

     BOOL hasAlpha = NO;
     if (alphaInfo == kCGImageAlphaPremultipliedLast ||
         alphaInfo == kCGImageAlphaPremultipliedFirst ||
         alphaInfo == kCGImageAlphaLast ||
         alphaInfo == kCGImageAlphaFirst) &#123;
         hasAlpha = YES;
     &#125;

     CGBitmapInfo bitmapInfo = kCGBitmapByteOrder32Host;
     bitmapInfo |= hasAlpha ? kCGImageAlphaPremultipliedFirst : kCGImageAlphaNoneSkipFirst;

     size_t width = CGImageGetWidth(cgImage);
     size_t height = CGImageGetHeight(cgImage);

     CGContextRef context = CGBitmapContextCreate(NULL, width, height, 8, 0, CGColorSpaceCreateDeviceRGB(), bitmapInfo);
     CGContextDrawImage(context, CGRectMake(0, 0, width, height), cgImage);
     cgImage = CGBitmapContextCreateImage(context);

     UIImage * image = [[UIImage imageWithCGImage:cgImage] cornerRadius:width * 0.5];
     CGContextRelease(context);
     CGImageRelease(cgImage);
     completion(image);
 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h5 data-id="heading-10">按需加载</h5>
顾名思义需要显示的加载出来，不需要显示的加载，例如 <code>TableView</code>中的图片滑动的时候不加载，在滑动停止的时候加载（可以使用<code>Runloop</code>，图片绘制设置 <code>defaultModal</code>就行）</li>
<li>
<h5 data-id="heading-11">异步渲染</h5>
再说异步渲染之前先了解一下 <code>UIView</code>和 <code>CALayer</code>的关系：
<ol>
<li><code>UIView</code>是基于 <code>UIKit</code>框架的，能够接受点击事件，处理用户的触摸事件，并管理子视图</li>
<li><code>CALayer</code>是基于 <code>CoreAnimation</code>，而<code>CoreAnimation</code>是基于<code>QuartzCode</code>的。所以<code>CALayer</code>只负责显示，不能处理用户的触摸事件</li>
<li><code>UIView</code>是直接继承 <code>UIResponder</code>的，<code>CALayer</code>是继承 <code>NSObject</code>的</li>
<li><code>UIVIew</code> 的主要职责是负责接收并响应事件；而 <code>CALayer</code> 的主要职责是负责显示<code> UI</code>。<code>UIView</code> 依赖于 <code>CALayer</code> 得以显示</li>
</ol>
总结：<code>UIView</code>主要负责时间处理，<code>CALayer</code>主要是视图显示
异步渲染的原理其实也就是在子线程将所有的视图绘制成一张位图，然后回到主线程赋值给 <code>layer</code>的 <code>contents</code>,例如 <code>Graver</code>框架的异步渲染流程如下：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5bef1cc68fa415abd8562b19ceb866c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
核心源码如下：
<pre><code class="copyable">if (drawingFinished && targetDrawingCount == layer.drawingCount)
  &#123;
      CGImageRef CGImage = context ? CGBitmapContextCreateImage(context) : NULL;
      &#123;
          // 让 UIImage 进行内存管理
          // 最终生成的位图  
          UIImage *image = CGImage ? [UIImage imageWithCGImage:CGImage] : nil;
          void (^finishBlock)(void) = ^&#123;
              // 由于block可能在下一runloop执行，再进行一次检查
              if (targetDrawingCount != layer.drawingCount)
              &#123;
                  failedBlock();
                  return;
              &#125;
              //主线程中赋值完成显示
              layer.contents = (id)image.CGImage;
              // ...
          &#125;
          if (drawInBackground) dispatch_async(dispatch_get_main_queue(), finishBlock);
          else finishBlock();
      &#125;

      // 一些清理工作: release CGImageRef, Image context ending
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
最终效果图如下：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de74bf18024142949f0262be0e10646b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
也可以使用 <code>YYAsyncLayer</code>和</li>
<li>
<h5 data-id="heading-12">其他</h5>
<ol>
<li>减少图层的层级</li>
<li>减少离屏渲染</li>
<li>图片显示的话图片的大小设置（不要太大）</li>
<li>少使用<code>addView</code> 给<code>cell</code>动态添加<code>view</code></li>
<li>尽量避免使用透明<code>view</code>，因为使用透明<code>view</code>，会导致在<code>GPU</code>中计算像素时，会将透明<code>view</code>下层图层的像素也计算进来，即颜色混合处理（当有两个图层的时候一个是半透明一个是不透明如果半透明的层级更高的话此时就会触发颜色混合，底层的混合并不是仅仅的将两个图层叠加而是会将两股颜色混合计算出新的色值显示在屏幕中）</li>
</ol>
</li>
</ul>
</li>
</ul></div>  
</div>
            