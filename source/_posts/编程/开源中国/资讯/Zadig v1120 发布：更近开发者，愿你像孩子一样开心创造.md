
---
title: 'Zadig v1.12.0 发布：更近开发者，愿你像孩子一样开心创造'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f32f37e875016cf6fe4db85bf0801543d54.png'
author: 开源中国
comments: false
date: Wed, 01 Jun 2022 08:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f32f37e875016cf6fe4db85bf0801543d54.png'
---

<div>   
<div class="content">
                                                                                            <div>
 <img height="766" src="https://oscimg.oschina.net/oscnet/up-f32f37e875016cf6fe4db85bf0801543d54.png" width="1800" referrerpolicy="no-referrer">
</div> 
<div>
  
</div> 
<div> 
 <p data-darkreader-inline-color style="--darkreader-inline-color:#cac5be; color:#303030; margin-left:0px; margin-right:0px; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxie.infoq.cn%2Flink%3Ftarget%3Dhttps%253A%252F%252Fwww.oschina.net%252Faction%252FGoToLink%253Furl%253Dhttps%25253A%25252F%25252Fgithub.com%25252Fkoderover%25252Fzadig" target="_blank">Zadig on Github</a></p> 
 <p data-darkreader-inline-color style="--darkreader-inline-color:#cac5be; color:#303030; margin-left:0px; margin-right:0px; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxie.infoq.cn%2Flink%3Ftarget%3Dhttps%253A%252F%252Fgitee.com%252Fkoderover%252Fzadig" target="_blank">Zadig on Gitee</a></p> 
</div> 
<div>
 迎六一，Zadig 正式推出 v1.12.0，以 
 <strong>开发者体验</strong>为重要使命，面向开发者 
 <strong>推出 VScode 插件</strong>，好工具就要到最后一公里；环境模块进一步增强 
 <strong>自测模式的</strong>应用范围，全面支持了 K8s YAML、Helm Chart 部署类型的项目；企业场景接入更为 
 <strong>简易灵活</strong>，支持 
 <strong>全局构建模板</strong>、代码源支持 
 <strong>标准 Git 协议</strong>、 
 <strong>现有 NS 零负担迁移</strong>；支持 
 <strong>GitOps 模式，</strong>服务配置可监听代码变更实现自动更新同步，Enjoy ～
</div> 
<div> 
 <h1>面向开发者增强终端能力，开发尽丝滑</h1> 
 <h3>正式推出 VS Code 插件，本地开发更高效</h3> 
</div> 
<div>
 面向开发者提供了环境查看，服务重启、详情查看、镜像更换，Pod 实时日志查看等功能，同时还支持远程开发容器配置，远程调试本地应用程序等。可以通过 VS Code 应用商店搜索下载：Zadig Toolkit
</div> 
<div> 
 <div>
  <img height="1834" src="https://oscimg.oschina.net/oscnet/up-000dc2ddaa3c070c800cc94bfc02b553d3d.png" width="2918" referrerpolicy="no-referrer">
 </div> 
</div> 
<div> 
 <h3>自测模式增强，人手一套子环境，开发者联调不用愁</h3> 
</div> 
<div>
 Zadig “自测模式” 全面支持 K8s YAML、Helm 部署类型的项目，基于 Istio + Tracing 技术方案实现上百开发者一套环境下的高效协作，管理员通过开启自测模式，工程师可以方便的创建独立自测联调子环境
</div> 
<div>
  
</div> 
<ul> 
 <li>管理员开启自测模式：</li> 
</ul> 
<div>
 <img height="1670" src="https://oscimg.oschina.net/oscnet/up-02714e3707deb7f336a46ddceb613b6cdca.png" width="2960" referrerpolicy="no-referrer">、
</div> 
<div>
  
</div> 
<ul> 
 <li>开发者创建子环境：</li> 
</ul> 
<div>
 <img height="1670" src="https://oscimg.oschina.net/oscnet/up-f290e7e86be5353d988be4cc9a9b1cbca71.png" width="2960" referrerpolicy="no-referrer">
</div> 
<div>
  
</div> 
<ul> 
 <li>按需选择自测联调的服务：</li> 
</ul> 
<div>
 <img height="1672" src="https://oscimg.oschina.net/oscnet/up-874b3605f35f5792eb557d41328d6659666.png" width="2960" referrerpolicy="no-referrer">
