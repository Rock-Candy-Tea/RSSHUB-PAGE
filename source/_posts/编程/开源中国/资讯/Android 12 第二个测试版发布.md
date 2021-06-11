
---
title: 'Android 12 第二个测试版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0611/065840_aRnR_2744687.gif'
author: 开源中国
comments: false
date: Fri, 11 Jun 2021 06:59:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0611/065840_aRnR_2744687.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Google 在 I/O 2021 大会结束后发布了 Android 12 的第一个测试版。时隔几周时间，Google 发布了 Android 12 的第二个 Beta 测试版，该版本补齐了此前承诺的部分功能。</p> 
<p>Android 12 Beta 2 包括补上了 Google I/O 上谈到的几个新的隐私功能，以及多项功能更新，以改善功能、稳定性和性能。以下是本次更新的一些亮点：</p> 
<p><strong>隐私仪表板：</strong></p> 
<p>Google 增加了一个隐私仪表板，让用户对应用程序正在访问的数据有更好的可见性。仪表板提供了一个简单而清晰的时间轴视图，显示最近的应用程序对麦克风、摄像头和位置的访问。用户还可以要求应用程序提供关于它为什么访问敏感数据的详细信息，开发人员可以通过处理新的系统意图（ACTION_VIEW_PERMISSION_USAGE_FOR_PERIOD）在活动中提供这些信息。Google 建议应用程序利用这个功能来主动帮助用户了解在给定时间段内的访问情况。</p> 
<p><img alt height="698" src="https://static.oschina.net/uploads/space/2021/0611/065840_aRnR_2744687.gif" width="960" referrerpolicy="no-referrer"></p> 
<p><strong>麦克风和摄像头指示器：</strong></p> 
<p>Google 在状态栏中添加了指示器，让用户知道应用程序何时在使用设备摄像头或麦克风。用户可以进入快速设置，查看哪些应用程序正在访问他们的摄像头或麦克风数据，并在需要时管理权限。对于开发者，我们建议审查你的应用程序对麦克风和摄像头的使用，并删除任何用户不会想到的东西。</p> 
<p><strong>麦克风和摄像头切换：</strong></p> 
<p>Google 在支持的设备上增加了快速设置切换，使用户能够轻松地立即禁用应用程序对麦克风和摄像头的访问。当切换器被关闭时，访问这些传感器的应用程序将收到空白的相机和音频馈送。开发人员可以使用一个新的 API，SensorPrivacyManager，来检查设备是否支持切换功能。麦克风和摄像头控制适用于所有应用程序。</p> 
<p><strong>剪贴板读取通知：</strong></p> 
<p>为了让用户更清楚地了解应用程序何时从剪贴板中读取信息，Android 12 现在会在应用程序每次调用 getPrimaryClip() 时，在屏幕底部显示一个弹出提醒。如果剪贴板内容是从同一个应用中复制的，系统就不会显示提示。Google 建议尽量减少你的应用程序从剪贴板中读取的内容，并确保你只在用户期望的情况下访问剪贴板。</p> 
<p><strong>更直观的连接体验：</strong></p> 
<p>为了帮助用户更好地了解和管理他们的网络连接，我们在状态栏、快速设置和设置中引入了更简单、更直观的连接体验。新的互联网面板帮助用户在他们的互联网供应商之间切换，并更容易地解决网络连接问题。</p> 
<p><img alt height="961" src="https://static.oschina.net/uploads/space/2021/0611/065857_CPzN_2744687.png" width="960" referrerpolicy="no-referrer"></p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2021%2F06%2Fandroid-12-beta-2-update.html" target="_blank"><code>https://android-developers.googleblog.com/2021/06/android-12-beta-2-update.html</code></a></p>
                                        </div>
                                      
</div>
            