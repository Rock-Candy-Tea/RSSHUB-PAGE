
---
title: 'Lucky  - 基于Websocket,TCP,KCP的轻量级网络框架，支持protobuf，json消息协议'
categories: 
 - 编程
 - 码农俱乐部
 - 开源项目
headimg: 'https://picsum.photos/400/300?random=2920'
author: 码农俱乐部
comments: false
date: 2021-12-20 14:08:19
thumbnail: 'https://picsum.photos/400/300?random=2920'
---

<div>   
Lucky
介绍
它是一个应用于游戏，APP 的网络框架，支持 Protobuf，JSON 消息协议，基于 WebSocket 或者 socket(TCP,KCP)进行数据传输， 支持对消息包加密解密。
数据包加密方式： AES128,AES192,AES256 以及 Byte 轻量级混淆加密。
数据包读、写、执行逻辑处理分别在各自 goroutine 中， 可以对单个连接恶意发包进行限制，不会堵塞底层网络。
使用者只需注册消息和消息对应的回调函数，在回调中处理具体逻辑。例如：
Processor.Reg...
          
</div>
            