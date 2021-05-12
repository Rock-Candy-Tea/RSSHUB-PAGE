
---
title: '【DoKit&北大专题】-DoKit For iOS视觉工具模块源码阅读'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe4ef576eefb4d70af842e72adbec235~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Apr 2021 00:09:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe4ef576eefb4d70af842e72adbec235~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">专题背景</h1>
<blockquote>
<p>近几年随着开源在国内的蓬勃发展，一些高校也开始探索让开源走进校园，让同学们在学生时期就感受到开源的魅力，这也是高校和国内的头部互联网企业共同尝试的全新教学模式。本专题会记录这段时间内学生们的学习成果。</p>
<p>更多专题背景参考:<a href="https://juejin.cn/post/6948247882172629005" target="_blank">【DoKit&北大专题】缘起</a></p>
</blockquote>
<h1 data-id="heading-1">系列文章</h1>
<p><a href="https://juejin.cn/post/6948247882172629005" target="_blank">【DoKit&北大专题】缘起</a></p>
<p><a href="https://juejin.cn/post/6948257290654842916" target="_blank">【DoKit&北大专题】-读小程序源代码（一）</a></p>
<p><a href="https://juejin.cn/post/6948300642767077412" target="_blank">【DoKit&北大专题】-读小程序源代码（二）</a></p>
<p><a href="https://juejin.cn/post/6955347254567764005/" target="_blank">【DoKit&北大专题】-读小程序源代码（三）</a></p>
<p><a href="https://juejin.cn/post/6955363977404612621/" target="_blank">【DoKit&北大专题】-实现DoKit For Web请求捕获工具（一）产品调研</a></p>
<p><a href="https://juejin.cn/post/6955767193929777182/" target="_blank">【DoKit&北大专题】-DoKit For 小程序源码分析</a></p>
<p><a href="https://juejin.cn/post/6956034588451799054/" target="_blank">【DoKit&北大专题】-浅谈滴滴DoKit业务代码零侵入思想（小程序端）</a></p>
<p><a href="https://juejin.cn/post/6956044954044989453/" target="_blank">【DoKit&北大专题】-滴滴DoKit For Web模块源码阅读</a></p>
<p><a href="https://juejin.cn/post/6956516714817273863/" target="_blank">【DoKit&北大专题】-滴滴DoKit For Web模块源码阅读（二）</a></p>
<p><strong><a href="https://juejin.cn/post/6956859493745426462/" target="_blank">【DoKit&北大专题】-DoKit For iOS视觉工具模块源码阅读</a></strong></p>
<h1 data-id="heading-2">原文</h1>
<p>本学期我选修了开源软件开发基础及实践这门课。虽然之前基本没有过泛前端项目的经验，但是为了扩充自己的技术栈与知识广度，选择了滴滴DoKit For iOS方向。由于我最终要完成的课程项目是做一个视觉工具插件，所以对视觉工具部分的代码进行了详细阅读与分析。</p>
<h2 data-id="heading-3">一、  DoKit项目简介</h2>
<p>DoraemonKit(简称Dokit) 诞生于滴滴城运服体验技术部,是一个功能齐备的泛终端研发百宝箱，能像哆啦A梦一样为他的主人提供各种各样的工具。自2018年项目发起以来，Dokit已经发展成为一个较为完整的生态，如DoKit For Android、DoKit For iOS、DoKit For 小程序、DoKit For Flutter、DoKit For Web等。目前DoKit在GitHub上该项目Unstar超过1.7万次，Fork超过2.5万次。Dokit在开源社区、BAT等互联网大厂和众多独角兽企业中有良好的声誉。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe4ef576eefb4d70af842e72adbec235~tplv-k3u1fbpfcp-zoom-1.image" alt="图形用户界面, 应用程序  描述已自动生成" loading="lazy" referrerpolicy="no-referrer">
<p>DoKit作为一个工具平台，能够让每个APP快速接入一些常用的或者没有实现的辅助开发工具、性能检测工具、测试工具、视觉辅助工具，还能在DoraemonKit面板中快速接入一些自己设计的一些非通用辅助工具。在开发测试APP时你可能需要进行帧率、CPU、内存等的监控，查看某一个模块的字体、位置、UI层次等信息，浏览、查找、删除APP下的文件……这些情境下DoKit都有了它的用武之地。</p>
<h2 data-id="heading-4">二、  DoKit For iOS模块简介</h2>
<p>DoKit的整个架构由公共和第三方、业务抽象类以及业务实现三部分组成。业务抽象类中主要有DoraemonCacheManager、DoraemonDBManager、DoraemonMockManager。公共和第三方主要是DoKit各个模块中会用到的一些工具，如地图、缓存、AFNetworking等。业务实现主要包括Mock Data、Health Check、File Sync等平台工具，App Info、Sanbox、Mock GPS等常用工具，FPS、CPU、Meomory、NetWork等性能检测工具和Color Picker、View Check、Align Ruler等视觉工具。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fd931c010ab4c8491857570eda16d08~tplv-k3u1fbpfcp-zoom-1.image" alt="image002" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在DoKit For iOS源码的Pods->Deveploment Pods->DoraemonKit->core中包含了Dokit项目的主要组成部分。Assets.xcassets中包含了项目中用到的icon和各种图片素材。Doraemon.string是一个中英文字符串对照表，包含了DoKit使用过程中大部分展示信息的中英文转换。在Plugin中有Common、Performance、Platform、UI等不同功能模块。而UI中则有ColorPick、Hierarchy、ViewAlign、Viewcheck、ViewMetrics这5个工具模块。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65ce250e924e4c59bcf2e6be5330d1b0~tplv-k3u1fbpfcp-zoom-1.image" alt="图片包含 表格  描述已自动生成" loading="lazy" referrerpolicy="no-referrer">
<p>通过Debug View Hierarchy可以看到UIWindowScene包含DoraemonHomeWindow、UIWindow、DoraemonEntryWindow和UITextEffectsWindow。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5caed290a8214d0380204dc9045c4787~tplv-k3u1fbpfcp-zoom-1.image" alt="图片包含 图示  描述已自动生成" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-5">三、  取色器工具源码分析</h2>
<p>选择DoKit面板中的Color Picker选项后，移动屏幕中出现的圆形放大镜，会吸取圆心所在元素的颜色值，并在可移动的窗口上显示该颜色值。点击窗口右边的关闭按钮，即可取消颜色吸管工作。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9843abf0cece44f8af3aac36eb5b8a0b~tplv-k3u1fbpfcp-zoom-1.image" alt="图形用户界面, 应用程序  描述已自动生成" loading="lazy" referrerpolicy="no-referrer">
<p>DoKit For iOS中DoraemonPickWindow中实现了图像放大器和颜色提取的功能，其中的[M]-colorAtPoint可以取出截图中单个点的颜色，在[M]-pan中会调用[M]-colorAtPoint将颜色信息传递给DoraemonColorPickInfoWindow。实现颜色提取的类DoraemonColorPickView已被弃用，现采用DoraemonColorPickMagnifyLayer。颜色提取工具的各模块关系如下图。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f105225ba4e4379a65106eb0ae0e0a9~tplv-k3u1fbpfcp-zoom-1.image" alt="图示  描述已自动生成" loading="lazy" referrerpolicy="no-referrer">
<p>在DoraemonColorPickWindow中的[P]magnifyLayer表示放大的图层，[P]screenShotImage是定位的图片，相当于视图的截屏。[M]-init会被[M]+shareInstance调用，初始化放大镜的位置在屏幕中央，并且设置self.windowLevel = UIWindowLevelStatusBar + 1.f，防止其被挡住。[M]updateScreenShotImage 会在每次调用[M]-pan时绘制截图，首先拿到一个相当于白版的context，然后拿到KeyWindow，把KeyWindow的图层渲染在白版上，再把context的内容导出成图像并把图像更新到self.screenShotImage。</p>
<p>实现在图片中取出某一点的颜色的方法是：1. 如果点超出图像范围，则退出; 2. 创建一个1x1像素字节数组和位图context来绘制像素;3. 将被取色图片绘制到context上并获得位图原数据；4. 找到取色点对应的像素（3个字节red，green，blue），获得RGB色即可。</p>
<p>在[M]-colorAtPoint方法中，如果图片不存在或者点在坐标范围之外，则返回nil。再通过点坐标创建一个1x1像素点pixelDataarray并用位图context来绘制像素。之后得到一个hexColor字符串，存储pixelData的RGB三通道信息。</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (NSString *)colorAtPoint:(CGPoint)point inImage:(UIImage *)image &#123;
    if (!image || !CGRectContainsPoint(CGRectMake(0.0f, 0.0f, image.size.width, image.size.height), point)) &#123;
        return nil;
    &#125;
    NSInteger pointX = trunc(point.x);
    NSInteger pointY = trunc(point.y);
    CGImageRef cgImage = image.CGImage;
    NSUInteger width = image.size.width;
    NSUInteger height = image.size.height;
    CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();
    int bytesPerPixel = 4;
    int bytesPerRow = bytesPerPixel * 1;
    NSUInteger bitsPerComponent = 8;
    unsigned char pixelData[4] = &#123; 0, 0, 0, 0 &#125;;
    CGContextRef context = CGBitmapContextCreate(pixelData,
                                                 1,
                                                 1,
                                                 bitsPerComponent,
                                                 bytesPerRow,
                                                 colorSpace,
                                                 kCGImageAlphaPremultipliedLast | kCGBitmapByteOrder32Big);
    CGColorSpaceRelease(colorSpace);
    CGContextSetBlendMode(context, kCGBlendModeCopy);
    
    CGContextTranslateCTM(context, -pointX, pointY-(CGFloat)height);
    CGContextDrawImage(context, CGRectMake(0.0f, 0.0f, (CGFloat)width, (CGFloat)height), cgImage);
    CGContextRelease(context);
    
    NSString *hexColor = [NSString stringWithFormat:@"#%02x%02x%02x",pixelData[0],pixelData[1],pixelData[2]];
    return hexColor;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>DoraemonColorPickWindow中的[M]-pan会在开始拖动的时候更新屏幕快照，并在获得拖动位移、清空拖动位移后重新设置控件位置。更新位置使self.magnifyLayer.targetPoint = centerPoint后会使magnifyLayer更新，通过调用[M]-colorAtPoin得到新的表示颜色的十六进制hexColor字符串传递给DoraemonColorPickInfoWindow。</p>
