
---
title: 'Ory  keto'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83df2a6a4a6345ec8f4c73952b2fbdcd~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 01:09:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83df2a6a4a6345ec8f4c73952b2fbdcd~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">权限服务器keto</h1>
<blockquote>
<p>keto介绍</p>
</blockquote>
<p>ORY Keto是一种权限服务器，它实现最佳实践访问控制机制：</p>
<ul>
<li>今天可用：具有精确，全局和正则表达式匹配策略的ORY风格的访问控制策略</li>
<li>即将推出：</li>
<li>访问控制列表</li>
<li>基于角色的访问控制</li>
<li>具有上下文的基于角色的访问控制（Google / Kubernetes风格）</li>
<li>Amazon Web Services身份和访问管理策略（AWS IAM策略）</li>
<li>每种机制都由在开放策略代理之上实现的决策引擎提供动力,并提供定义明确的管理和授权端点</li>
</ul>
<h2 data-id="heading-1">1 代码下载</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fory%2Fketo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ory/keto" ref="nofollow noopener noreferrer">keto源码地址下载</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ory.sh%2F%3Futm_source%3Dgithub%26utm_medium%3Dbanner%26utm_campaign%3Dketo" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ory.sh/?utm_source=github&utm_medium=banner&utm_campaign=keto" ref="nofollow noopener noreferrer">官方文档简单说明</a></p>
<blockquote>
<p>解压说明</p>
</blockquote>
<p><strong>把下载的源码解压后放在本地<code>%GOPATH%/src</code>目录下</strong></p>
<p><strong>注:GOPATH为项目的运行时的工作空间位置,GOPATH其中包含三个子目录如下</strong></p>
<ul>
<li>src 目录包含Go的源文件，它们被组织成包（每个目录都对应一个包）</li>
<li>pkg 目录包含包对象</li>
<li>bin 目录包含可执行命令</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83df2a6a4a6345ec8f4c73952b2fbdcd~tplv-k3u1fbpfcp-zoom-1.image" alt="<a data-fancybox title="keto存放位置" href="/img/goImage/keto1.png">[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-D5g6mf68-1591890034559)(/img/goImage/keto1.png)]</a>" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">2 关键词介绍</h2>
<h3 data-id="heading-3">2.1 RBAC</h3>
<blockquote>
<p>RBAC介绍</p>
</blockquote>
<p>​RBAC是基于角色的访问控制（<code>Role-Based Access Control</code> ）在 RBAC  中，权限与角色相关联，用户通过成为适当角色的成员而得到这些角色的权限。这就极大地简化了权限的管理。这样管理都是层级相互依赖的，权限赋予给角色，而把角色又赋予用户，这样的权限设计很清楚，管理起来很方便。
。RBAC  认为授权实际上是<code>Who</code> 、<code>What</code> 、<code>How</code> 三元组之间的关系，也就是<code>Who</code> 对<code>What</code> 进行<code>How</code> 的操作，也就是“主体”对“客体”的操作。
然后 RBAC  又分为<code>RBAC0、RBAC1、RBAC2、RBAC3</code> ，如果你不知道他们有什么区别，你可以百度百科：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fbaike.baidu.com%2Flink%3Furl%3DTg3nxejvD2QVLLkjKa_4XaQoOWSPAVpR1FgHAG_gANcamtN2cYIm1r1irNw9VZ816FBrMEvdoYqwzixqdHd5e_" target="_blank" rel="nofollow noopener noreferrer" title="http://baike.baidu.com/link?url=Tg3nxejvD2QVLLkjKa_4XaQoOWSPAVpR1FgHAG_gANcamtN2cYIm1r1irNw9VZ816FBrMEvdoYqwzixqdHd5e_" ref="nofollow noopener noreferrer">百度百科-RBAC</a> ,也可以看看我的介绍。</p>
<ul>
<li><code>Who</code>：是权限的拥有者或主体（如：User，Role）。</li>
<li><code>What</code>：是操作或对象（operation，object）。</li>
<li><code>How</code>：具体的权限（Privilege,正向授权与负向授权）。</li>
</ul>
<h3 data-id="heading-4">2.1 ABAC</h3>
<blockquote>
<p>ABAC介绍</p>
</blockquote>
<p>ABAC（Attribute Base Access Control） 基于属性的权限控制，不同于常见的将用户通过某种方式关联到权限的方式，ABAC则是通过动态计算一个或一组属性来是否满足某种条件来进行授权判断（可以编写简单的逻辑）。属性通常来说分为四类：用户属性（如用户年龄），环境属性（如当前时间），操作属性（如读取）和对象属性（如一篇文章，又称资源属性），所以理论上能够实现非常灵活的权限控制，几乎能满足所有类型的需求。
访问控制列表(**ACL **)是一种基于包过滤的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E8%25AE%25BF%25E9%2597%25AE%25E6%258E%25A7%25E5%2588%25B6%25E6%258A%2580%25E6%259C%25AF%2F5652430" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E6%8A%80%E6%9C%AF/5652430" ref="nofollow noopener noreferrer">访问控制技术</a>，它可以根据设定的条件对接口上的数据包进行过滤，允许其通过或丢弃。访问控制列表被广泛地应用于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E8%25B7%25AF%25E7%2594%25B1%25E5%2599%25A8%2F108294" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E8%B7%AF%E7%94%B1%E5%99%A8/108294" ref="nofollow noopener noreferrer">路由器</a>和三层<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E4%25BA%25A4%25E6%258D%25A2%25E6%259C%25BA%2F103532" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E4%BA%A4%E6%8D%A2%E6%9C%BA/103532" ref="nofollow noopener noreferrer">交换机</a>，借助于访问控制列表，可以有效地控制用户对网络的访问，从而最大程度地保障网络安全。</p>
<h3 data-id="heading-5">2.3 采坑bug修改</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a263e7435c32450bb77497823b874d2b~tplv-k3u1fbpfcp-zoom-1.image" alt="<a data-fancybox title="bug" href="/img/goImage/bug1.png">[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-AFOyCvyD-1591890034564)(/img/goImage/bug1.png)]</a>" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将url.go 中的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce36a01e6e754aee800887cf385108c8~tplv-k3u1fbpfcp-zoom-1.image" alt="<a data-fancybox title="bug1xxiu" href="/img/goImage/bug1xxiu.png">[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-9tJtz5Rl-1591890034568)(/img/goImage/bug1xxiu.png)]</a>" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改为
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d475de55f072426a82cddfe6d0646f6f~tplv-k3u1fbpfcp-zoom-1.image" alt="<a data-fancybox title="bug1xiu" href="/img/goImage/bug1xiu.png">[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-xCqOfDvW-1591890034572)(/img/goImage/bug1xiu.png)]</a>" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个问题存在是由于应用源码对字符串的解析问题，可以不写端口，采用默认的端口</p>
<h2 data-id="heading-6">3 项目运行</h2>
<blockquote>
<p>官方代码下载后编译成keto.exe执行，直接执行指挥出现提示页面</p>
</blockquote>
<h3 data-id="heading-7">3.1 代码示例</h3>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">dsn:</span> <span class="hljs-string">mysql://root:minda123@tcp(127.0.0.1)/keto?parseTime=true&multiStatements=true</span> 
<span class="hljs-comment"># 这里如果用默认端口就不要加端口号：3306</span>

