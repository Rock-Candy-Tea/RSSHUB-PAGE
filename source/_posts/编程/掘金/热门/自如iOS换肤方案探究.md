
---
title: '自如iOS换肤方案探究'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fd9019d03fa46278480fca73c385951~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 30 May 2021 18:16:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fd9019d03fa46278480fca73c385951~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言：</h2>
<p>往往到了重大的节假日，例如圣诞节、春节等，各大APP都会进行换肤，烘托喜庆的气氛。购物类APP在618或者双11的时候也会去换上自己的特色服装，找了几个APP分析了一下，大致有以下3种：</p>
<ol>
<li>图片资源直接放到APP包里，接口控制是否显示</li>
<li>接口返回图片的地址，APP根据图片地址去拿图片</li>
<li>下载压缩包，解压后替换图片</li>
</ol>
<p>第一种方式会增加APP的包体积，现在为了用户体验，还是尽量不要去给用户增加负担。灵活替换也是一个问题，严重依赖于发版。</p>
<p>第二种方式图片的地址是各自独立的，图片是各自下载，容易出现不完整性的情况，例如tabbar有一张图失败了，那岂不是换肤换了一半。</p>
<p>综合以上考虑，第三种采用压缩包的方式目前来说是比较推荐的。</p>
<p>下面针对我们详细说明一下自如APP的换肤过程。</p>
<h2 data-id="heading-1">二、实战</h2>
<h3 data-id="heading-2">2.1 换肤流程</h3>
<p>皮肤的替换流程图如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fd9019d03fa46278480fca73c385951~tplv-k3u1fbpfcp-watermark.image" alt="huanfuliuchengtu.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>APP启动后直接加载对应的皮肤文件，同时异步请求后台皮肤接口，接口返回一个压缩包链接，解压后解析包里的config.json文件，然后通过通知去触发换肤。
控制皮肤是否显示的逻辑完全由后台控制，后台返回skinSign为空则关闭换肤.</p>
<h3 data-id="heading-3">2.2 实现方式</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1148c058f264dc2a29bec8ee51b4432~tplv-k3u1fbpfcp-watermark.image" alt="huanfujiagou2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>皮肤管理组件分为网络模块、管理模块、Category</p>
<p>我们将皮肤管理器独立Cocoapods组件，业务层依赖换肤组件即可。</p>
<p>下面看一下config.json文件的内容示例:</p>
<pre><code class="copyable">&#123;
    "home_navi": &#123;
        "colors": &#123;
            "color_background": "#ffffff"
        &#125;,
        "images": &#123;
            "image_logo": "home_topLogo"
        &#125;
    &#125;,
    "home_tabbar": &#123;
        "colors": &#123;
            "color_background": "#F9F9F9",
            "color_button_normal": "#999999",
            "color_button_selected": "#444444"
        &#125;,
        "images": &#123;
            "image_one_button_normal": "tab按钮1图片",
            "image_one_button_selected": "tab按钮1选中图片",
            "image_two_button_normal": "tab按钮2图片",
            "image_two_button_selected": "tab按钮2选中图片",
            "image_three_button_normal": "tab按钮2图片",
            "image_three_button_selected": "tab按钮2选中图片"
        &#125;,
        "values": &#123;
            "value_one_button": "tab按钮1",
            "value_two_button": "tab按钮2",
            "value_three_button": "tab按钮3"
        &#125;
    &#125;,
    "loading": &#123;
        "resources": &#123;
            "resource_refreshImage" : "refresh.gif"
        &#125; 
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们针对首页导航(home_navi)、首页tabbar(home_tabbar)、加载loading(loading)三个模块进行举例。
在每个业务模块下都可以有4个功能模块分别是颜色(colors)、图片(images)、值(values)、资源(resources)，这4个模块根据自己的需要进行添加。colors控制的是颜色，这里我以16进制值为准。images控制的是图片，最普通的png文件。values控制的是值。resources控制的是资源文件，例如json、gif等文件。</p>
<p>针对UIView我们创建了一个Category，在这个Category中添加方法，如下：</p>
<pre><code class="copyable">- (void)configSkinMapModule:(NSString *)module skinMap:(NSDictionary *)skinMap;

