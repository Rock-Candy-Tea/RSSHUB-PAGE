
---
title: 'Bali 3.1.3 发布，支持事件驱动开发'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6029'
author: 开源中国
comments: false
date: Mon, 16 May 2022 11:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6029'
---

<div>   
<div class="content">
                                                                    
                                                        <p>这次的版本更新在原来已经支持的 HTTP、RPC 上增加了事件（event）支持。同时，软件的维护层面也增加了 CI 自动化测试的 Workflow。</p> 
<p>更新内容：</p> 
<p>1. 事件的定义 Event 基类</p> 
<p>2. 事件的处理方法及事件处理独立使用一个进程</p> 
<p>3. 文档全部使用 Mkdocs 迁移</p> 
<p> </p> 
<p>事件的定义方法（代码示例）</p> 
<pre><code class="language-python">from bali.events import Event

class HelloEvent(Event):
    # The __amqp_name__ here defaults to default, 
    # which means that the AMQP configuration using default is used
    __amqp_name__ = 'default' 

    def dict(self, *args, **kwargs):
        # Rewrite dict to allow events to be transferred in the AMQP component in the way you define. 
        # If dict is not rewritten, the message will be &#123;'type': self.type, 'payload': self.payload&#125;
        return &#123;'type': self.type, **self.payload&#125;</code></pre> 
<p> </p> 
<p>事件的 publish 方法（代码示例）</p> 
<pre><code class="language-python">dispatch(HelloEvent(type='hello', payload=&#123;'aaa':'bbb'&#125;))
</code></pre> 
<p>事件的 handle 方法（代码示例）</p> 
<pre><code class="language-python">class EventHandler:
    @event_handler('hello')
    def handle_event(event):
        print(event)</code></pre> 
<p>事件 handle 的进程启动</p> 
<pre><code class="language-bash">python main.py --event
</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            