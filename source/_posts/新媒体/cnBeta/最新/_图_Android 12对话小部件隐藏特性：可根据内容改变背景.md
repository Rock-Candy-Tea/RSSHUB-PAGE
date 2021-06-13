
---
title: '_图_Android 12对话小部件隐藏特性：可根据内容改变背景'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0613/f492db1f1eb6ffc.jpg'
author: cnBeta
comments: false
date: Sun, 13 Jun 2021 01:40:47 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0613/f492db1f1eb6ffc.jpg'
---

<div>   
几天前，Google放出了 Android 12 的第 2 个测试版本。它带来了新版系统最令人兴奋的功能之一：根据你的壁纸来自动更改背景色。在对新版本进行深度挖掘之后，外媒 XDA 还发现了备受期待的 Conversations 小部件，而且它的背景可以根据信息内容的不同而改变。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0613/f492db1f1eb6ffc.jpg" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0613/dd2a76420ddd632.jpg" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0613/b40b71b9af83a30.jpg" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0613/b286ec061f9c596.jpg" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0613/7ee92c97f86c4de.jpg" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0613/503999679f05e5c.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">Android 12 Beta 2 中的 Conversations 小部件显示了联系人的头像、名称以及最后一条信息的内容。Twitter 用户 Neil Rahmouni 向外媒 XDA 爆料，称信息中的某些文字可以触发更改 Conversations 小部件的背景。当用户收到一条包含 2 个或更多感叹号的消息时，小工具的背景突然充满了半透明的感叹号。</p><p style="text-align: left;">XDA 确认，当一条信息包含2个或更多的感叹号时，对话小组件确实会改变其背景。我们还发现，当消息中包含2个或更多的问号时，或者如果有混合的问号和感叹号，背景也会改变。此外，当重复使用一个表情符号时，背景也会改变。</p><p style="text-align: left;">深入研究 Android 12 Beta 2 的 SystemUI，XDA 了解到 PeopleTileViewHelper 类使用正则表达式来检查信息中的某些模式。如果有两个或更多的感叹号，两个或更多的问号，问号和感叹号的混合，或两个或更多相同的表情符号，那么该文本/表情符号就会被应用到小部件的背景上。</p><p style="text-align: left;">可以肯定的是，这是一个小功能，但它是一个很好的功能，因为它肯定会吸引你的注意力。代码显示，对话小组件还将显示联系人的生日、周年纪念日、"故事 "更新、游戏中的状态、位置等等的状态信息，但我们还没有看到这个功能。</p>   
</div>
            