</div> 
<div> 
 <h3>代码扫描即服务，为开发过程安全保驾</h3> 
</div> 
<div>
 支持代码扫描功能模块，通过 Webhook 同步异步触发自动扫描服务，第一时间将代码里的 
 <code>坏味道</code>反馈给开发者。
</div> 
<div> 
 <div> 
  <div>
   <img height="1674" src="https://oscimg.oschina.net/oscnet/up-0deb841297cbad5886101f34b87657b8818.png" width="2960" referrerpolicy="no-referrer">
  </div> 
  <div>
   <img height="1674" src="https://oscimg.oschina.net/oscnet/up-327b764295a356aef2567839830f9baafdf.png" width="2960" referrerpolicy="no-referrer">
  </div> 
 </div> 
</div> 
<div> 
 <h1>场景接入更灵活简易，通用又强大</h1> 
</div> 
<div> 
 <h3>支持全局构建模板，运维负担再次降低</h3> 
</div> 
<div>
 继 K8s YAML 模板库、K8s Helm Chart 模板库、Dockfile 模板库，重磅支持全局构建模版；数百微服务构建脚本只需一份搞定管理维护，尤其适合一个微服务一个代码仓的场景，向一切碎片化运维说不。
</div> 
<div>
  
</div> 
<ul> 
 <li>抽取通用构建过程为构建模板：</li> 
</ul> 
<div>
 <img height="721" src="https://oscimg.oschina.net/oscnet/up-e2772f15ad613329bf95af135a81caa2261.png" width="1280" referrerpolicy="no-referrer">
</div> 
<div>
  
</div> 
<ul> 
 <li>使用模板创建构建，组织服务和代码库即可，无需关注其他构建碎片信息：</li> 
</ul> 
<div>
 <img height="724" src="https://oscimg.oschina.net/oscnet/up-46bee38c0fdc6ce7cd74b978d9d46c85e2d.png" width="1280" referrerpolicy="no-referrer">
</div> 
<div> 
 <h3>支持集成标准 Git 协议，任何代码源皆可接入</h3> 
</div> 
<div>
 除了支持较为普遍的代码源，诸如 GitLab/GitHub/Gerrit/Gerrit，为方便更多企业现状场景，支持了标准的 Git 协议代码源接入。
</div> 
<div>
 <img height="721" src="https://oscimg.oschina.net/oscnet/up-29a9f2f57f74639d96d19e95b35a7b2f8d0.png" width="1280" referrerpolicy="no-referrer">
</div> 
<div>
 <img height="722" src="https://oscimg.oschina.net/oscnet/up-5fa95d8f6e90fba62de9eb0bdb0290666e0.png" width="1280" referrerpolicy="no-referrer">
</div> 
<div> 
 <h3>现有 NS 零负担迁移，接入更方便</h3> 
</div> 
<div> 
 <div>
  K8s YAML 项目支持从现有 K8s 导入服务，几乎无迁移成本，走上云原生交付流程。
 </div> 
</div> 
<div>
 <img height="721" src="https://oscimg.oschina.net/oscnet/up-12bcc60c8d74ba809eeca955af8087e78e4.png" width="1280" referrerpolicy="no-referrer">
</div> 
<div> 
 <h1>同步功能开启，GitOps 一触即发</h1> 
</div> 
<div> 
 <h3>服务配置 AsCode，环境自动更新</h3> 
</div> 
<div> 
 <div>
  代码库中服务配置变更，可以自动通知更新环境
 </div> 
</div> 
<div>
 <img height="639" src="https://oscimg.oschina.net/oscnet/up-cb6037754397bf0c8b0f0a23a73f981ad2e.gif" width="1152" referrerpolicy="no-referrer">
</div> 
<div> 
 <h3>模板库支持同步能力，运维便利更强大</h3> 
</div> 
<div> 
 <div>
  K8s YAML 模板/Helm Chart 模板支持自动同步，变更后只需一键操作，即可自动应用到所有相关的服务配置
 </div> 
</div> 
<div>
 <img height="639" src="https://oscimg.oschina.net/oscnet/up-412c251a4e5af7fba8613c2734412c498a5.gif" width="1152" referrerpolicy="no-referrer">
