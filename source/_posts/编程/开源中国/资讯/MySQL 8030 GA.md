
---
title: 'MySQL 8.0.30 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6125'
author: 开源中国
comments: false
date: Thu, 28 Jul 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6125'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#222222">MySQL 8.0.30 现已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.oracle.com%2Fmysql%2Fpost%2Fannouncing-july-2022-releases-featuring-mysql-8030" target="_blank">发布</a>。此版本在做了大量的修复的同时，也对一些功能进行了增强和改善。一些亮点内容如下：</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong>GIPK（<span style="color:#333333">Generated Invisible Primary Keys</span>）</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">当开启GIPK模式后，可以允许没有显示定义主键的InnoDB表，自动生成不可见的主键。生成的主键名称为 ‘my_row_id’ 并且无法更改，用户需要注意该关键字的使用。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong>XA 事务与复制</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">复制功能支持将XA事务的状态进行复制，解决了以往的复制功能<span>在</span><span>服务器节点出现异常时，无法保证</span><span>执行XA PREPARE、XA COMMIT或XA ROLLBACK</span><span>。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">对于任何多服务器复制拓扑(包括组复制<span>)， XA事务状态可以</span><span>一致地传播，以便所有服务器</span><span>始</span><span>终处于同一状态。</span><span>对于任意的拓扑结构</span><span>(包括单个服务器，只要</span><span>启用了二进制日志记录)，就可以</span><span>恢复到一致状态。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong>InnoDB doublewrite buffer</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">增加了I<span>nnodb_doublewrite系统变量，该变量可以设置为</span>DETECT_ONLY 或 DETECT_AND_RECOVER。设置为<span style="color:#333333">D</span><span style="color:#333333">ETECT_ONLY时，</span><span>数据库页面内容不会写入</span><span>doublewrite<span> </span><span style="color:#333333">buffer</span>，恢复时也不使用</span><span><span style="color:#333333">doublewrite </span><span style="color:#333333">buffer </span>修复不完整的页面写入。</span>该设置仅用于检测不完整页面写入。设置为DETECT_AND_RECOVER时，与现有的处理保持一致。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong>动态配置 Redo 日志容量</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">Redo日志现在支持动态设置容量。通过系统变量<span>innodb_redo_log_capacity</span><span> 可以增加或缩小Redo日志所使用的磁盘容量。InnoDB可以维护32个Redo日志，日志的默认大小为100M。用户配置</span>innodb_redo_log_capacity后，变量<span>innodb_log_files_in_group 和 innodb_log_file_size的值将被忽略。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong>更改 MySQL 部分系统表主键中的字段顺序</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">通过更改，以提高执行CREATE USER，DROP <span>USER，RENAME USER 语句的执行性能</span><span> </span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong>mysqldump 自定义长查询时间</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">mysqldump增加一个新的选项 -mysqld-long-query-time ，通过该选项，用户可以<span>增加</span><span>mysqldump查询所允许的经过时间</span><span>，以便</span><span>避免写入慢查询日志，从而减少不必要的日志记录。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong><span>Error log 组件</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">错误日志组件现在可以<span>在InnoDB存储引擎可用之前启动。</span><span>这种加载错误日志组件的</span><span>控件方法通过log_error_services变量定义。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">隐式加载错误日志组件具有如下<span>优点:</span></p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>InnoDB完全可用之前记录的信息</span><span>是可用的。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>它有助于避免日志信息的丢失</span><span>启动失败。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>显式错误日志组件安装使用</span><span>不再需要安装组件语法。用户</span><span>只需要将组件添加到</span><span>log_error_services设置。</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong><span>企业版审计</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>审计日志增加了查询时间选项，可以记录发送和接收的记录数及时间。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong><span>加密函数 </span><span>AES_ENCRYPT() 和 AES_DECRYPT()</span><span> 支持 KDF</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>KDF</span>（key derivation function）通过将<span>秘钥</span><span>密码或密码短语等信息</span>传递给函数，<span>用</span><span>来</span><span>创建密码学上的强密码</span><span>。</span><span>派生的密钥用于加密</span><span>并解密数据，它仍然保存在MySQL服务器中</span><span>实例，</span><span>用户无法访问。</span><span>强烈推荐<span style="color:#333333">使用KDF</span>，因为它提供了比</span><span>用户指定密码等方式</span><span>更为简单的方法，及更好的安全性。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">更多详细内容</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.oracle.com%2Fmysql%2Fpost%2Fannouncing-april-2022-releases-featuring-mysql-8029" target="_blank">可访问官网</a><span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">稿源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fh5l811FMpZH4xm6ATvU9tA" target="_blank">https://mp.weixin.qq.com/s/h5l811FMpZH4xm6ATvU9tA</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            