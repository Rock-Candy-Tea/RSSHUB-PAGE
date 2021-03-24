
---
title: 'Firefox 87.0 发布，进一步改善隐私'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: '/images/404.gif'
author: 开源中国
comments: false
date: Tue, 23 Mar 2021 23:04:00 GMT
thumbnail: '/images/404.gif'
---

<div>   
<div class="content">
                                                                                            <p>Mozilla Firefox 87.0 今天发布，在改善用户隐私方面做了进一步的努力。</p> 
<p>Firefox 87 引入了 SmartBlock，这是一种全新的智能追踪器拦截机制，适用于隐私浏览和严格追踪保护模式。通过为被屏蔽的第三方追踪脚本提供本地替身，在充分保护用户不受追踪器侵害的同时，也减少了网站无法正常加载的情况。</p> 
<p>由于当今网络正在走向https-only，浏览器也在采取措施提高用户的隐私，87 版本推出了新的默认HTTP Referrer 策略，而不是 'no-referrer-when-downgrade'。它是'strict-origin-when-cross-origin'，将删减 URL 中的路径和查询字符串等用户敏感信息，以保护隐私。</p> 
<p>此次更新内容具体如下：</p> 
<h3>新功能：</h3> 
<ul> 
 <li>在使用 SmartBlock 的"隐私浏览"和"严格的增强跟踪保护"时将会遇到更少的网站加载错误，SmartBlock 提供了替身脚本，使网站能够正常加载。</li> 
 <li>为了进一步保护您的隐私，我们新的默认 HTTP Referrer 策略将从 referrer 头中修改路径和查询字符串信息，以防止网站意外泄露敏感的用户数据。</li> 
 <li>在页面中查找中的"Highlight All"功能现在会在滚动条旁显示与该页面上找到的匹配位置相对应的勾号。</li> 
 <li>全面支持 macOS 内置屏幕阅读器 VoiceOver。</li> 
 <li>我们增加了一个新的语言：西里西亚语</li> 
</ul> 
<h3>修复：</h3> 
<ul> 
 <li>修复了几个重要的可访问性问题： 
  <ul> 
   <li>视频控件现在有了可见的焦点样式，视频和音频控件现在可以通过键盘导航；</li> 
   <li>HTML <meter> 现在可以被屏幕阅读器念出了；</li> 
   <li>Firefox 现在在附加组件管理器中设置了一个有用的初始焦点；</li> 
   <li>现在，当 aria-labelledby/describedby 内容发生变化时，Firefox 将启动名称/描述变化事件；</li> 
  </ul> </li> 
 <li>各种安全修复</li> 
</ul> 
<h3>变化：</h3> 
<ul> 
 <li>为了防止用户在填写表格时丢失数据，Firefox 已经禁用了 Backspace 键作为后退导航按钮的导航快捷键。要重新启用 Backspace 键盘快捷键，你可以将 about:config 偏好设置 <code>browser.backspace_action</code> 改为 0，你也可以使用推荐的 Alt+左箭头（Mac上为 Command + 左箭头）快捷键代替。</li> 
 <li>我们已经从"库"菜单中删除了不经常使用或在浏览器中有其他访问点的项目：同步标签页、最近的亮点和口袋列表。</li> 
 <li>我们简化了"帮助"菜单，减少了多余的项目，例如指向 Firefox 支持页面的项目，这些页面也可以通过"获取帮助"项目访问。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mozilla.org%2Fen-US%2Ffirefox%2F87.0%2Freleasenotes%2F" target="_blank">https://www.mozilla.org/en-US/firefox/87.0/releasenotes/</a></p>
                                        </div>
                                      
</div>
            