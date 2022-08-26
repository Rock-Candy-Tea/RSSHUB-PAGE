
---
title: 'GitLab 15.3 发布，GitOps 功能现已免费'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b8648eaba51c40abac0655d2c24f4a9060e.png'
author: 开源中国
comments: false
date: Fri, 26 Aug 2022 07:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b8648eaba51c40abac0655d2c24f4a9060e.png'
---

<div>   
<div class="content">
                                                                                            <p>GitLab 15.3 已正式发布。新版本包含 63 项改进，亮点包括：</p> 
<ul> 
 <li>支持在 issue 中创建任务 (task)</li> 
 <li>免费提供 GitOps 功能</li> 
 <li>SAML 组链接 API</li> 
 <li>高级密码复杂度要求</li> 
</ul> 
<p>另外值得注意的是，在 15.3 发布的同时，11.3-15.1.4，15.2.x 和 15.3.0 被曝出了一个严重的远程代码执行漏洞 CVE-2022-2884，为了避免受影响，用户需要升级 GitLab CE/EE 到 15.1.5、15.2.3、15.3.1 或更高版本。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b8648eaba51c40abac0655d2c24f4a9060e.png" referrerpolicy="no-referrer"></p> 
<p><strong>在 issue 中创建任务 (task)</strong></p> 
<p>任务提供了一种将问题细化为更小、更离散的工作单元的可靠方法。在旧版 GitLab 中，用户可以使用描述中的 markdown checklists 将 issue 分解为更小的部分。但是，这些清单项目无法在描述字段之外的任何地方轻松分配、标记或管理。</p> 
<p>现在，用户可以从 Child Items 的 issue 中创建任务。然后，可以直接在 issue 内打开任务以快速更新标题、设置权重或添加描述。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0825/172902_5Owp_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><strong>免费提供 GitOps 功能</strong></p> 
<p>当使用 GitOps 更新 Kubernetes 集群时，将获得改进的安全模型、更好的可扩展性和稳定性。</p> 
<p>适用于 Kubernetes 的 GitLab 代理从其初始版本开始就已支持 GitOps 工作流，但该功能一直只面向 GitLab Premium 或 Ultimate 提供。现在，GitLabs 免费版也包含了该功能。</p> 
<p>官方表示，未来计划为高级订阅添加内置的多租户支持，该功能类似于CI/CD 工作流已经可用的模拟功能。</p> 
<p><strong>定义密码复杂性要求</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>GitLab 管理员现在可以定义密码复杂性要求以及最小密码长度。对于新密码，可以配置包含以下这些要素：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>数字</li> 
 <li>大写字母</li> 
 <li>小写字母</li> 
 <li>符号</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>复杂的密码不太可能被泄露，配置密码复杂性有助于管理员执行他们的密码策略。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a881adde19ba2d9f628e57ac359205a7df8.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fabout.gitlab.com%2Freleases%2F2022%2F08%2F22%2Fgitlab-15-3-released%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            