<pre><code class="hljs language-objc copyable" lang="objc"> <span class="hljs-built_in">CGPoint</span> centerPoint = <span class="hljs-built_in">CGPointMake</span>(newX, newY);
    panView.center = centerPoint;
    
    <span class="hljs-keyword">self</span>.magnifyLayer.targetPoint = centerPoint;
    <span class="hljs-built_in">CGRect</span> magnifyFrame     = <span class="hljs-keyword">self</span>.magnifyLayer.frame;
    magnifyFrame.origin     = <span class="hljs-built_in">CGPointMake</span>(round(magnifyFrame.origin.x), round(magnifyFrame.origin.y));
    <span class="hljs-keyword">self</span>.magnifyLayer.frame = magnifyFrame;
    [<span class="hljs-keyword">self</span>.magnifyLayer setNeedsDisplay];
    
    [<span class="hljs-built_in">CATransaction</span> commit];
    
    <span class="hljs-built_in">NSString</span> *hexColor = [<span class="hljs-keyword">self</span> colorAtPoint:centerPoint];
    [[DoraemonColorPickInfoWindow shareInstance] setCurrentColor:hexColor];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>DoraemonColorPickMagnifyLayer设置了放大镜尺寸、放大镜边缘厚度、放大镜网格的数量、采集像素颜色时像素的间隔（kPixelSkip = 1）。[M]-drawInContext会对放大镜进行网格裁剪画出网格(网格数量15，放大镜尺寸150)。[M]-drawGridContext中首先会由于锚点修改对currentPoint进行偏移。之后进行两轮循环，在放大镜中画出网格，并使用当前点和周围点的颜色进行填充。循环时会横向寻找下一个相邻点，一行绘制完毕，横向回归起始点，纵向寻找下一个点。[M]-magnifyImage实现绘制裁剪区域、放大镜边缘、放大镜的两条边缘线之间的内容和中心的选择区域等。[M]-gridCirclePath实现对正方形进行裁剪绘制圆形放大镜。</p>
