
---
title: 'GitHub 防黑客新措施：弃用账密验证 Git 操作，改用 token 或 SSH 密钥，今晚 0 点执行'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/8/6aea8a65-4022-438c-9916-61da21b0aed1.png'
author: IT 之家
comments: false
date: Sat, 14 Aug 2021 04:40:45 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/8/6aea8a65-4022-438c-9916-61da21b0aed1.png'
---

<div>   
<p>还在用账户 + 密码对 GitHub 上的 Git 操作进行身份验证？</p><p>赶紧整个 token（令牌）或 SSH 密钥吧！</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/6aea8a65-4022-438c-9916-61da21b0aed1.png" w="1080" h="134" title="GitHub 防黑客新措施：弃用账密验证 Git 操作，改用 token 或 SSH 密钥，今晚 0 点执行" width="1080" height="102" referrerpolicy="no-referrer"></p><p>8 月 14 号 0 点（8 月 13 日 9:00 PST）开始，<span class="accentTextColor">在 GitHub 上执行 Git 操作就会导致失败</span>。</p><p>GitHub 官方表示，这一举措是为了提高 Git 操作的安全性，防止密码撞库等事情发生。</p><h2>哪些操作会受影响？</h2><p>简单来说，如果你还在用账密验证 Git 操作，这些行为都会受到影响：</p><ul class=" list-paddingleft-2"><li><p>命令行 Git 访问</p></li><li><p>采用 Git 的桌面应用程序（GitHub Desktop 不受影响）</p></li><li><p>账密访问 GitHub 上 Git repo 的一切应用程序/服务</p></li></ul><p>这些用户不会受影响：</p><ul class="ai-word-checked list-paddingleft-2"><li><p>已经采用 token 或 SSH 密钥方式验证，即启用双因素身份验证（2FA）的用户</p></li><li><p>使用 GitHub Enterprise Server 本地产品的用户（该产品尚未对此进行更改）</p></li><li><p>使用 GitHub App 的用户，此前已经不支持账密验证</p></li></ul><p>当然，大部分经常使用 Git 的用户应该都已经知道这件事了。</p><p>在今年 6 月 30 号（15~18 时）、7 月 1 号（0~3 时）、7 月 28 号（15~18 时）和 29 号（0~3 时），GitHub 已经针对这件事进行了预演，所有 Git 操作都被要求用 token 或 SSH 密钥验证。</p><p>现在，这项举措已经变成一个永久措施。</p><p>GitHub 究竟为什么要这样做呢？</p><h2>token 和 SSH 密钥安全在哪里？</h2><p>首先需要了解，只用账户和密码进行身份验证会有什么隐患。</p><p>互联网上，每天都有大量网站遭受黑客攻击，导致数据外泄，这些数据中就包括不少用户的账号密码。</p><p>拿到账号密码后，黑客会用它们试着登录其他网站，也就是所谓的密码撞库。</p><p>简单来说，如果你 ABC 网站用的是一套账户密码，在 A 网站的密码被泄露后，BC 网站也可能会被盗号。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/5075b4b9-9497-4384-b023-cee55d761a9f.jpg@s_2,w_820,h_601" w="1080" h="792" title="GitHub 防黑客新措施：弃用账密验证 Git 操作，改用 token 或 SSH 密钥，今晚 0 点执行" srcset="https://img.ithome.com/newsuploadfiles/2021/8/5075b4b9-9497-4384-b023-cee55d761a9f.jpg 2x" width="1080" height="601" referrerpolicy="no-referrer"></p><p>为了防止密码撞库，网站会采取更多手段验证身份信息，像 GitHub 就推出了双因素身份验证、登录警报、设备认证、防用泄露密码及支持 WebAuth 等措施。</p><blockquote><p>双因素身份验证，是指在秘密信息（密码等）、个人物品（身份证等）、生理特征（指纹/虹膜/人脸等）这三种因素中，同时用两种因素进行认证的过程。</p></blockquote><p>现在，GitHub 开始强制用户采用 token 或 SSH 密钥进行身份验证。相比于账密，这两者的安全性显然更高：</p><ul class=" list-paddingleft-2"><li><p>唯一性：仅限 GitHub 使用，根据设备/使用次数生成</p></li><li><p>可撤销性：可随时被单独撤销，其他凭证不受影响</p></li><li><p>区域性：使用范围可控，只允许在部分访问活动中执行</p></li><li><p>随机性：不受撞库影响，比账密复杂度更高</p></li></ul><p>那么，token 和 SSH 密钥之间，哪个更合适呢？</p><p>虽然目前 GitHub 官方推荐的是 token，因为它设置更为简单，不过相比之下，SSH 密钥的安全性要更高一些。</p><p>还没有设置 token 或 SSH 密钥的 Git 用户，可以戳官方教程整起来了~</p><p>GitHub 设置教程：</p><p>[1]https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token</p><p>[2]https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent</p><p>参考链接：</p><p>[1]https://github.blog/changelog/2021-08-12-git-password-authentication-is-shutting-down/</p><p>[2]https://www.theregister.com/2021/08/12/git_proxyshell_gigabyte/</p>
          
</div>
            