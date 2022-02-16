
---
title: 'QuickSSH 1.0.0 版本发布，纯 Java 实现 SSH 协议'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2461'
author: 开源中国
comments: false
date: Tue, 15 Feb 2022 16:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2461'
---

<div>   
<div class="content">
                                                                                            <h1><span>QuickSSH</span></h1> 
<p><span>纯Java实现SSH协议</span></p> 
<h1><span>快速入门</span></h1> 
<ul> 
 <li><span>导入QuickSSH</span></li> 
</ul> 
<pre><code class="language-xml"><dependency>
  <groupId>cn.schoolwow</groupId>
  <artifactId>QuickSSH</artifactId>
  <version>&#123;最新版本&#125;</version>
</dependency></code></pre> 
<p> </p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsearch.maven.org%2Fsearch%3Fq%3Da%3AQuickSSH" target="_blank"><span>QuickSSH最新版本查询</span></a></p> 
<ul> 
 <li><span>构建SSHClient</span></li> 
</ul> 
<pre><code class="language-java">//密码方式登录
SSHClient client = QuickSSH.newInstance()
        .host("127.0.0.1")
        .port(22)
        .username("root")
        .password("123456")
        .build();
//公钥文件方式登录
SSHClient client = QuickSSH.newInstance()
        .host("127.0.0.1")
        .port(22)
        .username("root")
        //目前仅支持rsa类型
        .publickey("/path/to/id_rsa", "passphrase")
        .build();
//执行exec命令
String resut = sshClient.exec("pwd");
//获取sftp命令
SFTPChannel sftpChannel = sshClient.sftp();
sftpChannel.xxxxxx();</code></pre> 
<h1><span>开源协议</span></h1> 
<p><span>本软件使用</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.gnu.org%2Flicenses%2Flgpl-3.0-standalone.html" target="_blank"><span>LGPL</span></a><span>开源协议!</span></p> 
<p>QuickSSH项目是本人参考SSH协议相关RFC文件(包括RFC4250-4254)开发而来，整体项目组织结构和相关代码未借鉴任何项目。本人有参阅jsch项目和mina子项目sshd的相关代码思想，但未复制任何代码。</p> 
<p>本项目代码力求言简意赅，一方面是作为本人学习SSH协议的实践，另一方面也希望能够给想学习SSH协议的开发者提供帮助。希望我们国家的开源事业蓬勃发展，另一方面也希望大家能够多多专注于底层实现，夯实我们国家的科技硬基础。</p>
                                        </div>
                                      
</div>
            