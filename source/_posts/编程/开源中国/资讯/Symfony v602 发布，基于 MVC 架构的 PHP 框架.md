
---
title: 'Symfony v6.0.2 发布，基于 MVC 架构的 PHP 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1553'
author: 开源中国
comments: false
date: Fri, 31 Dec 2021 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1553'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Symfony 是一款基于 MVC 架构的 PHP 框架，致力于减少重复代码的编写，以加速 Web 应用的开发和维护。Symfony 与许多关系型数据库集成非常好，使用成本较小。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此外，Symfony 也给予了开发者强大的配置功能：从文件结构到外部目录，几乎所有的东西都可以自定义。同时Symfony 也捆绑了一些诸如测试、调试、文档生成等额外的工具来满足企业的开发过程。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前 Symfony v6.0.2 发布了，此版本带来以下更新：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44828" target="_blank">#44828</a><span> </span>[Lock]<span> </span><span style="color:#24292f">失败时释放 DoctrineDbalPostgreSqlStore 连接锁</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44838" target="_blank">#44838</a><span> </span>[DependencyInjection][HttpKernel]<span> </span><span style="color:#24292f">修复枚举类型绑定</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44723" target="_blank">#44723</a><span> </span>[Lock]<span> </span><span style="color:#24292f">失败时释放 PostgreSqlStore 连接锁</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44826" target="_blank">#44826</a><span> </span>[HttpKernel]<span> </span><span style="color:#2e3033">不要尝试在控制器服务定位器中注册枚举参数</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44822" target="_blank">#44822</a><span> </span>[Mime][Security]<span> </span><span style="color:#2e3033">修复缺失的 sprintf 并添加测试</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44824" target="_blank">#44824</a><span> </span>[Mime] 修复 DkimSigner 中缺少的 sprintf</li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44816" target="_blank">#44816</a><span> </span>[Translation] [LocoProvider]<span> </span><span style="color:#24292f">使用 rawurlencode 和单独的标签设置</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44805" target="_blank">#44805</a><span> </span>[Security]<span> </span><span style="color:#24292f">修复了从 v4 反序列化会话有效负载</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44820" target="_blank">#44820</a><span> </span>[Cache]<span> </span><span style="color:#24292f">在进行嵌套计算时不要锁定</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44807" target="_blank">#44807</a><span> </span>[Messenger]<span> </span><span style="color:#24292f">修复了 32b arch 上的 Redis 支持</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44759" target="_blank">#44759</a><span> </span>[HttpFoundation]<span> </span><span style="color:#24292f">修复 HTTP_PHP_AUTH_USER 未通过时的通知</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44809" target="_blank">#44809</a><span> </span>[WebProfilerBundle]<span> </span><span style="color:#24292f">放宽内存数据收集器的返回类型</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44799" target="_blank">#44799</a><span> </span>[Cache]<span> </span><span style="color:#24292f">修复 apcu < 5.1.10 的兼容性</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44764" target="_blank">#44764</a><span> </span>[Form]<span> </span><span style="color:#24292f">展开 FormView 键以包含 int</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44730" target="_blank">#44730</a><span> </span>[Console] <span style="color:#2e3033">修复了使用默认值自动完成参数的问题</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44637" target="_blank">#44637</a><span> </span>[PropertyInfo]<span> </span><span style="color:#24292f">PhpStan 提取器嵌套对象修复</span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44085" target="_blank">#44085</a><span> </span>[Translation]<span> </span><span style="color:#24292f">使用 ICU 翻译修复 TranslationPullCommand </span></li> 
 <li>bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Fpull%2F44578" target="_blank">#44578</a><span> </span>[PropertyInfo]<span> </span><span style="color:#24292f">修复 phpstan 提取器问题</span></li> 
 <li>...</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多修复项请在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Freleases%2Ftag%2Fv6.0.2" target="_blank">更新公告</a>中查看。</p> 
<p> </p>
                                        </div>
                                      
</div>
            