</div> 
<div> 
 <h3>支持从 Gitee 代码库中同步服务配置，全场景覆盖</h3> 
</div> 
<div> 
 <div>
  继 v1.11.0 支持 Gitee 代码集成后，进一步增强对 Gitee 生态的支持；新增服务配置、模板库从 Gitee 仓库同步和导入能力的支持，Gitee 用户可以一站式接入 Zadig，实现完整的云原生交付流程
 </div> 
</div> 
<div>
 <img height="721" src="https://oscimg.oschina.net/oscnet/up-128849e72f70b9cf0ce2c0f8ce776f592aa.png" width="1280" referrerpolicy="no-referrer">
</div> 
<div>
 <img height="723" src="https://oscimg.oschina.net/oscnet/up-cfc9f0767d8ca6da9d133380a3674c92daf.png" width="1280" referrerpolicy="no-referrer">
</div> 
<div> 
 <h1>新增功能详情列表</h1> 
</div> 
<div>
 开发者工具
</div> 
<ul> 
 <li>支持 VS Code Plugin</li> 
</ul> 
<div>
 项目
</div> 
<ul> 
 <li>支持代码扫描</li> 
</ul> 
<ul> 
 <li>支持服务关联多个构建</li> 
</ul> 
<ul> 
 <li> 
  <div>
   K8s YAML 项目支持从现有 K8s 导入服务
  </div> </li> 
</ul> 
<ul> 
 <li> 
  <div>
   支持从 Gitee 代码库中同步服务配置
  </div> </li> 
</ul> 
<ul> 
 <li> 
  <div>
   支持服务配置变更后自动更新环境
  </div> </li> 
</ul> 
<ul> 
 <li> 
  <div>
   支持 
   <code>主机登录</code>权限独立管理
  </div> </li> 
</ul> 
<ul> 
 <li> 
  <div>
   K8s YAML 项目变量编辑框支持多行输入
  </div> </li> 
</ul> 
<div> 
 <div>
  模板库
 </div> 
</div> 
<ul> 
 <li> 
  <div>
   支持全局构建模板
  </div> </li> 
</ul> 
<ul> 
 <li> 
  <div>
   支持从 Gitee 代码源导入 Helm Chart 模板
  </div> </li> 
</ul> 
<ul> 
 <li> 
  <div>
   支持 K8s YAML 模板/Helm Chart 模板变更后自动更新服务配置
  </div> </li> 
</ul> 
<div>
 环境
</div> 
<ul> 
 <li>K8s Helm Chart 环境支持自测模式</li> 
</ul> 
<ul> 
 <li>K8s Helm Chart 环境支持 Release 视图</li> 
</ul> 
<div>
 工作流
</div> 
<ul> 
 <li>支持 IM 通知配置多个</li> 
</ul> 
<ul> 
 <li>支持自定义构建代码过滤规则</li> 
</ul> 
<div>
 系统设置
</div> 
<ul> 
 <li>支持配置全局系统权限</li> 
</ul> 
<ul> 
 <li>支持集成多个 Jenkins</li> 
</ul> 
<ul> 
 <li>支持配置默认登录页面</li> 
</ul> 
<ul> 
 <li>主机管理支持 HTTP/HTTPS 健康检查</li> 
</ul> 
<ul> 
 <li>支持集成标准 Git 协议的代码源</li> 
</ul> 
<ul> 
 <li> 
  <div>
   多集群管理升级能力增强
  </div> </li> 
</ul> 
<ul> 
 <li>支持 dind 多副本</li> 
</ul> 
<div>
 优化和缺陷修复：
</div> 
<ul> 
 <li>前端按钮级别的权限控制</li> 
</ul> 
<ul> 
 <li> 
  <div>
   环境中的服务列表支持一键刷新
  </div> </li> 
</ul> 
<ul> 
 <li>修复 K8s YAML 项目使用版本回溯的版本无法创建环境的问题</li> 
 <li>修复镜像清理功能状态异常情况下无法继续清理的问题</li> 
</ul> 
<div> 
 <h1>Release Note</h1> 
</div> 
<div>
 Developer Tools
</div> 
<ul> 
 <li>VS Code developer plugin</li> 
</ul> 
<div>
 Project
