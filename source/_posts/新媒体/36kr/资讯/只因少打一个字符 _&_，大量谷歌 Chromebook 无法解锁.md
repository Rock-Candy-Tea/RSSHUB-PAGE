
---
title: '只因少打一个字符 _&_，大量谷歌 Chromebook 无法解锁'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210726/v2_9cc6da7bbfe54d14bd1b3fab226f272b_img_000'
author: 36kr
comments: false
date: Mon, 26 Jul 2021 12:00:40 GMT
thumbnail: 'https://img.36krcdn.com/20210726/v2_9cc6da7bbfe54d14bd1b3fab226f272b_img_000'
---

<div>   
<p>初学编程的程序员难免会犯一些低级错误，这不难理解。</p> 
<p>可当这种低级错误出现在<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>经过三个开发者版本进而推出的 Chrome OS 正式版中时，就很令人疑惑：谷歌连这么明显的错误都没有看出来吗？</p> 
<p>上周，谷歌向 Chromebook 推送了一次 Chrome OS 版本更新，版本号为91.0.4772.165，而这次更新引起了重大 Bug：只因代码中少打一个字符“&”，导致大量用户无法解锁登录 Chromebook 。</p> 
<h2>小版本更新引起重大 Bug</h2> 
<p>自 6 月份谷歌正式发布 Chrome OS 91 稳定版以来，似乎就一直大小 Bug 不断。</p> 
<p>先是版本 91.0.4472.147 被用户反映 CPU 占用率太高，随后谷歌取消更新，使系统恢复到先前的 91.0.4472.114 版本，可这又引发了用户无法安装 Linux 的问题。</p> 
<p>本以为这些问题已经够糟心了，可跟这次 91.0.4772.165 版本导致的后果相比，简直是“小巫见大巫”。</p> 
<p>最早发现 Chrome OS91.0.4772.165 版本有问题的是网友 @u/rk_29，TA 在 Reddit 网站上发布了一则消息：</p> 
<p>警告：最新的稳定版更新正在阻止用户登录。我们建议你在进一步通知之前不要更新该版本。</p> 
<p class="image-wrapper"><img data-img-size-val="714,111" src="https://img.36krcdn.com/20210726/v2_9cc6da7bbfe54d14bd1b3fab226f272b_img_000" referrerpolicy="no-referrer"></p> 
<p>这则消息引来了众多 Chromebook 用户的关注，其中不少人因已更新而“遭殃”。有一位 Reddit 用户说，在更新至 91.0.4772.165 版本后，他们的两台 Chromebook 就无法顺利登录了。</p> 
<p>不仅登录界面无法识别正确账密，两台电脑状态也很不好。一台笔记本电脑陷入重启循环，另一台 Asus Chromebook C436 即便是采用 Powerwash（即强制重置为出厂状态，将 Chromebook 上存储的所有本地用户数据清除）也没办法解决问题，最终只能用 U 盘来让系统恢复到可用状态。</p> 
<p>这样的恢复方式未免代价也太过重大，因此彼时最好的建议就是暂时不要进行版本更新。如果 Chromebook 用户在系统托盘中收到更新提示，千万不要关闭电脑，否则 Chrome OS 会在开机时自动更新至有巨大 Bug 的 91.0.4772.165 版本。</p> 
<p>但正如有人向来不喜欢最新系统，也有那么一部分人就是习惯及时更新，因而这次 Chrome OS 更新导致的 Bug 使许多人都“中招”了。突然无法正常登录的电脑极大影响了他们的工作生活，为此不得不重装系统丢失重要文件的也不在少数，由此惹怒了许多用户。</p> 
<h2>只因缺少一个字符“&”</h2> 
<p>这个版本引起的混乱自然引起了谷歌的注意，它迅速删除了 91.0.4472.165 版本，并将 Chromebook 的系统版本退回至 91.0.4472.147，虽然这个版本也不是太安全，但起码用户可以登入电脑了。</p> 
<p>谷歌在 20 日的声明中说已经确定了问题所在，将于 21 日发布修复程序。而对于担心数据丢失的受影响用户来说，如果能等到 21 日谷歌的修复版本，待设备自动更新就无需通过 Powerwash 实现登录。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,363" src="https://img.36krcdn.com/20210726/v2_a74bf561115a482dba12a00bb18f2c85_img_000" referrerpolicy="no-referrer"></p> 
<p>随后谷歌按时推出了修复版本 91.0.4472.167，这应该也是谷歌对这次重大事故给出的最终解决方案。只要 Chromebook 系统更新至此新版本，用户就可以顺利登入电脑进行正常操作。</p> 
<p>虽然表面看来，91.0.4772.165 版本引发的问题到这里就告一段落了，但好奇心驱使人进行更深一步的探索：这么重大的 Bug 到底是由什么引起的？</p> 
<p>所幸 Chrome OS 是一款开源的操作系统，因此一切都有迹可循。一位 Reddit 用户 @elitist_ferret 就在其源码中疑似发现了问题所在：只因少打了一个字符“&”。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,418" src="https://img.36krcdn.com/20210726/v2_9495383bd226425089de1276283f8f78_img_000" referrerpolicy="no-referrer"></p> 
<p>谷歌将 Chrome OS 的 Cryptohome VaultKeyset 中的一个条件语句写错了，而这正是操作系统中保存用户加密密钥的关键部分。这一行原本应该是</p> 
<blockquote> 
 <p>if (key_data_.has_value() && !key_data_->label().empty()) &#123;</p> 
