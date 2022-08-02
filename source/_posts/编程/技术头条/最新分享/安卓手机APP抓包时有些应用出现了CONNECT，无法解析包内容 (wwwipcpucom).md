
---
title: '安卓手机APP抓包时有些应用出现了CONNECT，无法解析包内容 (www.ipcpu.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=656'
author: 技术头条
comments: false
date: 2022-08-02 06:13:43
thumbnail: 'https://picsum.photos/400/300?random=656'
---

<div>   
我们在Charles启动了一个8888端口，并将该端口配置在手机的WIFI代理服务器上， 这样就可以抓到手机产生的对外数据包。 Charles是可以抓取HTTPS数据包的，但前提是需要打开HTTPS抓包选项，并安装Charlrs的root根证书。 

但是，我们全部配置完毕以后，发现手机的浏览器访问百度等网站的数据包是没有问题的，可以正确解析出来，有一部分APP软件也是可以解析的，比如物美多点，但是美团买菜就不行，拼多多也不行。
    
</div>
            