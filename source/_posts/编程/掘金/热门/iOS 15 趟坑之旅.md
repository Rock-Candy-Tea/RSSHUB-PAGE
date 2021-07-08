
---
title: 'iOS 15 趟坑之旅'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=2355'
author: 掘金
comments: false
date: Fri, 25 Jun 2021 00:20:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=2355'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>本着苹果爸爸系统更新的一贯作风(UI必乱)，我开始了iOS15的探索；</p>
<p>基于Xcode Version 13.0 beta (13A5155e) iOS 15 beta2</p>
<h2 data-id="heading-1">NavigationBar颜色失效</h2>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">self.navigationController.navigationBar.barTintColor = [[RSLColorDarMode sharedInstance] colorProviderWithLightColor:[UIColor whiteColor] withDarColor:UIColorFromRGB(0x202020)];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>多么正常的代码，多么符合常理的操作，但是在iOS15的页面失效，不起作用；</p>
<p>无奈查找无果，便前去苹果论坛<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fforums%2Fthread%2F683265" title="https://developer.apple.com/forums/thread/683265" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">寻找答案</a>，果然功夫不负有心人让我找到了。</p>
<blockquote>
<p>As of iOS 15, UINavigationBar, UIToolbar, and UITabBar will use their scrollEdgeAppearance when your view controller's associated scroll view is at the appropriate edge (or always if you don't have a UIScrollView in your hierarchy, more on that below).</p>
</blockquote>
<p>从 iOS 15 开始，UINavigationBar、UIToolbar 和 UITabBar 将在您的视图控制器的关联滚动视图位于适当的边缘时使用它们的 scrollEdgeAppearance（或者总是如果您的层次结构中没有 UIScrollView，更多内容见下文）。</p>
<blockquote>
<p>You must adopt the UIBarAppearance APIs (available since iOS 13, specializations for each bar type) to customize this behavior. UIToolbar and UITabBar add scrollEdgeAppearance properties for this purpose in iOS 15.</p>
</blockquote>
<p>您必须采用 UIBarAppearance API（自 iOS 13 起可用，针对每种条形类型进行了专门化）来自定义此行为。 UIToolbar 和 UITabBar 为此在 iOS 15 中添加了 scrollEdgeAppearance 属性。</p>
<p>so，代码更改如下：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> if (@available(iOS 15.0, *)) &#123;
        UINavigationBarAppearance *navigationBarAppearance = [UINavigationBarAppearance new];
        navigationBarAppearance.backgroundColor = [[RSLColorDarMode sharedInstance] colorProviderWithLightColor:[UIColor whiteColor] withDarColor:UIColorFromRGB(0x202020)];
        self.navigationController.navigationBar.scrollEdgeAppearance = navigationBarAppearance;
        self.navigationController.navigationBar.standardAppearance = navigationBarAppearance;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">UITableView section增加默认高度</h2>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">/// Padding above each section header. The default value is `UITableViewAutomaticDimension`.
@property (nonatomic) CGFloat sectionHeaderTopPadding API_AVAILABLE(ios(15.0), tvos(15.0), watchos(8.0));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>UITableView又新增了一个新属性：sectionHeaderTopPadding 会给每一个section header 增加一个默认高度，当我们使用UITableViewStylePlain 初始化tableView的时候，就会发现系统默认给section header增高了22像素。</p>
<p>so, 代码更改如下：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">if (@available(iOS 15.0, *)) &#123;
    _tableView.sectionHeaderTopPadding = 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最好改在基类，一次解决所有问题；</p>
<p>目前发现的就是这两个问题，至于苹果爸爸后续会不会修复那鬼知道哦~</p>
<p>后续有新的会继续发出来，也欢迎大佬们留言讨论苹果爸爸的新坑~</p></div>  
</div>
            