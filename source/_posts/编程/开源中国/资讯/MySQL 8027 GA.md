
---
title: 'MySQL 8.0.27 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8468'
author: 开源中国
comments: false
date: Wed, 20 Oct 2021 07:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8468'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">时隔 3 个月，MySQL 的最新版本 8.0.27 于 2021 年 10 月 19 日正式 GA。这是 MySQL8.0 的一个维护版本，除了修复 207 个 Bug 之外，还增加了一些新功能：</span></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">多因素身份验证功能。MySQL支持对</span><span style="background-color:#ffffff; color:#333333">账户</span><span style="background-color:#ffffff; color:#333333">使用最多三种方法进行验证，可以在创建或者更改用户时启用该功能。命令行客户端可以使用--password1, --password2, --password3选项指定多个密码，用户可以利用该功能在关键操作上，使用多个用户密码同时进行验证，防止单一用户权限过大，或者误操作的现象发生。此外，企业版MySQL的该功能还支持使用智能卡、安全钥匙、生物识别读卡器进行验证，验证方法基于</span><span style="background-color:#ffffff; color:#333333">Fast Identity </span><span style="background-color:#ffffff; color:#333333">Online (FIDO)标准。</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">为了提高监视MySQL和故障排除的能力，Performance_Schema支持将度量线程名称（非mysqld）导出到操作系统，类似于Unix的ps执行效果。</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">引入了一个新的系统变量</span><span style="background-color:#ffffff; color:#333333">authentication_policy用以支持多因素身份验证功能，原有的变量</span><span style="background-color:#ffffff; color:#333333">default_authentication_plugin降级处理，未来将会删除。</span></li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>系统变量</span><span>g</span><span>roup_replication_components_stop_timeout用来指定在关闭组复制时，等待仍在进行的组件完成操作的时长。之前的默认值为</span><span>31536000（365天），无法起到应有的效果，新的默认值改为300秒。</span><span>组复制组件停止</span><span>5分钟后如果情况没有解决（仍有组件未完成操作），</span><span>允许成员重新启动并</span><span>重新加入。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">复制功能默认启用多线程复制，<span>一个多线程复制应用程序具有许多</span><span>并行执行事务的应用程序线</span><span>程。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">MySQL复制的异步连接故障转移机制支持副本使用组复制（单主模式），当主要成员发生故障时，其他组成员可以再次连接到发送者。换句话说，MySQL支持使用单主模式的组复制（主要成员用于接受日志）作为异步复制的副本，当主要成员发生故障时，其他成员可以再次连接到复制源。使用该功能可以配置两个复制组之间的异步复制，并支持连接故障转移。</p> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">稿源：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F7TI-2PnE1qe-M9h53wKYAg" target="_blank">https://mp.weixin.qq.com/s/7TI-2PnE1qe-M9h53wKYA</a></p>
                                        </div>
                                      
</div>
            