</blockquote> 
<p>但引发重大 Bug 的 91.0.4772.165 版本中这部分却少打了一个“&”（C++ 中逻辑与“AND”运算符的正确写法为“&&”），这就导致了 Chrome OS 无法解密登录信息：</p> 
<blockquote> 
 <p>if (key_data_.has_value() & !key_data_->label().empty()) &#123;</p> 
</blockquote> 
<h2>网友：谷歌没有 QA 测试吗?</h2> 
<p>这种错误实在太过低级，尤其是出现在谷歌通常要经过三个开发者测试版才推出的稳定版系统更新时，就显得更加匪夷所思。</p> 
<p>众多网友对这个低级错误引起的巨大 Bug 也感到非常疑惑：</p> 
<p>“这怎么能通过质量保证流程？谷歌是在没有进行 QA 测试的情况下就将代码发布推送了吗？”</p> 
<p>“谷歌取消质量检查了？”</p> 
<p>“测试时怎么会找不到这个 Bug ？！这让我觉得谷歌没有像我对操作系统制造商所期望的那样拥有强大的设备+足够的测试。”</p> 
<p>有网友猜测这可能是因为三个开发者版本的代码都不同：</p> 
<p>“我猜谷歌不会在测试过程的每个版本中都推送完全相同的代码。从 beta 到正式推送的期间，有人可能进行了手动更改以适应新环境，然后意外删除了一个不应该被触及领域的字符。不过谷歌还是应该在发布更新之前审查测试版和稳定版之间的所有更改。”</p> 
<p>有网友庆幸自己没有及时更新系统的习惯：</p> 
<p>“这就是我讨厌强制更新的原因。一般像我这样经验丰富的 IT 专业人士选择更新时，通常是在一大群人都更新了并且没有报告任何问题之后。”</p> 
<p>而这种低级错误也对谷歌产生了一定的负面影响：</p> 
<p>“谷歌在向我们展示这就是为什么 Chrome OS 还没有准备好迎接黄金时段。”</p> 
<p>“我猜谷歌会说：是实习生的错。相信我们，真的是实习生的错。”</p> 
<p>“我现在更没有理由也更不想使用 Chromebook。”</p> 
<p>那么对谷歌这次因更新引起的重大 Bug，你有什么看法吗？</p> 
<p>参考链接：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>https://arstechnica.com/gadgets/2021/07/google-pushed-a-one-character-typo-to-production-bricking-chrome-os-devices/?comments=1</p></li> 
 <li><p>https://www.androidpolice.com/2021/07/20/a-new-chrome-os-91-update-is-breaking-chromebooks-like-a-bull-in-a-china-shop/</p></li> 
 <li><p>https://www.reddit.com/r/chromeos/comments/onlcus/update_it_seems_google_has_pulled_the_165_stable/?sort=top</p></li> 
</ul> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/U4KEM7gRjQ2Y392jpkaypA">“CSDN”（ID:CSDNnews）</a>，作者：郑丽媛，36氪经授权发布。</p>  
</div>
            