
---
title: '阿里云安全工程师发现了史诗级大bug，全球网络工程师周末都在为此加班'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/c28bab494748ce8e1d77321ff32dc849.jpg!custom'
author: 煎蛋
comments: false
date: Sat, 11 Dec 2021 16:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/c28bab494748ce8e1d77321ff32dc849.jpg!custom'
---

<div>   
<blockquote><p>CVE-2021-44228，也叫Log4Shell或LogJam；攻击者可借助它在服务器上执行任意代码</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/c28bab494748ce8e1d77321ff32dc849.jpg!custom" referrerpolicy="no-referrer"><p>阿里安全团队的成员发现了一个全世界最大的网络漏洞(前后5年最严重的？)。这一漏洞本身可导致严重后果，同时覆盖范围超广——如今所有提供互联网服务的企业都在组织人马加班加点修复它。<em>所以双十二还搞吗？</em></p>
<p>发现者的微博为 @m0d9_。虽然能直接找到当事人的说法，这很好，但总不能把人家微博直接复制过来吧，那有点不合适啊。所以还是找了篇汇总相关信息的博客译介过来。</p>
<p>多家信息安全新闻机构报道了在Apache Log4j库中发现的关键漏洞CVE-2021-44228(CVSS严重程度为10级)。数百万的Java应用程序使用这个库来记录错误信息。更糟糕的是，攻击者已经在积极利用这处漏洞。出于这个原因，Apache基金会建议所有开发人员将该库更新到2.15.0版本，如果无法做到这一点，请使用Apache Log4j安全漏洞页面中描述的方法之一。</p>
<p><strong>为什么CVE-2021-44228如此危险</strong></p>
<p><strong>CVE-2021-44228</strong>，也叫<strong>Log4Shell或LogJam</strong>，是一个远程代码执行(RCE)类漏洞。如果攻击者设法在其中一个服务器上利用它，他们就会获得执行任意代码的能力，并有可能完全控制该系统。</p>
<p>CVE-2021-44228特别危险的地方是容易被利用：即使是没有经验的黑客也可以利用这个漏洞成功执行攻击。根据研究人员的说法，攻击者只需要强迫应用程序只写一个字符串到日志中，之后由于消息查找替换功能，他们就可以将自己的代码上传到应用程序中。</p>
<p>通过CVE-2021-44228进行攻击的工作概念证明(PoC)已经在互联网上出现了。因此，网络安全公司已经在登记大规模的网络扫描，以寻找有漏洞的应用程序以及对蜜罐的攻击(蜜罐是用于欺骗攻击者的假饵)，这并不令人惊讶。</p>
<p>漏洞是由阿里巴巴云安全团队的陈兆军(不确定人家是否真是这名字)发现的。</p>
<p><strong>什么是Apache Log4J，为什么这个库如此受欢迎？</strong></p>
<p>Apache Log4j是Apache Logging项目的一部分。总的来说，使用这个库是记录错误的最简单方法之一，这也是大多数Java开发者使用它的原因。</p>
<p>许多大型软件公司和在线服务都使用Log4j库，包括Amazon、Apple iCloud、Cisco、Cloudflare、ElasticSearch、Red Hat、Steam、Tesla、Twitter，以及更多。由于该库如此受欢迎，一些信息安全研究人员预计未来几天对脆弱服务器的攻击会大幅增加。</p>
<p><strong>哪些版本的Log4j库是脆弱的，如何保护你的服务器免受攻击？</strong></p>
<p>几乎所有版本的Log4j都有漏洞，从2.0-beta9到2.14.1。最简单和有效的保护方法是安装最新版本的库，2.15.0。你可以在项目页面上下载它。</p>
<p>如果因为某些原因无法更新库，Apache基金会建议使用其中一种缓解方法。如果是2.10到2.14.1的Log4J版本，他们建议设置log4j2.formatMsgNoLookups系统属性，或者设置LOG4J_FORMAT_MSG_NO_LOOKUPS环境变量为true。</p>
<p>为了保护Log4j的早期版本(从2.0-beta9到2.10.0)，库的开发者建议从classpath中删除JndiLookup类： zip -q -d log4j-core - *. Jar org / apache / logging / log4j / core / lookup / JndiLookup .class。</p>
<p>此外，我们建议在你的服务器上安装安全解决方案 - 在许多情况下，这将使你能够检测到恶意代码的启动，并阻止攻击的发展。</p>
<blockquote class="wp-embedded-content" data-secret="TtaAOsoXNI"><p><a href="https://www.kaspersky.com/blog/log4shell-critical-vulnerability-in-apache-log4j/43124/">Critical vulnerability in Apache Log4j library</a></p></blockquote>
<p><iframe title="“Critical vulnerability in Apache Log4j library” — Daily - English - Global - blog.kaspersky.com" class="wp-embedded-content" sandbox="allow-scripts" security="restricted" style="position: absolute; clip: rect(1px, 1px, 1px, 1px);" src="https://www.kaspersky.com/blog/log4shell-critical-vulnerability-in-apache-log4j/43124/embed/#?secret=TtaAOsoXNI" data-secret="TtaAOsoXNI" width="500" height="282" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe></p>  
</div>
            