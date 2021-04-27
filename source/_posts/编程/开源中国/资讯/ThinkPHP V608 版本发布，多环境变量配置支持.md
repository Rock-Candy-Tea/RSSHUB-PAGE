
---
title: 'ThinkPHP V6.0.8 版本发布，多环境变量配置支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6417'
author: 开源中国
comments: false
date: Tue, 27 Apr 2021 10:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6417'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <h3><code>V6.0.8</code>版本发布，本版本为常规更新，主要做了一些完善，尤其是对多环境变量配置的支持，以及增加了一个<code>LogRecord</code>事件。</h3> 
</blockquote> 
<h2 style="text-align:start">主要更新</h2> 
<ul> 
 <li>增加<code>LogRecord</code>事件</li> 
 <li>消除<code>Validate</code>类某处类型声明警告</li> 
 <li>路由分组增加<code>dispatcher</code>方法，支持设置分组的调度</li> 
 <li><code>Request</code>类增加<code>all</code>方法支持获取包括<code>File</code>在内的所有参数</li> 
 <li>改进环境变量定义支持多<code>env</code>文件读取</li> 
</ul> 
<p style="text-align:start"><code>ThinkORM</code>近期主要更新：</p> 
<ul> 
 <li>兼容 <code>symfony/cache</code> 组件规则，不能在 key 或 tag 中使用的保留字符<code>&#123;&#125;()/@:</code></li> 
 <li>调整修改器和类型转换的处理机制</li> 
 <li>改进关联查询</li> 
 <li>改进多次查询的时候<code>field</code>方法失效问题</li> 
 <li><code>MorphOne</code>关联支持绑定关联模型属性</li> 
 <li>修正<code>parseIn</code>方法</li> 
 <li>改进<code>__unset</code>方法</li> 
 <li>修正异常类注解</li> 
 <li><code>Connection->link*</code>属性补充类型注解</li> 
 <li>composer.json 声明 pdo 扩展是必须的</li> 
 <li>优化独立运行所需的兼容类</li> 
 <li>完善事务中的断连重试处理，避免数据污染</li> 
 <li>修复7.4以下版本存在无法把PDO警告转换为异常导致不兼容问题</li> 
 <li>修正<code>phpunit</code>兼容性</li> 
 <li>改进获取器</li> 
 <li>改进<code>getRealsql</code>方法处理</li> 
 <li>导出包时忽略掉不必要的文件</li> 
 <li>增强 <code>column</code>方法</li> 
 <li>改进模型的<code>getBindAttr</code>方法和获取器冲突问题</li> 
 <li>增加获取器场景功能</li> 
 <li>补充数据集方法</li> 
 <li>增加模型输出的场景设置功能 支持hidden visible append</li> 
 <li>改进 <code>WhereIn</code>空数组查询</li> 
 <li>改进<code>trigger</code></li> 
</ul> 
<h2 style="text-align:start">安装和更新</h2> 
<p style="text-align:start"><code>V6</code>版本开始仅支持<code>Composer</code>安装及更新，支持上个版本的无缝更新，直接使用</p> 
<pre style="text-align:start"><code>composer update
</code></pre> 
<p style="text-align:start">更新到最新版本即可。</p> 
<p style="text-align:start">如果需要全新安装，使用：</p> 
<pre style="text-align:start"><code>composer create<span style="background-color:rgba(255, 255, 255, 0.5)">-</span>project topthink<span style="background-color:rgba(255, 255, 255, 0.5)">/</span>think tp
</code></pre> 
<h2 style="text-align:start">官方文档</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fmanual%2Fthinkphp6_0%2Fcontent" target="_blank">官方<code>6.0</code>完全开发手册</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fthinkphp%2Fthinkphp6-quickstart" target="_blank"><code>6.0</code>入门必读教程</a></li> 
</ul>
                                        </div>
                                      
</div>
            