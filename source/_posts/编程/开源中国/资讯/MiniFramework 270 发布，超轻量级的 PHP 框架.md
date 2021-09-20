
---
title: 'MiniFramework 2.7.0 发布，超轻量级的 PHP 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1278'
author: 开源中国
comments: false
date: Sun, 19 Sep 2021 22:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1278'
---

<div>   
<div class="content">
                                                                                            <p>MiniFramework 2.7.0 已经发布，超轻量级的PHP框架。</p> 
<h1>版本变化</h1> 
<ul> 
 <li>新增常量 APP_ENV，默认值为"prod"，用于定义应用运行环境。</li> 
 <li>新增应用运行环境支持，可根据常量 APP_ENV 定义的环境加载对应的配置文件。</li> 
 <li>新增 join、innerjoin、leftjoin 和 rightjoin 连贯操作方法，用于联表查询。</li> 
 <li>新增 from 连贯操作方法，用于定义查询的数据表名（为符合使用习惯，封装了原 table 方法）。</li> 
 <li>新增通过 from 或 table 方法传入数组类型参数，对表名和别名进行定义的特性。</li> 
 <li>新增 debug 连贯操作方法，用于在执行数据库查询命令前输出显示最终拼装的 SQL 语句。</li> 
 <li>改进部分单例类，将 __clone 改为私有方法，防止由克隆引起的异常。</li> 
 <li>改进 Mini\Base\Model 类，取消自动追加"`"符号的特性，以增加兼容性。</li> 
 <li>修复 Mini\Base\Model::field() 方法遇到传入"*"时处理保留字的 Bug。</li> 
</ul> 
<h1>升级说明</h1> 
<ul> 
 <li>兼容 PHP 最低版本为 7.2.0，PHP 8.0.0 已测试可正常运行。</li> 
 <li>当前版本向前兼容至 V2.4.0 版本，使用 V2.4.0 及后续版本的开发者可直接升级至 V2.7.0 版本。</li> 
 <li>文档已同步更新，地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.miniframework.com%2Fdocv2%2Fguide%2F" target="_blank">http://www.miniframework.com/docv2/guide/</a></li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/jasonwei/miniframework/releases/2.7.0">https://gitee.com/jasonwei/miniframework/releases/2.7.0</a></p>
                                        </div>
                                      
</div>
            