<h2 data-id="heading-6">四、   组件检查工具源码分析</h2>
<p>点击DoKit面板中的View Check进行组件检查，再移动屏幕中出现的红芯圆，可获取圆心所在组件的各种组件规格值，包括控件名称、控件位置、字体颜色、字体大小等。信息会显示在屏幕下方的窗口中。点击窗口右上方的关按钮，即可取消View Check工作。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/691d7b717e2647c3bc630df513bf639e~tplv-k3u1fbpfcp-zoom-1.image" alt="图表  中度可信度描述已自动生成" loading="lazy" referrerpolicy="no-referrer">
<p>View Check中DoraemonViewCheckPlugin调用DoraemonViewCheckManager，而DoraemonViewAlignManager则持有DoraemonViewCheckView。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcc5d27058b241f7b25c90dfe0a75568~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<p>DoraemonViewCheckView中[M]-hexFromUIColor的作用是将UIColor转化为十六进制颜色的字符串，分为color不存在、color = [UIColor clearColor]、单色色彩、和可带透明度的RGB三通道色四种情况。[M]-nameWithInstance通过class_copyIvarList来获取实例的名字，这个方法在[M]- viewInfo获取属性名时会被使用到。[M]-needRefresh用于判断oldView是否存在和oldView与view是否相等。[M]-hitView的作用是来获取处于顶部的view。首先判断自身能否接收事件和点在不在自身上，判断为否则返回nil。之后遍历自己的子控件,把事件传递给子控件,调用子控件的hitTest。循环获取子控件时，要把当前点的坐标系转换成子控件的坐标系。[M]-topview则是在hitTest基础上，在顶部的view周围加上一个边框。</p>
<p>hitTest方法的原理是用户触摸屏幕进行交互时，系统会将触摸以UIEvent的方式加入到UIApplication事件队列中，Upplication从事件队列中取出队首的触摸事件交给UIWindow进行处理，UIWindow会进行hitTest寻找到触摸点的视图。hitTest方法中，在RootView上调用PointInside方法判断触摸点是否在当前视图内，如果返回No,则hitTest返回nil。否则向所有子视图发送hitTest，直到所有子视图返回非空对象或者全部子视图遍历完毕。</p>
<pre><code class="hljs language-objc copyable" lang="objc">-(<span class="hljs-built_in">UIView</span>*)topView:(<span class="hljs-built_in">UIView</span>*)view Point:(<span class="hljs-built_in">CGPoint</span>) point&#123;
    [_arrViewHit removeAllObjects];
    [<span class="hljs-keyword">self</span> hitTest:view Point:point];
    <span class="hljs-built_in">UIView</span> *viewTop=[_arrViewHit lastObject];
    [_arrViewHit removeAllObjects];
    <span class="hljs-keyword">return</span> viewTop;
