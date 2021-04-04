
---
title: '深入理解isKindOfClass、isMemberOfClass、synthesize、dynamic区别'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21de3a6476294261b70b0a7f2a9d7c15~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Apr 2021 00:49:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21de3a6476294261b70b0a7f2a9d7c15~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、isKindOfClass、isMemberOfClass区别</h3>
<p>跟大家分享一道关于isKindOfClass和isMemberOfClass的面试题,也是比较常见的面试题,请看下面的代码:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21de3a6476294261b70b0a7f2a9d7c15~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>请问当前控制台的打印是多少?这些题目看着特别的扯淡,为什么呢?首先我们在现实开发中绝对不会这么去写,也不会这么去判断,这也是主考官想知道你对这个知识点是否了解.这里也是考察我们对类对象,元类对象对使用isKindOfClass和isMemberOfClass的使用情况.</p>
<p>首先我们先创一个建命令行的项目,因为isKindOfClass和isMemberOfClass是开源的,我们可以直接去objc源码查看(<a href="https://opensource.apple.com/tarballs/" target="_blank" rel="nofollow noopener noreferrer">源码下载地址</a>)请看下图:(一般是在NSObject.mm文件里面查找,也可以直接搜索)</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9874992fcee647bf8b129096cef12f44~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>源码一看就非常清晰</p>
<p>- (<strong>BOOL</strong>)isMemberOfClass: 是判断当前对象的class,是不是就是传入的cls;</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a55bbf86628f4bcabc728136924fee57~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这个是调用- (<strong>BOOL</strong>)isMemberOfClass这个方法,所以上面的结果应该是很清晰,因为person的isMemberOfClass就是GDPerson</p>
<p>剩余的我就直接解释,不演示了,因为相对较简单</p>
<p>- (<strong>BOOL</strong>)isKindOfClass:(Class)cls:是判断当前对象的class,是不是传入的cls,或者当前对象的class是传入的cls的子类对象</p>
<p>+ (<strong>BOOL</strong>)isMemberOfClass: 是判断当前类对象的class,是不是就是传入的元类对象cls;</p>
<p>+ (<strong>BOOL</strong>)isKindOfClass:是判断当前类对象的class,是不是传入的元类对象cls,或者当前对象的mateclass是传入的元类对象cls的子类对象</p>
<p>有点绕,反正你就记住:-方法对应的是:对象和类对象 ; +方法对应的是:类和元类对象</p>
<p>所以 [[GDStudent class] isMemberOfClass:[GDStudent class]];这个是调用 +方法,左边是类对象没错,右边是元类对象一看就不是,所以是0</p>
<p>[[NSObject class] isMemberOfClass:[NSObject class]]:这个也是同样的道理,所以返回是0</p>
<p>[[GDStudent class] isKindOfClass:[GDStudent class]];这个右边也不是元类对象,所以返回是0</p>
<p>注意有个特殊的,你如果看过我之前的博客的一张图,还记得这张吗?<a href="https://www.jianshu.com/p/ce64c9429426" target="_blank" rel="nofollow noopener noreferrer">NSObject的isa和superclass区别</a></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29a877575c51419ca687e90ba0a15e2a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>注意上面的红色的箭头,当找不到元类对象的父类的时候,就会指向当前这个类,而root class很明显就是NSObject,</p>
<p>所以现在你来看这个[[NSObject class] isKindOfClass:[NSObject class]];所以这个返回的是YES</p>
<p>请看下面的运行结果:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f60d7e0fbaf424d91e12e57eb15513e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>结果很明显了</p>
<h2 data-id="heading-1">总结:</h2>
<p>- (<strong>BOOL</strong>)isMemberOfClass: 是判断当前对象的class,是不是就是传入的cls;</p>
<p>- (<strong>BOOL</strong>)isKindOfClass:(Class)cls:是判断当前对象的class,是不是传入的cls,或者当前对象的class是传入的cls的子类对象</p>
<p>+ (<strong>BOOL</strong>)isMemberOfClass: 是判断当前类对象的class,是不是就是传入的元类对象cls;</p>
<p>+ (<strong>BOOL</strong>)isKindOfClass:是判断当前类对象的class,是不是传入的元类对象cls,或者当前对象的mateclass是传入的元类对象cls的子类对象</p>
<h2 data-id="heading-2">二、@synthesize 、@dynamic的区别</h2>
<p>其实在开发中我们可能很少用到,但是面试的时候可能经常会问到这两个的区别,虽说不用,但是面试官要问,所以我们还是要了解一下这两个到底是干嘛的,到底有啥区别:</p>
<p>@synthesize: 修改变量名字,自动生成set和get并赋值.在以前的版本是没有自动生成set和get方法,往往定义一个变量,我们需要加这个东西,现在很少用,请看下面的代码:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f751df5e9ea848b0a2c541c7e96c7175~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f0d7478b68c4b3daf4a5b4dbc77502b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>所以没有问题.</p>
<p>@dynamic:提醒编译器不要自动生成setter和getter方法、不要自动生成成员变量</p>
<p>我们看下:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5aaae4bbfdb4d52958206d6b0189dd0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h2 data-id="heading-3">synthesize、dynamic总结</h2>
<p>1、@dynamic与@synthesize的区别@property有两个对应的词，一个是@synthesize，一个是@dynamic。如果@synthesize和@dynamic都没写，那么默认的就是@syntheszie var = _var; @synthesize的语义是如果你没有手动实现setter方法和getter方法，那么编译器会自动为你加上这两个方法。</p>
<p>@dynamic告诉编译器,属性的setter与getter方法由用户自己实现，不自动生成。（当然对于readonly的属性只需提供getter即可）。假如一个属性被声明为@dynamic var，然后你没有提供@setter方法和@getter方法，编译的时候没问题，但是当程序运行到instance.var =someVar，由于缺setter方法会导致程序崩溃；或者当运行到 someVar = var时，由于缺getter方法同样会导致崩溃。编译时没问题，运行时才执行相应的方法，这就是所谓的动态绑</p>
<h2 data-id="heading-4">介绍完这个面试题之后会再继续介绍runtime的其他知识点,来继续学习runtime</h2>
<h1 data-id="heading-5">如果觉得我写得对您有所帮助，请关注我，我会持续更新😄</h1></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            