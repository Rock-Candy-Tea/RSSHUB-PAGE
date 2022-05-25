
---
title: 'DBPack v0.1.0 发布公告'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1671'
author: 开源中国
comments: false
date: Wed, 25 May 2022 09:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1671'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><strong style="color:#2c3e50">经过一个多月的努力，DBPack 发布了今年第一个版本，该版本 Release 了分布式事务解决方案，并提供读写分离功能的预览。DBPack 支持任何微服务编程语言，我们已经准备了<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack-samples%2Fblob%2Fmain%2Fgo%2FREADME.md" target="_blank">go</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack-samples%2Fblob%2Fmain%2Fjava%2FREADME.md" target="_blank">java</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack-samples%2Fblob%2Fmain%2Fphp%2FREADME.md" target="_blank">php</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack-samples%2Fblob%2Fmain%2Fpython%2FREADME.md" target="_blank">python</a><span> </span>的示例。</strong></p> 
<h3 style="margin-left:.6rem; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcectc.github.io%2Fdbpack-doc%2F%23%2Fblogs%2Frelease-v0.1.0%3Fid%3D%25e4%25b8%258b%25e9%259d%25a2%25e6%2598%25af%25e6%2588%2591%25e4%25bb%25ac%25e4%25bf%25ae%25e5%25a4%258d%25e7%259a%2584-bug%25ef%25bc%259a" target="_blank"><span style="color:#34495e">下面是我们修复的 Bug：</span></a></h3> 
<ul> 
 <li>增加延迟退出配置 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fissues%2F4" target="_blank">#4</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2F5c607d48d1149218cff3988dcb00d83da571a561" target="_blank">6604ce8</a>)</li> 
 <li>使用<span> </span><code>db</code><span> </span>代理<span> </span><code>tx</code><span> </span>执行 sql (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fpull%2F8" target="_blank">#8</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2F52d78cab0bc414d92a5c59230f2827c8332c2bde" target="_blank">7e2b42d</a>)</li> 
 <li>当收到 ComQuit 请求，应该归还连接 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fpull%2F51" target="_blank">#51</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2Fe8f07086ccf76a7112f00512e3ed3f6e94aff410" target="_blank">627adc2</a>)</li> 
 <li>从连接上读取 sql 执行结果完毕应该关闭<span> </span><code>statement</code><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fpull%2F71" target="_blank">#71</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2F4c9a29271d73df0ff8daf92c3faebf1540b0cf01" target="_blank">f924e10</a>)</li> 
 <li><code>ping</code><span> </span>数据库后应该归还连接 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fpull%2F74" target="_blank">#74</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2Fc1c77710398ad58d7d3809ad66312550b0931236" target="_blank">07de56e</a>)</li> 
 <li>处理超时的全局事务应该刷新全局事务的状态 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fpull%2F86" target="_blank">#86</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2F6bf4090fbe897c60c229ac172fdb0c14720066ee" target="_blank">3046e17</a>)</li> 
 <li>当<span> </span><code>undologs</code><span> </span>不存在的时候应该释放<span> </span><code>tx</code><span> </span>对象 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fpull%2F93" target="_blank">#93</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2F99df0361ca1cf7876daa66151cf6bb462d0fd3bb" target="_blank">7aeaa4e</a>)</li> 
