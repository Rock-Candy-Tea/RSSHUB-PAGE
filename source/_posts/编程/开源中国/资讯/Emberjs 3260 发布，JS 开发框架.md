
---
title: 'Ember.js 3.26.0 发布，JS 开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: '/images/404.gif'
author: 开源中国
comments: false
date: Tue, 23 Mar 2021 23:22:00 GMT
thumbnail: '/images/404.gif'
---

<div>   
<div class="content">
                                                                                            <p>Ember.js 是一个 JavaScript 框架，可大大减少构建任何 Web 应用程序所需的时间、精力和资源。它致力于通过执行大多数 Web 开发项目中涉及的所有常见、重复但必不可少的任务，使开发者尽可能地高效。</p> 
<p>Ember 框架的一个有价值的属性是它使用语义版本控制来帮助项目跟上框架的变化。在删除任何功能或 API 之前，它首先会经过一个弃用期，在该期间内仍支持该功能，但是使用该功能会生成一条警告，并记录到浏览器控制台中。本次更新也围绕这类内容，以下是 Ember.js 3.26.0 版本更新的内容：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19255" target="_blank">#19255</a> 弃用控制器和路由的转换方法</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19359" target="_blank">#19359</a> 采用新的浏览器支持策略，弃用旧的浏览器支持策略。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19371" target="_blank">#19371</a>  弃用隐式的 <code>this</code> 属性查询回退</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19372" target="_blank">#19372</a>  为 Classic 版和可选功能添加弃用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19373" target="_blank">#19373</a> 取消旧版管理器的功能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19379" target="_blank">#19379</a> 重构 DataAdapter，使其不使用 Array Observers 或 Observers</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19345" target="_blank">#19345</a> 弃用 <code><LinkTo></code> 位置参数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19346" target="_blank">#19346</a> 弃用 <code>&#123;&#123;#with&#125;&#125;</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19358" target="_blank">#19358</a> 弃用隐式注入</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19378" target="_blank">#19378</a> 修正 template-only-glimmer-components 功能检测中的排版错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19298" target="_blank">#19298</a> 路由序列化没有提取代理服务器上的 param</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19469" target="_blank">#19469</a> 防止修饰符销毁时的急切参数消耗</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19405" target="_blank">#19405</a> 当 <code>app/router.js</code> 注入路由器服务时，避免实例化错误。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19436" target="_blank">#19436</a> 支持带冒号的 Observer 键</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19374" target="_blank">#19374</a> 弃用 hasBlock 和 hasBlockParams</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19375" target="_blank">#19375</a> 弃用旧的类绑定语法和 &#123;&#123;attrs&#125;&#125;</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19381" target="_blank">#19381</a> 弃用 Array Observers</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Freleases%2Ftag%2Fv3.26.0" target="_blank">https://github.com/emberjs/ember.js/releases/tag/v3.26.0</a></p>
                                        </div>
                                      
</div>
            