
---
title: 'ChromeOS更新源码打错一个符号，笔记本变砖'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2018/09/f96953561324ec8e2505a3246266a5ca.jpg!custom'
author: 煎蛋
comments: false
date: Tue, 27 Jul 2021 08:57:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2018/09/f96953561324ec8e2505a3246266a5ca.jpg!custom'
---

<div>   
<blockquote><p>Chrome OS 91.0.4472.165版本现在应该修正了吧</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2018/09/f96953561324ec8e2505a3246266a5ca.jpg!custom" referrerpolicy="no-referrer"><p>谷歌表示，它已经修复了一个重大的Chrome OS漏洞。该漏洞会导致用户无法登陆自己的设备。谷歌的公告说，上周短暂推出的Chrome OS 91.0.4472.165版本，使用户无法登录他们的设备，将PC电脑锁死。</p>
<p>Chrome OS会自动下载更新，并在重启后切换到新版系统。然而，重启的设备会锁死。所以，如果下载了上述更新，建议不要重启。</p>
<p>官方在几天前的公告说，正在推出的91.0.4472.167版本可以解决这个问题，但可能需要 "几天" 的时间。受不良更新影响的用户可以等待下一次更新，或者给设备 “放电"(主板放电按道理不会掉硬盘数据，但Chrome OS不了解)——意味着擦除所有本地数据——以获得登录权限。因为Chrome OS主要是基于云的系统，所以这个解决方案带来的问题比在其他操作系统上要少。但是，当然，丢失数据肯定会带来不便。</p>
<p>ChromeOS是开源的，所以我们可以得到更多关于bug的细节，这还要感谢安卓警察找到了用户elitist_ferret的Reddit评论。</p>
<p>这个问题显然可以归结为代码错误。谷歌在Chrome OS的Cryptohome VaultKeyset中弄错了一个条件语句——操作系统中保存用户加密密钥的部分语句。</p>
<p><strong>那一行应该是 </strong></p>
<p>"if (key_data_.has_value() && !key_data_->label().empty()) &#123;"，</p>
<p>但是更新中错把"&&"——C++版本的 "AND" 运算符——替换成了“&”，破坏了条件语句的后半部分。</p>
<p>由于这个错误，Chrome OS无法根据存储的密钥正确核查用户密码，所以即使是正确的密码，也会有一条消息说："对不起，你的密码未经验证。"</p>
<p>Chrome OS的整个卖点是它的可靠性，而像这样的错误无疑会损害操作系统的声誉。目前还不清楚像这样一个明显的、令人震惊的问题是如何进入发布渠道的。</p>
<p>Chrome OS有三大测试环节，"金丝雀"、"开发 "和 "测试"渠道，在两个版本之间有数周的测试期。但不知何故，这个bug成了漏网之鱼。</p>
<p>https://arstechnica.com/gadgets/2021/07/google-pushed-a-one-character-typo-to-production-bricking-chrome-os-devices/</p>  
</div>
            