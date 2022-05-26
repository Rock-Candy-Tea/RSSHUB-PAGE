
---
title: 'Laravel v9.14.0 发布，经典 PHP 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2073'
author: 开源中国
comments: false
date: Thu, 26 May 2022 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2073'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#000000">Laravel framework 包含  PHP 框架 Laravel 的核心代码，目前更新了 9.14.0 版本，主要更新内容如下：</span></p> 
<h3><strong>添加</strong></h3> 
<ul> 
 <li>添加了为 MySQL 和 Postgres 添加表注释的功能 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42401" target="_blank">#42401</a> )</li> 
 <li>添加了动态废弃工厂状态 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42414" target="_blank">#42414</a> )</li> 
 <li>添加了 Illuminate/Collections/Arr::prependKeysWith() ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42448" target="_blank">#42448</a> )</li> 
 <li>向 TestCase 添加了可启动特征（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42394" target="_blank">#42394</a>）</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>修复 updateOrCreate 和 firstOrCreate 上的克隆问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42434" target="_blank">#42434</a> )</li> 
 <li>防止在 RateLimiter@tooManyAttempts ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42462" target="_blank">#42462</a> )中双重清理密钥</li> 
 <li>将刷新处理程序添加到流式测试响应的输出缓冲区（错误修复）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42481" target="_blank">#42481</a>）</li> 
</ul> 
<h3><strong>改变</strong></h3> 
<ul> 
 <li>向 SES 异常添加简洁的错误消息 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42426" target="_blank">#42426</a> )</li> 
 <li>当路由被缓存时，使用 duplicate 而不是 createFromBase 来克隆请求（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42420" target="_blank">#42420</a>）</li> 
 <li>当路由参数未指定自定义绑定字段但不同的参数指定时使用模型路由键 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42425" target="_blank">#42425</a> )</li> 
 <li>添加了将 paginate() $perPage 参数作为可调用的功能，并可以访问 $total ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42429" target="_blank">#42429</a> )</li> 
 <li>将 ServeCommand 环境列表提取到静态属性 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42444" target="_blank">#42444</a> )</li> 
 <li>在视图中使用路由参数（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F42461" target="_blank">#42461</a>）</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Freleases%2Ftag%2Fv9.14.0" target="_blank">https://github.com/laravel/framework/releases/tag/v9.14.0</a></p>
                                        </div>
                                      
</div>
            