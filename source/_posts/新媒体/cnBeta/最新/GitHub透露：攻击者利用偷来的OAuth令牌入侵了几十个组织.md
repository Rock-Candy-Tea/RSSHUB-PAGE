
---
title: 'GitHub透露：攻击者利用偷来的OAuth令牌入侵了几十个组织'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0416/4528f6dabb31e9d.webp'
author: cnBeta
comments: false
date: Sat, 16 Apr 2022 07:02:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0416/4528f6dabb31e9d.webp'
---

<div>   
GitHub今天透露，一名攻击者正在使用偷来的OAuth用户令牌（原本发放给Heroku和Travis-CI），从私人仓库下载数据。自2022年4月12日首次发现这一活动以来，威胁者已经从几十个使用Heroku和Travis-CI维护的OAuth应用程序（包括npm）的受害组织中访问并窃取数据。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0416/4528f6dabb31e9d.webp" title alt="GitHub_headpic.webp" referrerpolicy="no-referrer"></p><p>"这些集成商维护的应用程序被GitHub用户使用，包括GitHub本身，"GitHub的首席安全官（CSO）Mike Hanley今天透露。"我们不相信攻击者是通过破坏GitHub或其系统来获得这些令牌的，因为GitHub没有以原始的可用格式存储这些令牌。我们对威胁行为者的其他行为的分析表明，行为者可能正在挖掘被盗的OAuth令牌所能访问的下载的私有仓库内容，以寻找可用于渗透其他基础设施的秘密。"</p><p>根据Hanley的说法，受影响的OAuth应用程序的列表包括：</p><blockquote><p>Heroku Dashboard（ID：145909）</p><p>Heroku Dashboard (ID: 628778)</p><p>Heroku Dashboard - Preview (ID: 313468)</p><p>Heroku Dashboard - Classic (ID: 363831)</p><p>Travis CI (ID: 9216)</p></blockquote><p>GitHub安全部门在4月12日发现了对GitHub的npm生产基础设施的未经授权的访问，因为攻击者使用了一个被泄露的AWS API密钥。攻击者很可能是在使用偷来的OAuth令牌下载了多个私有npm仓库后获得了该API密钥。</p><p>"在4月13日晚上发现非GitHub或npm存储的第三方OAuth令牌被更广泛地窃取后，我们立即采取行动，通过撤销与GitHub和npm内部使用这些受损应用程序有关的令牌来保护GitHub和npm，"Hanley补充说。对npm组织的影响包括未经授权访问GitHub.com的私有存储库和"潜在访问"AWS S3存储上的npm包。</p><p>GitHub的私人存储库未受影响</p><p>虽然攻击者能够从被攻击的存储库中窃取数据，但GitHub认为，在这次事件中，没有一个软件包被修改，也没有用户账户数据或凭证被访问。</p><p>Hanley说："npm使用与GitHub.com完全不同的基础设施；GitHub在这次原始攻击中没有受到影响。虽然调查仍在继续，但我们没有发现任何证据表明其他GitHub拥有的私有仓库被攻击者使用窃取的第三方OAuth令牌克隆。"</p><p><img src="https://static.cnbetacdn.com/article/2022/0416/6b8aacc6e132233.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>GitHub正在努力通知所有受影响的用户和组织，因为他们被确认了更多信息。</p><p>作为GitHub的成员，您应该应该审查您和您的组织的审计日志和用户账户的安全日志，看看是否有异常的、潜在的恶意活动。</p><p>您可以在周五发布的安全警报中找到更多关于GitHub如何应对以保护其用户以及客户和组织需要知道的信息。</p>   
</div>
            