
---
title: 'Mongoose 的 save() 方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7156'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 02:41:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=7156'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与8月更文挑战的第29天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
</blockquote>
<p>Mongoose 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fapi%2Fmodel.html%23model_Model-save" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/api/model.html#model_Model-save" ref="nofollow noopener noreferrer"><code>save()</code> 方法</a>是将文档更改保存到数据库的一种方法。在 Mongoose 中更新文档有几种方法，如：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fapi.html%23document_Document-update" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/api.html#document_Document-update" ref="nofollow noopener noreferrer"><code>update</code>、<code>updateOne</code></a>。但 <code>save()</code> 是功能最齐全的方法。除非有充分理由不更新文档，否则应使用 <code>save()</code> 更新文档。</p>
<h2 data-id="heading-0">使用 <code>save()</code> 进行操作</h2>
<p><code>save()</code> 是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fdocuments.html" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/documents.html" ref="nofollow noopener noreferrer">Mongoose documents</a> 上的一个方法。<code>save()</code> 方法是异步的，因此它返回一个可以 <code>await</code> 执行的 Promise。</p>
<p>当您使用 <code>new</code> 创建 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fmodels.html" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/models.html" ref="nofollow noopener noreferrer">Mongoose 模型</a>的实例时，调用 <code>save()</code> 会使 Mongoose 插入一个新文档。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Person = mongoose.model(<span class="hljs-string">'Person'</span>, Schema(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">rank</span>: <span class="hljs-built_in">Number</span>
&#125;))
​
<span class="hljs-keyword">const</span> doc = <span class="hljs-keyword">new</span> Person(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'O.O'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
&#125;)
<span class="hljs-comment">// 插入一个 name = O.O, age = 18 的新文档</span>
<span class="hljs-keyword">await</span> doc.save()
​
<span class="hljs-keyword">const</span> person = <span class="hljs-keyword">await</span> Person.findOne()
<span class="hljs-built_in">console</span>.log(person.name) <span class="hljs-comment">// O.O</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果从数据库加载现有文档并对其进行修改，则 <code>save()</code> 会更新现有文档。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> person = <span class="hljs-keyword">await</span> Person.findOne()
person.name <span class="hljs-comment">// O.O</span>
​
<span class="hljs-comment">// Mongoose 跟踪文档的更改。Mongoose 跟踪您设置的 age 属性，并将更改持久化到数据库中。</span>
person.age = <span class="hljs-number">18</span>
<span class="hljs-keyword">await</span> person.save()
​
<span class="hljs-comment">// 从数据库加载文档并查看更改</span>
<span class="hljs-keyword">const</span> docs = <span class="hljs-keyword">await</span> Person.find()
​
<span class="hljs-built_in">console</span>.log(docs.length) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(docs[<span class="hljs-number">0</span>].age) <span class="hljs-comment">// 18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Mongoose 的更改跟踪根据您对文档所做的更改向 MongoDB 发送最小更新。您可以设置 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fapi%2Fmongoose.html%23mongoose_Mongoose-set" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/api/mongoose.html#mongoose_Mongoose-set" ref="nofollow noopener noreferrer">Mongoose 的调试模式</a>，以查看 Mongoose 发送给 MongoDB 的操作。</p>
<pre><code class="hljs language-js copyable" lang="js">mongoose.set(<span class="hljs-string">'debug'</span>, <span class="hljs-literal">true</span>)
​
person.age = <span class="hljs-number">18</span>
<span class="hljs-comment">// Mongoose: people.updateOne(&#123; _id: ObjectId("...") &#125;, &#123; '$set': &#123; age: 18 &#125; &#125;)</span>
<span class="hljs-keyword">await</span> person.save()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">验证</h2>
<p>Mongoose 在保存之前验证修改后的路径。如果将字段设置为无效值，Mongoose 将在尝试 <code>save()</code> 该文档时抛出错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Person = mongoose.model(<span class="hljs-string">'Person'</span>, Schema(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">Number</span>
&#125;))
​
<span class="hljs-keyword">const</span> doc = <span class="hljs-keyword">await</span> Person.create(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Will Riker'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;)
​
<span class="hljs-comment">// 将 name 设置为无效值是可以的。。。</span>
doc.age = <span class="hljs-string">'lotto'</span>
​
<span class="hljs-comment">// 但尝试 save() 时，文档会出错</span>
<span class="hljs-keyword">const</span> err = <span class="hljs-keyword">await</span> doc.save().catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> err)
err <span class="hljs-comment">// 路径 age 处的值 lotto 的强制转换为数字失败</span>
​
<span class="hljs-comment">// 但是，如果将 age 设置为有效值，则 save() 将成功。</span>
doc.age = <span class="hljs-number">20</span>
<span class="hljs-keyword">await</span> doc.save()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">中间件</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fmiddleware.html" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/middleware.html" ref="nofollow noopener noreferrer">Mongoose 中间件</a>允许您在每次调用 <code>save()</code> 时告诉 Mongoose 执行一个方法。例如，调用 <code>pre('save')</code> 告诉 Mongoose在执行 <code>save()</code> 之前先执行一个方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> schema = Schema(&#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>, <span class="hljs-attr">age</span>: <span class="hljs-built_in">Number</span> &#125;)
schema.pre(<span class="hljs-string">'save'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 在 save 中间件中，this 是正在保存的文档。</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Save'</span>, <span class="hljs-built_in">this</span>.name)
&#125;)
<span class="hljs-keyword">const</span> Person = mongoose.model(<span class="hljs-string">'Person'</span>, schema)
​
<span class="hljs-keyword">const</span> doc = <span class="hljs-keyword">new</span> Person(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'O.O'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;)
​
<span class="hljs-comment">// Save O.O</span>
<span class="hljs-keyword">await</span> doc.save()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似地，<code>post('save')</code> 告诉 Mongoose 在调用 <code>save()</code> 后执行一个方法。例如，您可以将 <code>pre('save')</code> 和 <code>post('save')</code> 组合起来打印 <code>save()</code> 所用的时间。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> schema = Schema(&#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>, <span class="hljs-attr">age</span>: <span class="hljs-built_in">Number</span> &#125;)
schema.pre(<span class="hljs-string">'save'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.$locals.start = <span class="hljs-built_in">Date</span>.now()
&#125;)
schema.post(<span class="hljs-string">'save'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'保存时间为 '</span>, <span class="hljs-built_in">Date</span>.now() - <span class="hljs-built_in">this</span>.$locals.start, <span class="hljs-string">' ms'</span>)
&#125;)
<span class="hljs-keyword">const</span> Person = mongoose.model(<span class="hljs-string">'Person'</span>, schema)
​
<span class="hljs-keyword">const</span> doc = <span class="hljs-keyword">new</span> Person(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'O.O'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;)
​
<span class="hljs-comment">// 保存时间为 12 ms</span>
<span class="hljs-keyword">await</span> doc.save()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>save()</code> 中间件是递归的，因此对父文档调用 <code>save()</code> 也会触发子文档的 <code>save()</code> 中间件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> friendSchema = Schema(&#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>, <span class="hljs-attr">age</span>: <span class="hljs-built_in">Number</span>, <span class="hljs-attr">hobby</span>: <span class="hljs-built_in">String</span> &#125;)
friendSchema.pre(<span class="hljs-string">'save'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Save'</span>, <span class="hljs-built_in">this</span>.hobby)
&#125;)
<span class="hljs-keyword">const</span> schema = Schema(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">friend</span>: friendSchema
&#125;)
<span class="hljs-keyword">const</span> Person = mongoose.model(<span class="hljs-string">'Person'</span>, schema)
​
<span class="hljs-keyword">const</span> doc = <span class="hljs-keyword">new</span> Person(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'O.O'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
  <span class="hljs-attr">friend</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'D.O'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>,
    <span class="hljs-attr">hobby</span>: <span class="hljs-string">'sing'</span>
  &#125;
&#125;)
​
<span class="hljs-comment">// Save sing</span>
<span class="hljs-keyword">await</span> doc.save()
​
doc.friend.hobby = <span class="hljs-string">'dance'</span>
<span class="hljs-comment">// Save dance</span>
<span class="hljs-keyword">await</span> doc.save()
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            