
---
title: 'Symfony 5.2.9 发布，经典 PHP Web 开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5843'
author: 开源中国
comments: false
date: Mon, 24 May 2021 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5843'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Symfony 是一款基于 MVC 架构的 PHP 框架，致力于减少重复代码的编写，以加速 Web 应用的开发和维护。Symfony 与许多关系型数据库集成的也非常好，成本也较小。</p> 
<p>此外，Symfony 致力于在企业背景下创建健壮的应用，同时也给予了开发者强大的配置功能：从文件结构到外部目录，几乎所有的东西都可以自定义。Symfony 也捆绑了一些诸如测试、调试、文档生成等额外的工具来满足企业的开发过程。</p> 
<p>Symfony 5.2.9 更新内容如下：</p> 
<ul> 
 <li>[Security\Core] 通过 response body 修复无效凭证上的用户枚举；</li> 
 <li>bug 修复未定义的方法调用；</li> 
 <li>[SecurityBundle] 删除无效的未使用服务；</li> 
 <li>[Security] [DataCollector] 移除数据收集器中允许的匿名信息；</li> 
 <li>[FrameworkBundle][Validator] 修复了 Doctrine Annotations+Cache 弃用的问题；</li> 
 <li>[Mailer] 修复 SES API 调用 UTF-8 地址的问题；</li> 
 <li>bug 修正了关于传递 null 作为参数的弃用警告</li> 
 <li>[Finder] 修复带有 "**" 的 gitignore regex build ；</li> 
 <li>[HttpClient] 修复了将查询字符串添加到具有作用域客户端的相对 URL 问题；</li> 
 <li>[DependencyInjection][ProxyManagerBridge] 不要在 null 调用 class_exists() ；</li> 
 <li>[Notifier] 为 Slack 通知器的内容类型添加缺失的字符集；</li> 
 <li>[Console] 修复 Windows 代码页支持；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Freleases" target="_blank">https://github.com/symfony/symfony/releases</a></p>
                                        </div>
                                      
</div>
            