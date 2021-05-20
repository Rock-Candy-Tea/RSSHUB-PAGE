
---
title: 'iOS插件开发思想'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dabdd4e3b4a4379b975466419826c1a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 00:11:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dabdd4e3b4a4379b975466419826c1a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>随着公司业务的发展，公司的播放器功能也越来越复杂，另外播放器作为通用功能，还需要支持不同业务线的播放器的定制，因此想着我们是不是可以借鉴前端开发一些插件化思想，把我们播放器的每个功能都当做一个插件，各个业务根据自己的喜好去定制不同的插件：</p>
<ul>
<li>下载</li>
<li>分享</li>
<li>字幕</li>
<li>弹幕</li>
<li>清晰度</li>
<li>速率</li>
<li>……</li>
</ul>
<p>对于播放器来说只需要维护通用的播放器的一些状态，比如播放的开始播放，暂停，结束，缓存进度，播放进度等。
因此希望通过下面这个Demo，模拟器了一下如何使用原生的方式模拟一下插件的开发思想。</p>
<h3 data-id="heading-0">一.整个代码的结构如下</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dabdd4e3b4a4379b975466419826c1a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>主要包含<code>CCPlayer</code>, <code>CCPlayerBuilder</code>,<code>CCPlayerPlugin</code>, <code>CCPlayerConfig</code> 这四个主要文件，接下来我们一个个介绍，这几个类分别做了哪些事情，提供了哪些方法？</p>
<h3 data-id="heading-1">二. 接下来我们详细介绍一下每个类扮演什么角色</h3>
<h5 data-id="heading-2">1. CCPlayer</h5>
<p>这个是一个通用的管理配置和插件的地方</p>
<pre><code class="copyable">@class CCPlayerBuilder;
@interface CCPlayer : NSObject

/** 单例 */
+ (id)sharedInstance;

/** 添加构造器 */
- (void)addPlayerBuilder:(CCPlayerBuilder *)builder;

/** 开启插件 */
- (void)startPlugins;

/** 停止插件 */
- (void)stopPlugins;

/** 获取所有插件 */
- (NSMutableSet *)getPlugins;

/** 移除所有插件 */
- (void)removeAllPlugin;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">2. CCPlayerBuilder</h5>
<p>这个一个专门管理插件的地方，同时承接插件的代理回调</p>
<pre><code class="copyable">@interface CCPlayerBuilder : NSObject

@property (nonatomic, weak) id<CCPlayerPluginListenerDelegate> pluginListener;

/** 获取所有插件 */
- (NSMutableSet *)getPlugins;

/** 移除所有插件 */
- (void)removeAllPlugin;

/** 根据tag获取插件 */
- (CCPlayerPlugin *)getPluginWithTag:(NSString *)tag;

/** 添加插件 */
- (void)addPlugin:(CCPlayerPlugin *)plugin;

/// 移除插件
/// @param tag 插件名称
- (void)removePluginWithTag:(NSString *)tag;

/** 移除插件 */
- (void)removePlugin:(CCPlayerPlugin *)plugin;

/** 是否包含某个插件 */
- (BOOL)isContainPlugin:(CCPlayerPlugin *)plugin;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">3. CCPlayerPlugin</h5>
<ul>
<li>定义插件的生命周期</li>
<li>插件的优先级</li>
<li>插件的配置</li>
</ul>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import "CCPlayerPluginConfig.h"

NS_ASSUME_NONNULL_BEGIN

/** 设置优先级 */
typedef NS_OPTIONS(NSUInteger, CCPlayerPluginPriority) &#123;
    CCPlayerPluginPriorityHigh,
    CCPlayerPluginPriorityMiddle,
    CCPlayerPluginPriorityLow
&#125;;

#pragma mark - CCPlayerPluginListenerDelegate
@protocol CCPlayerPluginProtocol;

// 添加时间监听代理
@protocol CCPlayerPluginListenerDelegate <NSObject>

@optional

- (void)onInit:(id<CCPlayerPluginProtocol>)plugin;
- (void)onStart:(id<CCPlayerPluginProtocol>)plugin;
- (void)onStop:(id<CCPlayerPluginProtocol>)plugin;
- (void)onDestroy:(id<CCPlayerPluginProtocol>)plugin;

/** 插件的优先级 */
- (void)onPriority:(id<CCPlayerPluginProtocol>)plugin;

@end


#pragma mark - CCPlayerPluginProtocol

@protocol CCPlayerPluginProtocol <NSObject>

@required

/** 开始 */
- (void)start;

/** 结束 */
- (void)stop;

/** 销毁 */
- (void)destroy;

/** 添加监听 */
- (void)setupPluginListener:(id<CCPlayerPluginListenerDelegate>)pluginListener;

/** 获取插件tag */
- (NSString *)getTag;

/** 插件的优先级 */
- (CCPlayerPluginPriority)pluginPriority;

@end


#pragma mark - CCPlayerPlugin

@interface CCPlayerPlugin : NSObject <CCPlayerPluginProtocol>

/** 插件配置类 */
@property (nonatomic, strong) CCPlayerPluginConfig *pluginConfig;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">4. CCPlayerConfig</h5>
<p>这个类做一些通用的配置</p>
<h3 data-id="heading-6">三、如何写插件？</h3>
<p>为了能够让大家更好的理解这几个类是怎么联系的，写了两个简单的插件，下载插件和分享插件</p>
<h4 data-id="heading-7">1. 分享插件</h4>
<ul>
<li>分享的配置</li>
</ul>
<pre><code class="copyable">@interface CCPlayerShareConfig : NSObject

