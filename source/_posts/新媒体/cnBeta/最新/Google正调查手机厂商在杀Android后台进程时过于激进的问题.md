
---
title: 'Google正调查手机厂商在杀Android后台进程时过于激进的问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0614/2d56f9c4824e057.jpg'
author: cnBeta
comments: false
date: Mon, 14 Jun 2021 03:26:10 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0614/2d56f9c4824e057.jpg'
---

<div>   
在过去的几年里，Google已经大大改善了Android系统处理后台应用程序的方式。Doze和App Standby Buckets等优化措施有助于将系统资源分配给最需要的应用程序，同时确保滥用的应用程序不会在后台肆意运行。<br>
 <p>在很长一段时间里Android用户批评iOS积极杀死在后台运行的应用程序的方式。Android<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>的多任务处理能力、更大的内存池和更大的电池被作为该平台优越性的例子四处宣扬。然而因为种种原因，一些制造商已经自行采取了更严格的措施，甚至可能违背了Google的政策，Google现在想知道这些OEM厂商是谁。<br></p><p><strong>调查表格：</strong></p><p><a href="https://docs.google.com/forms/d/e/1FAIpQLSd9P3gLKgMbVwQnAra6UhOjnCWtKpp55kYmigUKo8-ynmvdPg/viewform?resourcekey=0-e65sRbpisoGmtEe_zPZnMg" _src="https://docs.google.com/forms/d/e/1FAIpQLSd9P3gLKgMbVwQnAra6UhOjnCWtKpp55kYmigUKo8-ynmvdPg/viewform?resourcekey=0-e65sRbpisoGmtEe_zPZnMg" target="_blank">https://docs.google.com/forms/d/e/1FAIpQLSd9P3gLKgMbVwQnAra6UhOjnCWtKpp55kYmigUKo8-ynmvdPg/viewform?resourcekey=0-e65sRbpisoGmtEe_zPZnMg</a><br></p><p>大多数Android应用可能不需要总是在后台运行，但肯定有一类应用需要。事实上，有一类应用根本就不应该在后台运行，特别是那些意图不纯的应用，如恶意软件。然而，一些以健康为中心的应用程序可能需要一直运行，但系统可能不会总是让这些应用程序运行。</p><p>当然，后台应用程序虽然带来了不少便利，但也不是没有代价的，通常是在CPU占用和最终带来的电池续航表现缩短方面。这就是为什么包括Android在内的平台对哪些应用程序可以这样做以及何时这么做设定了规则和限制。Android系统也为例外情况留出了空间，并提供了支持应用程序进入睡眠状态并再次唤醒的方法。</p><p>另一方面，Google也为OEM厂商制定了规则，使其在后台杀应用程序进程的过程透明化，但这就是事情变得有点混乱的地方。一些原始设备制造商在Android系统的基础上实施他们自己的应用程序杀进程政策，但通常不会让开发者、更不会让用户知道这些。具体就会表现在一些应用程序，如睡眠监测或活动跟踪应用程序可以在一个手机上运行，在另一个品牌上可能无法正常工作，只是因为后者更积极地杀死了在后台运行的应用程序。</p><p>多年来，应用程序开发人员一直在抱怨这种情况，似乎Google终于听到了他们的请求。有人报告说某些品牌甚至扼杀了重要的Android可访问性辅助服务（这被视为照顾视障听障人士等弱势群体的操作系统基本功能）。早在2018年，AOSP错误跟踪器就创建了一个问题，详细说明了一部分OEM厂商是如何滥用Android的核心功能，禁止第三方应用程序在后台运行。这个问题充满了数百名应用开发者的回应，呼应了类似的经历，敦促Google阻止OEM厂商违反Android系统的合规性，实施如此激进的政策。</p><p><a href="https://static.cnbetacdn.com/article/2021/0614/2d56f9c4824e057.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0614/2d56f9c4824e057.jpg" title alt="dontkillmyapp.jpg" referrerpolicy="no-referrer"></a></p><p>2021年6月8日，一位用户评论说，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&aid=450&euid=&t=http%3A%2F%2Fwww.mi.com%2F" target="_blank">小米</a>和<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&aid=942&euid=&t=http%3A%2F%2Fwww.oneplus.com" target="_blank">一加</a>等OEM厂商甚至杀死了AccessibilityService。作为回应，一名Google员工最近评论说，他们将研究这个问题，并邀请应用程序开发人员提交他们的反馈。</p><p><strong>Google要求开发者提供以下细节：</strong></p><p>受影响的应用程序的名称</p><p>他们观察到问题的OEM和设备型号的名称</p><p>Android操作系统版本</p><p>重现该问题的步骤，以及预期结果和观察到的结果</p><p>受影响的API</p><p>他们是否能够在Pixel设备（或其他运行相同Android版本的设备）上重现相同的问题。</p><p>考虑到这种情况已经持续了多年，这项调查真的是姗姗来迟。正如他们所说，迟到总比不到好。Google甚至不需要亲自询问开发者，因为 "Don’t Kill My App"网站也已经存在多年了，想要从苦手机厂商者久矣的程序员中获得事实情况并不算困难。</p><p><strong>Android资料库中有关电源管理的章节：</strong></p><p><a href="https://developer.android.com/about/versions/pie/power" _src="https://developer.android.com/about/versions/pie/power" target="_blank">https://developer.android.com/about/versions/pie/power</a></p><p><strong>Android开发社区中投诉OEM厂商杀进程的错误跟踪页面：</strong><br></p><p><a href="https://issuetracker.google.com/issues/122098785?pli=1#comment155" _src="https://issuetracker.google.com/issues/122098785?pli=1#comment155" target="_blank">https://issuetracker.google.com/issues/122098785?pli=1#comment155</a><br></p>   
</div>
            