
---
title: 'Linux 5.19-rc8仍受Retbleed漏洞的影响 但距离问题解决已经不远'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0724/6605770916b315c.png'
author: cnBeta
comments: false
date: Sun, 24 Jul 2022 11:24:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0724/6605770916b315c.png'
---

<div>   
虽然通常情况下，对CPU漏洞进行安全缓解工作在漏洞禁运日的状态良好，但Retbleed是一个例外。在Retbleed被公开近两周后，围绕它的Linux内核补丁修复工作仍在继续，今天在Linux 5.19-rc8之前有更多的补丁被送来，以解决缓解处理带来的影响。<br>
 <p>这次的Retbleed补丁有点粗糙，许多问题直到这次投机执行攻击被公开和补丁被合并到Linux内核之后才被发现。在Retbleed补丁在"补丁星期二"登陆Linux内核后，各组织的Linux内核持续集成（CI）和构建方开始从被缓解的代码中发现一些边缘案例和不同的构建/运行时间问题。这些问题的出现要归功于于开发人员意识到并能够查看这些内核补丁。</p><p>随后一些后续的修复措施开始解决Retbleed代码的各种问题，今天又有一轮Retbleed的余波正在为情况依然不佳的Linux 5.19-rc8进行“再包扎”。</p><p>将近两周后，由于各种问题的出现，Retbleed的缓解措施仍然没有在Linux稳定系列中出现。但随着Retbleed修复措施的放缓，看起来缓解措施和所有的修复措施将很快在目前支持的稳定/LTS系列中首发。</p><p>今天早上，随着v5.19-rc8的x86/urgent新闻组列表更新，好消息终于来到，Borislav Petkov给Linus Torvalds发来消息说：</p><p>Hi，Linus请再拉出几个retbleed的fallout fixes。看起来他们的紧迫性在降低，所以看起来我们已经成功地抓住了规模有限的-rc测试所暴露的任何漏洞。也许我们正在准备... :)</p><p><img src="https://static.cnbetacdn.com/article/2022/0724/6605770916b315c.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>一些修复以防止返回thunks修补不需要的LKDTM模块，避免在eIBRS部分的每个内核条目上写入SPEC_CTRL MSR，从而增强错误输出；通过在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> CPU上发出IBPB来保护EFI固件调用，以及将Retbleed缓解明确限制在x86_64内核。正如昨天所指出的，Retbleed缓解措施在x86 32位内核上不起作用，而且关键的上游开发者也没有兴趣去做这方面的支持。这些只是功能修复，但Retbleed对受影响的CPU型号仍有相当大的影响。</p><p>这些Retbleed修复和其他各种修复将是今天晚些时候推出的Linux 5.19-rc8内核的一部分。Linux 5.19稳定版预计将在下周末发布。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1296039.htm" target="_blank">Linux x86 32位架构易受Retbleed漏洞影响 但别指望它能快速得到修复</a></p></div>   
</div>
            