
---
title: 'PHP 8.1 进入 Alpha 阶段，旧版本发布安全更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4601'
author: 开源中国
comments: false
date: Sat, 03 Jul 2021 07:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4601'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PHP 8.1 已进入 Alpha 阶段，8.1 将是继 8 之后的又一个重要版本更新。</p> 
<p>主要变化如下：</p> 
<ul> 
 <li>完成枚举功能 (Enums)，具体细节<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Fenumerations">查看 RFC</a></li> 
 <li>引入 fsync() 函数，用于帮助确保操作系统将数据变化（以及元数据）写入底层存储，以及新的相似 fdatasync() 函数确保同步数据（非元数据）</li> 
 <li>支持 Fibers 以改进 PHP 中的异步机制。PHP Fibers 可保证 PHP 函数在不污染调用堆栈的情况下被中断，并支持现有接口的透明非阻塞 I/O 实现</li> 
 <li>支持将更多 PHP 资源转换为对象</li> 
 <li>PHP-FPM 支持在 macOS 上对进程进行重命名</li> 
 <li>通过哈希接口 (hashing interface) 支持 MurmurHash V3 和 xxHash</li> 
 <li>PHP Sodium 支持 XChaCha20 流加密函数和 Ristretto255 函数</li> 
 <li>PHP OPcache 包含继承缓存 (inheritance cache)</li> 
 <li>持续的性能优化</li> 
 <li>……</li> 
</ul> 
<p>目前 PHP 8.1 Alpha 2 已发布，下一个版本 Alpha 3 计划于 2021 年 7 月 8 日发布。在此之后，将会进入功能冻结 (Feature Freeze) 阶段。该阶段之后在 8 月中旬前还将会发布 3 个 Beta 版本，9 月起陆续推出多个候选版本，正式 GA 的时间暂定于今年 11 月月底。</p> 
<p>最后，PHP 旧版本的三个分支也发布了安全更新，分别是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.php.net%2Farchive%2F2021.php%232021-07-01-3" target="_blank">PHP 7.4.21</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.php.net%2Farchive%2F2021.php%232021-07-01-2" target="_blank">PHP 8.0.8</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.php.net%2Farchive%2F2021.php%232021-07-01-1" target="_blank">PHP 7.3.29</a>。</p>
                                        </div>
                                      
</div>
            