&#125;


-(<span class="hljs-keyword">void</span>)hitTest:(<span class="hljs-built_in">UIView</span>*)view Point:(<span class="hljs-built_in">CGPoint</span>) point&#123;
    <span class="hljs-keyword">if</span>([view isKindOfClass:[<span class="hljs-built_in">UIScrollView</span> <span class="hljs-keyword">class</span>]])
    &#123;
        point.x+=((<span class="hljs-built_in">UIScrollView</span>*)view).contentOffset.x;
        point.y+=((<span class="hljs-built_in">UIScrollView</span>*)view).contentOffset.y;
    &#125;
    <span class="hljs-keyword">if</span> ([view pointInside:point withEvent:<span class="hljs-literal">nil</span>] &&
        (!view.hidden) &&
        (view.alpha >= <span class="hljs-number">0.01</span>f) && (view!=_viewBound) && ![view isDescendantOfView:<span class="hljs-keyword">self</span>]) &#123;
        [_arrViewHit addObject:view];
        <span class="hljs-keyword">for</span> (<span class="hljs-built_in">UIView</span> *subView <span class="hljs-keyword">in</span> view.subviews) &#123;
            <span class="hljs-built_in">CGPoint</span> subPoint = <span class="hljs-built_in">CGPointMake</span>(point.x - subView.frame.origin.x,
                                           point.y - subView.frame.origin.y);
            [<span class="hljs-keyword">self</span> hitTest:subView Point:subPoint];
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>DoraemonViewCheckManager 中[M]- observeValueForKeyPath的作用是监听对象属性变更，变更时则处理事件，把viewCheckView放在最前面。DoraemonViewCheckView中[P]viewBound是当前需要探测的view的边框，[P]infoWindow是顶部被探测到的view中信息显示的UIwindow。[M]-init中初始化探测位置为屏幕中央，并设置好infoWindow。[M]-touchesBegandun、[M]-touchesMoved、[M]-touchesCancelled、[M]-touchesEnded的作用与平移检测器[M]-pan拖动位移获取控件信息的作用类似，可改变self.frame，并调用[M]-needRefresh来更新infoWindow。更新infoView使用[M]-viewInfo，在获得属性名后修改信息窗口中的控件名称、控件位置、背景颜色、字体颜色、字体大小等信息。</p>
<h2 data-id="heading-7">五、    对齐尺寸工具源码分析</h2>
<p>DoKit For IOS中的Align Ruler工具能够实时捕获屏幕坐标，查看组件是否对齐。进入到Align Ruler选项之后，移动屏幕中的红芯圆，可以获取到圆心所在位置相对于屏幕周围上下左右的距离，四个方向线中部以及屏幕下方窗口内会显示圆心到屏幕每一边的距离。点击下方窗口的关闭按钮，可取消尺寸对齐。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed3c56c6025442c99c1560b20fd5b467~tplv-k3u1fbpfcp-zoom-1.image" alt="日程表  描述已自动生成" loading="lazy" referrerpolicy="no-referrer">
<p>Align Ruler中DoraemonViewAlignPlugin调用DoraemonViewAlignManager，而DoraemonViewAlignManager持有DoraemonViewAlignView。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20b872133a5241eb9dd0f2223dc9cfff~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<p>DoraemonViewAlignManager中的[P]alignView持有2个UIView，1个UIImageView,4个UILabel,1个infoWindow，管理其显示和隐藏等。[M]-init会监听rootViewController被更改的事件，目标是把其持有的alignView提到最前面,同时也会监听被关闭的事件。[M]-dealloch会防止内存泄漏。[M]-0bserveValueForKeyPath会把alignView放到最前面。</p>
<p>DoraemonViewAlignView中的[P]imageView是中部红芯圆，[P]horizontalLine和[P]verticalLine分别是水平线和垂直线。[P]leftLabel、[P]rightLabel、[P]topLabe和[P]bottomLabel 分别是位于线中部左右上下四个位置标签。[P]infoWindow是屏幕下方信息窗口。[M]-init会将alignView扩展到全屏，设置背景色为透明。同时由于与低值层相比，高值层在视觉上更接近查看者，设置self.layer.zPosition = FLT_MAX，这样zPosition放在最高的位置，可防止alignView被遮挡。之后通过DoraemonScreenWidth和kViewCheckSize得到矩形的左上角两个坐标及宽高，再加载imageView圆圈，使_imageView = imageView。这样就可以进行用户事件监听和用户手势监听。初始化横线和高度后调用[selfbringSubviewToFront:_imageView]，则再次将imageView提前，防止被挡住。</p>
<pre><code class="hljs language-objc copyable" lang="objc">-(<span class="hljs-keyword">instancetype</span>)init&#123;
    <span class="hljs-keyword">self</span> = [<span class="hljs-keyword">super</span> init];
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">self</span>) &#123;
        <span class="hljs-keyword">self</span>.frame = <span class="hljs-built_in">CGRectMake</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, DoraemonScreenWidth, DoraemonScreenHeight);
        <span class="hljs-keyword">self</span>.backgroundColor = [<span class="hljs-built_in">UIColor</span> clearColor];
        <span class="hljs-keyword">self</span>.layer.zPosition = FLT_MAX;
        <span class="hljs-built_in">UIImageView</span> *imageView = [[<span class="hljs-built_in">UIImageView</span> alloc] initWithFrame:<span class="hljs-built_in">CGRectMake</span>(DoraemonScreenWidth/<span class="hljs-number">2</span>-kViewCheckSize/<span class="hljs-number">2</span>, DoraemonScreenHeight/<span class="hljs-number">2</span>-kViewCheckSize/<span class="hljs-number">2</span>, kViewCheckSize, kViewCheckSize)];
        imageView.image = [<span class="hljs-built_in">UIImage</span> doraemon_xcassetImageNamed:<span class="hljs-string">@"doraemon_visual"</span>];
        [<span class="hljs-keyword">self</span> addSubview:imageView];
        _imageView = imageView;
        imageView.userInteractionEnabled = <span class="hljs-literal">YES</span>;
        <span class="hljs-built_in">UIPanGestureRecognizer</span> *pan = [[<span class="hljs-built_in">UIPanGestureRecognizer</span> alloc] initWithTarget:<span class="hljs-keyword">self</span> action:<span class="hljs-keyword">@selector</span>(pan:)];
        [imageView addGestureRecognizer:pan];
        _horizontalLine = [[<span class="hljs-built_in">UIView</span> alloc] initWithFrame:<span class="hljs-built_in">CGRectMake</span>(<span class="hljs-number">0</span>, imageView.doraemon_centerY<span class="hljs-number">-0.25</span>, <span class="hljs-keyword">self</span>.doraemon_width, <span class="hljs-number">0.5</span>)];
        _horizontalLine.backgroundColor = [<span class="hljs-built_in">UIColor</span> doraemon_colorWithHexString:ALIGN_COLOR];
        [<span class="hljs-keyword">self</span> addSubview:_horizontalLine];
        _verticalLine = [[<span class="hljs-built_in">UIView</span> alloc] initWithFrame:<span class="hljs-built_in">CGRectMake</span>(imageView.doraemon_centerX<span class="hljs-number">-0.25</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.5</span>, <span class="hljs-keyword">self</span>.doraemon_height)];
        _verticalLine.backgroundColor = [<span class="hljs-built_in">UIColor</span> doraemon_colorWithHexString:ALIGN_COLOR];
        [<span class="hljs-keyword">self</span> addSubview:_verticalLine];
        [<span class="hljs-keyword">self</span> bringSubviewToFront:_imageView];
        