+ (CCPlayerShareConfig *)defaultConfig;

/** 应用id */
@property (nonatomic, copy) NSString *appId;
/** 引用密码 */
@property (nonatomic, copy) NSString *appSecret;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>分享插件</li>
</ul>
<p>具体的插件的实现，可以下载代码，看细节</p>
<pre><code class="copyable">@protocol CCPlayerSharePluginDelegate <NSObject>

/** 分享平台 */
- (void)sharePlatform:(NSString *)platform;

- (void)shareError:(NSString *)error;

@end

@interface CCPlayerSharePlugin : CCPlayerPlugin

/** 添加分享平台 */
- (void)addPlatform:(NSArray *)platforms;

@property (nonatomic, assign) id<CCPlayerSharePluginDelegate> delegate;

@property (nonatomic, strong) CCPlayerShareConfig *config;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">2. 下载插件</h4>
<ul>
<li>下载配置</li>
</ul>
<pre><code class="copyable">@interface CCPlayerDownloadConfig : CCPlayerPluginConfig

+ (CCPlayerDownloadConfig *)defaultConfig;

/** 下载URL */
@property (nonatomic, copy) NSString *videoUrl;

/** 保存地址 */
@property (nonatomic, copy) NSString *saveFilePath;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>下载插件</li>
</ul>
<pre><code class="copyable">@protocol CCPlayerDownloadPluginDelegate<NSObject>

/** 开始下载 */
- (void)startDownLoadWithUrl:(NSString *)url;
/** 下载中 */
- (void)downloadWithProgress:(float)process;
/** 开始完成 */
- (void)finishDownloadLoadWithUrl:(NSString *)url;

@end

@interface CCPlayerDownloadPlugin : CCPlayerPlugin

@property (nonatomic, strong) CCPlayerDownloadConfig *config;

@property (nonatomic, weak) id<CCPlayerDownloadPluginDelegate> delegate;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">四、如何使用？</h3>
<pre><code class="copyable">#import "ViewController.h"
#import "CCPlayer.h"
#import "CCPlayerBuilder.h"
#import "CCPlayerSharePlugin.h"
#import "CCPlayerDownloadPlugin.h"

@interface ViewController ()<CCPlayerPluginListenerDelegate, CCPlayerSharePluginDelegate, CCPlayerDownloadPluginDelegate>

@end

@implementation ViewController

- (void)viewDidLoad &#123;
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    self.view.backgroundColor = [UIColor whiteColor];

    // 测试插件
    CCPlayer *player = [CCPlayer sharedInstance];
    CCPlayerBuilder *playerBuilder = [[CCPlayerBuilder alloc] init];
    playerBuilder.pluginListener = self; // pluginListener 回调 plugin 的相关事件
        
    CCPlayerSharePlugin *sharePlugin = [[CCPlayerSharePlugin alloc] init];
    sharePlugin.delegate = self;
    [playerBuilder addPlugin:sharePlugin];
    
    // 配置下载插件
    CCPlayerDownloadPlugin *downloadPlugin = [[CCPlayerDownloadPlugin alloc] init];
    
    CCPlayerDownloadConfig *config = [[CCPlayerDownloadConfig alloc] init];
    config.videoUrl = @"http://www.baidu.com";
    config.saveFilePath = @"/usr/download/video";
    downloadPlugin.config = config;
    
    downloadPlugin.delegate = self;
    [playerBuilder addPlugin:downloadPlugin];

    [player addPlayerBuilder:playerBuilder];
    [sharePlugin start];
    [downloadPlugin start];
    
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(100 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^&#123;
        // 移除插件
        [playerBuilder removePlugin:downloadPlugin];
        NSLog(@"插件%@", [player getPlugins]);
    &#125;);

    NSLog(@"插件个数%@", [player getPlugins]);
    NSLog(@"tag获取的插件是%@", [playerBuilder getPluginWithTag:@"downloadPlugin"]);
    NSLog(@"是否包含分享插件----%@", @([playerBuilder isContainPlugin:sharePlugin]));
&#125;

#pragma mark - CCPlayerPluginListenerDelegate
- (void)onInit:(id<CCPlayerPluginProtocol>)plugin &#123;
    
&#125;

- (void)onStart:(id<CCPlayerPluginProtocol>)plugin &#123;
    NSLog(@"插件是啥%@", plugin);
&#125;

- (void)onStop:(id<CCPlayerPluginProtocol>)plugin &#123;
    
&#125;

- (void)onDestroy:(id<CCPlayerPluginProtocol>)plugin &#123;
    
&#125;

- (void)onPriority:(id<CCPlayerPluginProtocol>)plugin &#123;
    
&#125;

#pragma mark - CCPlayerSharePluginDelegate
- (void)sharePlatform:(NSString *)platform &#123;
    NSLog(@"分享平台---%@", platform);
&#125;

- (void)shareError:(NSString *)error &#123;
    NSLog(@"错误信息是---%@", error);
&#125;

#pragma mark - CCPlayerDownloadPluginDelegate

- (void)startDownLoadWithUrl:(NSString *)url &#123;
    NSLog(@"开始下载--%@", url);
&#125;

- (void)downloadWithProgress:(float)process &#123;
    NSLog(@"下载进度--%@", @(process));
&#125;

- (void)finishDownloadLoadWithUrl:(NSString *)url &#123;
    NSLog(@"下载完成--%@", url);
&#125;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">五、由于代码比较简单，具体实现细节可查看</h3>
<p><a href="https://github.com/zwcshy/PluginDemo" target="_blank" rel="nofollow noopener noreferrer">传送门</a></p></div>  
</div>
            