</div> 
<ul> 
 <li>SourceCode scanning has been supported</li> 
 <li>Service can be linked to multiple builds</li> 
 <li>Services can be loaded from kubernetes cluster</li> 
 <li>Services can be loaded from Gitee</li> 
 <li>Environments can be automatically updated when the service is updated</li> 
 <li>Minor improvements</li> 
</ul> 
<div>
 Templates
</div> 
<ul> 
 <li>Build template has been added</li> 
 <li>Helm chart template can be loaded from Gitee</li> 
 <li>Service created from templates can automatically be updated after the template's update.</li> 
</ul> 
<div>
 Environment
</div> 
<ul> 
 <li>Testing mode for helm projects.</li> 
 <li>Helm Releases can be listed for helm projects.</li> 
 <li>Add a button to refresh the service list.</li> 
</ul> 
<div>
 Workflow
</div> 
<ul> 
 <li>Multiple IM notification support.</li> 
 <li>Branch/Tag filter for repository when executing workflow.</li> 
</ul> 
<div>
 System
</div> 
<ul> 
 <li>Multiple Jenkins integration</li> 
 <li>Clone with git protocol is supported.</li> 
 <li>Multiple DinD instances are supported</li> 
 <li>Minor improvements</li> 
</ul> 
<div>
 Bugfix & Improvements
</div> 
<ul> 
 <li>Button-level authorization config implemented</li> 
 <li>Minor bugfixes</li> 
</ul> 
<div> 
 <h3> </h3> 
</div> 
<div>
 <strong>特别感谢以下社区小伙伴，提出的宝贵建议：</strong>
</div> 
<div>
 @Alex @dav @乔克@Eʟɪᴀᴜᴋ @Aurora @添 @ 
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkoderover%2Fzadig%2Fissues%3Fq%3Dis%3Aissue%2Bis%3Aopen%2Bauthor%3Azwkno1" target="_blank">zwkno1</a> @In @fangzhengjin @天堂@杭州@John Wong @leim @renle177 @ 
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fploynomail" target="_blank">ploynomail</a> @ 
 <a href="https://gitee.com/shouyong">shouyong</a> @Oliver+7 @Zzzzzz @Good Time @放开那女孩
</div> 
<div>
  
</div> 
<div>
 <strong>同时感谢代码贡献者，让 Zadig 更开放、强大：</strong>
</div> 
<div>
 @ 
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzxdvd" target="_blank">zxdvd</a>
</div> 
<ul> 
 <li>https://github.com/koderover/zadig/pull/1538</li> 
 <li>https://github.com/koderover/zadig/pull/1412</li> 
 <li>https://github.com/koderover/zadig/pull/1516<span> </span></li> 
 <li>https://github.com/koderover/zadig/pull/1517</li> 
</ul> 
<div>
 @ 
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frovast" target="_blank">rovast</a>
</div> 
<ul> 
 <li>https://github.com/koderover/zadig-portal/pull/862</li> 
</ul> 
<div> 
 <div>
   
 </div> 
</div> 
<div> 
 <div>
  Zadig，让工程师更专注创造！欢迎加入 
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg4NDY0NTMyNw%3D%3D%26mid%3D2247485614%26idx%3D2%26sn%3D408952415996c09a72c000f651ee1928%26chksm%3Dcfb4440ef8c3cd18c4d2a0be5db803422b22d9086d771645acc39727e863d98dfa60b5be596c%26scene%3D21%23wechat_redirect" target="_blank">开源吐槽群🔥</a>
 </div> 
 <div>
   
 </div> 
 <div> 
  <p data-darkreader-inline-color style="--darkreader-inline-color:#cac5be; color:#303030; margin-left:0px; margin-right:0px; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxie.infoq.cn%2Flink%3Ftarget%3Dhttps%253A%252F%252Fwww.oschina.net%252Faction%252FGoToLink%253Furl%253Dhttps%25253A%25252F%25252Fgithub.com%25252Fkoderover%25252Fzadig" target="_blank">Zadig on Github</a></p> 
  <p data-darkreader-inline-color style="--darkreader-inline-color:#cac5be; color:#303030; margin-left:0px; margin-right:0px; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxie.infoq.cn%2Flink%3Ftarget%3Dhttps%253A%252F%252Fgitee.com%252Fkoderover%252Fzadig" target="_blank">Zadig on Gitee</a></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            