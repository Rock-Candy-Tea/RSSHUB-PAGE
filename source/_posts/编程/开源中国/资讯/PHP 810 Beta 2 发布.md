
---
title: 'PHP 8.1.0 Beta 2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9817bf8b88c84d95c59b09579bbb850a056.png'
author: 开源中国
comments: false
date: Fri, 13 Aug 2021 07:08:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9817bf8b88c84d95c59b09579bbb850a056.png'
---

<div>   
<div class="content">
                                                                                            <p>PHP 8.1.0 Beta 2 已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.php.net%2Farchive%2F2021.php%232021-08-05-2" target="_blank">发布</a>。下一个版本将是 Beta 3，计划于 2021 年 8 月 19 日发布。8.1 将是继 8 之后的又一个重要版本更新，正式 GA 的时间暂定于今年 11 月月底。PHP 8.1 具体的发布周期如下：</p> 
<p><img height="295" src="https://oscimg.oschina.net/oscnet/up-9817bf8b88c84d95c59b09579bbb850a056.png" width="500" referrerpolicy="no-referrer"></p> 
<p>需要注意的是，Beta 阶段的版本不适合用于生产中。此版本主要更新内容如下：</p> 
<p><strong>Core</strong></p> 
<ul> 
 <li>修复了 bug #81303：匹配错误信息的改进</li> 
</ul> 
<p><strong>Mbstring</strong></p> 
<ul> 
 <li>修复了 bug #81298：当指定 7bit 编码时，mb_detect_encoding() 出现故障</li> 
</ul> 
<p><strong>MySQLnd</strong></p> 
<ul> 
 <li>修复了 bug #63327：在 mysqlnd 中由于错误的对齐方式而崩溃（总线错误）</li> 
</ul> 
<p><strong>Opcache</strong></p> 
<ul> 
 <li>修复了 bug #81255：使用功能性 JIT 的 PHPUnit 的内存泄漏问题</li> 
 <li>修复了 bug #80959：在 JIT 编译过程中构建 cfg 的无限循环</li> 
</ul> 
<p><strong>Reflection</strong></p> 
<ul> 
 <li>修复了 bug #80821：ReflectionProperty::getDefaultValue() 返回静态的当前值</li> 
 <li>修复了 bug #80564：ReflectionProperty::__toString() 呈现当前值，而不是默认值</li> 
</ul> 
<p><strong>SimpleXML</strong></p> 
<ul> 
 <li>修复了 bug #81325：zif_simplexml_import_dom 中的 Segfault</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphp%2Fphp-src%2Fblob%2Fphp-8.1.0beta2%2FNEWS" target="_blank">https://github.com/php/php-src/blob/php-8.1.0beta2/NEWS</a></p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.php.net%2F%7Eramsey%2F" target="_blank">https://downloads.php.net/~ramsey/</a></p>
                                        </div>
                                      
</div>
            