- (void)configSkinMapModule:(NSString *)module skinMap:(NSDictionary *)skinMap
&#123;
    if (![ZRSkinManager sharedInstance].isOpenZRSkinManager) &#123;
        return;
    &#125;
    NSMutableDictionary *tempDic = [skinMap mutableCopy];
    for (NSUInteger i = 0; i < tempDic.allKeys.count; i ++) &#123;
        NSString *key = tempDic.allKeys[i];
        NSString *value = tempDic[key];
        tempDic[key] = [NSString stringWithFormat:@"%@.%@",module,value];
    &#125;
    self.skinMap = [tempDic copy];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们在需要换肤的模块上注册一下，例如我们给tabbar的第一个按钮添加一下换肤功能，代码如下:</p>
<pre><code class="copyable">[_tabbarButton configSkinMapModule:kSkin_MODULE_HOME_TABBAR skinMap:
     @&#123;kSkinMapKey_button_image : @"image_one_button_normal",
       kSkinMapKey_button_selectedImage : @"image_one_button_selected",
       kSkinMapKey_button_titleColor : @"color_button_normal",
       kSkinMapKey_button_titleSelectedColor : @"color_button_selected",
       kSkinMapKey_button_title : @"value_one_button"
       &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行了以上代码之后发生了什么呢？我会在skinMap的set方法中给此_tabbarButton加上NSNotificationCenter</p>
<pre><code class="copyable">[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(skinChanged) name:kZRSkinDidChangeNotification object:nil];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当要换肤的时候，我们会触发kZRSkinDidChangeNotification通知。</p>
<p>那么skinChanged方法做了哪些操作呢？</p>
<p>我会创建一个SkinConstants文件去定义一下替换的方式标识。</p>
<pre><code class="copyable">// button相关
static NSString * const kSkinMapKey_button_image = @"kSkinMapKey_button_image";
static NSString * const kSkinMapKey_button_highlightedImage = @"kSkinMapKey_button_highlightedImage";
static NSString * const kSkinMapKey_button_selectedImage = @"kSkinMapKey_button_selectedImage";
static NSString * const kSkinMapKey_button_disabledImage = @"kSkinMapKey_button_disabledImage";
static NSString * const kSkinMapKey_button_titleColor = @"kSkinMapKey_button_titleColor";
static NSString * const kSkinMapKey_button_titleHighlightedColor = @"kSkinMapKey_button_titleHighlightedColor";
static NSString * const kSkinMapKey_button_titleSelectedColor = @"kSkinMapKey_button_titleSelectedColor";
static NSString * const kSkinMapKey_button_titleDisabledColor = @"kSkinMapKey_button_titleDisabledColor";
static NSString * const kSkinMapKey_button_title = @"kSkinMapKey_button_title";

// label相关
static NSString * const kSkinMapKey_label_text = @"kSkinMapKey_label_text";
static NSString * const kSkinMapKey_label_textColor = @"kSkinMapKey_label_textColor";
static NSString * const kSkinMapKey_label_backgroundColor = @"kSkinMapKey_label_backgroundColor";

// imageview相关
static NSString * const kSkinMapKey_imageView_image = @"kSkinMapKey_imageView_image";
static NSString * const kSkinMapKey_imageView_gif = @"kSkinMapKey_imageView_gif"; // gif动画
static NSString * const kSkinMapKey_imageView_backgroundColor = @"kSkinMapKey_imageView_backgroundColor";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信从名字你们就能看出来，每一个定义都是UIKit里面的一个方法。</p>
<p>然后我说一下刚才那个Category中加的方法，其中module对应的正是config.json中的业务模块，例如home_navi。skinMap中的key是替换的方式标识正是SkinConstants中的定义，value则是config.json中的对应的模块的key值。
也就是上面加的方法的意思是给这个home_navi业务模块中的某一个button增加了修改普通模式图片(kSkinMapKey_button_image)、修改选中模式图片(kSkinMapKey_button_selectedImage)、普通模式文字颜色(kSkinMapKey_button_titleColor)、修改选中模式图片(kSkinMapKey_button_selectedImage)、修改文字值(kSkinMapKey_button_title)的功能。</p>
<p>我们在通知触发方法中使用如下代码去执行替换过程</p>
<pre><code class="copyable">- (void)changeSkin
&#123;
    NSDictionary *map = self.skinMap;
    if ([self isKindOfClass:[UIButton class]]) &#123;
        UIButton *obj = (UIButton *)self;
        if (map[kSkinMapKey_button_image]) &#123;
            [obj setImage:SkinImage(map[kSkinMapKey_button_image]) forState:UIControlStateNormal];
        &#125;
        if (map[kSkinMapKey_button_highlightedImage]) &#123;
            [obj setImage:SkinImage(map[kSkinMapKey_button_highlightedImage]) forState:UIControlStateHighlighted];
        &#125;
        if (map[kSkinMapKey_button_selectedImage]) &#123;
            [obj setImage:SkinImage(map[kSkinMapKey_button_selectedImage]) forState:UIControlStateSelected];
        &#125;
        if (map[kSkinMapKey_button_disabledImage]) &#123;
            [obj setImage:SkinImage(map[kSkinMapKey_button_disabledImage]) forState:UIControlStateDisabled];
        &#125;
        if (map[kSkinMapKey_button_titleColor]) &#123;
            [obj setTitleColor:SkinColor(map[kSkinMapKey_button_titleColor]) forState:UIControlStateNormal];
        &#125;
      ...以下省略...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时我本地会存有一个localConfig.json用于管理本地的需要替换皮肤的模块，内容和config.json一模一样。只是他取的都是本地默认的皮肤资源配置。
SkinImage是处理images模块的，这个宏定义是pngResourceForSign:方法的宏，用于去处理该加载哪个图片文件。
关于colors、resources等其他模块我就不一一介绍了，都是大同小异。</p>
<pre><code class="copyable">// 获取Png资源
- (UIImage *)pngResourceForSign:(NSString *)sign;
&#123;
    NSArray *array = [sign componentsSeparatedByString:@"."];
    NSString *module = array.firstObject;
    NSString *key = array.lastObject;
    NSDictionary *moduleDic = self.configData[module];
    NSDictionary *imageDic = moduleDic[@"images"];
    NSString *value = imageDic[key];
    // 这里已经在初始化的时候做了判断，self.path有值则为后台皮肤，无值则为本地默认皮肤。
    if (!self.path.length) &#123;
        return [UIImage imageNamed:value];
    &#125;
    NSString *filePath = [self.path stringByAppendingFormat:@"/%@",value];
    UIImage *image = [UIImage imageWithContentsOfFile:filePath];
    return image;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是换肤的核心思路部分，主要就是通过Category的方式，使每一个UIView都拥有换肤的能力，然后通过NSNotificationCenter的方式触发。皮肤下载，皮肤管理等部分就不一一介绍了。</p>
<h2 data-id="heading-4">三、结语：</h2>
<p>换肤的方式千千万，但基于iOS的特性都离不开Category，如果你还有其他的方案，欢迎一起交流。</p>
<p>参考资料：</p>
<ol>
<li><a href="https://github.com/yanjunz/ThemeManager" target="_blank" rel="nofollow noopener noreferrer">github·ThemeManager</a></li>
<li><a href="https://github.com/jiecao-fm/SwiftTheme" target="_blank" rel="nofollow noopener noreferrer">github·SwiftTheme</a></li>
<li><a href="https://www.jianshu.com/p/54a1f56f5249" target="_blank" rel="nofollow noopener noreferrer">iOS换肤方案</a></li>
<li><a href="https://github.com/JyHu/EasyTheme" target="_blank" rel="nofollow noopener noreferrer">github·EasyTheme</a></li>
<li><a href="https://www.cnblogs.com/darrydai/p/5117131.html" target="_blank" rel="nofollow noopener noreferrer">「节日换肤」通用技术方案__iOS端实现</a></li>
</ol>
<blockquote>
<p><strong>本文作者：自如大前端研发中心-曲茵</strong></p>
</blockquote>
<h2 data-id="heading-5">招聘信息</h2>
<blockquote>
<h4 data-id="heading-6">自如大前端研发中心招募新同学！</h4>
<p>FE/iOS/Android工程师</p>
<p>公司福利有：</p>
<ul>
<li>全额五险一金，并额外购买商业保险</li>
<li>免费健身房+年度体检</li>
<li>公司附近租房9折优惠</li>
<li>每年2次晋升机会</li>
</ul>
<p>办公地点：北京酒仙桥普天实业科技园
欢迎对技术有执着热爱的你加入我们！简历请投递 <a href="mailto:zhangxl122@ziroom.com">zhangxl122@ziroom.com</a>, 或加微信 v-nice-v 详聊！</p>
</blockquote></div>  
</div>
            