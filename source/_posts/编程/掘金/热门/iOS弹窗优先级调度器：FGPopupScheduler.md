
---
title: 'iOS弹窗优先级调度器：FGPopupScheduler'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1562c1cc7fff4df88a5ad8e0a1a5044f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 21:47:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1562c1cc7fff4df88a5ad8e0a1a5044f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>GitHub 地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFoneG%2FFGPopupScheduler" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FoneG/FGPopupScheduler" ref="nofollow noopener noreferrer">FGPopupScheduler</a><br>
支持 cocopods，使用简便，效率不错的基础组件。</p>
<h4 data-id="heading-0">前言</h4>
<p>前些天测试反馈当新用户刚打开APP的时候，由于弹窗过多，再加上还有半透明的引导层，经常会出现多个弹窗互相覆盖，甚至阻断正常流程的情况。而需要解决这类问题，不单单要理清楚弹窗之间的依赖关系，还需要处理弹窗本身出现的条件。并且在每次有新的弹窗加入时都需要查看之前弹窗的逻辑。每一步都要耗费开发资源。</p>
<p>所以我们的目的就是为了解决多个弹窗，如何拆分各个弹窗间的依赖关系，并在恰当地时刻依次显示弹窗。</p>
<h4 data-id="heading-1">需求分析</h4>
<p>首先是弹窗本身的需求</p>
<ul>
<li>弹窗显示</li>
<li>弹窗隐藏</li>
<li>弹窗显示需要满足的条件</li>
</ul>
<p>然后是关于弹窗与弹窗</p>
<ul>
<li>弹窗的优先级</li>
<li>弹窗是否会受到已显示弹窗的影响</li>
</ul>
<p>弹窗显示有一个特征，就是同一个时刻只会显示一个弹窗，并且可以是一个接一个显示。如果采用采用队列来管理的话，理所当然地就需要额外处理插入、删除、清空、遍历等行为。</p>
<p>这一套流程下来貌似就解决了，但实际上当把所有弹窗的统一交给一个调度器来管理的话，我们必须要考虑在什么时机显示/隐藏这些弹窗才是更加合理的。</p>
<p>当然，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFoneG%2FFGPopupScheduler" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FoneG/FGPopupScheduler" ref="nofollow noopener noreferrer">FGPopupScheduler</a>   就能帮忙处理上面这些琐碎的事情，而且不止于此。</p>
<h4 data-id="heading-2">实现分析</h4>
<p>考虑到弹窗本身的多样性，甚至可能不是View。所以采用协议将弹窗的逻辑抽象处理放到<code><FGPopupView></code>中，只要遵守了协议将能作为就能被调度器统一管理。</p>
<pre><code class="copyable">@protocol FGPopupView <NSObject>

@optional
/*
 FGPopupSchedulerStrategyQueue会根据 -showPopupView: 来监听显示逻辑，如果含有动画请实现-showPopupViewWithAnimation:方法
 */
- (void)showPopupView;

/*
 FGPopupSchedulerStrategyQueue会根据 -dismissPopupView: 来监听隐藏逻辑，如果含有动画请实现-showPopupViewWithAnimation:方法
 */
- (void)dismissPopupView;

/*
 FGPopupSchedulerStrategyQueue会根据 -showPopupViewWithAnimation: 来监听显示逻辑
 */
- (void)showPopupViewWithAnimation:(FGPopupViewAnimationBlock)block;

/*
 FGPopupSchedulerStrategyQueue会根据 -dismissPopupView: 来监听隐藏逻辑，如果含有动画请实现-dismissPopupViewWithAnimation:方法
 */
- (void)dismissPopupViewWithAnimation:(FGPopupViewAnimationBlock)block;

/**
 FGPopupSchedulerStrategyQueue会根据-canRegisterFirstPopupView判断，当队列顺序轮到它的时候是否能够成为响应的第一个优先级PopupView。默认为YES
 */
- (BOOL)canRegisterFirstPopupViewResponder;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于弹窗显示的顺序和优先级，实际操作中还会涉及到中途插入或者移除的操作，数据结构更类似于链表，所以这里采用了C++的STL标准库：list。</p>
<p>具体的策略如下</p>
<pre><code class="copyable">typedef NS_ENUM(NSUInteger, FGPopupSchedulerStrategy) &#123;
    FGPopupSchedulerStrategyFIFO = 1 << 0,           //先进先出
    FGPopupSchedulerStrategyLIFO = 1 << 1,           //后进先出
    FGPopupSchedulerStrategyPriority = 1 << 2        //优先级调度
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上使用者还可以结合 <code>FGPopupSchedulerStrategyPriority | FGPopupSchedulerStrategyFIFO</code> 一起使用，来处理当选择优先级策略时，如何决定同一优先级弹窗的排序。</p>
<p>通过<code>hitTest</code>来解决弹窗显示条件的需求，如果根据当前的命中的弹窗没有通过<code>hitTest</code>，则会根据选择的调度器策略，在当前的list中获取下一个弹窗进行测试。</p>
<pre><code class="copyable">- (PopupElement *)hitTestFirstPopupResponder&#123;
    list<PopupElement*>::iterator itor = _list.begin();
    PopupElement *element;
    do &#123;
        PopupElement *temp = *itor;
        id<FGPopupView> data = temp.data;
        __block BOOL canRegisterFirstPopupViewResponder = YES;
        if ([data respondsToSelector:@selector(canRegisterFirstPopupViewResponder)]) &#123;
            dispatch_sync_main_safe(^()&#123;
                canRegisterFirstPopupViewResponder = [data canRegisterFirstPopupViewResponder];
            &#125;);
        &#125;
        if (canRegisterFirstPopupViewResponder) &#123;
            element = temp;
            break;
        &#125;
        itor++;
    &#125; while (itor!=_list.end());
    return element;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于通过<code>FGPopupScheduler</code>来统一管理所以的弹窗，所以弹窗上面时候触发就需要组件自己来处理。这个笔者一共考虑了3个触发情况</p>
<ul>
<li>添加弹窗对象的时候</li>
<li>通过Runloop监听主线程空闲的时刻</li>
<li>用户主动触发</li>
</ul>
<p>通过上面3种情况，差不多已经能覆盖所有的使用场景。</p>
<p>另外，还给调度器添加了<code>suspended</code>状态，来主动挂起/恢复弹窗队列，用来控制当前调度器是否能触发<code>hitTest</code>进而展示的逻辑。</p>
<p>此外组件支持线程安全。考虑到操作的时机可能在任意线程，<del>组件通过<code>pthread_mutex_t</code>来保证线程安全</del>。值得注意的是，弹窗的显示过程会切换到主线程进行，所以不需要去额外处理了。
<code>pthread_mutex_t</code>虽然可以保证资源不会被同时占用，但必须保证上锁和解锁都在同一个线程。所以组件最后采用了信号量来替代互斥锁做线程保护。</p>
<p>至此，整个组件的业务是比较清晰了。FGPopupScheduler采用了状态模式，
组件需要让这三种处理方式可以自由的变动，所以采用策略模式来处理，下面是 UML 类图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1562c1cc7fff4df88a5ad8e0a1a5044f~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            