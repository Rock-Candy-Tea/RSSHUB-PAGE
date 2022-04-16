
---
title: 'GitHub：有人用偷来的 OAuth 令牌入侵了几十个组织，已采取保护措施'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/4/f4bbe527-5122-4a74-bf07-86f455caae4f.jpg'
author: IT 之家
comments: false
date: Sat, 16 Apr 2022 07:21:55 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/4/f4bbe527-5122-4a74-bf07-86f455caae4f.jpg'
---

<div>   
<p data-vmark="a574"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 4 月 16 日消息，GitHub 官方今日发公告，GitHub Security 在 4 月 12 日发现有攻击者利用被盗的 OAuth 用户令牌（原属于 Heroku 和 Travis-CI 两家第三方集成商），从私人仓库下载数据。</p><p data-vmark="8ba0">据称，自 2022 年 4 月 12 日首次发现这一活动以来，威胁者已经从几十个使用上述集成商维护 OAuth 应用程序（包括 npm）的受害组织中访问并窃取数据。</p><p data-vmark="607c" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/4/f4bbe527-5122-4a74-bf07-86f455caae4f.jpg" w="680" h="357" title="GitHub：有人用偷来的 OAuth 令牌入侵了几十个组织，已采取保护措施" width="680" height="357" referrerpolicy="no-referrer"></p><p data-vmark="43ab">据称，很多 GitHub 用户会使用这些集成商维护的应用程序，包括 GitHub 本身。</p><p data-vmark="3e54">GitHub 不相信攻击者是通过 GitHub 或其系统的入侵获得这些令牌的，因为 GitHub 并没有以原始的可用格式保存令牌。经过调查，参与者可能正在偷偷下载一些私库内容，以获取可以用于其他基础设施的秘密。</p><p data-vmark="91e0">截至 2022 年 4 月 15 日的已知受影响的 OAuth 应用程序：</p><ul class=" list-paddingleft-2"><li><p data-vmark="caaa">Heroku Dashboard （ID： 145909）</p></li><li><p data-vmark="9222">Heroku Dashboard （ID： 628778）</p></li><li><p data-vmark="7bbd">Heroku Dashboard – Preview （ID： 313468）</p></li><li><p data-vmark="04d9">Heroku Dashboard – Classic （ID： 363831）</p></li><li><p data-vmark="d59b">Travis  CI （ID： 9216）</p></li></ul><p data-vmark="4ff2">4 月 12 日，GitHub Security 发现 npm 生产基础设施出现未经授权的访问，当时攻击者使用的是一个受损的 AWS API 密钥。</p><p data-vmark="500e">根据后续分析，GitHub 认为该 API 密钥是由攻击者在下载一组私有 npm 库时获得的，攻击者使用了从上述两个受影响的第三方 OAuth 应用程序之一窃取的 OAuth 令牌。</p><p data-vmark="5d89">IT之家了解到，在 4 月 13 日晚发现第三方 OAuth 令牌被盗后 GitHub 便立即采取了行动，撤销了与 GitHub 和 npm 内部使用这些被盗应用程序相关的令牌以保护用户数据。</p>
          
</div>
            