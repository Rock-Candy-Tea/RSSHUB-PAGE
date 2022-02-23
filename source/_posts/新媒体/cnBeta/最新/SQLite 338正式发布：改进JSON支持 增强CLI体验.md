
---
title: 'SQLite 3.38正式发布：改进JSON支持 增强CLI体验'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0223/0d4afc0d5173a2a.png'
author: cnBeta
comments: false
date: Wed, 23 Feb 2022 08:31:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0223/0d4afc0d5173a2a.png'
---

<div>   
SQLite 是一个小型、快速、自包含、高可靠性、全功能的嵌入式 SQL 数据库引擎。早在 2015 年发布的 SQLite 3.9 版本中，开发者就已经为它添加了对 JSON1 模块的支持。<strong>现在，随着 2022 年首个重大更新的发布，该模块已在 SQLite 3.38 中被默认包含、而无需启用编译时选项。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0223/0d4afc0d5173a2a.png" referrerpolicy="no-referrer"></p><p>SQLite 3.38 还引入了 -> 和 ->> 操作符，以便更轻松地处理 JSON 数据、并且兼容 MySQL 和 PostgreSQL 数据库的使用方式。</p><p>这些运算符可将 JSON 字符串作为左操作数，将路径表达式 / 对象字段标签（或数组索引）作为右操作数，以简化用户的使用体验。</p><blockquote><p>此外 SQLite 3.38 添加了用于返回 Unix 时间戳的 unixepoch() 函数、用于将 SQL 错误本地化为特定字符的 sqlite3_error_offset() 。</p><p>以及各种虚拟表改进和命令行增强，比如列输出（columnar output）模式现可正确处理文本中的制表符 / 换行符。</p><p>查询规划器（query planner）等增强功能方面，SQLite 3.38 现也使用布隆过滤（bloom filter）来加速大型分析查询。</p></blockquote><p>总体而言，作为 2022 年的首个新版，3.38 也是 SQLite 的一次盛大更新。</p><p>感兴趣的朋友，可移步至 SQLite.org 官网（<a href="https://sqlite.org/releaselog/3_38_0.html" target="_self">传送门</a>），以获取有关这款嵌入式数据库的更多详细信息。</p><p><strong>下载地址（2022-02-22 / Version 3.38.0）：</strong></p><blockquote><p><a href="https://www.sqlite.org/download.html" _src="https://www.sqlite.org/download.html" target="_blank">https://www.sqlite.org/download.html</a></p></blockquote>   
</div>
            