<span class="hljs-attr">secrets:</span>
  <span class="hljs-attr">system:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">admin1</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">admin2</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">admin3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-go copyable" lang="go">>keto.exe --config F:/awesomeProject/bin/config.yaml migrate sql -e
      
time=<span class="hljs-string">"2019-12-25T16:27:28+08:00"</span> level=info msg=<span class="hljs-string">"Connecting with mysql://*:*@tcp(127.0.0.1)/keto?multiStatements=true"</span>
time=<span class="hljs-string">"2019-12-25T16:27:28+08:00"</span> level=info msg=<span class="hljs-string">"Connected to SQL!"</span>
time=<span class="hljs-string">"2019-12-25T16:27:28+08:00"</span> level=info msg=<span class="hljs-string">"Applying storage SQL migrations..."</span>
time=<span class="hljs-string">"2019-12-25T16:27:28+08:00"</span> level=info msg=<span class="hljs-string">"Successfully applied SQL migrations"</span> applied_migrations=<span class="hljs-number">1</span> migration=name
time=<span class="hljs-string">"2019-12-25T16:27:28+08:00"</span> level=info msg=<span class="hljs-string">"Done applying storage SQL migrations"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">3.2 启动服务</h3>
<pre><code class="hljs language-go copyable" lang="go">serve --config F:/awesomeProject/bin/config.yaml
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3.3 项目API</h3>
<p><a href="https://juejin.cn/go/middleware/go-swagger.html" target="_blank" title="/go/middleware/go-swagger.html"><strong>swagger安装教程</strong></a></p>
<blockquote>
<p>进入项目根目录，启动swagger服务</p>
</blockquote>
<pre><code class="hljs language-go copyable" lang="go">swagger serve -F=swagger F:\awesomeProject\src\github.com\ory\keto\docs\api.swagger.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>运行成功后会提示服务运行在的地址，点击进入即可看到如下页面：</strong></p>
<h3 data-id="heading-10">3.4 主要是要用的访问策略</h3>
<h4 data-id="heading-11">ACL：</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aaaad43c79b43f49af7bfcc602aabbd~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
访问控制列表</p>

































