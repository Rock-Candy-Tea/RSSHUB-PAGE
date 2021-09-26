
---
title: '22个最佳实践助你API设计能力更上一层楼'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210921/d7ad35c0dfef7802df2e2e38c4273165.png'
author: Dockone
comments: false
date: 2021-09-26 01:53:11
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210921/d7ad35c0dfef7802df2e2e38c4273165.png'
---

<div>   
<br>【编者的话】为设计REST API而苦恼？不要慌，这里有设计REST API的超实用建议！<br>
<br>曾经因为一个糟糕的API而感到沮丧吗？<br>
<br>在这个微服务的世界里，后端API的一致性设计是必不可少的。<br>
<br>今天，我们将讨论一些可遵循的最佳实践。我们将保持简短和甜蜜——所以系好安全带，出发咯！<br>
<h3>首先介绍一些术语</h3>任何API设计都遵循一种叫做“面向资源设计”的原则<br>
<ul><li><strong>资源</strong>：资源是数据的一部分，例如：<strong>用户</strong></li><li><strong>集合</strong>：一组资源称为集合，例如：<strong>用户列表</strong></li><li><strong>URL</strong>：标识资源或集合的位置，例如：<strong>/user</strong></li></ul><br>
<br><h3>1. 对URL使用kebab-case（短横线小写隔开形式）</h3>例如，如果你想要获得订单列表。<br>
<br>不应该：<br>
<pre class="prettyprint">/systemOrders或/system_orders<br>
</pre><br>
应该：<br>
<pre class="prettyprint">/system-orders<br>
</pre><br>
<h3>2. 参数使用camelCase（驼峰形式）</h3>例如，如果你想从一个特定的商店购买产品。<br>
<br>不应该：<br>
<pre class="prettyprint">/system-orders/&#123;order_id&#125; <br>
</pre><br>
或者：<br>
<pre class="prettyprint">/system-orders/&#123;OrderId&#125; <br>
</pre><br>
应该：<br>
<pre class="prettyprint">/system-orders/&#123;orderId&#125; <br>
</pre><br>
<h3>3. 指向集合的复数名称</h3>如果你想获得系统的所有用户。<br>
<br>不应该：<br>
<pre class="prettyprint">GET /user<br>
</pre><br>
或：<br>
<pre class="prettyprint">GET /User<br>
</pre><br>
应该：<br>
<pre class="prettyprint">GET /users<br>
</pre><br>
<h3>4. URL以集合开始，以标识符结束</h3>如果要保持概念的单一性和一致性。<br>
<br>不应该：<br>
<pre class="prettyprint">GET /shops/:shopId/category/:categoryId/price<br>
</pre><br>
这很糟糕，因为它指向的是一个属性而不是资源。<br>
<br>应该：<br>
<pre class="prettyprint">GET /shops/:shopId/或GET /category/:categoryId<br>
</pre><br>
<h3>5. 让动词远离你的资源URL</h3>不要在URL中使用动词来表达你的意图。相反，使用适当的HTTP方法来描述操作。<br>
<br>不应该：<br>
<pre class="prettyprint">POST /updateuser/&#123;userId&#125; <br>
</pre><br>
或：<br>
<pre class="prettyprint">GET /getusers<br>
</pre><br>
应该：<br>
<pre class="prettyprint">PUT /user/&#123;userId&#125; <br>
</pre> <br>
<h3>6. 对非资源URL使用动词</h3>如果你有一个端点，它只返回一个操作。在这种情况下，你可以使用动词。例如，如果你想要向用户重新发送警报。<br>
<br>应该：<br>
<pre class="prettyprint">POST /alarm/245743/resend<br>
</pre><br>
请记住，这些不是我们的CRUD操作。相反，它们被认为是在我们的系统中执行特定工作的函数。<br>
<h3>7. JSON属性使用camelCase驼峰形式</h3>如果你正在构建一个请求体或响应体为JSON的系统，那么属性名应该使用驼峰大小写。<br>
<br>不应该：<br>
<pre class="prettyprint">&#123;<br>
user_name: "Mohammad Faisal"<br>
user_id: "1"<br>
&#125; <br>
</pre><br>
应该：<br>
<pre class="prettyprint">&#123;<br>
userName: "Mohammad Faisal"<br>
userId: "1"<br>
&#125; <br>
</pre><br>
<h3>8. 监控</h3>RESTful HTTP服务必须实现<code class="prettyprint">/health</code>和<code class="prettyprint">/version</code>和<code class="prettyprint">/metrics</code>API端点。他们将提供以下信息。<br>
<h4>/health</h4>用200 OK状态码响应对<code class="prettyprint">/health</code>的请求。<br>
<h4>/version</h4>用版本号响应对<code class="prettyprint">/version</code>的请求。<br>
<h4>/metrics</h4>这个端点将提供各种指标，如平均响应时间。<br>
<br>也强烈推荐使用<code class="prettyprint">/debug</code>和<code class="prettyprint">/status</code>端点。<br>
<h3>9. 不要使用table_name作为资源名</h3>不要只使用表名作为资源名。从长远来看，这种懒惰是有害的。<br>
<br>不应该：<br>
<pre class="prettyprint">product_order<br>
</pre><br>
应该：<br>
<pre class="prettyprint">product-orders<br>
</pre><br>
这是因为公开底层体系结构不是你的目的。<br>
<h3>10. 使用API设计工具</h3>有许多好的API设计工具用于编写好的文档，例如：<br>
<ul><li>API蓝图：<a href="https://apiblueprint.org/" rel="nofollow" target="_blank">https://apiblueprint.org/</a></li><li>Swagger：<a href="https://swagger.io/" rel="nofollow" target="_blank">https://swagger.io/</a></li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210921/d7ad35c0dfef7802df2e2e38c4273165.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210921/d7ad35c0dfef7802df2e2e38c4273165.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
拥有良好而详细的文档可以为API使用者带来良好的用户体验。<br>
<h3>11. 使用简单序数作为版本</h3>始终对API使用版本控制，并将其向左移动，使其具有最大的作用域。版本号应该是v1，v2等等。<br>
<br>应该：<a href="http://api.domain.com/v1/shops/3/products" rel="nofollow" target="_blank">http://api.domain.com/v1/shops/3/products</a><br>
<br>始终在API中使用版本控制，因为如果API被外部实体使用，更改端点可能会破坏它们的功能。<br>
<br><h3>12. 在你的响应体中包括总资源数</h3>如果API返回一个对象列表，则响应中总是包含资源的总数。你可以为此使用total属性。<br>
<br>不应该：<br>
<pre class="prettyprint">&#123;<br>
users: [ <br>
 ...<br>
]<br>
&#125; <br>
</pre><br>
应该：<br>
<pre class="prettyprint">&#123;<br>
users: [ <br>
 ...<br>
],<br>
total: 34<br>
&#125; <br>
</pre><br>
<h3>13. 接受limit和offset参数</h3>在GET操作中始终接受limit和offset参数。<br>
<br>应该：<br>
<pre class="prettyprint">GET /shops?offset=5&limit=5<br>
</pre><br>
这是因为它对于前端的分页是必要的。<br>
<h3>14. 获取字段查询参数</h3>返回的数据量也应该考虑在内。添加一个<code class="prettyprint">fields</code>参数，只公开API中必需的字段。<br>
<br>例子：<br>
<br>只返回商店的名称，地址和联系方式。<br>
<pre class="prettyprint">GET /shops?fields=id,name,address,contact<br>
</pre><br>
在某些情况下，它还有助于减少响应大小。<br>
<h3>15. 不要在URL中通过认证令牌</h3>这是一种非常糟糕的做法，因为url经常被记录，而身份验证令牌也会被不必要地记录。<br>
<br>不应该：<br>
<pre class="prettyprint">GET /shops/123?token=some_kind_of_authenticaiton_token<br>
</pre><br>
相反，通过头部传递它们：<br>
<pre class="prettyprint">Authorization: Bearer xxxxxx, Extra yyyyy<br>
</pre><br>
此外，授权令牌应该是短暂有效期的。<br>
<h3>16. 验证内容类型</h3>服务器不应该假定内容类型。例如，如果你接受<code class="prettyprint">application/x-www-form-urlencoded</code>，那么攻击者可以创建一个表单并触发一个简单的POST请求。<br>
<br>因此，始终验证内容类型，如果你想使用默认的内容类型，请使用：<br>
<pre class="prettyprint">content-type: application/json<br>
</pre><br>
<br><h3>17. 对CRUD函数使用HTTP方法</h3>HTTP方法用于解释CRUD功能。<br>
<br><code class="prettyprint">GET</code>：检索资源的表示形式。<br>
<br><code class="prettyprint">POST</code>：创建新的资源和子资源。<br>
<br><code class="prettyprint">PUT</code>：更新现有资源。<br>
<br><code class="prettyprint">PATCH</code>：更新现有资源，它只更新提供的字段，而不更新其他字段。<br>
<br><code class="prettyprint">DELETE</code>：删除已存在的资源。<br>
<h3>18. 在嵌套资源的URL中使用关系</h3>以下是一些实际例子：<br>
<ul><li><code class="prettyprint">GET /shops/2/products</code>：从shop 2获取所有产品的列表。</li><li><code class="prettyprint">GET /shops/2/products/31</code>：获取产品31的详细信息，产品31属于shop 2。</li><li><code class="prettyprint">DELETE /shops/2/products/31</code>：应该删除产品31，它属于商店2。</li><li><code class="prettyprint">PUT /shops/2/products/31</code>：应该更新产品31的信息，只在resource-URL上使用PUT，而不是集合。</li><li><code class="prettyprint">POST /shops</code>：应该创建一个新的商店，并返回创建的新商店的详细信息。在集合url上使用POST。</li></ul><br>
<br><h3>19. CORS（跨源资源共享）</h3>一定要为所有面向公共的API支持CORS（跨源资源共享）头部。<br>
<br>考虑支持CORS允许的“*”来源，并通过有效的OAuth令牌强制授权。<br>
<br>避免将用户凭证与原始验证相结合。<br>
<h3>20. 安全</h3>在所有端点、资源和服务上实施HTTPS（tls加密）。<br>
<br>强制并要求所有回调url、推送通知端点和webhooks使用HTTPS。<br>
<h3>21. 错误</h3>当客户端向服务发出无效或不正确的请求，或向服务传递无效或不正确的数据，而服务拒绝该请求时，就会出现错误，或者更具体地说，出现服务错误。<br>
<br>例子包括无效的身份验证凭证、不正确的参数、未知的版本id等。<br>
<ul><li>当由于一个或多个服务错误而拒绝客户端请求时，一定要返回4xx HTTP错误代码。</li><li>考虑处理所有属性，然后在单个响应中返回多个验证问题。</li></ul><br>
<br><h3>22. 黄金法则</h3>如果您对API格式的决定有疑问，这些黄金规则可以帮助我们做出正确的决定。<br>
<ul><li>扁平比嵌套好。</li><li>简单胜于复杂。</li><li>字符串比数字好。</li><li>一致性比定制更好。</li></ul><br>
<br>就是这样——如果你已经走到了这一步，恭喜你！希望你学到了一些东西。<br>
<br>希望你度过美好的一天！<br>
<br><strong>原文链接：<a href="https://betterprogramming.pub/22-best-practices-to-take-your-api-design-skills-to-the-next-level-65569b200b9?gi=a68a39522ef8">22 Best Practices to Take Your API Design Skills to the Next Level</a></strong><br>
<br><strong>译者</strong>：Mr.lzc，软件工程师、DevOpsDays、HDZ深圳核心组织者，目前供职于华为，从事云计算工作，专注于K8s、微服务领域。
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            