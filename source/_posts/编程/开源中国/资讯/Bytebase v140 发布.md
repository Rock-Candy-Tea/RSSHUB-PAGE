
---
title: 'Bytebase v1.4.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9377183461c5c5bf0975af11988833264f3.gif'
author: 开源中国
comments: false
date: Sat, 17 Sep 2022 07:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9377183461c5c5bf0975af11988833264f3.gif'
---

<div>   
<div class="content">
                                                                                            <p>Bytebase 是一个基于网络、零配置、无依赖的数据库 Schema 变更和版本控制管理工具，适用于开发人员和 DBA。</p> 
<p>Bytebase 1.4.0 发布，更新内容如下：</p> 
<h3><strong>新功能</strong></h3> 
<ul> 
 <li>支持将数据库备份存储到 AWS S3</li> 
 <li>新增新手引导</li> 
</ul> 
<p><img alt height="391" src="https://oscimg.oschina.net/oscnet/up-9377183461c5c5bf0975af11988833264f3.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3><strong>改进</strong></h3> 
<ul> 
 <li>启动命令选项中引入了 <code>--external-url</code>，并且移除了 <code>--host</code>。由此统一了如何配置供外部访问的 URL方式。</li> 
</ul> 
<p><img alt height="273" src="https://oscimg.oschina.net/oscnet/up-fe8f10b948674680732b321b1c0cbccf87b.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>VCS 中 File path template 里 &#123;&#123;TYPE&#125;&#125; 字段支持使用 DDL 和 DML</li> 
 <li>MySQL 备份中支持视图</li> 
 <li>显示 PITR 还原任务的进度</li> 
 <li>提升了 SQL Editor 查询结果表格的性能</li> 
 <li>SQL Editor 查询结果表格支持调整列宽</li> 
 <li>改善了 SQL Editor tab 栏的交互</li> 
 <li>将语句类型检查的错误级别从「错误级别」调整至「默认级别」</li> 
</ul> 
<h3><strong>Bug 修复</strong></h3> 
<ul> 
 <li>修复了在 VCS 中新增使用已有变更版本的文件时，工单显示为成功但是并未执行的问题。</li> 
 <li>通过 VCS 方式做数据库变更时，点击需变更的数据库后按照「文件路径模板」跳转到 VCS。</li> 
 <li>项目 key 不能为空</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytebase%2Fbytebase%2Freleases%2Ftag%2F1.4.0" target="_blank">https://github.com/bytebase/bytebase/releases/tag/1.4.0</a></p>
                                        </div>
                                      
</div>
            