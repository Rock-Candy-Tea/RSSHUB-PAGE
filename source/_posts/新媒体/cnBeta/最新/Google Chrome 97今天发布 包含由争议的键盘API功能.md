
---
title: 'Google Chrome 97今天发布 包含由争议的键盘API功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0104/bb1cde4c520ea7d.jpg'
author: cnBeta
comments: false
date: Tue, 04 Jan 2022 09:35:19 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0104/bb1cde4c520ea7d.jpg'
---

<div>   
Google Chrome
96在近两个月前进入稳定频道，尽管目前的发布节奏意味着我们应该期待每四周就有一个新的版本，但由于西方的假日季节，Chrome
97的情况并非如此。今天，Chrome 97终于来到稳定频道，其中一个值得注意的特点是键盘API中的一个新属性，这可以说是相当有争议的。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0104/bb1cde4c520ea7d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0104/bb1cde4c520ea7d.jpg" title alt="1641273994_a7c1gq_(4).jpg" referrerpolicy="no-referrer"></a></p><p>此前一些网络应用如Excel、PowerPoint和Word无法使用键盘API来识别在特定的布局上按下了哪个键，如法语或英语。增加"键盘地图"值解决了这个问题，虽然网络开发者显然支持它，但它面临着来自<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>WebKit团队和Mozilla开发团队的强烈批评。两者都表达了对隐私的担忧，说这个API暴露了一个访客指纹，可以用来识别和跟踪人们，特别是当他使用的键盘布局在一个地区不常见时。因此，苹果和Mozilla将这一API变化列为"有害"，并将不会在Safari和Firefox中分别实施。</p><p>另一个变化是，表格中的换行规范化现在将在Chrome的后期阶段完成，这将使其行为与Safari和Firefox保持一致，后者已经做到了这一点。此外，CSS数学函数现在可以接受一个"数字"值，而以前只支持"整数"。同样，透视CSS函数现在支持一个"none"参数，它可以解析为身份矩阵，因此利用它的动画可以以更简单的方式使用它。</p><p>一个新的HTMLScriptElement.supports()方法也被引入，这使开发者能够利用一个统一的方式来检测使用脚本元素的新功能。使用两个新的方法，从数组的最后一个索引开始搜索也更加容易。</p><p>Chrome 97中另一个有趣的功能是对通信协议的增强。目前，开发者在与远程服务器进行双向通信时使用WebSockets或RTCDataChannel。前者基于TCP，这意味着不适合对延迟敏感的应用，而后者基于SCTP，主要为点对点通信而设计。Google现在推出了一个WebTransport协议框架，解决了这两个问题，并支持使用可取消流和UDP式数据报的可靠和不可靠数据的双向通信。苹果公司还没有对此提出看法，但Mozilla已经将其归类为"值得进行原型设计"，这显然是一个好兆头。</p><p>最后，"PermissionStatus"接口也增加了一个"名称"属性，以便更容易识别和区分Permissions API的不同对象。处理导航请求的服务工作者现在也将利用来自"FetchEvent.request"的起源和重定向链。</p><p>Chrome 97将在今天晚些时候开始推出。如果你的浏览器没有自动更新到97版，请到帮助>关于Google浏览器，一旦有了更新，就会自动触发更新。接下来是Chrome 98，它将于1月6日进入测试频道，并将于2月1日登陆稳定通道。</p>   
</div>
            