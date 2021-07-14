
---
title: 'MongoDB的基础操作'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6536'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 04:00:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=6536'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1 数据库\集合操作</h1>
<h2 data-id="heading-1">1.1 创建数据库</h2>
<p><strong>语法</strong>：<code>use DATABASE_NAME</code><br>
<strong>说明</strong>：切换到指定的数据库，若数据库不存在，则创建以该名称命名的数据库<br>
<strong>实例</strong>：创建一个名为socialmedia的数据库</p>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">use socialmedia
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意，此时由于该数据库为空，因此不会显示在数据库列表中。</p>
<h2 data-id="heading-2">1.2 创建集合</h2>
<p><strong>语法</strong>：<code>db.createCollection(name, options)</code><br>
<strong>说明</strong>：</p>
<ul>
<li>name: 所创建的集合名称</li>
<li>options: 指定有关内存大小，暂时了解即可</li>
</ul>
<p><strong>实例</strong>：在socialmedia的数据库中创建名为douyin和bilibili的集合</p>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.createCollection("douyin")
db.createCollection("bilibili")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时再输入<code>show collections</code>，可以查看该数据库中所有的集合；输入<code>show dbs</code>也可以顺利地在数据库列表中查看到新建的数据库。</p>
<h2 data-id="heading-3">1.3 删除集合</h2>
<p><strong>语法</strong>：<code>db.collection.drop()</code><br>
<strong>实例</strong>：将socialmedia的数据库中的bilibili集合删除</p>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.bilibili.drop()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时再输入<code>show collections</code>，可以看到集合bilibili已被删除</p>
<h2 data-id="heading-4">1.4 删除数据库</h2>
<p><strong>语法</strong>：<code>db.dropDatabase()</code><br>
<strong>实例</strong>：删除socialmedia数据库</p>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">use socialmedia
db.dropDatabase()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时再输入<code>show dbs</code>，可以看到数据库socialmedia已被删除</p>
<h1 data-id="heading-5">2 文档的增删改</h1>
<h2 data-id="heading-6">2.1 插入文档</h2>
<p><strong>语法</strong>：</p>
<ol>
<li>insertOne()方法，插入一个文档</li>
</ol>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.collection.insertOne(
    < document > ,
    &#123;
        writeConcern: < document > 
    &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>insertMany()方法，插入多个文档</li>
</ol>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.collection.insertMany(
    [ < document1 > , < document2 > , ...],
    &#123;
        writeConcern: < document > ,
        ordered: < boolean > 
    &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>insert()方法，是前两者方法的结合，但推荐用前两种方法，因为具有较好的可读性~</li>
</ol>
<p><strong>说明</strong>：<br>
如果插入文档到一个不存在的集合，MongoDB则会自动创建和命名该集合，再插入文档。</p>
<ul>
<li>document：所插入的文档</li>
<li>writeConcern：写入策略，暂时了解即可</li>
<li>ordered：指定是否按顺序写入</li>
</ul>
<p><strong>实例</strong>：在socialmedia库的douyin集合插入多个文档</p>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.douyin.insertMany(
    [
        &#123;
            "aweme_id": 115615646865,
            "aweme_name": "蜜雪冰城甜蜜蜜",
            "likes": 555,
            "follower": 3
        &#125;,
        &#123;
            "aweme_id": 11561564565,
            "aweme_name": "105度的热爱",
            "likes": 5545,
            "follower": 24
        &#125;,
        &#123;
            "aweme_id": 115615325565,
            "aweme_name": "三句话让男人为我花18w",
            "likes": 5545,
            "follower": 45
        &#125;,
        &#123;
            "aweme_id": 11561534265,
            "aweme_name": "套马杆",
            "likes": 666,
            "follower": 45
        &#125;
    ]
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时再输入<code>db.douyin.find()</code>，可以查看到该集合中的所有文档。</p>
<h2 data-id="heading-7">2.2 更新文档</h2>
<p><strong>语法</strong>：</p>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.collection.update(
    < query > ,
    < update > ,
    &#123;
        upsert: < boolean > ,
        multi: < boolean > ,
        writeConcern: < document > 
    &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>说明</strong>：</p>
<ul>
<li>query: update的查询条件</li>
<li>update: update对象的更新操作</li>
<li>upsert: 若不存在update的对象，是否插入新数据，默认为不插入</li>
<li>multi: 是否更新找到的所有符合条件的记录，默认仅更新找到的第一条数据</li>
<li>writeConcern :抛出异常的级别</li>
</ul>
<p><strong>实例</strong>：将刚才插入的4条数据中所有"follower"=45的文档中的"aweme_id"改为88888888</p>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.douyin.update(
    &#123;"follower": 45&#125;,
    &#123;$set: &#123;"aweme_id": 88888888&#125;&#125;,
    &#123;multi: true&#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时再输入<code>db.douyin.find()</code>，可以看到数据已经更新，如果不写<code>&#123;multi:true&#125;</code>，那么MongoDB就只会更新找到的第一条数据，需要注意~</p>
<h2 data-id="heading-8">2.3 删除文档</h2>
<p><strong>语法</strong>：</p>
<ol>
<li>deleteOne()方法，只删除一个符合条件的文档</li>
</ol>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.collection.deleteOne(
    < filter > ,
    &#123;
        writeConcern: < document > ,
        collation: < document > 
    &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>deleteMany()方法，删除所有符合条件的文档</li>
</ol>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.collection.deleteMany(
    < filter > ,
    &#123;
        writeConcern: < document > ,
        collation: < document > 
    &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>remove()方法，实质上是前两者方法的结合，多出一个justOne参数来控制只删除一个或者全删，但推荐使用前两种方法以提升代码的可读性~</li>
</ol>
<p><strong>说明</strong>：</p>
<ul>
<li>filter: 过滤文档的条件</li>
<li>writeConcern: 抛出异常的级别</li>
<li>collation: 指定用于操作的collation</li>
</ul>
<p><strong>实例</strong>：删除douyin集合中"aweme_id"=8888888的所有文档</p>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.douyin.deleteMany(&#123;
    "aweme_id": 88888888
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时再输入<code>db.douyin.find()</code>，可以看到符合条件的文档已被删除</p>
<h1 data-id="heading-9">3 文档查询</h1>
<h2 data-id="heading-10">3.1 find()方法</h2>
<p><strong>语法</strong>：<code>db.collection.find(query, projection)</code><br>
<strong>说明</strong>：</p>
<ul>
<li>query：使用查询操作符指定查询条件，若不指定查询条件则用&#123;&#125;代替</li>
<li>projection：指定返回的键，该参数有两种模式：</li>
</ul>
<ol>
<li>在inclusion模式中，输入格式例如&#123;title: 1&#125;，用1来表示要返回的字段，不需要返回的字段不用写；</li>
<li>在exclusion模式中，输入格式例如&#123;title: 0&#125;，用0来表示不需要返回的字段，除此以外的字段都会返回；</li>
</ol>
<ul>
<li>唯一主键<code>_id</code>默认返回，需要主动指定 <code>_id: 0</code>才会隐藏主键。</li>
</ul>
<h2 data-id="heading-11">3.2 AND和OR条件</h2>
<p><strong>语法</strong>：</p>
<ol>
<li>AND条件</li>
</ol>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.collection.find(&#123;
    key1: value1,
    key2: value2
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>OR条件</li>
</ol>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.collection.find(
    &#123;
        $or: [
            &#123;key1: value1&#125;,
            &#123;key2: value2&#125;
        ]
    &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>说明</strong>：</p>
<ul>
<li>AND条件仅需要传入多个键值对，用逗号隔开即可</li>
<li>OR条件则需要使用关键字<code>$or</code>，将键值对以数组的方式传入</li>
</ul>
<h2 data-id="heading-12">3.3 条件操作符</h2>















































<table><thead><tr><th>条件</th><th>操作符</th><th>MongoDB语法</th><th>SQL语法</th></tr></thead><tbody><tr><td>等于（数值判断）</td><td>/</td><td>db.collection.find(&#123;key: value&#125;)</td><td>where key = value</td></tr><tr><td>小于</td><td>$lt</td><td>db.collection.find(&#123;key: &#123;$lt: value&#125;&#125;)</td><td>where key < value</td></tr><tr><td>小于等于</td><td>$lte</td><td>db.collection.find(&#123;key: &#123;$lte: value&#125;&#125;)</td><td>where key <= value</td></tr><tr><td>大于</td><td>$gt</td><td>db.collection.find(&#123;key: &#123;$gt: value&#125;&#125;)</td><td>where key > value</td></tr><tr><td>大于等于</td><td>$gte</td><td>db.collection.find(&#123;key: &#123;$gte: value&#125;&#125;)</td><td>where key >= value</td></tr><tr><td>不等于</td><td>$ne</td><td>db.collection.find(&#123;key: &#123;$ne: value&#125;&#125;)</td><td>where key != value</td></tr></tbody></table>
<h2 data-id="heading-13">3.4 其他方法</h2>
<h3 data-id="heading-14">3.4.1 limit()方法</h3>
<p><strong>语法</strong>：<code>db.collection.find().limit(number)</code><br>
<strong>说明</strong>：在符合查询结果的文档中，显示number条文档。</p>
<h3 data-id="heading-15">3.4.2 skip()方法</h3>
<p><strong>语法</strong>：<code>db.collection.find().skip(number) </code><br>
<strong>说明</strong>：在符合查询结果的文档中，先跳过number条文档后，再显示后续文档。</p>
<h3 data-id="heading-16">3.4.3 sort()方法</h3>
<p><strong>语法</strong>：<code>db.collection.find().sort(&#123;KEY:1&#125;)</code><br>
<strong>说明</strong>：在符合查询结果的文档中，对指定字段进行排序，并使用1和-1来指定排序方式，其中1为升序排列，而 -1是降序排列。</p>
<h2 data-id="heading-17">3.5 举个栗子</h2>
<ol>
<li>向socialmedia数据库的bilibili集合中插入若干条文档</li>
</ol>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">use socialmedia
db.bilibili.insertMany([
    &#123;"aweme_id": 115615646865,"aweme_name": "蜜雪冰城甜蜜蜜","likes": 555,"follower": 3&#125;,
    &#123;"aweme_id": 11561564565,"aweme_name": "105度的热爱","likes": 5545,"follower": 24&#125;,
    &#123;"aweme_id": 115615325565,"aweme_name": "三句话让男人为我花18w","likes": 5545,"follower": 45&#125;,
    &#123;"aweme_id": 11561534265,"aweme_name": "套马杆","likes": 666,"follower": 56&#125;,
    &#123;"aweme_id": 115615352525,"aweme_name": "A","likes": 67,"follower": 35&#125;,
    &#123;"aweme_id": 11561453434534,"aweme_name": "B","likes": 65646,"follower": 70&#125;,
    &#123;"aweme_id": 117987978975,"aweme_name": "C","likes": 666,"follower": 80&#125;
])
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>查询"likes"大于1000且小于10000或者"follower"不等于70和3,返回"likes"和"aweme_name"字段，不显示_id，查询结果按"likes"降序排列，跳过第1条文档且仅显示4条文档</li>
</ol>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.bilibili.find(
    &#123;$or: [
        &#123;likes: &#123;$gt: 1000, $lt: 10000&#125;&#125;, 
        &#123;follower: &#123;$ne: 70, $ne: 3&#125;&#125;
        ]
    &#125;, 
    &#123;likes: 1,aweme_name: 1,_id: 0&#125;
).sort(&#123;likes: -1&#125;).skip(1).limit(4)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-18">4 聚合查询</h1>
<h2 data-id="heading-19">4.1 aggregate()方法</h2>
<ul>
<li>MongoDB的聚合函数就是将文档输入处理管道，在管道内完成对文档的操作，最终将文档转换为聚合结果。</li>
<li>自己的理解：aggregate()就像流水线上的一道道工序，大致的流程是从查询文档到计算数据。</li>
</ul>
<p><strong>语法</strong>：<code>db.collection.aggregate(AGGREGATE_OPERATION)</code><br>
<strong>说明</strong>：</p>
<ul>
<li>aggregate()方法需要结合管道操作符一起使用</li>
<li>基本管道操作提供过滤器，其操作类似查询和文档转换，可以修改输出文档的形式</li>
<li>其他管道操作提供了按特定字段对文档进行分组和排序的工具，以及用于聚合数组内容的工具</li>
<li>此外，在管道阶段还可以使用运算符来执行诸如计算平均值或连接字符串之类的任务</li>
</ul>
<h2 data-id="heading-20">4.2 常用的管道操作符</h2>
<p>MongoDB的聚合管道将MongoDB文档在一个管道处理完毕后将结果传递给下一个管道处理，管道操作可以搭配使用，使用多个管道操作符需要以数组的形式传入函数。聚合框架中常用的管道操作符如下：</p>
<ul>
<li>$project：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档</li>
<li>$match：用于过滤数据，只输出符合条件的文档</li>
<li>$limit：用来限制MongoDB聚合管道返回的文档数</li>
<li>$skip：在聚合管道中跳过指定数量的文档，并返回余下的文档</li>
<li>$unwind：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值</li>
<li>$group：将集合中的文档分组，可用于统计结果</li>
<li>$sort：将输入文档排序后输出</li>
</ul>
<h3 data-id="heading-21">4.2.1 $project</h3>
<p>$project的基本格式可以参考find()方法中的projection参数，但是可以利用运算符实现更多功能：</p>













































<table><thead><tr><th>运算符</th><th>功能</th><th>说明</th></tr></thead><tbody><tr><td>$add</td><td>加法</td><td>数值计算</td></tr><tr><td>$subtract</td><td>减法</td><td>数值计算</td></tr><tr><td>$multipy</td><td>乘法</td><td>数值计算</td></tr><tr><td>$divide</td><td>除法</td><td>数值计算</td></tr><tr><td>$mod</td><td>求模</td><td>数值计算</td></tr><tr><td>$concat</td><td>连接</td><td>字符串操作</td></tr><tr><td>$substr</td><td>截取</td><td>字符串操作</td></tr></tbody></table>
<p>除此以外还有处理关系运算和逻辑运算的运算符，其实就是判断大小类型和与或非，特点是返回结果为布尔值。</p>
<p><strong>实例</strong>:</p>
<ol>
<li>在socialmeida库中的xiaohongshu集合中插入一些文档：</li>
</ol>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">use socialmedia
db.xiaohongshu.insertMany([
    &#123;"author": "aaa","aweme_name": "蜜雪冰城甜蜜蜜","likes": 555,"follower": 3&#125;,
    &#123;"author": "bbb","aweme_name": "105度的热爱","likes": 5545,"follower": 24&#125;,
    &#123;"author": "bbb","aweme_name": "三句话让男人为我花18w","likes": 5545,"follower": 45&#125;,
    &#123;"author": "aaa","aweme_name": "套马杆","likes": 666,"follower": 56&#125;,
    &#123;"author": "ccc","aweme_name": "哈哈哈","likes": 67,"follower": 35&#125;,
    &#123;"author": "ccc","aweme_name": "啦啦啦","likes": 65646,"follower": 70&#125;,
    &#123;"author": "bbb","aweme_name": "嘻嘻嘻","likes": 666,"follower": 80&#125;
])
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>拼接"author"和"aweme_name"字段，格式为"author---aweme_name"，并将该字段命名为"A1"，将"likes"和"follower"相加，并将该字段命名为"A2"：</li>
</ol>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.xiaohongshu.aggregate(&#123;
    $project: &#123;
        _id: 0,
        A1: &#123;"$concat": ["$author", "---", "$aweme_name"]&#125;,
        A2: &#123;"$add": ["$likes", "$follower"]&#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">4.2.2 $group</h3>
<p>$group类似于SQL中的<code>group by</code>，可以对数据进行分组聚合，常用运算符如下：</p>

























<table><thead><tr><th>运算符</th><th>功能</th></tr></thead><tbody><tr><td>$sum</td><td>计算总和</td></tr><tr><td>$avg</td><td>计算平均值</td></tr><tr><td>$min</td><td>计算最小值</td></tr><tr><td>$max</td><td>计算最大值</td></tr></tbody></table>
<p><strong>实例</strong>：<br>
沿用上一节的数据，在socialmeida库中的xiaohongshu集合中计算每个author的作品数量和likes平均值</p>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.xiaohongshu.aggregate(&#123;
    $group: &#123;
        _id: "$author",
        "作品数": &#123;$sum: 1&#125;,
        "平均值": &#123;$avg: "$likes"&#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中<code>_id</code>后是需要聚合的字段，该参数可以为null<br>
代码中的<code>&#123;$sum: 1&#125;</code>和SQL中<code>count(*)</code>类似，可以对比着理解</p>
<h3 data-id="heading-23">4.2.3 $match</h3>
<p>$match类似于find()方法中的query参数，仅用于过滤数据。<br>
<strong>实例</strong>：<br>
沿用上一节的数据，在socialmeida库中的xiaohongshu集合中查询follower大于50的"aweme_name"。</p>
<pre><code class="hljs language-mongodb copyable" lang="mongodb">db.xiaohongshu.aggregate([
    &#123;$project: &#123;_id: 0, aweme_name: 1, follower: 1&#125;&#125;,
    &#123;$match: &#123;follower: &#123;$gt: 50&#125;&#125;&#125;
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中利用<code>$project</code>来选择需要显示的字段，再用<code>$match</code>过滤数据，反过来也是可以的~</p></div>  
</div>
            