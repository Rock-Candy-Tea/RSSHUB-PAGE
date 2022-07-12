
---
title: '云原生框架 Bali 3.2.2 发布：修复未处理的事件消息堆积'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7425'
author: 开源中国
comments: false
date: Tue, 12 Jul 2022 13:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7425'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">修复</h3> 
<ul> 
 <li>修复未处理的事件消息堆积<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaoj2010" target="_blank">@baoj2010</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbali-framework%2Fbali%2Fpull%2F139" target="_blank">PR#139</a></li> 
</ul> 
<p>---</p> 
<p>比如你的 event hander 是这样的：</p> 
<pre><code class="language-python">class EventHandler:
    @event_handler('UserCreated')
    def handle_user_created(self, event: UserCreatedEvent):
         pass</code></pre> 
<p>这里消息列队里面收到 `UserDeleted` 事件，在 3.2.2 之前的版本，是不会处理 `UserDeleted` 事件的，这样就会造成消息堆积了。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbali-framework.github.io%2Fbali%2F" target="_blank">Bali</a> 3.2.2 是专为这个优化单独发布的一个 patch 版本。</p>
                                        </div>
                                      
</div>
            