
---
title: 'Symfony 5.3.11 发布，经典 PHP Web 开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3011'
author: 开源中国
comments: false
date: Wed, 24 Nov 2021 06:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3011'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Symfony 是一款基于 MVC 架构的 PHP 框架，致力于减少重复代码的编写，以加速 Web 应用的开发和维护。Symfony 与许多关系型数据库集成的也非常好，成本也较小。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此外，Symfony 致力于在企业背景下创建健壮的应用，同时也给予了开发者强大的配置功能：从文件结构到外部目录，几乎所有的东西都可以自定义。Symfony 也捆绑了一些诸如测试、调试、文档生成等额外的工具来满足企业的开发过程。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Symfony 5.3.11 更新内容如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44188" target="_blank">#44188</a><span> </span>[VarExporter]<span> </span><span style="color:#2e3033">修正了实现<span> </span><code>__sleep()</code><span> </span>时会导出已声明但未设置的属性的问题</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44176" target="_blank">#44176</a><span> </span>[Console]<span> </span><span style="color:#2e3033">默认 ansi 选项为空</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44119" target="_blank">#44119</a><span> </span>[HttpClient][Mime]<span> </span><span style="color:#2e3033">添加正确的 IDN 标志，以符合 IDNA2008 标准</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44131" target="_blank">#44131</a><span> </span>[Yaml]<span> </span><span style="color:#24292f">正确解析用 !!str 标记的引用字符串</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42323" target="_blank">#42323</a><span> </span>[TwigBridge]<span> </span><span style="color:#24292f">不合并标签类到扩展选项标签里边</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44110" target="_blank">#44110</a><span> </span>[FrameworkBundle]<span> </span><span style="color:#2e3033">修复了在 PHP 8 中没有安装 doctrine/annotation 时，验证和序列化程序配置中的默认 PHP 属性支持</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44121" target="_blank">#44121</a><span> </span>[Serializer] 修复对惰性属性（lazy properties）的支持</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44108" target="_blank">#44108</a><span> </span>[FrameworkBundle][Messenger] 序列化器不可用时，移除<span> </span><code>FlattenExceptionNormalizer</code><span> </span>定义</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44111" target="_blank">#44111</a><span> </span>[Serializer] 修复对低于 7.4 版本的 PHP 的未设置属性支持</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44070" target="_blank">#44070</a><span> </span>[Process]<span> </span><span style="color:#24292f">与 getenv() 相交以填充默认环境</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43990" target="_blank">#43990</a><span> </span>[Translation] [Loco]<span> </span><span style="color:#2e3033">生成 id 参数，不再让 Loco 完成。 </span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44043" target="_blank">#44043</a><span> </span>[Cache] 修复 dbindex Redis</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44050" target="_blank">#44050</a><span> </span>[Notifier] 修复包名称</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44042" target="_blank">#44042</a><span> </span><span style="color:#24292f">修复 DateIntervalToStringTransformer::transform() 文档</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44034" target="_blank">#44034</a><span> </span>[Yaml] 不要尝试替换引用字符串中的引用</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44028" target="_blank">#44028</a><span> </span>[ErrorHandler] 修复 FlattenException::setPrevious 参数类型</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44012" target="_blank">#44012</a><span> </span>[DependencyInjection]<span> </span><span style="color:#2e3033">修复涉及非共享服务时的内联问题</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44002" target="_blank">#44002</a><span> </span>[Cache]<span> </span><span style="color:#2e3033">解决内存泄漏问题</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43981" target="_blank">#43981</a><span> </span>[FrameworkBundle]<span> </span><span style="color:#2e3033">修正了延迟重置服务的注册问题</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43988" target="_blank">#43988</a><span> </span>[DoctrineBridge]<span> </span><span style="color:#2e3033">添加对 JSON 类型的支持</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43987" target="_blank">#43987</a><span> </span>[PhpUnitBridge] 修复未捕获的值错误</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43961" target="_blank">#43961</a><span> </span>[HttpClient]<span> </span><span style="color:#24292f">Curl http 客户端必须在重置时重新初始化 curl 多句柄</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43948" target="_blank">#43948</a><span> </span>[Asset][Security]<span> </span><span style="color:#2e3033">修正了 PHP 8.1 弃用的遗留问题</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43945" target="_blank">#43945</a><span> </span>[Runtime]<span> </span><span style="color:#2e3033">修复了 Dotenv 未启用时定义 APP_DEBUG 的问题</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43922" target="_blank">#43922</a><span> </span>[DependencyInjection] 只允许<span> </span><code>ReflectionNamedType</code><span> </span>为<span> </span><code>ServiceSubscriberTrait</code><span> </span>的类型</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43814" target="_blank">#43814</a><span> </span>[Intl]<span> </span><span style="color:#24292f">将 ICU 数据更新为 70.1 - 5.3</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43915" target="_blank">#43915</a><span> </span>[Messenger] 修复测试</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43901" target="_blank">#43901</a><span> </span>[SecurityBundle] 默认合并 access_decision_manager.strategy 选项</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43909" target="_blank">#43909</a><span> </span>[VarExporter]<span> </span><span style="color:#2e3033">转义与方向性有关的 unicode 字符</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43900" target="_blank">#43900</a><span> </span>[Security]<span> </span><span style="color:#24292f">修复 ChainUserProvider 中的类型错误（TypeError） 消息</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43884" target="_blank">#43884</a><span> </span>[Console]<span> </span><span style="color:#2e3033">psr/log  3.0 以上版本使用运行时冲突代替<span> </span></span>composer 冲突。</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43867" target="_blank">#43867</a><span> </span>[VarDumper]<span> </span><span style="color:#24292f">使转储 DateInterval 实例与时区无关</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43096" target="_blank">#43096</a><span> </span>[Messenger] 用<span> </span><code>TransportMessageIdStamp</code><span> </span>在<span> </span><code>InMemoryTransport</code><span> </span>允许重试</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42168" target="_blank">#42168</a><span> </span>[RateLimiter]<span> </span><span style="color:#24292f">修复固定窗口策略的等待时间</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43501" target="_blank">#43501</a><span> </span>[HttpKernel] 修复 CacheWarmerAggregate 的  ErrorException</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42361" target="_blank">#42361</a><span> </span>[Translation] 使用 TargetOperation 正确处理国际域名</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43833" target="_blank">#43833</a><span> </span>[Runtime]<span> </span><span style="color:#24292f">在解析 APP_RUNTIME 和 APP_RUNTIME_OPTIONS 时还要考虑 $_ENV</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43834" target="_blank">#43834</a><span> </span>[Inflector] 修复 "zombies" 的偏转器</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F43267" target="_blank">#43267</a><span> </span>[Config]<span> </span><span style="color:#2e3033">修复 PHP 8.1 中使用嵌套属性生成签名的问题</span></li> 
 <li>[PR]<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44194" target="_blank">#44194</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Freleases%2Ftag%2Fv5.3.11" target="_blank">https://github.com/symfony/symfony/releases/tag/v5.3.11</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            