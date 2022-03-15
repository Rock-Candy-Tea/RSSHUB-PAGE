
---
title: 'Apache Maven 3.8.5 发布，项目管理和构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2294'
author: 开源中国
comments: false
date: Tue, 15 Mar 2022 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2294'
---

<div>   
<div class="content">
                                                                                            <p>Apache Maven 3.8.5 发布了。Apache Maven 是一个项目管理和构建工具。基于项目对象模型（POM）的概念， Maven 可以从中心位置管理项目的构建、报告和文档。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Bug</strong></p> 
<ul> 
 <li>[MNG-5180] - 版本控制的快照版本列表不包括在元数据合并中</li> 
 <li>[MNG-5561] - 插件重新定位会丢失配置</li> 
 <li>[MNG-5982] - ... 的 POM 是无效的，<span style="background-color:#ffffff; color:#222222">传递依赖</span>... 而属性被覆盖</li> 
 <li>[MNG-6326] - 在没有找到核心扩展时继续构建</li> 
 <li>[MNG-6727] - 在父版本和 CI 友好版本中使用版本范围失败</li> 
 <li>[MNG-6802] - FileProfileActivator 改变了 FileProfileActivator.existence，让扁平化的 resolveCiFriendliesOnly 取决于激活配置文件的失败</li> 
 <li>[MNG-7156] - 并行构建可能导致 clean 和 forked 目标之间的问题。</li> 
 <li>[MNG-7335] - [回归] 由于编译路径中缺少 JAR 构件，并行构建失败。</li> 
 <li>[MNG-7347] - SessionScoped beans 应该是给定会话的单例。</li> 
 <li>[MNG-7357] - 所有 Maven Core JARs 都有不寻常的进入顺序</li> 
 <li>[MNG-7362] - DefaultArtifactResolver 有虚假的"Failure detected"的 INFO 日志</li> 
 <li>[MNG-7374] - Mutating RelocatedArtifact 不保留类型</li> 
 <li>[MNG-7386] - ModelMerger$MergingList不可序列化</li> 
 <li>[MNG-7402] - BuildListCalculator 从未分离出 classloader</li> 
 <li>[MNG-7417] - 有几个类没有正确设置属性以满足构建请求</li> 
</ul> 
<p><strong>New Feature</strong></p> 
<ul> 
 <li>[MNG-7395] - 支持 extensions.xml 中的插值</li> 
 <li>[MNG- 7407] - 引入 ModelVersionProcessor 组件以使 CI Friendly Versions pluggable</li> 
</ul> 
<p><strong><span style="background-color:#ffffff; color:#222233">Improvement</span></strong></p> 
<ul> 
 <li>[MNG-6960] - 使用 RuntimeInformation 而不是 reading properties</li> 
 <li>[MNG-7349] - 将重定位警告信息限制在直接的依赖项</li> 
 <li>[MNG-7380] - 如果只构建单个模块，则不要记录非线程安全警告</li> 
 <li>[MNG-7381] - 将并行构建器线程名称缩短为 artifactId， 有条件地使用 groupId</li> 
 <li>[MNG-7385] - 改进关于存储库元数据的文档</li> 
 <li>[MNG-7400] - 允许更多 WorkspaceReaders 参与</li> 
 <li>[MNG-7408] - 解释报告插件版本自动选择 （在 Maven 3 中）</li> 
</ul> 
<p><strong><span style="background-color:#ffffff; color:#222233">Dependency upgrade</span></strong></p> 
<ul> 
 <li>[MNG-7370] - 将 Maven Wagon 升级到 3.5.1</li> 
 <li>[MNG-7384] - 将 Maven JAR 插件升级到 3.2.2</li> 
 <li>[MNG-7428] - 将 Maven <span style="background-color:#ffffff; color:#222233">Parent </span>升级到 35</li> 
</ul> 
<p>详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.apache.org%2Fthread%2Fl01w7rxgz5btv4bkvjvrzzqgc9fmvt7r" target="_blank">查看官方公告</a>。</p>
                                        </div>
                                      
</div>
            