<table><thead><tr><th></th><th>blog_post.create</th><th>blog_post.delete</th><th>blog_post.modify</th><th>blog_post.read</th></tr></thead><tbody><tr><td>Alice</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td></tr><tr><td>Bob</td><td>no</td><td>no</td><td>no</td><td>yes</td></tr><tr><td>Peter</td><td>yes</td><td>no</td><td>yes</td><td>yes</td></tr></tbody></table>
<h4 data-id="heading-12">RBAC：</h4>
<h2 data-id="heading-13">4 ORY Access Control Policies</h2>
<h3 data-id="heading-14">4.1 策略准备</h3>
<blockquote>
<p>put请求：<a href="https://link.juejin.cn/?target=http%3A%2F%2F127.0.0.1%3A4444%2F%2Fengines%2Facp%2Fory%2Fglob%2Fpolicies" target="_blank" rel="nofollow noopener noreferrer" title="http://127.0.0.1:4444//engines/acp/ory/glob/policies" ref="nofollow noopener noreferrer">http://127.0.0.1:4444//engines/acp/ory/glob/policies</a></p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"subjects"</span>: [<span class="hljs-string">"alice"</span>],
  <span class="hljs-attr">"resources"</span>: [<span class="hljs-string">"blog_posts:my-first-blog-post"</span>],
  <span class="hljs-attr">"actions"</span>: [<span class="hljs-string">"delete"</span>],
  <span class="hljs-attr">"effect"</span>: <span class="hljs-string">"allow"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"subjects"</span>: [<span class="hljs-string">"alice"</span>, <span class="hljs-string">"bob"</span>],
  <span class="hljs-attr">"resources"</span>: [
    <span class="hljs-string">"blog_posts:my-first-blog-post"</span>,
    <span class="hljs-string">"blog_posts:2"</span>,
    <span class="hljs-string">"blog_posts:3"</span>
  ],
  <span class="hljs-attr">"actions"</span>: [<span class="hljs-string">"delete"</span>, <span class="hljs-string">"create"</span>, <span class="hljs-string">"read"</span>, <span class="hljs-string">"modify"</span>],
  <span class="hljs-attr">"effect"</span>: <span class="hljs-string">"allow"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会在数据库生成新的记录</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"subjects"</span>: [<span class="hljs-string">"peter"</span>],
  <span class="hljs-attr">"resources"</span>: [
    <span class="hljs-string">"blog_posts:my-first-blog-post"</span>,
    <span class="hljs-string">"blog_posts:2"</span>,
    <span class="hljs-string">"blog_posts:3"</span>
  ],
  <span class="hljs-attr">"actions"</span>: [<span class="hljs-string">"delete"</span>, <span class="hljs-string">"create"</span>, <span class="hljs-string">"read"</span>, <span class="hljs-string">"modify"</span>],
  <span class="hljs-attr">"effect"</span>: <span class="hljs-string">"deny"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>The <code>:</code> is a delimiter in ORY Access Control Policies. Other supported syntax
