
---
title: 'Let’s Encrypt错误签发数百万张证书 所有错误证书将在5天内吊销'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0126/e9891fa724078af.png'
author: cnBeta
comments: false
date: Wed, 26 Jan 2022 14:21:13 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0126/e9891fa724078af.png'
---

<div>   
提醒：如果你使用Let’s Encrypt提供的免费SSL证书，请检查你提交申请时留的邮箱，如果邮箱收到来自Let’s Encrypt的通知则你的证书很可能会在未来5天内被吊销。<br>
 <p>如果你当时留的邮箱是随便填写的，那么基于稳妥考虑建议你重新申请并签发证书，确保旧证书不会被自动吊销。</p><p>吊销工作将从国际协调时2022年1月28日16:00开始(<strong>UTC +0，下同</strong>)，最迟会在5天内完成吊销，如果快的话那么最近签发的错误证书很可能很快就会被吊销。</p><p><a href="https://img.lancdn.com/landian/2020/03/70712.png"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0126/e9891fa724078af.png"><img data-original="https://static.cnbetacdn.com/article/2022/0126/e9891fa724078af.png" src="https://static.cnbetacdn.com/thumb/article/2022/0126/e9891fa724078af.png" referrerpolicy="no-referrer"></a></p><p><strong>吊销原因：</strong></p><p>根据Let’s Encrypt发布的公告，第三方仓库Boulder向ISRG(Let’s Encrypt的运营方)发出通知，该机构使用的ALPN TLS验证存在两个违规问题，因此ISRG必须对其TLS-APLN-01质询验证的工作方式进行更改。</p><p>Let’s Encrypt工程师称在2022年1月26日00:48部署修复程序时发现，所有通过TLS-APLN-01质询颁发和验证的证书都是错误的。根据Let’s Encrypt Certificate Policy政策要求，证书颁发机构需在5天内让错误证书失效，<strong>Let’s Encrypt计划从2022年1月28日16:00开始吊销错误证书</strong>。</p><p>但请注意，并非所有证书都受此问题影响，Let’s Encrypt仅会撤销受影响的错误证书，当前已经向相关用户发送邮件通知。</p><p>Let’s Encrypt预计少于1%的活跃证书受此问题影响，但考虑到Let’s Encrypt活跃证书超过2.21亿张，<strong>即便是1%也影响数百万张证书</strong>，这对应着数百万个网站和网络服务。一旦证书被吊销HTTPS将出现连接失败，也就是直接导致网站或服务无法连接。</p><p><strong>潜在处理方法：</strong></p><p>比较简单直接的处理方法就是直接删除旧的Let’s Encrypt证书然后重新申请签发新证书，由于修复程序已经被部署因此新签发的证书是木有问题的，这样解决比较简单有效。因为Let’s Encrypt没有提供方法来验证证书是否是错误的，所以如果用户没预留真实邮箱或未收到通知邮件不知道自己的证书是否受影响。</p><p>宝塔面板用户可在网站设置的SSL中，先关闭SSL功能，然后在证书夹中删除Let’s Encrypt证书，最后重新申请签发即可。</p><p>使用LNMP用户操作方法类似，先将网站配置文件(.conf)中的SSL证书码注释掉，然后将证书存放路径里的证书(.cer以及.key)删除，重启nginx使之生效，最后重新使用ACME或cerbot申请新证书即可。</p><p><strong>有关此问题的官方公告：</strong></p><p><a href="https://community.letsencrypt.org/t/2022-01-25-issue-with-tls-alpn-01-validation-method/170450">https://community.letsencrypt.org/t/2022-01-25-issue-with-tls-alpn-01-validation-method/170450</a></p>   
</div>
            