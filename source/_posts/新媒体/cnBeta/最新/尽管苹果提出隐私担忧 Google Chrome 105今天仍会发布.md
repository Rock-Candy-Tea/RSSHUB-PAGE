
---
title: '尽管苹果提出隐私担忧 Google Chrome 105今天仍会发布'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0830/c97c1b1267fdb19.jpg'
author: cnBeta
comments: false
date: Tue, 30 Aug 2022 09:15:34 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0830/c97c1b1267fdb19.jpg'
---

<div>   
本月早些时候，Google Chrome 104来到稳定通道，更新了网络蓝牙API，由于暴露了可用于侵犯用户隐私的访问指纹，Google面临苹果和Mozilla的一致批评。今天，Chrome 105还是会照常发布，虽然它不像以前的版本那样有争议，但苹果对这个版本还是有一些担忧。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0830/c97c1b1267fdb19.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0830/c97c1b1267fdb19.jpg" title alt="1661845423_10790277_(12).jpg" referrerpolicy="no-referrer"></a></p><p>Google Chrome 105在后台有很多变化，其中之一是用户代理客户端提示，这是一个公开设备活动和条件信息的API，以便开发者可以使他们的网页对各种硬件作出动态响应。随着3月份Chrome 100的发布，Google告诫网络开发者，他们必须在2023年3月之前迁移到这个客户端提示API，而不是依赖用户代理字符串。</p><p>因此，对客户端提示API的批评并不新鲜，但Chrome 105对其做了一些改变，开发者可以请求显示内容的浏览器窗口的高度信息。以前，这个API只暴露了视口的宽度信息，但Google认为，获取高度也是有用的，可以确保网页上受高度限制的图像正常显示。客户端提示委托访问的语法也在改变，以回应开发者的反馈。</p><p>Google强调了一个可以追溯到2020年的问题报告，在这个帖子中，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>的WebKit团队提到了对客户端提示API被用来识别用户的担忧。</p><p>以下是该帖文的摘录：</p><blockquote><p>我可能误读了规范，但按照书面规定，getHighEntropyValues似乎可以访问第一方上下文中的第三方脚本和在第三方iframe中运行的脚本的所有高熵客户端提示，而不管网站通过相关的HTTP头选择了哪种提示。</p></blockquote><p>如果你想知道为什么苹果对Chrome浏览器的想法如此重要，那是因为网络开发者最好希望编写的代码能够在所有的浏览器上保持一致和兼容。因此，当涉及到一个新功能时，主要浏览器供应商的支持是很重要的。如果某个厂商拒绝一项功能，就意味着开发者要么完全放弃这项功能，要么为该浏览器编写特定的代码，以确保跨平台的兼容性和行为。</p><p>还有其他一些值得注意的变化，虽然没有那么大的争议性。在非安全情况下使用WebSQL被废弃，因为它是2009年的一个遗留规范，苹果在2019年放弃了它，Mozilla甚至没有实现它。Chrome 105中其他被删除的功能包括从未打算发布的手势滚动DOM事件以及在自定义标识符中使用"默认"CSS关键字的能力。</p><p>一个名为"onbeforeinput"的全局事件处理程序也被引入，它得到了苹果、Mozilla和网络开发者的支持。同样，另一个得到开发者支持的新功能是明确标记应被阻止渲染的资源。</p><p>与Chrome 105一起发布的其他功能有：为元素提供更多组成样式的容器查询，两个伪类选择器，一种更容易访问TransformStre<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>efaultController类的方法，以及导航类的一些新方法，以及在超滚动期间固定元素的一些行为变化。</p><p>另一件会让使用文件系统访问API的开发者非常高兴的事情是，能够在同一提示下获得可写目录和可读目录。以前，这只返回后者，这给用户造成了混乱和权限疲劳。同样，一个获取上传流的方法已经被引入，所以开发者不必在WebSocket上额外写入杂乱的代码来达到同样的目的。此外，Sanitizer API的MVP版本也将发布，它通过将一些维护负担转移到平台上，使开发者能够以更容易的方式建立无XSS的网络应用。</p><p><a href="https://static.cnbetacdn.com/article/2022/0830/4759e0b20e9cf8d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0830/4759e0b20e9cf8d.jpg" title alt="1661846059_10790277_(13).jpg" referrerpolicy="no-referrer"></a></p><p>Chrome还正在对音频输入和输出机制进行重大修改。流媒体和视频会议应用现在应该明确请求接收非系统音频。还有一个新的方法来解决导入的URL，以及一个媒体源扩展（MSE）API，此外，现在创建一个JSON响应更容易了。Worklet的加载现在也被报告给了资源计时，以增加透明度。</p><p>虽然这些都是普遍可用的功能，但也有相当多的功能被锁定在开发者标志后面。这些功能包括将所有的定时器（包括DOM定时器）限制到125Hz，这会鼓励开发者迁移到更好、更省电的替代品。其他有趣的功能包括匿名的iframe对象（在这里阅读所有的技术细节），从"canmakepayment"服务工作者事件中移除商家身份，并将WebHID API暴露给扩展服务工作者。</p><p>除了在Android上已经可以使用外，为了功能上的平等，Google也正在实施桌面版的Priorender 2。那些在Android<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>上使用游戏手柄玩游戏的人将会非常高兴地知道，游戏手柄API将能够利用触觉反馈选项，如触发式摇晃和双重摇晃（仅限Android 12以上）。最后，Chrome 105还实现了TLS加密客户端招呼特性（ECH），以改善标志后的隐私，这种做法类似于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>Edge。</p><p>正如你可能已经从这篇文章的篇幅中猜到的那样，Chrome 105是一个重大更新。它将在今天晚些时候开始推出。如果Chrome浏览器在一天中没有自动更新到105版本，请前往"帮助">"关于Google浏览器"，以便在更新可用时触发该更新。接下来是Chrome 106，它将于9月1日进入测试频道，并将于9月27日登陆稳定版。</p>   
</div>
            