is:</p>
<p><strong>single symbol wildcard:</strong> <code>?at</code> matches <code>cat</code> and <code>bat</code> but not <code>at</code>
<strong>wildcard:</strong> <code>foo:*:bar</code> matches <code>foo:baz:bar</code> and <code>foo:zab:bar</code> but not
<code>foo:bar</code> nor <code>foo:baz:baz:bar</code>
<strong>super wildcard:</strong> <code>foo:**:bar</code> matches <code>foo:baz:baz:bar</code>, <code>foo:baz:bar</code>, and
<code>foo:bar</code>, but not <code>foobar</code> or <code>foo:baz</code>
<strong>character list:</strong> <code>[cb]at</code> matches <code>cat</code> and <code>bat</code> but not <code>mat</code> nor <code>at</code>.
<strong>negated character list:</strong> <code>[!cb]at</code> matches <code>tat</code> and <code>mat</code> but not <code>cat</code>
nor <code>bat</code>.
<strong>ranged character list:</strong> <code>[a-c]at</code> <code>cat</code> and <code>bat</code> but not <code>mat</code> nor <code>at</code>.
<strong>negated ranged character list:</strong> <code>[!a-c]at</code> matches <code>mat</code> and <code>tat</code> but not
<code>cat</code> nor <code>bat</code>.
<strong>alternatives list:</strong> <code>&#123;cat,bat,[mt]at&#125;</code> matches <code>cat</code>, <code>bat</code>, <code>mat</code>, <code>tat</code>
and nothing else.
<strong>backslash:</strong> <code>foo\\bar</code> matches <code>foo\bar</code> and nothing else. <code>foo\bar</code>
matches <code>foobar</code> and nothing else. <code>foo\*bar</code> matches <code>foo*bar</code> and nothing
else. Please note that when using JSON you need to double escape backslashes:
<code>foo\\bar</code> becomes <code>&#123;"...": "foo\\\\bar"&#125;</code>.</p>
<p>The pattern syntax is:</p>
<pre><code class="hljs language-json copyable" lang="json">  pattern:

      &#123; term &#125;

  term:

      *         matches any sequence of non-separator characters

      **        matches any sequence of characters

      ?         matches any single non-separator character

      [ [ ! ] &#123; character-range &#125; ]

                  character class (must be non-empty)

      &#123; pattern-list &#125;

                  pattern alternatives

      c           matches character c (c != *, **, ?, \, [, &#123;, &#125;)

      \ c       matches character c

  character-range:

      c           matches character c (c != \\, -, ])

      \ c       matches character c

      lo - hi   matches character c for lo <= c <= hi

  pattern-list:

      pattern &#123; , pattern &#125;

                  comma-separated (without spaces) pattern

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">4.2 json实例</h3>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"One policy to rule them all."</span>,
  <span class="hljs-attr">"subjects"</span>: [<span class="hljs-string">"users:maria:*"</span>],
  <span class="hljs-attr">"actions"</span>: [<span class="hljs-string">"delete"</span>, <span class="hljs-string">"create"</span>, <span class="hljs-string">"update"</span>,<span class="hljs-string">"modify"</span>,<span class="hljs-string">"get"</span>,<span class="hljs-string">"read"</span>],
  <span class="hljs-attr">"effect"</span>: <span class="hljs-string">"allow"</span>,
  <span class="hljs-attr">"resources"</span>: [<span class="hljs-string">"resources:articles:<.*>"</span>],
  <span class="hljs-attr">"conditions"</span>: &#123;
    <span class="hljs-attr">"someKeyName"</span>: &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"StringMatchCondition"</span>,
      <span class="hljs-attr">"options"</span>: &#123;
        <span class="hljs-attr">"matches"</span>: <span class="hljs-string">"foo.+"</span>
      &#125;
    &#125;,
    <span class="hljs-attr">"someKey"</span>: &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"StringPairsEqualCondition"</span>,
      <span class="hljs-attr">"options"</span>: &#123;&#125;
    &#125;, 
    <span class="hljs-attr">"myKey"</span>: &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"StringEqualCondition"</span>,
      <span class="hljs-attr">"options"</span>: &#123;
        <span class="hljs-attr">"equals"</span>: <span class="hljs-string">"expected-value"</span>
      &#125;
    &#125;,      
    <span class="hljs-attr">"remoteIPAddress"</span>: &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"CIDRCondition"</span>,
      <span class="hljs-attr">"options"</span>: &#123;
        <span class="hljs-attr">"cidr"</span>: <span class="hljs-string">"192.168.0.0/16"</span>
      &#125;
    &#125;,
    <span class="hljs-attr">"this-key-will-be-matched-with-the-context"</span>: &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"SomeConditionType"</span>,
      <span class="hljs-attr">"options"</span>: &#123;
        <span class="hljs-attr">"some"</span>: <span class="hljs-string">"configuration options set by the condition type"</span>
      &#125;
    &#125;
  &#125;,
   <span class="hljs-attr">"context"</span>: &#123;
    <span class="hljs-attr">"someKey"</span>: [[<span class="hljs-string">"foo"</span>, <span class="hljs-string">"foo"</span>], [<span class="hljs-string">"bar"</span>, <span class="hljs-string">"bar"</span>]]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">4.3 主要请求及其说明</h3>
<h4 data-id="heading-17">参数说明</h4>
<h4 data-id="heading-18">响应参数说明</h4>





























































<table><thead><tr><th>Name</th><th>Type</th><th>Required</th><th>Restrictions</th><th>Description</th></tr></thead><tbody><tr><td>code</td><td>integer(int64)</td><td>false</td><td>none</td><td>none</td></tr><tr><td>details</td><td>[object]</td><td>false</td><td>none</td><td>none</td></tr><tr><td>additionalProperties</td><td>object</td><td>false</td><td>none</td><td>none</td></tr><tr><td>message</td><td>string</td><td>false</td><td>none</td><td>none</td></tr><tr><td>reason</td><td>string</td><td>false</td><td>none</td><td>none</td></tr><tr><td>request</td><td>string</td><td>false</td><td>none</td><td>none</td></tr><tr><td>status</td><td>string</td><td>false</td><td>none</td><td>none</td></tr></tbody></table>
<h4 data-id="heading-19">请求参数说明</h4>



















<table><thead><tr><th>Parameter</th><th>In</th><th align="left">Type</th><th align="left">Required</th><th>Description</th></tr></thead><tbody><tr><td>flavor</td><td>path</td><td align="left">string</td><td align="left">true</td><td>The ORY Access Control Policy flavor. Can be "regex", "glob", and "exact".</td></tr></tbody></table>
<h3 data-id="heading-20">4.4 检查请求是否允许通过</h3>
<p>请求头</p>
<pre><code class="hljs language-html copyable" lang="html">POST /engines/acp/ory/&#123;flavor&#125;/allowed HTTP/1.1

Content-Type: application/json

Accept: application/json

<span class="copy-code-btn">复制代码</span></code></pre>
<p>body</p>
<pre><code class="copyable">&#123;
  "action": "string",
  "context": &#123;
    "property1": &#123;&#125;,
    "property2": &#123;&#125;
  &#125;,
  "resource": "string",
  "subject": "string"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">4.5 参数列表</h3>
<p>OryAccessControlPolicyAllowedInput*</p>















































<table><thead><tr><th>Name</th><th>Type</th><th>Required</th><th>Restrictions</th><th>Description</th></tr></thead><tbody><tr><td>action</td><td>string</td><td>false</td><td>none</td><td>Action is the action that is requested on the resource.</td></tr><tr><td>context</td><td>object</td><td>false</td><td>none</td><td>Context is the request's environmental context.</td></tr><tr><td><strong>additionalProperties</strong></td><td>object</td><td>false</td><td>none</td><td>none</td></tr><tr><td>resource</td><td>string</td><td>false</td><td>none</td><td>Resource is the resource that access is requested to.</td></tr><tr><td>subject</td><td>string</td><td>false</td><td>none</td><td>Subject is the subject that is requesting access.</td></tr></tbody></table>
<p>response</p>
<p><code>&#123;"allowed":"true"&#125;</code>  or <code>&#123;"allowed":"false"&#125;</code></p>
<h2 data-id="heading-22">5 访问控制策略操作</h2>
<h3 data-id="heading-23">5.1 获取访问控制策略集合</h3>
<pre><code class="copyable">GET /engines/acp/ory/&#123;flavor&#125;/policies HTTP/1.1
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数列表</p>






















































<table><thead><tr><th>Parameter</th><th>In</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td>flavor</td><td>path</td><td>string</td><td>true</td><td>The ORY Access Control Policy flavor. Can be "regex", "glob", and "exact"</td></tr><tr><td>limit</td><td>query</td><td>integer(int64)</td><td>false</td><td>The maximum amount of policies returned.</td></tr><tr><td>offset</td><td>query</td><td>integer(int64)</td><td>false</td><td>The offset from where to start looking.</td></tr><tr><td>subject</td><td>query</td><td>string</td><td>false</td><td>The subject for whom the policies are to be listed.</td></tr><tr><td>resource</td><td>query</td><td>string</td><td>false</td><td>The resource for which the policies are to be listed.</td></tr><tr><td>action</td><td>query</td><td>string</td><td>false</td><td>The action for which policies are to be listed.</td></tr></tbody></table>
<h3 data-id="heading-24">5.2 更新访问控制策略</h3>
<pre><code class="hljs language-go copyable" lang="go">PUT /engines/acp/ory/&#123;flavor&#125;/policies HTTP/<span class="hljs-number">1.1</span>
Content-Type: application/json
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数列表</p>




































































<table><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th><strong>Restrictions</strong></th><th>Description</th></tr></thead><tbody><tr><td>actions</td><td>[string]</td><td>false</td><td>none</td><td>Actions is an array representing all the actions this ORY Access Policy applies to.</td></tr><tr><td>conditions</td><td>object</td><td>false</td><td>none</td><td>Conditions represents a keyed object of conditions under which this ORY Access Policy is active.</td></tr><tr><td><strong>additionalProperties</strong></td><td>object</td><td>false</td><td>none</td><td>none</td></tr><tr><td>description</td><td>string</td><td>false</td><td>none</td><td>Description is an optional, human-readable description.</td></tr><tr><td>effect</td><td>string</td><td>false</td><td>none</td><td>Effect is the effect of this ORY Access Policy. It can be "allow" or "deny".</td></tr><tr><td>id</td><td>string</td><td>false</td><td>none</td><td>访问策略的唯一标识，用来查询，更新和删除</td></tr><tr><td>resources</td><td>[string]</td><td>false</td><td>none</td><td>Resources is an array representing all the resources this ORY Access Policy applies to.</td></tr><tr><td>subjects</td><td>[string]</td><td>false</td><td>none</td><td>Subjects is an array representing all the subjects this ORY Access Policy applies to.</td></tr></tbody></table>
<h3 data-id="heading-25">5.3 查询具体的策略</h3>
<pre><code class="copyable">GET /engines/acp/ory/&#123;flavor&#125;/policies/&#123;id&#125; HTTP/1.1
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">5.4  删除访问控制策略</h3>
<pre><code class="copyable">DELETE /engines/acp/ory/&#123;flavor&#125;/policies/&#123;id&#125; HTTP/1.1
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">6 访问控制策略角色操作</h2>
<h3 data-id="heading-28">6.1 查询寻访问控制角色集合</h3>
<pre><code class="copyable">GET /engines/acp/ory/&#123;flavor&#125;/roles HTTP/1.1
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数说明：</p>








































<table><thead><tr><th>Parameter</th><th>In</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td>flavor</td><td>path</td><td>string</td><td>true</td><td>The ORY Access Control Policy flavor. Can be "regex", "glob", and "exact"</td></tr><tr><td>limit</td><td>query</td><td>integer(int64)</td><td>false</td><td>The maximum amount of policies returned.</td></tr><tr><td>offset</td><td>query</td><td>integer(int64)</td><td>false</td><td>The offset from where to start looking.</td></tr><tr><td>member</td><td>query</td><td>string</td><td>false</td><td>The member for which the roles are to be listed.</td></tr></tbody></table>
<h3 data-id="heading-29">6.2 添加访问控制的角色</h3>
<pre><code class="copyable">PUT /engines/acp/ory/&#123;flavor&#125;/roles HTTP/1.1
Content-Type: application/json
Accept: application/json

<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子：</p>
<pre><code class="copyable">&#123;
  "id": "string",
  "members": ["string"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数列表</p>























<table><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td>id</td><td>string</td><td>false</td><td>ID is the role's unique id.</td></tr><tr><td>members</td><td>[string]</td><td>false</td><td>Members is who belongs to the role.</td></tr></tbody></table>
<h3 data-id="heading-30">6.3 获取访问控制角色信息</h3>
<pre><code class="copyable">GET /engines/acp/ory/&#123;flavor&#125;/roles/&#123;id&#125; HTTP/1.1
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">6.4 删除访问控制角色信息</h3>
<pre><code class="copyable">DELETE  /engines/acp/ory/&#123;flavor&#125;/roles/&#123;id&#125; HTTP/1.1
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">6.5 为角色添加用户</h3>
<pre><code class="copyable">PUT /engines/acp/ory/&#123;flavor&#125;/roles/&#123;id&#125;/members HTTP/1.1 Content-Type: application/json Accept: application/json

请求体：
&#123;
  "members": ["string"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">6.6从角色中删除某个用户成员</h3>
<pre><code class="copyable">DELETE /engines/acp/ory/&#123;flavor&#125;/roles/&#123;id&#125;/members/&#123;member&#125; HTTP/1.1 Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-34">7 健康检查</h2>
<h3 data-id="heading-35">7.1 检查存活状态</h3>
<pre><code class="copyable">GET /health/alive HTTP/1.1
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：（官方说明总是ok）</p>
<pre><code class="copyable">&#123;  "status": "ok" &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">7.2 检查准备就绪</h3>
<pre><code class="copyable">GET /health/ready HTTP/1.1
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">7.3 获取当前版本</h3>
<pre><code class="copyable">GET /version HTTP/1.1 
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-38">8 测试样例</h2>
<pre><code class="copyable">put   http://127.0.0.1:4444/engines/acp/ory/glob/policies

&#123;
  "actions": ["get","create","modify","delete"],
  "conditions": &#123;
    "optionAccess": &#123;
    "type": "CIDRCondition",
    "options": &#123;
        "cidr": "192.168.0.0/16"
      &#125;
    &#125;
  &#125;,
  "description": "test q",
  "effect": "allow",
  "id": "string",
  "resources": [ 
  "blog_posts:my-first-blog-post",
    "blog_posts:2",
    "blog_posts:3"],
  "subjects": ["admin","admin1","admin2"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ation/json</p>
<pre><code class="copyable">


## 8 测试样例

<span class="copy-code-btn">复制代码</span></code></pre>
<p>put   <a href="https://link.juejin.cn/?target=http%3A%2F%2F127.0.0.1%3A4444%2Fengines%2Facp%2Fory%2Fglob%2Fpolicies" target="_blank" rel="nofollow noopener noreferrer" title="http://127.0.0.1:4444/engines/acp/ory/glob/policies" ref="nofollow noopener noreferrer">http://127.0.0.1:4444/engines/acp/ory/glob/policies</a></p>
<p>&#123;
"actions": ["get","create","modify","delete"],
"conditions": &#123;
"optionAccess": &#123;
"type": "CIDRCondition",
"options": &#123;
"cidr": "192.168.0.0/16"
&#125;
&#125;
&#125;,
"description": "test q",
"effect": "allow",
"id": "string",
"resources": [
"blog_posts:my-first-blog-post",
"blog_posts:2",
"blog_posts:3"],
"subjects": ["admin","admin1","admin2"]
&#125;</p>
<pre><code class="copyable">


  






<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            