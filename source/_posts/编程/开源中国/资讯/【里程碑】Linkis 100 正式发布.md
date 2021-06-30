
---
title: '【里程碑】Linkis 1.0.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8523'
author: 开源中国
comments: false
date: Wed, 30 Jun 2021 10:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8523'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>Linkis 1.0.0是 Linkis 践行“计算治理”的里程碑，提供了计算编排、一次性作业、Web前端和Linkis-Cli的全新shell命令提交代码方式，标志着 Linkis 正式进入1.0版本时代。</p> 
</blockquote> 
<p>Linkis 1.0.0 作为正式版，主要提供了Linkis-Orchetrator计算编排、优化了大量“计算治理”的架构代码、增加了对OnceEngineConn一次性作业的支持，用于OLAP作业和Streaming作业、同时还简化了Linkis的安装部署。</p> 
<p>通过 Orchestrator计算编排 和强大的标签管理能力，Linkis 1.0.0已经为跨集群/跨IDC 的细粒度路由、负载均衡、多租户、流量控制、资源管控和编排策略，例如 双活、混合计算等提供了扩展性足够强的架构基石，接下来只需要编写转换规则即可实现各个计算编排的能力。</p> 
<hr> 
<h2>新特性</h2> 
<h4>Orchestrator</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F746" target="_blank">Linkis-746</a> 新增Linkis Orchestrator核心模块，为Orchestrator模块提供顶层架构和扩展接口。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F739" target="_blank">Linkis-739</a> 新增Linkis交互式场景的Orchestrator模块。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F733" target="_blank">Linkis-733</a> 新增linkis-code-orchestrator模块，用于支持脚本编排场景。</li> 
</ul> 
<h4>EngineConn</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F799" target="_blank">Linkis-799</a> 新增linkis-once-engineconn模块，用于支持一次性作业，如OLAP Job和Streaming Job。</li> 
</ul> 
<h4>Web</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F757" target="_blank">Linkis-757</a> 新增Linkis前端web模块，提供全局历史、资源管理、参数配置、全局变量等模块。</li> 
</ul> 
<h4>Client</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F754" target="_blank">Linkis-754</a> 新增Linkis-Cli模块，提供shell命令提交代码的新方式。</li> 
</ul> 
<hr> 
<h2>增强</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F818" target="_blank">Linkis-818</a> 将Eureka中EngineConn修改为 Linkis-CG-EngineConn，以遵循命名规范。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F807" target="_blank">Linkis-807</a> 增强Linkis1.0.0通用模块，为其他模块提供大量工具类。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F805" target="_blank">Linkis-805</a> 使用Utils.tryCatch 捕获异常，而不是try...catch 直接catch异常。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F797" target="_blank">Linkis-797</a> 为所有日志添加中英文支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F789" target="_blank">Linkis-789</a> 一部分常量替换优化。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F788" target="_blank">Linkis-788</a> 优化 DESUtil 类中的一些魔法值。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F782" target="_blank">Linkis-782</a> 优化Linkis代码中的一些魔法值。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F781" target="_blank">Linkis-781</a> 优化错误码的定义。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F777" target="_blank">Linkis-777</a> 将publicservice与其他publicenhancement微服务合并，并增加了组合打包方式。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F775" target="_blank">Linkis-775</a> 优化Linkis计算治理模块，适配Linkis1.0新架构。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F768" target="_blank">Linkis-768</a> 删除所有注释代码并优化 HttpBmlClient 。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F767" target="_blank">Linkis-767</a> 优化类的规范性，去掉类顶部的所有@author和@Date。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F752" target="_blank">Linkis-752</a> 优化Linkis engineconn模块，适配Linkis1.0新架构。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F751" target="_blank">Linkis-751</a> 优化Linkis micro-service模块，适配Linkis1.0新架构。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F749" target="_blank">Linkis-749</a> 添加一个新的linkis-io-file-client 模块，修改一些注释并添加License。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F748" target="_blank">Linkis-748</a> 优化public-enhancements模块，适配Linkis1.0新架构。</li> 
</ul> 
<hr> 
<h2>Bugs修复</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F825" target="_blank">Linkis-825</a> 解决SparkPythonExecutor的close方法中递归调用问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fissues%2F816" target="_blank">Linkis-816</a> 修复多executor 的EngineConn场景下，仅关闭默认的executor而不是关闭所有executor的缺陷。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fissues%2F815" target="_blank">Linkis-815</a> 修复 Orchestrator AsyncExec ResultSet等待器不会收到通知的缺陷并删除 Orchestrator 限制5000条结果集的约束。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F804" target="_blank">Linkis-804</a> 修复用户提交sql如'select*'时不会自动添加'limit 5000'的bug，可能会导致全表搜索，导致结果集很大。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F803" target="_blank">Linkis-803</a> 修复SSOUtils线程安全问题，可能导致OOM异常。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F787" target="_blank">Linkis-787</a> 修复hive版本升级导致的包冲突问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F780" target="_blank">Linkis-780</a> 修复Yarn capacity scheduler中RM模块的值转换问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis%2Fpull%2F729" target="_blank">Linkis-729</a> 解决登录后cookies不生效，添加到Action的cookies没有被HttpClient传递到网关的问题.</li> 
</ul> 
<hr> 
<h2>贡献者</h2> 
<p>Linkis 1.0.0 的发布离不开 WeDataSphere 社区的贡献者。在此感谢各位社区的贡献者!</p> 
<hr> 
<h2>云资源</h2> 
<ol> 
 <li><strong>腾讯云</strong>:</li> 
</ol> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fosp-1257653870.cos.ap-guangzhou.myqcloud.com%2FWeDatasphere%2FLinkis%2F1.0.0%2Fwedatasphere-linkis-1.0.0-combined-package-dist.tar.gz" target="_blank">https://osp-1257653870.cos.ap-guangzhou.myqcloud.com/WeDatasphere/Linkis/1.0.0/wedatasphere-linkis-1.0.0-combined-package-dist.tar.gz</a></p>
                                        </div>
                                      
</div>
            