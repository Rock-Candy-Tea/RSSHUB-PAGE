
---
title: 'MySQL 8.0.28 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1142'
author: 开源中国
comments: false
date: Thu, 20 Jan 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1142'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0">MySQL 8.0.28 于 2022 年 1 月 18 日正式 GA。这是一个维护版本，在这个版本里除了进行 Bug 修复，还进行了一些功能增强与调整。详细内容如下：</p> 
<ul> 
 <li>InnoDB 支持使用“ALGORITHM=INSTANT”在线执行“ALTER TABLE ... RENAME COLUMN”。</li> 
 <li>“innodb_open_files”变量用来定义 InnoDB 一次可以打开文件的数量，现在支持使用 SELECT innodb_set_open_files_limit(N) 语句设置。</li> 
 <li>函数 FROM_UNIXTIME(), UNIX_TIMESTAMP(), 和 CONVERT_TZ() 可以处理 64 位的值，FROM_UNIXTIME() 最大 32536771199.999999 seconds 秒，对应'3001-01-18 23:59:59.999999' UTC。UNIX_TIMESTAMP() 最大值'3001-01-18 23:59:59.999999' UTC,对应 32536771199.999999 秒。CONVERT_TZ() 执行 2038 以上的时区转换，最大'3001-01-18 23:59:59.999999' UTC.</li> 
 <li>增加状态变量“Global_connection_memory”用来观察所有用户连接所消耗的总内存。通过设置“connection_memory_limit”，可以指定每个用户连接的资源消耗限制。</li> 
 <li>AUDIT_ABORT_EXEMPT 权限允许用户的查询总是被执行，以防止具有充足权限的用户利用 MySQL Enterprise Audit 的错误地在审计日志筛选器中创建一个“abort”项，阻止自己和其他管理员访问系统。</li> 
 <li>当禁用系统变量“read_only”时，服务器会按需自动重启事件调度器。</li> 
 <li>使用预编译语句时，DATE_ADD() 和 DATE_SUB() 返回 DATETIME 值，即使计算中包含 YEAR, MONTH, 或 DAY 不包含时间部分。</li> 
</ul> 
<p style="margin-left:0"><strong>降级&删除</strong></p> 
<ul> 
 <li> 删除对 TLSv1 和 TLSv1.1 的支持。</li> 
 <li>字符集 latin1 的快捷方式 ASCII 和 UNICODE 的快捷方式 ucs2 被弃用，MySQL 的未来版本中将删除它们。用户可以使用 CHARACTER SET 代替。</li> 
 <li>字符集及排序规则 ucs2、macroman、macce、dec、p8 将降级，未来将删除。用户可以使用 utf8mb4 代替。</li> 
</ul> 
<p style="margin-left:0">更多详细内容<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.oracle.com%2Fmysql%2Fpost%2Fannouncing-january-2022-releases-featuring-mysql-8028" target="_blank">可访问官网</a>。</p>
                                        </div>
                                      
</div>
            