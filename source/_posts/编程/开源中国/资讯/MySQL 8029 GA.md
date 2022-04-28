
---
title: 'MySQL 8.0.29 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7418'
author: 开源中国
comments: false
date: Thu, 28 Apr 2022 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7418'
---

<div>   
<div class="content">
                                                                    
                                                        <p>MySQL 的最新版本 8.0.29 于 2022 年 4 月 26 日正式发行（GA）。<span>MySQL8.0 发布至今已经历 4 年（2018 年 4 月 19 日 GA），已经进入了标准生命周期的末期，如果你还在继续使用 MySQL 5.7 版本，甚至是 5.6 版本，现在应该认真考虑未来的数据库安全问题。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>MySQL 8.0.29 是一个维护版本，在这个版本里面做了大量的缺陷修复以及少数的改进，让我们快速浏览一下。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong>缺陷修复</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">MySQL8.0.29修复了160个缺陷与错误，特别感谢Yuhui Wang和中国移动的Bin Wang，他们为MySQL贡献了两处修复代码。欢迎广大爱好者持续为MySQL提交错误报告和缺陷修复。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong><span>功能改进</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>MySQL8.0.29中做了少量的功能改进，包括未来版本中将使用的基础功能及将弃用的功能。用户需要注意如下内容：</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>字符串：服务器在使用“SHOW”语句输出、及报告无需字符时，使用utf8mb3代替之前使用的utf8。此外，服务器使用utf8mb3代替utf8用于填充数据字典表的字符集名称，将影响字符集和相关信息的显示。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>时间格式：MySQL之前对时间格式的分隔符或空白等要求宽松，从此版本开始，推荐用户使用标准格式，使用其他格式将输出警告信息。例如，</span></p> 
<pre><code><span>mysql> <span style="color:#ca7d37">SELECT</span> <span style="color:#ca7d37">DATE</span><span style="color:#dd1144">"2020/02/20"</span>;</span></code><code><span>+<em>------------------+</em></span></code><code><span>| DATE"2020/02/20" |</span></code><code><span>+<em>------------------+</em></span></code><code><span>| 2020-02-20|</span></code><code><span>+<em>------------------+</em></span></code><code><span>1 row in <span style="color:#ca7d37">set</span>, <span style="color:#0e9ce5">1</span> <span style="color:#ca7d37">warning</span> (<span style="color:#0e9ce5">0.00</span> sec)</span></code>
<code><span>mysql> <span style="color:#ca7d37">SHOW</span> <span style="color:#ca7d37">WARNINGS</span>\G</span></code><code><span>*************************** <span style="color:#0e9ce5">1.</span> <span style="color:#ca7d37">row</span> ***************************</span></code><code><span>  <span style="color:#ca7d37">Level</span>: <span style="color:#ca7d37">Warning</span></span></code><code><span>   Code: <span style="color:#0e9ce5">4095</span></span></code><code><span>Message: Delimiter <span style="color:#dd1144">'/'</span> <span style="color:#ca7d37">in</span> <span style="color:#ca7d37">position</span> <span style="color:#0e9ce5">4</span> <span style="color:#ca7d37">in</span> datetime <span style="color:#ca7d37">value</span> <span style="color:#dd1144">'2020/02/20'</span> <span style="color:#ca7d37">at</span></span></code><code><span> <span style="color:#ca7d37">row</span> <span style="color:#0e9ce5">1</span> <span style="color:#ca7d37">is</span></span></code><code><span>deprecated. Prefer the standard <span style="color:#dd1144">'-'</span>.</span></code><code><span><span style="color:#0e9ce5">1</span> <span style="color:#ca7d37">row</span> <span style="color:#ca7d37">in</span> <span style="color:#ca7d37">set</span> (<span style="color:#0e9ce5">0.00</span> sec)</span></code>
</pre> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>复制相关：系统变量“</span>replica_parallel_type”降级，该变量将不再使用，MySQL默认开启并行复制。引入新变量“binlog_expire_logs_auto_purge”用于控制日志清理。“group_replication_set_as_primary ”函数，可以指定新的主要成员，用于覆盖自动选举过程产生的主要成员。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">InnoDB：支持使用ALGORITHM=INSTANT，执行<span>ALTER TABLE ... DROP COLUMN语句，在线删除列。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">克隆：增加系统变量“clone_delay_after_data_drop”，允许在接收者删除数据之后增加延时，以使接收者在开始克隆之前释放足够的空间。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">更多详细内容</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.oracle.com%2Fmysql%2Fpost%2Fannouncing-april-2022-releases-featuring-mysql-8029" target="_blank">可访问官网</a><span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">稿源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F43XvlwMXZqv3loUYCOzJpw" target="_blank">https://mp.weixin.qq.com/s/43XvlwMXZqv3loUYCOzJpw</a></p>
                                        </div>
                                      
</div>
            