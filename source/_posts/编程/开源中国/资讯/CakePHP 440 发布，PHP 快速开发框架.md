
---
title: 'CakePHP 4.4.0 发布，PHP 快速开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7874'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7874'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">CakePHP 是一个运用了诸如 ActiveRecord、Association Data Mapping、Front Controller 和 MVC（model–view–controller） 等著名设计模式的开源 Web 框架。CakePHP 用 PHP 编写，以 Ruby on Rails 的概念为模型，并在 MIT 许可下进行分发。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">4.4.0 是新的稳定版本，对 CakePHP 进行了大量改进，主要集中在以下方面：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f">有一个新的错误和异常处理框架，更容易扩展</span></li> 
 <li><code>RedisEngine</code><span> </span>支持使用<span> </span><code>deleteAsync()</code>。</li> 
 <li>RedisEngine 现在支持使用 deleteAsync() 进行快速删除。</li> 
 <li>bin/cake 路线现在突出显示路线模板中的碰撞。</li> 
 <li>添加了<span> </span><span style="color:#24292f"><code>Controller::viewClasses()</code></span>， 此方法使控制器能够控制可以响应的内容类型。</li> 
 <li>视图类可以定义静态方法 contentType() 来参与内容类型协商。</li> 
 <li>添加了 Query::expr() ，作为 Query::newExpr() 的替代方法。</li> 
 <li>QueryExpression::case() 构建器现在支持 then() 和 else() 的表达式推断类型。</li> 
 <li>BaseApplication::handle() 现在将 $request 添加到服务容器中。</li> 
 <li>HttpsEnforcerMiddleware 现在有一个 hsts 选项，允许配置 Strict-Transport-Security 标头。</li> 
 <li>TreeBehavior 支持在删除节点时触发 ORM 回调。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcakephp%2Fcakephp%2Freleases%2Ftag%2F4.4.0" target="_blank">https://github.com/cakephp/cakephp/releases/tag/4.4.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            