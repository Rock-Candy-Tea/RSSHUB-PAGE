
---
title: 'Oracle云时代MySQL HTAP解决方案'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c85bb91e82b43f0ae2a31e54f58d102~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 02:35:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c85bb91e82b43f0ae2a31e54f58d102~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Oracle Cloud 在2020年终于大张旗鼓的上线了推动，终于搞出来一个本地MySQL和线上MySQL大差异点云上HTAP MySQL方案：MySQL HeatWave。架构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c85bb91e82b43f0ae2a31e54f58d102~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>      在MySQL HeatWave架构下实现了数据请求单一入口，数据写入先写InnoDB，如果该表定义为Rapid引擎，同时从会InnoDB则推送给HeatWave; 对于SELECT请求，优化器会判断，如果从InnoDB中请求快，则从InnoDB层请求数据返回，如果涉及到复杂运算则从HeatWave中请求及返回。可以说这个结构是行(InnoDB)+列（HeatWave)混合存储的结构，同一个架构完美解决OLTP，OLAP需求（感觉也是一个高富帅的解决方法），从油管上看BenchMark基本是同行业无敌。</p>
<p>这里大概也罗列一下HeatWave的一些限制，供使用者一些参考：</p>
<p>1.  HeatWave Cluster目前支持最多24个节点，每个节点最大内存420G，共9T数据，Rapid引擎数据在内存中，Youtube上有一些详细介绍，自行翻墙观看。</p>
<p>2. HeatWave只能处理SELECT请求</p>
<p>3. 表的数据需要自动用HeatWave处理的，引擎需要改为：rapid为第二个引擎，数据还是持久化在InnoDB中, 对于不支持的列需要定义加上：not secondary 参考支持的数据类型： </p>
<p><a href="https://dev.mysql.com/doc/heatwave/en/heatwave-supported-data-types.html" target="_blank" rel="nofollow noopener noreferrer">dev.mysql.com/doc/heatwav…</a></p>
<p>4. 表引擎没有指定为Rapid的，如果想用HeatWave，需要手工加载到HeatWave中，如：alter table TBname secondary_load;</p>
<p>因为这个架构是基于云上基础能力开发的架构，目前没办法线下部署想体验，只能用Oracle Cloud上的MySQL  Service，在Oracle MySQL Service中也可以看到低于9T的数据，HTAP基本随意造了。</p>
<p>如果你没办法使用Oracle Cloud，也可以考虑使用clickhouse扮演一部分这个功能，参考：<a href="https://clickhouse.tech/docs/en/engines/database-engines/materialize-mysql/" target="_blank" rel="nofollow noopener noreferrer">clickhouse.tech/docs/en/eng…</a></p>
<p>用好这个功能也可以给MySQL手工安装一个OLAP的翅膀。</p></div>  
</div>
            