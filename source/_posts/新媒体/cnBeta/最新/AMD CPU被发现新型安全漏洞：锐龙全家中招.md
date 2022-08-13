
---
title: 'AMD CPU被发现新型安全漏洞：锐龙全家中招'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0813/9b8d073f4043cb8.png'
author: cnBeta
comments: false
date: Sat, 13 Aug 2022 12:14:26 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0813/9b8d073f4043cb8.png'
---

<div>   
如今的CPU处理器异常复杂，被发现安全漏洞也是平常事，以往发现的几次重要漏洞中AMD的锐龙处理器因为问世较晚，经常躲过一劫，Intel处理器才是重灾区，不过这一次发布的新漏洞没Intel什么事，AMD的三代锐龙都中招了。<br>
 <p>这个新型漏洞被命名为SQUIP，由?PIC Leak 漏洞研究团队及奥地利格拉茨科技大学的团队联合发现，<strong>它跟处理器的SMT多线程架构设计有关，AMD的Zen架构中每个执行单元都有自己的调度程序队列，</strong>就会被SQUIP影响，让黑客有机会进行侧信道进行攻击、提权。</p><p>根据研究团队的测试，<strong>这个漏洞可以让黑客在38分钟内攻破RSA-4096 密钥。</strong></p><p>这个漏洞主要在AMD处理器上发现，Intel的CPU使用了不同的架构，没有这个问题，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>的M1处理器架构类似AMD CPU，但不支持SMT多线程，因此也不受影响。</p><p>AMD将这个漏洞编号为MD-SB-1039，<strong>确认影响的处理器包括Zen1、Zen2及Zen3/3+架构处理器，</strong>也就是锐龙2000到锐龙6000在内的桌面版、移动版、服务器版，全家都中招了。</p><p><a href="https://img1.mydrivers.com/img/20220813/e035fe4b20224049aaa3be5eddbba24f.png" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0813/9b8d073f4043cb8.png"><img data-original="https://static.cnbetacdn.com/article/2022/0813/9b8d073f4043cb8.png" src="https://static.cnbetacdn.com/thumb/article/2022/0813/9b8d073f4043cb8.png" referrerpolicy="no-referrer"></a></p>   
</div>
            