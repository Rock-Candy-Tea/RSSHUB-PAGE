
---
title: '针对某个 UITextField 禁用第三方键盘'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f70c2ee7f774fddaa3243e0c2c70ae9~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 02:37:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f70c2ee7f774fddaa3243e0c2c70ae9~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在日常开发中，可能某个 <code>UITextField</code> 只能输入数字，但是因为安装了第三方键盘（搜狗、百度等）会受到影响，需要禁用第三方键盘。</p>
<p>禁用第三方键盘需要在 <code>AppDelegate.m</code> 中实现以下代码</p>
<pre><code class="copyable">- (BOOL)application:(UIApplication *)application
shouldAllowExtensionPointIdentifier:(NSString *)extensionPointIdentifier
&#123;
    if ([extensionPointIdentifier isEqualToString:@"com.apple.keyboard-service"]) &#123;
        return NO;
    &#125;
    return YES;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就全局禁用了第三方键盘，下面针对某个 <code>UITextField</code> 进行禁用第三方键盘</p>
<h4 data-id="heading-0">对某个 <code>UITextField</code> 禁用第三方键盘</h4>
<ol>
<li>
<p>给 <code>UITextField</code> 创建一个分类，然后在分类的 .h 文件中添加一个实例对象属性 <code>yxc_usingSystemKeyboard</code> 和一个类对象属性 <code>yxc_globalUsingSystemKeyboard</code></p>
<pre><code class="copyable">@property (nonatomic, assign) BOOL yxc_usingSystemKeyboard;  /**< 使用系统键盘 */
@property (nonatomic, assign, class) BOOL yxc_globalUsingSystemKeyboard;   /**< 全局是否使用系统键盘，主动设置无效 */
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>关联属性</p>
<pre><code class="copyable">- (void)setYxc_usingSystemKeyboard:(BOOL)yxc_usingSystemKeyboard &#123;
    
    objc_setAssociatedObject(self, @selector(yxc_usingSystemKeyboard), @(yxc_usingSystemKeyboard), OBJC_ASSOCIATION_ASSIGN);
&#125;

- (BOOL)yxc_usingSystemKeyboard &#123;
    
    NSNumber *yxc_usingSystemKeyboard = objc_getAssociatedObject(self, @selector(yxc_usingSystemKeyboard));
    return [yxc_usingSystemKeyboard boolValue];
&#125;

+ (void)setYxc_globalUsingSystemKeyboard:(BOOL)yxc_globalUsingSystemKeyboard &#123;
    
    objc_setAssociatedObject(self, @selector(yxc_globalUsingSystemKeyboard), @(yxc_globalUsingSystemKeyboard), OBJC_ASSOCIATION_ASSIGN);
&#125;

+ (BOOL)yxc_globalUsingSystemKeyboard &#123;
    
    NSNumber *yxc_globalUsingSystemKeyboard = objc_getAssociatedObject(self, @selector(yxc_globalUsingSystemKeyboard));
    return [yxc_globalUsingSystemKeyboard boolValue];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>监听 <code>UITextFieldTextDidBeginEditingNotification</code> 和 <code>UITextFieldTextDidEndEditingNotification</code> 通知</p>
<pre><code class="copyable"> [[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(textFieldDidBeginEdit:)
                                             name:UITextFieldTextDidBeginEditingNotification
                                           object:self];

[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(textFieldDidEndEdit:)
                                             name:UITextFieldTextDidEndEditingNotification
                                           object:self];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在监听到 <code>UITextFieldTextDidBeginEditingNotification</code> 和 <code>UITextFieldTextDidEndEditingNotification</code> 通知对 <code>yxc_globalUsingSystemKeyboard</code> 值修改</p>
<pre><code class="copyable">- (void)textFieldDidBeginEdit:(NSNotification *)notification &#123;
    
    UITextField.yxc_globalUsingSystemKeyboard = self.yxc_usingSystemKeyboard;
&#125;

- (void)textFieldDidEndEdit:(NSNotification *)notification &#123;
    
    UITextField.yxc_globalUsingSystemKeyboard = NO;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>AppDelegate</code> 中 <code>application:shouldAllowExtensionPointIdentifier:</code> 方法中修改</p>
<pre><code class="copyable">- (BOOL)application:(UIApplication *)application shouldAllowExtensionPointIdentifier:(NSString *)extensionPointIdentifier
 &#123;
  if ([extensionPointIdentifier isEqualToString:@"com.apple.keyboard-service"]) &#123;
      if (UITextField.yxc_globalUsingSystemKeyboard) &#123;
          return NO;
      &#125;
  &#125;
  return YES;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过对某个 <code>UITextField</code> 实例对象设置 <code>yxc_usingSystemKeyboard</code> 属性值为 <code>YES</code>  后就对某个 <code>UITextField</code> 禁用了第三方键盘.</p>
<p>效果:</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f70c2ee7f774fddaa3243e0c2c70ae9~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="针对某个输入框禁用第三方键盘效果.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这里，第一个输入框默认的样式，不禁用第三方键盘，第二个输入框禁用第三方键盘并且设置键盘样式为 <code>UIKeyboardTypeNumberPad</code></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fguoguangtao%2FYXCTool" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/guoguangtao/YXCTool" ref="nofollow noopener noreferrer">代码</a></p></div>  
</div>
            