
---
title: 'Mongoose 唯一索引（unique）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6425'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 23:10:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=6425'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与8月更文挑战的第31天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
</blockquote>
<p>Mongoose 的唯一索引 <code>unique</code> 选项都作用是，对于给定的路径，每个文档必须具有唯一的值。例如，下面是如何告诉 Mongoose 用户的 <code>email</code> 必须是唯一的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mongoose = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mongoose'</span>)
​
<span class="hljs-keyword">const</span> userSchema = <span class="hljs-keyword">new</span> mongoose.Schema(&#123;
  <span class="hljs-attr">email</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">unique</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// email 必须是唯一的</span>
  &#125;
&#125;);
<span class="hljs-keyword">const</span> User = mongoose.model(<span class="hljs-string">'User'</span>, userSchema)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果您尝试使用相同的 <code>name</code> 创建两个用户，您将得到一个重复密钥错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 抛出 MongoError:E11000 重复密钥错误集合</span>
<span class="hljs-keyword">await</span> User.create([
  &#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test@163.com'</span> &#125;,
  &#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test2@163.com'</span> &#125;
])
​
<span class="hljs-keyword">const</span> doc = <span class="hljs-keyword">new</span> User(&#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test@google.com'</span> &#125;)
<span class="hljs-comment">// 抛出 MongoError:E11000 重复密钥错误集合</span>
<span class="hljs-keyword">await</span> doc.save()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更新还可能引发重复的密钥错误。例如，如果您创建了一个具有唯一电子邮件地址的用户，然后将其电子邮件地址更新为非唯一值，您将得到相同的错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">await</span> User.create(&#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test2@google.com'</span> &#125;)
​
<span class="hljs-comment">// 抛出 MongoError:E11000 重复密钥错误集合</span>
<span class="hljs-keyword">await</span> User.updateOne(&#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test2@google.com'</span> &#125;, &#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test@google.com'</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0"><code>unique</code> 定义索引，而不是验证器</h2>
<p>一个常见的问题是 <code>unique</code> 选项告诉 Mongoose 定义一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.mongodb.com%2Fmanual%2Fcore%2Findex-unique%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.mongodb.com/manual/core/index-unique/" ref="nofollow noopener noreferrer">唯一索引</a>。这意味着当您使用 <code>validate()</code> 时，Mongoose 不会检查唯一性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">await</span> User.create(&#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test@163.com'</span> &#125;)
​
<span class="hljs-keyword">const</span> doc = <span class="hljs-keyword">new</span> User(&#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test@163.com'</span> &#125;)
<span class="hljs-keyword">await</span> doc.validate() <span class="hljs-comment">// 不会抛出错误</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在编写自动测试时，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fvalidation.html%23the-unique-option-is-not-a-validator" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/validation.html#the-unique-option-is-not-a-validator" ref="nofollow noopener noreferrer"><code>unique</code> 定义索引而不是验证器</a>这一点很重要。如果删除 <code>User</code> 模型所连接的数据库，还将删除 <code>unique</code> 索引，并且可以保存重复的索引。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">await</span> mongoose.connection.dropDatabase()
​
<span class="hljs-comment">// 成功，因为 unique 索引已消失！</span>
<span class="hljs-keyword">await</span> User.create([
  &#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test@163.com'</span> &#125;,
  &#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test@163.com'</span> &#125;
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在生产环境中，通常不会删除数据库，因此这在生产环境中很少成为问题。</p>
<p>编写 Mongoose 测试时，通常建议使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fapi%2Fmodel.html%23model_Model.deleteMany" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/api/model.html#model_Model.deleteMany" ref="nofollow noopener noreferrer"><code>deleteMany()</code></a> 清除测试之间的数据，而不是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fapi%2Fconnection.html%23connection_Connection-dropDatabase" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/api/connection.html#connection_Connection-dropDatabase" ref="nofollow noopener noreferrer"><code>dropDatabase()</code></a>。这样可以确保删除所有文档，而无需清除数据库级别的配置，如索引和排序规则 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fapi%2Fconnection.html%23connection_Connection-dropDatabase" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/api/connection.html#connection_Connection-dropDatabase" ref="nofollow noopener noreferrer"><code>deleteMany()</code> 也比 <code>dropDatabase()</code> 快得多</a>。</p>
<p>但是，如果选择在测试之间删除数据库，则可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmongoosejs.com%2Fdocs%2Fapi.html%23model_Model.syncIndexes" target="_blank" rel="nofollow noopener noreferrer" title="https://mongoosejs.com/docs/api.html#model_Model.syncIndexes" ref="nofollow noopener noreferrer"><code>Model.syncIndexes()</code></a> 方法重新生成所有唯一索引。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">await</span> mongoose.connection.dropDatabase()
​
<span class="hljs-comment">// 重新生成所有索引</span>
<span class="hljs-keyword">await</span> User.syncIndexes()
​
<span class="hljs-comment">// 抛出 MongoError:E11000 重复密钥错误集合</span>
<span class="hljs-keyword">await</span> User.create([
  &#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test@163.com'</span> &#125;,
  &#123; <span class="hljs-attr">email</span>: <span class="hljs-string">'test@163.com'</span> &#125;
])  
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">处理 <code>null</code> 值</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmasteringjs.io%2Ftutorials%2Ffundamentals%2Fnull" target="_blank" rel="nofollow noopener noreferrer" title="https://masteringjs.io/tutorials/fundamentals/null" ref="nofollow noopener noreferrer"><code>null</code></a> 是一个不同的值，您不能保存两个具有 <code>null</code> 的 <code>email</code> 用户。同样，不能保存两个没有 <code>email</code> 属性的用户。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 抛出，因为两个文档都有 undefined</span>
<span class="hljs-keyword">await</span> User.create([
  &#123;&#125;,
  &#123;&#125;
])
​
<span class="hljs-comment">// 抛出，因为两个文档都有 null</span>
<span class="hljs-keyword">await</span> User.create([
  &#123; <span class="hljs-attr">email</span>: <span class="hljs-literal">null</span> &#125;,
  &#123; <span class="hljs-attr">email</span>: <span class="hljs-literal">null</span> &#125;
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一种解决方法是使用 <code>required</code> 属性 ，这将不允许 <code>null</code> 和 <code>undefined</code> 的值存在：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> userSchema = <span class="hljs-keyword">new</span> mongoose.Schema(&#123;
  <span class="hljs-attr">email</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">unique</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// email 必须是唯一的</span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果您需要 <code>email</code> 是唯一的，除非它没有定义，您可以改为定义一个 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.mongodb.com%2Fmanual%2Fcore%2Findex-sparse%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.mongodb.com/manual/core/index-sparse/" ref="nofollow noopener noreferrer">Sparse Indexes（稀疏索引）</a></strong> 在 <code>email</code> 上，如下所示。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> userSchema = <span class="hljs-keyword">new</span> mongoose.Schema(&#123;
  <span class="hljs-attr">email</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-comment">// email 必须是唯一的，除非没有定义</span>
    <span class="hljs-attr">index</span>: &#123;
      <span class="hljs-attr">unique</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">sparse</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">用户友好的重复键错误</h2>
<p>要使 <code>MongoDB E11000</code> 错误消息对用户友好，您可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fmongoose-beautiful-unique-validation" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/mongoose-beautiful-unique-validation" ref="nofollow noopener noreferrer">mongoose-beautiful-unique-validation</a> 包。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> schema = <span class="hljs-keyword">new</span> Schema(&#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span> &#125;)
schema.plugin(<span class="hljs-built_in">require</span>(<span class="hljs-string">'mongoose-beautiful-unique-validation'</span>))
​
<span class="hljs-keyword">const</span> UserModel = mongoose.model(<span class="hljs-string">'User'</span>, schema)
​
<span class="hljs-keyword">const</span> doc = <span class="hljs-keyword">await</span> UserModel.create(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'O.O'</span> &#125;)
​
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-comment">// 尝试创建具有相同 _id 的文档。这将始终失败，因为 MongoDB 集合在 _id 上总是有唯一的索引。</span>
  <span class="hljs-keyword">await</span> UserModel.create(<span class="hljs-built_in">Object</span>.assign(&#123;&#125;, doc.toObject()))
&#125; <span class="hljs-keyword">catch</span> (err) &#123;
  <span class="hljs-comment">// _id 不是唯一的。</span>
  <span class="hljs-built_in">console</span>.log(err.errors[<span class="hljs-string">'_id'</span>].message)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            