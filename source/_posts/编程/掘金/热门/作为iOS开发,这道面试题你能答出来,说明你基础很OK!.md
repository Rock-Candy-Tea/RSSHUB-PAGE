
---
title: '作为iOS开发,这道面试题你能答出来,说明你基础很OK!'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://juejin.cn/post/undefined'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 02:39:17 GMT
thumbnail: 'https://juejin.cn/post/undefined'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>首先我们先来看一下这道面试题是啥?</p>
<p><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​题目看着非常简单,我是先创建了一个继承NSObject的GDPerson类;</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7d248db3ce34b99b689667de93c8439~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>GDPerson类的.h文件</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/425145f181914f209b9c75e15821de91~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>GDPerson类的.m文件</p>
<p>再看一下我们viewController.m里面的代码:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90e2f8439c6e4c1c85a6de2ba254ce97~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这是题目</p>
<p>请问:</p>
<p>1.print能不能调用成功?如果不能会怎么样?如果能的话调用结果是什么?</p>
<p>这个又是一个更扯的面试题,真正开发的时候,谁也不会这么写,这个还是主要考你基础!相信你看到这个题目之后应该心中已经有了答案,要不知道结果,要么可能知道结果,要么犹豫不决,要么不知道哈哈!</p>
<p>其实这个面试题考点比较多,考点如下:</p>
<p>1.你要了解super的本质,第一个参数要传结构体</p>
<p>2.函数的堆栈分配问题</p>
<p>3.消息机制,调用方法是怎么调用</p>
<p>4.访问成员变量的本质</p>
<p>这样,我们先来看一下调用结果吧!</p>
<p>请看结果:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/716faeb8b93244619d57e24b84d363e3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>面试题运用结果</p>
<p>这里跟你想的答案一样吗?</p>
<p>这样我在cls前面加一段代码,我们再看一下结果:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db1946a6c39a4ed8b4368cee66e486c1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>面试题运用结果</p>
<p>首先我们立刻会有2个疑问:</p>
<p>1.为什么能调用成功?</p>
<p>2.为什么self.name调用结果是viewController?</p>
<h2 data-id="heading-0">一.为什么能调用成功?</h2>
<p>[(<strong>__bridge</strong> <strong>id</strong>)obj print];由之前的学习,我们知道这个代码的本质是:给obj发一条print的消息,就会去通过obj的isa找到obj的类对象,去找方法列表,这个是非常清楚的.这个能调用成功,说明(<strong>__bridge</strong> <strong>id</strong>)obj也存在我们之前说的是isa指针这个东西</p>
<p>我画个图,这样理解的比较清楚.</p>
<p>cls是指向GDPerson,obj是指向cls,所以图如下:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ea15e563c06474d8e4183ba299737e6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>上面绿色是[GDPerson class],图比较模糊</p>
<p>再请看下面的代码:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b680c20c81541c0890ef55eb4514f53~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>person指向GDPerson的实例变量,而GDPerson的实例变量是包括isa和成员变量等等,这个也很清楚.而isa是指向GDPerson的类对象,所以请看下面的图:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af5c02a22e144d8b98c39ea44511a671~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>我们根据之前的源码分析知道,isa和_name是存在一个结构体,而对于结构体来说,第一个成员变量的地址值就是这个结构体的地址.所以person就是指向isa.</p>
<p>好了,这两个图我们分析清楚了以后,你看这两个图是不是很类似,几乎是一样的,我们再看下面的一个图:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8878cde70e284ef58301c03c530101d0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>上面绿色是[GDPerson class],图比较模糊</p>
<p>所以从上面的结构上,你看是不是就是一样的,obj就相当于person,所以能调用,这个比较抽象.说白了,你上面写的cls就是isa作用,因为我们知道指向类对象的指针就是isa.isa就是存储类对象的地址值.而你可能有疑问cls里面都没有_name怎么能算是GDPerson对象呢?注意,我们是调用print方法,调用方法没有说一定有_name成员变量!是这样吧!它是跟有没有成员变量是没有关系的.</p>
<p>第二个角度解释:obj怎么找到cls,就是通过cls对象的前8个字节的内存地址找到它,前8个字节也是结构体的地址,通过地址就能很容易找到class对象,是这样的.所以它能够调用成功!这就是调用的本质,后面那条线的调用也是如此.</p>
<h2 data-id="heading-1">二.为什么self.name调用结果是其他的?</h2>
<p>首先你要知道堆栈排列的知识点,请看下图:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84a5f76bb64a44d9983733e88aa75d2a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这些变量都是存在栈空间的,而且内存地址是由高地址到底地址.</p>
<p>好我们再看下面这个之前的图:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/463d574f512a46fea384c7165fc39514~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>我们画一下这些地址排列如下</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cb96f289b3145c8aa9c1612ce1e0ac0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>上面代码的结构示意图</p>
<p>上面绿色是[GDPerson class],图比较模糊,这个图很清楚.</p>
<p>现在我们来回忆一下:之前我们定义一个对象,比如上面的GDPerson这个类,它的底层生成的结构是下面这个样子的</p>
<p><strong>struct</strong>GDPerson_IMPL</p>
<p>&#123;</p>
<p>Class isa;</p>
<p>NSString *_name;</p>
<p>&#125;</p>
<p>上面这个结构体就是底层的结构,现在我们想一下,怎么找到_name这个地址,肯定是找到isa指针的地址加上8个字节就能找到_name吧?看下图</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/390dc54a4c9a4d93b653adbd76b15492~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这个应该是很明显,找name就是通过isa找到name对应的这块内存地址就行了.</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fd117e83dc5422e93b7b5e30d54ab2e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>现在大家知道下结果了吧?上面的cls就是我们的isa指针,所以找name就找到了test这里面!好我们再运行一下看看</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f4d8f49b27a42bcb2f739e8440345fa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这里你定义test,你定义任何其他的都是一样,都会找到cls前面声明的变量.比如我再定义一个objct再看下.</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c24c478e95041a9a1f766a3e8d4b7b0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>输出的结果就是cls上面最近的一个创建的.还有一个未解决就是self.name调用结果是viewController</p>
<h3 data-id="heading-2">三、为什么self.name调用结果是viewController?</h3>
<p>我们把test变量去掉,结果就会是viewController 我直接说了这个主要是[<strong>super</strong> viewDidLoad]影响;从上一张博客我们知道</p>
<p>super做了什么事它底层是这样实现的(上个博客说得很清楚): objc_msgSendSuper(&#123; <strong>self</strong>,[UIViewController Class]&#125; ,<strong>@selector</strong>(viewDidLoad));其他就是做了这件事**@selector**(viewDidLoad)也可以写出sel_registerName("viewDidLoad")</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef2768dabbd74145bfaa01e68ecbece7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这个肯定要开始定义一个局部的结构体才能传入 objc_msgSendSuper这个方法.所以最高地址是abc这个结构体,而结构体的第一个参数的地址就是结构体的地址,所以输出的就是self也就是viewController.</p>
<p>如下图:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00541882774447098a76c517349bad2f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>就会找到self</p>
<h2 data-id="heading-3">下面我们通过内存来证明一下这个东西:</h2>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47133bba9a8b4354b47bb84ba74205fb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这个题目涉及的知识点还是比较多,如果直接给你题目凭空想想,还是很难想出答案,好了,就说这么多了</p>
<h2 data-id="heading-4">接下来我会继续介绍runtime的实战应用,来继续学习runtime.</h2>
<h1 data-id="heading-5">如果觉得我写得对您有所帮助，请关注我，我会持续更新😄</h1></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            