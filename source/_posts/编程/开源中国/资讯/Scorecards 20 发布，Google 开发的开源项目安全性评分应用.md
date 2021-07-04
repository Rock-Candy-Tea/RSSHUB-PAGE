
---
title: 'Scorecards 2.0 发布，Google 开发的开源项目安全性评分应用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1096'
author: 开源中国
comments: false
date: Sun, 04 Jul 2021 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1096'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Scorecards 是谷歌开发，由开源安全基金会 (OpenSSF) 开源的首批项目之一，其目标是为开源项目自动生成一个 "安全分数"，以帮助用户确定用例的信任度、风险和安全态势。</p> 
<p>Scorecards 2.0 正式发布，本次更新的内容包括：</p> 
<ul> 
 <li>识别风险：自去年秋天以来，Scorecards 的覆盖范围不断扩大；该项目增加了几个新的检查，遵循 Google 的「Know, Prevent, Fix」框架。</li> 
 <li>发现恶意贡献者：具有恶意意图或被盗帐户的贡献者可能会在代码中引入潜在的后门。代码审查有助于减轻此类攻击。通过新的 "分支保护" 检查，开发人员可以验证项目在提交代码之前是否强制要求另一个开发人员进行代码审查。目前，由于 GitHub API 的限制，这个检查只能由仓库管理员运行。</li> 
 <li>易受攻击的代码： 即使开发人员和同行评审尽了最大努力，但糟糕的代码仍然可以进入代码库而不被发现。这就是为什么要启用持续模糊测试和静态代码测试以在开发生命周期的早期捕获错误很重要的原因 。Scorecards 现在会检查项目是否使用模糊测试和 SAST 工具作为其持续集成/持续部署 (CI/CD)管道的一部分。</li> 
 <li>构建系统妥协： GitHub 项目使用的常见 CI/CD 解决方案是 GitHub Actions。这些操作工作流的危险在于它们可能会处理不受信任的用户输入。这意味着，攻击者可以制作恶意拉取请求以获得对特权 GitHub 令牌的访问权限，并因此能够将恶意代码推送到存储库而无需审查。为了降低这种风险，Scorecard 的令牌权限（Token-Permissions）预防检查现在通过将 GitHub 令牌设置为默认只读来验证 GitHub 工作流是否遵循最小权限原则。</li> 
 <li>不良依赖： 程序的安全性取决于其最弱的依赖项。这听起来很明显，但是了解我们的依赖项的第一步就是声明它们。有了这些来源信息，你就可以评估程序的风险并降低这些风险。</li> 
 <li>加密哈希让我们将依赖项固定为一个已知值。如果这个值发生变化，构建系统会检测到它并拒绝构建。固定依赖项在我们有依赖项的任何地方都很有用：不仅在编译期间，而且在 Dockerfiles、CI/CD 工作流等中。Scorecards 使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fossf%2Fscorecard%2Fblob%2Fmain%2Fchecks%2Fchecks.md%23frozen-deps" target="_blank">Frozen-Deps</a> check 来检查这些模式。此检查有助于缓解恶意依赖项攻击，例如最近的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fabout.codecov.io%2Fsecurity-update%2F" target="_blank">CodeCov</a> 攻击。</li> 
 <li>当在修补依赖项的漏洞时，散列也需要不时更新。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.github.com%2Fen%2Fcode-security%2Fsupply-chain-security%2Fmanaging-vulnerabilities-in-your-projects-dependencies%2Fconfiguring-dependabot-security-updates" target="_blank">Dependabot</a> 或 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frenovatebot%2Frenovate" target="_blank">renovatebot</a> 等工具可以查看和更新哈希值。Scorecards <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fossf%2Fscorecard%2Fblob%2Fmain%2Fchecks%2Fchecks.md%23automatic-dependency-update" target="_blank">Automated-Dependency-Update</a> 检查验证开发人员是否依赖此类工具来更新他们的依赖项。</li> 
 <li>在将其用作依赖项之前了解项目中的漏洞很重要。Scorecards 可以通过新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fossf%2Fscorecard%2Fblob%2Fmain%2Fchecks%2Fchecks.md%23vulnerabilities" target="_blank">漏洞</a>检查提供此信息，而无需订阅漏洞警报系统。</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fossf%2Fscorecard%2Freleases" target="_blank">https://github.com/ossf/scorecard/releases</a></p>
                                        </div>
                                      
</div>
            