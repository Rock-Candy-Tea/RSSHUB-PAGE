
---
title: 'CakePHP 4.4.3 发布，PHP 快速开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7322'
author: 开源中国
comments: false
date: Thu, 28 Jul 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7322'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px"><span style="color:#333333">CakePHP 是一个运用了诸如 ActiveRecord、Association Data Mapping、Front Controller 和 MVC（model–view–controller） 等著名设计模式的开源 Web 框架。CakePHP 用 PHP 编写，以 Ruby on Rails 的概念为模型，并在 MIT 许可下进行分发。</span></p> 
<p>CakePHP 4.4.3 已发布，这是 4.4 分支的维护版本，修复了几个社区报告的问题</p> 
<ul> 
 <li>修复了文件断言方法中对 null 的潜在方法调用。</li> 
 <li>改进了与 PHP 8.2 的兼容性。</li> 
 <li>如果表配置了选项然后被模拟，TableLocator::get() 不再抛出错误。</li> 
 <li>更新了 CI 配置以使用 Windows 2022 映像。</li> 
 <li>修复了未正确设置 umask 的 Folder::create() 中的回归。</li> 
 <li>与 FileEngine 一起使用的缓存键现在是 URL 编码的。 这会将缓存键中的有效字符与其他引擎对齐。 对于以前使用字母数字范围之外的字符的应用程序，它可能会导致缓存未命中。</li> 
 <li>删除了多余的类类型检查。</li> 
 <li>修复了 ResultSet 索引在启用 xdebug 时因循环内抛出的异常而发生变异。</li> 
 <li>TableLocator 现在可以更好地处理通过命名空间类名获取表。</li> 
 <li>不推荐使用 Database\Query 中未使用的属性。</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcakephp%2Fcakephp%2Freleases%2Ftag%2F4.4.3" target="_blank">https://github.com/cakephp/cakephp/releases/tag/4.4.3</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            