</ul> 
<h3 style="margin-left:.6rem; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcectc.github.io%2Fdbpack-doc%2F%23%2Fblogs%2Frelease-v0.1.0%3Fid%3D%25e4%25b8%258b%25e9%259d%25a2%25e6%2598%25af%25e4%25b8%2580%25e4%25ba%259b%25e9%2587%258d%25e5%25a4%25a7%25e7%259a%2584%25e7%2589%25b9%25e6%2580%25a7%25ef%25bc%259a" target="_blank"><span style="color:#34495e">下面是一些重大的特性：</span></a></h3> 
<ul> 
 <li>etcd watch 机制驱动的分布式事务 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fpull%2F11" target="_blank">#11</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2Fe9910501e32d23741f99f5fe9ece1077ba1b348c" target="_blank">ce10990</a>)</li> 
 <li>支持 TCC 模式事务分支提交回滚 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fissues%2F12" target="_blank">#12</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2Ffeab7aefe819bf3217363994c67515b887f8adb9" target="_blank">c0bfdf9</a>)</li> 
 <li>支持<span> </span><code>GlobalLock</code><span> </span>Hint (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fissues%2F14" target="_blank">#14</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2F5c7c96797539943ed75495d1cfa92f6094ff548e" target="_blank">8369f8f</a>)</li> 
 <li>支持 Leader 选举，只有 Leader 可以处理事务的提交回滚 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fpull%2F19" target="_blank">#19</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2Fd7ab60b6ed5547f1bc9a6c426e1fb9ee21d6f4f3" target="_blank">b89c672</a>)</li> 
 <li>增加 Prometheus 指标 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fissues%2F25" target="_blank">#25</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2F627adc2ced9da499e6b658f718b23417e7df9903" target="_blank">627adc2</a>)</li> 
 <li>增加<span> </span><code>readiness</code><span> </span>和<span> </span><code>liveness</code><span> </span>探针 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fissues%2F52" target="_blank">#52</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2Ff43ab5f4ed6eafaf950a73e241c536849a16e4f9" target="_blank">fd889cc</a>)</li> 
</ul> 
<h3 style="margin-left:.6rem; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcectc.github.io%2Fdbpack-doc%2F%23%2Fblogs%2Frelease-v0.1.0%3Fid%3D%25e4%25b8%2580%25e4%25ba%259b%25e4%25bf%25ae%25e6%2594%25b9%25ef%25bc%259a" target="_blank"><span style="color:#34495e">一些修改：</span></a></h3> 
<ul> 
 <li>优化分支事务处理逻辑 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fpull%2F17" target="_blank">#17</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack%2Fcommit%2F06d624511c65a379e73dae91c2be4fb3785b9bf0" target="_blank">c6a6626</a>)</li> 
</ul> 
<h3 style="margin-left:.6rem; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcectc.github.io%2Fdbpack-doc%2F%23%2Fblogs%2Frelease-v0.1.0%3Fid%3D%25e4%25b8%258b%25e9%259d%25a2%25e6%2598%25af%25e4%25b8%25ba%25e6%259c%25ac%25e6%25ac%25a1%25e7%2589%2588%25e6%259c%25ac%25e5%258f%2591%25e5%25b8%2583%25e5%2581%259a%25e5%2587%25ba%25e8%25b4%25a1%25e7%258c%25ae%25e7%259a%2584%25e8%25b4%25a1%25e7%258c%25ae%25e8%2580%2585%25e5%2590%258d%25e5%258d%2595%25ef%25bc%258c%25e9%259d%259e%25e5%25b8%25b8%25e6%2584%259f%25e8%25b0%25a2%25e5%25a4%25a7%25e5%25ae%25b6%25e7%259a%2584%25e4%25bb%2598%25e5%2587%25ba%25ef%25bc%259a" target="_blank"><span style="color:#34495e">下面是为本次版本发布做出贡献的贡献者名单，非常感谢大家的付出：</span></a></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frocymp" target="_blank">@rocymp</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorexlv" target="_blank">@gorexlv</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzackzhangkai" target="_blank">@zackzhangkai</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyx9o" target="_blank">@yx9o</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbohehe" target="_blank">@bohehe</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffatelei" target="_blank">@fatelei</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhu733756" target="_blank">@zhu733756</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwybrobin" target="_blank">@wybrobin</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftanryberdi" target="_blank">@tanryberdi</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuwanXu" target="_blank">@JuwanXu</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhzliangbin" target="_blank">@hzliangbin</a></li> 
</ul>
                                        </div>
                                      
</div>
            