
---
title: 'Symfony 5.2.7 发布，经典 PHP Web 开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7717'
author: 开源中国
comments: false
date: Tue, 04 May 2021 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7717'
---

<div>   
<div class="content">
                                                                                            <p>Symfony 是一款基于 MVC 架构的 PHP 框架，致力于减少重复代码的编写，以加速 Web 应用的开发和维护。Symfony 与许多关系型数据库集成的也非常好，成本也较小。</p> 
<p>此外，Symfony 致力于在企业背景下创建健壮的应用，同时也给予了开发者强大的配置功能：从文件结构到外部目录，几乎所有的东西都可以自定义。Symfony 也捆绑了一些诸如测试、调试、文档生成等额外的工具来满足企业的开发过程。</p> 
<p>Symfony 5.2.7 更新内容如下：</p> 
<ul> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F41008" target="_blank">#41008</a> [Security] 不要尝试重写空密码</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40993" target="_blank">#40993</a> [Security] [Security/Core] 修正对 bcrypt 的检查</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40923" target="_blank">#40923</a> [Yaml] 在内联符号结构中检测到暴露的引用</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40964" target="_blank">#40964</a> [HttpFoundation] 修复 PHP 8.1 的弃用</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40919" target="_blank">#40919</a> [Mailer] 在访问 SMTP 的 php.ini 值时使用正确的拼写</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40514" target="_blank">#40514</a> [Yaml] 允许标签作为标记之间的分隔符</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40882" target="_blank">#40882</a> [Cache] phpredis: 为 RedisCluster 添加了完整的 TLS 支持</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40872" target="_blank">#40872</a> [DependencyInjection] [AliasDeprecatedPublicServicesPass] 服务为私有时不执行操作</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40802" target="_blank">#40802</a> [FrameworkBundle] 在 debug:router 中修复阵列控制器的链接</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40793" target="_blank">#40793</a> [DoctrineBridge] 增加对驱动类型为"属性"的支持</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40807" target="_blank">#40807</a> 修复了当 _controller 是一个闭包时的 RequestMatcher 问题</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40811" target="_blank">#40811</a> [PropertyInfo] 对定义在 traits 中的 methods 使用正确的上下文</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40791" target="_blank">#40791</a> [WebProfilerBundle] 在 twig render() 中使用 ControllerReference 而不是 URL</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40330" target="_blank">#40330</a> [SecurityBundle] "access_control"下以破折号开始的空行导致所有规则被跳过</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40780" target="_blank">#40780</a> [Cache] 将 NullAdapter 应用为 Null 对象</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40740" target="_blank">#40740</a> [Cache][FrameworkBundle] 修复 TagAwareAdapter 的日志记录</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Freleases%2Ftag%2Fv5.2.7" target="_blank">https://github.com/symfony/symfony/releases/tag/v5.2.7</a></p>
                                        </div>
                                      
</div>
            