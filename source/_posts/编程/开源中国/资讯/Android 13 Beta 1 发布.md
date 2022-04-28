
---
title: 'Android 13 Beta 1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c4b7ec2451b0b6ad4d23fef27f55b6d1eb5.png'
author: 开源中国
comments: false
date: Thu, 28 Apr 2022 07:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c4b7ec2451b0b6ad4d23fef27f55b6d1eb5.png'
---

<div>   
<div class="content">
                                                                                            <p>Google 近日发布了 Android 13 的首个 Beta 测试版本，也正式宣告 Android 13 已走出开发者预览阶段。虽说现在马上就到五月份了，但首个 Beta 版本还是赶上了此前官方开发进度时间轴中所预期的时间表。</p> 
<h3>Android 13 开发进度时间轴</h3> 
<p><img alt height="160" src="https://oscimg.oschina.net/oscnet/up-c4b7ec2451b0b6ad4d23fef27f55b6d1eb5.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>Android 13 Beta 1 的新内容</h2> 
<p>Beta 1 包括了 Google 之前在开发者预览版中宣布的功能的最新更新，如新的通知权限、照片选择器、主题应用图标、改进的本地化和语言支持等，在此基础上，Android 13 Beta 1 还引入了少量的新功能。</p> 
<h3>媒体文件访问的权限更加细化：</h3> 
<p>以前，当一个应用程序想要读取本地存储中的共享媒体文件时，它需要申请 <code>READ_EXTERNAL_STORAGE</code> 权限，该权限可以访问所有类型的媒体文件。为了给用户带来更多的透明度和控制权，我们将引入一套新的权限，在访问共享媒体文件时有更细化的范围。</p> 
<p>有了新权限，应用现在可以请求访问共享存储中特定类型的文件：</p> 
<ul> 
 <li><code>READ_MEDIA_IMAGES</code>（用于图像和照片）</li> 
 <li><code>READ_MEDIA_VIDEO</code>（用于视频）</li> 
 <li><code>READ_MEDIA_AUDIO</code>（对于音频文件）</li> 
</ul> 
<p><img alt height="598" src="https://oscimg.oschina.net/oscnet/up-00bc661bcf57366078b223c6957fcf93a7c.png" width="700" referrerpolicy="no-referrer"></p> 
<p>当用户授予权限时，应用程序将拥有对相应媒体文件类型的读取权限。为了简化用户的体验，如果一个应用程序同时请求 <code>READ_MEDIA_IMAGE</code> 和 <code>READ_MEDIA_VIDEO</code>，系统会显示一个授予两种权限的对话框。</p> 
<h3>Keystore 和 KeyMint 中更好的错误报告:</h3> 
<p>对于生成密钥的应用，Keystore 和 KeyMint 现在提供了更详细准确的错误指示。Google 在 <code>java.security.ProviderException</code> 下添加了一个异常类层级，其中有 Android 特有的异常，其中包括 Keystore/KeyMint 错误代码，以及错误是否可以重试。你也可以修改密钥生成、签名和加密的方法来抛出新的异常。改进的错误报告现在应该给你提供你所需要的相关信息来重试密钥生成。</p> 
<h3><strong>预见性音频路由：</strong></h3> 
<p>为了帮助媒体应用程序确定他们的音频将如何被路由，Google 在 <code>AudioManager</code> 类中增加了新的音频路由 API。新的 <code>getAudioDevicesForAttributes()</code> API 允许你检索可能用于播放指定音频的设备列表，Google 还添加了 <code>getDirectProfilesForAttributes()</code> API 来帮助你了解你的音频流是否可以直接播放。使用这些新的 API 来确定为你的音轨使用的最佳 <code>AudioFormat</code>。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2022%2F04%2Fandroid-13-beta-1-blog.html" target="_blank"><span>https://android-developers.googleblog.com/2022/04/android-13-beta-1-blog.html</span></a></p>
                                        </div>
                                      
</div>
            