
---
title: 'Electron 15.1.0 发布，跨平台桌面应用开发工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2584'
author: 开源中国
comments: false
date: Tue, 05 Oct 2021 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2584'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Electron 15.1.0 现已发布，主要更新内容如下： </span></p> 
<p style="text-align:start"><strong>Features</strong></p> 
<ul> 
 <li>添加了 WebHID 支持</li> 
 <li>向“context-menu”事件的<code>params</code>对象添加了<code>frame</code>属性</li> 
 <li>为<code>'certificate-error'</code>事件添加了<code>isMainFrame</code>参数</li> 
 <li>添加<code>textWidth</code>选项到<code>dialog.showMessageBox()</code>/ <code>dialog.showMessageBoxSync()</code></li> 
</ul> 
<p><strong>Fixes</strong></p> 
<div> 
 <div> 
  <ul> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了 Let's Encrypt DST Root CA X3 证书过期问题</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了<code>navigator.fonts.query()</code>的崩溃</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了 BrowserView 拖动行为与 MacOS 窗口拖动不一致的问题</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了文件选择器中的按钮标签在 Linux 上本地化不正确的问题</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了一个问题，即对<code>BrowserWindow</code>中的可拖动区域的更改会错误地影响到附加的<code>BrowserView</code>中的区域</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了设置纵横比的不可调整大小的非全屏窗口可能会给<code>isMaximized()</code>返回不正确结果的问题</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了无法立即拖动失焦的 BrowserViews 的问题</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了一个问题，即使用 BoringSSL 不支持的算法对<code>crypto.createPrivateKey</code>的一些调用会在调用其返回值的方法时导致崩溃</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了禁用调整大小后页面周围的黑色边框</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了 destroying WebContents 时由于 double free 导致的崩溃</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>修复了 v8 中由于<code>(Check failed: !regexp_stack_-&gt;is_in_use())</code> 引起的崩溃</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
  <p><strong>Other Changes</strong></p> 
  <ul> 
   <li><span><span><span><span><span><span><span><span><span><span><span><span><span>将 Chromium 更新为 94.0.4606.61</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
</div> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv15.1.0" target="_blank">https://github.com/electron/electron/releases/tag/v15.1.0</a> </p>
                                        </div>
                                      
</div>
            