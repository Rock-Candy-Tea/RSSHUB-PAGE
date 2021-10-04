
---
title: 'go-mysql-transfer  - MySQL Binlog增量实时同步工具'
categories: 
 - 编程
 - 码农俱乐部
 - 开源项目
headimg: 'https://picsum.photos/400/300?random=2179'
author: 码农俱乐部
comments: false
date: 2021-10-04 05:07:45
thumbnail: 'https://picsum.photos/400/300?random=2179'
---

<div>   
简介
go-mysql-transfer 是使用 Go 语言实现的 MySQL 数据库实时增量同步工具。能够实时监听 MySQL 二进制日志(binlog)的变动，将变更内容形成指定格式的消息，发送到接收端。在数据库和接收端之间形成一个高性能、低延迟的增量数据(Binlog)同步管道。
特性
1、不依赖其它组件，一键部署
2、集成多种接收端，如：Redis、MongoDB、Elasticsearch、RabbitMQ、Kafka、RocketMQ，不需要再编写客户端，开箱即用
3、内置丰富的数据解析、消息生...
          
</div>
            