
---
title: '全量同步Elasticsearch方案之Canal'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc658b0257964160b57657368e8ce763~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 17:24:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc658b0257964160b57657368e8ce763~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc658b0257964160b57657368e8ce763~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、前言</h2>
<p><code>Canal</code> 是阿里的一款开源项目，纯 <code>Java</code> 开发。基于数据库增量日志解析，提供增量数据订阅&消费，目前主要支持了 <code>MySQL</code>(也支持 <code>mariaDB</code>)。</p>
<p><img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f536061fd084ca280e2aeeb3cc6c4c2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>Canal</code> 除了支持 <code>binlog</code> 实时 <strong>增量同步</strong> 数据库之外也支持 <strong>全量同步</strong> ，本文主要分享使用Canal来实现从MySQL到Elasticsearch的全量同步；</p>
<p>可通过使用 <code>adapter</code> 的 <code>REST</code> 接口手动触发 <code>ETL</code> 任务，实现全量同步。</p>
<blockquote>
<p>在执行全量同步的时候，同一个 <code>destination</code> 的增量同步任务会被 <strong>阻塞</strong>，待全量同步完成被阻塞的增量同步会被 <strong>重新唤醒</strong></p>
</blockquote>
<p><strong>PS</strong>：关于Canal的部署与 <strong>实时同步</strong> 请看文章《<a href="https://mp.weixin.qq.com/s/QwvmxqxXirjf-J6mqYY44Q" target="_blank" rel="nofollow noopener noreferrer">Canal高可用架构部署</a>》</p>
<p> </p>
<h2 data-id="heading-1">二、ETL接口</h2>
<p><code>adapter</code> 的 <code>ETL</code> 接口为：<code>/etl/&#123;type&#125;/&#123;task&#125;</code></p>
<ul>
<li>默认web端口为 <code>8081</code></li>
<li><strong>type</strong> 为类型(hbase/es7/rdb)</li>
<li><strong>task</strong> 为任务名对应配置文件名，如sys_user.yml</li>
</ul>
<p> </p>
<p><strong>例子</strong>：</p>
<pre><code class="hljs language-bash copyable" lang="bash">curl -X POST http://127.0.0.1:8081/etl/es7/sys_user.yml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行成功输出：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;<span class="hljs-attr">"succeeded"</span>:<span class="hljs-literal">true</span>,<span class="hljs-attr">"resultMessage"</span>:<span class="hljs-string">"导入ES 数据：17 条"</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h2 data-id="heading-2">三、实践过程中遇到的坑</h2>
<h3 data-id="heading-3">3.1. 连接池不够</h3>
<p>当同步的数据量比较大时，执行一段时间后会出现下图的错误
<img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bb1ec6bccf54a768704496e704968d0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">3.1.1. 原因分析</h4>
<p>查看 <code>canal</code> 源码得知当同步的数据量大于1w时，会分批进行同步，每批1w条记录，并使用多线程来并行执行任务，而 <code>adapter</code> 默认的连接池为3，当线程获取数据库连接等待超过1分钟就会抛出该异常。</p>
<blockquote>
<p>线程数为当前服务器cpu的可用线程数</p>
</blockquote>
<p> </p>
<h4 data-id="heading-5">3.1.2. 解决方式</h4>
<p>修改 <code>adapter</code> 的 <code>conf/application.yml</code> 文件中的 <code>srcDataSources</code> 配置项，增加 <code>maxActive</code> 配置数据库的最大连接数为当前服务器cpu的可用线程数</p>
<p>cpu线程数可以下命令查看</p>
<pre><code class="hljs language-bash copyable" lang="bash">grep <span class="hljs-string">'processor'</span> /proc/cpuinfo | sort -u | wc -l
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h3 data-id="heading-6">3.2. es连接超时</h3>
<p>当同步的表字段比较多时，几率出现以下报错
<img alt="mark" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/268d9f6dffcc444981f84bf46fcd1181~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">3.2.1. 原因分析</h4>
<p>由于 <code>adapter</code> 的表映射配置文件中的 <code>commitBatch</code> 提交批大小设置过大导致(6000)</p>
<p> </p>
<h4 data-id="heading-8">3.2.2. 解决方式</h4>
<p>修改 <code>adapter</code> 的 <code>conf/es7/xxx.yml</code> 映射文件中的 <code>commitBatch</code> 配置项为3000</p>
<p> </p>
<h3 data-id="heading-9">3.3. 同步慢</h3>
<p>三千万的数据量用时3.5小时左右</p>
<h4 data-id="heading-10">3.3.1. 原因分析</h4>
<p><img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70e9c31372074ff691c37f6048e48788~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>由于当数据量大于1w时 <code>canal</code> 会对数据进行分批同步，每批1w条通过分页查询实现；所以当数据量较大时会出现深分页的情况导致查询非常慢。</p>
<p> </p>
<h4 data-id="heading-11">3.3.2. 解决方式</h4>
<p>预先使用ID、时间或者业务字段等进行数据分批后再进行同步，减少每次同步的数据量。</p>
<p> </p>
<h4 data-id="heading-12">3.3.3. 案例</h4>
<p>使用ID进行数据分批，适合增长类型的ID，如自增ID、雪花ID等；</p>
<ol>
<li>查出 <strong>最小ID</strong>、<strong>最大ID</strong> 与 <strong>总数据量</strong></li>
<li>根据每批数据量大小计算每批的 <strong>ID区间</strong></li>
</ol>
<p> </p>
<p><strong>计算过程</strong>：</p>
<ul>
<li>最小ID = 1333224842416979257</li>
<li>最大ID = 1341698897306914816</li>
<li>总数据量 = 3kw</li>
<li>每次同步量 = 300w</li>
</ul>
<p> </p>
<p><strong>(1) 计算同步的次数</strong></p>
<pre><code class="hljs language-math copyable" lang="math">总数据量 / 每次同步量 = 10
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p><strong>(2) 计算每批ID的增量值</strong></p>
<pre><code class="hljs language-math copyable" lang="math">(最大ID - 最小ID) / 次数 = 847405488993555.9
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p><strong>(3) 计算每批ID的值</strong></p>
<pre><code class="hljs language-math copyable" lang="math">最小ID + 增量值 = ID2

ID2 + 增量值 = ID3

...

ID9 + 增量值 = 最大ID
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p><strong>(4) 使用分批的ID值进行同步</strong></p>
<p>修改sql映射配置，的 <code>etlCondition</code> 参数：</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">etlCondition:</span> <span class="hljs-string">"where id >= &#123;&#125; and id < &#123;&#125;"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p>调用etl接口，并增加 <code>params</code> 参数，多个参数之间使用 <code>;</code> 分割</p>
<pre><code class="hljs language-bash copyable" lang="bash">curl -X POST http://127.0.0.1:8081/etl/es7/sys_user.yml?params=最小ID;ID2

curl -X POST http://127.0.0.1:8081/etl/es7/sys_user.yml?params=ID2;ID3

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p><strong>扫码关注有惊喜！</strong></p>
<p><img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fe9275c0a1348ed978bc060e8b6aff9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            