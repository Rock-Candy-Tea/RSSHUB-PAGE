
---
title: 'Redis 7.0即将迎来_重大性能优化_'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0813/0b4bfb7099eec7a.png'
author: cnBeta
comments: false
date: Tue, 01 Feb 2022 01:06:31 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0813/0b4bfb7099eec7a.png'
---

<div>   
本周一，Redis 7.0 迎来了首个候选发布（RC）版本。<strong>可知这款内存键值数据库迎来了“重大的性能优化”和其它功能改进，但也有些影响到了这款流行的开源项目的向后兼容性支持。</strong>性能调教包括通过各种优化来“显著”节省内存资源、降低写入时复制内存的开销、提升内存效率，改进 fsync 来避免大量的磁盘写入和优化延迟表现。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0813/0b4bfb7099eec7a.png" referrerpolicy="no-referrer"></p><p>Redis 7.0-rc1 的其它一些变动，包括将“Redis 函数”作为新的服务器端脚本功能，细粒度 / 基于键的权限、改进子命令处理 / Lua 脚本 / 各种新命令。</p><p>此外此群代码现也支持主机名（而不仅仅是 IP 地址），辅以针对默认阻止的敏感配置 / 命令的安全改进、避免记录 auth-pass 值等。</p><p>最后，<a href="https://www.phoronix.com/scan.php?page=news_item&px=Redis-7.0-rc1" target="_self">Phoronix</a> 将于稳定版发布后再开展 Redis 7.0 的基准测试报告。等不及的朋友，可先通过 <a href="https://github.com/redis/redis/releases/tag/7.0-rc1" target="_self">GitHub</a> 获取 Redis 7.0-rc1 测试版进行体验。</p>   
</div>
            