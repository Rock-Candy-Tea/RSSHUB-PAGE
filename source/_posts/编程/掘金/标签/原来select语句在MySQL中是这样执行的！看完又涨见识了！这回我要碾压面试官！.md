
---
title: '原来select语句在MySQL中是这样执行的！看完又涨见识了！这回我要碾压面试官！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17153fe0b9f34897acb24a8e11c01e0f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 18:40:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17153fe0b9f34897acb24a8e11c01e0f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>大家好，我是冰河~~</strong></p>
<p>MySQL作为互联网行业使用最多的关系型数据库之一，与其免费、开源的特性是密不可分的。然而，很多小伙伴工作了很多年，只知道使用MySQL进行CRUD操作，这也导致很多小伙伴工作多年后，想跳槽进入大厂，却在面试的时候屡屡碰壁。</p>
<p><strong>问个简单的问题：select语句是如何在MySQL中执行的？</strong> 这也是很多面试官喜欢问的问题，如果你连这个简单的问题都不能回答的话，那就要好好规划下自己的职业生涯了。</p>
<p>好了，今天我们就一起来聊聊select语句是如何在MySQL中执行的。文章的主要内容如下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17153fe0b9f34897acb24a8e11c01e0f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">频繁使用的select语句</h2>
<p>为了更好地贯穿全文，这里先来列举一个最简单的select查询语句，例如：查询user表中id为1001的用户信息，使用下面的SQL语句进行查询。</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">select</span> <span class="hljs-operator">*</span> <span class="hljs-keyword">from</span> <span class="hljs-keyword">user</span> <span class="hljs-keyword">where</span> user_id <span class="hljs-operator">=</span> <span class="hljs-number">1001</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们在MySQL的命令行中输入上述SQL语句时，这条SQL语句到底在MySQL中是如何执行的呢？接下来，我们就以这条SQL语句为例，说说select语句是如何在MySQL中执行的。</p>
<h2 data-id="heading-1">MySQL逻辑架构</h2>
<p>在介绍select语句在MySQL中的执行流程之前，我们先来看看MySQL的逻辑架构，因为任何SQL语句的执行都离不开MySQL逻辑架构的支撑。也就是说，SQL语句在MySQL中的执行流程与MySQL的逻辑架构是密不可分的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1a79a6251554638b7803f6f5db60854~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上图中，我们简单的画了下MySQL的逻辑架构图，并且给出了逻辑分层和每层中各部分的功能。从逻辑上，我们可以将MySQL粗略地分成三层：Server层、存储引擎层和系统文件层，而Server层中又可以分成网络连接层（连接器）和数据服务层（Server层）。</p>
<p>Server层中包含了连接器、查询缓存、分析器、优化器和执行器等MySQL的核心组成部分，另外，在Server层中还包含了所有的内置函数（比如：日期时间函数、加解密函数、聚合函数、数学函数等），存储引擎、触发器、视图等等。</p>
<p>存储引擎层主要负责和系统文件层进行交互，存储引擎层本身是插件式的架构设计，支持InnoDB、MyISAM、Archive、Memory等存储引擎。在MySQL 5.5.5及以后的版本中，MySQL的默认存储引擎是InnoDB。</p>
<p>系统文件层主要负责存储实际的数据，将数据以文件的形式存储到服务器的磁盘上。</p>
<p>接下来，我们就来说说一条select语句在MySQL的逻辑架构的每一部分到底是如何执行的。</p>
<h2 data-id="heading-2">连接器是如何授权的？</h2>
<p>首先，我们先来看看在服务器命令行输入连接MySQL的命令时，MySQL的连接器是如何进行验证的。比如，我们在服务器的命令行输入了如下命令。</p>
<pre><code class="hljs language-sql copyable" lang="sql">mysql <span class="hljs-operator">-</span>ubinghe <span class="hljs-operator">-</span>p
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行“回车”后，输入binghe账户的密码，与MySQL进行连接。此时，连接的过程需要完成经典的TCP握手操作。之后，连接器就开始认证连接的身份是否合法，最直接的就是验证用户名和密码是否正确。</p>
<p>如果用户名或者密码错误，MySQL会提示 <code>Access denied for user  </code>。如果用户名和密码正确，则连接器会到MySQL的权限表中查询当前连接拥有的权限。查询到权限之后，只要这个连接没有断开，则这个连接涉及到的权限操作都会依赖此时查询到的权限。</p>
<p>换句话说，一个用户登录MySQL并成功连接MySQL后，哪怕是管理员对当前用户的权限进行了修改操作，此时只要这个用户没有断开MySQL的连接，就不会受到管理修改权限的影响。管理员修改权限后，只有对新建的连接起作用。</p>
<p>如果客户端连接MySQL后，长时间没有执行任何操作，则连接器会自动断开与这个客户端的连接。具体多长时间断开是由MySQL的参数<code>wait_timeout</code>控制的，这个值默认是8小时。我们可以根据实际业务需要，自行调整这个参数的值，以使MySQL能够满足我们的实际业务场景。</p>
<p>由于客户端与MySQL的连接是比较复杂的，这个过程也是比较耗时的，它会涉及TCP的握手操作，还会查询当前连接的权限信息等。往往在实际的工作过程中，我们会使用数据库连接池的方式，将数据库的连接缓存起来，这就意味着我们是使用长连接与MySQL进行交互的。</p>
<p>但是使用长连接连接MySQL也会有一个问题：那就是有时候会发现MySQL占用的内存涨得特别快，这是因为<strong>MySQL在执行的过程中，使用的临时内存是在连接对象里面进行管理的</strong>。这些占用的资源只有在连接断开的时候，才会被释放。如果连接长时间不释放，就会出现大量的临时内存占用内存空间。如果时间久了，可能会导致占用过多的内存，从而被操作系统“消灭”了，给人的感觉就是MySQL意外重启了。</p>
<p><strong>我们可以使用如下的方案来解决这个问题：</strong></p>
<ul>
<li>定期或者执行过一个比较占内存的查询操作后，断开连接，以后再重新建立和MySQL的连接。</li>
<li>如果使用MySQL 5.7或更新的MySQL版本，可以通过执行<code>mysql_reset_connection</code>重新初始化MySQL的资源。重新初始化的过程不会重新连接MySQL，也不会重新做权限的验证操作。</li>
</ul>
<h2 data-id="heading-3">查询缓存的作用是什么？</h2>
<p>登录MySQL后，客户端就会与MySQL建立连接，此时执行select语句时，首先会到查询缓存中查询是否执行过当前select语句。如果之前执行过相应的select语句，则执行过的select语句和查询结果会以key-value的形式存放在查询缓存中，其中，key是查询语句，value是查询的结果数据。</p>
<p>如果在查询缓存中没有找到相应的数据，则会继续执行后续的查询阶段。执行完成后，会将结果缓存到查询缓存中。后续的查询如果命中缓存，则直接返回查询缓存中的数据，性能还是挺高的。</p>
<p>但是，大多数时候我不太建议小伙伴们开启查询缓存，为啥？原因很简单：<strong>查询缓存失效的频率是非常频繁的，只要对一个表进行更新操作，则这张表上所有的查询缓存都会被清空。</strong> 而且在MySQL 8.0中，直接删除了查询缓存的功能（<strong>冰河在看MySQL源码时，也证明了这一点</strong>）。</p>
<h2 data-id="heading-4">分析器对select语句做了什么？</h2>
<p>分析器主要是对select语句进行 <strong>词法分析和语法分析</strong> 操作。</p>
<p>如果select语句没有命中缓存，则首先会由分析器对其进行“词法分析”操作，此时，MySQL会识别select语句中的每个字符串代表什么含义。</p>
<p>例如，MySQL会通过"select"关键字识别出这是一个查询语句，也会把"user"识别为"数据表名user"，把"id"识别成"字段名id"。接下来，就要进行“语法分析了”，根据语法规则，判断select语句是否满足MySQL的语法。如果判断出输入的SQL语句不满足语法规则，则MySQL会提示相应的错误信息。</p>
<h2 data-id="heading-5">优化器是如何优化select语句的？</h2>
<p>对select语句进行了词法分析和语法分析后，还要经过优化器的优化处理才能执行。比如，我们的select语句中如果使用了多个索引，则优化器会决定使用哪个索引来查询数据；再比如，在select语句中，有多表关联的操作，优化器会决定各表的连接顺序，数据表的连接顺序不同，对于执行的效率会大不相同，优化器往往会选择使用查询效率高的连接顺序。</p>
<p>如果select语句经过优化器的优化之后，就会进入执行阶段了。</p>
<h2 data-id="heading-6">执行器如何执行select语句？</h2>
<p>进入执行阶段的select语句，首先，执行器会对当前连接进行权限检查，最直接的方式就是检查当前连接是否对数据表user具有查询权限。如果当前连接对数据表user没有查询权限，就会返回没有权限的错误。例如，会返回如下错误。</p>
<pre><code class="hljs language-sql copyable" lang="sql">ERROR <span class="hljs-number">1142</span> (<span class="hljs-number">42000</span>): <span class="hljs-keyword">SELECT</span> command denied <span class="hljs-keyword">to</span> <span class="hljs-keyword">user</span> <span class="hljs-string">'binghe'</span>@<span class="hljs-string">'localhost'</span> <span class="hljs-keyword">for</span> <span class="hljs-keyword">table</span> <span class="hljs-string">'user'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果当前连接具有对数据表user的查询权限，则会继续执行。首先会进行打开数据表的操作，此时优化器会根据创建表时使用的存储引擎，使用相应存储引擎的接口执行查询操作。这里，我们举一个例子：</p>
<p>假设，我们在id字段上没有建立索引，执行器执行的流程大致如下所示。</p>
<p>（1）通过存储引擎读取数据表user的第一行数据，判断当前行的id值是否等于1001，如果不等于1001，则继续读取下一行数据；如果等于1001，则将当前行放入结果集中。</p>
<p>（2）继续通过存储引擎读取下一行数据，执行与（1）相同的逻辑判断，直到处理完user表中的所有数据。</p>
<p>（3）处理完所有的数据后，执行器就会将结果集中的数据返回给客户端。</p>
<p>如果在id字段上有索引的话，执行的整体逻辑与id字段上没有索引大体一致。</p>
<p>如果开启了慢查询的话，执行select语句时，会在慢查询日志中输出一个rows_examined字段，这个字段表示select语句在执行的过程中扫描了数据表中的多少行数据。不过在有些场景下，执行器调用一次，存储引擎内部会会扫描多行，这就导致存储引擎扫描的行数与rows_examined字段标识的行数并不完全相同。</p>
<p><strong>好了，今天就到这儿吧，我是冰河，我们下期见~~</strong></p></div>  
</div>
            