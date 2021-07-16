
---
title: '_JDBC_ Kettle on MaxCompute 使用指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3fd033195454e25a1269ca57d0e6dd0~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 19:37:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3fd033195454e25a1269ca57d0e6dd0~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> Kettle是一款开源的ETL工具，纯Java实现，可以在Windows、Unix和Linux上运行，提供图形化的操作界面，可以通过拖拽控件的方式，方便地定义数据传输的拓扑 。基本讲介绍基于Kettle的MaxCompute插件实现数据上云。</p>
<p>Kettle版本：8.2.0.0-342</p>
<p>MaxCompute JDBC driver版本：3.2.8</p>
<h1 data-id="heading-0">Setup</h1>
<ol>
<li>下载并安装Kettle</li>
<li>下载MaxCompute JDBC driver</li>
<li>将MaxCompute JDBC driver置于Kettle安装目录下的lib子目录（data-integration/lib）</li>
<li>下载并编译MaxCompute Kettle plugin：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faliyun%2Faliyun-maxcompute-data-collectors" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/aliyun/aliyun-maxcompute-data-collectors" ref="nofollow noopener noreferrer">github.com/aliyun/aliy…</a></li>
<li>将编译后的MaxCompute Kettle plugin置于Kettle安装目录下的lib子目录（data-integration/lib）</li>
<li>启动spoon</li>
</ol>
<h1 data-id="heading-1">Job</h1>
<p>我们可以通过Kettle + MaxCompute JDBC driver来实现对MaxCompute中任务的组织和执行。</p>
<p>首先需要执行以下操作：</p>
<ol>
<li>新建Job</li>
<li>新建Database Connection<br>
JDBC连接串格式为：jdbc:odps:?project=<br>
JDBC driver class为：com.aliyun.odps.jdbc.OdpsDriver<br>
Username为阿里云AccessKey Id<br>
Password为阿里云AccessKey Secret<br>
JDBC更多配置见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelp.aliyun.com%2Fdocument%255C_detail%2F161246.html" target="_blank" rel="nofollow noopener noreferrer" title="https://help.aliyun.com/document%5C_detail/161246.html" ref="nofollow noopener noreferrer">help.aliyun.com/document\_d…</a></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3fd033195454e25a1269ca57d0e6dd0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>之后，可以根据业务需要，通过SQL节点访问MaxCompute。下面我们以一个简单的ETL过程为例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64d2e7e37da249528367a89e66e5e4f5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Create table节点的配置如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/beb4f544e03f48c5938ca537bfee97ca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要注意：</p>
<ol>
<li>这里Connection需要选择我们配置好的</li>
<li>不要勾选Send SQL as single statement</li>
</ol>
<p>Load from OSS节点配置如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aef5f95135be4ac28c060eb3ab780ae6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要注意的点同Create table节点。有关更多Load的用法，见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelp.aliyun.com%2Fdocument%255C_detail%2F157418.html" target="_blank" rel="nofollow noopener noreferrer" title="https://help.aliyun.com/document%5C_detail/157418.html" ref="nofollow noopener noreferrer">help.aliyun.com/document\_d…</a></p>
<p>Processing节点配置如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78b568ecde264b338fd554d83b4cf75b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要注意的点同Create table节点。</p>
<h1 data-id="heading-2">Transformation</h1>
<p>我们可以通过MaxCompute Kettle plugin实现数据流出或流入MaxCompute。</p>
<p>首先新建Transformation，之后新建Aliyun MaxCompute Input节点，配置如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4cc326f66c3402089aa6cf9532280ff~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在MaxCompute中新建一张空表，schema与test_partition_table一致。</p>
<p>新建Aliyun MaxCompute Output节点，配置如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f9445ca7026412ba2a185012764db9f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行Transformation，数据便从test_partition_table被下载，后被上传至test_partition_table_2。</p>
<h1 data-id="heading-3">其他</h1>
<p><strong>置MaxCompute flags设</strong></p>
<p>如图，在执行DDL/DML/SQL之前，可以通过set key=value;的方式配置flags。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbd69c3bdafc46dba770520332aa1d14~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Script模式</strong></p>
<p>暂时无法支持</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000284018%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000284018/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            