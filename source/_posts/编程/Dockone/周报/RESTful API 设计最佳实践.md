
---
title: 'RESTful API 设计最佳实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9072'
author: Dockone
comments: false
date: 2021-04-21 12:10:36
thumbnail: 'https://picsum.photos/400/300?random=9072'
---

<div>   
<br><h3>简介</h3>RESTful API 是目前最流行的API设计规范，它用于Web数据接口的设计。它允许包括浏览器在内的各种客户端与服务器进行通信。因此正确是设计我们的RESTful是相当重要的！我们的API必须安全、高性能、同时易于使用。<br>
<br>在本文我们将探讨如何设计出易于使用并且安全快速的的RESTful API。<br>
<br>RESTful API 即是基于Rest构建的API。那么在开始之前，我们先来看看 REST 是什么？<br>
<br>REST与技术无关，它代表的是一种软件架构风格，REST它是Representational State Transfer的简称，中文的含义是: 表现层状态转移（转移：通过HTTP动词实现）。即URL定位资源，HTTP动词操作（GET，POST，PUT，DELETE）描述操作。<br>
<h3>确保接受并响应JSON数据格式</h3>RESTful API应该接受JSON格式的请求，并返回的响应体也应该是JSON格式的。JSON是一种数据传输标准，主流编程语言几乎都能很好的支持它。同时在浏览器中我们的JavaScript也能很轻松方便的操作这些数据。所以，以JSON格式编写的 RESTful API 具有简单、易读、易用的特点。<br>
<br>为了确保当我们的RESTful API服务使用JSON格式响应，我们应该将其响应头的<code class="prettyprint">Content-Type</code>设置为<code class="prettyprint">application/json</code>。<br>
<br>让我们来看一个接收JSON数据并返回JSON数据的API示例。本示例使用Node.js的<a href="https://expressjs.com/">Express</a>框架。我们使用了<a href="https://www.npmjs.com/package/body-parser">body-parser</a>中间件来解析JSON请求体，然后使用<code class="prettyprint">res.json</code>返回传入的JSON对象。<br>
<pre class="prettyprint">const express = require('express');<br>
const bodyParser = require('body-parser');<br>
<br>
const app = express();<br>
<br>
app.use(bodyParser.json());<br>
<br>
app.post('/', (req, res) => &#123;<br>
res.json(req.body);<br>
&#125;);<br>
<br>
app.listen(3000, () => console.log('server started'));<br>
</pre><br>
在本示例中<code class="prettyprint">bodyParser.json()</code>将JSON请求体的字符解析为JavaScript对象，然后将其分配给该<code class="prettyprint">req.body</code>对象。<br>
<h3>在API路径中使用名词代替动词</h3>RESTful API是面向资源的API，HTTP动词操作（GET，POST，PUT，DELETE）描述操作。<br>
<br>我们不应该在URL路径中使用动词。我们应该使用要操作的实体的名词作为路径名。因为我们的HTTP请求方法本身就是动词，就能描述要进行的操作，如常见的方法包括 GET，POST，PUT和 DELETE，这些请求方法即可完成<a href="https://en.wikipedia.org/wiki/Create,_read,_update_and_delete">CRUD</a>。<br>
<ul><li>GET 检索资源。</li><li>POST 将新数据提交到服务器。</li><li>PUT 更新现有数据。</li><li>DELETE 删除数据。</li></ul><br>
<br>例如，我们有个文章（/articles/）资源。我们对其进行CRUD的RESTful API如下：<br>
<ul><li>使用GET <code class="prettyprint">/articles/</code>来获取文章列表</li><li>使用POST <code class="prettyprint">/articles/</code>添加新文章</li><li>使用PUT <code class="prettyprint">/articles/:id</code>更新给定ID的文章</li><li>使用DELETE <code class="prettyprint">/articles/:id</code>删除具有给定ID的文章</li></ul><br>
<br>我们通过Express来实现上面这个增删改查的例子，如下所示：<br>
<pre class="prettyprint">const express = require('express');<br>
const bodyParser = require('body-parser');<br>
<br>
const app = express();<br>
<br>
app.use(bodyParser.json());<br>
<br>
app.get('/articles', (req, res) => &#123;<br>
const articles = [];<br>
// code to retrieve an article...<br>
res.json(articles);<br>
&#125;);<br>
<br>
app.post('/articles', (req, res) => &#123;<br>
// code to add a new article...<br>
res.json(req.body);<br>
&#125;);<br>
<br>
app.put('/articles/:id', (req, res) => &#123;<br>
const &#123; id &#125; = req.params;<br>
// code to update an article...<br>
res.json(req.body);<br>
&#125;);<br>
<br>
app.delete('/articles/:id', (req, res) => &#123;<br>
const &#123; id &#125; = req.params;<br>
// code to delete an article...<br>
res.json(&#123; deleted: id &#125;);<br>
&#125;);<br>
<br>
app.listen(3000, () => console.log('server started'));<br>
</pre><br>
在上面的示例代码中，我们定义了API来操作文章（articles）资源。如我们所见，API URL路径中使用的都是名词，作为动词的请求方法说明了API的操作意图。<br>
<h3>使用名词复数</h3>我们应该使用复数名词来命名集合。<br>
<br>通常，我们想要取得的数据都是一个集合，而不是单个项目。同时数据库中的表也是具有多个条目的。所以我们的API 也应该使用复数名词，这样更合乎情理。<br>
<h3>嵌套分层的资源对象</h3>在处理嵌套资源的API时，应该将嵌套资源附加到父资源的路径之后。<br>
<br>例如一个文章有评论列表，获取某个文章的评论列表的API则为：<br>
<pre class="prettyprint">GET /articles/:articleId/comments<br>
</pre><br>
我们可以使用express来做个示范：<br>
<pre class="prettyprint">const express = require('express');<br>
const bodyParser = require('body-parser');<br>
<br>
const app = express();<br>
<br>
app.use(bodyParser.json());<br>
<br>
app.get('/articles/:articleId/comments', (req, res) => &#123;<br>
const &#123; articleId &#125; = req.params;<br>
const comments = [];<br>
// code to get comments by articleId<br>
res.json(comments);<br>
&#125;);<br>
<br>
<br>
app.listen(3000, () => console.log('server started'));<br>
</pre><br>
<h3>使用标准的http状态码</h3>为了消除API server发生错误时用户的困惑，我们应该优雅地处理错误，并返回指示发生了具体错误的HTTP响应代码以及明确的错误信息。这可以很好的为API使用者提供了足够的信息来了解所发生的问题。<br>
<br>常见的错误HTTP状态代码包括：<br>
<ul><li><code class="prettyprint">400</code>错误的请求 – 这意味着客户端输入验证失败。</li><li><code class="prettyprint">401</code>未经授权 - 这意味着用户无权访问资源。通常在用户未通过身份验证时返回。</li><li><code class="prettyprint">403</code>禁止访问 - 表示用户已通过身份验证，但不允许其访问资源。</li><li><code class="prettyprint">404</code> Not Found – 表示找不到资源。</li><li><code class="prettyprint">500</code>内部服务器错误 – 这是一般服务器错误。它可能不应该明确地抛出。</li><li><code class="prettyprint">502</code><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502">错误的网关</a>  - 这表明来自上游服务器的无效响应。</li><li><code class="prettyprint">503</code>服务不可用 – 这表示服务器端发生了意外情况（可能是服务器过载，系统某些部分发生故障等）。</li></ul><br>
<br>我们应该抛出服务错误相对应的错误码。例如，如果我们要拒绝客服端发起的请求，则应在Express API中返回如下所示的<code class="prettyprint">400</code>响应：<br>
<pre class="prettyprint">const express = require('express');<br>
const bodyParser = require('body-parser');<br>
<br>
const app = express();<br>
<br>
// existing users<br>
const users = [<br>
&#123; email: 'abc@foo.com' &#125;<br>
]<br>
<br>
app.use(bodyParser.json());<br>
<br>
app.post('/users', (req, res) => &#123;<br>
const &#123; email &#125; = req.body;<br>
const userExists = users.find(u => u.email === email);<br>
if (userExists) &#123;<br>
return res.status(400).json(&#123; error: 'User already exists' &#125;)<br>
&#125;<br>
res.json(req.body);<br>
&#125;);<br>
<br>
<br>
app.listen(3000, () => console.log('server started'));<br>
</pre><br>
在上面的示例中，用户尝试创建一个已经存在的user，将获得400响应状态代码，并带有一条<code class="prettyprint">'User already exists'</code>的错误消息，让用户知道该用户已经存在。利用这些信息，用户可以通过使用其他email来创建新用户。<br>
<br>通常错误代码需要附带明确错误消息，以便用户有足够的信息来了解自己遇到了什么问题。<br>
<br>每当我们的API未成功调用时，都应通过发送明确的错误信息来帮助用户采取纠正措施来完成操作。<br>
<h3>添加过滤，排序和分页功能</h3>通常我们的数据都会非常庞大。我们不可能一次全部返回，这会非常慢也可能导致系统崩溃。因此，我们需要有过滤，分页数据的方式。过滤和分页都可以通过减少消耗服务器资源来提高性能。这些功能相当基础且重要。<br>
<br>分页、过滤、排序查询都功能都应该使用查询参数来实现。如：<br>
<pre class="prettyprint">/employees?page=1&pageSize=10&firstName=Xing<br>
</pre><br>
下面这就是一个带有过滤查询的示例：<br>
<pre class="prettyprint">const express = require('express');<br>
const bodyParser = require('body-parser');<br>
<br>
const app = express();<br>
<br>
// employees data in a database<br>
const employees = [<br>
&#123; firstName: 'Jane', lastName: 'Smith', age: 20 &#125;,<br>
//...<br>
&#123; firstName: 'John', lastName: 'Smith', age: 30 &#125;,<br>
&#123; firstName: 'Mary', lastName: 'Green', age: 50 &#125;,<br>
]<br>
<br>
app.use(bodyParser.json());<br>
<br>
app.get('/employees', (req, res) => &#123;<br>
const &#123; firstName, lastName, age &#125; = req.query;<br>
let results = [...employees];<br>
if (firstName) &#123;<br>
results = results.filter(r => r.firstName === firstName);<br>
&#125;<br>
<br>
if (lastName) &#123;<br>
results = results.filter(r => r.lastName === lastName);<br>
&#125;<br>
<br>
if (age) &#123;<br>
results = results.filter(r => +r.age === +age);<br>
&#125;<br>
res.json(results);<br>
&#125;);<br>
<br>
app.listen(3000, () => console.log('server started'));<br>
</pre><br>
<h3>保持良好的安全意识</h3>客户端和服务器之间的大多数通信应该是私有的。因此，必须使用SSL/TLS进行安全保护。现在加载SSL成本是相当低的。我们没有理由不使用它。<br>
<br>同时，不同的用户具有不同的数据访问权限。例如，普通用户不应该能够访问其他用户的信息。他们也不应该能够访问管理员的数据。<br>
<h3>适当缓存数据以提高性能</h3>可以适当添加缓存服务，从缓存中返回常用数据，而不是每次都从数据库去读取。缓存的好处是可以更快地获取数据，但是也让我们获取最新的数据变得复杂。缓存方式有很多如：Redis、内存缓存（in-memory cache）等等，我们应该根据自己的应用具体情况来选择是不是该用缓存，使用哪种缓存机制。<br>
<br>这儿我们来使用Express的<a href="https://www.npmjs.com/package/apicache">apicache</a>中间件来实现一个简单的内存缓存：<br>
<pre class="prettyprint">const express = require('express');<br>
const bodyParser = require('body-parser');<br>
const apicache = require('apicache');<br>
const app = express();<br>
let cache = apicache.middleware;<br>
app.use(cache('5 minutes'));<br>
<br>
// employees data in a database<br>
const employees = [<br>
&#123; firstName: 'Jane', lastName: 'Smith', age: 20 &#125;,<br>
//...<br>
&#123; firstName: 'John', lastName: 'Smith', age: 30 &#125;,<br>
&#123; firstName: 'Mary', lastName: 'Green', age: 50 &#125;,<br>
]<br>
<br>
app.use(bodyParser.json());<br>
<br>
app.get('/employees', (req, res) => &#123;<br>
res.json(employees);<br>
&#125;);<br>
<br>
app.listen(3000, () => console.log('server started'));<br>
</pre><br>
<h3>版本化我们的API</h3>原则上我们应该尽量让API避免破坏性变更，保持向后兼容。但是经常有些时候破坏性的变更是不可避免的，这时版本化的API就派上用场了。当我们发布了不兼容或重大更改变，则可以将其发布在新版本中的API。<br>
<br>我们通常通过URL来实现版本化，及添加版本号在我们API路径的开头，例如：<code class="prettyprint">api.liuxing.io/v1</code>、<code class="prettyprint">api.liuxing.io/v2</code>。<br>
<br>我们可以在express很简单的实现版本化的RESTful API：<br>
<pre class="prettyprint">const express = require('express');<br>
const bodyParser = require('body-parser');<br>
const app = express();<br>
<br>
app.use(bodyParser.json());<br>
<br>
app.get('/v1/employees', (req, res) => &#123;<br>
const employees = [];<br>
// code to get employees<br>
res.json(employees);<br>
&#125;);<br>
<br>
app.get('/v2/employees', (req, res) => &#123;<br>
const employees = [];<br>
// different code to get employees<br>
res.json(employees);<br>
&#125;);<br>
<br>
app.listen(3000, () => console.log('server started'));<br>
</pre><br>
<h3>总结</h3>设计高质量RESTful API的最重要的一点是遵循Web标准和约定以保持一致性。JSON、SSL/TLS和HTTP状态代码都是现代Web的标准。性能也是重要的考虑因素。我们可以使用分页、缓存等手段来提升性能。可维护性可扩展性也是我们需要考虑的。<br>
<br>原文链接：<a href="https://www.liuxing.io/blog/best-practices-for-restful-api/" rel="nofollow" target="_blank">https://www.liuxing.io/blog/be ... -api/</a>
                                
                                                              
</div>
            