<span class="copy-code-btn">复制代码</span></code></pre>
<p>[M]-init之后还会进行标签初始化，设置4个label的字体、颜色、文字、大小、位置等信息。之后在进行infroWindow的设置时将其放在最下方，需要设置好其位置放在屏幕底部“黑杠”，防止被遮挡。[M]-pan控制控件的平移拖动。在获得拖动位移后清空拖动位移，再重新设置空间位置。得到中心点之后，可以调整horizontalLine和verticalLine的位置，更新4个位置标签的信息，最后在[M]-pan中调用[M]-configInfoLblText，更新inforWindow中显示的信息。</p>
<h2 data-id="heading-8">六、    元素边框线工具源码分析</h2>
<p>点击DoKit面板上的View Border选项，再打开View border switch开关。跳转到任意想要查看的页面，可以看到页面内每一个元素的边框都会绘制出来，并且每一个边框的颜色都不一样。这样看上起非常直观，对组件布局的设局有一定的参考意义。再次回到View Border选项关闭View border switch开关即可关闭元素边框线功能。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc3e11aa1b4e410ab509abe8675d1680~tplv-k3u1fbpfcp-zoom-1.image" alt="图形用户界面, 应用程序, 表格  描述已自动生成" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f0963b910464ebaa09058ba5ed3ea81~tplv-k3u1fbpfcp-zoom-1.image" alt="手机屏幕的截图  描述已自动生成" loading="lazy" referrerpolicy="no-referrer">
<p>View Border中的模块关系如上图所示。DoraemonViewMetricsPlugin中[M]-pluginDidLoad会初始化一个DoraemonMetricsViewController，在将其替换为DoraemonHomeWindow的根ViewController。而DoraemonMetricsViewController中的[P] switchView是一个开关，[M]-viewDidLoad则用来设置开关的布局。在DoraemonViewMetricsConfig中定义了[M]+defaultConfig、[M]-init和[M]-setEnable。</p>
<p>UIView+DoraemonViewMetrics中的重写的[M]-setMetricsBorderLayert采用键值对关联一个对象（setAssociatedObject），key为@selector(metricsBorderLayer)，value是metricsBorderLayer。[M]-doraemonMetricsRecursiveEnable中调用了[M]-setMetricsBorderLayert。首先设定状态栏不显示元素边框。再采用深度优先搜索，在每一个UIView的subView中调用[M]-doraemonMetricsRecursiveEnable。之后，如果在defaultConfig中设定了borderColor则采用borderColor，如果未采用则将边框颜色设定为随机色。if(!self.metricsBorderLayer)语句中设置了一个闭包，用于初始化一个Layer,并把它加入到视图里，之后再设定图层的位置和范围。</p>
<h2 data-id="heading-9">七、    总结</h2>
<p>虽然之前有过阅读和分析开源项目代码的经历，但是读iOS开发的代码还是第一次。我在阅读了DoKit For iOS项目视觉工具部分的颜色吸管、组件检查、尺寸对齐、元素边框线四部分源码后，主要有三点收获。一是学会了一些iOS源码分析方法，如Debug View Hierachy、Find Call Hierarchy、断点 + control + step into 跟踪方式等。二是学习了一些视觉工具中常用的方法，如提取某一区域或某一点的颜色、防止view被遮挡、通过hitTest获得想要的view等。三是体会到了整个项目中模块之间相互解耦，各自完成独立的功能的设计思想。这使得项目有很好的扩展性，在掌握了项目总体框架后可定位到自己感兴趣的部分进行分析，也易于项目新功能的开发与引入。</p>
<h1 data-id="heading-10">作者信息</h1>
<p>作者：<a href="https://juejin.cn/user/35633801475630" target="_blank">astralibertas</a></p>
<p>原文链接：<a href="https://juejin.cn/post/6956828413667573773/" target="_blank">juejin.cn/post/695682…</a></p>
<p>来源：掘金</p></div>  
</div>
            