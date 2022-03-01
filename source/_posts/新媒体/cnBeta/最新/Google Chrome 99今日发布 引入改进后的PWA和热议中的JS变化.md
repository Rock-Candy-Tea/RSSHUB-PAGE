
---
title: 'Google Chrome 99今日发布 引入改进后的PWA和热议中的JS变化'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/02/14914042d4dc347.webp'
author: cnBeta
comments: false
date: Tue, 01 Mar 2022 09:55:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/02/14914042d4dc347.webp'
---

<div>   
Google Chrome 98在一个月前发布，由于稳定版发布通道的更新频率最近转为四周一次，现在是Chrome 99发布的时候了。在这个版本中并没有出现大量的新功能，但考虑到Google已经非常接近Chrome 100的里程碑，这也是合理的。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/02/14914042d4dc347.webp" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/02/14914042d4dc347.webp" referrerpolicy="no-referrer"></a></p><p>Chrome 99将改变JavaScript（JS）adoptedStyleSheets规范的实现。这之前使用的是FrozenArray支持阵列，但现在将利用ObservableArray。新的方法将使突变JS数组变得更加容易。虽然这看上去都是相当技术性的，但对我们的读者来说，可以说算得上有趣的是，自2018年以来，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>、Mozilla、<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>和Google之间一直在争论这一规范的变化。</p><p>按照目前的情况，Google将在Chrome 99中继续推进实施，因为它得到了Mozilla和微软的支持。另一方面，苹果的WebKit团队拒绝支持实施上的改变，理由是没有值得这么做的好处。Google表示，它将继续确保向后兼容以前的实现方式，但是以相当失望的口吻回应的。尽管网络组件社区的其他成员普遍同意，并且得到了开发者社区的支持，但WebKit仍然对这一功能的实用性持怀疑态度。因此，互操作的风险主要是WebKit决定不实现这个功能。</p><p>最新版本的Chrome浏览器还整合了一个新的手写识别API，网络开发者可以利用它来提供墨迹功能，例如，在笔记类网络应用中。他们将不需要依靠第三方的整合。</p><p>谈到网络应用，Chrome 99将允许已安装的渐进式网络应用程序（PWA）在屏幕上覆盖更多区域，以便它们看起来更像本地应用而不是网络应用。</p><p>在CSS方面，calc()数学函数现在的功能更接近于官方规范。CSS级联层应该会让开发者更容易管理网络组件中的层。同样，"-webkit-standard"字体家族值被移除，以提高与Firefox的互操作性，开发者可以明确地使用"-webkit-body"来代替。如果你正在使用CSS进行文本格式化，可以在这里查看Chrome 99支持的新属性。</p><p>Canvas 2D API正在加速现代化，以达到与其他2D API相同的功能，利用现有的CSS属性，并提高性能。该API主要用于游戏和"全功能应用"。同样，Gamepad API也在增强，以符合标准规范。</p><p>Google还提供了一个新的文件系统访问API，如果你是一个使用Origin私有文件系统的开发者，它将提供对文件的高性能和就地写访问。苹果的WebKit团队也正在实现这个功能。</p><p>还有其他一些面向开发者的功能，如ShadowDOM中的自动填充，HTML输入元素的编程选择器，Intl Enumeration和Intl Locale Info API的引入，以及PaintWorklet的新目标。但这还不是全部，因为Chrome 99 DevTools中也有很多新功能，你可以在这里查看所有的细节。</p><p><a href="https://developer.chrome.com/blog/new-in-devtools-99/" _src="http://developer.chrome.com/blog/new-in-devtools-99/" target="_blank">http://developer.chrome.com/blog/new-in-devtools-99/</a><br></p><p>Chrome 99将在今天晚些时候开始推出。如果你在一天中没有自动更新到99版，请前往帮助>关于Google浏览器，一旦有了更新，就触发更新。接下来是Chrome 100，它将于3月3日进入Beta通道，并将于3月29日登陆稳定版，因为众所周知的UA发生了位数的变化，希望它不会出乱子。</p>   
</div>
            