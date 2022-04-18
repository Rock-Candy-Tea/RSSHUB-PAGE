
---
title: '【安全公司：iCloud 用戶的MetaMask钱包遭遇钓鱼攻击是由于自身的安全意识不足】据官方消息，慢雾发布iCloud 用戶的MetaMask钱包遭遇钓鱼攻击简析，首先用户遭遇...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=4212'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=4212'
---

<div>   
【安全公司：iCloud 用戶的MetaMask钱包遭遇钓鱼攻击是由于自身的安全意识不足】据官方消息，慢雾发布iCloud 用戶的MetaMask钱包遭遇钓鱼攻击简析，首先用户遭遇了钓鱼攻击，是由于自身的安全意识不足，泄露了iCloud账号密码，用户应当承担大部分的责任。但是从钱包产品设计的角度上分析，MetaMask iOS App 端本身就存在有安全缺陷。 
MetaMask安卓端在AndroidManifest.xml中有android:allowBackup="false" 来禁止应用程序被用户和系统进行备份，从而避免备份的数据在其他设备上被恢复。 
MetaMask iOS端代码中没有发现存在这类禁止钱包数据(如 KeyStore 文件)被系统备份的机制。默认情况下iCloud会自动备份应用数据，当iCloud账号密码等权限信息被恶意攻击者获取，攻击者可以从目标 iCloud 里恢复 MetaMask iOS App 钱包的相关数据。 
慢雾安全团队经过实测通过 iCloud 恢复数据后再打开 MetaMask 钱包，还需要输入验证钱包的密码，如果密码的复杂度较低就会存在被破解的可能。  
</div>
            