
---
title: '使用React hooks如何只让下面这段代码的子组件只render一次？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=6356'
author: 知乎
comments: false
date: Sat, 14 Aug 2021 02:25:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=6356'
---

<div>   
nekocode的回答<br><br><p>作为给 ant design 贡献过代码的人，可以告诉你 antd 内部是用的 forwardRef 和 useImperativeHandle 来实现这个效果。这也是目前仅通过内部 hooks 来实现的最正确的做法。</p><p>看了一圈这个问题下的回答，只有 <a class="member_mention" href="http://www.zhihu.com/people/eaf86504c6f9ac2b343632b0526d7f8c" data-hash="eaf86504c6f9ac2b343632b0526d7f8c" data-hovercard="p$b$eaf86504c6f9ac2b343632b0526d7f8c">@maxcalibur</a> 回答到这两个 hook，但是却一个赞都没（黑人问号）。其他人要么直接说没法实现，要么通过各种绕弯子来实现，。。</p><p>另外拓展一下，用我这个基于观察者模式共享 state 的库来做也是可以实现的：</p><a href="http://link.zhihu.com/?target=https%3A//github.com/nekocode/use-shared-state" data-draft-node="block" data-draft-type="link-card" data-image="https://pic1.zhimg.com/v2-8b372cbb1bc1a2c3bb0755f0239f1359_qhd.jpg" data-image-width="1200" data-image-height="600" class=" wrap external" target="_blank" rel="nofollow noreferrer">GitHub - nekocode/use-shared-state: React hook for sharing state or notifying event between components. Just like the widget controller in Flutter.</a><p>去看一下我写的 readme 下的 live example 就知道了，目前已在几家大大小小的公司中投产了。</p><p>还有一些其他不算方法的方法：</p><ol><li>子组件直接用父组件传的 props 而不是用内部自己维护的 state 来渲染，然后通过 callback 反馈给父组件来刷新传进来的 props 也是可以的，但是子组件一定要自己维护 state 的情况就不能这么用了。</li><li>再另外，父组件渲染时改变一下子组件的 key 来强制重新创建 dom 也是可以实现题主要的效果的，只不过性能上会更差（狗头）。</li></ol><p>那些说没法实现的不是被打脸么。</p>  
</div>
            