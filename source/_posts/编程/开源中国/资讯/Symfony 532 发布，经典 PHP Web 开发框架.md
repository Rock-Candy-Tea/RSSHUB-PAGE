
---
title: 'Symfony 5.3.2 发布，经典 PHP Web 开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8612'
author: 开源中国
comments: false
date: Sat, 19 Jun 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8612'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Symfony 是一款基于 MVC 架构的 PHP 框架，致力于减少重复代码的编写，以加速 Web 应用的开发和维护。Symfony 与许多关系型数据库集成的也非常好，成本也较小。</p> 
<p>此外，Symfony 致力于在企业背景下创建健壮的应用，同时也给予了开发者强大的配置功能：从文件结构到外部目录，几乎所有的东西都可以自定义。Symfony 也捆绑了一些诸如测试、调试、文档生成等额外的工具来满足企业的开发过程。</p> 
<p>Symfony 5.3.2 更新内容如下：</p> 
<ul> 
 <li>[SecurityHttp] 修复 "多个防火墙的认证授权"；</li> 
 <li>[Uid] 修复性能问题并防止与真正的 clock_seq 发生冲突；</li> 
 <li>[Security] 修复 TokenInterface::getUser() 字符串返回上的弃用通知；</li> 
 <li>[Security] 恢复 MessageDigestPasswordEncoder 的扩展点；</li> 
 <li>[Messenger] 修复 RequestContext 未更新的问题；</li> 
 <li>[Messenger] 移除不使用 TLS 时的 TLS 相关选项；</li> 
 <li>[FrameworkBundle] 修复找不到 "test.service_container" 服务的问题；</li> 
 <li>[Console] 修正使用不含 DI 的 #[AsCommand] 的问题；</li> 
 <li>[DependencyInjection] 修复对属性的解析类；</li> 
 <li>[Runtime] 修复使用单命令应用程序重写 --env|-e 的问题；</li> 
 <li>[HttpClient] 修正与 cURL <= 7.37 的兼容问题；</li> 
 <li>[Console] 修复在命令被延迟加载时的信号管理；</li> 
 <li>[PasswordHasher] 修复丢失的 PasswordHasherAwareInterface 允许类型；</li> 
 <li>[HttpClient] 当 AsyncDecoratorTrait 得到一个已经消耗的响应时抛出异常；</li> 
 <li>[Notifier] 为 Telegram 的传输提供转译 <code>.</code> 字符；</li> 
 <li>[Config] 修复 ReflectionClassResource 中的跟踪属性；</li> 
 <li>[Process] 修复不正确的参数类型；</li> 
 <li>[HttpClient] 恢复绑定到未受影响的 PHP 版本的解决方法；</li> 
 <li>[DependencyInjection] 修复导入文件内 <code>when@&#123;env&#125;</code> 的问题；</li> 
 <li>[Messenger] 使用不存在的别名修复 FrameworkBundle 4.4 的 BC；</li> 
 <li>修复非空获取集合键类型；</li> 
 <li>[PasswordHasher] 防止使用自动算法时出现 PHP 严重错误；</li> 
 <li>[Security] 修复 opcache 预加载的别名类；</li> 
 <li>[Serializer] 不允许将只带有空格的字符串去正规化，使之成为有效的 DateTime 对象</li> 
 <li>[Console] 修复无法访问的否定选项；</li> 
 <li>[Validator] 如果服务的类不存在，则删除该服务；</li> 
 <li>[DependencyInjection] 当调用 ContainerConfigurator::withPath 时更新加载器的目录；</li> 
 <li>[FrameworkBundle] 使用无状态防火墙修正 KernelBrowser::loginUser；</li> 
 <li>[SecurityBundle] 将 UserProviderListener 链接到正确的防火墙调度程序；</li> 
 <li>[Console] 转义概要输出；</li> 
 <li>[Notifier] [Bridge] 删除 SmsBiurasTransport 对 HttpFoundation 的隐藏依赖；</li> 
 <li>放宽对 symfony/runtime 的要求；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Freleases%2Ftag%2Fv5.3.2" target="_blank">https://github.com/symfony/symfony/releases/tag/v5.3.2</a></p>
                                        </div>
                                      
</div>
            