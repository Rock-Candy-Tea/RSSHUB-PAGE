
---
title: 'code-gen v1.5.6 已经发布，代码生成工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5618'
author: 开源中国
comments: false
date: Fri, 21 Jan 2022 14:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5618'
---

<div>   
<div class="content">
                                                                                            <p>code-gen v1.5.6 已经发布，代码生成工具</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>【新增】常用变量</li> 
</ul> 
<div> 
 <pre><code>$&#123;context.randomInt&#125;：int随机数
$&#123;context.randomLong&#125;：long随机数
$&#123;context.randomBoolean&#125;：boolean随机
$&#123;context.uuid&#125;：生成uuid
$&#123;context.nextId&#125;：生成唯一id，基于雪花算法
</code></pre> 
 <div>
   
 </div> 
</div> 
<ul> 
 <li>【新增】新增velocity变量， <code>$&#123;column.isNullable&#125;</code>：字段是否可空,返回boolean <a href="https://gitee.com/durcframework/code-gen/issues/I4QAMO" target="_blank">#I4QAMO</a></li> 
 <li>【新增】新增velocity变量， <code>$&#123;column.columnNameLF&#125;</code>：表中字段名首字母小写 <a href="https://gitee.com/durcframework/code-gen/issues/I4QJJY" target="_blank">#I4QJJY</a></li> 
 <li>【优化】多个模板组切换问题 <a href="https://gitee.com/durcframework/code-gen/issues/I4QFDO" target="_blank">#I4QFDO</a></li> 
 <li>【修复】修复升级1.4.0表名重复问题 <a href="https://gitee.com/durcframework/code-gen/issues/I4LQJW" target="_blank">#I4LQJW</a></li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/durcframework/code-gen/releases/v1.5.6">https://gitee.com/durcframework/code-gen/releases/v1.5.6</a></p>
                                        </div>
                                      
</div>
            