
---
title: 'Symfony 5.2.6 发布，经典 PHP Web 开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3533'
author: 开源中国
comments: false
date: Thu, 01 Apr 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3533'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Symfony 是一款基于 MVC 架构的 PHP 框架，致力于减少重复代码的编写，以加速 Web 应用的开发和维护。Symfony 与许多关系型数据库集成的也非常好，成本也较小。</p> 
<p>此外，Symfony 致力于在企业背景下创建健壮的应用，同时也给予了开发者强大的配置功能：从文件结构到外部目录，几乎所有的东西都可以自定义。Symfony 也捆绑了一些诸如测试、调试、文档生成等额外的工具来满足企业的开发过程。</p> 
<p>Symfony 5.2.6 更新内容如下：</p> 
<ul> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40598" target="_blank">#40598</a> 字符串不能被解析为日期的表单错误；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40510" target="_blank">#40510</a> [Form] IntegerType: 总是使用 en 来表示 IntegerToLocalizedStringTransformer；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40593" target="_blank">#40593</a> 根据选项的长短，为控制台选项使用正确的赋值操作；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40535" target="_blank">#40535</a> [HttpKernel] ConfigDataCollector 不需要 Kernel 就能返回已知数据；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40552" target="_blank">#40552</a> [Translation] 修复更新现有 +int-icu 域的密钥；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40541" target="_blank">#40541</a> 修正了没有消息键的废弃定义的解析；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40537" target="_blank">#40537</a> [Security] 为 remember me cookie security 正确处理'自动'选项；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40524" target="_blank">#40524</a> [Console] 修复表情符号弄乱行宽的问题；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40506" target="_blank">#40506</a> [Validator] 避免触发用户输入值的自动加载器；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40544" target="_blank">#40544</a> [FrameworkBundle] 确保 TestBrowserToken::$firewallName 被序列化；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40538" target="_blank">#40538</a> [HttpClient] 删除对 $htt _respons _header 的使用；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40508" target="_blank">#40508</a> [PhpUnitBridge] 修复了从 DebugClassLoader 回报的弃用问题；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40497" target="_blank">#40497</a> [HttpFoundation] 尽快使用 HTTP 缓存启用 HTTP 方法覆盖；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40348" target="_blank">#40348</a> [Console] 修正块输出中装饰文字的换行；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40499" target="_blank">#40499</a> [Inflector][String] 修正了"coupon"的复数化；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40494" target="_blank">#40494</a> [PhpUnitBridge] 修正与 symfony/debug 的兼容问题；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40453" target="_blank">#40453</a> [VarDumper] 为 VarDumper 添加 ReflectionUnionType 支持；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40460" target="_blank">#40460</a> 正确清除多行进度条消息的行；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40490" target="_blank">#40490</a> [Security] 为身份验证管理器添加 XML 支持；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40242" target="_blank">#40242</a> [ErrorHandler] 修正 include + ope _basedir 引起的错误；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40368" target="_blank">#40368</a> [FrameworkBundle] 让 TestBrowserToken 可以和其他 token 互换；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40450" target="_blank">#40450</a> [Console] ProgressBar 在更新时清除了太多行；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40178" target="_blank">#40178</a> [FrameworkBundle] 执行 About 命令时排除不可读文件；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40472" target="_blank">#40472</a> [BridgeTwig] 为范围输入类型添加"form-control-range"；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40481" target="_blank">#40481</a> 使 async-ses 成为必需；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F39866" target="_blank">#39866</a> [Mime] 地址名中的逗号转义；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40373" target="_blank">#40373</a> 检查模板引擎是否支持给定视图；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F39992" target="_blank">#39992</a> [Security] 在 SwitchUserListener 中刷新原始用户；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40417" target="_blank">#40417</a> [Form] 即使将 clear missing 设置为 false，也要清除未选中的选择单选框；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40388" target="_blank">#40388</a> [ErrorHandler] 为 FlattenException 添加了缺失的类型注解；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F40407" target="_blank">#40407</a> [TwigBridge] 允许 Twig 额外包的第三版；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Freleases%2Ftag%2Fv5.2.6" target="_blank">https://github.com/symfony/symfony/releases/tag/v5.2.6</a></p>
                                        </div>
                                      
</div>
            