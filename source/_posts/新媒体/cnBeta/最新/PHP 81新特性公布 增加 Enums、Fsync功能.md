
---
title: 'PHP 8.1新特性公布 增加 Enums、Fsync功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0404/a7b3f0cbc28f841.png'
author: cnBeta
comments: false
date: Sun, 04 Apr 2021 11:45:49 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0404/a7b3f0cbc28f841.png'
---

<div>   
当大多数人的Linux 发行版的默认包中还没有升级到PHP 8.0，更不用说在生产环境中了，PHP 8.1
正在开发中，预计正式发布时间在11月底左右。日程安排和大多数年份一样，在连续发布三个双周的Alpha版本之后，PHP 8.1
功能冻结预计在七月底，然后再进入测试版，然后是许多候选版本。<br>
 <p><strong>如果一切顺利，PHP 8.1.0将在11月25日发布。至于 PHP 8.1 将会带来什么，到目前为止，已知的变化包括：</strong></p><p>- Enums 将被引入。PHP 终于在语言中引入了枚举。关于新增的细节可以通过这个 RFC 找到：<a href="https://wiki.php.net/rfc/enumerations" _src="https://wiki.php.net/rfc/enumerations" target="_blank">https://wiki.php.net/rfc/enumerations</a><br></p><p>- PHP 8.1 引入了 fsync() 函数，以帮助确保操作系统已经将数据变化（和 metdata）写入底层存储。还有一个新的fdatasync()函数只关注同步数据，而不是元数据--或者说在<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>/非POSIX环境下的行为与fsync()相同。</p><p>- PHP性能改进的工作继续进行，带来更多的优化。到目前为止，其中一个细节是 PHP 8.1 opcache 增加了一个继承缓存，这应该有助于减少PHP类继承的开销。</p><p>- 增加了对 "Fibers"的支持，以改善PHP中的异步支持。这些变化使得 PHP 函数现在可以在不污染调用栈的情况下完成中断，并且支持现有接口的透明非阻塞 I/O 实现。</p><p>- PHP 8.1 散列代码增加了 xxHash 和 MurmurHash V3 支持。</p><p>- 继续PHP8的工作，将更多的资源过渡到对象。对于 PHP 8.1，fileinfo、GD、FTP、IMAP、LDAP 和其他代码的资源将会被过渡到对象。</p><p>随着11月发布日期的临近，请继续关注PHP 8.1功能工作的更多细节。</p><p><a href="https://static.cnbetacdn.com/article/2021/0404/a7b3f0cbc28f841.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0404/a7b3f0cbc28f841.png" title alt="C@&#123;G8)AOL(RG1&#123;Q[$F~(KIO.png" referrerpolicy="no-referrer"></a></p>   
</div>
            