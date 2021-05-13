
---
title: 'iOS 实现渐变色的导航栏'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64ec1a3f14b64bc8b04d0e7ca1f6ddad~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 09 May 2021 21:48:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64ec1a3f14b64bc8b04d0e7ca1f6ddad~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>效果图</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64ec1a3f14b64bc8b04d0e7ca1f6ddad~tplv-k3u1fbpfcp-zoom-1.image" alt="渐变色" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Demo访问地址(<a href="https://github.com/HuangHaiPo/HPNavigationBarGradient.git" target="_blank" rel="nofollow noopener noreferrer">github.com/HuangHaiPo/…</a>)</p>
<ul>
<li>
<p>直接在navigationBar上添加一个渐变色View会导致遮盖导航上的标题和按钮，所以直接把渐变色view转换为图片设置为导航栏的背景图片，可以很方便解决上面的问题。</p>
</li>
<li>
<p>主要流程是在UIView上添加渐变色，然后把渐变色视图转变为图片，然后添加为NavigationBar的背景图片即可。</p>
</li>
</ul>
<h5 data-id="heading-0">渐变色</h5>
<p>渐变色使用的<code>CAGradientLayer</code>绘制，主要属性有开始渐变的位置和结束渐变的位置，用来控制颜色渐变的方向.方向是由起始坐标<code>(startPoint)</code>指向结束坐标<code>(endPoint)</code></p>
<pre><code class="copyable"> // gradient
    CAGradientLayer *gradientLayer = [CAGradientLayer layer];
    gradientLayer.frame = self.bounds;
    gradientLayer.startPoint = CGPointMake(0.1, 0.1);
    gradientLayer.endPoint = CGPointMake(1, 0.5);
    gradientLayer.colors = @[(__bridge id)[UIColor hexColorFromString:@"#00ADDE"].CGColor,
                             (__bridge id)[UIColor hexColorFromString:@"#00B8D6"].CGColor,
                             (__bridge id)[UIColor hexColorFromString:@"#00CAC9"].CGColor,
                             (__bridge id)[UIColor hexColorFromString:@"#00D6C1"].CGColor,
                             (__bridge id)[UIColor hexColorFromString:@"#00E0B8"].CGColor
    ];
    gradientLayer.locations = @[@(0), @(0.24f), @(0.48f), @(0.6f), @(0.85f)];
    self.layer.shadowColor = [UIColor colorWithRed:70/255.0 green:199/255.0 blue:200/255.0 alpha:0.5].CGColor;
    self.layer.shadowOffset = CGSizeMake(0,3);
    self.layer.shadowOpacity = 1;
    self.layer.shadowRadius = 9;
    [self.layer insertSublayer:gradientLayer atIndex:0];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a25486fe05aa46949824235083710d45~tplv-k3u1fbpfcp-zoom-1.image" alt="起始和结束坐标说明" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>左上角开始到右边中间结束</li>
</ul>
<pre><code class="copyable"> gradientLayer.startPoint = CGPointMake(0.1, 0.1);
 gradientLayer.endPoint = CGPointMake(1, 0.5);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>colors<code>(数组)</code>设置渐变色颜色组，CGColor类型。</li>
<li>locations<code>(数组)</code>可为空，用来控制颜色占比和颜色组中的颜色显示的位置的，传NSnumber类型的数字 0 ~ 1，正常来说是和<code>colors</code>数组对应的。</li>
</ul>
<pre><code class="copyable"> gradientLayer.colors = @[(__bridge id)[UIColor hexColorFromString:@"#00ADDE"].CGColor,
                             (__bridge id)[UIColor hexColorFromString:@"#00B8D6"].CGColor,
                             (__bridge id)[UIColor hexColorFromString:@"#00CAC9"].CGColor,
                             (__bridge id)[UIColor hexColorFromString:@"#00D6C1"].CGColor,
                             (__bridge id)[UIColor hexColorFromString:@"#00E0B8"].CGColor
    ];
gradientLayer.locations = @[@(0), @(0.24f), @(0.48f), @(0.6f), @(0.85f)];
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-1">设置渐变色导航栏</h5>
<p>渐变色视图画好后，我们只需要直接添加到导航控制器的navigationBar上即可。或者直接新建一个继承自<code>UINavigationController</code>的类，直接在上面添加如下。</p>
<pre><code class="copyable">/// 直接在self添加渐变视图会遮盖子视图 所有转换为图片 添加为背景图
[self.navigationBar setBackgroundImage:[UIImage convertViewToImage:[[HPNavigationBar alloc]initWithFrame:CGRectMake(0, -STATUS_BAR_HEIGHT, MN_WIDTH, NAVIGATION_HRIGHT)]] forBarMetrics:UIBarMetricsDefault];
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>视图转换为图片方法</li>
</ul>
<pre><code class="copyable">+ (UIImage *)convertViewToImage:(UIView *)view&#123;
    CGSize size = view.bounds.size;
    /**
     * size: 表示区域大小
     * opaque: 是否透明, NO - 半透明, YES - 非透明
     * scale: 屏幕密度(几倍像素)
     */
    UIGraphicsBeginImageContextWithOptions(size, NO, [UIScreen mainScreen].scale);
    [view.layer renderInContext:UIGraphicsGetCurrentContext()];
    UIImage *image = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    return image;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>修改导航按钮颜色和字体大小</li>
</ul>
<pre><code class="copyable">UIBarButtonItem *bedNumItem = [[UIBarButtonItem alloc]initWithTitle:@"001床" style:UIBarButtonItemStylePlain target:self action:@selector(back)];
bedNumItem.tintColor = [UIColor whiteColor];
NSMutableDictionary *attributs = [NSMutableDictionary dictionary];
attributs[NSForegroundColorAttributeName] = [UIColor whiteColor];
attributs[NSFontAttributeName] = MNFontSize(14);
[bedNumItem setTitleTextAttributes:attributs forState:UIControlStateNormal];
self.navigationItem.rightBarButtonItem = bedNumItem;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            