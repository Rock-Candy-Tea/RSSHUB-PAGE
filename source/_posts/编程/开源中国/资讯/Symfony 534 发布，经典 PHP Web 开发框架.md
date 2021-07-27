
---
title: 'Symfony 5.3.4 发布，经典 PHP Web 开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6816'
author: 开源中国
comments: false
date: Tue, 27 Jul 2021 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6816'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Symfony 是一款基于 MVC 架构的 PHP 框架，致力于减少重复代码的编写，以加速 Web 应用的开发和维护。Symfony 与许多关系型数据库集成的也非常好，成本也较小。</p> 
<p>此外，Symfony 致力于在企业背景下创建健壮的应用，同时也给予了开发者强大的配置功能：从文件结构到外部目录，几乎所有的东西都可以自定义。Symfony 也捆绑了一些诸如测试、调试、文档生成等额外的工具来满足企业的开发过程。</p> 
<p>Symfony 5.3.4 更新内容如下：</p> 
<ul> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42243" target="_blank">#42243</a> [Translation] [Lokalise] 修复 <code>base_uri</code></li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42223" target="_blank">#42223</a> [Debug][ErrorHandler] 不要使用php80 polyfill</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42207" target="_blank">#42207</a> [Console] 修复表 setHeaderTitle 没有 headers 的问题</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42130" target="_blank">#42130</a> [Translation] 修正回退到 Locale::getDefault() 的问题</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42184" target="_blank">#42184</a> [Mailer] 确保 Http TransportException 不被泄露</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42150" target="_blank">#42150</a> [Form] 修复 <code>invalid_message</code> 在多个 ChoiceType 中的使用</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42183" target="_blank">#42183</a> [Notifier] 允许将先前的 throwable 传递给异常</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42173" target="_blank">#42173</a> [Messenger] [Redis] 修复被错误认为无效的身份验证选项</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42174" target="_blank">#42174</a> 标明与 psr/log 2 和 3 的兼容性</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42112" target="_blank">#42112</a> [HttpFoundation] 修复 PHP 8.1 下的 FileBag</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42131" target="_blank">#42131</a> [PhpUnitBridge] 修复Windows下的合成器解析</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42097" target="_blank">#42097</a> [DependencyInjection] 支持交叉类型</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42114" target="_blank">#42114</a> [HttpFoundation] 修复 <code>SessionHandler::gc()</code> 的返回类型；</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42074" target="_blank">#42074</a> 修复 ctype_digit 弃用</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42084" target="_blank">#42084</a> [WebProfilerBundle] 修复一些 CSS 属性的值</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42079" target="_blank">#42079</a> [FrameworkBundle] 修复了 Sodium vault seal 中的文件操作</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42078" target="_blank">#42078</a> [DoctrineBridge] [Doctrine Bridge] 修复一个异常信息</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42067" target="_blank">#42067</a> [Messenger] [Redis] Make <code>auth</code> option works (<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FwelcoMattic" target="_blank">@welcoMattic</a></strong>)</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42054" target="_blank">#42054</a> [DoctrineBridge] 修正在 php 8/7 上分别设置默认映射类型为属性/注释的问题</li> 
 <li>bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F42049" target="_blank">#42049</a> [TwigBridge] 不要两次渲染相同的标签 id 属性</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Freleases%2Ftag%2Fv5.3.4" target="_blank">https://github.com/symfony/symfony/releases/tag/v5.3.4</a></p>
                                        </div>
                                      
</div>
            