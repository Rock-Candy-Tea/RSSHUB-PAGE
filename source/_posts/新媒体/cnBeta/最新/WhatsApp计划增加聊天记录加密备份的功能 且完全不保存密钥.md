
---
title: 'WhatsApp计划增加聊天记录加密备份的功能 且完全不保存密钥'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0911/3e0161edecdd4ad.webp'
author: cnBeta
comments: false
date: Sat, 11 Sep 2021 07:38:00 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0911/3e0161edecdd4ad.webp'
---

<div>   
<strong>WhatsApp周五宣布，将让其20多亿用户对他们的信息进行完全加密后的备份。</strong>WhatsApp在未来几周向iOS和Android用户推出之前，在一份白皮书中详细介绍了这一计划，目的是保护WhatsApp用户已经发送到Google Drive或苹果iCloud的备份，使其在没有加密密钥的情况下无法读取。<br>
 <p>选择加密备份的WhatsApp用户将被要求保存一个64位数的加密密钥，或创建一个与密钥绑定的密码。</p><p><img src="https://static.cnbetacdn.com/article/2021/0911/3e0161edecdd4ad.webp" title alt="Whatsapp_E2EE_Backups.webp" referrerpolicy="no-referrer"></p><p>Facebook首席执行官马克-扎克伯格（Mark Zuckerberg）在一份声明中说："WhatsApp是第一个提供端到端加密信息和备份的全球信息服务，要做到这一点是一个非常艰难的技术挑战，需要一个全新的框架来实现跨操作系统的密钥存储和云存储。"</p><p>如果有人创建了一个与其账户加密密钥绑定的密码，WhatsApp将把相关的密钥存储在一个物理硬件安全模块中，即HSM，该模块由Facebook维护，只有在WhatsApp中输入正确的密码时才能解锁。HSM就像一个加密和解密数字密钥的保险箱。</p><p>一旦用WhatsApp中的相关密码解锁，HSM就会提供加密密钥，反过来解密存储在<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>或Google服务器上的账户备份。如果反复尝试密码，存储在WhatsApp的HSM保险箱中的密钥将永久无法访问。硬件本身位于Facebook在世界各地拥有的数据中心，以防止互联网中断。</p><p><strong>"我们预计会因此受到一些人的批评"</strong></p><p>WhatsApp的负责人Will Cathcart表示，该系统旨在确保除了账户所有者之外，没有人能够获得备份的权限。他说，让人们创建更简单的密码的目的是为了使加密的备份更容易获得。WhatsApp将只知道HSM中存在一个密钥，而不知道密钥本身或解锁的相关密码。</p><p>WhatsApp的这一举措是在印度等世界各国政府--WhatsApp最大的市场--威胁要打破加密的工作方式时采取的。"我们预计会因此受到一些人的批评，"Cathcart说。"这对我们来说并不新鲜......。我坚信，政府应该推动我们拥有更多的安全性，而不是做相反的事情。"</p><p>WhatsApp的声明意味着该应用比苹果更进一步，苹果对iMessages进行了加密，但仍持有加密备份的钥匙；这意味着苹果可以协助恢复，但也可以迫使它将钥匙交给执法部门。Cathcart说，过去几年，WhatsApp一直在努力使加密备份成为现实，虽然一开始是选择加入，但他希望随着时间的推移，"这将成为所有人的工作方式"。</p>   
</div>
            