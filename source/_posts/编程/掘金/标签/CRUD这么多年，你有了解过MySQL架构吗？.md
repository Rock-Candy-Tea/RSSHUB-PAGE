
---
title: 'CRUD这么多年，你有了解过MySQL架构吗？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42943cbaac4d41e888a9eebb901c67de~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 19:51:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42943cbaac4d41e888a9eebb901c67de~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>目前大部分的后端开发人员对<code>MySQL</code>的理解可能停留在一个黑盒子阶段。</p>
<p>对<code>MySQL</code>基本使用没什么问题，比如建库、建表、建索引，执行各种增删改查。</p>
<p>所有很多后端开发人员眼中的<code>MySQL</code>如下图所示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42943cbaac4d41e888a9eebb901c67de~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>导致在实际工作中碰到<code>MySQL</code>中死锁异常、<code>SQL</code>性能太差、异常报错等问题时，直接百度搜索。</p>
<p>然后跟着博客捣鼓就解决了，可能自己都没搞明白里面的原理。</p>
<p>为了解决这种<strong>知其然而不知其所以然</strong>的问题，阿星的<strong>重学MySQL系列</strong>会带着大家去探索MySQL底层原理的方方面面。</p>
<p>这样大家碰到<code>MySQL</code>的一些异常或者问题时，能够直戳本质，快速地定位解决。</p>
<h1 data-id="heading-1">连接管理</h1>
<p>系统（客户端）访问<code>MySQL</code>服务器前，做的第一件事就是建立<code>TCP</code>连接。</p>
<p>经过三次握手建立连接成功后，<code>MySQL</code>服务器对<code>TCP</code>传输过来的账号密码做身份认证、权限获取。</p>
<ul>
<li><strong>用户名或密码不对，会收到一个Access denied for user错误，客户端程序结束执行</strong></li>
<li><strong>用户名密码认证通过，会从权限表查出账号拥有的权限与连接关联，之后的权限判断逻辑，都将依赖于此时读到的权限</strong></li>
</ul>
<p>接着我们来思考一个问题</p>
<p>一个系统只会和<code>MySQL</code>服务器建立一个连接吗？</p>
<p>只能有一个系统和<code>MySQL</code>服务器建立连接吗？</p>
<p>当然不是，多个系统都可以和<code>MySQL</code>服务器建立连接，每个系统建立的连接肯定不止一个。</p>
<p>所以，为了解决<code>TCP</code>无限创建与<code>TCP</code>频繁创建销毁带来的资源耗尽、性能下降问题。</p>
<p><code>MySQL</code>服务器里有专门的<code>TCP</code>连接池限制接数，采用长连接模式复用<code>TCP</code>连接，来解决上述问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a2fa649da7c46a5b877f7d73971be22~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>TCP</code>连接收到请求后，必须要分配给一个线程去执行，所以还会有个线程池，去走后面的流程。</p>
<p>这些内容我们都归纳到<code>MySQL</code>的<strong>连接管理</strong>组件中。</p>
<p>所以<strong>连接管理</strong>的职责是负责认证、管理连接、获取权限信息。</p>
<h1 data-id="heading-2">解析与优化</h1>
<p>经过了连接管理，现在<code>MySQL</code>服务器已经获取到<code>SQL</code>字符串。</p>
<p>如果是查询语句，<code>MySQL</code>服务器会使用<code>select SQL</code>字符串作为<code>key</code>。</p>
<p>去缓存中获取，命中缓存，直接返回结果（<strong>返回前需要做权限验证</strong>），未命中执行后面的阶段，这个步骤叫<strong>查询缓存</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6baec6660a8449b6bbec0f46ce04a8aa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要注意，<code>select SQL</code>字符串要完全匹配，有任何不同的地方都会导致缓存不被命中（<strong>空格、注释、大小写、某些系统函数</strong>）。</p>
<blockquote>
<p>小贴士：虽然查询缓存有时可以提升系统性能，但也不得不因维护这块缓存而造成一些开销，从MySQL 5.7.20开始，不推荐使用查询缓存，并在MySQL 8.0中删除。</p>
</blockquote>
<p>没有命中缓存，或者非<code>select SQL</code>就来到<strong>分析器</strong>阶段了。</p>
<p>因为系统发送过来的只是一段文本字符串，所以<code>MySQL</code>服务器要按照<code>SQL</code>语法对这段文本进行解析。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5595835bc5df44cbb3c8d9520083428e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你的<code>SQL</code>字符串不符合语法规范，就会收到<code>You have an error in your SQL syntax</code>错误提醒</p>
<p>通过了<strong>分析器</strong>，说明<code>SQL</code>字符串符合语法规范，现在<code>MySQL</code>服务器要执行<code>SQL</code>语句了。</p>
<p><code>MySQL</code>服务器要怎么执行呢？</p>
<p>你需要产出执行计划，交给<code>MySQL</code>服务器执行，所以来到了<strong>优化器</strong>阶段。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b3f3b210b374f78bc28698e93afcfb9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>优化器不仅仅只是生成执行计划这么简单，这个过程它会帮你优化<code>SQL</code>语句。</p>
<p>如<strong>外连接转换为内连接、表达式简化、子查询转为连接、连接顺序、索引选择</strong>等一堆东西，优化的结果就是执行计划。</p>
<p>截止到现在，还没有真正去读写真实的表，仅仅只是产出了一个执行计划。</p>
<p>于是就进入了<strong>执行器</strong>阶段，<code>MySQL</code>服务器终于要执行<code>SQL</code>语句了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a1f1ba045a0401c92d2355ad36dfd39~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>开始执行的时候，要先判断一下对这个表有没有相应的权限，如果没有，就会返回权限错误。</p>
<p>如果有权限，根据执行计划调用存储引擎<code>API</code>对表进行的读写。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6f5b7f190954d5d9ce6ac3fa482ed07~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>存储引擎<code>API</code>只是抽象接口，下面还有个<strong>存储引擎层</strong>，具体实现还是要看表选择的存储引擎。</p>
<p>讲到这里，上面提到的<strong>查询缓存、分析器、优化器、执行器</strong>都可以归纳到<code>MySQL</code>的<strong>解析与优化</strong>组件中。</p>
<p>所以<strong>解析与优化</strong>的职责如下：</p>
<ul>
<li><strong>缓存</strong></li>
<li><strong>SQL语法解析验证</strong></li>
<li><strong>SQL优化并生成执行计划</strong></li>
<li><strong>根据执行计划调用存储引擎接口</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b26a2dfeff64457b9163fd61ffb41f34~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中<strong>连接管理</strong>与<strong>解析与优化</strong>处于<code>MySQL</code>架构中的<code>Server</code>层。</p>
<h1 data-id="heading-3">小结</h1>
<p>在学习任何知识前，先不要着急的陷入细节，而是先了解大致脉络，有个全局观，之后再去深入相关的细节。</p>
<p><code>MySql</code>架构分为<code>Server</code>层与<strong>存储引擎</strong>层。</p>
<p><strong>连接管理、解析与优化</strong>这些并不涉及读写表数据的组件划分到<code>Server</code>层，读写表数据而是交给<strong>存储引擎层</strong>来做。</p>
<p>通过这种架构设计，我们发现<code>Server</code>层其实就是公用层，<strong>存储引擎层</strong>就是多态层，按需选择具体的存储引擎。</p>
<p>再细想下，它和<strong>模板方法设计模式</strong>一摸一样，它们的执行流程是固定的，<code>Server</code>层等于公用模板函数，<strong>存储引擎层</strong>等于抽象模板函数，按需子类实现。</p>
<p>阿星最后以一张<code>MySQL</code>简化版的架构图结束本文，我们下期再见~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12cad21be64b4d9fa199217c2b3af6fc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>站在巨人的肩膀上：</p>
<ul>
<li>《MySQL实战45讲》</li>
<li>《从零开始带你成为MySQL实战优化高手》</li>
<li>《MySQL是怎样运行的：从根儿上理解MySQL》</li>
<li>《MySQL技术Innodb存储引擎》</li>
</ul>
<h1 data-id="heading-4">Java并发编程好文推荐</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FjuYh4j3fskCJL3Ph3rmhjw" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/juYh4j3fskCJL3Ph3rmhjw" ref="nofollow noopener noreferrer">33张图剖析ReentrantReadWriteLock源码</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FNvNWmqZzpbKGRLhBJq9GuA" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/NvNWmqZzpbKGRLhBJq9GuA" ref="nofollow noopener noreferrer">图文并茂的聊聊ReentrantReadWriteLock的位运算</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fks1-_tsTdWm1FEux42rgZw" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/ks1-_tsTdWm1FEux42rgZw" ref="nofollow noopener noreferrer">通俗易懂的ReentrantLock，不懂你来砍我</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FY4GbMdNmSDvHtomxtObRSg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/Y4GbMdNmSDvHtomxtObRSg" ref="nofollow noopener noreferrer">万字长文 | 16张图解开AbstractQueuedSynchronizer</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FxSro-bwg__ir9EXwoCJ-rg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/xSro-bwg__ir9EXwoCJ-rg" ref="nofollow noopener noreferrer">写给小白看的LockSupport</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FesLXkYi3KiYMxYDiVXSnkA" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/esLXkYi3KiYMxYDiVXSnkA" ref="nofollow noopener noreferrer">13张图，深入理解Synchronized</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FGR7lLGp9JH4bsAgQB3uLrw" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/GR7lLGp9JH4bsAgQB3uLrw" ref="nofollow noopener noreferrer">由浅入深CAS，小白也能与BAT面试官对线</a>0</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F48OLw2koXwrcJ5YOKSNmFw" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/48OLw2koXwrcJ5YOKSNmFw" ref="nofollow noopener noreferrer">小白也能看懂的Java内存模型</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FwoFmXOt5zOxidlkduIfruA" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/woFmXOt5zOxidlkduIfruA" ref="nofollow noopener noreferrer">保姆级教学，22张图揭开ThreadLocal</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FVDFANBzOG6GlSWCwW-vfGQ" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/VDFANBzOG6GlSWCwW-vfGQ" ref="nofollow noopener noreferrer">透彻Java线程状态转换</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FjhOSjVyRA6rNKqVT2pKMIQ" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/jhOSjVyRA6rNKqVT2pKMIQ" ref="nofollow noopener noreferrer">进程、线程与协程傻傻分不清？一文带你吃透！</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F_ATueOBN4UM2bim_1hDBFQ" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/_ATueOBN4UM2bim_1hDBFQ" ref="nofollow noopener noreferrer">什么是线程安全？一文带你深入理解</a></li>
</ul>
<h1 data-id="heading-5">关于我</h1>
<p>阿星是一个热爱技术的<code>Java</code>程序猿，公众号  <strong>「程序猿阿星」</strong> 定期分享有趣有料的精品原创文章！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93fb57a146a84ba9b361155d1c769797~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>非常感谢各位小哥哥小姐姐们能看到这里，原创不易，文章有帮助可以关注、点个赞、分享与评论，都是支持（莫要白嫖）！</p>
<p>愿你我都能奔赴在各自想去的路上，我们下篇文章见。</p></div>  
</div>
            